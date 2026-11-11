# Integrated research roadmap and execution contract

Status: historical planning handoff, 2026-11-10. Execution has begun; the current operating contract and active checkpoint in `RESEARCH_STATE.md` supersede historical sequencing. This document integrates the user's requests, the Computer System Atlas, existing research and a proposed execution sequence. It does not claim comprehensive coverage, independently verify the atlas, decide a scoring model, or authorize a blanket implementation of gates. The separate user-provided roles list is still pending.

## Mission and boundaries

Develop a generalizable, evidence-based way to discover and evaluate what quality means for a repository and the system, artifact, or work it supports. It must adapt to arbitrary domains, components, project stages and constraints, including obscure and foundational machinery. It should help people and AI agents identify missing expertise and work, select defensible practices, evaluate real outcomes, and eventually use appropriate checks and gates. Repositories are an entry point, not a complete window into running systems, physical devices, human experience or organizations. The intended audience includes people doing all kinds of work, not only professional software teams or public GitHub projects.

The atlas maps what could exist and how parts connect; this project investigates how to do and assess the relevant work well. Neither the atlas's examples nor current catalogues define the boundary. Treat any finite inventory, and this plan itself, as expandable and fallible. Preserve distinctions between a user's requirement, an observed fact, an atlas claim, an inference, and the research team's proposal.

Keep the user's breadth: from foundational math, data structures, compilers, operating systems, firmware and hardware to interfaces, production systems, security tools, entertainment, communications, finance, media, human support, economics and presentation; from single-purpose libraries to integrated products, physical and critical systems; from greenfield work to modifications, ports, replacements, compatibility, recovery, maintenance and retirement. Existing examples are probes, not exhaustive categories. Do not assume each system includes all components or requires a separate person for every responsibility.

## Starting position and source of truth

1. Read `AGENTS.md`, `RESEARCH_STATE.md`, this roadmap, `docs/execution-handoff.md`, `docs/failure-pattern-research-handoff.md`, `docs/atlas-context-recovery.md`, `docs/open-ended-systems-model.md`, `docs/research-model-v2.md`, `docs/research-protocol.md`, and `research/v2/integrity-and-migration.md`; inspect the actual repository and `git status` before edits. Consult the original shared atlas and pasted file identified in the recovery note, including its detailed content and the user's correction, when integrating them. Preserve user's local changes.
2. Existing catalogues, source routes, searches, stress cases and examples are partial research seeds. The historical matrix has known provenance defects. A browser example and a numerical count are not proof of domain coverage. Check actual raw records where available; never fabricate missing search terms, dates, counts or results.
3. The public remote exists at `https://github.com/harshgounder/repo-quality-framework.git`. Current planning notes and earlier local edits were uncommitted when this roadmap was written. Inspect current state rather than assuming the remote contains them. The user requested a GitHub repository, but this planning handoff does not itself publish the user's pasted conversation or private material. Review scope and sensitivity before any publication; do not silently discard existing edits.
4. The supplied atlas is not the separately promised list of roles. Preserve that distinction. Start independent research once the user switches to the execution model; the role list is pending input, not a reason to halt unrelated work. Integrate it when received.

## Model: connected dimensions, not a flat checklist

Maintain a navigable graph of evidence-bearing records, with stable IDs and links. Start with the existing v2 structure and extend it after checking compatibility rather than creating competing inventories. Represent a research cell as a scoped selection of values and relationships from at least:

- **Source and access:** platform, service, region, instance, community, collection, channel and actual access route; source type, author, institution, publication/version, date and language. Social posts are discovery and practitioner evidence, not automatically authoritative.
- **Search strategy:** question, query intent, terms/synonyms/acronyms, specialist jargon, translation, exclusions, search syntax, time window, ranking, pagination, access and sampling strategy.
- **System:** domain and purpose, environment, stakeholders, system boundary, subsystem, interface, dependency, algorithm/data structure, implementation/engine, hardware or physical process, and interactions; cross-layer paths are graphs, not a required linear stack.
- **Work and people:** role, specialty, responsibility, decision, handoff, affected person, artifact and lifecycle stage, including user, operator and independent reviewer perspectives. Track missing roles as missing responsibilities/decisions, not mandatory hires.
- **Context:** deployment and exposure, users, workload, resources, hardware, geography/jurisdiction, threat and hazard, criticality, organizational maturity, release and compatibility constraints, and whether assessment evidence is observable.
- **Quality and consequences:** correctness, fitness, performance, resource use, security, safety, resilience, usability and accessibility, privacy, maintainability, portability, interoperability, transparency, operations, cost and other context-specific outcomes; competing objectives, harms and failure modes.
- **Evidence and assessment:** research method, source claim and precise locator, test or measurement, actual behavior, standard and version, tool mechanism, human review, operational and external evidence, limitations, uncertainty, counterexamples and disagreements.
- **Time:** date of search and source, version, historical foundation, current state, emerging work and revalidation date. Recency alone is not a measure of quality.

