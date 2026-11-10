# Research progress report — 2026-11-10

**Status:** research snapshot dated 2026-11-10; published after the user requested it.

**Repository checkpoint before this report:** `063b34a` on `main`, aligned with `origin/main`.

**Purpose:** give a candid account of what has been built and researched, what it suggests, where execution ran into limits, and what remains open.

## Executive summary

This project began with a broad goal: investigate how to make repositories much more dependable and professionally complete, including repositories produced with AI. The user repeatedly corrected an early, too-generic approach. The scope was widened from ordinary application repositories and familiar “repo health” lists to **arbitrary systems and arbitrary kinds of work**: browsers, operating systems, compilers, game engines, firmware, financial and mobility services, mapping, security tools, video systems, codecs, AI infrastructure, research artifacts, military or safety-relevant systems, and work not yet named.

The work has therefore focused on building a research process before inventing a framework. The repository now contains a linked evidence-research model, source and query records, system decomposition examples, failure-pattern evidence, evaluator and benchmark research, AI research-lab artifact audits, and specialization notes for performance and bloat. The current data has grown to 27 campaigns, 344 query records, 133 planned cells, 30 axes, 177 source routes, 159 search-ledger records, and 612 benchmark-index leads.

Those totals describe **research bookkeeping**, not completeness. Of 133 cells, 109 are thin, 21 are queued, two recorded searches found no evidence within their narrow scope, one contains only a static-source check, and none is saturated. No universal gate, score, weight, profile set, repository template, or implementation has been approved or validated. No benchmark/model run or project test has been performed in this research work.

The strongest current methodological conclusion is modest but important: repository quality cannot be inferred from one badge, score, code metric, passing test suite, or benchmark. Any useful future check has to name its target, applicability, evidence, oracle, workload, lifecycle, cost, and known failure modes. A good framework will likely be a context-aware composition of evidence-backed checks, not a single number.

## Mission and scope corrections

The project is meant to help people make better repositories across different languages, domains, sizes, maturity levels, hosting providers, and audiences. Repository contents are only one part of quality: the repository may define or produce a system that has users, operators, devices, data, dependencies, protocols, physical effects, and lifecycle obligations outside the source tree.

The user corrected the scope several times, and those corrections changed the working model:

| User correction | What changed in the work |
|---|---|
| Initial repo-rater/source scouting was too shallow | Began recording query wording, routes, result windows, access state, provenance, evidence type, limitations, and follow-up instead of treating a handful of names as a survey. |
| Research must span platforms and communities | Added candidate routes across forges, social networks, Q&A, forums, mailing lists, scholarly portals, standards, lab pages, practitioner writing, and operational evidence. Added native Hacker News and Stack Exchange samples as well as Reddit and X routes. |
| Track platforms and search dimensions together | Replaced the flat list as the active model with linked campaigns, queries, cells, runs, and source routes. Dimensions cover venue, language, geography, artifact, responsibility, stakeholders, methods, lifecycle, measurement, and benchmark validity. |
| Generalize to any kind of system | Added recursive, open-ended system decomposition and examples spanning browsers, OSes, compilers, embedded systems, finance, security, aviation, geospatial work, media, and other systems. Examples are prompts for expansion, not the boundary of scope. |
| Include obscure professional responsibilities, roles, and engines | Preserved the pending user-supplied technology-role list and the Computer System Atlas as separate inputs. The Atlas was read and summarized; it is a source of vocabulary, not a verified taxonomy. The anticipated role list has not yet arrived. |
| Study subtle bugs and human/AI failure patterns | Turned the settings-panel transcript into a testable behavioral-path question and collected 33 sourced failure-pattern/community/tool-evaluation cards across multiple system areas. Kept the video’s duplication diagnosis as a hypothesis. |
| Research advanced benchmarks and current AI-lab work | Added benchmark identity/method audits, cross-domain AI evaluations, recent agent-maintenance and oracle evidence, AI lab and repository routes, and research-index freshness checks. No benchmark was executed. |
| Efficiency, cleanliness, and bloat also matter | Added performance and bloat as explicit tracks, with warnings against treating fewer lines or dependencies as automatic improvements. Measurements must preserve behavior and reflect target workloads and environments. |

