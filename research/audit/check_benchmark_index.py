#!/usr/bin/env python3
"""Count exact index-field overlaps; never treat URL equality as identity proof."""
import csv
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
with (ROOT/'research/v2/benchmarks/candidate-index-leads.csv').open(newline='',encoding='utf-8-sig') as f:
    rows=list(csv.DictReader(f))
print('rows:',len(rows))
for key in ('benchmark_name_group','primary_paper_or_reference_url','code_repository_url','dataset_url'):
    values=[r[key].strip() for r in rows]; present=[v for v in values if v]; counts=Counter(present)
    print(f'{key}: present={len(present)} missing={len(values)-len(present)} distinct_exact={len(counts)} repeated_values={sum(n>1 for n in counts.values())} rows_in_repeats={sum(n for n in counts.values() if n>1)}')
print('Exact strings are not canonical identities; missing fields do not prove missing artifacts.')