A conceptual Cartesian product is much larger than can be fully searched; values are dependent and often open-ended. Do not manufacture coverage by multiplying labels. Record selected combinations and why, planned vs executed work, relevant unselected areas, uncertainty and next actions. Sample deliberately across specialist depth, source diversity, system types, risks, languages and opposing views; expand when discoveries expose important blind spots. Locally bounded saturation is a finding about a stated search, not a global completion claim.

## Execution sequence

### 0. Reconcile and set up a verifiable baseline

- Check repository and remote state; identify existing files, partial work, conflicting conventions and source-log gaps. Read the continuity and integrity records. Preserve original records; mark unrecoverable fields unknown and correct errors with provenance. Avoid inventing backfilled queries or evidence.
- Check current access to Exa, Parallel, X, browser and available search routes; the user authorized using them for research. Test actual access before relying on prior status; record failures and limits. No permission to post, contact or message others is implied.
- Produce a short baseline in `RESEARCH_STATE.md`: what exists, what was verified, actual git status, role-list state, gaps and next batch. Do not treat this setup as research completion.

### 1. Integrate the atlas into the system model

- Read both original user requests and both substantive responses. Capture concepts, components, interactions and specialist vocabulary at useful granularity, preserving source locations and separating candidate content from verified knowledge. Record open gaps instead of assuming a full closed inventory.
- Pilot a trace from a primitive to implementations and real system roles, and trace backwards from a product outcome to the machinery that can affect it. Include user-facing and human processes as well as computational internals. Distinguish real dependencies established by sources from hypothetical examples.
- Expand `research/v2/systems/` and the relevant model rather than dumping the whole atlas into an unstructured list. Each added entity needs a definition, parent/relations as applicable, source and state. Deduplicate carefully without erasing alternative terms or disagreements. Atlas integration is intake, not independent validation.

### 2. Turn source breadth into an executable campaign

- Expand `research/v2/source-routes.csv`, `campaigns.csv` and `query-bank.csv` using host → service → instance → community → collection distinctions. Cover regional code forges, social platforms including X and Reddit, discussion boards and forums, Q&A, developer communities, standards organizations, documentation, research archives and venues, conferences, universities, engineering blogs, design practitioners, package registries, source code, test suites, incidents, benchmarking and relevant niche communities. Find actual communities and routes; do not infer activity or access from a platform name.
- Build queries from role × system component × operation × quality/property × failure × assessment/evidence, with domain-specific synonyms, versions, negative searches and appropriate native-language terminology. Record translations as unverified until checked. Search independently enough that general search ranking does not erase niche sources.
- Select and document initial campaigns, including unselected breadth. Log exact run details per `AGENTS.md`. A search snippet is a lead; open the underlying material and inspect methodology or code where the claim depends on it. Follow citations, implementations, standards references and community discussions in both directions.
- A first current AI-lab/artifact sample now exists in campaign C25 and [its evidence note](../research/v2/agent-quality/current-lab-artifacts-and-frontier-evidence-2026-11.md). It is deliberately bounded: continue with paper-to-artifact status, lab and regional source routes, non-English discovery, and source-feed freshness instead of treating the initial names or portal counts as coverage.

### 3. Produce deep, contrasting worked investigations

Select several meaningfully different system/component-context combinations, drawing from the user's examples and beyond. Include at least one foundational/specialist engine, one user-facing distributed workflow, and one low-level, physical, or high-assurance context. The choice is illustrative, not a permanent priority or a claim that these exhaust the space.

For each pilot:
1. State the exact assessment object, boundary, use cases, dependencies, user outcomes and representative workload; identify unknowns and assumptions.
2. Decompose relevant internals and edges until the research question reaches concrete mechanisms, e.g. parsing/decoding and timestamps for media; numerical precision and degenerate cases for geometry; retry, reconciliation and support for payments. Investigate actual implementations rather than assigning a named engine to a product by assumption.
3. Map responsibilities and decisions across design, build, verification, release, operations and retirement, with affected users and human handoffs. Record role gaps even before the pending list arrives.
4. Find and inspect multiple appropriate evidence types: primary specs/versions, actual source and tests, research methods and datasets, practitioner discussions, failures/incidents, independent measurements and contrary evidence. Log inaccessible material and do not present vendor marketing as validation.
5. Derive quality questions and candidate checks with applicability and counterexamples. Specify what repository evidence can show and what needs runtime, user, physical, organizational or specialist evidence. Note tradeoffs and unknowns.
6. Publish a linked investigation note with the exact source locators, search runs, findings, conflicting results, gaps and next questions. A populated diagram or list of links alone does not pass.

