# OpenScan Blog Tools

This directory contains one-off migration and maintenance helpers for the
OpenScan blog.

## Shopify Blog Migration

The Shopify-to-Jekyll migration script lives at
[`shopify_to_jekyll.py`](shopify_to_jekyll.py). It reads Shopify blog content
from the Admin REST API, downloads referenced assets, writes Jekyll posts, and
creates migration artifacts.

Install the Python dependencies in a local environment:

```shell
pip install requests beautifulsoup4
```

Use an existing Admin API access token:

```shell
export SHOPIFY_SHOP="your-shop.myshopify.com"
export SHOPIFY_ADMIN_TOKEN="..."
python3 tools/shopify_to_jekyll.py --dry-run
```

Or use the Shopify Dev Dashboard client credentials flow:

```shell
export SHOPIFY_SHOP="your-shop"
export SHOPIFY_CLIENT_ID="..."
export SHOPIFY_CLIENT_SECRET="..."
python3 tools/shopify_to_jekyll.py --dry-run
```

Optional variables:

```shell
export SHOPIFY_API_VERSION="2026-01"
export OUTPUT_DIR="/path/to/jekyll/repo"
```

Unpublished Shopify articles are fetched by default and written to `_drafts/`.
Use `--no-export-drafts` to skip unpublished articles.

The script writes migration artifacts such as `migration_redirects.csv` and
`migration_raw/shopify_articles.json`. These files can contain internal Shopify
URLs or draft metadata and should stay out of Git.

## Cleaning / Markdownify Migrated Posts

After migration, clean noisy Shopify/editor markup with:

```shell
python tools/clean_migrated_posts.py --dry-run
python tools/clean_migrated_posts.py --write --backup
git diff
```

The cleaner preserves YAML front matter, protects Liquid and code blocks, and
keeps complex HTML such as iframes, figures, video, audio, and tables as HTML.

## Local Build Helpers

Run a local Jekyll server:

```shell
bash tools/run.sh
```

Build and test the generated site:

```shell
bash tools/test.sh
```
