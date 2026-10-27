#!/usr/bin/env python3
"""Download official 2026 conference indexes and match the local paper list."""
import concurrent.futures
import argparse
import csv
import difflib
import hashlib
import html
import io
import json
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'notes/conference-index-2026'
SHARED = ROOT.parent / 'literature-index/tmp'
RAW = OUT / 'raw'
NS = {'m': 'http://www.loc.gov/mods/v3'}


def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(str(s or ''))).strip()


def norm(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', clean(s)).lower())


def download(spec):
    name, url, cache = spec
    target = RAW / name
    error = None
    if target.exists():
        path, mode = target, 'downloaded-local'
    else:
        temp = target.with_suffix(target.suffix + '.part')
        r = subprocess.run(['curl', '-fLsS', '--http1.1', '--connect-timeout', '15',
                            '--max-time', '45', '--retry', '2', '--retry-all-errors',
                            '--retry-delay', '1', url, '-o', str(temp)],
                           capture_output=True, text=True, timeout=170)
        if r.returncode == 0:
            temp.replace(target)
            path, mode = target, 'downloaded'
        elif cache and cache.exists():
            temp.unlink(missing_ok=True)
            path, mode, error = cache, 'shared-cache-fallback', r.stderr.strip()[-350:]
        else:
            temp.unlink(missing_ok=True)
            return {'name': name, 'url': url, 'error': r.stderr.strip()[-350:]}
    data = path.read_bytes()
    return {'name': name, 'url': url, 'path': str(path), 'mode': mode,
            'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'download_error': error}


def miniconf(venue, source, abstract_source):
    payload = json.loads(Path(source['path']).read_text())
    abstracts = json.loads(Path(abstract_source['path']).read_text()) if abstract_source else {}
    rows = {}
    for item in payload.get('results', []):
        decision = clean(item.get('decision'))
        origin = clean(item.get('sourceurl'))
        if not decision.lower().startswith('accept'):
            continue
        expected = f'{venue}.cc/2026/'.lower()
        if expected not in origin.lower() and 'journal-track/' not in origin:
            continue
        track = origin.split('2026/')[-1] if expected in origin.lower() else 'journal'
        if track == 'BlogPosts':
            continue
        paper_url = clean(item.get('paper_url'))
        oid = re.search(r'[?&]id=([^&]+)', paper_url)
        pid = oid.group(1) if oid else str(item['id'])
        row = {'venue': venue, 'year': 2026, 'track': track, 'decision': decision,
               'paper_id': pid, 'title': clean(item.get('name')),
               'authors': [clean(a.get('fullname')) for a in item.get('authors', [])],
               'abstract': clean(abstracts.get(str(item['id']), '')),
               'official_url': f'https://{venue.lower()}.cc' + clean(item.get('virtualsite_url')),
               'paper_url': paper_url, 'source_url': source['url'],
               'arxiv_ids': sorted(set(re.findall(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})',
                                    ' '.join(clean(item.get(k)) for k in ['paper_url', 'paper_pdf_url', 'external_url']))))}
        key = (pid, track)
        rank = lambda d: 3 if 'oral' in d.lower() else 2 if 'spotlight' in d.lower() else 1
        if key not in rows or rank(decision) > rank(rows[key]['decision']):
            rows[key] = row
    return list(rows.values())


def anthology(source, track):
    root = ET.parse(source['path']).getroot()
    rows = []
    def txt(node):
        return clean(''.join(node.itertext())) if node is not None else ''
    for item in root.findall('m:mods', NS):
        url = txt(item.find('m:location/m:url', NS))
        if not re.search(r'/2026\.(?:acl-(?:long|short)|findings-acl)\.\d+/?$', url) or url.rstrip('/').endswith('.0'):
            continue
        authors = []
        for name in item.findall("m:name[@type='personal']", NS):
            if not any(txt(x).lower() == 'author' for x in name.findall('m:role/m:roleTerm', NS)):
                continue
            parts = name.findall("m:namePart[@type='given']", NS) + name.findall("m:namePart[@type='family']", NS)
            authors.append(' '.join(txt(x) for x in parts))
        rows.append({'venue': 'ACL', 'year': 2026, 'track': track, 'decision': 'accepted',
                     'paper_id': url.rstrip('/').split('/')[-1],
                     'title': txt(item.find('m:titleInfo/m:title', NS)), 'authors': authors,
                     'abstract': txt(item.find('m:abstract', NS)), 'official_url': url,
                     'paper_url': url, 'source_url': source['url']})
    return rows


def emnlp(source):
    rows = []
    for item in csv.DictReader(io.StringIO(Path(source['path']).read_text())):
        pid = item['Paper ID #-track)'].strip()
        rows.append({'venue': 'EMNLP', 'year': 2026, 'track': pid.split('-')[-1],
                     'decision': clean(item.get('Assigned \nPres Type')),
                     'paper_id': pid, 'title': clean(item['Title']), 'authors': [],
                     'abstract': '', 'official_url': 'https://2026.emnlp.org/program/',
                     'paper_url': '', 'source_url': source['url']})
    return rows


