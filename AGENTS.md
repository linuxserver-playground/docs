# AGENTS.md - docs

## Purpose

This repository produces the documentation site at https://linuxserver-playground.github.io/docs/: the
general guides (running, updating, customising our containers; PUID/PGID; SWAG; Kubernetes, Podman, LXC and
app-store guides; how a build happens; contributing) plus one page per image. The image pages are not
written here. The hub renders them from each image's `image.yml` and `scripts/fetch-image-pages.py` downloads
them at build time. Consumers are users of the images, the www site (which links here) and the README badges
of every image repository.

## Layout

| Path | What |
| --- | --- |
| `mkdocs.yml` | Site config: mkdocs-material, awesome-pages nav, redirects, `extra.lsio` shared shell, `hooks`. |
| `docs/general/`, `docs/misc/`, `docs/FAQ.md`, `docs/index.md`, `docs/API.md` | Hand-written pages. |
| `docs/.pages`, `docs/general/.pages` | Navigation order and section titles (awesome-pages). |
| `docs/images/`, `docs/deprecated_images/`, `docs/images-by-category.md` | Generated at build time; in `.gitignore`. |
| `docs/assets/`, `docs/stylesheets/`, `docs/javascripts/`, `overrides/partials/` | Theme: logo, fonts, CSS, header and footer. |
| `scripts/fetch-image-pages.py` | Fetches the generated pages from the hub (`--local <hub checkout>` for development). |
| `hooks/deprecated_redirects.py` | mkdocs hook: redirects from `images/docker-<name>/` to `deprecated_images/` after the build. |
| `.github/workflows/` | `deploy.yml` (push, daily cron, `repository_dispatch: hub-updated`) and `check.yml` (PRs, `--strict`). |

## What you may edit

Everything except the three generated paths above. Never commit anything under `docs/images/`,
`docs/deprecated_images/` or `docs/images-by-category.md`; a wrong image page is fixed in that image's
`image.yml`, a wrong rendering in the builder's `templates/docs.md.j2` or the hub's `generate/docs.py`. Keep
the general pages accurate to the v2 world (image.yml, `builder check`/`render`, GitHub Actions, the hub, the
control plane); there is no Jenkins, `readme-vars.yml` or templates repository to mention. New pages need an
entry in the relevant `.pages` file. Links into the hub use `https://linuxserver-playground.github.io/hub/...`;
links into this site from `mkdocs.yml` `extra.lsio` are absolute with the `/docs/` prefix.

## How to validate

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r docs/requirements.txt
python scripts/fetch-image-pages.py                 # or: --local ../hub
CI=true mkdocs build --strict                       # exactly what deploy.yml and check.yml run
mkdocs serve                                        # preview at http://127.0.0.1:8000/docs/
```

`--strict` fails on any warning: broken relative links, pages missing from the nav, unknown anchors in the
`.pages` files. Fix the warning; do not relax the setting.

## Contracts

Consumes, from the hub (which in turn renders with `builder.render` from `linuxserver-playground/builder`):
`/stores/docs/images/docker-<name>.md` and `/stores/docs/images-by-category.md` (Markdown with mkdocs
front matter: `title`, `tags`, `description`), and `/api/v1/images.deprecated.json` (v1 `ImagesResponse`,
`name` and `deprecated` per image) for the fleet list. Produces no schema. `docs/assets/run.tpl` is fetched by
the support alias in `general/how-to-get-support.md`; keep its path stable. See
[`CONVENTIONS.md`](https://github.com/linuxserver-playground/builder/blob/main/CONVENTIONS.md) §1 (`docs`:
everything hand-edited except `docs/images/`).

## Pull request rules

Disclose AI use in the PR description. One change per PR. Commit subjects are short imperative sentences
(`Add Kubernetes guide`); no conventional-commit prefixes, emoji or trailers. No typo-only PRs (open an
issue). Do not commit generated pages, `site/` or credentials. The PR check must pass `mkdocs build --strict`.
