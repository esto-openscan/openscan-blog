# Chirpy Starter

[![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy)][gem]&nbsp;
[![GitHub license](https://img.shields.io/github/license/cotes2020/chirpy-starter.svg?color=blue)][mit]

A minimal, ready-to-use template for creating a blog with the [**Chirpy**][chirpy] Jekyll theme. Get up and running in minutes with all critical files pre-configured.

## Why This Starter Exists

When installing Chirpy through [RubyGems.org][gem], Jekyll can only read a subset of theme files (`_data`, `_layouts`, `_includes`, `_sass`, `assets`) and limited `_config.yml` options from the gem. As a result, users cannot enjoy the full out-of-the-box experience that Chirpy offers.

To unlock all features, the following files must be present in your Jekyll site:

```shell
.
├── _config.yml
├── _plugins
├── _tabs
└── index.html
```

This starter bundles those files from the latest **Chirpy** release along with a [CD][CD] workflow, so you can start writing immediately.

## Usage

Check out the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

## Shopify Blog Migration

The one-off Shopify-to-Jekyll migration script lives at `tools/shopify_to_jekyll.py`.
It is read-only for Shopify blog content. The only POST it can send to Shopify is
the optional OAuth client credentials token exchange at `/admin/oauth/access_token`.

Install the Python dependencies in a local environment:

```shell
pip install requests beautifulsoup4
```

Use an existing Admin API access token:

```shell
export SHOPIFY_SHOP="openscan.myshopify.com"
export SHOPIFY_ADMIN_TOKEN="..."
python3 tools/shopify_to_jekyll.py --dry-run
```

Or use the Shopify Dev Dashboard client credentials flow:

```shell
export SHOPIFY_SHOP="openscan"
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
Use `--no-export-drafts` when you want to skip them. Shopify `summary_html` is
exported as front matter: `description` contains a plain-text excerpt, and
`shopify_summary_html` keeps the original HTML.

## Local development with Docker

Build and start the local preview:

```shell
docker compose up --build
```

The site is available at <http://localhost:4000>. Jekyll runs inside the container with LiveReload enabled and uses a Docker volume for the Bundler gem cache.

Stop the local environment:

```shell
docker compose down
```

Generated local files such as `_site`, `.jekyll-cache`, `.sass-cache`, `vendor/bundle`, `vendor/cache`, and `node_modules` should not be committed.

## Contributing

This repository is automatically updated with new releases from the theme repository. If you encounter any issues or want to contribute to its improvement, please visit the [theme repository][chirpy] to provide feedback.

## License

This work is published under [MIT][mit] License.

[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
[CD]: https://en.wikipedia.org/wiki/Continuous_deployment
[mit]: https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE
