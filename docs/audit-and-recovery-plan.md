# Repository quality project: audit and recovery plan

**Prepared:** 2026-11-10. **State:** plan ready; execution checkpoints below are open.
**Purpose:** establish what the previous execution actually did, expose unsupported or abandoned work, and direct a new execution model toward a broadly applicable, evidence-backed quality framework.

## 1. What this plan responds to

The user requested a general research framework for all kinds of systems and work, with wide and deep discovery across platforms, regions, roles, sources, research, obscure failures, raters, standards, benchmarks, efficiency, and specialized engineering. The user's examples are entry points, not a closed list. The Computer System Atlas supplies a substantial source of primitives, engines, product operations, and interactions. A separate role list remains pending.

The goal is to make high-quality engineering obligations discoverable and testable in context. A repository may be the entry point, while the system's actual quality depends on implementation, users, runtime, operators, devices, organizations, and surrounding services. A badge, static scan, generic checklist, passing test, or LLM verdict cannot prove the whole system is fit for purpose.

## 2. Audit findings established so far

These are bounded observations, not a completed audit of every session turn, source, or claim. Paths refer to the existing `repo-quality-framework` repository.

| ID | Finding and evidence | Assessment | Unresolved check |
|---|---|---|---|
| A01 | `docs/integrated-research-roadmap.md` §1 and §3 require Atlas integration and several deep contrasting investigations; `docs/atlas-context-recovery.md` explicitly identifies missing specialist concepts; the browser example describes itself as illustrative. | Major planned work remains outstanding. | Inventory every Atlas request and response, each system artifact, and evidence needed by each promised pilot. |
| A02 | `research/v2/query-bank.csv`: 344 rows, 334 labelled English; all 10 rows labelled other languages are marked `planned; not executed`. A Portuguese Reddit thread was separately opened. | Planned multilingual search did not progress; that does not mean all non-English sources were untouched. | Audit ledger and native-platform evidence separately; inspect source language, not just query-bank labels. |
| A03 | `research/v2/campaigns.csv`: 11 exact `queued` statuses: C01, C04–C09, C12, C15, C16, C18. They include accessibility/design, operations, safety/privacy, role responsibilities, cleanliness and ecosystem-specific work. | Significant breadth is still queued while C22–C27 concentrate on AI/research evaluation. C01's status conflicts with the separate static estimator inspection and requires reconciliation. | For each queued campaign, compare its status with existing search logs and evidence; distinguish genuinely unstarted from stale status. |
| A04 | `research/v2/benchmarks/candidate-index-leads.csv`: 233 discovery-only and 379 survey-index-only rows; all 612 have unresolved identity. | Counts represent imported leads; source reports do disclose this, but the README visual can suggest a more mature inventory. | Audit selected rows against original index, paper, task, dataset and repo; measure identity/verification coverage. |
| A05 | README's diagram includes source → claim → practice; `docs/research-model-v2.md` says results, sources and claims still need distinct IDs. | The diagram blends implemented joins with intended future relations. | Produce a field-by-field implementation inventory and demonstrate traceability with actual records. |
| A06 | `research/v2/integrity-and-migration.md` records swapped follow-ups, nonexistent fetch IDs, an unverified reconstructed query, and incomplete reconciliation. C26/C27 include retrospective material with missing details. | Historical provenance cannot be treated as fully verified. | Compare a declared sample against original transcripts/tool output; preserve unrecoverable fields as unknown. |
| A07 | Data check found no missing referenced campaign, cell, query, or run/ledger IDs in six explicit foreign-key comparisons. | These reference checks pass for the current CSV snapshot. | They do not establish that a query actually ran, a source supports a claim, or a link has the correct meaning. |
| A08 | Three failure-card sources were reopened: React Native Web issue #1817 reports the modal behavior; Redis PR #4143 describes cancellation loss and its reported tests; VueUse PR #5574 describes stale-success behavior after a prior error-path guard. | The checked core descriptions are supported by their linked source narratives. They were not independently reproduced. | Verify actual patch/test code, version, merge state, and remaining card claims through a declared sample and then the complete high-impact queue. |
| A09 | 133 planned cells: 109 thin, 21 queued, two `no evidence found`, one static-source-only, zero saturated, using status-prefix grouping of free text. | Counts describe the selected cells, not coverage of the whole research universe. | Audit cell definitions, scope, query/run mappings, selection bias and status semantics. |

