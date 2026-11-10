# Open-ended systems research model

**Status:** working research model, 2026-11-10. This extends the linked research model; it does not assert that the examples, components or obligations below are complete.

## User's correction

The target includes any system or part of one: new implementations, rewrites, compatible replacements, extensions, ports, integrations and research prototypes. Examples include browsers, OS kernels, game engines, firmware, compilers, trading platforms, mobility systems, maps, defensive security tools, reverse-engineering suites, video platforms and codecs. These are stress cases, not a closed list. A generic repository checklist and a fixed catalog of technology profiles cannot determine the engineering work required for every possible system.

## A system is a graph, with an unknown frontier

Represent a target as a graph rather than force it into one product category:

- **Nodes:** objectives; stakeholders; system-of-systems; system; subsystem; component; protocol; algorithm; interface; data and state; hardware; toolchain; release artifact; operating environment; human or organization; evidence; decision.
- **Edges:** contains, calls, communicates, depends on, exchanges data with, controls, observes, compiles to, runs on, is supplied by, verifies, is governed by, or causes external effects. Edges can cross repositories, teams, vendors and physical boundaries.
- **Views:** user journeys, functional behavior, architecture and runtime flow, data and state, physical deployment, operational ownership, threat and trust boundaries, lifecycle/supply chain, legal and domain obligations, economics, quality attributes, and evidence. Each view can reveal nodes another missed.
- **Unknowns:** explicit unknown components, undocumented dependencies, third-party behavior, inaccessible standards and unobserved use cases. Record why an exploration stopped and what could change the map.

Decompose recursively until the component and interaction are specific enough to identify behaviors, external contracts, failure modes, specialist knowledge, and meaningful evidence. Examples are illustrative and must not be mistaken for complete architectures.

## Independent dimensions and combinations

The research matrix must connect the **source/search world** to the **target-system world**. It is not enough to cross a language with an artifact.

1. Problem domain, intended users and affected people.
2. Target transformation: new system, partial implementation, rewrite, port, compatible replacement, integration, optimization, maintenance, migration or retirement.
3. Scale and boundary: line/algorithm, component, subsystem, complete product, fleet, ecosystem, cyber-physical system, or system of systems.
4. Functional capability, user journey and observable contract.
5. Architecture, execution, data, state, physical interfaces, protocols, algorithms and dependencies; relationships between components.
6. Language, runtime, compiler, OS, architecture, accelerators, devices, frameworks, codecs and third-party versions.
7. Inputs, adversarial/malformed inputs, data distributions, concurrency, hardware, network and workload.
8. Stakeholders, specialist disciplines, governance and decision rights.
9. Quality properties: correctness, functional completeness, interoperability, security, privacy, safety, usability/accessibility, reliability, availability, performance, resource efficiency, maintainability, testability, portability, reproducibility, observability, evolvability and sustainability.
10. Domain-specific properties, e.g. order matching and settlement integrity, media timing and fidelity, browser isolation and standards conformance, spatial accuracy and routing behavior, compiler semantic preservation, device timing, financial risk controls and human factors.
11. Lifecycle, deployment, compatibility, migration, fault/recovery, incident and decommissioning.
12. Consequence, threat, uncertainty, environment, jurisdiction, certification and contractual context.
13. Evaluation mode and evidence, including independent implementations, reference datasets, field trials, physical tests, formal evidence and operational telemetry.
14. Source route, community, terminology, language/region, date/version, access, research method and evidence strength.
15. Tradeoffs, constraints, cost, reversibility, unknown/N/A and decision authority.

These axes are not assumed independent. A single system may require simultaneous combinations, such as real-time scheduling × firmware × hardware fault × safety-critical deployment × recovery and certification; or video streaming × codec × client device × network variability × copyright/rights handling × accessibility. Higher-order interactions should be selected because of realistic behavior, risk or a gap, with rationale and unsearched combinations preserved.

## From an arbitrary brief to a research plan

1. Capture intended capability, operating context, scope and non-goals. Ask for missing critical constraints when required; keep uncertainties open.
2. Decompose recursively using multiple views. Trace upstream/downstream dependencies, boundaries and external systems. Identify optional and rare paths.
3. Identify candidate specialist disciplines and affected people for every node and consequential edge. Include roles beyond software: safety, human factors, hardware, finance, legal, manufacturing, operations, data, localization and domain experts.
4. Generate a question set per node and interface: intended behavior, contracts, assumptions, inputs, state, invariants, failure modes, risks, abuse/misuse, degraded operation, performance and resource constraints, accessibility, operational needs and maintenance.
5. Discover the relevant standards, protocols, conformance suites, mature reference implementations, specifications, research, incident reports, specialist communities, regulatory material and domain practices. Version, regional authority and access must be checked.
6. Construct an evidence plan using applicable techniques: correctness and conformance suites; fuzzing; differential, metamorphic, property-based, model-based and formal methods; profiling; physical experiments; accessibility studies; security testing with authorization; end-to-end and operational evaluation.
7. Cross-check component interactions, emergent behavior and system-wide outcomes. Component-level success cannot by itself establish whole-system success.
8. Derive conditional practices or gates only after the intended decision, applicability, evidence, uncertainty, cost, ownership, false positives/negatives, failure consequences and override are understood.
9. Track coverage in both directions: system nodes/edges × obligations × evidence, and source routes × research questions × contexts. Show the unmapped and unsearched frontier.

## Quality boundaries

“Leanest,” “cleanest,” “fastest” and “best” require an objective and constraints. A browser may optimize startup while preserving compatibility; an exchange may prioritize correctness and predictable tail latency; embedded firmware may need timing and memory bounds; an accessibility function may impose necessary resource costs. Measure representative workloads, correctness, variance and tradeoffs. A repo can provide source and build evidence; operation, physical effects, licensing obligations and actual user outcomes often require external evidence.

Safety-critical and regulated contexts require domain specialists and applicable authorities. A generic framework can identify evidence and missing expertise; it cannot by itself certify a system.

## Research artifacts

- systems/stress-cases.csv: illustrative system decomposition and open questions.
- systems/capability-catalog.csv: reusable capability families for discovering components across examples and unseen systems.
- systems/compound-research-cells.csv: concrete proposed or thin-evidence intersections; queued means not researched.
- systems/domain-sources.md: primary source anchors and scope limits.
- Existing performance and freshness research remains applicable, but all catalogs are seeds. No example list is exhaustive and no score or gate is finalized.
