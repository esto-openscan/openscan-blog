#!/usr/bin/env python3
"""One-off Shopify blog migration to Jekyll Chirpy.

Required packages:
    pip install requests beautifulsoup4

Configuration:
    SHOPIFY_SHOP=your-shop.myshopify.com  # or your-shop
    SHOPIFY_ADMIN_TOKEN=...              # preferred when available
    SHOPIFY_CLIENT_ID=...                # fallback with SHOPIFY_CLIENT_SECRET
    SHOPIFY_CLIENT_SECRET=...
    SHOPIFY_API_VERSION=2026-01
    OUTPUT_DIR=.

The script only reads from the Shopify Admin REST API. It writes posts,
downloaded assets, a redirect CSV, and a raw JSON backup to OUTPUT_DIR.
The only non-GET request to Shopify is the optional OAuth client credentials
token exchange at /admin/oauth/access_token.
Unpublished Shopify articles are exported to _drafts by default.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import posixpath
import re
import sys
import time
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, unquote, urlparse

import requests
from bs4 import BeautifulSoup


ASSET_EXTENSIONS = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".svg",
    ".webp",
    ".zip",
}
IMAGE_EXTENSIONS = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
DOWNLOAD_HOSTS = {
    "cdn.shopify.com",
    "openscan.eu",
    "www.openscan.eu",
}
STYLE_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
HTML_SPLIT_RE = re.compile(r"<[^>]+>|&[a-zA-Z0-9#]+;|\s+")


@dataclass
class Config:
    shop: str
    token: str | None
    client_id: str | None
    client_secret: str | None
    version: str
    output_dir: Path
    export_drafts: bool
    dry_run: bool
    overwrite: bool
    timeout: float
    max_retries: int
    retry_backoff: float


@dataclass
class MigrationStats:
    blogs: int = 0
    articles: int = 0
    exported_posts: int = 0
    exported_drafts: int = 0
    downloaded_images: int = 0
    downloaded_files: int = 0
    failed_downloads: int = 0
    skipped_unpublished: int = 0
    skipped_existing: int = 0
    problematic_articles: list[str] = field(default_factory=list)


class ShopifyClient:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": "openscan-shopify-jekyll-migration/1.0",
            }
        )
        self.base_url = f"https://{config.shop}/admin/api/{config.version}"
        self.cached_token = config.token
        self.token_expires_at = 0.0

    def get(self, path_or_url: str, params: dict[str, Any] | None = None) -> requests.Response:
        url = path_or_url if path_or_url.startswith("http") else f"{self.base_url}{path_or_url}"
        last_error: Exception | None = None
        for attempt in range(self.config.max_retries + 1):
            try:
                self.session.headers["X-Shopify-Access-Token"] = self.access_token()
                response = self.session.get(url, params=params, timeout=self.config.timeout)
            except requests.RequestException as exc:
                last_error = exc
                self._sleep_before_retry(attempt, None)
                continue

            if response.status_code == 429 or 500 <= response.status_code < 600:
                if attempt < self.config.max_retries:
                    self._sleep_before_retry(attempt, response)
                    continue
            response.raise_for_status()
            return response

        if last_error:
            raise RuntimeError(f"Request failed after retries: {url}") from last_error
        raise RuntimeError(f"Request failed after retries: {url}")

    def access_token(self) -> str:
        if self.config.token:
            return self.config.token
        if self.cached_token and time.time() < self.token_expires_at:
            return self.cached_token
        return self.fetch_client_credentials_token()

    def fetch_client_credentials_token(self) -> str:
        if not self.config.client_id or not self.config.client_secret:
            raise RuntimeError("Missing Shopify credentials")

        token_url = f"https://{self.config.shop}/admin/oauth/access_token"
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
        }

        try:
            self.session.headers.pop("X-Shopify-Access-Token", None)
            response = self.session.post(token_url, headers=headers, data=data, timeout=self.config.timeout)
        except requests.RequestException as exc:
            raise RuntimeError(f"Shopify token request failed: {exc}") from exc

        if response.status_code >= 400:
            body = truncate_text(redact_sensitive(response.text, self.config), 500)
            raise RuntimeError(f"Shopify token request failed with HTTP {response.status_code}: {body}")

        try:
            payload = response.json()
        except json.JSONDecodeError as exc:
            body = truncate_text(redact_sensitive(response.text, self.config), 500)
            raise RuntimeError(f"Shopify token response was not valid JSON: {body}") from exc

        access_token = str(payload.get("access_token") or "")
        if not access_token:
            body = truncate_text(redact_sensitive(response.text, self.config), 500)
            raise RuntimeError(f"Shopify token response did not contain access_token: {body}")

        try:
            expires_in = int(payload.get("expires_in") or 0)
        except (TypeError, ValueError):
            expires_in = 0

        self.cached_token = access_token
        if expires_in > 0:
            self.token_expires_at = time.time() + max(expires_in - 60, 1)
        else:
            self.token_expires_at = time.time() + 300
        return access_token

    def get_paginated(self, path: str, collection_key: str, params: dict[str, Any]) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        next_url: str | None = None
        next_params: dict[str, Any] | None = dict(params)

        while True:
            response = self.get(next_url or path, params=next_params)
            payload = response.json()
            items.extend(payload.get(collection_key, []))
            next_url = parse_next_link(response.headers.get("Link"))
            next_params = None
            if not next_url:
                return items

    def _sleep_before_retry(self, attempt: int, response: requests.Response | None) -> None:
        if attempt >= self.config.max_retries:
            return

        retry_after = response.headers.get("Retry-After") if response is not None else None
        delay = parse_retry_after(retry_after)
        if delay is None:
            delay = self.config.retry_backoff * (2**attempt)
        time.sleep(delay)


def main() -> int:
    args = parse_args()
    try:
        config = load_config(args)
    except ValueError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2

    ensure_dependencies_available()

    client = ShopifyClient(config)
    stats = MigrationStats()
    raw_backup: dict[str, Any] = {"blogs": [], "articles_by_blog": {}}
    redirects: list[dict[str, str]] = []
    used_post_slugs: set[str] = set()
    used_draft_slugs: set[str] = set()

    try:
        blogs = client.get_paginated("/blogs.json", "blogs", {})
    except Exception as exc:
        print(f"Failed to fetch blogs: {exc}", file=sys.stderr)
        return 1

    stats.blogs = len(blogs)
    raw_backup["blogs"] = blogs

    for blog in blogs:
        blog_id = str(blog.get("id"))
        blog_title = clean_text(str(blog.get("title") or "Blog"))
        print(f"Fetching articles for blog {blog_id} ({blog_title})")
        try:
            article_params: dict[str, Any] = {"limit": 250}
            if config.export_drafts:
                article_params["published_status"] = "any"
            articles = client.get_paginated(f"/blogs/{blog_id}/articles.json", "articles", article_params)
        except Exception as exc:
            stats.problematic_articles.append(f"blog {blog_id}: failed to fetch articles: {exc}")
            continue

        raw_backup["articles_by_blog"][blog_id] = articles
        stats.articles += len(articles)

        for article in articles:
            try:
                migrate_article(
                    config=config,
                    blog=blog,
                    article=article,
                    stats=stats,
                    redirects=redirects,
                    used_post_slugs=used_post_slugs,
                    used_draft_slugs=used_draft_slugs,
                )
            except Exception as exc:
                ident = article_identifier(article)
                stats.problematic_articles.append(f"{ident}: {exc}")

    exit_code = 0
    try:
        write_raw_backup(config, raw_backup)
        write_redirects(config, redirects)
    except Exception as exc:
        exit_code = 1
        stats.problematic_articles.append(f"migration artifact write failed: {exc}")
    print_summary(stats)
    return exit_code


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Migrate Shopify blog articles to Jekyll/Chirpy Markdown files."
    )
    parser.add_argument(
        "--export-drafts",
        action="store_true",
        help="Export unpublished articles to _drafts/slug.md. This is the default.",
    )
    parser.add_argument(
        "--no-export-drafts",
        dest="export_drafts",
        action="store_false",
        help="Skip unpublished articles instead of exporting them to _drafts.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and process data without writing files or downloading assets.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacing existing Markdown, asset, CSV, and raw backup files.",
    )
    parser.add_argument("--timeout", type=float, default=30.0, help="HTTP request timeout in seconds.")
    parser.add_argument("--max-retries", type=int, default=5, help="Retries for 429 and 5xx responses.")
    parser.add_argument("--retry-backoff", type=float, default=2.0, help="Base seconds for exponential retry.")
    parser.set_defaults(export_drafts=True)
    return parser.parse_args()


def load_config(args: argparse.Namespace) -> Config:
    shop = os.environ.get("SHOPIFY_SHOP", "").strip()
    token = os.environ.get("SHOPIFY_ADMIN_TOKEN", "").strip()
    client_id = os.environ.get("SHOPIFY_CLIENT_ID", "").strip()
    client_secret = os.environ.get("SHOPIFY_CLIENT_SECRET", "").strip()
    version = os.environ.get("SHOPIFY_API_VERSION", "2026-01").strip()
    output_dir = Path(os.environ.get("OUTPUT_DIR", ".")).expanduser().resolve()

    if not shop:
        raise ValueError("SHOPIFY_SHOP is required, for example your-shop.myshopify.com or your-shop")
    if not token and not (client_id and client_secret):
        raise ValueError(
            "Set SHOPIFY_ADMIN_TOKEN, or set both SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET "
            "for the Shopify client credentials grant"
        )
    shop = normalize_shop_domain(shop)
    if not version:
        raise ValueError("SHOPIFY_API_VERSION must not be empty")

    return Config(
        shop=shop,
        token=token or None,
        client_id=client_id or None,
        client_secret=client_secret or None,
        version=version,
        output_dir=output_dir,
        export_drafts=args.export_drafts,
        dry_run=args.dry_run,
        overwrite=args.overwrite,
        timeout=args.timeout,
        max_retries=args.max_retries,
        retry_backoff=args.retry_backoff,
    )


def ensure_dependencies_available() -> None:
    # Imports above already validate dependencies; this keeps the failure message near startup.
    return None


def normalize_shop_domain(shop: str) -> str:
    if shop.startswith("http://") or shop.startswith("https://"):
        shop = urlparse(shop).netloc
    shop = shop.strip().strip("/")
    if "." not in shop:
        return f"{shop}.myshopify.com"
    return shop


def migrate_article(
    *,
    config: Config,
    blog: dict[str, Any],
    article: dict[str, Any],
    stats: MigrationStats,
    redirects: list[dict[str, str]],
    used_post_slugs: set[str],
    used_draft_slugs: set[str],
) -> None:
    title = clean_text(str(article.get("title") or "untitled"))
    published_at = article.get("published_at")
    is_published = bool(published_at)

    if not is_published and not config.export_drafts:
        stats.skipped_unpublished += 1
        return

    date = parse_shopify_datetime(published_at or article.get("created_at") or article.get("updated_at"))
    date_prefix = date.strftime("%Y-%m-%d")
    base_slug = slugify(str(article.get("handle") or title or article.get("id") or "article"))

    if is_published:
        slug = unique_slug(base_slug, used_post_slugs)
        markdown_rel = Path("_posts") / f"{date_prefix}-{slug}.md"
        asset_key = f"{date_prefix}-{slug}"
        new_path = f"/posts/{slug}/"
    else:
        slug = unique_slug(base_slug, used_draft_slugs)
        markdown_rel = Path("_drafts") / f"{slug}.md"
        asset_key = slug
        new_path = "/" + markdown_rel.as_posix()

    markdown_path = config.output_dir / markdown_rel
    if markdown_path.exists() and not config.overwrite:
        stats.skipped_existing += 1
        stats.problematic_articles.append(
            f"{article_identifier(article)}: target exists and --overwrite was not set: {markdown_rel}"
        )
        return

    soup = BeautifulSoup(article.get("body_html") or "", "html.parser")
    cover_url = get_cover_url(article)

    image_base_rel = Path("assets") / "img" / "posts" / asset_key
    file_base_rel = Path("assets") / "files" / "posts" / asset_key
    downloader = AssetDownloader(config=config, stats=stats)
    rewrite_assets(
        soup=soup,
        config=config,
        downloader=downloader,
        image_base_rel=image_base_rel,
        file_base_rel=file_base_rel,
    )

    local_cover_path = ""
    if cover_url and should_download_url(cover_url):
        try:
            local_cover_path = downloader.download(
                cover_url,
                image_base_rel if is_image_url(cover_url) else file_base_rel,
                prefer_image=True,
            )
        except Exception as exc:
            stats.failed_downloads += 1
            stats.problematic_articles.append(f"{article_identifier(article)}: cover download failed: {exc}")

    old_url = shopify_article_url(config.shop, blog, article)
    front_matter = build_front_matter(
        title=title,
        date=date,
        author=clean_text(str(article.get("author") or "")),
        description=summary_description(article),
        summary_html=str(article.get("summary_html") or ""),
        categories=categories_for_article(blog),
        tags=tags_for_article(article),
        image_path=local_cover_path,
        redirect_from=old_url,
    )
    markdown_body = f"---\n{front_matter}---\n\n{soup.decode(formatter='html')}\n"

    redirects.append(
        {
            "old_url": old_url,
            "new_path": new_path,
            "title": title,
            "published_at": str(published_at or ""),
        }
    )

    if config.dry_run:
        print(f"[dry-run] Would write {markdown_rel}")
        if is_published:
            stats.exported_posts += 1
        else:
            stats.exported_drafts += 1
        return

    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(markdown_body, encoding="utf-8")
    if is_published:
        stats.exported_posts += 1
    else:
        stats.exported_drafts += 1


class AssetDownloader:
    def __init__(self, *, config: Config, stats: MigrationStats) -> None:
        self.config = config
        self.stats = stats
        self.session = requests.Session()
        self.downloaded: dict[str, str] = {}
        self.used_paths: set[Path] = set()

    def download(self, url: str, base_rel: Path, *, prefer_image: bool = False) -> str:
        normalized_url = normalize_asset_url(url)
        if normalized_url in self.downloaded:
            return self.downloaded[normalized_url]

        rel_path = self._target_path(normalized_url, base_rel)
        abs_path = self.config.output_dir / rel_path
        jekyll_path = "/" + rel_path.as_posix()

        if self.config.dry_run:
            print(f"[dry-run] Would download {normalized_url} -> {rel_path}")
            self._increment_download_stat(prefer_image or is_image_url(normalized_url))
            self.downloaded[normalized_url] = jekyll_path
            return jekyll_path

        if abs_path.exists() and not self.config.overwrite:
            raise FileExistsError(f"asset exists and --overwrite was not set: {rel_path}")

        response = self._get(normalized_url)
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_bytes(response.content)
        self._increment_download_stat(prefer_image or is_image_url(normalized_url))
        self.downloaded[normalized_url] = jekyll_path
        return jekyll_path

    def _get(self, url: str) -> requests.Response:
        last_error: Exception | None = None
        for attempt in range(self.config.max_retries + 1):
            try:
                response = self.session.get(url, timeout=self.config.timeout)
            except requests.RequestException as exc:
                last_error = exc
                self._sleep_before_retry(attempt, None)
                continue

            if response.status_code == 429 or 500 <= response.status_code < 600:
                if attempt < self.config.max_retries:
                    self._sleep_before_retry(attempt, response)
                    continue
            response.raise_for_status()
            return response

        if last_error:
            raise RuntimeError(f"download failed after retries: {url}") from last_error
        raise RuntimeError(f"download failed after retries: {url}")

    def _sleep_before_retry(self, attempt: int, response: requests.Response | None) -> None:
        if attempt >= self.config.max_retries:
            return
        retry_after = response.headers.get("Retry-After") if response is not None else None
        delay = parse_retry_after(retry_after)
        if delay is None:
            delay = self.config.retry_backoff * (2**attempt)
        time.sleep(delay)

    def _target_path(self, url: str, base_rel: Path) -> Path:
        parsed = urlparse(url)
        filename = safe_asset_filename(parsed)
        candidate = base_rel / filename
        suffix_counter = 2
        while candidate in self.used_paths:
            candidate = base_rel / f"{Path(filename).stem}-{suffix_counter}{Path(filename).suffix}"
            suffix_counter += 1
        self.used_paths.add(candidate)
        return candidate

    def _increment_download_stat(self, is_image: bool) -> None:
        if is_image:
            self.stats.downloaded_images += 1
        else:
            self.stats.downloaded_files += 1


def rewrite_assets(
    *,
    soup: BeautifulSoup,
    config: Config,
    downloader: AssetDownloader,
    image_base_rel: Path,
    file_base_rel: Path,
) -> None:
    for img in soup.find_all("img"):
        src = img.get("src")
        data_src = img.get("data-src")
        srcset = img.get("srcset")
        chosen_url = src or data_src

        if srcset:
            local = download_largest_srcset(downloader, srcset, image_base_rel, img)
            if local:
                img["src"] = local
            if img.has_attr("srcset"):
                del img["srcset"]
            if img.has_attr("data-src"):
                del img["data-src"]
        elif chosen_url and should_download_url(chosen_url):
            local = try_download_asset(downloader, chosen_url, image_base_rel, img, "image")
            if local:
                img["src"] = local
                if img.has_attr("data-src"):
                    del img["data-src"]

        rewrite_style_urls(img, downloader, image_base_rel, file_base_rel)

    for source in soup.find_all("source"):
        srcset = source.get("srcset")
        if srcset:
            local = download_largest_srcset(downloader, srcset, image_base_rel, source)
            if local:
                source["srcset"] = local
            else:
                del source["srcset"]
        rewrite_style_urls(source, downloader, image_base_rel, file_base_rel)

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and is_downloadable_asset(href) and should_download_url(href):
            local = try_download_asset(
                downloader,
                href,
                image_base_rel if is_image_url(href) else file_base_rel,
                link,
                "linked asset",
            )
            if local:
                link["href"] = local
        rewrite_style_urls(link, downloader, image_base_rel, file_base_rel)

    for tag in soup.find_all(style=True):
        rewrite_style_urls(tag, downloader, image_base_rel, file_base_rel)


def try_download_asset(
    downloader: AssetDownloader,
    url: str,
    base_rel: Path,
    tag: Any,
    label: str,
) -> str:
    try:
        return downloader.download(url, base_rel, prefer_image=base_rel.parts[:2] == ("assets", "img"))
    except Exception as exc:
        downloader.stats.failed_downloads += 1
        downloader.stats.problematic_articles.append(f"{label} download failed for {url}: {exc}")
        tag["data-migration-download-error"] = str(exc)
        return ""


def download_largest_srcset(
    downloader: AssetDownloader,
    srcset: str,
    image_base_rel: Path,
    tag: Any,
) -> str:
    candidates = parse_srcset(srcset)
    for candidate_url, _descriptor in sorted(candidates, key=lambda item: srcset_descriptor_weight(item[1]), reverse=True):
        if should_download_url(candidate_url):
            return try_download_asset(downloader, candidate_url, image_base_rel, tag, "srcset image")
    return ""


def rewrite_style_urls(tag: Any, downloader: AssetDownloader, image_base_rel: Path, file_base_rel: Path) -> None:
    style = tag.get("style")
    if not style:
        return

    def replace(match: re.Match[str]) -> str:
        original = match.group(2).strip()
        if not original or original.startswith(("data:", "#")):
            return match.group(0)
        if not should_download_url(original):
            return match.group(0)
        base_rel = image_base_rel if is_image_url(original) else file_base_rel
        local = try_download_asset(downloader, original, base_rel, tag, "style asset")
        return f"url('{local}')" if local else match.group(0)

    tag["style"] = STYLE_URL_RE.sub(replace, style)


def parse_srcset(srcset: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    for part in srcset.split(","):
        tokens = part.strip().split()
        if not tokens:
            continue
        candidates.append((tokens[0], tokens[1] if len(tokens) > 1 else ""))
    return candidates


def srcset_descriptor_weight(descriptor: str) -> float:
    descriptor = descriptor.strip().lower()
    if descriptor.endswith("w"):
        return float(descriptor[:-1] or 0)
    if descriptor.endswith("x"):
        return float(descriptor[:-1] or 0) * 10000
    return 1


def parse_next_link(link_header: str | None) -> str | None:
    if not link_header:
        return None
    for part in link_header.split(","):
        section = part.strip()
        if 'rel="next"' not in section:
            continue
        match = re.search(r"<([^>]+)>", section)
        if match:
            return match.group(1)
    return None


def parse_retry_after(value: str | None) -> float | None:
    if not value:
        return None
    try:
        return max(float(value), 0.0)
    except ValueError:
        try:
            retry_at = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        if retry_at.tzinfo is None:
            retry_at = retry_at.replace(tzinfo=timezone.utc)
        return max((retry_at - datetime.now(timezone.utc)).total_seconds(), 0.0)


def parse_shopify_datetime(value: Any) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    text = str(value).strip()
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return datetime.now(timezone.utc)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def build_front_matter(
    *,
    title: str,
    date: datetime,
    author: str,
    description: str,
    summary_html: str,
    categories: list[str],
    tags: list[str],
    image_path: str,
    redirect_from: str,
) -> str:
    lines = [
        f"title: {yaml_scalar(title)}",
        f"date: {yaml_scalar(date.isoformat())}",
    ]
    if author:
        lines.append(f"author: {yaml_scalar(author)}")
    if description:
        lines.append(f"description: {yaml_scalar(description)}")
    if summary_html:
        lines.append("shopify_summary_html: |-")
        lines.extend(yaml_block_lines(summary_html))
    lines.append("categories:")
    for category in categories:
        lines.append(f"  - {yaml_scalar(category)}")
    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {yaml_scalar(tag)}")
    else:
        lines.append("tags: []")
    if image_path:
        lines.append("image:")
        lines.append(f"  path: {yaml_scalar(image_path)}")
    lines.append("redirect_from:")
    lines.append(f"  - {yaml_scalar(absolute_path_from_url(redirect_from))}")
    lines.append(f"  - {yaml_scalar(redirect_from)}")
    return "\n".join(lines) + "\n"


def yaml_scalar(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_block_lines(value: str) -> list[str]:
    lines = value.splitlines() or [""]
    return [f"  {line}" if line else "  " for line in lines]


def summary_description(article: dict[str, Any]) -> str:
    summary_html = str(article.get("summary_html") or "")
    if not summary_html:
        return ""
    text = clean_text(BeautifulSoup(summary_html, "html.parser").get_text(" "))
    return truncate_text(text, 320)


def categories_for_article(blog: dict[str, Any]) -> list[str]:
    title = clean_text(str(blog.get("title") or "Blog"))
    return [title] if title else ["Blog"]


def tags_for_article(article: dict[str, Any]) -> list[str]:
    raw_tags = article.get("tags") or ""
    if isinstance(raw_tags, list):
        tags = raw_tags
    else:
        tags = [tag.strip() for tag in str(raw_tags).split(",")]
    return [clean_text(tag) for tag in tags if clean_text(tag)]


def get_cover_url(article: dict[str, Any]) -> str:
    image = article.get("image") or {}
    if isinstance(image, dict):
        return str(image.get("src") or "")
    return ""


def shopify_article_url(shop: str, blog: dict[str, Any], article: dict[str, Any]) -> str:
    blog_handle = str(blog.get("handle") or slugify(str(blog.get("title") or "blog")))
    article_handle = str(article.get("handle") or slugify(str(article.get("title") or article.get("id") or "article")))
    public_host = "openscan.eu" if "openscan" in shop else shop
    return f"https://{public_host}/blogs/{quote(blog_handle)}/{quote(article_handle)}"


def absolute_path_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if parsed.query:
        path = f"{path}?{parsed.query}"
    return path


def should_download_url(url: str) -> bool:
    normalized = normalize_asset_url(url)
    parsed = urlparse(normalized)
    return parsed.scheme in {"http", "https"} and parsed.netloc.lower() in DOWNLOAD_HOSTS


def is_downloadable_asset(url: str) -> bool:
    return asset_extension(url) in ASSET_EXTENSIONS


def is_image_url(url: str) -> bool:
    return asset_extension(url) in IMAGE_EXTENSIONS


def asset_extension(url: str) -> str:
    parsed = urlparse(normalize_asset_url(url))
    path = unquote(parsed.path)
    return Path(path).suffix.lower()


def normalize_asset_url(url: str) -> str:
    value = str(url).strip()
    if value.startswith("//"):
        return f"https:{value}"
    return value


def safe_asset_filename(parsed_url: Any) -> str:
    path = unquote(parsed_url.path)
    name = posixpath.basename(path.rstrip("/")) or "asset"
    stem = slugify(Path(name).stem) or "asset"
    suffix = Path(name).suffix.lower()
    if not suffix:
        query_ext = extension_from_query(parsed_url.query)
        suffix = query_ext or ".bin"
    return f"{stem}{suffix}"


def extension_from_query(query: str) -> str:
    values = parse_qs(query)
    for key in ("format", "fm", "ext"):
        if key in values and values[key]:
            ext = values[key][0].strip().lower().lstrip(".")
            if re.fullmatch(r"[a-z0-9]{2,5}", ext):
                return f".{ext}"
    return ""


def slugify(value: str) -> str:
    value = transliterate_german(value)
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug or "untitled"


def transliterate_german(value: str) -> str:
    replacements = {
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ẞ": "SS",
        "ß": "ss",
    }
    return "".join(replacements.get(char, char) for char in value)


def unique_slug(base_slug: str, used_slugs: set[str]) -> str:
    slug = base_slug
    counter = 2
    while slug in used_slugs:
        slug = f"{base_slug}-{counter}"
        counter += 1
    used_slugs.add(slug)
    return slug


def clean_text(value: str) -> str:
    without_html = HTML_SPLIT_RE.sub(" ", value)
    return re.sub(r"\s+", " ", without_html).strip()


def truncate_text(value: str, max_length: int) -> str:
    if len(value) <= max_length:
        return value
    return f"{value[:max_length]}..."


def redact_sensitive(value: str, config: Config) -> str:
    redacted = value
    for secret in (config.token, config.client_secret):
        if secret:
            redacted = redacted.replace(secret, "[redacted]")
    redacted = re.sub(r'("access_token"\s*:\s*")[^"]+(")', r"\1[redacted]\2", redacted)
    redacted = re.sub(r'("client_secret"\s*:\s*")[^"]+(")', r"\1[redacted]\2", redacted)
    redacted = re.sub(r"((?:access_token|client_secret)=)[^&\s]+", r"\1[redacted]", redacted)
    return redacted


def write_raw_backup(config: Config, payload: dict[str, Any]) -> None:
    path = config.output_dir / "migration_raw" / "shopify_articles.json"
    if config.dry_run:
        print(f"[dry-run] Would write {path.relative_to(config.output_dir)}")
        return
    if path.exists() and not config.overwrite:
        raise FileExistsError(f"raw backup exists and --overwrite was not set: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_redirects(config: Config, redirects: list[dict[str, str]]) -> None:
    path = config.output_dir / "migration_redirects.csv"
    if config.dry_run:
        print(f"[dry-run] Would write {path.relative_to(config.output_dir)}")
        return
    if path.exists() and not config.overwrite:
        raise FileExistsError(f"redirect CSV exists and --overwrite was not set: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["old_url", "new_path", "title", "published_at"])
        writer.writeheader()
        writer.writerows(redirects)


def print_summary(stats: MigrationStats) -> None:
    print("\nMigration summary")
    print(f"Blogs: {stats.blogs}")
    print(f"Articles: {stats.articles}")
    print(f"Exported posts: {stats.exported_posts}")
    print(f"Exported drafts: {stats.exported_drafts}")
    print(f"Skipped unpublished: {stats.skipped_unpublished}")
    print(f"Skipped existing files: {stats.skipped_existing}")
    print(f"Downloaded images: {stats.downloaded_images}")
    print(f"Downloaded files: {stats.downloaded_files}")
    print(f"Failed downloads: {stats.failed_downloads}")
    if stats.problematic_articles:
        print("Problematic articles:")
        for item in stats.problematic_articles:
            print(f"- {item}")
    else:
        print("Problematic articles: none")


def article_identifier(article: dict[str, Any]) -> str:
    title = clean_text(str(article.get("title") or "untitled"))
    article_id = article.get("id") or "unknown-id"
    return f"article {article_id} ({title})"


if __name__ == "__main__":
    raise SystemExit(main())