Sources for A08: https://github.com/necolas/react-native-web/issues/1817 ; https://github.com/redis/go-redis/pull/4143 ; https://github.com/vueuse/vueuse/pull/5574 . Opening a report is not the same as reproducing its claimed behavior.

## 3. Non-negotiable execution rules

1. Read this document, `AGENTS.md`, `RESEARCH_STATE.md`, `docs/integrated-research-roadmap.md`, `docs/atlas-context-recovery.md`, and `research/v2/integrity-and-migration.md` before work. Read the actual relevant content, not only headings.
2. Preserve existing files and historical statements. Add corrections with source, timestamp, changed claim, reason, and links to superseded records. Do not silently rewrite history.
3. Use `unknown`, `planned`, `executed`, `opened`, `appraised`, `independently checked`, `reproduced`, `disputed`, and `inaccessible` for what they actually mean. A search result is a lead, a record is not an independently verified fact, and a claimed test result is not our reproduction.
4. Never fabricate precise queries, dates, counts, test outcomes, source reads, agent reviews, authorship, benchmarks, or external observations. Missing raw context is an explicit audit result.
5. Keep public-source descriptions separate from personal account data. No posting or contacting others without separate authorization. Follow source access terms; do not bypass authentication or execute untrusted repositories without appropriate isolation.
6. The roadmap is a research plan, not proof that a universal system, role, source universe or future technique has been fully enumerated. Use an expandable model, prioritized samples, counterexamples, and measurable coverage.
7. Record time, route, exact query if available, filter, window, selected/opened/retained counts if actually known, version, source locator, claim and competing evidence. Unknown values remain unknown.
8. Every checkpoint has an evidence manifest and a checker. A checker must report its identity, exact scope, evidence inspected, findings, limitations, and pass/fail/rework. Separate worker and checker when independent review is available; if not, mark self-review explicitly and leave independent review open. No model may certify its own work as independent.
9. No score or mandatory gate becomes authoritative until a context-specific validation study covers false alarms, misses, burden, exceptions, governance, and outcomes. A candidate can be documented before validation as `proposed/untested`.
10. The user's pending role list is not assumed to exist. Continue independent work; when supplied, preserve its entries and integrate them without replacing it with an invented list.

## 4. Work products and ownership

Create the following under the repository. Names may be adapted if the existing schema already serves the exact purpose; document that decision.

| Artifact | Responsibility |
|---|---|
| `research/audit/session-inventory.md` | Locate the exact session and all child records; identify accessible ranges, gaps, timestamps, and constraints; no private content published without review. |
| `research/audit/requirements-trace.csv` | One row per atomic user/roadmap obligation; original locator, scope, artifact, actual evidence, state, gap, owner, next action. |
| `research/audit/claim-audit.csv` | Claim ID, exact claim and locator, source/version, evidence, verification method/result, discrepancy, severity, remediation, reviewer. |
| `research/audit/coverage-audit.md` | Actual source, geography, language, system, artifact, role, lifecycle and method coverage; sampling method, denominator and blind spots. |
| `research/audit/record-integrity.md` | Reproducible structural checks, semantic sample, mismatches, data snapshot/commit and repair log. |
| `research/v2/systems/atlas-intake/` | Traceable source-span inventory and candidate entities/relations with provenance and unresolved uncertainty. |
| `research/investigations/` | Complete, contrasting system investigations and evidence manifests. |
| `research/audit/reviewer-ledger.csv` | Checkpoint, artifact revision, checker identity/method, scope, findings, disposition, date and recheck result. |
| `RESEARCH_STATE.md` | Durable checkpoint, unresolved blockers, exact next step, artifact pointers, commit/remote state. |