The initial weakness was real: early discovery was too generic and the first source seed did not support the user’s “all types of systems” ambition. The work now has a much stronger research structure and more diverse evidence, but it has **not** solved the underlying completeness problem. The current source map, system map, role map, language coverage, and framework remain incomplete.

## Work completed

### A. Repository and continuity scaffolding

- Created a separate Git repository, `repo-quality-framework`, with a public GitHub remote.
- Added durable scope, decisions, source-universe, research-protocol, matrix, findings, handoff, and continuity documents.
- Added `AGENTS.md` so later contributors have local working instructions.
- Kept a detailed chronology in [`RESEARCH_STATE.md`](../RESEARCH_STATE.md) and exact search/fetch/access notes in [`research/search-log.md`](../research/search-log.md), with a compact [`research/search-ledger.csv`](../research/search-ledger.csv).
- Recovered the prior Computer System Atlas conversation and the pasted long-form attachment. Recorded what was actually reviewed, how it relates to this project, and the remaining audit gap in [`docs/atlas-context-recovery.md`](atlas-context-recovery.md).
- Created an integrated roadmap and model-switch handoff so context compression or a change of model does not silently erase unresolved items.

The existing research checkpoints were committed and pushed previously at the user’s request. The expanded README and this report were first kept local at the user's request, then published after the user asked to put the work on GitHub.

### B. Search and evidence model

The early flat matrix made it difficult to distinguish what was planned from what had actually been searched. The v2 structure now separates:

```text
campaign → planned cell ↔ exact query ↔ search/fetch run → source route → claim/evidence → candidate practice
```

It uses normalized many-to-many links because one query/run can inform several cells and a cell can require several queries/runs. Search records are kept separate from source identities and research claims. Candidate dimensions and compound cells can evolve as the system model expands.

The current inventory has **30 axes and 509 axis-value records**. These include source/venue, access route, time, language, geography, query intent, research freshness, artifact and project context, runtime and ecosystem, responsibilities, stakeholder roles, harm/outcome, lifecycle, evaluation method, measurement, bloat, benchmark identity, task/oracle validity, run contract, results, and leakage/sampling. These are working axes, not a final ontology.

The current cell status counts, normalized from the free-text status notes, are:

| Status grouping | Cells | Meaning |
|---|---:|---|
| Thin | 109 | Some discovery or appraisal exists, but evidence depth or scope is insufficient for a strong conclusion. |
| Queued | 21 | Planned and not yet searched. |
| No evidence found | 2 | Exact recorded searches returned no evidence; the result is limited to those query windows and routes. |
| Searched: static source only | 1 | A source snapshot was inspected without a fuller method or outcome evaluation. |
| Saturated | 0 | No cell met even the cell-local stopping rule. |

The research method is informed by evidence mapping, systematic/multivocal literature review, snowballing, provenance, and source appraisal. The project-specific method is described in [`research/v2/methods/evidence-research-methods.md`](../research/v2/methods/evidence-research-methods.md). It is not itself a universal research standard.

### C. Source landscape and route discovery

Candidate sources were added across:

- Hosted and self-hosted source forges, including major international services, Gitea/Forgejo-style systems, Codeberg, SourceHut, Gitee, and regional candidates such as AtomGit/GitCode.
- Developer discussions and community evidence: X, Reddit, Hacker News, Stack Overflow, Lobsters, forums, mailing lists, and project issue trackers.
- Standards, policy, and guidance: ISO/IEC software-quality and assessment material, ISO/IEC data-quality work, NIST SSDF, OpenSSF guidance, ACM SIGSOFT empirical standards, and domain-specific standards leads.
- Research literature and discovery routes: papers, lab publication pages, GitHub artifacts, Hugging Face datasets, ACL Anthology, AlphaXiv, arXiv-related routes, The Latest in AI, and an independent lab-paper tracker.
- Tool and metric owners: OpenSSF Scorecard and Criticality Score, OSPS, Best Practices Badge, CLOMonitor, inspect.software, RepoPulse, OSS Compass, CHAOSS, QSOS, RSMM, and adjacent systems.

The current source inventories contain **177 v2 route records** and **173 source-register records**. A route can be a community, platform, API, repository, paper index, or access mechanism. Many records are candidates, not verified active sources. Route count is not coverage: a source can be represented without having been read, and one platform can contain many distinct communities and collections.

