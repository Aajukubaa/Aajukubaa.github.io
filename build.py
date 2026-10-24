#!/usr/bin/env python3
"""
Build script for Kabir Bhuchar's portfolio.

Reads content.py + templates/index.html.j2, renders a single static
index.html at the repo root. Nothing here runs in the visitor's browser —
this only runs on your machine (or in CI) before you push.

Usage:
    pip install -r requirements.txt   # first time only
    python build.py
"""
import hashlib
import json
import copy
import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content
import bento

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_FILE = ROOT / "index.html"
ASSET_FILES = ["style.css", "main.js", "chess-dashboard.js", "search.js"]


def file_hash(path: Path, length: int = 8) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:length]


def build() -> None:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(enabled_extensions=("j2",)),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("index.html.j2")

    # Categories are consumed by main.js at runtime to fill in the detail
    # modal. Escape "</" so a literal "</script>" inside any content string
    # can't break out of the embedding <script> tag.
    categories = copy.deepcopy(content.CATEGORIES)
    for name, category in categories.items():
        bento.validate(name, category["bento"])
        category["bento"] = bento.render(category["bento"])
    categories_json = json.dumps(categories).replace("</", "<\\/")

    # A content hash appended as a query string (assets/style.css?v=abcd1234)
    # forces browsers/CDNs to fetch the new file the moment it actually
    # changes, instead of serving a stale cached copy indefinitely.
    asset_versions = {name: file_hash(ROOT / "assets" / name) for name in ASSET_FILES}

    html = template.render(
        site=content.SITE,
        nav_tabs=content.NAV_TABS,
        hero=content.HERO,
        specs=content.SPECS,
        connect_links=content.CONNECT_LINKS,
        connect_category_order=content.CONNECT_CATEGORY_ORDER,
        domain_cards=content.DOMAIN_CARDS,
        highlight_projects=content.HIGHLIGHT_PROJECTS,
        creative_archive=content.CREATIVE_ARCHIVE,
        now=content.NOW,
        current_year=datetime.date.today().year,
        categories_json=categories_json,
        asset_versions=asset_versions,
    )

    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"Built {OUTPUT_FILE} ({len(html):,} bytes)")


if __name__ == "__main__":
    build()