All IDs must be stable. Each row must name its source locator and assessment unit. A field dictionary must define allowed states, date semantics, and unknown values before tooling or migration.

## 5. Checkpoint sequence

### CP0 — Freeze baseline and recover session evidence

**Tasks**
- Record commit, branch, remote and working-tree state; inventory tracked/untracked files without overwriting user work. Snapshot CSV row counts and hashes for comparison.
- Locate the exact Codex session and any child-agent transcripts using available thread tools or local session discovery. Enumerate candidates, ID, source, timestamp range, pages, access failures, and which records were read. Read user messages and relevant assistant/tool outputs in bounded chunks; preserve original records read-only.
- Compare the raw conversation with the visible summary, Atlas shared conversation and pasted attachment. Log missing turns, oversized tool output and unsupported assertions; never represent a summary as a full transcript.
- Check Exa, Parallel, browser/X, native APIs, GitHub and research-source access. Record actual test results, not historical availability. No posting.

**Pass:** baseline and session inventory identify exact sources and inaccessible ranges; no guessed history. **Checker:** different reviewer samples at least five user instructions and five execution claims against their original records; if raw session is unavailable, mark this checkpoint partial and proceed with repo audit.

### CP1 — Build the requirements and abandonment register

**Tasks**
- Extract atomic obligations from user turns, Atlas, role-intake request, roadmap, failure-pattern handoff, and later corrections. Preserve source span and relationship to prior requests.
- Link every obligation to concrete artifact(s), execution evidence, actual status, owner, gap, next action, and acceptance condition. Include original rater and estimator requests, professional roles, source matrix, subtle failure checks, efficiency, specialized systems, latest research, benchmarks, GitHub, and continuity.
- Classify `met`, `partial`, `not started`, `contradicted`, `blocked`, `unknown`, or `superseded`; a planned document does not by itself satisfy an execution obligation. Document when no evidence is found after a defined search.

**Pass:** every located user instruction has an entry or explicit explanation of grouping; conflicting instructions have chronology and resolution. **Checker:** independently reconstruct requirements from at least three separated transcript windows, including one after context loss; reconcile missing or merged items.

### CP2 — Audit truth, provenance and data integrity

**Tasks**
- Re-run the six foreign-key checks already sampled, plus duplicates, duplicate aliases, orphan records, impossible status transitions, unlinked cells, multi-valued fields, dangling Markdown links, and free-text status variants. Save commands and complete output; avoid reporting only pass counts.
- Fix only verified clerical/data issues, with before/after records and rationale. Reconcile C01's `queued` status with the static pre.dev inspection; do not assume that inspection completed the campaign.
- Select an explicitly documented initial audit sample: at least 24 claims, stratified across evaluator/standards, failure cards, systems/performance, AI/lab, benchmark, social/community, recent and older material. Include at least four high-impact numerical claims, four negative/access claims, three retrospective runs, three random selections with recorded seed, and at least three contradictory or weak-evidence leads. These categories may overlap; publish the exact selection before checking.
- For each sample: trace original assertion → cited locator and edition → underlying source/patch/data → original run/output where available → affected cells and downstream summaries. Record supported, partly supported, contradicted, unavailable or cannot assess; do not treat missing raw logs as proof of fabrication.
- Expand to all claims that affect decisions or represent material facts; sample results do not certify unsampled material. Review high-severity discrepancies before continuing downstream synthesis.

**Pass:** structural report plus reproducible sample manifest and per-claim adjudications exist; unresolved discrepancies remain visible. **Checker:** independently retry at least six sampled claims including one numerical claim and one access failure; challenge at least one favorable conclusion. No generic “looks good” signoff.

### CP3 — Repair the research model and coverage accounting

