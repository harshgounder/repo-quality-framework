# Claim-audit sample manifest — 2026-11-10

Selection: targeted, non-representative sample; not a statistical survey. The FP-01–08 and evaluator/benchmark selections were assigned to independent Luna workers before this manifest was written; some source checking may have begun before it was saved. The eight empirical/AI paper claims below were selected before their sources were opened in this turn. No random seed was used. This sample alone does not meet the recovery plan's separate requirements for three randomized claims, three retrospective-run audits, four access/negative claims, and independent rechecks; these remain open unless separately documented.

| IDs | Claim and existing locator | Selection reason |
|---|---|---|
| F01–F08 | FP-01 through FP-08, `research/v2/failure-patterns/initial-evidence-batch.md` | Consecutive claims about original video-adjacent failure mechanisms; several reports and unverified diagnoses |
| B01 | 612 index rows are not 612 unique suites, benchmark landscape §1 | Identity/unit risk |
| B02 | HOW2BENCH v5 reports 672 analysis units vs 379 Appendix F records, benchmark landscape §1 | Numerical and extraction risk |
| B03 | ABC selected 10 benchmarks and found validity issues, benchmark landscape meta-review | Numerical/method risk |
| B04 | OpenAI judged SWE-bench Verified unsuitable for frontier capability, benchmark landscape SWE-bench row | Owner interpretation and current status |
| B05 | SWE-Maintain paired Python study and inherited failures, README AI lane | Counterevidence and causal interpretation |
| B06 | RepoPulse missing-input treatment, `research/mechanism-audit.md` | Negative/unknown handling |
| B07 | CLOMonitor disabled-tool checks, `research/mechanism-audit.md` | Failure/unknown semantics |
| B08 | OpenSSF Criticality pipeline shutdown chronology, `research/mechanism-audit.md` | Operational freshness and negative claim |
| E01 | 33,596 agent PRs and 4,027 matched human PRs, `research/v2/agent-quality/empirical-evidence-batch.md` | Numerical corpus claim |
| E02 | Build study 632 candidates → 387 PRs and 945 build files, same file | Numerical and build-system sample |
| E03 | Debloating paper evaluated ten tools on 20 programs and 12 metrics, same file | Suspected conflict with later correction |
| E04 | Python bloat 1,302 projects and 3,232 dependencies, same file | Numerical/measurement claim |
| E05 | LibCache three apps, twelve workloads and mean 18× cache size, same file | Workload and tradeoff claim |
| E06 | RepoNorm 121 tasks/six repos/160 norms, `research/v2/agent-quality/current-lab-artifacts-and-frontier-evidence-2026-11.md` | Numeric and primary-artifact release claim |
| E07 | SWE-CC 12 projects/823 checkers/500 contributions, same file | Numeric and mechanism claim |
| E08 | All Smoke No Alarm 86,156 test patches, 33,596 PRs, 80.2% weak/no signal, same file | Numeric and construct validity claim |

Each record will distinguish source-supported claims, source-author assertions, code inspection and independent reproduction. An unreachable source remains inaccessible; it is not counted as a contradiction.

## Additional seeded sample

Selected before opening these three sources in this audit: Python `random.Random(20261110).sample(range(9, 34), 3)`, sorted, gives **FP-14, FP-18, FP-29**. Population is the numbered failure cards FP-09–FP-33 (25 cards), deliberately excluding the assigned FP-01–08 batch. This seeded sample is representative only of its defined list under this selection, not of all project claims or systems. It is an extension of the targeted 24, not a substitute for stratified selection across the full project.

The later R14/R18/R29 extension supplies three seeded selections from the explicitly limited FP-09–FP-33 frame; the original 24 selections remain targeted and do not become a stratified random sample. Three retrospective fetch events were subsequently located and checked as documented in `session-inventory.md`. Four access-route checks were subsequently attempted, but their selection was documented after opening and they are not part of a prospectively declared 24-claim sample. Six E-series source claims were independently rechecked by Luna; the evaluator/source-access review had its own retrieval limits. Full-plan representativeness and complete historical reconciliation remain open.
