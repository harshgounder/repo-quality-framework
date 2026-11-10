#!/usr/bin/env python3
"""Report structural integrity of the v2 research snapshot; semantics need review."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read(path):
    with (ROOT / path).open(newline='', encoding='utf-8-sig') as stream:
        return list(csv.DictReader(stream))

c = read('research/v2/campaigns.csv')
q = read('research/v2/query-bank.csv')
p = read('research/v2/planned-cells.csv')
cq = read('research/v2/cell-queries.csv')
cr = read('research/v2/cell-runs.csv')
l = read('research/search-ledger.csv')
b = read('research/v2/benchmarks/candidate-index-leads.csv')

def ids(rows, key):
    return {r[key] for r in rows if r[key]}

def duplicate(rows, key):
    return {k: v for k, v in Counter(r[key] for r in rows if r[key]).items() if v > 1}

for name, rows, key in [('campaigns',c,'campaign_id'),('queries',q,'query_id'),('cells',p,'cell_id'),('ledger',l,'entry_id'),('index rows',b,'inventory_row_id')]:
    print(f'{name}: {len(rows)} rows; duplicate {key}: {duplicate(rows,key)}')
for name, rows, key, valid in [('query campaign',q,'campaign_id',ids(c,'campaign_id')),('cell campaign',p,'campaign_id',ids(c,'campaign_id')),('cell primary query',p,'query_id',ids(q,'query_id')),('cell-query cell',cq,'cell_id',ids(p,'cell_id')),('cell-query query',cq,'query_id',ids(q,'query_id')),('cell-run cell',cr,'cell_id',ids(p,'cell_id')),('cell-run ledger',cr,'run_id',ids(l,'entry_id'))]:
    missing = sorted(ids(rows,key) - valid)
    print(f'{name}: {len(missing)} distinct missing values: {missing}')
print('cell-query pair duplicates:', {str(k):v for k,v in Counter((x['cell_id'],x['query_id']) for x in cq).items() if v>1})
print('cell-run triple duplicates:', {str(k):v for k,v in Counter((x['cell_id'],x['run_id'],x['relationship']) for x in cr).items() if v>1})
print('normalized cell status:', dict(Counter(x['status'].split(':',1)[0] for x in p)))
print('query languages:', dict(Counter(x['language'] for x in q)))
print('benchmark origin:', dict(Counter(x['source_index'] for x in b)))
print('legacy primary cell/run pairs absent from join table:')
join_pairs = {(x['cell_id'], x['run_id']) for x in cr}; ledger_ids=ids(l,'entry_id')
for x in p:
    v=x['run_id']
    if v and (x['cell_id'], v) not in join_pairs:
        print(f"  {x['cell_id']}: {v}; exact ledger ID: {v in ledger_ids}")
print('NOTE: join-table absence does not by itself establish a missing search; investigate provenance and compatibility fields.')