The exact [`search-log.md`](../research/search-log.md) preserves search terms, tool route, result windows, fetch status, and access limitations where available. Early discovery was reconstructed from compressed context; it is marked retrospective instead of being assigned invented exact search strings or timestamps.

### D. Evaluators, standards, and metric mechanisms

The first mechanism pass separated unlike systems that are often all called “repo quality tools”:

| Mechanism family | What it tends to observe | What it cannot establish by itself |
|---|---|---|
| Weighted repo-health score | A chosen bundle of repository signals | That the weights match a specific project’s outcomes or that missing inputs mean poor quality |
| Criteria badge or checklist | Whether stated practices/evidence are present | Whether the practice is effective in context or independently verified |
| Maturity rubric | Organizational or process maturity against a model | Product correctness, runtime behavior, or universal applicability |
| Community metrics | Project activity, diversity, sustainability, or participation | Technical correctness or a single project’s total worth |
| Component-selection service | Evidence relevant to adopting a dependency | Quality of the whole system or its deployment |
| Criticality/popularity estimator | Importance, usage, or dependency influence proxies | Intrinsic quality; popularity varies across language ecosystems and can be gamed |
| License/value estimator | License, reuse, or economic signals | General repository quality or engineering fitness |

Owner docs and code were sampled for selected tools; the full mechanism and validity audit remains open. Important unanswered questions include what each score does with unknown data, how relevance is decided, who the comparison population is, how stale inputs are handled, whether independent outcomes validate the scores, and how incentives change behavior.

The standards pass sampled metadata and selected public sources, including ISO/IEC 25010:2023, ISO/IEC 25040:2024, ISO/IEC 5259-4:2024, NIST SSDF 1.1, ACM SIGSOFT Empirical Standards, and OpenSSF guidance. Some content was behind access errors or only available as metadata/excerpts. The work does not claim to have reviewed every normative text. Standards, provider recommendations, badges, tools, studies, and practitioner opinion are kept as different evidence types.

One mixed result was preserved rather than flattened: a study found many software badges were reasonably reliable signals in its sampled npm projects, while a separate study found stars/downloads vary as importance proxies among language ecosystems. Neither yields a universal repository score.

### E. System and domain expansion

After the user listed examples such as browsers, OSes, game engines, compilers, firmware, exchanges, rideshare/maps, security tools, reverse-engineering, video, codecs, and military systems—and explicitly said this still was not exhaustive—the model shifted from a closed list to recursive decomposition.

Added:

- A graph model for purposes, stakeholders, boundaries, components, interfaces, dependencies, data, runtime, physical context, operations, governance, and lifecycle.
- 18 illustrative system stress cases, 62 capability seeds, and 14 proposed/thin compound research cells.
- A worked browser decomposition and initial domain-source notes covering browser/OS/compiler, finance/security/aviation, and other engineering areas.
- Specialization tracks for ecosystem profiles, performance/bloat, research freshness, and tools.

These examples demonstrate how to expand a brief; they are not a catalog of all systems, architecture verification, or audited standards crosswalk. The role list expected from the user has not been supplied, and no roles were invented to fill that gap.

### F. Subtle failure patterns and candidate checks

The video transcript described a settings panel whose close animation worked through Escape but not through the close button. It suggested duplicated behavior as a possible cause. The transcript is not source code and does not establish the cause. The research reframed it as a testable question about whether different triggers preserve a shared behavioral contract.

The [failure evidence batch](../research/v2/failure-patterns/initial-evidence-batch.md) now has 33 numbered cards plus supporting practitioner/provider/conformance notes. It includes cases concerning:

- UI paths, nested dialogs, animation, focus, event bubbling, IME input, and browser/platform differences.
- Cancellation, stale asynchronous responses, retries, duplicate external side effects, webhook semantics, and service scheduling.
- Transactions, database index consistency, migration drift, and concurrency.
- Embedded reset/recovery behavior and an explicitly unverified driver diagnosis.
- Release artifact metadata, build/deploy file parity, and gates that watch the wrong paths.
- Workload-specific runtime regressions, artifact bloat, and measurements that can move in opposite directions.
- AI agents copying repository vulnerabilities, missing policy violations, overclaiming bug discovery, and long-horizon work that fails after individually plausible changes.
- Test oracles and fixtures that can manufacture failures or pass without checking the intended behavior.