**Tasks**
- Inventory implemented versus proposed records and relations. Include source identity/version, route, run, search result, claim, evidence locator, disagreement, assessment object, mechanism and practice. Show what currently exists and what is only conceptual.
- Map legacy v1 data to v2 only when identity and provenance are supported; keep unknowns and original rows. Add a field dictionary and normalized status vocabulary with a documented migration of existing free text, preserving originals.
- Define coverage with explicit denominators and independent axes: discoverable routes, attempted routes, accessible routes, screened sources, appraised claims, evaluated system nodes/edges, and benchmark identities. Record unselected regions and intersection cells. Do not use Cartesian-product size or source count as completed coverage.
- Include a worked trace from query to source to claim to component to candidate check, including disagreement, missing evidence and verification status.

**Pass:** checker can follow at least three distinct traces back and forward without relying on invented identifiers; a deliberately missing source remains unknown, and a multi-cell run does not duplicate result counts. **Checker:** schema and trace review by someone other than the author when available.

### CP4 — Integrate the Atlas and role responsibilities

**Tasks**
- Re-read the entire provided Atlas text and original prompts in bounded sections; record section/page/line spans. Check reading completeness against the source, not an existing summary.
- Extract concepts, data structures, algorithms, engines, components, interfaces, product flows, operations, people and responsibilities with source provenance. Normalize synonyms and keep alternatives; link entities as graph edges with evidence/confidence.
- Pilot both directions: primitive → implementation → subsystem → system outcome, and a user/operational outcome → workflow → components → primitives. Choose examples from distinct areas such as FFT/media, regex/parsing, and payments/reconciliation. Verify real dependencies in the system inspected; hypothetical edges remain labelled.
- Translate role families into decisions, artifacts, handoffs and outcomes without requiring one person per role. Incorporate every entry from the separate user list only after it is supplied.

**Pass:** independently sampled source spans map to entities or reasoned exclusions, both directional traces have direct evidence, and missing Atlas areas are visible. **Checker:** choose five source spans not selected by the worker and look for missed machinery or human workflows.

### CP5 — Rebuild and execute the source campaign

**Tasks**
- Expand source universe by host/service/instance/community/collection: global and regional forges, package registries, issue and patch trackers, X/Reddit and other social, Stack Exchange/HN/Lobsters, language/runtime/engine communities, forums, archives, standards, institutions, labs, conferences, manuals, postmortems, code/test suites, designers and operations communities.
- Record source identity, geography/language, scope, access, active state, retrieval route, ownership, version, primary/secondary role, result limitations and last checked. Do not treat public snippets as native-platform coverage.
- Generate task-specific queries across system × component × operation × stakeholder × failure/property × artifact × lifecycle × method × source/region/language. Include alternative terms, historical versions, failures, criticism, false positives and counterexamples. Validate translations with native sources where possible.
- Run a declared initial tranche that includes the existing queued non-English queries where feasible, direct specialist communities, and regional forges. Save query/run evidence, native route and filters. Access failures or unavailable language expertise become explicit queue items, not forced completions.

**Pass:** each selected cell has genuine executed operations and an evidence trail, or explicit inaccessible/unknown state; source claims are tied to actual opened material. **Checker:** choose five supposedly covered cells and reproduce discovery using recorded filters; identify at least two omitted venue families or explain why none surfaced in that bounded sample.

### CP6 — Deliver contrasting deep investigations

At minimum deliver four independently reviewable pilots, with exact scope selected and justified before searching:

1. **Specialist engine:** numerical/geometry, regex/parser, media codec or another underlying engine.
2. **Distributed user workflow:** payment, marketplace, mobility, maps or equivalent, including failure, recovery, human support and user experience.
3. **Low-level or physical system:** OS, compiler, firmware, device or safety-related system; distinguish simulation, hardware and certification evidence.
4. **Complex interactive product:** browser, game engine, media or accessibility-critical interface, spanning internal components and user behavior.

Each pilot must specify system boundary, workloads, threat/failure model, roles and lifecycle; concrete components and interfaces; source/standard/version and implementation/tests; real failure/counterexample; measurable properties and oracles; runtime and organizational evidence missing from source code; proposed checks with scope, false positives/negatives, costs and exceptions; and explicit unknowns. The user examples are illustrative and additional domains remain open.

