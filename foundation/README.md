# Evidence graph: initial prototype

This is a small working extension to the research model—not a complete corpus, crawler, assessment engine, universal standard or replacement for existing CSVs and logs. Sources identify where a claim came from; entities can represent arbitrary observations, components, changes, incidents, documents or other things; each directed assertion connects two entities to a specific source, locator, evidence status and qualification. Types and predicates are open strings, so the model does not privilege a fixed system family. Source-reported, independently checked, reproduced, disputed, inaccessible and unknown are distinct; their meaning is scoped to the assertion, not the whole case.

## Try it

Requires Python 3 and its built-in SQLite library. From the repository root:

```sh
python foundation/store.py /tmp/repo-quality-evidence.sqlite foundation/examples/clickhouse.json
python -m unittest discover -s foundation/tests -v
```

Use a fresh path or a database created by this tool. The loader preserves IDs and fails on conflicting reimports; identical snapshots can be imported again. A failed import rolls back as one transaction. Foreign keys reject links to missing entities or sources. The database is local and is not committed; the example JSON is a compact, manually curated, source-attributed seed. See [the original trace](../research/discovery/2026-11-10-open-world/clickhouse-trace.md) for limits. One example cannot demonstrate broad coverage.

## Scope and next steps

SQLite's constraints support this small pilot, while `docs/research-model-v2.md` remains the wider model of sources, routes, queries, runs, evidence and matrix cells. The bounded adapter below can prepare the earlier two-page issue-search CSV snapshot as unreviewed leads; it does not fetch issue bodies or promote reports to findings. It writes a new output file and refuses to overwrite an existing one:

```sh
python foundation/prepare_issue_leads.py research/discovery/2026-11-10-scale-tranche /tmp/repo-quality-leads.json
python foundation/store.py /tmp/repo-quality-evidence.sqlite /tmp/repo-quality-leads.json
```

Its batch ID is specific to that recorded input set, so do not use it for unrelated or changed snapshots. The old CSVs and run manifests remain the provenance records: the graph does not copy issue state, timestamps, labels or full search-run metadata. Its current URL deduplication keeps only the first discovery route; this batch contains no duplicate URLs, but a later multi-run importer must preserve every route and check per-run counts. It does not verify that the input files remain identical to the original snapshot.

The prototype does **not** yet store source snapshots or detailed event chronology, provide full text search, crawl a platform, keep immutable revision history, implement multi-reviewer workflows, track legal rights or licenses, deduplicate canonical entities, evaluate claims, run tests, or render end-to-end cases. Model versions and more granular source/observation/reviewer/contradiction/provenance relations must be designed before production use. The source `version` field is descriptive text, not a verified immutable snapshot. `independently_checked` is a label requiring human evidence and does not itself prove independence. Do not use this tool to publish a score or unvalidated quality gate.

Read [the prior-art inventory](../research/prior-art/2026-11-11-projects.md) and [open-world direction](../research/discovery/2026-11-10-open-world/atlas-and-failure-corpus.md) for source limitations, rights and the much larger continuing research scope.

A separate reviewer rechecked the ownership guard with an unrelated SQLite database and its existing row remained intact. The application ID is an ownership marker, not a security boundary; table definitions are not checked for a foreign database that happens to carry the same markers. The loader enforces no-update-on-reimport, not immutability against direct SQL edits.
