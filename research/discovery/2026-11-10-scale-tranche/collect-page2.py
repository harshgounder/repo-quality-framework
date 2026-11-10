#!/usr/bin/env python3
"""Collect a bounded, predeclared second page of public GitHub issue-search metadata."""
import csv, datetime, json, subprocess, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = 2
PROJECTS = ['llvm/llvm-project','godotengine/godot','zephyrproject-rtos/zephyr','bitcoin/bitcoin','opencv/opencv','OSGeo/gdal','eclipse-sumo/sumo','grafana/grafana','ClickHouse/ClickHouse']
rows, runs, seen = [], [], set()
for project in PROJECTS:
    query = f'repo:{project} is:issue label:bug'
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    cmd = ['gh','api','--method','GET','search/issues','-f',f'q={query}',
           '-f','sort=updated','-f','order=desc','-f','per_page=100','-f',f'page={PAGE}']
    proc = subprocess.run(cmd, text=True, capture_output=True)
    run = {'project':project,'retrieved_utc':started,'query':query,'sort':'updated',
           'order':'desc','per_page':100,'page':PAGE,'status':'error','api_total_count':'',
           'incomplete_results':'','returned':'','retained':'','error':''}
    if proc.returncode:
        run['error'] = proc.stderr.strip()[:500]
    else:
        try:
            payload = json.loads(proc.stdout)
            items = payload['items']
            run.update(status='ok',api_total_count=payload.get('total_count',''),
                       incomplete_results=payload.get('incomplete_results',''),returned=len(items))
            before = len(rows)
            for item in items:
                url = item['html_url']
                if url in seen: continue
                seen.add(url)
                rows.append({'source_project':project,'issue_number':item['number'],'url':url,
                             'title':item['title'],'state':item['state'],
                             'created_at':item['created_at'],'updated_at':item['updated_at'],
                             'labels':' | '.join(x['name'] for x in item['labels']),
                             'triage_status':'unreviewed search lead', 'run_query':query})
            run['retained'] = len(rows)-before
        except (ValueError,KeyError,TypeError) as err:
            run['status']='parse-error'; run['error']=str(err)
    runs.append(run)
    print(project, run['status'], run['returned'], run['retained'], flush=True)
    time.sleep(0.3)
for name, records in [(f'issue-leads-page{PAGE}.csv',rows),(f'run-manifest-page{PAGE}.csv',runs)]:
    if records:
        with (ROOT/name).open('w',encoding='utf-8',newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=records[0].keys(), lineterminator="\n")
            writer.writeheader(); writer.writerows(records)
