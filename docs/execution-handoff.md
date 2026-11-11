# Execution handoff: repository and system quality research

**Status:** historical planning handoff, originally prepared while the user was considering a model switch. Execution is now authorized and has begun. The current [operating contract](operating-contract-and-continuity.md) and active checkpoint at the top of `RESEARCH_STATE.md` take precedence over this document’s historical ordering. The separately promised role list has not been received; do not wait for it. Existing research remains a starting point, not a completed framework or source map.

## First actions

Read AGENTS.md, RESEARCH_STATE.md, docs/integrated-research-roadmap.md, docs/failure-pattern-research-handoff.md, this handoff, docs/atlas-context-recovery.md, docs/open-ended-systems-model.md, docs/research-model-v2.md, docs/research-protocol.md and research/v2/integrity-and-migration.md. Check git status and inspect actual files. Preserve user changes. The user may provide a separate role list later; it has not been received. Do not invent the list or wait for it: proceed with independent role research now.

The goal is a deeply researched, general framework for repositories and the systems they represent. It must handle arbitrary systems and parts, from new builds to ports, rewrites, compatible replacements, integrations and maintenance. Browsers, OSes, compilers, game engines, firmware, finance, mobility, maps, video, codecs, security tools and reverse engineering are examples, not boundaries. Decompose systems into capabilities, components, interfaces, technology, operational and physical context, users, risks, and specialist responsibilities. Explore global and regional platforms, communities, standards, research, practitioners, obscure specialist sources and current work. Cover lean design, bloat and resource efficiency.

The user repeatedly rejected generic lists, shallow source maps, misleading counts and plans that replace research. Existing v2 CSVs are seeds and planned cells; they do not establish coverage. The prior flat matrix has provenance errors and needs reconciliation. The pre.dev estimator was statically inspected, not executed; see research/v2/first-findings.md.

The user provided a Computer System Atlas conversation and full pasted copy, not the pending role list. The atlas includes 126 broad sections and a more detailed computational-foundations pass. Study its actual contents and relation to the quality framework; see docs/atlas-context-recovery.md.

## Role-list intake

When the user supplies the list:

1. Preserve the original wording, ordering, groups, source and user context in a dated intake record. Make a separate normalized mapping; never silently drop duplicates.
2. Give every original entry a stable ID and a processing state. Preserve ambiguity and differences between a job title, discipline, activity, stakeholder and decision authority. One person may perform multiple responsibilities and titles vary by context.
3. For each entry map specializations, responsibilities, decisions, inputs, outputs, handoffs, failure modes, affected stakeholders, artifacts, system components, lifecycle, applicability, evidence, relevant tools/standards, cost, disagreements and unresolved questions.
4. Compare the supplied roles with existing seeds and find missing or overlapping disciplines, including hardware, safety, operations, legal, design, accessibility, data, domain expertise and user perspectives. The user's list is input, not a closed boundary. Do not make every title a mandatory hire or impose every role on every project.
5. Use roles, responsibilities, deliverables and failure modes to generate targeted search vocabulary, source routes and compound research cells. Verify translations before treating them as reliable.

Suggested schema: source_role_id; original_label; original_group; normalized_concept; concept_type; specialties; responsibilities; decisions; inputs; outputs; handoffs; affected stakeholders; capabilities; artifacts; lifecycle; context/risk; evidence; sources; ambiguity; overlap; status; next action.

**Acceptance:** every supplied entry has an ID, original text, a processing state and a mapping or explicit unresolved reason. A pilot must show concrete responsibilities and evidence; a list of titles is not enough.

## Workflow after intake

1. **Integrity:** reconcile prior records where possible; distinguish observed facts, source claims, inferences, and leads. Unknown query/count/time stays unknown. Never reconstruct exact searches. Check current tool access.
2. **Source landscape:** map each platform down to relevant communities, archives and actual access routes; distinguish forge software, hosted services and projects. Map standards bodies to individual versions, research venues to papers and artifacts, and practitioner sources to actual work. Include social, forums, mailing lists, chats where accessible, code hosts and regional alternatives, registries, standards, research, conferences and postmortems. Verify activity and access.
3. **Research vocabulary:** generate query families from roles, system capabilities, artifacts, lifecycle, responsibilities, evidence, standards, failures and specialist terms. Include synonyms, acronyms and native-language variants. Search venues separately when combined rankings would obscure coverage.
4. **Coverage:** link planned cells, actual search runs, source versions, claims and roles to system nodes/edges and contextual responsibilities. Track planned, searched, thin, unknown, inaccessible, no evidence found, conflicting and justified not-applicable distinctly. Report unsearched combinations and selection rationale. Do not count a source or a cell as evidence of comprehensive coverage.
5. **Mechanism audits:** inspect actual sources and implementation for representative evaluators, standards, rubrics, conformance suites and operational assessments. Record inputs, computation or procedures, weights, outputs, applicability, missingness, N/A, versions, false results, gaming, correction, cost and independent validation. The user-supplied pre.dev estimator is one starting point.
6. **System and role research:** recursively decompose several very different systems and their interfaces. For each, find specialist disciplines, authoritative specifications, reference implementations, scientific research, practitioner discussions, incidents and meaningful evaluation techniques. Map supplied role responsibilities against concrete system components and lifecycle steps. Continue beyond the user's examples.
7. **Efficiency and frontier work:** study lean architecture, unwanted dependencies and features, code/binary/bundle size, algorithms, CPU, memory, I/O, latency, throughput, build time, GPU/energy and cognitive load as separate questions. Require workload, hardware, version, baseline, measurement uncertainty and behavior/compatibility preservation. Include dynamic entry points, reflection, plugins, rare paths and safety. Search current papers, release notes, proposals and niche communities while preserving older foundational work.
8. **Synthesis and validation:** develop conditional practices only when objective, applicability, evidence, unknown/N/A, false results, burden, gaming, ownership, exceptions and validation can be explained. Seek counterexamples and conflicting evidence. Separate repository-visible evidence from operational, physical, legal and user outcomes. Safety or regulatory certification requires qualified domain authorities.

## Per-batch loop

1. Pick an explicit compound scope and state why it matters.
2. Use genuinely different discovery routes and search terms, including counterexamples and specialist vocabulary.
3. Log exact queries, filters, tool, actual date/time and timezone if available, result window/pagination, access, returned/screened/opened/retained counts and stopping reason. Unknown is allowed.
4. Open primary sources and, when relevant, tool code or full study methods. Capture version and a precise locator. A snippet is a lead.
5. Record concrete findings, applicability, limitations, disagreements and follow-up. Do not equate owner marketing with independent validation.
6. Update source, role, evidence and coverage links; record unresolved cells and next batch in RESEARCH_STATE.md.
7. Report actual findings and gaps. Do not present new files, categories, counts or a single pilot as completed research.

## Existing access and boundaries

Exa, Parallel search/fetch, and connected X have been available; Parallel web_research previously returned HTTP 402 and Agent Reach CLI was unavailable. Verify current state. The user authorized Parallel and signed-in Brave/X for research. They did not authorize posting, contacting or messaging others.

Before model changes or context compression, update RESEARCH_STATE.md with current user instructions, original role-list status, files changed, exact research done, sources opened, unresolved gaps, next action, git status and remote state. Do not call the research complete because the repository exists or a checkpoint was committed.
