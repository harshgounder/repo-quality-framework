# Evidence foundation initial implementation plan

**Goal:** Make a small, locally usable, validated starting point for linking observations, artifacts and claims without replacing the existing research model.

**Architecture:** Versioned SQLite schema stores independently identified sources, arbitrary-type entities and source-attributed assertions between them. A Python standard-library loader atomically imports an explicit JSON snapshot; it rejects dangling references, invalid statuses and conflicting reimports, and enables foreign keys on every connection. Existing CSVs and historical artifacts remain unchanged. A qualified worked example derives from the ClickHouse audit, not from inferred fixes.

**Tech:** Python 3 standard library and SQLite. **Spec:** `research/discovery/2026-11-10-open-world/atlas-and-failure-corpus.md` and `docs/research-model-v2.md`.

- [x] Write tests for an idempotent import, conflicting record rollback, missing references and invalid status.
- [x] Implement schema and loader; use open entity/relation vocabularies and per-assertion evidence statuses. Never upgrade source narratives into reproduced findings.
- [x] Seed a bounded, source-attributed example with an unmerged proposal and a distinct merged PR, plus the documented test artifact; preserve open questions.
- [x] Document usage, operational limitations, relationship to the existing model and a research-prior-art comparison; independently verify counts, example links and tests.

**Review focus:** open vocabularies, unknown evidence, contradictions, same-ID differences, transactional safety, missing sources, independently verified vs source-reported events. This is a first foundation, not a finished ingestion platform, migration, universal score or coverage claim.

A bounded adapter now imports the earlier issue-search snapshot as unreviewed leads; this is not a general source-harvesting system.
