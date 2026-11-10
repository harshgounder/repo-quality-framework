# Repository Quality Framework Research

This repository is the working home for research toward a **general-purpose, evidence-based framework for making software repositories dependable, usable, maintainable, and fit for their purpose**.

The intended reach is broad: repositories made by people or AI, across different languages, domains, sizes, maturity levels, and hosting platforms. The project must account for the fact that a library, a research artifact, a website, an infrastructure repo, a data project, and a small script do not have identical obligations. The eventual framework may therefore need profiles, conditional requirements, and evidence-based gates instead of one undifferentiated checklist.

## Current phase

**Research design and source mapping.** The repository is deliberately not yet a product specification, scoring system, template repo, or implementation. The earlier reconnaissance is a starting set of leads, not a completed survey. Read [`RESEARCH_STATE.md`](RESEARCH_STATE.md) before continuing; update it whenever research advances or a decision changes.

## Working principles

- Cover practices that materially affect repository outcomes, including engineering, security, operations, governance, accessibility, documentation, user experience, release quality, and stewardship.
- Separate normative standards, platform rules, empirical research, expert practice, tool checks, and community opinion. They are different kinds of evidence.
- Record sources and claims at the smallest useful level, including date, scope, method, limitations, and conflicts.
- Treat missing evidence as unknown. A search result, badge, or passing automated check is not proof of overall quality.
- Design for applicability: a requirement should say when it applies, how it can be evidenced, and who bears the cost.
- Keep the source universe and research coverage visible. “Searched,” “saturated,” and “complete” are not interchangeable.
- Do not turn the research notes into a universal gate before examining false positives, burden, gaming, context, and failure modes.

**Open-ended systems direction:** [recursive system model](docs/open-ended-systems-model.md), [illustrative system decompositions](research/v2/systems/stress-cases.csv), [capability families](research/v2/systems/capability-catalog.csv), and [compound research cells](research/v2/systems/compound-research-cells.csv), and [a worked browser example](research/v2/systems/worked-decomposition.md). These are provisional, not a closed universe.

**Current research model:** [v2 linked coverage design](docs/research-model-v2.md), with [source routes](research/v2/source-routes.csv), [axis values](research/v2/axis-values.csv), [campaigns](research/v2/campaigns.csv), [query bank](research/v2/query-bank.csv), [planned cells](research/v2/planned-cells.csv), [cell-to-query links](research/v2/cell-queries.csv), [run-to-cell links](research/v2/cell-runs.csv), and [integrity notes](research/v2/integrity-and-migration.md). The earlier flat matrix is historical and needs reconciliation.

**Research method:** [evidence-research method and appraisal design](research/v2/methods/evidence-research-methods.md). **Failure-pattern evidence:** [initial sourced batch and candidate behavioral checks](research/v2/failure-patterns/initial-evidence-batch.md). Both are provisional and document their source limits.

**Evidence on AI-authored changes:** [initial empirical study appraisal](research/v2/agent-quality/empirical-evidence-batch.md) keeps post-merge quality, build-system code, bloat removal and workload/resource trade-offs separate.

**Benchmark landscape:** [benchmark landscape and method audit](research/v2/benchmarks/benchmark-landscape-and-method-audit-2026-11.md) compares benchmark families and their oracles, scope, validity limits, lifecycle, reuse, and efficiency measures. The attached [candidate index leads](research/v2/benchmarks/candidate-index-leads.csv) currently has 612 uncanonicalized source-index records; this is not a count of unique or validated benchmarks.

**AI research beyond coding agents:** [cross-domain evaluations and research routes](research/v2/agent-quality/cross-domain-ai-evaluation-and-research-routes-2026-11.md) covers scientific and desktop agents, reliability studies, lab artifacts, discovery portals, source-health limits and follow-up gaps.

**AI-generated repository quality and lab code:** [maintainability benchmarks, field studies, AI-for-AI work, and agent-first repositories](research/v2/agent-quality/ai-generated-repository-maintainability-and-lab-artifacts-2026-11.md) records evidence about hidden structural failures, duplicated logic, post-merge debt, research-source freshness, and artifact limitations.

