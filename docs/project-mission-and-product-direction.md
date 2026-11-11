# Project mission and product direction

**User correction, 2026-11-11:** the project is to create a broadly usable, exceptionally capable repository and system-quality framework, including contextual practices and gates that help people and AI produce complete, high-quality work. It is not primarily a project to solve all historical bugs or build a bug database. Historical failures, fixes, discussions and tests are one important evidence stream for designing and checking the framework, alongside standards, professional practices, designs, research, raters, benchmarks, successful projects and lived user/operator experience.

## Intended outcome

For a specific work item and its context, help a person or AI agent understand what a well-engineered result requires, identify missing responsibilities and weak areas, choose the relevant practices, assemble meaningful evidence, and improve and re-evaluate the work over its lifetime. Repositories are an entry point: the work can involve code, data, research, documentation, designs, tools, hardware, services, products and other artifacts and their real environments. The framework should generalize without assuming that all projects have the same purpose, stack, team, budget, danger or maturity.

The user's ambition is maximum practical quality and completeness for the situation: technical correctness and reliability; security and safety where applicable; lean and efficient operation; usability, accessibility, aesthetic and interaction quality; coherent architecture and maintainability; reproducibility and releases; documentation and onboarding; privacy, legal and governance obligations; operational support, recovery and observability; and domain-specific properties and professional responsibilities. These are starting directions, not a final exhaustive taxonomy or a mandatory checklist for all work. A small experimental library, a production payment system and a physical device must be assessed differently, and evidence may lie outside source control.

## Proposed product-facing capabilities to research and eventually build

The following are hypotheses and intended deliverables, not completed features or settled universal rules:

1. **Context and applicability:** identify the kind of work, system boundaries, lifecycle, stakeholders, relevant constraints and layers, including non-code and physical or organizational context; show unknowns and allow users to correct assumptions.
2. **Responsibility and quality map:** surface applicable professional decisions, deliverables and cross-role handoffs, as well as system- and domain-specific obligations. Make missing work visible without assuming every project needs a specialist or a particular artifact.
3. **Knowledge and evidence base:** connect practices, standards and editions, tools, exemplars, research, user needs, benchmarks and historical failures/fixes to applicability, rationales, counterexamples, cost and uncertainty. Historical defect/fix corpora feed this layer; they are not the product's organizing objective.
4. **Assessment and improvement:** translate the map into understandable findings, evidence, gaps, priorities, tradeoffs and an actionable improvement plan. Support human expert judgment, direct tests and real-world evidence; distinguish measured, inferred, unknown, not applicable and inaccessible.
5. **Contextual checks and gates:** evaluate possible automated checks, manual reviews, release conditions and ongoing monitoring for their actual decision context. Each needs a purpose, inputs, explicit applicability, evidence, limits, owner, escape/exception path and validation of usefulness and burden. Whether a gate blocks, warns or does not apply depends on the context and governance; no single mandatory list or score is decided.
6. **Build and maintenance workflows:** apply the framework during planning, implementation, review, operation, release and evolution, for existing and new repositories, and both human and AI contributors. Track versions and changing requirements; help people act rather than just label the repo.
7. **Presentation and human experience:** make both the framework's output and the repository's user-facing surfaces clear, coherent and well designed. A polished README is useful but cannot establish underlying product, engineering or operational quality.

These capabilities are a target for research and prototyping, not a claim that the current repository implements them. Study actual raters, standards, tool implementations and comparators, as originally requested, and keep expanding across specialist systems and sources. The originally supplied pre.dev script was inspected as a starting point: the recorded snapshot calculates an estimated non-exclusive licensing value from heuristic code/history token counts; it does not itself establish repository quality. Do not conflate it with a validated quality score or claim its owner's wider products have no other features.

## Evidence and discovery in service of the mission

The user expects deep, open-ended, large-scale discovery across systems, artifacts, professions, sources and regions, including thousands of meaningful candidates per relevant class. Candidate counts are not evidence that any item was reviewed or that quality is established. Avoid restricting research to familiar app categories, source-control files, defect reports, social popularity or one ecosystem. Use standards and expert practice as well as counterexamples and observed failures, compare alternatives, and assess properties that have no known historical bug.

The SQLite evidence graph under `foundation/` is a limited experimental research tool for preserving source-attributed links. It is not a repository-quality rater, a complete knowledge base, the framework, or the main objective. Its example is a defect history because that happened to be the available seed; future examples must also link positive practices, responsibilities, standards, design decisions, quality properties, measurements and contextual checks. Existing records and the historical-failure research are preserved as useful evidence.

## Immediate work priorities

- Audit and deepen existing rater and standards work: pin versions and examine actual inputs, mechanism, applicability, unknowns, limitations and evidence of effectiveness. Distinguish a valuation estimate, criticality signal, security check and overall quality assessment.
- Develop an expandable responsibility × quality-property × system/artifact × lifecycle map grounded in primary sources and professional practice; include design quality, clean/efficient implementation, operations and context beyond software code. Keep the Atlas and prior lists as seeds, not the boundary.
- Trace several contrasting examples from context and desired outcome through responsibilities, candidate practices, evidence, checks, tradeoffs and an improvement decision. Include positive engineering practice and at least one case where a proposed check is irrelevant or harmful; historical defects can inform but need not define examples.
- Prototype a small end-to-end assessment/improvement workflow only after its evidence, applicability and validation plan are clear. Evaluate usability and false findings; report what it cannot assess. Build on existing research rather than treating the evidence database as the product.
- Continue broad and specialist discovery and compare existing projects' implementations and licenses; include latest research as it develops. Keep the multi-dimensional search ledger, explicit gaps and independent review, with no claim of full coverage from a finite sample.

## Current state

This repository has research, partial audits, source leads, a limited evidence graph and one importer. It does not yet implement the intended quality framework, production-ready assessment, complete standards map, mature rater comparison, validated gates, or comprehensive system and role coverage. The separately promised role list remains pending. No particular score, preset, gate policy or artifact structure is imposed by this document.
