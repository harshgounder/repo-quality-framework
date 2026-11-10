# Discovery round 2: standards, communities, forge scope, and counter-signals

**Research date:** 2026-11-10 (Asia/Kolkata)
**Status:** discovery and source-opening pass; no cell is saturated and no framework decision is made.

## Why this round

The first mechanism sample leaned toward evaluators and empirical papers. This round probes the source and artifact axes more directly: practitioner venues, regional forge documentation, standards with different units of quality, and studies that can challenge claims about score or badge usefulness. Queries were run through Exa, Parallel search/fetch, and the connected X search route. Agent Reach was unavailable in the local environment; its doctor and update commands both returned command-not-found. Parallel's dedicated web_research route had previously returned HTTP 402, so this round used its ordinary search/fetch route. The signed-in X connector returned noisy, weakly relevant results; no post was treated as substantive evidence from those searches.

Exact searches, filters, result counts, and fetch IDs are in search-log.md sections E-003 through F-007 and the corresponding rows in search-ledger.csv.

## What the sources add

### Community expectations are negotiated, not self-evident

The Open edX discussion documents a concrete tension: a team disabled pylint because it was not a priority, while participants debated whether linting was an undocumented repository requirement, which tools should qualify, and how to balance common expectations with project autonomy. That is useful design evidence about applicability and governance, not a universal verdict about linting.

The Sustain Open Source Forum thread describes a template intended to help projects cover description, contribution, conduct, governance, license, ownership, issue/PR forms, security, funding, and citation. It is a proposal and community discussion; it does not establish that adopting the files improves outcomes.

An individual Rust forum thread lists local gates such as formatting, linting, tests, and dependency checks, while also stating language-specific style preferences. It is an anecdotal, language-specific practice lead, not a cross-project requirement.

### Professional practice can be much broader than files or CI

Geomys's Standard of Care is a practitioner-defined policy scoped to its maintained projects. It covers review, complexity control, static analysis, compatibility, ongoing maintenance, dependency strategy, phishing-resistant authentication, vulnerability handling, and other operational responsibilities. It is an important practitioner source; its resourcing assumptions and project scope limit direct transfer to volunteer, solo, non-Go, or low-risk work.

Zalando's 2019 release process describes human review, sustainability questions, licensing and confidentiality/IP checks, basic communication and policy files, and a decision to release, request changes, or reject. The post says details of later monitoring and graduation/archive criteria would follow in a later post, so it does not establish the complete lifecycle process.

### Standards have different units and boundaries

- ISO/IEC 25010:2023 defines a product-quality model for ICT and software products, with nine characteristics and subcharacteristics. It is a product model, not a checklist for repository files or community health.
- ISO/IEC 25040:2024 is the SQuaRE quality evaluation framework. Its official page exposes scope/version metadata, while the complete standard text is not available in the fetched excerpt.
- ISO/IEC 5259-4:2024 covers data quality process for analytics and machine learning. This makes dataset and ML quality a distinct lane rather than an incidental software-code concern.
- NIST SSDF 1.1 provides secure software-development recommendations. Security remains one responsibility domain among many.
- ACM SIGSOFT Empirical Standards describe evidence expectations for software-engineering studies. They may help assess research quality in this project, but they are not product-quality criteria.

These sources are useful anchors, not evidence that one model can be applied uniformly across repository types. Edition, normative force, complete text access, and applicability need to be recorded in each later mechanism audit.

### Validity evidence is mixed and construct-specific

The 2018 ICSE study analyzed 294,941 npm packages, surveyed npm developers, and examined eight hypotheses using regression and time-series regression-discontinuity designs. Its abstract reports that many badges acted as reasonably reliable signals in that npm sample. This is positive counter-evidence to treating all badges as empty decoration. The result remains badge-specific and ecosystem-specific; it does not validate arbitrary badge catalogs or a whole-repository score.

The NDSS 2024 study asks whether GitHub stars measure project importance. Its dataset contains 925,978 observations across PHP, Ruby, and JavaScript and compares stars, downloads, and detected JavaScript deployments. The abstract reports weak and language-varying star/download relationships (0.47 in PHP and 0.14 in JavaScript) and moderate correlations between stars or downloads and detected JavaScript deployments (0.61 and 0.63). This is evidence about popularity/importance proxies in those contexts, not a direct measure of software quality.

A 2024 tertiary study on source-code metrics synthesizes secondary studies and reports contradictory prior results, concentration on object-oriented systems, and limited, uneven links between metrics and external attributes. This strengthens the need to name the construct and context before using a metric.

A newly indexed 2026 preprint frames software-supply-chain trust signals through signaling theory, Goodhart effects, and adverse selection. It is retained as a cutting-edge lead only; peer-review status and its detailed claims need follow-up before using it as evidence.

### Forge documentation does not equal quality evaluation

The Gitee help center exposes documentation for files, branches, releases, SSH keys, repository statistics/settings, and membership. Gitea documents feature differences across hosting alternatives. Codeberg describes itself as a non-profit, community-driven Forgejo-based forge and publishes operating/usage guidance. These opened sources establish platform and collaboration mechanisms, not a repository quality rating or proof that projects hosted there meet practices. They also show why platform software, hosted service, and hosted project must remain separate units in the matrix.

## Search quality and coverage caveats

- Exa surfaced useful first-party community threads and standards, alongside unrelated pages.
- Parallel returned useful standards and primary pages, but broad community discovery also surfaced a suspicious generic OpenCode community result and templated or promotional-looking Reddit content. These were not used as evidence.
- Searches against Hacker News, Stack Exchange, and Lobsters did not surface strong relevant items in the selected result window. This is a low-recall search result, not evidence that those communities contain no relevant discussion.
- The X queries returned substantial topical noise and no strong evidence about a general repository-quality framework. X remains a discovery source; this round produced no validated claim from X.
- The searches were English-language and bounded to the tools' returned windows. Native-language regional searches, authenticated forum coverage, and platform-specific API searches remain open.

## Next round

1. Verify additional forge families and service models, including China-focused hosts, regional alternatives, self-hosted/federated instances, and non-GitHub project practices.
2. Translate and run native-language searches for selected regional communities and standards.
3. Audit standards by artifact and decision unit: software, API, data, ML model, research artifact, infrastructure, documentation, accessibility, privacy, licensing, and operations.
4. Search failure reports and postmortems for cases where repository-visible signals diverged from deployed outcomes.
5. Expand the mechanism atlas and role/lifecycle matrix; each proposed gate needs evidence, applicability, unknown/N/A semantics, cost, gaming risk, and a correction or appeal route.
