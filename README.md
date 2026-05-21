# OpenScan Blog

This repository contains the Jekyll source for the OpenScan blog.

The site is built with Jekyll and the Chirpy theme. Theme code, bundled
third-party assets, fonts, and vendored libraries keep their original licenses.

## Local Development

Build and start the local preview:

```shell
docker compose up --build
```

The site is available at <http://localhost:4000>. Jekyll runs inside the
container with LiveReload enabled and uses a Docker volume for the Bundler gem
cache.

Stop the local environment:

```shell
docker compose down
```

Generated local files such as `_site`, `.jekyll-cache`, `.sass-cache`,
`vendor/bundle`, `vendor/cache`, and `node_modules` should not be committed.

## Tools

Migration and content-cleanup helpers live in [`tools/`](tools/README.md).
Shopify migration artifacts such as `migration_redirects.csv`, `migration_raw/`,
and `_drafts/` are intentionally ignored.

## Licensing

This repository uses multiple licenses because it contains code, editorial
content, media assets, and third-party dependencies.

See [`LICENSE`](LICENSE) for the repository-level licensing policy and
[`LICENSES/`](LICENSES/) for the referenced license notices.