Evidence cards distinguish confirmed fixes and source history from questions, practitioner reports, research findings, unverified diagnoses, and product opinion. The current candidate recipe is: define the expected behavior and observable oracle, enumerate applicable triggers and histories, include state/interleaving/platform conditions, add deterministic and generative checks where appropriate, and verify tests themselves are meaningful. Duplication detectors or shared-handler rules alone cannot establish correctness.

The detailed modal analysis is in [`modal-path-equivalence.md`](../research/v2/failure-patterns/modal-path-equivalence.md). This remains a candidate method, not a universal gate or proof of how often the bug occurs.

### G. AI-generated repository quality and current lab work

AI-related research was expanded beyond “does the generated patch pass?” It now covers post-merge maintenance, structural quality, test oracles, inherited failures, long-horizon work, cross-repository changes, policy compliance, vulnerability context, AI infrastructure performance, evaluation reproducibility, research feeds, and artifact availability.

Named work sampled includes RepoNorm, SWE-CC, SWE-Maintain, CrossSWE, InfraDev, Infrathon, TestExplora, NITR, benchmark contamination/reliability studies, and selected AI-lab methods/artifacts. Examples of findings recorded:

- Repository norms can be explicit or implicit; a norm acquisition method’s evidence and calibration artifacts matter.
- A policy evaluator may inspect both an agent’s trajectory and final contribution.
- The existence or syntax of test files is a weak proxy for whether meaningful behavior was verified.
- SWE-Maintain provides counter-evidence against an overly broad claim that agent maintenance quality necessarily degrades over a sequence: in its paired Python setting, many later-task failures were explained by inherited failing tests.
- Cross-repository and infrastructure tasks add linked-repository, compute, environment, and workload constraints.
- A research portal’s count and “latest” date can vary across endpoints; an incomplete or stale snapshot should disclose that instead of implying full recall.

Selected discovery included The Latest in AI, AlphaXiv, lab pages, GitHub, Hugging Face, ACL Anthology and other research routes. The inspected 19-lab tracker snapshot was partial and five days old, with source failures and a large pending metadata queue. It is an example of freshness reporting, not a complete lab census. Most current evidence was read from selected pages, papers, or preprints; no common independent re-analysis was done.

### H. Benchmarks and evaluation methods

The benchmark pass added a landscape report and **612 raw index rows**:

| Record origin | Rows | Interpretation |
|---|---:|---|
| Pinned Awesome-Code-Benchmark README snapshot | 233 | Source index entries at a pinned revision |
| HOW2BENCH v5 Appendix F extraction | 379 | Bibliography-linked entries extracted from the appendix |
| **Total** | **612** | **Uncanonicalized leads; not unique benchmark identities** |

HOW2BENCH’s reported 672 analysis units do not align one-to-one with the appendix extraction. A separate survey corpus of 425 non-functional-improvement studies is not counted as benchmark suites. Alias and paper/dataset/task identity resolution remains open.

The method audit covers benchmark validity, task and outcome validity, reporting, lifecycle maintenance, task discovery from documentation, witness tests, mutation, contamination, reuse, repeated-run variance, performance/bloat, resource use, and system-specific conformance/fuzzing/simulation. 38 named system-specific candidates were recorded across 36 report rows; some rows group related systems, and some named candidates are standards or test frameworks until tied to an explicit task, oracle, environment, and score.

Two bounded findings illustrate why sample and method matter:

- TestExplora reports documentation-derived test oracles over 2,389 tasks across 482 repositories. This is evidence about a specific generated-task collection, not every repository or an independently reproduced result here.
- A USENIX debloating study reports 20 programs and 12 metrics; source retrieval covered 24 tools, of which 17 were successfully built/run in its study. The paper’s passable/sound/robust results are sample-specific and not universal success rates.

The modal example was connected to trigger-equivalence and sequence testing, browser dialog behavior, and test-oracle design. The project did not run any benchmark suite, repeat a paper experiment, run a model, or execute benchmark code.

## What research routes were actually used

