# Empirical evidence on agent-authored repository changes

**Status:** initial primary-source batch, retrieved 2026-11-10. It is a scoped literature sample, not a settled verdict on AI-generated code. Two included 2026 arXiv papers were read through selected method/results/validity sections; their peer-review status and replication packages need a separate audit.

## Why this track is separate

“AI code quality” bundles different units and outcomes: patch-level patterns, build scripts, functional behavior, security, maintenance after merge, review work, and task success. A benchmark pass, static analyzer issue, revert, or maintainer approval measures a different thing. The project should not collapse those into one agent score or assume differences are uniform across products, languages, tasks, or repository practices.

## Primary studies opened

### Agent products vary by outcome in a large GitHub sample

[Not All Agents Are Equal: Code Quality and Post-Merge Maintenance Across Five Autonomous Coding Agents in the Wild](https://arxiv.org/abs/2609.17598), posted 2026-09-12, uses AIDev provenance labels plus cached GitHub API responses. The reported corpus contains 33,596 agent PRs and 4,027 matched human PRs from overlapping repositories/time windows; the matched human subset covers 810 repositories. The study follows 26,283 merged PRs over 90 days and analyzes three languages. Outcomes include regex-detected security smells, structural maintainability proxies, post-merge churn, reverts, and review behavior.

The paper reports that several outcomes differed more among agent products than between a pooled agent group and humans. It reports 6.1% reverts for Codex-authored PRs versus 11.5% for the matched human sample and 14.5% for Devin-authored PRs. Those are corpus-specific observed rates, not causal agent effects or predictions for private/commercial work. The authors explicitly note self-selection into tasks and tools; regex “security smells” are patterns rather than confirmed vulnerabilities, and revert detection misses silent rewrites. The paper is an arXiv preprint in the retrieved record; publication status was not independently checked.

### Post-merge static issues in merged bug-fix PRs

[Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests](https://arxiv.org/html/2601.20109v1), posted 2026-01-27, compares pre- and post-merge SonarQube findings for 1,210 merged agent-generated bug-fix PRs from 206 Python repositories. It measures bugs, code smells, vulnerability flags, security hotspots, duplicate blocks and estimated technical debt. It reports that raw issue totals are sensitive to change size and that normalization can alter apparent between-agent differences.

The sample contains only merged Python bug-fix PRs, has no matched human baseline, and uses static tool-defined signals rather than downstream runtime behavior or long-term maintenance. The authors report agent imbalance and caution against over-interpreting small per-agent samples. Treat it as evidence about one population and one analysis instrument.

### Build-system code is a distinct artifact with different failure modes

[AI Builds, We Analyze: An Empirical Study of AI-Generated Build Code Quality](https://arxiv.org/html/2601.16839), posted 2026-01-23, studies Gradle, Maven, CMake and Make changes from AIDev. The paper manually filters 632 candidate PRs to 387 build-related PRs, then analyzes 945 before/after build files with the build-specific Sniffer tool. The retrieved paper excerpts report new smells in 66 files, improvements in 31, and no smell-state change in most files. Its labeled dataset, manual annotations and code are described as a replication package; availability and execution remain to be checked.

This is useful because build/release configuration is a separate repository component from product source. Its limitations include a small and imbalanced agent sample (the extracted report lists only two Claude PRs), static smell rules, and the restrictions of one build-file classifier. The result does not estimate the chance that any future agent change is unsafe.

### Bloat removal is a transformation that needs its own correctness oracle

[A Broad Comparative Evaluation of Software Debloating Tools](https://arxiv.org/html/2312.13274v2) evaluates ten tools on 20 benchmarks using 12 performance, security and correctness metrics. Its authors report that many transformations failed to produce passable results on medium/high-complexity benchmarks and use differential testing to detect crashes, inconsistent behavior, and retained features that were supposed to be removed. Their reported rates are bounded to their selected tools, benchmark configurations, and testable variants; passing this dynamic comparison is not a formal proof of equivalence.

[Bloat beneath Python’s Scales](https://dl.acm.org/doi/10.1145/3660821), published in 2024, analyzes dependency graphs for 1,302 popular Python projects and 3,232 transitive dependencies. Its static graph construction can have false positives and negatives because Python is dynamic, and its findings are restricted to its Python/PyPI population. This is evidence that “unused dependency” measurements depend on language semantics and observed/reconstructed reachability.

### An optimization can trade startup time against artifact size and build cost

[Dependencies that Bundle Code and Execution](https://arxiv.org/html/2607.02618) evaluates LibCache on three Java applications and twelve workloads. The paper reports 30 workload runs for timing comparisons, startup improvements in its tested configurations, execution caches averaging 18× the size of the JARs, additional build-time cost, and workload-specific inversions or differences within measurement noise. It also identifies test-suite coverage as a threat: dependency tests may not represent production class-access patterns. This is a small, purpose-specific study, not a recommendation to ship caches.

## What this changes in the research model

- Preserve the unit and lifecycle of each result: changed file, PR, merged commit, repository, release artifact, runtime workload or consumer project.
- Keep source-code metrics, build validation, functional tests, security analysis, benchmark data and post-merge maintenance as separate evidence fields unless a study validates a combined measure.
- Record agent/product version, task class, language, repository selection, review/merge state, time horizon, denominator and comparison group.
- For detector claims, record rules, representation, dynamic-language behavior, generated/vendor exclusions, thresholds, known false positives/negatives and whether any finding was manually validated.
- For removal/refactoring/optimization, compare behavior with a suitable domain oracle and measure all relevant budgets (e.g. binary size, memory, startup, throughput, build time, energy and maintainability) under representative workload conditions.
- Search for counterevidence, including cases where a simplification reduces static indicators but worsens runtime or functionality, and cases where a low-cost/maintainable solution intentionally duplicates code.

The current inference is limited: existing primary work supports measuring multiple outcomes and preserving product/task/context variation; it does not establish a universal AI-repository deficit, an optimal score, or a required gate. Exact queries, result windows and the extraction identifier are indexed in [`../../search-log.md`](../../search-log.md) under `AI-S01` and `AI-F01`.
