#!/usr/bin/env python3
"""Shared conference metadata cache and full-text search."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sqlite3
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "papers.sqlite"
USER_AGENT = "research-literature-index/0.1"
MINICONF_VENUES = {"iclr": "ICLR", "icml": "ICML"}
ACL_NS = {"m": "http://www.loc.gov/mods/v3"}


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def connect() -> sqlite3.Connection:
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.executescript(
        """
        PRAGMA journal_mode = WAL;
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY,
            paper_id TEXT NOT NULL,
            title TEXT NOT NULL,
            abstract TEXT NOT NULL DEFAULT '',
            authors TEXT NOT NULL DEFAULT '',
            institutions TEXT NOT NULL DEFAULT '',
            venue TEXT NOT NULL,
            year INTEGER NOT NULL,
            track TEXT NOT NULL DEFAULT 'main',
            decision TEXT NOT NULL DEFAULT 'accepted',
            topic TEXT NOT NULL DEFAULT '',
            keywords TEXT NOT NULL DEFAULT '',
            official_url TEXT NOT NULL,
            paper_url TEXT NOT NULL DEFAULT '',
            pdf_url TEXT NOT NULL DEFAULT '',
            source_url TEXT NOT NULL,
            synced_at TEXT NOT NULL,
            UNIQUE(venue, year, paper_id)
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS papers_fts USING fts5(
            title, abstract, authors, institutions, topic, keywords,
            content='papers', content_rowid='id'
        );
        CREATE TRIGGER IF NOT EXISTS papers_ai AFTER INSERT ON papers BEGIN
          INSERT INTO papers_fts(rowid,title,abstract,authors,institutions,topic,keywords)
          VALUES(new.id,new.title,new.abstract,new.authors,new.institutions,new.topic,new.keywords);
        END;
        CREATE TRIGGER IF NOT EXISTS papers_ad AFTER DELETE ON papers BEGIN
          INSERT INTO papers_fts(papers_fts,rowid,title,abstract,authors,institutions,topic,keywords)
          VALUES('delete',old.id,old.title,old.abstract,old.authors,old.institutions,old.topic,old.keywords);
        END;
        CREATE TRIGGER IF NOT EXISTS papers_au AFTER UPDATE ON papers BEGIN
          INSERT INTO papers_fts(papers_fts,rowid,title,abstract,authors,institutions,topic,keywords)
          VALUES('delete',old.id,old.title,old.abstract,old.authors,old.institutions,old.topic,old.keywords);
          INSERT INTO papers_fts(rowid,title,abstract,authors,institutions,topic,keywords)
          VALUES(new.id,new.title,new.abstract,new.authors,new.institutions,new.topic,new.keywords);
        END;
        CREATE TABLE IF NOT EXISTS sync_runs (
            venue TEXT NOT NULL,
            year INTEGER NOT NULL,
            source_url TEXT NOT NULL,
            paper_count INTEGER NOT NULL,
            synced_at TEXT NOT NULL,
            PRIMARY KEY(venue, year, source_url)
        );
        """
    )
    return db


def clean_text(value: object) -> str:
    return re.sub(r"\s+", " ", html.unescape(str(value or ""))).strip()


def openreview_id(url: str, fallback: object) -> str:
    query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    return query.get("id", [str(fallback)])[0]


def fetch_miniconf(venue: str, year: int) -> tuple[list[dict], list[str]]:
    slug = venue.lower()
    base = f"https://{slug}.cc"
    papers_url = f"{base}/static/virtual/data/{slug}-{year}-orals-posters.json"
    abstracts_url = f"{base}/static/virtual/data/{slug}-{year}-abstracts.json"
    payload = json.loads(fetch(papers_url))
    abstracts = json.loads(fetch(abstracts_url))
    expected_source = f"{venue.upper()}.cc/{year}/Conference"
    synced_at = dt.datetime.now(dt.UTC).isoformat()
    rows = []

    for item in payload["results"]:
        source_url = clean_text(item.get("sourceurl"))
        if expected_source not in source_url:
            continue
        decision = clean_text(item.get("decision"))
        if not decision.lower().startswith("accept"):
            continue
        paper_url = clean_text(item.get("paper_url"))
        item_id = str(item["id"])
        paper_id = openreview_id(paper_url, item_id)
        authors = [clean_text(a.get("fullname")) for a in item.get("authors", [])]
        institutions = sorted(
            {clean_text(a.get("institution")) for a in item.get("authors", []) if a.get("institution")}
        )
        official_path = clean_text(item.get("virtualsite_url"))
        official_url = urllib.parse.urljoin(base, official_path)
        pdf_url = clean_text(item.get("paper_pdf_url"))
        if not pdf_url and "openreview.net/forum" in paper_url:
            pdf_url = f"https://openreview.net/pdf?id={urllib.parse.quote(paper_id)}"
        keywords = item.get("keywords") or []
        if not isinstance(keywords, list):
            keywords = [keywords]
        rows.append(
            {
                "paper_id": paper_id,
                "title": clean_text(item.get("name")),
                "abstract": clean_text(abstracts.get(item_id, "")),
                "authors": "; ".join(filter(None, authors)),
                "institutions": "; ".join(institutions),
                "venue": venue.upper(),
                "year": year,
                "track": "main",
                "decision": decision,
                "topic": clean_text(item.get("topic")),
                "keywords": "; ".join(clean_text(k) for k in keywords),
                "official_url": official_url,
                "paper_url": paper_url,
                "pdf_url": pdf_url,
                "source_url": papers_url,
                "synced_at": synced_at,
            }
        )
    return rows, [papers_url, abstracts_url]


def xml_text(node: ET.Element | None) -> str:
    return clean_text("".join(node.itertext())) if node is not None else ""


def fetch_acl(year: int) -> tuple[list[dict], list[str]]:
    synced_at = dt.datetime.now(dt.UTC).isoformat()
    rows: list[dict] = []
    sources: list[str] = []

    for track in ("long", "short"):
        source_url = f"https://aclanthology.org/volumes/{year}.acl-{track}.xml"
        sources.append(source_url)
        root = ET.fromstring(fetch(source_url))
        for item in root.findall("m:mods", ACL_NS):
            official_url = xml_text(item.find("m:location/m:url", ACL_NS))
            match = re.search(rf"/({year}\.acl-{track}\.\d+)/?$", official_url)
            if not match or match.group(1).endswith(".0"):
                continue
            authors = []
            for name in item.findall("m:name[@type='personal']", ACL_NS):
                roles = [xml_text(x).lower() for x in name.findall("m:role/m:roleTerm", ACL_NS)]
                if "author" not in roles:
                    continue
                given = [xml_text(x) for x in name.findall("m:namePart[@type='given']", ACL_NS)]
                family = xml_text(name.find("m:namePart[@type='family']", ACL_NS))
                authors.append(" ".join([*filter(None, given), family]).strip())
            rows.append(
                {
                    "paper_id": match.group(1),
                    "title": xml_text(item.find("m:titleInfo/m:title", ACL_NS)),
                    "abstract": "",
                    "authors": "; ".join(authors),
                    "institutions": "",
                    "venue": "ACL",
                    "year": year,
                    "track": track,
                    "decision": "accepted",
                    "topic": "",
                    "keywords": "",
                    "official_url": official_url,
                    "paper_url": official_url,
                    "pdf_url": official_url.rstrip("/") + ".pdf",
                    "source_url": source_url,
                    "synced_at": synced_at,
                }
            )
    return rows, sources


PAPER_COLUMNS = (
    "paper_id", "title", "abstract", "authors", "institutions", "venue", "year",
    "track", "decision", "topic", "keywords", "official_url", "paper_url",
    "pdf_url", "source_url", "synced_at",
)


def sync(venue: str, year: int) -> int:
    if venue in MINICONF_VENUES:
        rows, sources = fetch_miniconf(MINICONF_VENUES[venue], year)
        venue_name = MINICONF_VENUES[venue]
    elif venue == "acl":
        rows, sources = fetch_acl(year)
        venue_name = "ACL"
    else:
        raise ValueError(f"unsupported venue: {venue}")
    if not rows:
        raise RuntimeError(f"{venue_name} {year}: official source returned no accepted papers")
    rows = list({row["paper_id"]: row for row in rows}.values())

    placeholders = ",".join("?" for _ in PAPER_COLUMNS)
    updates = ",".join(f"{column}=excluded.{column}" for column in PAPER_COLUMNS[1:])
    with connect() as db:
        db.execute("DELETE FROM papers WHERE venue=? AND year=?", (venue_name, year))
        db.executemany(
            f"""
            INSERT INTO papers ({",".join(PAPER_COLUMNS)}) VALUES ({placeholders})
            ON CONFLICT(venue,year,paper_id) DO UPDATE SET {updates}
            """,
            [[row[column] for column in PAPER_COLUMNS] for row in rows],
        )
        db.execute("DELETE FROM sync_runs WHERE venue=? AND year=?", (venue_name, year))
        for source in sources:
            db.execute(
                "INSERT INTO sync_runs VALUES (?,?,?,?,?)",
                (venue_name, year, source, len(rows), rows[0]["synced_at"]),
            )
    print(f"{venue_name} {year}: {len(rows)} papers")
    return len(rows)


def fts_query(text: str, any_term: bool) -> str:
    terms = re.findall(r"\w+", text, flags=re.UNICODE)
    if not terms:
        raise ValueError("query has no searchable terms")
    operator = " OR " if any_term else " AND "
    return operator.join(f'"{term.replace(chr(34), chr(34) * 2)}"' for term in terms)


def search(args: argparse.Namespace) -> None:
    where = ["papers_fts MATCH ?"]
    params: list[object] = [fts_query(args.query, args.any)]
    if args.venue:
        where.append("p.venue = ?")
        params.append(args.venue.upper())
    if args.year:
        where.append("p.year = ?")
        params.append(args.year)
    if args.track:
        where.append("p.track = ?")
        params.append(args.track)
    params.append(args.limit)
    sql = f"""
        SELECT p.*, bm25(papers_fts, 5.0, 1.0, 0.3, 0.3, 0.5, 0.5) AS score
        FROM papers_fts JOIN papers p ON p.id = papers_fts.rowid
        WHERE {" AND ".join(where)}
        ORDER BY score, p.year DESC, p.title
        LIMIT ?
    """
    rows = [dict(row) for row in connect().execute(sql, params)]
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    for row in rows:
        print(f"[{row['venue']} {row['year']} · {row['track']}] {row['title']}")
        print(f"  {row['official_url']}")
    print(f"{len(rows)} result(s)")


def status() -> None:
    db = connect()
    rows = db.execute(
        """
        SELECT venue, year, COUNT(*) AS papers, MAX(synced_at) AS synced_at
        FROM papers GROUP BY venue, year ORDER BY year DESC, venue
        """
    ).fetchall()
    if not rows:
        print("index is empty")
        return
    for row in rows:
        print(f"{row['venue']} {row['year']}: {row['papers']} papers · {row['synced_at']}")
    print(f"database: {DB_PATH}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_parser = subparsers.add_parser("sync", help="download official conference metadata")
    sync_parser.add_argument("--venue", choices=["iclr", "icml", "acl", "all"], default="all")
    sync_parser.add_argument("--year", type=int, default=dt.date.today().year)

    search_parser = subparsers.add_parser("search", help="search title, abstract, authors and affiliations")
    search_parser.add_argument("query")
    search_parser.add_argument("--venue", choices=["iclr", "icml", "acl"])
    search_parser.add_argument("--year", type=int)
    search_parser.add_argument("--track")
    search_parser.add_argument("--limit", type=int, default=20)
    search_parser.add_argument("--any", action="store_true", help="match any query term instead of all terms")
    search_parser.add_argument("--json", action="store_true")

    subparsers.add_parser("status", help="show indexed conference coverage")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "sync":
            venues = MINICONF_VENUES if args.venue == "all" else [args.venue]
            if args.venue == "all":
                venues = [*MINICONF_VENUES, "acl"]
            for venue in venues:
                sync(venue, args.year)
        elif args.command == "search":
            search(args)
        else:
            status()
    except (OSError, ValueError, RuntimeError, sqlite3.Error, ET.ParseError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