**Pass:** each note has at least three distinct appropriate evidence types including an original implementation or test where accessible, a relevant standard/specification where available, and incident/research/independent counterevidence; exceptions are recorded, not fabricated. A reviewer can trace one finding to source and show a case where the proposed rule does not apply. **Checker:** domain-aware reviewer attempts to falsify one core claim per pilot and checks user/operational paths, not only source code.

### CP7 — Raters, standards and benchmarks

**Tasks**
- Audit the pre.dev script at its recorded pinned snapshot, then sample distinct rater families (weighted scores, badge, maturity rubric, conformance checker, community metrics and criticality estimator). Record input, implementation/version, formula, missing/N/A, data freshness, deployment, gaming, cost, independent validity and appropriate use.
- Resolve benchmark identities using original survey, pinned index, canonical paper, code/dataset, release version, task unit and aliases. Preserve merged/split records, uncertainty and HOW2BENCH appendix-to-analysis-unit discrepancy. Never count papers or study corpora as benchmark suites by default.
- Select a stratified, declared appraisal sample across repository maintenance, tests/oracles, performance, embedded/compiler/browser, scientific/ML, security and high-consequence systems. For each describe task, oracle, environment, scoring, sample, lifecycle, contamination, licensing/access, cost, limitations and reuse potential.
- Check whether standards are mandatory for a specified context, consensus standards, provider guidance, or research. Cite edition and access state; do not assert legal or certification compliance from metadata alone.

**Pass:** at least one complete worked comparison of multiple distinct rater mechanisms and a traceable benchmark sample with alias decisions; all unreviewed rows remain leads. **Checker:** recompute a documented scoring example when inputs and rules permit, seek one counterexample, and independently resolve five benchmark records.

### CP8 — Turn subtle failures into demonstrated checkers

**Tasks**
- Grow failure evidence across source and system types. For each case retain original issue/version, observable symptoms, root-cause confidence, patch/test evidence, legitimate counterexamples and affected component/lifecycle/roles.
- Start with a controlled modal-path fixture inspired by the transcript, clearly fictional and separate from the original application: correct behavior, one trigger omitting animation, a deliberate allowed difference, rapid toggle/cancel, focus, and reduced-motion conditions. Define the contract first.
- Choose checks appropriate to the fixture (e.g., behavior/state tests and mutation). Record exact environment, tool versions and commands. Show whether the known defect is detected and whether the legitimate difference is accepted; investigate surviving/equivalent mutants and any false positives.
- Repeat on two different mechanisms such as cancellation/timeout and stale/concurrent state or transaction recovery. Include at least one negative control and one intentional defect for each. Compare static, runtime, property, differential, fuzz or model-based methods where justified; do not mandate all techniques.
- Document `proposed`, `demonstrated`, `independently reproduced`, and `validated for deployment` as distinct statuses. A local synthetic fixture cannot establish real-world detector precision/recall.

**Pass:** each demonstration has reproducible setup, defect/control, expected and actual output, oracle, limitation and conditional applicability; a reviewer can run it independently where authorized. **Checker:** a fresh reviewer introduces an unannounced valid variant and an unannounced fault, records detection and analyzes unexpected results. No production stress testing.

### CP9 — Performance, bloat, architecture and role-specific depth

**Tasks**
- Audit queued cleanliness, ecosystem and optimization-tradeoff campaigns. Define behavior preservation, workload distribution, environment, hardware, versions, sample/run variance and baseline before measuring.
- Investigate redundant functionality, architectural duplication, dependency and binary costs, runtime/latency/throughput/memory/energy/build impacts, dynamic features, rare paths and compatibility. Compare multiple outcomes; no line-count-only objective.
- Sample specialist design, accessibility, operations, safety, security/privacy, licensing, support and governance evidence. Connect obligations to artifacts, decisions, stakeholders and lifecycle rather than listing job titles.