def match(papers):
    exact = {}
    for row in papers:
        exact.setdefault(norm(row['title']), []).append(row)
    matches = []
    for path in sorted((ROOT / 'research-wiki/papers').glob('*.md')):
        local = yaml.safe_load(path.read_text().split('---', 2)[1])
        title, authors = local['title'], set(map(norm, local.get('authors', [])))
        arxiv = str(local['external_ids']['arxiv'])
        found = exact.get(norm(title), [])
        id_matches = [row for row in papers if arxiv in row.get('arxiv_ids', [])]
        candidates = []
        if not found:
            lt = set(re.findall(r'[a-z0-9]+', title.lower()))
            for row in papers:
                common = authors & set(map(norm, row['authors']))
                rt = set(re.findall(r'[a-z0-9]+', row['title'].lower()))
                jaccard = len(lt & rt) / max(1, len(lt | rt))
                if jaccard < .18 and len(common) < 2:
                    continue
                ratio = difflib.SequenceMatcher(None, norm(title), norm(row['title'])).ratio()
                if ratio < .48 and len(common) < 2:
                    continue
                score = ratio + .15 * min(len(common), 4)
                candidates.append({'record': row, 'title_similarity': round(ratio, 4),
                                   'shared_authors': sorted(common), 'score': round(score, 4)})
            candidates.sort(key=lambda x: x['score'], reverse=True)
        matches.append({'file': str(path.relative_to(ROOT)), 'title': title,
                        'arxiv': arxiv, 'authors': local.get('authors', []),
                        'exact_matches': found, 'identifier_matches': id_matches,
                        'candidates': candidates[:3]})
    return matches


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    specs = []
    for venue in ['iclr', 'icml', 'neurips']:
        for kind in ['orals-posters', 'abstracts']:
            name = f'{venue}-2026-{kind}.json'
            cache = SHARED / 'neurips-2026-index' / name if venue == 'neurips' else None
            specs.append((name, f'https://{venue}.cc/static/virtual/data/{name}', cache))
    for volume in ['2026.acl-long', '2026.acl-short', '2026.findings-acl']:
        specs.append((volume + '.xml', f'https://aclanthology.org/volumes/{volume}.xml', None))
    csv_url = 'https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/export?format=csv&gid=943432490'
    specs.append(('emnlp-2026-schedule.csv', csv_url,
                  SHARED / 'emnlp-2026-availability-20261014/official_schedule_csv.csv'))
    sources = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for future in concurrent.futures.as_completed([pool.submit(download, s) for s in specs]):
            try:
                result = future.result()
            except Exception as error:
                result = {'error': str(error)}
            sources.append(result)
            print(json.dumps({k: v for k, v in result.items() if k in ['name', 'mode', 'bytes', 'error']}, ensure_ascii=False), flush=True)
    (OUT / 'sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2))
    good = {s['name']: s for s in sources if 'path' in s}
    papers, errors = [], []
    for venue in ['iclr', 'icml', 'neurips']:
        source = good.get(f'{venue}-2026-orals-posters.json')
        if source:
            try:
                papers += miniconf(venue.upper(), source, good.get(f'{venue}-2026-abstracts.json'))
            except Exception as error:
                errors.append({'venue': venue, 'error': str(error)})
    for volume, track in [('2026.acl-long', 'main-long'), ('2026.acl-short', 'main-short'), ('2026.findings-acl', 'Findings')]:
        if volume + '.xml' in good:
            try:
                papers += anthology(good[volume + '.xml'], track)
            except Exception as error:
                errors.append({'volume': volume, 'error': str(error)})
    if 'emnlp-2026-schedule.csv' in good:
        papers += emnlp(good['emnlp-2026-schedule.csv'])
    with (OUT / 'papers.jsonl').open('w') as f:
        for paper in papers:
            f.write(json.dumps(paper, ensure_ascii=False) + '\n')
    matches = match(papers)
    (OUT / 'mopd-matches.json').write_text(json.dumps(matches, ensure_ascii=False, indent=2))
    from collections import Counter
    summary = {'date': '2026-10-16', 'coverage': dict(Counter(p['venue'] + ':' + p['track'] for p in papers)),
               'total_records': len(papers), 'local_papers': len(matches), 'errors': errors,
               'exact_matches': [{'title': m['title'], 'venues': [(x['venue'], x['track'], x['decision'], x['paper_id']) for x in m['exact_matches']]} for m in matches if m['exact_matches']]}
    (OUT / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--search', help='Search the downloaded index without downloading again')
    parser.add_argument('--venue', choices=['ICLR', 'ICML', 'NEURIPS', 'ACL', 'EMNLP'])
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    if args.search:
        terms = re.findall(r'[a-z0-9]+', args.search.lower())
        if not terms:
            parser.error('search needs at least one searchable term')
        count = 0
        with (OUT / 'papers.jsonl').open() as stream:
            for line in stream:
                row = json.loads(line)
                text = clean(' '.join([row['title'], row['abstract'], *row['authors']])).lower()
                words = set(re.findall(r'[a-z0-9]+', text))
                if args.venue and row['venue'] != args.venue:
                    continue
                if all(term in words for term in terms):
                    count += 1
                    if count <= args.limit:
                        print(json.dumps({k: row[k] for k in ['venue', 'track', 'decision', 'paper_id', 'title', 'paper_url', 'source_url']}, ensure_ascii=False))
        print(json.dumps({'total_matches': count, 'shown': min(count, args.limit)}))
    else:
        main()
