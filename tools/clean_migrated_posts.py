#!/usr/bin/env python3
"""Clean migrated Shopify post bodies while preserving YAML front matter.

Usage:
    python tools/clean_migrated_posts.py --dry-run
    python tools/clean_migrated_posts.py --write --backup
    python tools/clean_migrated_posts.py --path _posts/2024-02-04-is-openscan-an-open-source-project.md --write --backup

Dependency:
    pip install beautifulsoup4

Recommended workflow:
    git checkout -b chore/clean-migrated-posts
    python tools/clean_migrated_posts.py --dry-run
    python tools/clean_migrated_posts.py --write --backup
    git diff
    docker compose up --build
    # visually inspect the site
    git add _posts _drafts tools/clean_migrated_posts.py
    git commit -m "chore: clean migrated Shopify post markup"
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup
from bs4.element import NavigableString, PageElement, Tag


DEFAULT_PATTERNS = ("_posts/*.md", "_drafts/*.md")
PROTECTED_RE = re.compile(r"```.*?```|{{.*?}}|{%.*?%}", re.DOTALL)
BLANK_LINES_RE = re.compile(r"\n{3,}")
NOISY_ATTRS = {"class", "id", "data-mce-fragment", "data-pm-slice", "indentation", "textstyle", "level"}
COMPLEX_BLOCK_TAGS = {
    "audio",
    "figure",
    "figcaption",
    "iframe",
    "pre",
    "script",
    "style",
    "table",
    "video",
}
VOID_TAGS = {"br", "embed", "hr", "iframe", "img", "input", "source"}
INLINE_TAGS = {"a", "b", "br", "code", "em", "i", "img", "span", "strong", "u"}
ALLOWED_ATTRS = {
    "a": {"href"},
    "audio": {"autoplay", "controls", "loop", "muted", "preload", "src"},
    "iframe": {"allow", "allowfullscreen", "frameborder", "height", "src", "title", "width"},
    "img": {"alt", "height", "src", "width"},
    "ol": {"start"},
    "source": {"src", "srcset", "type"},
    "video": {"autoplay", "controls", "height", "loop", "muted", "playsinline", "poster", "preload", "src", "width"},
}


@dataclass
class Result:
    checked: int = 0
    changed: list[Path] = field(default_factory=list)
    skipped: list[Path] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def main() -> int:
    args = parse_args()
    if args.write and args.dry_run:
        print("Use either --dry-run or --write, not both.", file=sys.stderr)
        return 2

    paths = discover_paths(args.path)
    result = Result()

    for path in paths:
        result.checked += 1
        try:
            status = process_file(path, write=args.write, backup=args.backup)
        except Exception as exc:  # noqa: BLE001 - this is a migration helper; continue with other files.
            result.errors.append(f"{path}: {exc}")
            continue

        if status == "changed":
            result.changed.append(path)
            action = "updated" if args.write else "would update"
            print(f"{action}: {path}")
        elif status == "skipped":
            result.skipped.append(path)

    print_summary(result, write=args.write)
    return 1 if result.errors else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean noisy migrated Shopify HTML in Jekyll post bodies."
    )
    parser.add_argument("--dry-run", action="store_true", help="Show files that would change. This is the safe default.")
    parser.add_argument("--write", action="store_true", help="Write cleaned files. Without this flag, nothing is written.")
    parser.add_argument("--backup", action="store_true", help="Create a .bak file before overwriting a changed file.")
    parser.add_argument("--path", type=Path, help="Optional file or directory to process instead of _posts and _drafts.")
    return parser.parse_args()


def discover_paths(path: Path | None) -> list[Path]:
    if path is None:
        discovered: list[Path] = []
        for pattern in DEFAULT_PATTERNS:
            discovered.extend(Path(".").glob(pattern))
        return sorted(p for p in discovered if p.is_file())

    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.md") if p.is_file())
    raise FileNotFoundError(f"path does not exist: {path}")


def process_file(path: Path, *, write: bool, backup: bool) -> str:
    original = path.read_text(encoding="utf-8")
    split = split_front_matter(original)
    if split is None:
        return "skipped"

    front_matter, body = split
    cleaned_body = clean_body(body)
    cleaned = f"{front_matter.rstrip()}\n\n{cleaned_body}\n"

    if cleaned == original:
        return "unchanged"

    if write:
        if backup:
            backup_path = path.with_suffix(path.suffix + ".bak")
            if not backup_path.exists():
                backup_path.write_text(original, encoding="utf-8")
        path.write_text(cleaned, encoding="utf-8")

    return "changed"


def split_front_matter(content: str) -> tuple[str, str] | None:
    lines = content.splitlines(keepends=True)
    if not lines or not re.fullmatch(r"---[ \t]*\r?\n?", lines[0]):
        return None

    for index in range(1, len(lines)):
        if re.fullmatch(r"---[ \t]*\r?\n?", lines[index]):
            return "".join(lines[: index + 1]), "".join(lines[index + 1 :])
    return None


def clean_body(body: str) -> str:
    protected, placeholders = protect_fragments(body)
    soup = BeautifulSoup(protected, "html.parser")
    cleanup_tree(soup)
    rendered = render_nodes(soup.contents)
    restored = restore_fragments(rendered, placeholders)
    return normalize_body(restored)


def protect_fragments(text: str) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        placeholder = f"@@SHOPIFY_CLEAN_PROTECTED_{len(placeholders)}@@"
        placeholders[placeholder] = match.group(0)
        return placeholder

    return PROTECTED_RE.sub(replace, text), placeholders


def restore_fragments(text: str, placeholders: dict[str, str]) -> str:
    restored = text
    for placeholder, original in placeholders.items():
        restored = restored.replace(placeholder, original)
    return restored


def cleanup_tree(soup: BeautifulSoup) -> None:
    for tag in list(soup.find_all(True)):
        cleanup_attrs(tag)

    for span in list(soup.find_all("span")):
        if not span.attrs:
            span.unwrap()

    unwrap_paragraphs_around_single_complex_block(soup)

    for tag in reversed(list(soup.find_all(True))):
        if should_remove_empty_tag(tag):
            tag.decompose()


def cleanup_attrs(tag: Tag) -> None:
    allowed = ALLOWED_ATTRS.get(tag.name, set())
    for attr in list(tag.attrs):
        if attr == "dir" and tag.get(attr) not in {"rtl"}:
            del tag.attrs[attr]
            continue
        if attr == "dir":
            continue
        if attr in NOISY_ATTRS or attr.startswith("data-") or attr == "style" or attr == "rel" or attr == "target":
            del tag.attrs[attr]
            continue
        if allowed and attr in allowed:
            continue
        if not allowed:
            del tag.attrs[attr]
            continue
        del tag.attrs[attr]


def unwrap_paragraphs_around_single_complex_block(soup: BeautifulSoup) -> None:
    for paragraph in list(soup.find_all("p")):
        meaningful = meaningful_children(paragraph)
        if len(meaningful) == 1 and isinstance(meaningful[0], Tag) and meaningful[0].name in {"iframe", "video", "audio"}:
            paragraph.unwrap()


def meaningful_children(tag: Tag) -> list[PageElement]:
    return [
        child
        for child in tag.children
        if not (isinstance(child, NavigableString) and not str(child).strip())
    ]


def should_remove_empty_tag(tag: Tag) -> bool:
    if tag.name in VOID_TAGS or tag.name in {"script", "style", "td", "th"}:
        return False
    if tag.find(lambda child: isinstance(child, Tag) and child.name in VOID_TAGS):
        return False
    return not tag.get_text(strip=True)


def render_nodes(nodes: Iterable[PageElement]) -> str:
    blocks: list[str] = []
    pending_text: list[str] = []

    def flush_text() -> None:
        text = "".join(pending_text).strip()
        pending_text.clear()
        if text:
            blocks.append(text)

    for node in nodes:
        if isinstance(node, NavigableString):
            text = str(node)
            if text.strip():
                pending_text.append(text)
            continue

        if not isinstance(node, Tag):
            continue

        if is_inline_tag(node):
            pending_text.append(render_inline(node))
            continue

        flush_text()
        rendered = render_block(node).strip()
        if rendered:
            blocks.append(rendered)

    flush_text()
    return "\n\n".join(blocks)


def render_block(tag: Tag) -> str:
    name = tag.name or ""

    if re.fullmatch(r"h[1-6]", name):
        level = int(name[1])
        text = normalize_inline(render_inline_children(tag))
        return f"{'#' * level} {text}" if text else ""

    if name == "p":
        if contains_complex_block(tag):
            return render_html_block(tag)
        text = render_inline_children(tag).strip()
        return cleanup_inline_newlines(text)

    if name == "ul":
        return render_list(tag, ordered=False)

    if name == "ol":
        return render_list(tag, ordered=True)

    if name == "blockquote":
        return render_blockquote(tag)

    if name == "hr":
        return "---"

    if name == "div":
        if is_simple_container(tag):
            return render_nodes(tag.contents)
        return render_html_block(tag)

    if name in COMPLEX_BLOCK_TAGS:
        return render_html_block(tag)

    if is_inline_tag(tag):
        return render_inline(tag)

    if is_simple_container(tag):
        return render_nodes(tag.contents)

    return render_html_block(tag)


def render_list(tag: Tag, *, ordered: bool) -> str:
    start = 1
    if ordered:
        try:
            start = int(tag.get("start") or 1)
        except (TypeError, ValueError):
            start = 1

    lines: list[str] = []
    for index, item in enumerate(tag.find_all("li", recursive=False), start=start):
        content = render_list_item(item)
        if not content:
            continue
        marker = f"{index}." if ordered else "-"
        item_lines = content.splitlines()
        lines.append(f"{marker} {item_lines[0]}")
        indent = " " * (len(marker) + 1)
        for continuation in item_lines[1:]:
            lines.append(f"{indent}{continuation}" if continuation else "")
    return "\n".join(lines)


def render_list_item(item: Tag) -> str:
    if contains_complex_block(item) or has_block_children(item):
        rendered = render_nodes(item.contents).strip()
        return BLANK_LINES_RE.sub("\n", rendered)
    return cleanup_inline_newlines(render_inline_children(item)).strip()


def render_blockquote(tag: Tag) -> str:
    if contains_complex_block(tag):
        return render_html_block(tag)
    content = render_nodes(tag.contents).strip() or cleanup_inline_newlines(render_inline_children(tag)).strip()
    lines = content.splitlines()
    return "\n".join(f"> {line}" if line else ">" for line in lines)


def render_inline(node: PageElement) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    name = node.name or ""
    if name in {"strong", "b"}:
        text = render_inline_children(node).strip()
        return f"**{text}**" if text else ""
    if name in {"em", "i"}:
        text = render_inline_children(node).strip()
        return f"*{text}*" if text else ""
    if name == "a":
        href = str(node.get("href") or "").strip()
        text = render_inline_children(node).strip() or href
        return f"[{text}]({href})" if href else text
    if name == "img":
        if is_simple_image(node):
            alt = str(node.get("alt") or "")
            src = str(node.get("src") or "")
            return f"![{alt}]({src})"
        return render_html_block(node)
    if name == "br":
        return "  \n"
    if name == "code":
        return str(node)
    if name == "span":
        return render_inline_children(node)
    if name == "u":
        return render_inline_children(node)
    if name in INLINE_TAGS:
        return render_inline_children(node)
    return str(node)


def render_inline_children(tag: Tag) -> str:
    return "".join(render_inline(child) for child in tag.children)


def is_simple_image(tag: Tag) -> bool:
    return tag.name == "img" and bool(tag.get("src")) and set(tag.attrs).issubset({"src", "alt"})


def is_inline_tag(tag: Tag) -> bool:
    return tag.name in INLINE_TAGS


def contains_complex_block(tag: Tag) -> bool:
    for child in tag.descendants:
        if isinstance(child, Tag) and child.name in COMPLEX_BLOCK_TAGS:
            return True
    return False


def has_block_children(tag: Tag) -> bool:
    return any(isinstance(child, Tag) and not is_inline_tag(child) for child in tag.children)


def is_simple_container(tag: Tag) -> bool:
    if tag.attrs:
        return False
    return not any(
        isinstance(child, Tag) and child.name in {"table", "figure", "iframe", "video", "audio", "script", "style", "pre"}
        for child in tag.descendants
    )


def render_html_block(tag: Tag) -> str:
    return str(tag).strip()


def normalize_inline(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def cleanup_inline_newlines(text: str) -> str:
    lines = [re.sub(r"[ \t]+$", "", line) for line in text.splitlines()]
    cleaned = "\n".join(line.strip() if line.strip() else "" for line in lines)
    return cleaned.strip()


def normalize_body(text: str) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    normalized = "\n".join(lines)
    normalized = BLANK_LINES_RE.sub("\n\n", normalized)
    return normalized.strip()


def print_summary(result: Result, *, write: bool) -> None:
    mode = "write" if write else "dry-run"
    print("\nSummary")
    print(f"Mode: {mode}")
    print(f"Checked files: {result.checked}")
    print(f"Files with changes: {len(result.changed)}")
    print(f"Skipped files: {len(result.skipped)}")
    print(f"Errors: {len(result.errors)}")

    if result.changed:
        print("Changed files:")
        for path in result.changed:
            print(f"- {path}")

    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"- {error}")


if __name__ == "__main__":
    raise SystemExit(main())