**Pass:** at least one bounded comparison presents baseline, workload, results, correctness oracle, tradeoff, uncertainty and a counterexample; unexecuted studies remain author-reported. **Checker:** review measurement design for unfair workloads, missing behavior, hidden setup costs, and generalization beyond the sample.

### CP10 — Synthesis and independent review

**Tasks**
- Compare alternative framework architectures using the pilots and their contradictions. Map each conditional candidate to outcome, applicability, evidence, oracle, owner, automation/human review, burden, false results, exceptions, incentives and ongoing validation.
- Design a staged evaluation on heterogeneous repositories and systems, with baselines, blinded/independent judgment where possible, reproducibility, and explicit user-facing outcomes. Treat private/physical/organizational evidence separately from observable repository evidence.
- Publish a coverage and evidence dashboard showing verified claims, unverified leads, inaccessible regions, stale sources, open disagreements and last refresh. Distinguish discovered breadth from appraised depth.
- Conduct an independent whole-work review. Reopen any checkpoint when new evidence contradicts it; preserve reviewer findings and dispositions.

**Pass:** user can trace a candidate check to source evidence and a concrete applicable case, inspect counterexamples and exceptions, and see unmeasured areas. No blanket score or universal gate is declared solely because a checkpoint passes.

## 6. Checker protocol and anti-shortcut rules

Each checker receives the actual artifact and an immutable revision, not only the worker's summary. It records:

1. **Completeness:** compare requirements, source spans and task acceptance criteria with actual outputs; sample omitted cases.
2. **Truth:** open original evidence, inspect exact location/version, recalculate counts and identify inference or unsupported causal language.
3. **Coverage:** inspect both searched and unsearched dimensions; require denominator, selection rationale, source route and access state.
4. **Adversarial cases:** seek a counterexample, disagreement, misleading success, missing evidence, false positive and false negative where applicable.
5. **Reproducibility:** another person can follow search records, stable artifact versions, documented commands and results; distinguish provider claims from our observations.
6. **Continuity:** update open questions, next step, status and scope in `RESEARCH_STATE.md`; after compaction read the ledger and this plan before proceeding.
7. **Disposition:** `pass`, `pass with named open issues`, `rework`, or `cannot assess`. Every issue has severity, evidence, owner and next check; a reviewer cannot silently waive a critical discrepancy.

Stop a checkpoint from being marked complete when: an unavailable source is called negative evidence; planned searches are counted as executed; counts combine different units; a citation does not support its claim; a diagram depicts a planned relationship as operational; a tool result is credited to an unrun test; a project-specific finding becomes a universal rule; a reviewer has not inspected the artifact; or lost context is replaced by plausible invented detail.

## 7. Control loop for the execution model

```text
Read user requirements and current state
   ↓
Choose one bounded question and declare scope + exclusions
   ↓
Execute searches / inspect original evidence / preserve exact provenance
   ↓
Write claims, counterexamples, unknowns and reproducible artifacts
   ↓
Run structural checks → independent content check → fix or record disagreement
   ↓
Update requirements register, coverage state, checkpoint and next action
   ↓
Continue to another domain or reopen an earlier checkpoint
```

For every work batch report **question; selected dimensions and why; operations actually executed; original sources opened; substantive findings and counterevidence; outputs; checker and result; unresolved gaps; next action**. Do not report counts alone as progress. No claiming overall completion from a single batch, a README, or a clean CSV check.

## 8. Order and handoff

Begin CP0–CP3 immediately. CP4–CP9 can proceed in parallel only when workers have distinct files or coordinated changes and a named reviewer; keep the broad discovery track active while deep pilots run. CP10 waits for evidence from the pilots, mechanism audit, and demonstrated checks. The user's separate role list can be integrated whenever it arrives and does not block unrelated research.

**Initial execution deliverable:** a requirements trace, session/source availability ledger, integrity report, 24-claim sample manifest and adjudications, plus a checkpoint review showing exactly what remains unknown. This is an audit tranche, not completion of the project or proof that all previous work is true or false.