**Current AI-lab artifacts and frontier evidence:** [current lab methods, papers and repositories](research/v2/agent-quality/current-lab-artifacts-and-frontier-evidence-2026-11.md) follows recent work on repository norms, test oracles, maintenance history, cross-repository changes, model infrastructure, research outputs, lab evaluation methods and paper-feed freshness.

Specialization tracks: [performance and bloat](research/v2/specialization/performance-and-bloat.md), [freshness and research depth](research/v2/specialization/freshness-and-depth.md), [ecosystem profiles](research/v2/specialization/ecosystem-profiles.csv), and [performance tooling](research/v2/specialization/tooling.csv).

**Next-model handoff:** [integrated research roadmap](docs/integrated-research-roadmap.md), [execution workflow and role-list intake](docs/execution-handoff.md), [subtle failures and checks](docs/failure-pattern-research-handoff.md), and [atlas context recovery](docs/atlas-context-recovery.md). The user is preparing a separate role list; its contents are not yet known.

## Repository map

- [`RESEARCH_STATE.md`](RESEARCH_STATE.md): continuity ledger and exact current status.
- [`AGENTS.md`](AGENTS.md): instructions for future contributors and AI agents working here.
- [`docs/research-protocol.md`](docs/research-protocol.md): research dimensions, evidence handling, sampling, and stopping rules.
- [`docs/source-universe.md`](docs/source-universe.md): candidate platform and source families; seeds are explicitly unverified and non-exhaustive.
- [`docs/decisions.md`](docs/decisions.md): settled directions and open decisions.
- [`research/preliminary-findings.md`](research/preliminary-findings.md): early leads with scope cautions and source links.
- [`research/search-log.md`](research/search-log.md): exact search queries, tool routes, result counts, leads, and access limits.
- [`research/search-ledger.csv`](research/search-ledger.csv): compact index into the detailed search log.
- [`research/v2/methods/evidence-research-methods.md`](research/v2/methods/evidence-research-methods.md): literature-informed method for mapping, deep reviews, source appraisal, claim extraction and evidence updates.
- [`research/v2/failure-patterns/initial-evidence-batch.md`](research/v2/failure-patterns/initial-evidence-batch.md): issue/fix, research and Q&A evidence on behavioral-path drift, retries, cancellation, event ordering and detector limits.
- [`research/matrix-template.csv`](research/matrix-template.csv): schema for multidimensional coverage tracking.
- [`research/dimension-catalog.csv`](research/dimension-catalog.csv): seeded dimensions and values for the sparse, compound coverage matrix.
- [`research/source-register.csv`](research/source-register.csv): platform and source candidates, their roles, and verification state.
- [`research/rater-inventory.csv`](research/rater-inventory.csv): early evaluator candidates, kept separate by scope and mechanism.

- [docs/matrix-model.md](docs/matrix-model.md): theoretical cross-product, applicability filter, sparse coverage strategy, and compound-cell rules.
- [docs/research-start-plan.md](docs/research-start-plan.md): staged work plan and decision point before synthesis.
- [research/coverage-round-2.md](research/coverage-round-2.md): second discovery round across standards, communities, forges, and signal-validity evidence.
- [research/mechanism-audit.md](research/mechanism-audit.md): first mechanism and empirical-evidence audit.

## Status language

Use `unplanned`, `queued`, `searched`, `thin`, `inaccessible`, `conflicting`, `no evidence found`, `not applicable justified`, or `saturated` for matrix cells. A no-hit result is local to its recorded query, route, filter, language, and date window; it does not mean no evidence exists elsewhere. `Saturated` means additional targeted searches are producing little new evidence **for the recorded cell and search method**; it does not mean the whole platform or topic is exhausted. Reserve `complete` for a defined deliverable whose acceptance criteria have been checked and recorded.
