#!/usr/bin/env python3
"""
Converts each certificate PDF's first page into a JPG image — browsers
can't display a raw PDF with an <img> tag, so this renders one at build
time instead. Output goes into the same certificates/ folder as the
source PDFs, using a URL-safe version of the same filename (spaces in
the original PDF names aren't a great fit for a web asset URL).

Run automatically by .github/workflows/build.yml whenever a file in
certificates/ changes. Can also be run manually:

    pip install -r requirements.txt
    python render_certificates.py
"""
import re
from pathlib import Path

import pymupdf

CERT_DIR = Path(__file__).parent / "certificates"
DPI = 200  # sharp enough to read clearly, without producing huge files


def slugify(name: str) -> str:
    name = name.lower().replace("&", "and")
    name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return name


def main() -> None:
    if not CERT_DIR.exists():
        print(f"No {CERT_DIR} folder yet — nothing to convert.")
        return

    pdfs = sorted(CERT_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {CERT_DIR}.")
        return

    for pdf_path in pdfs:
        out_path = CERT_DIR / f"{slugify(pdf_path.stem)}.jpg"
        doc = pymupdf.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap(dpi=DPI)
        pix.save(out_path)
        doc.close()
        print(f"Rendered {pdf_path.name} -> {out_path.name}")


if __name__ == "__main__":
    main()
