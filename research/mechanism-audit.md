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
