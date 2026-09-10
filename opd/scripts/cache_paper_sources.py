#!/usr/bin/env python3
"""Cache arXiv/OpenReview papers as markdown for OPD brief generation."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


STORAGE = Path.home() / ".arxiv-mcp-storage"
USER_AGENT = "opd-autoresearch/1.0 (paper cache)"


class TextHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "h4", "li", "tr", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "h4", "li", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        text = unescape(" ".join(self.parts))
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n\s+", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


def html_to_text(html: bytes) -> str:
    parser = TextHTMLParser()
    parser.feed(html.decode("utf-8", errors="ignore"))
    return parser.text()


def pdf_to_text(pdf_bytes: bytes) -> str:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - environment guard
        raise RuntimeError("bundled Python runtime is missing pypdf") from exc

    import io

    reader = PdfReader(io.BytesIO(pdf_bytes))
    chunks = []
    for idx, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text.strip():
            chunks.append(f"\n\n# Page {idx}\n\n{text.strip()}")
    return "\n".join(chunks).strip()


def write_cache(cache_id: str, source_url: str, text: str) -> Path:
    STORAGE.mkdir(parents=True, exist_ok=True)
    out = STORAGE / f"{cache_id}.md"
    out.write_text(f"Source: {source_url}\n\n{text.strip()}\n", encoding="utf-8")
    return out


def cache_arxiv(arxiv_id: str) -> Path:
    html_url = f"https://arxiv.org/html/{arxiv_id}"
    try:
        text = html_to_text(fetch(html_url))
        if len(text) > 5000:
            return write_cache(arxiv_id, html_url, text)
    except Exception as html_exc:
        last_error = html_exc
    else:
        last_error = RuntimeError("arXiv HTML too short")

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    try:
        text = pdf_to_text(fetch(pdf_url))
        if len(text) > 5000:
            return write_cache(arxiv_id, pdf_url, text)
    except Exception as pdf_exc:
        raise RuntimeError(f"failed arXiv cache for {arxiv_id}: html={last_error}; pdf={pdf_exc}") from pdf_exc
    raise RuntimeError(f"failed arXiv cache for {arxiv_id}: html={last_error}; pdf text too short")


def cache_openreview(cache_id: str, forum_id: str) -> Path:
    urls = [
        f"https://openreview.net/pdf?id={forum_id}",
        f"https://openreview.net/attachment?id={forum_id}&name=pdf",
    ]
    errors = []
    for url in urls:
        try:
            blob = fetch(url)
            text = pdf_to_text(blob)
            if len(text) > 3000:
                return write_cache(cache_id, url, text)
            errors.append(f"{url}: extracted text too short")
        except Exception as exc:
            errors.append(f"{url}: {exc}")
    raise RuntimeError(f"failed OpenReview cache for {forum_id}: " + "; ".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arxiv-id", nargs="*", default=[])
    parser.add_argument("--openreview", nargs=2, action="append", metavar=("CACHE_ID", "FORUM_ID"), default=[])
    args = parser.parse_args()

    failures = []
    for arxiv_id in args.arxiv_id:
        try:
            path = cache_arxiv(arxiv_id)
            print(f"cached {arxiv_id}: {path}")
        except Exception as exc:
            failures.append(f"{arxiv_id}: {exc}")
            print(f"FAILED {arxiv_id}: {exc}", file=sys.stderr)
    for cache_id, forum_id in args.openreview:
        try:
            path = cache_openreview(cache_id, forum_id)
            print(f"cached {cache_id}: {path}")
        except Exception as exc:
            failures.append(f"{cache_id}: {exc}")
            print(f"FAILED {cache_id}: {exc}", file=sys.stderr)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
