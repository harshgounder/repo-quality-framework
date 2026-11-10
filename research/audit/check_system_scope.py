#!/usr/bin/env python3
"""Describe recorded system-example and specialization status, not actual coverage."""
import csv
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
for path in ('research/v2/systems/capability-catalog.csv','research/v2/systems/stress-cases.csv','research/v2/systems/compound-research-cells.csv','research/v2/specialization/ecosystem-profiles.csv'):
    with (ROOT/path).open(newline='',encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
    print(path, 'rows=',len(rows),'status=',dict(Counter(x['status'] for x in rows)))
    if rows and 'purpose' in rows[0]:print('  distinct recorded purpose text:',len({x['purpose'] for x in rows}))
print('These are recorded statuses and seed descriptions; they do not measure all research or the space of possible systems.')
