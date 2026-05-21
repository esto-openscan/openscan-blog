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

## Formatting

See the Chirpy [formatting examples](https://chirpy.cotes.page/posts/text-and-typography/).

## Tools

Migration and content-cleanup helpers live in [`tools/`](tools/README.md).
Shopify migration artifacts such as `migration_redirects.csv`, `migration_raw/`,
and `_drafts/` are intentionally ignored.

## Legacy Posts

Posts migrated from the old OpenScan blog that describe older hardware or
software generations should use this front matter flag:

```yaml
legacy: true
```

Legacy posts automatically show an archive note above the article content. Do
not use `legacy` or `outdated` as public tags; keep topic tags focused on
searchable subjects such as hardware, firmware, workflows, or product names.

## Theme Overrides

This site intentionally overrides selected Chirpy theme files:

- `_layouts/post.html` adds the legacy archive note above post content.
- `_includes/sidebar.html` adds the OpenScan.eu and Shop links above the sidebar
  footer.

When upgrading `jekyll-theme-chirpy`, compare these local files with the new
theme versions and merge upstream changes as needed.

## Licensing

This repository uses multiple licenses because it contains code, editorial
content, media assets, and third-party dependencies.

See [`LICENSE`](LICENSE) for the repository-level licensing policy and
[`LICENSES/`](LICENSES/) for the referenced license notices.
