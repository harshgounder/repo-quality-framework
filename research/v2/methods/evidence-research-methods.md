# Research method for an open-ended repository and system-quality framework

**Status:** provisional method design, based on an initial methods-literature pass on 2026-11-10. This is not a settled protocol or a claim of complete literature coverage.

## Why the project needs a research framework of its own

The target is too broad for a conventional “best practices” list or one review question. A repository can support a tiny script, browser engine, operating system, database, compiler, game engine, research artifact, financial system, safety-critical device, security tool, or a component inside any of those. The same check can be essential in one context, misleading in another, and impossible to automate in a third. New work, rewrites, replacements, integrations, deployment and long-term maintenance also create different obligations.

The research object must therefore be a **linked evidence system**, not a checklist spreadsheet. It should connect:

`system graph / artifact → scoped question → search campaign and exact run → source version and passage → extracted claim → evidence quality and conflicts → applicability conditions → candidate assurance mechanism → validation result`.

This is an architectural inference for this project, informed by evidence-synthesis methods below. No reviewed methods paper prescribes this exact schema.

## Methods evidence opened in this pass

| Source | What it contributes | Scope and limits |
|---|---|---|
| Kitchenham and Charters, [Guidelines for Performing Systematic Literature Reviews in Software Engineering, EBSE-2007-01 v2.3](https://ebse.webspace.durham.ac.uk/wp-content/uploads/sites/49/2022/08/Systematic-reviews-5-8.pdf) | A disciplined sequence for a review: define questions/protocol; identify and select primary studies; assess quality; extract and monitor data; synthesize. This is a useful procedural backbone for question-focused research. | A 2007 software-engineering technical report. It is not a universal platform-search protocol, an exhaustive source directory, or authority to treat all evidence classes alike. |
| Wohlin, [Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering](https://www.wohlin.eu/ease14.pdf), EASE 2014 | Backward-reference and forward-citation snowballing can complement database searches. Starter set selection matters; the paper advises diversity across communities, venues, years and authors. | A complementary discovery technique, not proof that citation networks contain practitioner incidents, current tools, unindexed languages, or all relevant work. A narrow starter set can reproduce its blind spots. |
| Garousi, Felderer and Mäntylä, [Guidelines for Including Grey Literature and Conducting Multivocal Literature Reviews in Software Engineering](https://pureadmin.qub.ac.uk/ws/files/178657399/GuidelinesforconductingMLRs_Sept18.pdf) | Gives methods for bringing practitioner and other non-academic material into software-engineering reviews and distinguishes secondary-study purposes (including mapping versus synthesis). This supports a separate, explicit practitioner-evidence stream. | Grey literature is heterogeneous. A maintainer issue, vendor page, personal blog and social post are not interchangeable, and inclusion does not make their claims independently validated. |
| Garousi et al., [Grey Literature in Software Engineering: A Critical Review](https://www.sciencedirect.com/science/article/pii/S0950584921000860), 2021 | A review of secondary SE studies reported that only a subset used grey literature to answer research questions and that roughly half of the grey-literature URLs they checked no longer worked. It highlights appraisal and source-persistence problems. | The reported percentages describe the review's corpus and period, not all research or current web persistence. Use as a reason to preserve provenance and access details, not as a universal failure rate. |
| Wohlin and colleagues, [SEGRESS: Software Engineering Guidelines for Reporting Secondary Studies](https://www.computer.org/csdl/journal/ts/2023/03/09772383/1DgjFlquCaI), IEEE TSE 2023 | Reporting guidance specifically accounts for software-engineering secondary studies, including systematic maps and qualitative syntheses; it discusses transparency, selection and threats to validity. | Reporting guidance improves inspectability; following a report template alone does not make the underlying search complete or the conclusions valid. |
| Miake-Lye et al., [What is an evidence map?](https://pubmed.ncbi.nlm.nih.gov/26864942/), 2016 | Reviews definitions, products and methods used for evidence maps; their sample found variation rather than one settled map format. Their own search included databases, reference mining and topic experts. | It is from health evidence synthesis, not software engineering. Its useful caution is that “evidence map” is not a magic standardized shape; adapt transparently rather than claiming universal convention. |

The primary-source extracts and exact search runs are indexed in [`../../search-log.md`](../../search-log.md) under `METH-*` and `METH-F-*`.

## Recommended research lifecycle

### 1. Define a decision question, not a vague topic

For each campaign, state what decision the research could inform. Examples:

- Which defect classes can result when two ways of initiating or stopping an action do not share a behavioral contract?
- Under what conditions does clone detection find change-coupled duplication, and what does it miss?
- Which checks can establish that retrying an operation does not repeat an external side effect?
- Which repository-visible signals have been validated against a defined quality outcome, in which population?

Keep separate questions for **what a standard requires**, **what has been observed**, **what mechanism may detect it**, and **whether the mechanism is suitable for a particular system**. A single query that mixes these asks makes evidence quality hard to judge.

### 2. Keep the open systems model, but decompose before searching

Represent the target as a recursive graph of capabilities, components, interfaces, state, data, users/operators, dependencies, physical and deployment context, and lifecycle transitions. Link a question to the relevant graph nodes and edges; do not force every system into a fixed domain list. The system model in [`docs/open-ended-systems-model.md`](../../../docs/open-ended-systems-model.md) is the current framing.

Maintain independent dimensions (at minimum): system/artifact and component; lifecycle and change type; capability/behavior and failure class; user, operator and specialist role; assurance method/tool; source venue and access route; evidence class and quality; language/region; risk and operating context; version/date; and applicability. Add values when evidence exposes a missing concept. Distinguish `unknown`, `not applicable`, `not searched`, `inaccessible`, and `no evidence found`.

The theoretical product of these axes is a scope model, **not a search itinerary**. Predeclare why a cell or combination is selected, what can transfer from adjacent cells, and what remains uncovered. Use separate one-axis coverage, representative pairwise coverage, risk- or mechanism-driven compound interactions, counterexample searches, and gap-driven follow-ups. Pairwise coverage alone is not adequate for important higher-order interactions; it is one economical discovery device.

### 3. Use multiple discovery routes with separate evidence lanes

Search academic indexes and publisher/author repositories for empirical and method work; standards bodies and official docs for normative scope and mechanisms; project-owned repositories/issues/PRs/commits/tests for incident and fix histories; practitioner forums, Q&A, mailing lists, blogs and social sites for vocabulary, symptoms and workarounds; datasets and incident reports for population-level or operational evidence; and source code/release history when a rater's mechanism must be inspected.

For a question, combine:

1. a planned semantic query family and synonyms for the mechanism and its failure symptom;
2. native search on the venue or project where possible (web indexing is not native-platform coverage);
3. backward references and forward citations for relevant research;
4. linked issue, pull request, commit and regression test inspection for reported software failures;
5. counterexample and negative-evidence searches;
6. language/region variants where relevant; and
7. follow-up searches generated from newly observed terms, maintainers, tools and failure mechanisms.

The exact venue set must be chosen for the question. Reddit, X, Hacker News, Stack Overflow, GitHub issues, mailing lists and project forums are distinct samples; one indexed search across them cannot stand in for all of them. Preserve access route, filters, language, ranking mode, time window, result window and failures.

### 4. Separate broad mapping from deep synthesis

First **map** the candidate source, method, artifact and failure landscape, recording gaps and thin regions. Then perform focused reviews where a high-consequence or recurring decision warrants depth: open primary materials, extract methods and scope, inspect linked artifacts, and compare independent evidence. Do not imply that a high search-result count equals coverage or that broad discovery snippets support a causal claim.

For practitioner and other grey literature, run a multivocal stream with its own selection and appraisal rules. Preserve it because it may surface new failure language or implementation detail absent from papers; corroborate it before turning it into a general claim. Appraisal should fit the source type: a regression report is judged partly by reproducer, environment, maintainer response and linked fix; a study by its research question, sampling, measures, analysis and threats; a standard by edition, normative status and scope; a tool by its actual implementation, configuration, outputs and known blind spots.

### 5. Extract claims and mechanisms, not just titles

Each retained source record should capture identity, author/maintainer, date and version, source class, stable URL/commit/DOI, access and retrieval date, relevant passage/location, and links to parent/child artifacts. Each claim should state: who asserts it; whether it is direct observation, reported claim, normative requirement, empirical result, maintainer diagnosis, inference or unresolved hypothesis; target population/context; method and denominator; confidence; limitations; and conflicting evidence.

Mechanism records should say exactly what a check observes, what condition it flags, what it cannot observe, expected false-positive/negative paths, required setup, runtime/cost, evidence output, and who can interpret/fix it. For a proposed test, record the oracle/invariant and how test validity was checked. Keep source, claim and mechanism identifiers linkable rather than copying summaries into untraceable matrix cells.

### 6. Appraise the measurement itself

Do not assume a quality score measures quality because its ingredients look plausible. Arif, Kuutila and Ralph's 2026 ESEM study, [Assessing the Construct Validity of Object-Oriented, Class-Level Code Quality Metrics](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.10), examined 63 metrics from three tools on Java object-oriented projects. In its study, some metrics did not align with their purported constructs, loaded on other factors, or were inconclusive. This is scoped evidence, not a verdict on every metric; it is a warning to inspect construct validity before setting thresholds.

For every rater, score, badge or gate, ask: What is the construct and unit? Is it measured directly or via proxy? Was it validated against an outcome meaningful to its stated use? On what languages, project types and maturity range? What happens with missing data, inactive repositories, private artifacts, generated/vendor files and `N/A`? What are the costs, false positives/negatives, incentives, gaming routes and update policy? Can a low score mean “not measured” rather than “bad”? Keep independent validation separate from owner claims.

### Follow-up: evidence strength must be local to the claim and review type

The 2025/2026 tertiary study [The unfinished business of evidence strength in software engineering](https://link.springer.com/article/10.1007/s10664-025-10728-9) examined 22 secondary studies that claimed to assess evidence strength. It reports that GRADE was the most common method but was not necessarily appropriate for the review type; most assessments gave one generic grade to all review findings instead of evaluating each finding or outcome; qualitative-review guidance such as GRADE-CERQual was not being used; and few reviews made explicit practitioner recommendations, with none rating the strength of those recommendations. This is a methods study, not a recommendation to import a medical evidence scale unchanged into this project.

The immediate implication is to keep **claim-level evidence appraisal** separate from a source's overall label. The type of question matters: a standard's normative scope, a qualitative maintainer report, a measured association, a reproduced bug, a security exploit, a gate's predictive performance and a proposed causal mechanism need different confidence criteria. If the project later recommends a gate, record separately (a) confidence in the supporting claim, (b) applicability to the target system/context, (c) evidence that the gate detects the condition, and (d) expected harms and costs of using it.

Recent repository-health studies illustrate why metric presence is not measurement validity. A 2025 study of OpenSSF Scorecard practices in npm repositories reports associations with vulnerability and update-response outcomes but remains observational and ecosystem-specific. A separate 2025 preprint tests a Composite Stability Index on 100 highly ranked repositories and reports that weekly aggregation and medians can fit the examined data better than daily aggregation and means; it does not validate a general repository-quality construct. A 2026 practitioner study identifies 21 OSS health aspects and 72 associated metrics, while reporting weaker measurement support for qualitative aspects and the need to account for project and assessor context. These are different questions and methods; they should not be averaged into a single evidence grade.

The exact studies and scoped results are in [`../agent-quality/frontier-ai-coding-agent-research-2026-11.md`](../agent-quality/frontier-ai-coding-agent-research-2026-11.md). This addendum extends the initial methods sample; it does not resolve the suitability of one universal appraisal rubric.

### 7. Synthesize disagreement and set local stopping rules

Do not resolve disagreement by counting hits or source popularity. Reconcile differences by claim scope, population, mechanism, version, method and source proximity. A standard answers what it says; it does not establish that following it guarantees field success. A merged fix verifies that the project changed code and tests for a reported case; it does not prove the bug class is universal. A forum report may be the only evidence for an obscure symptom, but remains a report until reproduced or otherwise corroborated.

Use a stopping rule local to each cell, query family, language, date range and access route: saturation means new targeted searches stop adding materially new mechanisms/sources for that declared scope. A blocked or inaccessible route is not saturated. A large open-ended frontier should remain explicitly open.

### 8. Revisit and version the evidence

Store publication, project release/commit, search date and retrieved source version independently. Set review intervals by volatility and consequence: standards/platform rules and active tool behavior need freshness checks; established theory can be revisited less often; a live incident thread is not “closed” until linked resolution is checked. Preserve prior source versions and corrections so a model switch does not erase provenance.

## What this changes in the current research workflow

The existing v2 axes and source routes remain seeds; do not replace them or claim they are exhaustive. Add the following records only as the workflow calls for them:

- a **search-run record** for every actual operation (exact query/API operation, tool, route, time/timezone, filters, returned and screened counts, opened URLs, access failure, and follow-up);
- source records that distinguish candidate, opened, primary, inaccessible, stale and closed/deleted; and
- claim/mechanism records that preserve versions, scope, evidence class, limitations, conflicts and links to system-graph cells.

The exact ledger headers and current model should be reviewed before adding a schema migration. This pass adds evidence notes first rather than silently treating planned cells as executed or changing the framework's dimensions.

## Research boundaries and remaining gaps

- This is an initial methods pass, not a new systematic review of every evidence-synthesis method.
- Search was English-heavy. X connection was used; Agent Reach was unavailable, and no native Reddit, Stack Exchange, mailing-list or regional-language query route was verified in this pass.
- Parallel web search returned ranked windows, not the total number of eligible sources on each platform. Exa and web-indexed search should be treated as discovery routes, not venue coverage.
- Several primary methods papers were extracted as relevant excerpts, not read line-by-line in full. One source from health evidence mapping is used only for its finding that definitions vary.
- The research ontology proposed above is our design inference. It needs user review and later usability/replicability evaluation before it becomes a durable standard for the project.
