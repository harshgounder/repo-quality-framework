#!/usr/bin/env python3
"""Index JSONL record types without copying private message or tool-output bodies."""
import collections
import hashlib
import json
import sys
from pathlib import Path
if len(sys.argv) < 2:
    raise SystemExit('usage: python index_session_structure.py SESSION.jsonl [SESSION.jsonl ...]')
for arg in sys.argv[1:]:
    p=Path(arg); counts=collections.Counter(); tools=collections.Counter(); sha=hashlib.sha256(); size=0; bad=[]
    with p.open('rb') as f:
        for n,line in enumerate(f,1):
            sha.update(line);size+=len(line)
            try: obj=json.loads(line)
            except (json.JSONDecodeError,UnicodeDecodeError): bad.append(n);continue
            payload=obj.get('payload') or {}; typ=obj.get('type','?'); sub=payload.get('type',''); role=payload.get('role','')
            counts[(typ,sub,role)]+=1
            item=payload.get('item') or {}
            if typ=='event_msg' and sub=='item_completed' and item.get('type')=='McpToolCall':
                tools[(item.get('server','?'),item.get('tool','?'))]+=1
    print(f'file={p.name} bytes_read={size} lines={n if size else 0} sha256_of_read_stream={sha.hexdigest()} invalid_json_lines={bad}')
    for key,num in sorted(counts.items()): print('record', '/'.join(x for x in key if x), num)
    for (server,tool),num in tools.most_common():print('tool_event',server,tool,num)
    print('Counts are record counts, not verified distinct research operations or content reviews; live files can grow.')
