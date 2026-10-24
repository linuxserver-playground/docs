# docs

The documentation site of the LinuxServer.io v2 playground, published at
https://linuxserver-playground.github.io/docs/. It is the evolution of
[linuxserver/docker-documentation](https://github.com/linuxserver/docker-documentation): the same
mkdocs-material site, the same general guides, but the image pages are no longer pushed here by each image
build. The [hub](https://linuxserver-playground.github.io/hub/) renders one page per image from its `image.yml`
and this repository fetches them at build time. Nothing under `docs/images/` is committed.

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r docs/requirements.txt
python scripts/fetch-image-pages.py          # docs/images/, docs/deprecated_images/, docs/images-by-category.md
mkdocs serve                                 # http://127.0.0.1:8000/docs/
CI=true mkdocs build --strict                # what the deploy runs (CI enables the slow plugins)
```

For work against a local hub checkout, `python scripts/fetch-image-pages.py --local ../hub` reads
`out/stores/docs/` and `dist/api/v1/` there instead of the Pages site (run `python -m lsio_hub.build` and
`python -m lsio_hub.generate --offline` in the hub first).

## Layout

| Path | What |
| --- | --- |
| `mkdocs.yml` | Site configuration. `site_url` is the Pages URL under `/docs/`; `extra.lsio` is the shared header and footer with the www site; the `hooks` entry adds redirects for deprecated images. |
| `docs/general/` | The guides: containers 101, compose, PUID/PGID, volumes, updating, customisation, branding, SWAG, split DNS, and the v2 pages: how a build happens, contributing an image, Kubernetes, Podman quadlets, Docker in LXC on Proxmox, app stores. |
| `docs/misc/` | Support policy, read-only and non-root operation, finances. |
| `docs/FAQ.md`, `docs/index.md`, `docs/API.md` | The FAQ, the landing page, and the hub's OpenAPI specification rendered in place. |
| `docs/images/`, `docs/deprecated_images/`, `docs/images-by-category.md` | **Generated.** Written by `scripts/fetch-image-pages.py`, ignored by git. |
| `docs/.pages`, `docs/general/.pages` | Navigation (mkdocs-awesome-pages). |
| `docs/assets/`, `docs/stylesheets/`, `docs/javascripts/`, `overrides/` | Logo, fonts, `run.tpl` for the support alias, the LinuxServer.io theme and the header/footer partials. |
| `scripts/fetch-image-pages.py` | Downloads the generated pages from the hub; moves deprecated images to their own section. |
| `hooks/deprecated_redirects.py` | After the build, writes a redirect at the old address of every deprecated image. |
| `.github/workflows/deploy.yml` | Push to `main`, daily, `repository_dispatch` type `hub-updated`: fetch, `mkdocs build --strict`, deploy to Pages. |
| `.github/workflows/check.yml` | Pull requests: fetch and `mkdocs build --strict`. |

## How the image pages get here

Every image repository carries one manifest, `image.yml`. The hub ingests every release and renders
`images/docker-<name>.md` (mkdocs front matter, categories as tags) and `images-by-category.md` with the
builder's docs template, and publishes them at `https://linuxserver-playground.github.io/hub/stores/docs/`.
`scripts/fetch-image-pages.py` reads `/api/v1/images.deprecated.json` for the list of images and their
deprecation flag, downloads each page, puts the pages of deprecated images under `docs/deprecated_images/`
(rewriting the links in the category index) and writes `docs/deprecated_images/index.md`. The build fails if
any page cannot be fetched, so the site never publishes a partial fleet.

To change an image page, change its `image.yml`; see
[Contributing an image](https://linuxserver-playground.github.io/docs/general/contributing-an-image/).

## Deploying

Set the repository's Pages source to GitHub Actions. The site lives under the `/docs/` base path, which
`site_url` in `mkdocs.yml` sets; mkdocs-material resolves every internal link relative to it, and the
absolute links in `extra.lsio` (header and footer) are written with the `/docs/` prefix. The hub sends
`repository_dispatch` type `hub-updated` after each of its deploys; the daily cron catches anything missed.

Conventions: [`CONVENTIONS.md`](https://github.com/linuxserver-playground/builder/blob/main/CONVENTIONS.md) in
the builder repository. License: GPL-3.0, as the original.
