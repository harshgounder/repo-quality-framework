#!/usr/bin/env python3
"""Read declared subtree metadata; never execute upstream code."""
import csv, datetime, json, subprocess
from pathlib import Path
from urllib.parse import quote
ROOT = Path(__file__).resolve().parent
SOURCES = [('torvalds/linux','Documentation/devicetree/bindings',('.yaml','.yml')),
           ('FFmpeg/FFmpeg','tests/fate',('.mak',)),
           ('ros2/design','articles',('.md',)),
           ('RTEMS/rtems-central','spec',('.yaml','.yml'))]
def api(path):
    p=subprocess.run(['gh','api',path],capture_output=True,text=True)
    if p.returncode: raise RuntimeError(p.stderr.strip()[:500])
    return json.loads(p.stdout)
rows=[]; runs=[]
for project,subtree,suffixes in SOURCES:
    run={'project':project,'subtree':subtree,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'commit':'','subtree_tree_sha':'','api_truncated':'','tree_entries':'','retained':'','status':'error','error':''}
    try:
        commit=api(f'repos/{project}/commits/HEAD'); sha=commit['sha']; tree=commit['commit']['tree']['sha']
        run['commit']=sha
        for part in subtree.split('/'):
            listing=api(f'repos/{project}/git/trees/{tree}')
            matches=[x for x in listing['tree'] if x['path']==part and x['type']=='tree']
            if len(matches)!=1: raise RuntimeError(f'subtree component not uniquely found: {part}')
            tree=matches[0]['sha']
        run['subtree_tree_sha']=tree
        listing=api(f'repos/{project}/git/trees/{tree}?recursive=1')
        run['api_truncated']=listing.get('truncated','unknown'); run['tree_entries']=len(listing['tree'])
        start=len(rows)
        for item in listing['tree']:
            if item['type']!='blob' or not item['path'].lower().endswith(suffixes): continue
            path=f'{subtree}/{item["path"]}'
            rows.append({'source_project':project,'commit':sha,'path':path,'blob_sha':item['sha'],
                         'source_url':f'https://github.com/{project}/blob/{sha}/{quote(path, safe="/")}',
                         'triage_status':'unreviewed source-file lead'})
        run['retained']=len(rows)-start; run['status']='ok'
    except (RuntimeError,ValueError,KeyError,TypeError) as e: run['error']=str(e)
    runs.append(run); print(project,run['status'],run['retained'],run['error'],flush=True)
for name,data in [('source-file-leads.csv',rows),('source-file-runs.csv',runs)]:
    if data:
        with (ROOT/name).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=data[0].keys(),lineterminator='\n');w.writeheader();w.writerows(data)
