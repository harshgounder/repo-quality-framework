#!/usr/bin/env python3
"""Check that the integrity report surfaces three planted structural faults."""
import csv
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [
    'research/audit/check_integrity.py',
    'research/v2/campaigns.csv',
    'research/v2/query-bank.csv',
    'research/v2/planned-cells.csv',
    'research/v2/cell-queries.csv',
    'research/v2/cell-runs.csv',
    'research/v2/benchmarks/candidate-index-leads.csv',
    'research/search-ledger.csv',
]
with tempfile.TemporaryDirectory(prefix='repo-quality-checker-') as directory:
    tmp=Path(directory)
    for name in FILES:
        target=tmp/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/name,target)
    campaigns=tmp/'research/v2/campaigns.csv'
    with campaigns.open(newline='',encoding='utf8') as f:
        original=list(csv.reader(f))
    with campaigns.open('a',newline='',encoding='utf8') as f:
        csv.writer(f,lineterminator='\n').writerow(original[1])
    with (tmp/'research/v2/cell-runs.csv').open('a',newline='',encoding='utf8') as f:
        csv.writer(f,lineterminator='\n').writerow(['PC999','NONEXISTENT-RUN','controlled-fixture','synthetic'])
    run=subprocess.run(['python',str(tmp/'research/audit/check_integrity.py')],capture_output=True,text=True,check=True)
    checks={
        'duplicate campaign': "duplicate campaign_id: {'C01': 2}" in run.stdout,
        'missing cell': "'PC999'" in run.stdout,
        'missing run': "'NONEXISTENT-RUN'" in run.stdout,
    }
    print('synthetic fault detection:',checks)
    if not all(checks.values()):
        raise SystemExit('checker missed a planted fixture fault')