| Route | Completed sample | What remains unknown |
|---|---|---|
| Parallel search/fetch | Broad discovery and selected source extraction across platforms, standards, tools, system domains, AI labs, and benchmarks | Search results were bounded/ranked; the specialized `web_research` route returned HTTP 402 in an earlier attempt; ordinary search worked |
| Exa | Evaluator, regional forge, performance, standards, and AI research discovery/fetches | Result coverage and recall were not measured; one earlier pass is retrospective |
| Connected GitHub | Read/search for evaluator and AI-lab repositories, issue/PR status, and benchmark artifacts | Bounded query results; zero results are not proof of absence; some large datasets were not retrievable via the connected content endpoint |
| X via connected route and signed-in Brave | A few repository-health, AI quality, benchmark, and failure-pattern searches | Some 20-post windows were low-yield/noisy; two later benchmark searches surfaced few useful leads; this is not representative prevalence data |
| Reddit via Brave | Two public threads opened, one Portuguese | Very small sample and no broad subreddit/language sweep |
| Hacker News Algolia + Firebase item route | Five query windows, four original threads, 18 sampled comments | Partial API route and selected comments; not all HN content or time periods |
| Stack Exchange API | Two query windows, two questions, four answers, one comment | Query-local sample; no site-wide or language-wide saturation |
| Research portals and lab pages | Selected recency/feed comparisons and paper-to-code/dataset routes | No precision/recall study; no complete lab, venue, language, or region census |

The user authorized Parallel AI and the signed-in Brave/X browser for research. That authorization has only been used for read-only discovery and inspection; no messages or posts were made.

## Obstacles, corrections, and provenance problems

| Obstacle / issue | How it was handled | Remaining limitation |
|---|---|---|
| Major conversation-context compression and earlier lost details | Re-read the session/Atlas material where available; created a detailed state ledger and handoffs; marked unrecoverable search metadata as retrospective | Early exact query strings and times cannot be reconstructed safely |
| Agent Reach not installed | Recorded the failed availability check and continued with available Parallel, Exa, connected services, and browser routes | Agent Reach route is still unavailable unless the environment changes |
| Parallel `web_research` returned HTTP 402 | Used ordinary Parallel search/fetch where it worked | Deep-research route was not available in that attempt; account/credit state may change |
| Some source paths or repositories failed | Rediscovered the correct CHAOSS repository after a guessed path returned 404; recorded 403/404/502 and dataset gating rather than silently treating them as negative findings | Individual access failures need future rechecks; they do not establish nonexistence |
| Search endpoints return ranked windows or zero hits | Logged query/window and bounded the claim to those records | No platform-level recall estimate or saturation claim |
| Paper and artifact counts do not match | Separated reported analysis units from extracted bibliography rows; recorded mismatched endpoint freshness snapshots | Benchmark identities and source-to-paper mapping remain unresolved |
| Some current papers are preprints or selected excerpts | Marked publication status and appraisal depth in the research notes | Replication, full-method audit, and independent common-sample comparison remain open |
| Initial approach was too shallow | Rebuilt the source/model around campaign-cell-query-run-source links and widened to all systems | Improved structure is not equivalent to complete research; large gaps remain |
| CSV status values contain explanatory prose | Grouped statuses only for this report and disclosed that they are normalized | Source statuses are free text; a controlled vocabulary migration may be useful after schema review |

Specific source-level caveats include: an incorrect early Scorecard fetch reference and swapped follow-up records were corrected/flagged; three extracted-run details were reconstructed and marked retrospective; a guessed CHAOSS URL returned 404 before the official repository was found; some standards sources were 403-protected; the Infrathon code route returned 404 and its dataset required accepted conditions without a dataset card; and a one-digit AlphaXiv paper-ID typo led to an unrelated paper until checked against the canonical identifier.

## What has not been done

- No exhaustive inventory of all platforms, communities, languages, regions, standards, labs, practitioners, or tools.
- No comprehensive source-native audit of every named platform; no broad non-English or regional-language research campaign.
- No complete Computer System Atlas audit and no user technology-role intake yet.
- No canonical benchmark database; no 612-identity deduplication; no complete task/paper/dataset/leaderboard map.
- No exhaustive comparison or independent validation of repo raters, badges, maturity models, or metric systems.
- No validated final ontology for responsibilities, roles, systems, or artifacts.
- No universal checklist, scores, weights, gates, supported-profile set, template, or implementation.
- No benchmark, model, stress test, repository project test, dataset download, or research-code experiment run.
- No measured false-positive/negative rates, gate burden, gaming, exemptions, ownership model, governance, or cost model.
- No saturation claim for any cell; in particular, no complete coverage claim for social platforms, regional routes, labs, domains, or current research.

