# Preliminary findings and leads

**Evidence status:** orientation only. These notes preserve leads from the previous reconnaissance. They are not an exhaustive comparison, and exact original search strings/screening counts were not retained. Open primary sources and revalidate versions before relying on any detail.

## Distinct approaches observed

| Candidate | Initial read | What to investigate next |
|---|---|---|
| [OpenSSF Scorecard](https://scorecard.dev/) | Automated security and software supply-chain checks, producing check-level results and an aggregate score. It is security-oriented, not a complete account of repository quality. | Rule set and weights/aggregation by version; evidence collection; unsupported contexts; false positives; relation to actual outcomes; update and governance model. |
| [OpenSSF Best Practices Badge](https://www.bestpractices.dev/en/criteria) | Criteria-based project self-assessment with evidence and badge levels; broader than an automated scan, but still a particular open-source scope. | Criterion rationale, evidence/verification, level thresholds, maintenance burden, adoption and validity. |
| [OSPS Baseline](https://baseline.openssf.org/) | A versioned security baseline with requirements for project maturity/profile. | Current baseline levels, requirement mapping, applicability, exceptions, evidence, change process, and fit outside its intended scope. |
| [CLOMonitor checks](https://clomonitor.io/docs/topics/checks/) | Project health monitor with code, community, documentation, and related checks; some checks are repository/file-presence oriented. | Full rules and scoring, source-of-truth behavior, applicability, project selection, outputs, and how check results correlate with health. |
| [LFX Health Score](https://insights.linuxfoundation.org/docs/metrics/health-score) | Project-health metrics spanning activity/community dimensions. | Formula, data sources, weighting, bias against project types/lifecycles, freshness, and validation. |
| [GitHub Community Profile](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories) | Host-specific indicators for community-facing repository files and practices. | Current checklist, exact platform behavior, boundaries, and difference between discoverable files and actual community quality. |
| [REUSE](https://reuse.software/spec/) | A focused specification and tooling approach for licensing/copyright metadata in source files. | Compliance evidence, tool behavior, applicability to different artifact types, and integration with broader legal/provenance responsibilities. |
| [pre.dev licensing estimator](https://api.pre.dev/api/code-licensing/estimate.mjs) and [codebase docs](https://docs.pre.dev/labs/codebases) | A script/API that estimates licensing value from selected code and history signals. This is not a general quality rater. Earlier reconnaissance also noted a quality grade/rubric whose public mechanism was not established. | Re-run safely against a test/public repo; inspect code/docs and disclosures; separate valuation, licensing, and quality signals; determine the quality grade's public evidence and limits. |
| [Repository Standards](https://github.com/repository-standards/core) | A prescriptive set of numbered repository rules with profiles and validation concepts; a useful design reference, not a neutral universal standard. | Rule rationale, profile choices, tooling assumptions, POSIX/Node/jq constraints, accessibility for other stacks, governance, adoption, and extension model. |
| [Microsoft Agent Readiness Check](https://github.com/microsoft/agentrc/blob/main/docs/concepts.md) | Agent-oriented readiness model with five levels and nine pillars, according to initial docs. It is a specialized lens, not a general repo-quality model. | Current concept/rubric, evidence, intended user, validation and boundaries; what agent readiness reveals about future repository needs. |
| [eyebrow](https://eyebrow.cc/docs) | AI-tool integrity/readiness checks were surfaced; docs reportedly caution that it is not a full code audit or safety guarantee. | Inspect current docs/rules/implementation and exact boundary language; distinguish repository metadata from behavior or security assurance. |

## Standards and adjacent frameworks surfaced

- [NIST SSDF](https://csrc.nist.gov/Projects/ssdf/) offers a secure-development practice framework; it is risk-informed security guidance rather than a universal repository checklist.
- [ISO/IEC 25010](https://www.iso.org/standard/78176.html) is a software/product quality model; investigate current edition, quality characteristics, scope, and how characteristics translate (or fail to translate) into repo evidence.
- [OWASP SAMM](https://owasp.org/projects/samm) is an application security maturity model; study maturity staging, assessment mechanism, and context.
- [SLSA build provenance](https://slsa.dev/spec/v1.2/build-provenance) and [CycloneDX](https://cyclonedx.org/) are supply-chain/provenance or BOM-related standards, not general quality measures.
- [ECMA-424](https://ecma-international.org/publications-and-standards/standards/ecma-424/) is relevant to agentic AI concepts; inspect actual scope before using it as a repo requirement source.
- [FAIR4RS](https://github.com/force11/FAIR4RS) concerns research software; assess its research artifact scope and guidance status.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) defines web accessibility criteria; relevance to repository content, demos, and shipped products varies by artifact.
- [Buf breaking-change detection](https://buf.build/docs/breaking/) is a focused API compatibility mechanism, useful as an example of domain-specific gates.
- [Kubernetes PRR](https://www.kubernetes.dev/resources/keps/1194/) illustrates production readiness review for Kubernetes features; investigate transferability and review process.
- [IEEE Computer Society software engineering body of knowledge](https://www.computer.org/education/bodies-of-knowledge/software-engineering) may help map professional responsibilities; it is not itself a repo scoring system.

## Coverage and maturity caution

The previous reconnaissance found an OpenSSF Scorecard comparison against a February 2026 OSPS Baseline version reporting 8 covered, 17 partially covered, 31 gaps, and 3 not observable. Treat these counts as a dated, version-specific illustration of the difficulty of automating standards coverage; re-open the [coverage mapping](https://github.com/ossf/scorecard/blob/main/docs/osps-baseline-coverage.md) and current baseline before citing the numbers as current.

## Practitioner/social leads

- An X post by [eyebrowCC](https://x.com/eyebrowCC/status/2108455520164319385) surfaced an AI-tool integrity badge/check concept. It is a discovery lead; inspect the underlying docs and implementation before attributing claims.
- A post by Oren Melamed surfaced a practitioner claim that AI coding shifts bottlenecks toward review, architecture, and documentation. The exact source link was not preserved in the prior notes; rediscover and record it before using the claim.
- Social and X observations should inform vocabulary and counterexamples, then be corroborated where possible. They do not establish consensus or standards.

## Useful comparison axes emerging from the leads

1. **Scope:** security, licensing, community health, agent readiness, compatibility, product quality, research software, or broad project stewardship.
2. **Evidence:** files/metadata, source inspection, CI/workflow state, API/platform signals, self-attestation, expert review, or operating outcomes.
3. **Decision output:** binary check, maturity level, category score, aggregate score, badge, recommendations, or valuation estimate.
4. **Applicability:** universal, profile/level-based, ecosystem-specific, artifact-specific, organization-specific, or user-configured.
5. **Assurance boundary:** what passing demonstrates, what it does not demonstrate, and which claims would be unsafe to infer.
6. **Change model:** versioning, maintainers, appeals, exceptions, stale evidence, and migration behavior.

These are working comparison dimensions, not a final taxonomy.
