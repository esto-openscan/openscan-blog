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

## Writing a New Post

Create a Markdown file in `_posts/` using Jekyll's post filename format:

```text
YYYY-MM-DD-post-slug.md
```

Example:

```text
_posts/2026-05-27-blog-moved-to-jekyll-and-chirpy.md
```

Use front matter like this:

```yaml
---
title: "The OpenScan Blog Has Moved"
date: "2026-05-27T15:16:12+02:00"
author: "Thomas Megel"
description: "Short summary for previews and SEO."
categories:
  - "News"
tags:
  - "openscan"
  - "blog"
---
```

For a title or preview image, place the file next to other post assets:

```text
assets/img/posts/2026-05-27-blog-moved-to-jekyll-and-chirpy/cover.png
```

Then reference it in the post front matter:

```yaml
image:
  path: "/assets/img/posts/2026-05-27-blog-moved-to-jekyll-and-chirpy/cover.png"
  alt: "OpenScan blog migration announcement cover image"
```

If a post uses LaTeX or other MathJax syntax, enable math explicitly:

```yaml
math: true
```

Inline math then works like this:

```markdown
$E = mc^2$
```

Before publishing, run a production build:

```shell
docker compose exec -T -u vscode -e JEKYLL_ENV=production site bundle exec jekyll build
```

If the local preview container is running, the site can also be checked at
<http://localhost:4000>.

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