## Current artifacts to read

| Artifact | What it contains |
|---|---|
| [`RESEARCH_STATE.md`](../RESEARCH_STATE.md) | The detailed continuity ledger and current next steps |
| [`docs/integrated-research-roadmap.md`](integrated-research-roadmap.md) | Sequenced work program and acceptance/self-correction rules |
| [`docs/research-model-v2.md`](research-model-v2.md) | Campaign/query/cell/run/source record model |
| [`docs/source-universe.md`](source-universe.md) and [`research/v2/source-routes.csv`](../research/v2/source-routes.csv) | Candidate route map and access states |
| [`research/search-log.md`](../research/search-log.md) | Search strings, result windows, fetches, errors, and retrospective notes |
| [`research/v2/failure-patterns/initial-evidence-batch.md`](../research/v2/failure-patterns/initial-evidence-batch.md) | 33 numbered evidence cards and cross-case analysis |
| [`research/v2/benchmarks/benchmark-landscape-and-method-audit-2026-11.md`](../research/v2/benchmarks/benchmark-landscape-and-method-audit-2026-11.md) | Benchmark families, method validity, candidates, and evidence limits |
| [`research/v2/benchmarks/candidate-index-leads.csv`](../research/v2/benchmarks/candidate-index-leads.csv) | 612 uncanonicalized source-index rows |
| [`research/v2/systems/`](../research/v2/systems/) | Capability seeds, stress cases, compound cells, and worked decomposition |
| [`research/v2/agent-quality/`](../research/v2/agent-quality/) | Agent-code, AI lab, cross-domain evaluation, and research-artifact notes |
| [`research/v2/specialization/`](../research/v2/specialization/) | Performance/bloat, ecosystem, tooling, and research-freshness tracks |

## Recommended continuation sequence

1. **Preserve the user’s inputs.** When the role list arrives, add it as a supplied source and map roles to responsibilities, artifacts, decisions, interfaces, and evidence. Keep it distinct from the Computer System Atlas.
2. **Baseline and integrity audit.** Reconcile old v1 records to v2; check identifiers, foreign keys, duplicate identities, statuses, source links, and search-ledger coverage. Do not rewrite historical search claims to make the data look cleaner.
3. **Expand the system graph from real briefs.** Select several contrasting systems—including at least one low-level/system artifact, one interactive consumer system, one data/AI workload, and one high-consequence or operational system—then recursively identify missing components, roles, dependencies, and failure boundaries.
4. **Broaden native source coverage.** Continue direct venue/API searches and original-thread reading on Stack Overflow, Reddit, HN, Lobsters, forums, mailing lists, issue trackers, X, and regional/non-English routes. Record what each route can and cannot expose.
5. **Deepen evidence, not just counts.** Select stratified cells and trace claims to primary sources, implementation, issue/PR/test history, task manifest, dataset, oracle, or standard as appropriate. Seek conflicting evidence and counterexamples.
6. **Audit evaluators and benchmarks.** Canonicalize benchmark identities and compare a declared sample of mechanisms, inputs, missing-data handling, validity evidence, versioning, fairness, cost, and gaming. No execution until a specific run is authorized and reproducible conditions are recorded.
7. **Study efficiency with behavior preserved.** Define candidate workloads and environmental conditions; inspect how size, startup, runtime, memory, energy, build cost, and dependency count trade off. Avoid a single “leanest code” proxy.
8. **Only then prototype framework options.** Make every candidate check state applicability, claim/evidence, oracle, owner, burden, failure modes, exception path, and validation plan. Compare alternative profiles and gate policies before implementing them.

Keep the next model’s scope tied to [`docs/integrated-research-roadmap.md`](integrated-research-roadmap.md), preserve the user’s corrections, and update the continuity ledger after each substantive batch.

## Repository and publication state

The published checkpoint before this documentation update was `063b34a` on `main`, and the working tree was clean. The README, report, and continuity-ledger update are now being published to `origin/main` following the user's updated instruction.
