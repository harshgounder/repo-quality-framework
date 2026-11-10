#!/usr/bin/env python3
"""Summarize exact/status-prefix source records; no source validity inference."""
import collections
import csv
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
ROOT=Path(__file__).resolve().parents[2]
def read(path):
    with (ROOT/path).open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def normalize(url):
    p=urlsplit(url.strip())
    return urlunsplit((p.scheme.lower(),p.netloc.lower(),p.path.rstrip('/'),p.query,p.fragment))
for path,namekey,urlkey in [('research/source-register.csv','name','first_party_or_discovery_url'),('research/v2/source-routes.csv','venue','url')]:
    rows=read(path); names=collections.Counter(x[namekey].strip() for x in rows);urls=collections.defaultdict(list)
    for x in rows:urls[normalize(x[urlkey])].append(x[namekey])
    duplicate_urls={k:v for k,v in urls.items() if len(v)>1}
    print(path,'rows',len(rows),'unique_exact_labels',len(names),'duplicate_normalized_url_groups',len(duplicate_urls))
    for url,labels in duplicate_urls.items():print(' ',url,labels)
    if path.endswith('source-register.csv'):
        c=collections.Counter(x['verification_state'].strip().lower().split(';')[0] for x in rows)
        print(' status first-phrase exact:',{k:c[k] for k in ('seed-unverified','search-lead','prior-lead')})
    else:print(' candidate-prefix statuses:',sum(x['verification_state'].strip().lower().startswith('candidate') for x in rows))
print('Counts describe rows and free-text labels, not actual access, distinct sources, or evidence coverage.')
