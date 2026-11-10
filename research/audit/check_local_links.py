#!/usr/bin/env python3
"""Report relative Markdown link targets; fenced code, anchors and external URLs excluded."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[2]
files=[p for p in ROOT.rglob('*.md') if '.git' not in p.parts]
missing=[];checked=0
for path in files:
    text=re.sub(r'```.*?```','',path.read_text(encoding='utf8'),flags=re.S)
    for raw in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
        target=raw.strip().split(' ',1)[0].strip('<>'); parts=urlsplit(target)
        if parts.scheme or target.startswith('#'): continue
        local=unquote(parts.path)
        if local:
            checked+=1
            if not (path.parent/local).exists():missing.append((str(path.relative_to(ROOT)),target))
print('Markdown files:',len(files),'relative targets checked:',checked,'missing:',len(missing))
for source,target in missing:print(source,'->',target)
print('Anchor fragments, external URLs, reference-style links, fenced code and images were not checked.')
if missing:raise SystemExit(1)
