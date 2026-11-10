#!/usr/bin/env python3
"""Prepare one recorded GitHub search batch for the evidence graph as leads."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

BATCH = 'github-issue-scale-2026-11-10'

def stable(prefix, value):
    return prefix + '-' + hashlib.sha256(value.encode('utf-8')).hexdigest()

def convert(rows, batch):
    sources, entities, assertions, seen = [], [{'id':batch,'kind':'discovery-batch','label':batch}], [], {}
    for row in rows:
        url = row['url']; signature = (row['title'], row['source_project'], row['issue_number'])
        if url in seen:
            if seen[url] != signature: raise ValueError(f'conflicting records for {url}')
            continue
        seen[url] = signature
        identity = stable('issue', url); source = stable('source', batch + '\n' + url)
        sources.append({'id':source,'url':url,'kind':'issue-search-result',
                        'version':f'{batch}; observed {row.get("_retrieved_utc", "unknown")} (mutable)'})
        entities.append({'id':identity,'kind':'issue-search-lead','label':row['title']})
        assertions.append({'id':stable('lead',batch + '\n' + url),'subject':batch,'predicate':'discovered_lead',
            'object':identity,'source':source,'locator':f'CSV {row.get("_input_file", "unknown")}; query {row.get("run_query", "unknown")}',
            'evidence_status':'lead','note':f'Unreviewed search metadata; {row["source_project"]} issue {row["issue_number"]}; not an independently verified defect.'})
    return {'sources':sources,'entities':entities,'assertions':assertions}

def read_batch(directory):
    rows=[]
    for page in (1,2):
        runfile=directory/f'run-manifest-page{page}.csv'
        with runfile.open(encoding='utf-8',newline='') as f:
            runs={r['project']:r for r in csv.DictReader(f)}
        path=directory/f'issue-leads-page{page}.csv'
        with path.open(encoding='utf-8',newline='') as f:
            for row in csv.DictReader(f):
                run=runs[row['source_project']]
                if run['status'] != 'ok': raise ValueError('record refers to unsuccessful run')
                row['_retrieved_utc']=run['retrieved_utc']; row['_input_file']=path.name
                rows.append(row)
    return rows

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch_dir',type=Path);p.add_argument('output',type=Path)
    a=p.parse_args();data=convert(read_batch(a.batch_dir), BATCH)
    with a.output.open('x',encoding='utf-8') as f: json.dump(data,f,ensure_ascii=False,indent=2)
    print(f'{len(data["assertions"])} unreviewed issue leads prepared')

if __name__=='__main__': main()