### 4. Study actual raters and quality mechanisms

Retain the original request: find existing repo raters, maturity models, benchmarks, standards, rubrics and conformance systems, including obscure and specialized examples. For a representative mechanism, inspect its specification and implementation where accessible. Record target and inputs, observed evidence, algorithm/weighting and thresholds if any, default/unknown/N/A/exception behavior, version, output, strengths, blind spots, false results, incentives/gaming, costs and governance. Seek independent validation or critiques. Distinguish an estimate of licensing value from quality assessment: the inspected pre.dev script is one lead and was statically examined, not executed. Do not infer its findings apply to other versions.

### 4a. Discover subtle failures and derive meaningful checks

Execute `docs/failure-pattern-research-handoff.md` as a distinct, cross-cutting campaign. Research real complaints, defects and reports, including divergent behavior across paths and hidden change-propagation bugs; investigate causes, context, counterexamples and the real capabilities of tools and tests. Turn supported findings into conditional checks linked to the system and evidence model. The user-supplied modal transcript is a motivating hypothesis, not verified source code.

### 5. Research efficiency, cleanliness and bloat as measurable properties

Ask what work is necessary for the intended behavior and constraints, and investigate redundant complexity, dependencies and features as well as algorithmic and resource costs. Separate code and binary size from CPU, memory, latency, throughput, startup, I/O, bandwidth, GPU, energy, build time and maintainability. Establish a comparable baseline, workload/distribution, hardware, versions, confidence or variability, correctness and compatibility; look for performance regressions and alternative implementations. Analyze dynamic loading, plugins, rare paths, accessibility, security and safety before labeling code dead or removable. A smaller line count or dependency count is not automatically better. Follow current work and specialist practice while retaining foundational methods.

### 6. Synthesize and validate candidate framework designs

Only after sufficient scoped evidence, propose conditional quality objectives and candidate practices. For each: intended outcome; applicable object/context and stakeholder; evidence and source versions; procedure/tool and limitations; unknown and N/A handling; human review and decision rights; risks, conflicts, cost, gaming and exception process; and a way to validate that the check improves the outcome. Treat automated checks, expert judgment, process evidence and real-world outcomes as different evidence classes. Some critical claims need qualified specialists and external assurance; a repository badge cannot establish certification. Compare multiple framework architectures and scoring/gating options against worked cases and counterexamples before making product decisions. Avoid a universal score or mandatory gate by default.

### 7. Role-list intake whenever the user provides it

Follow the detailed `docs/execution-handoff.md` intake: preserve the original, stable IDs, group/order, duplicates, ambiguity and processing state; separately normalize titles, disciplines, responsibilities and authority. Map each entry to specializations, decisions, artifacts, handoffs, failures, evidence and applicability; compare with system research and expand the list without claiming it is closed. Every entry must have a mapping or explicit unresolved reason. Protect private material when publishing.

## Evidence and reporting contract

For every batch record: question and selection rationale; exact source routes and actual query or operation, filters, time/timezone when known, result window and pagination; returned/screened/opened/retained counts only when known; primary source/version and locator; claim versus interpretation; limitations and competing evidence; related system/role/context cells; next step. Keep counts attached to runs, not duplicated or summed across cells. Distinguish unselected, planned, searched, thin, no evidence found, inaccessible, conflicting, unknown, justified not applicable and locally saturated. Never infer no evidence from lack of access. Use existing status definitions and explicitly reconcile naming changes before altering them.

In every update, give concrete findings and their evidence, the exact scope covered, uncertainty, source/access limits, and next work. Counts are activity indicators, not quality or completeness. Record unsuccessful searches, counterexamples and negative evidence. Every meaningful checkpoint updates `RESEARCH_STATE.md` and links changed artifacts; preserve a concise next action that survives context loss. Re-read this roadmap after compaction instead of assuming a partial milestone means the objective is complete.

## Review criteria and self-correction

A useful batch must answer a real question more deeply than generic advice, with traceable sources and clear scope. A completed pilot must let another investigator follow the system path, role responsibilities, evidence and counterexamples, and understand which proposed evaluations apply and which require further work. Periodically review source and system diversity, narrow-language and popularity bias, stale versions, overreliance on social claims, inaccessible sources, unchecked assumptions, unintended mandatory gates and operational or human gaps. Reopen the matrix when new components, roles or evidence reveal omissions.

There is no defensible promise to enumerate literally every system, platform, profession or future technique. The practical commitment is an open-ended process that can expose gaps, expand systematically, document limits, and make strong claims only at the scope supported by evidence. Do not call the overall project finished because this plan, a role catalog, a pilot, a repository or a research matrix exists.
