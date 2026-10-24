"""
mkdocs hook: a deprecated image keeps its old address.

scripts/fetch-image-pages.py moves the page of every image the hub marks deprecated from docs/images/ to
docs/deprecated_images/. Links to the old address (README badges, the OCI documentation label, search
engines) still arrive at /images/docker-<name>/, so after the build this hook writes a small redirect page
there. The set of deprecated images changes with every hub run, so it cannot live in mkdocs.yml.
"""

from __future__ import annotations

import os
from pathlib import Path

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting...</title>
<link rel="canonical" href="{target}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
Redirecting to <a href="{target}">{target}</a>...
</body>
</html>
"""


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    deprecated = sorted(p.stem for p in (docs_dir / "deprecated_images").glob("docker-*.md"))
    for name in deprecated:
        if config["use_directory_urls"]:
            page = site_dir / "images" / name / "index.html"
            target = f"../../deprecated_images/{name}/"
        else:
            page = site_dir / "images" / f"{name}.html"
            target = f"../deprecated_images/{name}.html"
        if page.exists():
            # A live page with that name exists; the hub listed it twice. Leave it alone.
            continue
        os.makedirs(page.parent, exist_ok=True)
        page.write_text(TEMPLATE.format(target=target), encoding="utf-8")
