# Research model v2: a linked coverage system

Status: working design, 2026-11-10. The v1 matrix remains historical and requires reconciliation. This model does not claim the source universe or any framework is complete.

## Why change the model?

A platform, a search, a document, a claim, a project, and a quality requirement are different objects. Putting them in one CSV row caused bundled platforms, repeated result counts, reconstructed queries and a false impression that a listed source had been searched. It also hid disagreement and made coverage by community, language, artifact or responsibility hard to calculate.

## Linked records

1. **Venue**: named host, search engine, archive, community, institution or event. Model host → service → instance → community → collection separately; one entity may play multiple roles.
2. **Search route**: venue + access method + geographic/language scope + discovery mechanism + access state. A platform can have several routes, e.g. native search, external indexing, API, browsing a specific forum, or a mailing-list archive. A working route is not proof that its whole platform is searchable.
3. **Research question and vocabulary**: intent, target concepts, synonyms, translations, exclusion terms and exact venue-specific syntax. Separate generated search plans from searches actually executed.
4. **Campaign and planned coverage cell**: a declared combination of venue/route × query family × source role × artifact × responsibility × lifecycle × stakeholder × context, with time, language, method, selection rationale and priority. Each value can be a set; every set must be expanded or qualified in reports. Broad discovery cells do not establish coverage of each member.
5. **Search run**: immutable actual query, filters, date and time or explicit unknown, account/access route, tool, result window, pagination, returned count, screened count, retained count, stops and errors. A run can serve multiple planned cells; counts belong to the run, never copied and summed across cells.
6. **Source and version**: canonical identity, authorship, source type, publication/edition, access and snapshot/locator. Multiple routes can find one source; one venue hosts many sources.
7. **Evidence/claim**: source locator, precise claim, source statement versus our interpretation, study population and method, uncertainty, conflicting evidence and date. One source can support multiple claims or contradict another.
8. **Assessment object and context**: artifact, release, dependency, product, operation, organization, community or ecosystem, with appropriate metadata. Do not silently apply observations from one unit to another.
9. **Mechanism**: target property, input, detection, computation/weights, unknown/N/A/exception behavior, output, evidence provenance, access/safety, cost, governance and independent validation.
10. **Candidate practice or gate**: desired outcome, applicability, evidence and decision rights, affected stakeholders, harms, alternatives, enforcement, appeals and validation. These are future synthesis objects, not settled requirements.

Relations: venue contains community; route accesses venue; campaign selects planned cells; run executes a query against a route and covers scoped cells; result links run to source; source supports or disputes claim; claim informs a mechanism or candidate practice; practice applies conditionally to an assessment object and context.

## Dimension catalog

The structured value inventory is research/v2/axis-values.csv. Values are seeds rather than exhaustive enumerations. It separates: source identity and role; geography/language; query intent and terminology; discovery and access; artifact and assessment unit; stakeholders and responsibilities; lifecycle; context and risk; evaluation mechanism; outcomes and harms; time/version; and research method. Add values and narrower children with definitions as discoveries justify them.

Important combinations include:
- research dataset × publication × data steward × reproducibility × archived release × evidence accessible to third parties;
- private service × deployment × operator/SRE × incident response × sensitive environment × operational telemetry;
- public accessibility library × release × disabled end user × assistive technology × compatibility × human evaluation;
- small hardware project × fabrication × manufacturing engineer × safety × CAD/BOM/firmware × physical review;
- security-critical OSS dependency × adoption × procurement/legal/security × origin and maintenance × supply chain × attestations and human review.

These examples are hypotheses to search, not predetermined requirements.

## Coverage and stopping

The full conceptual space is the product of values and their relations. Applicability is a relation requiring justification, not a guess from missing rows. Preserve multi-valued identities and dependencies; for example, a paper may be found on X, archived on arXiv and published in a journal. A plan must expose unselected, planned, in-progress, searched, thin, inaccessible, conflicting and locally saturated scopes. Record no evidence found separately from inaccessible and not applicable.

Campaigns in research/v2/campaigns.csv provide concrete proposed combinations, entry routes, queries and deliverables. They are queued unless an actual run is linked. Coverage reporting must measure planned/run cells and show exclusions, route failures and selection rationale; it cannot use source counts as coverage. Local saturation requires documented independent query variants and source types with no substantive novelty, bounded by date/language/access and reopened as sources evolve.

## Repair and migration

- v1 files remain preserved as historical research; their exact-query and counts need reconciliation against primary tool records before reuse.
- Results, sources and claims need distinct IDs before migrating; do not invent per-query counts or manufacture search timestamps.
- Correct known swapped evaluator follow-ups and missing log references; tag unreconciled rows in the integrity ledger.
- New source routes are candidates unless primary pages were opened; discovery sources are not proof of platform activity or authority.
- The public GitHub repository is already created; local changes require an explicit push to update it.
