#!/usr/bin/env python3
"""Build SQLite FTS5 search index from Sphinx HTML output.

Creates searchindex.db in the build directory with four BM25-weighted fields:
title (10x), code_blocks (5x), image_alt (5x), body_text (1x).

Usage:
    python scripts/build_searchindex.py <build_dir>
"""

import sqlite3
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Comment

_SKIP_FILES = {"search.html", "genindex.html", "searchindex.js"}

_STRIP_TAGS = {
    "script", "style", "nav", "footer", "header",
    "noscript", "form", "button",
}

_STRIP_CLASSES = {
    "wy-nav-top", "wy-nav-side", "wy-breadcrumbs",
    "rst-versions", "footer", "headerlink",
    "toctree-wrapper",
    "sphinxsidebar", "related",
    "sphinx-tabs-tab",
}

_SPHINX_INTERNALS = {
    "_static", "_sources", "_images", "_downloads",
    "_sphinx_design_static", "doctrees",
}


def _strip_noise(soup):
    """Remove navigation chrome and HTML comments in-place.

    Collects tags first, then decomposes — avoids mutating the tree mid-iteration.
    """
    to_remove = []
    for tag in soup.find_all(True):
        if tag.name in _STRIP_TAGS:
            to_remove.append(tag)
        else:
            classes = set(tag.get("class") or [])
            if classes & _STRIP_CLASSES:
                to_remove.append(tag)
    for tag in to_remove:
        tag.decompose()
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()


def _extract_fields(html_path):
    """Parse one HTML file and return (title, code_blocks, image_alt, body_text).

    :param html_path: Path to the HTML file
    :returns: (title, code_blocks, image_alt, body_text) as plain strings
    """
    soup = BeautifulSoup(
        html_path.read_text(encoding="utf-8", errors="ignore"),
        "html.parser",
    )

    h1 = soup.find("h1")
    if h1:
        for span in h1.find_all("span", class_="section-number"):
            span.decompose()
        title = h1.get_text(" ", strip=True)
    else:
        title = ""
    if not title:
        t = soup.find("title")
        title = t.get_text(" ", strip=True) if t else html_path.stem

    # Extract code-like markup before stripping noise so these land in
    # code_blocks (5x weight) not body_text (1x).
    # :command: → <strong class="command">, :program: → <strong class="program">
    code_parts = []
    for tag in soup.find_all(["pre", "code"]):
        text = tag.get_text(" ", strip=True)
        if text:
            code_parts.append(text)
        tag.decompose()

    for tag in soup.find_all("strong", class_=lambda c: c and (
            "command" in c or "program" in c)):
        text = tag.get_text(" ", strip=True)
        if text:
            code_parts.append(text)
        tag.decompose()

    code_blocks = " ".join(code_parts)

    # Extract image alt text (5x weight)
    alt_parts = []
    for img in soup.find_all("img"):
        alt = img.get("alt", "").strip()
        if alt:
            alt_parts.append(alt)
    image_alt = " ".join(alt_parts)

    _strip_noise(soup)

    # Theme-specific main content selectors: RTD → classic → fallback
    main = (
        soup.find("div", {"role": "main"})
        or soup.find("div", class_="document")
        or soup.find("div", class_="body")
        or soup.find("body")
        or soup
    )
    body_text = main.get_text(" ", strip=True) if main else soup.get_text(" ", strip=True)

    return title, code_blocks, image_alt, body_text


def build_index(build_dir):
    db_path = build_dir / "searchindex.db"
    if db_path.exists():
        db_path.unlink()

    con = sqlite3.connect(db_path)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("""
        CREATE TABLE docs (
            id          INTEGER PRIMARY KEY,
            docname     TEXT NOT NULL,
            title       TEXT,
            code_blocks TEXT,
            image_alt   TEXT,
            body_text   TEXT
        )
    """)
    con.execute("""
        CREATE VIRTUAL TABLE fts USING fts5(
            title,
            code_blocks,
            image_alt,
            body_text,
            content=docs,
            content_rowid=id,
            tokenize='porter ascii'
        )
    """)

    html_files = sorted(build_dir.rglob("*.html"))
    total = len(html_files)
    inserted = 0

    print(f"Indexing {total} HTML files in {build_dir} ...")

    for i, html_path in enumerate(html_files):
        if html_path.name in _SKIP_FILES:
            continue
        relative = html_path.relative_to(build_dir)
        if relative.parts[0] in _SPHINX_INTERNALS:
            continue

        try:
            title, code_blocks, image_alt, body_text = _extract_fields(html_path)
        except Exception as exc:
            print(f"  SKIP {relative}: {exc}")
            continue

        con.execute(
            "INSERT INTO docs (docname, title, code_blocks, image_alt, body_text) VALUES (?,?,?,?,?)",
            (str(relative.with_suffix("")), title, code_blocks, image_alt, body_text),
        )
        inserted += 1

        if (i + 1) % 50 == 0:
            print(f"  {i + 1}/{total} processed ...")

    con.execute("""
        INSERT INTO fts(rowid, title, code_blocks, image_alt, body_text)
        SELECT id, title, code_blocks, image_alt, body_text FROM docs
    """)
    con.commit()
    con.execute("INSERT INTO fts(fts) VALUES('optimize')")
    con.commit()
    con.close()

    size_kb = db_path.stat().st_size // 1024
    print(f"Done. Indexed {inserted} pages → {db_path} ({size_kb} KB)")
    return db_path


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    build_dir = Path(sys.argv[1])
    if not build_dir.exists():
        print(f"ERROR: {build_dir} does not exist")
        sys.exit(1)
    build_index(build_dir)


if __name__ == "__main__":
    main()
