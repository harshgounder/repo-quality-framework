# Initial mechanism and measurement audit

**As of:** 2026-11-10 (Asia/Kolkata)
**Status:** first-party documents and a small empirical-paper sample reviewed; not a complete tool audit or framework synthesis.

## How to read these notes

Tool documentation establishes what a tool says it does. It does not independently validate the quality of its outputs. Empirical findings apply to the study's sample, measures, and time window. Search and access records are in [`search-log.md`](search-log.md); broad candidate coverage is in [`rater-inventory.csv`](rater-inventory.csv).

## Mechanism comparisons

### OpenSSF Scorecard — automated security evidence and scores

**Observed mechanism.** The current latest release page reports **v5.6.0**. The project reads a repository through a host API or scans a local directory; the architecture says it does not build or execute scanned repository code. Probes produce findings with locations/remediation; checks score findings from 0–10, or `-1` when inconclusive; an aggregate score weights checks by risk. Users can set policy thresholds without changing the underlying check scores. Sources include the [README](https://github.com/ossf/scorecard/blob/main/README.md), [architecture](https://github.com/ossf/scorecard/blob/main/ARCHITECTURE.md), [check catalog](https://github.com/ossf/scorecard/blob/main/docs/checks.md), and [latest release](https://github.com/ossf/scorecard/releases/latest).

**Governance signal.** The project's check-writing guidance requires checks to use automatable and objective data, be actionable, and support maintainer correction, hints, and disputes about findings/applicability. Its README acknowledges that choices about checks, exclusions, weights, and aggregation are opinionated, and that different consumers care about different behavior.

**Version boundary.** The current `main` branch [roadmap](https://github.com/ossf/scorecard/blob/main/docs/ROADMAP.md) describes Scorecard v6 as an evidence-engine direction: probe evidence could feed both 0–10 check scores and PASS/FAIL/UNKNOWN conformance labels. This is roadmap material. The latest release observed in this pass is v5.6.0, so the v6 direction must not be described as released behavior.

**Open version-mapping question.** The current [Scorecard OSPS coverage page](https://github.com/ossf/scorecard/blob/main/docs/osps-baseline-coverage.md) analyzes the 59-control OSPS Baseline **v2026.02.19**. The baseline's own site labels **v2026.08.28** current. The Scorecard mapping reports 8 controls covered, 17 partial, 31 gaps, and 3 not observable against its February version. This is a concrete version alignment question to follow up, not proof by itself that either project is defective.

**Boundary.** Scorecard is a security/supply-chain signal system. Its structured evidence and correction path are useful mechanisms to study; its aggregate number cannot stand in for the quality of every artifact or project responsibility.

### OSPS Baseline — maturity-level security controls

The [current baseline](https://baseline.openssf.org/) is version **2026.08.28** and defines required security controls relative to project maturity levels. The published controls use MUST requirements and explain intent/examples. Its FAQ explicitly says the baseline is **not intended as a project comparison, score, or grade**; it is for understanding and improving security posture. The FAQ also describes applicability across project sizes, complexities, and source forges.

This separates a normative requirement set from an automated rater. A conformance implementation still needs explicit evidence and unknown handling, but the standard itself does not collapse the controls into an overall quality number.

### OpenSSF Best Practices Badge — self-certification with mitigations

The [criteria](https://www.bestpractices.dev/en/criteria?details=true&rationale=true) define Passing, Silver, and Gold levels and different normative strengths. The [vetting policy](https://github.com/ossf/best-practices-badge/blob/main/docs/vetting.md) says the approach is based on self-certification to make broad participation feasible, including practices that are not easy to automate. It also describes mitigations: automatic checks can reject claims known to be false, suspicious events can prompt spot checks, and anyone can dispute a claim for review. The project says the badge does not guarantee the absence of defects or vulnerabilities.

This model trades a full expert audit for scale and participation, with limited automation and a correction/dispute process. The next audit should inspect how criterion evidence, justified unmet SHOULDs, N/A answers, and spot-check outcomes are represented in practice.

### CLOMonitor — project checks across categories

The [check catalog](https://clomonitor.io/docs/topics/checks/) groups checks across code, community, and documentation-oriented areas. It includes concrete checks for project files and signals, such as README/contributing/maintainer docs, license status, release recency, CLA/DCO, and badges. One OpenSSF Scorecard badge check passes when a matching badge is found in the README. That check establishes badge presence; it does not itself establish that the badge is current, that the underlying practice is effective, or that the project is generally healthy.

The next audit should inspect the implementation and output model, including check-level unknowns, applicability, configuration, history, and any composite aggregation.

## Additional current owner mechanism audit — batch RAT (2026-11-10)

**Scope:** seven candidates from the inventory were selected for primary-source mechanism inspection. This adds implementation detail; it does not validate the ratings against real-world outcomes.

### OpenSSF Scorecard — evidence probes, check scores and consumer policy

The [architecture](https://github.com/ossf/scorecard/blob/main/ARCHITECTURE.md) describes a pipeline from repository/API data and local files to raw facts, probes, findings with locations/remediation, per-check scores and a risk-weighted aggregate. The current architecture page says the scanner does not build or run the target repository. Checks can report -1 when inconclusive; the README warns that included/excluded checks, importance weights and aggregation are opinionated, and recommends reading individual behaviors rather than relying only on the aggregate. The [policy spec](https://github.com/ossf/scorecard/blob/main/openspec/specs/policy/spec.md) lets a consumer enforce or disable selected checks at thresholds without changing the emitted scores.

The [maintainer annotation model](https://github.com/ossf/scorecard/blob/main/config/README.md) distinguishes test-data, remediated, not-applicable, not-supported and not-detected. That is useful because a false negative, unsupported practice, non-applicable condition and actual mitigation are different states. These annotations add maintainer-supplied context; they are not independent verification of the explanation. The project's check-writing guidance asks for objective, automatable, actionable checks and a maintainer correction/dispute path. This is a narrow security and supply-chain evaluator, not a general repo-quality definition.

### OpenSSF Best Practices Badge — normative strength plus self-attestation

The [criteria discussion](https://www.bestpractices.dev/en/criteria_discussion) says the badge uses self-certification to scale across a very large FLOSS population and practices that cannot all be automated. Badge levels distinguish MUST/MUST NOT, SHOULD and SUGGESTED requirements. A SHOULD may be unmet with justification; SUGGESTED items must be considered; N/A counts as met only where allowed; unknown required information blocks a badge. The owner says automation can fill or check some conventional signals, while spot-checks and public disputes provide limited vetting.

This is a structured claim-and-evidence rubric, not an independent audit of every code path or deployed artifact. Spot checks and disputes are meaningful correction mechanisms, but no prevalence, false-claim rate or outcome-prediction evidence was measured in this batch. Keep unknown, justified unmet, N/A and verified met separate in any future comparison.

### CLOMonitor — selected checks, different denominators and external-tool status

The [check docs](https://clomonitor.io/docs/topics/checks/) define code, code-lite, community and docs sets. The project says registered repositories are checked periodically and supports explicit exemptions with a displayed reason. The selected [score implementation](https://github.com/cncf/clomonitor/blob/main/clomonitor-core/src/score/mod.rs) and [report model](https://github.com/cncf/clomonitor/blob/main/clomonitor-core/src/linter/report.rs) show a weighted score per report section and a global weighted score. In the code, only checks present in a report enter the denominator; checks marked passed or exempt enter the numerator; exemptions therefore count as passing after the reason is attached. Check-set selection can change which checks are present, so projects with different sets can have different scoring denominators. Agent-readiness has a separate score and is excluded from the global score.

The [linter input/tool-mode source](https://github.com/cncf/clomonitor/blob/main/clomonitor-core/src/linter/mod.rs) describes an unavailable/disabled external tool as causing dependent checks to be reported as failed. This is an observed code-path contract, not proof that the hosted service is currently misconfigured. It does mean an evaluator deployment must distinguish “could not run the detector” from “the project failed the practice.” The docs also say CLOMonitor does not follow symlinks for file checks. These are useful, concrete edge cases for assessor design.

### inspect.software — versioned public-signal index with explicit missingness

The owner [methodology](https://inspect.software/methodology), [health-index rules](https://inspect.software/wiki/health-index), [rating bands](https://inspect.software/wiki/scoring-bands), and public [scanner repository](https://github.com/inspect-software/scanner) describe raw observed data, metrics, categories and an overall 1–100 index. Formulas, weights, thresholds and bands are versioned; reports are intended to identify the methodology version and expose component inputs. The missing-data rule excludes unavailable components, renormalizes remaining weights, and reports the reason rather than treating missing as zero. The rating curve is described as a fixed methodology constant between version changes, not a live peer percentile.

The publisher explicitly calls the result a signal rather than a warranty and says it performs no line-by-line code audit. The methodology includes policy choices beyond code quality, including bounded organization-stewardship effects and a jurisdiction-risk policy; these choices warrant independent fairness, applicability and stakeholder review. The FAQ also documents a reproduction limit: public reports omit some contributor profile details used by one policy, so an independent recomputation can differ when those details changed the score. These are owner disclosures, not independently reproduced findings. The scanner and method are public, but this research batch did not run the scanner or independently recompute any report.

### RepoPulse — percentile score relative to selected GitHub cohorts

Current live [scoring documentation](https://repopulse-arun-gupta.vercel.app/baseline) and the [42-signal method](https://github.com/arun-gupta/repo-pulse/blob/main/docs/oss-health-42-signals/README.md) describe five buckets weighted Activity 25%, Responsiveness 25%, Contributors 23%, Security 15% and Documentation 12%. Each dimension is compared by percentile within selected GitHub star brackets. The product documentation says insufficient verified inputs should remain explicitly unavailable; no score should be assigned without sufficient verified data. Solo profiles are routed to a different scoring profile. These choices can improve comparability for selected cohorts, while the star brackets and GitHub-only corpus define who is comparable.

The owner [calibration documentation](https://github.com/arun-gupta/repo-pulse/blob/main/docs/scoring-and-calibration.md) and public calibration artifact describe data sourcing and fallbacks. It also says some age-stratified bins have sampleSize 0 and intentionally fall back to a less-specific bracket pending sampling. The owner site says calibration fixtures refresh weekly, while a completed repository issue describes a quarterly calibration-generation process; the actual shipped refresh/version needs a timestamped artifact check. Older product-definition text describes a different phase/formula than the current live five-bucket page, so future comparison must pin a release or commit and reconcile methodology docs with deployed output. No independent reproduction or outcome validation was done.

**Source-level clarification, 2026-11-10:** at [commit `17165e6`](https://github.com/arun-gupta/repo-pulse/blob/17165e6457e28b1c7333b3a7074f0f38e1843c96/lib/scoring/health-score.ts#L76-L99), the composite collects available bucket percentiles, renormalizes their weights and returns a numeric composite when at least one bucket is available; it returns an insufficient-data label if none are available. Individual bucket rules can themselves return insufficient data. This code-level behavior is narrower than interpreting the [product document's](https://github.com/arun-gupta/repo-pulse/blob/17165e6457e28b1c7333b3a7074f0f38e1843c96/docs/PRODUCT.md#L71-L75) statement as requiring all buckets or a validated minimum coverage before any composite score. It does not establish what the deployed service currently runs; no application or test was executed.

### OpenSSF Criticality Score — influence proxy with a stopped population pipeline

The [algorithm](https://github.com/ossf/criticality_score/blob/main/README.md) combines capped, weighted GitHub signals such as project age, last-update recency, contributor and organization counts, commit activity, releases, issue activity, comments and dependent mentions into a 0–1 estimate of influence/importance. The score does not directly establish software correctness, safety, or repository quality. A maintainer discussion [raised dependency-tree blind spots](https://github.com/ossf/criticality_score/issues/8): a widely depended-on but low-visibility component may not rank like a popular direct project. This is a practitioner critique, not an evaluated false-negative rate.

Freshness is now material. The project's [August 2026 shutdown notice](https://github.com/ossf/criticality_score/issues/833) says the production pipeline had not run since May 2026 and the last successful run was July 2025, with Google Cloud storage and BigQuery turned down in August 2026; repository data remains available as infrequently updated files. The scorer can still be run locally, but that does not make an archived population dataset current.

### OSS Compass — explicit metrics with local and lifecycle caveats

The selected official [artifact robustness scorecard model](https://compass.gitee.com/docs/metrics-models/software_artifact/robustness/scorecard) describes individual security checks with 0–10 values, assigned weights and a weighted-sum score. The selected [activity model](https://compass.gitee.com/docs/metrics-models/collaboration/robustness/activity) defines GitHub activity signals and weights, including a negative weight for time since update; its own text cautions that higher iteration frequency is not always better and says cadence should be interpreted by industry/project type and relative peers. That caveat directly counters treating commit frequency as a universal “more is better” quality proxy.

This is a valuable regional and metric-model source, but the selected pages do not establish the completeness of platform coverage, the exact production data pipeline, the current model version, or independent validity. It should be researched as a family of ecosystem/community/artifact models, not collapsed into one undifferentiated “Gitee score.”

### Cross-evaluator observations and unresolved comparison rules

- The same number may represent conformance, evidence confidence, hygiene, public practice, peer percentile, adoption or systemic importance. These constructs cannot be ranked against one another without an explicit target decision and validation outcome.
- Missingness differs: explicit unknown/inconclusive, badge-blocking unknown, check omission and weight renormalization, justified exemption treated as pass, unavailable field, and stale population data. Store the state and denominator alongside every score.
- A visible file/badge or a maintainer declaration is evidence of presence or assertion, not necessarily of execution, correctness, current release behavior or deployed parity. Conversely, static repository scans may miss host settings, runtime configuration, generated artifacts and physical/hardware context.
- Profile, check-set, population, language/forge, time window and methodology version alter what the result means. Comparisons need those fields and evidence timestamps.
- The observations above suggest candidate requirements for future evaluator research—provenance, applicability, evidence age, denominator visibility, detector-failure states, correction routes and context-specific outcomes. They are research questions, not settled universal gates or an endorsed composite score.

## Empirical evidence about indicator limits

### Context-free community-health indicators and sustainability (2023)

The study [“Individual context-free online community health indicators fail to identify open source software sustainability”](https://arxiv.org/abs/2309.12120) monitored 38 projects for about a year using repository signals plus surveys. Projects varied widely in age, staffing, funding, practices, and goals. The authors report that similar indicators can mean different things in different project contexts and caution against cross-project comparisons for high-stakes sustainability decisions. **Key limitation:** no projects failed during the observation period, so the study could not compare failures against sustained projects or establish strong predictors of failure.

### QA badge usage and correlations (2024)

The study [“What can we learn from quality assurance badges in open-source software?”](https://link.springer.com/article/10.1007/s11432-022-3611-3) analyzed 100,000 GitHub projects, categorized QA-badge properties, and reported statistically significant correlations between badges and selected software metrics. This shows usage patterns and associations in that GitHub sample. It does not establish that badges cause quality improvements or predict outcomes across all platforms and artifact types.

### Practitioner intake assessment (2026)

The qualitative study [“Assessing open source software health in organizations’ intake processes”](https://link.springer.com/article/10.1007/s10664-026-10846-y) interviewed 17 industry experts, identified 21 health aspects and 72 connected metrics, and applied a subset in one large automotive-company case study. It emphasizes lifecycle stage, complexity, governance concentration, and the focal organization's strategic importance; the case also shows resource limits on how much can be measured. Its sample and single organizational case bound generalization, while its practitioner perspective helps identify areas existing frameworks may miss.

### Repository stability metrics (2025 preprint)

The arXiv preprint [“An Empirical Validation of Open Source Repository Stability Metrics”](https://arxiv.org/abs/2508.01358) examines a Composite Stability Index using 100 highly ranked GitHub repositories. It reports that weekly commit sampling behaved more feasibly than daily sampling and that medians improved some resolution/review-time measures. The study itself notes that it did not categorize repositories by type; the highly ranked GitHub sample limits transfer to smaller, regional, non-GitHub, or different-purpose repositories. Treat it as a promising measurement study, not validation of a universal health score.

### Construct validity of code metrics (2026 preprint)

The arXiv preprint [“Assessing the Construct Validity of Object-Oriented, Class-Level Code Quality Metrics”](https://arxiv.org/abs/2609.20411) uses factor analysis on metrics extracted from Apache Maven and tests a model against 22 additional OSS projects. It reports that several metrics did not correspond to retained constructs or had low loadings. The scope is class-level object-oriented code metrics, not project health; it is useful evidence that a metric's name alone does not prove it measures the intended property.

### Software-quality dataset (2025 preprint)

[SQuaD](https://arxiv.org/abs/2511.11265) describes a time-aware dataset spanning 450 mature repositories and 63,586 releases with more than 700 metrics from nine analysis tools plus version-control, issue, vulnerability, and process data. It may support future validation work. Its mature-project selection and tool-derived measures are part of the dataset's boundary; the dataset is not itself an endorsed quality score.

### Review of OSS evaluation indicators (2021)

The review [“Evaluation indicators for open-source software: a review”](https://link.springer.com/article/10.1186/s42400-021-00084-8) surveys 56 prior papers and groups indicators into code, license, popularity, developer, and sponsorship categories. It reports both confirmed and contested correlations. Its evidence is a synthesis of studies published mainly from 1999–2020 and it notes that it did not perform fresh experimental verification, so it is a map of prior evidence rather than a current validation.

## First working interpretation

Across these sources, several designs should stay separate in later synthesis:

1. raw evidence/probes;
2. check-level judgments;
3. versioned normative conformance requirements;
4. self-certified claims with bounded verification and dispute handling;
5. descriptive metrics and composite scores;
6. project criticality, visibility, adoption, and sustainability signals;
7. decisions tailored to a focal consumer and context.

The research supports asking for **claim-to-evidence traceability and context-aware applicability** before any gate is recommended. It does not yet prove a specific universal architecture or decide whether the final system should expose a score.

## Next questions for this audit

- Which Scorecard v6 capabilities are shipped versus only planned, and how does the current versioned output encode unknowns and applicability?
- Why does the Scorecard coverage map still use OSPS v2026.02.19 when the baseline identifies v2026.08.28 as current? Is an updated crosswalk planned?
- How are Best Practices badge claims evidenced, N/A or justified-unmet answers handled, and disputes resolved in current operations?
- Does CLOMonitor compute an aggregate score, or present independent checks? What does its supported-host matrix exclude?
- Which findings generalize beyond English-language GitHub projects, and which must be validated for other hosts, languages, artifact types, and project sizes?
- What outcome measures would validate repository-quality signals without using the same proxy both as the score input and the definition of “quality”?
