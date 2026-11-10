# Research protocol

## 1. Research question

What should a repository-level framework inspect, recommend, measure, or gate so repositories across different kinds of work become trustworthy and useful throughout their lifecycle, without imposing irrelevant burdens or implying guarantees it cannot support?

Related questions:

1. What do existing raters, badges, standards, and automated checks actually measure?
2. What important responsibilities are omitted, or measured only weakly?
3. Which obligations vary by artifact, audience, risk, maturity, deployment model, jurisdiction, or lifecycle stage?
4. What evidence can establish a requirement, and what can be checked automatically, manually, or only in operation?
5. How do users and maintainers experience these systems, including false positives, gaming, maintenance burden, exclusion, and failures?

## 2. Matrix dimensions

The matrix is a structured coverage model. Each row is a scoped research cell; not every value must be crossed with every other value. Add dimensions when evidence shows the model is missing a meaningful distinction.

| Dimension | Example values or questions |
|---|---|
| Source platform / venue | Code forge, standards body, academic index, social network, forum, mailing list, issue tracker, conference, documentation portal, practitioner publication |
| Source/evidence role | Normative standard, consensus baseline, empirical study, tool/rater, platform heuristic, maintainer report, practitioner opinion, incident/postmortem |
| Query family | Rater discovery, mechanism audit, omitted-practice search, failure/counterexample, applicability, adoption/burden, gaming/metric validity, trend/version check |
| Exact query and filters | Verbatim query, language, date range, domain/repo filters, sort/ranking, account/access context, result limits |
| Artifact archetype | Library/package, application/service, website, CLI, infrastructure, data/dataset, research software, model/ML artifact, docs/content, monorepo, template, firmware, educational/example repo, small script |
| Responsibility domain | Correctness, testing, security, privacy, safety, accessibility, operability, reproducibility, provenance, licensing/IP, governance, documentation, UX, performance, sustainability, interoperability, dependency health, maintainer health |
| Lifecycle phase | Initiation, contribution, review, build, release, deployment/use, incident response, maintenance, migration, archival/end of life |
| Context | Risk/impact, public/private, scale, maturity, team capacity, regulated status, language/region, user vulnerability, criticality, threat model |
| Evaluation mechanism | File rule, metadata rule, static analysis, test, attestation, human review, operational metric, community evidence, policy/process, composite score |
| Population / unit | Repository, release, workflow, organization, maintainer team, dependency graph, deployed service, research artifact |
| Time/version | Search date, standard/tool version, historical interval, freshness expectations |
| Access | Public, authenticated, API, rate-limited, gated, unavailable, language-limited |
| Outcome | Finding, check, requirement, evidence type, risk reduction, usability/adoption, false-positive/negative, cost, known gap |

## 3. Compound coverage

The theoretical space is the product of these dimensions, but a literal exhaustive crawl would be both infeasible and misleading. Use a staged design:

1. **Map the axes:** enumerate candidate values and document why they matter.
2. **Broad discovery:** run general searches across each source family and query family to reveal missing vocabulary and source types.
3. **Mechanism audits:** select representative raters/standards and inspect primary documentation, implementation, examples, versions, and known limitations.
4. **Cross-axis sampling:** deliberately cover important pairs and triples, such as artifact × lifecycle, domain × evidence mechanism, and risk × gate strictness. Add higher-order combinations when risk, evidence, or user stories demand them.
5. **Counterexample sampling:** search for repositories that passed a tool/badge yet failed, failed a check yet worked well, or could not comply for justified reasons.
6. **Gap review:** inspect under-covered regions, non-English sources, non-GitHub hosts, less-common artifact types, and underrepresented roles.

Keep a coverage table or matrix view that shows which combinations were selected, why, and what remains. Any prioritization or omitted region must be recorded; do not present sampling as exhaustive coverage.

## 4. Query families

Adapt these families to each venue; record the exact resulting query and filters:

- **Discovery:** repo quality evaluator, project health index, repository score, software project assessment, repository checklist, project readiness.
- **Mechanism:** how a named tool/standard computes results; rule catalog; weight; threshold; missing/unknown handling; versioning; evidence source; CI integration.
- **Coverage and omissions:** what a named rater does not check; blind spots; non-applicable checks; unsupported ecosystems; manual-only criteria.
- **Validity:** correlation with incidents, defects, adoption, maintainability, security outcomes; validation study; predictive validity; construct validity.
- **Operational experience:** false positives, maintenance burden, adoption, complaints, bypasses, workarounds, successful use, abandoned tools.
- **Counterexample / failure:** incident, supply-chain compromise, data loss, inaccessible product, unreproducible paper, broken release, bus factor/maintainer crisis, despite passing badges/checks.
- **Context and applicability:** small project vs critical system; library vs service; research/data/ML/infra; regulated/public-sector; solo maintainer; private repository.
- **Incentives / gaming:** Goodhart effects, badge chasing, checkbox compliance, metric manipulation, security theater, performative docs.
- **Version and governance:** revision history, change process, release cadence, maintainers, deprecation, appeals, evidence provenance.
- **Future and emerging practice:** AI-generated changes, agent-readable instructions, provenance/attestations, reproducible builds, emerging domain guidance. Date-stamp claims.

## 5. Evidence handling

For every claim, capture a source record with at least: stable URL/identifier, title, authoring body, publication/update date, access date, version, source type, claim supported, excerpt or location reference, applicability, limitations, and confidence.

Evidence classes (do not collapse them into a single popularity score):

1. Primary normative text or official specification.
2. Primary implementation/documentation from the tool or platform owner.
3. Peer-reviewed or methodologically transparent empirical research.
4. Incident report, postmortem, audit, or case study with direct evidence.
5. Practitioner/maintainer account with identifiable context.
6. Community discussion or social post, useful for leads and lived experience.
7. Search snippet, secondary summary, or marketing claim, useful only for discovery until verified.

Prefer independent corroboration for consequential claims. Record evidence against as well as in favor. For conflicting sources, preserve dates, definitions, populations, and likely reasons for disagreement.

## 6. Search and screening rules

- Search broadly, then open primary sources and relevant implementation artifacts.
- Log the exact query, chosen platform/tool, filters, sort, date range, result count, screened count, retained count, and reason for stopping.
- Distinguish results returned from results actually screened and sources actually read.
- Include language and region where supported. Translate queries when useful and record the language.
- Record login/API/rate-limit restrictions and whether a result is only a snippet.
- Deduplicate sources while preserving where each was discovered.
- Record null searches; they can show vocabulary mismatch or indexing/access limits, not proof that no evidence exists.

## 7. Status and stopping rule

Use the statuses defined in the README. Mark a scoped cell `saturated` only after multiple query variants and relevant source types stop yielding materially new mechanisms or evidence, with the time window and limits stated. Reopen it when a standard/tool changes, new evidence appears, or its scope changes. Never report global completeness from local saturation.

Before synthesis, report coverage by dimension and important compound combinations; unresolved conflicts; inaccessible regions; language/region imbalance; thin evidence; and claims supported only by social/marketing sources.

## 8. Eventual evaluation of checks and gates

For every candidate requirement/check, eventually capture: intended outcome; applicability conditions; rationale/source; unit of assessment; required evidence; automated/manual/operational method; severity and remediation; unknown/non-applicable semantics; failure modes; false positive/negative risk; bypass/gaming risk; maintenance cost; accessibility and small-team burden; domain/context adaptations; validation evidence; ownership/versioning; and appeal/override path. This is a research schema, not a settled gate design.
