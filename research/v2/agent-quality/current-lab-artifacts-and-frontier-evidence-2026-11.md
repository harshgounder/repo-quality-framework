# Current AI-lab artifacts and frontier evidence

**Reviewed:** 2026-11-10 (Asia/Kolkata)
**Status:** scoped research pass; no repository, benchmark, model, or task suite was executed. Most studies below are recent arXiv papers, not independently reproduced results. DeepResearch RewardBench is listed in Findings of EMNLP 2026.
**Campaign:** C25; planned cells PC99–PC108; exact searches and access limits are recorded in `research/search-log.md`.

## Why this pass matters

The request is not just to find more coding-agent scoreboards. It is to study how labs and research groups turn incomplete real systems into testable tasks, how they decide what counts as success, what their published checks miss, what the released repositories actually contain, and how current work is discovered. This pass therefore follows papers into GitHub, Hugging Face, lab evaluation-method pages, and source-feed pages. A paper result is kept separate from a released artifact; an artifact page is not proof that the reported experiment can currently be reproduced.

Several new studies directly extend the settings-panel example. They ask whether a patch satisfies a repository's process rules, whether its tests contain a meaningful oracle, whether the next change inherits broken tests, and whether edits that cross repositories remain consistent. Other studies test the AI infrastructure that trains or serves models, including performance claims that ordinary unit tests do not establish.

## New findings close to repository quality

### Repository norms are both written and implicit

[RepoNorm](https://arxiv.org/abs/2610.07757) proposes acquiring repository-specific norms from a frozen source snapshot and Git history, grounding candidate claims in source evidence, checking counterexamples, and exporting accepted norms for coding agents. Its [public implementation](https://github.com/SYSUSELab/RepoNorm) includes RepoNormBench: 121 tasks from six Python repositories at 14 snapshots, 160 reference norms, 1,024 task–norm links, and 1,089 released model executions across three models and three conditions. The paper reports sampled precision of 86%; its repository also includes calibration data, 140 double-reviewed items, reference audits, paired intervals, costs, integrity hashes, and a reproduction path that recomputes published analyses without calling a model provider.

This is a useful mechanism sample because it distinguishes finding a rule from proving that it applies to a particular change. It includes source discovery, explicit extraction, inference from current code, Git-history checks, evidence verification, counterexample checks, and separate runtime, static, patch, test, and documentation checks. It also records non-findings and uncertainty. The authors report norm-compliance gains against both no guidance and CodeWiki; functional success gains over the raw condition were not statistically significant in their paired comparisons.

Limits matter: six Python repositories do not establish language- or domain-wide behavior. The authors say fixed analysis budgets can miss norms and counterexamples, packages can become stale as repositories evolve, and agents may ignore relevant material in a large norm package. The work does not isolate each component's contribution or establish optimal settings. Repository-specific norms are context evidence, not universal standards.

[SWE-CC](https://arxiv.org/abs/2610.06193) complements norm acquisition with a policy-compliance audit. Its [released benchmark](https://github.com/dangtruong01/swe-cc-arxiv) converts documentation from 12 SWE-bench Verified projects into 823 deterministic checker functions and evaluates 500 end-to-end contributions, including the agent's trajectory, final patch, commits, and pull-request text. It compares a native condition, where the agent must find rules in the repository, with a consolidated condition, where rules are mounted for it. The paper reports that agents violated 43.1% of applicable policies, with nearly half of violations occurring during intermediate execution.

That split changes the evaluation question: final code may be correct while the path used to produce it broke a freeze, skipped a required workflow, or violated an operational rule. The benchmark's deterministic checkers make a clearly specified policy machine-checkable; they cannot make undocumented, ambiguous, or culturally contextual prose objective. The release is specific to 12 projects and one task family, so it is evidence for an evaluable mechanism, not a universal repository policy set.

### Test files can exist without testing the behavior

[All Smoke, No Alarm](https://arxiv.org/abs/2606.18168) studies 86,156 test-file patches from 33,596 agent-authored pull requests across 2,807 repositories and five agents. A qualitative sample of 384 patches informed an eight-category taxonomy of explicit oracle signals. The paper reports 80.2% of test patches had weak or no explicit oracle signal. Stronger syntactic signals were associated with higher merge likelihood after the authors' regression adjustments (OR 1.28, p < 0.001).

This is a warning against gates like “a test file was added” or even “an assertion exists.” The study explicitly says its patch-level regex categories detect syntax, not semantic adequacy: an equality assertion can check the wrong property, and a new test patch can inherit assertions elsewhere in the file. Its merge association is observational, and its dataset excludes repositories below 100 stars and is skewed toward Codex PRs. Treat the categories as triage signals, not test-quality proof.

### Later work separates code debt from inherited failures

[SWE-Maintain](https://arxiv.org/abs/2610.14768) provides an important counterweight to broad claims that AI-generated code is intrinsically harder to maintain. It constructs 100 three-event maintenance episodes from 50 real Python repositories and compares the same later task, agent, and tests from either developer history or agent history. The paper reports 1,996 paired events across five coding systems and two backbones. Later-task resolution was 5.6 percentage points lower on average from the agent's own prior history; the difference rose to 14 points when all earlier tests also had to pass.

However, two-thirds of those agent-history starting repositories already failed earlier tests. Once the inherited repository passed all previous tests and the next task was not already solved, the reported disadvantage disappeared: +2.7 points with a 95% confidence interval from −0.5 to +6.1. The authors conclude that, in this benchmark, the accumulated failure burden mostly came from earlier tests left failing rather than a demonstrated general increase in code-maintenance difficulty. This is a strong reason to preserve test state and compare like-for-like histories before attributing later friction to architecture, duplication, or style. It is a Python-only preprint and does not settle structural-quality questions measured by NITR or RepoNorm.

### Functional correctness stops at repository boundaries

[CrossSWE](https://arxiv.org/abs/2611.01484) evaluates joint changes across repositories: 171 tasks, 165 repositories, 20 technical areas, and 13 languages. The benchmark checks that partial repository edits are insufficient for the requested behavior, rather than merely using extra repositories as context. The paper reports a 58.48% Pass@1 for its strongest tested model and identifies cross-repository inconsistencies as 44.2% of failures. Its own limitation is that 165 tasks use two repositories; only six require three or more.

The [Hugging Face dataset release](https://huggingface.co/datasets/CrossSWE/CrossSWE-Bench) exposes task contracts, pinned environment image references, repository and source-release commits, task SHA-256 values, gold and test patches, pass-to-pass and fail-to-pass tests, an evaluation-support field, and per-instance license records. That artifact surface is itself useful: reproducibility and license status are represented as data alongside the task. The connected GitHub repository search did not find a CrossSWE repository; that search failure does not establish that no code exists. The dataset is public and was inspected, but not downloaded or run.

### AI infrastructure requires hidden correctness and measured performance

[InfraDev](https://arxiv.org/abs/2610.36589) constructs 36 real pull-request tasks from Megatron-LM, vLLM, and verl, covering training, inference, and reinforcement learning, with multi-file and multi-GPU execution. It reports that 32% of submissions passing all official tests were rejected by additional hidden probes. Among 36 original changes, 24 had no test checking a numerical result; 13 of 15 performance optimizations lacked a test checking the promised saving. Its central method jointly synthesizes hidden probes and a prompt that declares the interfaces those probes call.

The authors report a best resolution rate of 38.9% across six frontier models and a 10.5-point gain after adding an agent skill on Megatron-LM tasks. These are paper results, not reproduced here. The task set is small and expensive, and the paper's retrieved public-source path did not establish a runnable code release in this pass. Its core lesson for research design is specific: functional tests can miss numerical behavior, state interactions, memory/time/traffic limits, and whether an optimization actually improves the workload it claims to improve.

[Infrathon](https://arxiv.org/abs/2611.11995) moves from patch correctness to long-running model-training and serving optimization. The paper describes 25 tasks across operator, module, and system levels, 12–24-hour budgets, six models, and 150 runs consuming over 10,000 GPU-hours. It reports ranking changes across run horizons and that 135 of 150 runs improved during their second half. Its [paper-linked GitHub URL](https://github.com/InfrathonX/Infrathon) returned 404 from the connected GitHub repository endpoint in this pass. The paper also points to a [Hugging Face dataset](https://huggingface.co/datasets/Infrathon/Infrathon), whose current page requires accepting conditions, displays no dataset card, and did not expose the files without acceptance. The paper/code/data routes therefore remain unreconciled. The compute cost is also a major accessibility and replication constraint.

[DeltaML-Bench](https://arxiv.org/abs/2608.19653), an independent ML-research benchmark, evaluates agents improving published results inside imperfect research repositories. The public [Inspect adapter](https://github.com/AlgorithmicResearchGroup/deltaml-bench-inspect) is unusually explicit about scope: 35 active PWC task families with main and hidden-score variants; five incomplete imports and fourteen tasks are archived for unsuitability or redundancy; the AI-research task family is not supported by that runtime. It audits agent-reported metrics against code and declared logs, submits a redacted code-and-trajectory bundle to an integrity judge, and verifies the upstream task objects before launch. The companion [Vivaria repository](https://github.com/AlgorithmicResearchGroup/deltaml-bench-vivaria) has a separate task/runtime surface. These are versioned releases with different supported scopes; do not silently combine their coverage or attribute the paper's reported set to one current adapter.

### Existing code can teach agents to repeat its defects

[Coding Agents Propagate Vulnerabilities](https://arxiv.org/abs/2611.11455) uses a paired-context design: the same task is evaluated in repositories whose neighboring code differs in secure versus insecure implementations. Its [public repository](https://github.com/eth-sri/vulnerability-propagation) covers 96 backend-generation tasks and 20 paired C/C++ repository tasks. The paper reports lower secure-and-functional success in insecure contexts and says prompts to follow style or “be careful” did not eliminate propagation. The setup is narrow to its selected CWE classes, frameworks, languages, and tasks; it establishes a contextual mechanism in those experiments, not a universal degradation rate.

This connects repository baseline quality to AI-output quality: an existing pattern can be a training signal for the agent even when it is a defect. A checker that only examines the new diff may miss that the agent copied a dangerous local convention. Conversely, “duplicate code” alone is not a defect oracle. Any future test must name the property at risk and compare behavior or a security-relevant invariant.

### Multi-condition tasks challenge surface size metrics

The preprint [Beyond Surface Metrics](https://arxiv.org/abs/2611.03162) uses a frozen 18-criterion taxonomy to compare 2,925 Apache Fineract issues with 944 tasks from three AI coding benchmarks. It reports that task pairs matched on issue class, modified-file count, and churn still had highly disjoint fulfillment-condition sets; 57.4% of 1,177 matched pairs had no shared condition category. The paper presents descriptive corpus comparisons and selected test examples, not benchmark-wide proof of omitted checks or a causal failure estimate. A single investigator coded the benchmark conditions, an explicit validity limitation.

This supports a research direction: model a request as a set of outcome conditions and their dependencies, instead of using task labels, LOC, file counts, or “tests passed” as substitutes for completeness. It does not justify a universal fixed list of conditions; domains and project contracts determine which conditions apply.

## Other useful frontier work and evaluator research

[DeepResearch RewardBench](https://aclanthology.org/2026.findings-emnlp.1611/) evaluates reward models and model judges on long-form research reports, using paired, triplet, and quadruplet preference data, task-specific rubrics, multi-round filtering, and human verification. It is in Findings of EMNLP 2026. The paper's extracted code link, [NLP2CT/DRRB](https://github.com/NLP2CT/DRRB), returned 404 through the connected GitHub metadata route. A separate [similarly titled repository page](https://github.com/zyt2312/DeepResearch-RewardBench-Evaluating-Reward-Models-for-Deep-Research-Report) found in web search calls itself official but currently says code and data are coming soon. Those routes are not reconciled; publication does not yet mean the benchmark can be reproduced from the observed release. Its method is relevant to research-output assessment, but a judge's preference score is not a substitute for truth, citation provenance, or domain validation.

[Station](https://arxiv.org/abs/2610.08927) tests open-ended discovery in a simulated scientific ecosystem. It gives agents research questions from three prior ICLR oral papers while withholding their results and disabling web access, then measures how many original findings are rediscovered. It also reports two tasks without oracle papers. The paper's abstract reports 62.7% criterion rediscovery for Station against lower results for two baselines. The oracle set is only three studies, and open-ended discovery is difficult to score without anchoring on known findings; treat the result as a small controlled probe, not a general scientific-capability estimate. A previous one-digit paper-ID transcription opened an unrelated Go-deadlock paper and was discarded; the corrected ID above was checked against its title and author affiliations.

[Who Can Evaluate AI Independently?](https://arxiv.org/abs/2611.08134) contributes a different research-infrastructure lens: Power, Access, Adequacy, and Independence (PAAI). It analyzes 12 African evaluation projects and published joint evaluations across AI Safety Institutes, asking who can choose questions, run models, retain infrastructure, interpret results, publish, and continue the work. This is not a repository quality score. It is a reminder that a benchmark's apparent coverage can reflect who controls compute, data, and publication rather than which systems matter. The same access and control dimensions should be retained when mapping regional labs and research sources.

## First-party lab practices from released repositories and methods

### Google DeepMind gBench

The public [google-deepmind/gbench](https://github.com/google-deepmind/gbench) repository distinguishes model capability from serving performance. Its current README documents workload campaigns, repeated measurements, mean/median/standard deviation and latency percentiles, a coefficient-of-variation repeatability threshold (default 5%), and open-loop stress sweeps that repeat rate points and bracket pass/fail capacity. It also writes per-run metadata, failures, logs, sample traces, and provenance rather than only a final score.

Its [scaffold versioning design](https://github.com/google-deepmind/gbench/blob/main/docs/scaffold-versioning.md) separates model subject from the conditions of the experiment and includes prompt, schema, scoring, permissions, attempts, decoding, dataset snapshot, serving environment, and load shape. This prevents a model change and harness change from being collapsed into one apparent “model score.” Its [dataset inventory](https://github.com/google-deepmind/gbench/blob/main/docs/THIRD_PARTY_DATASETS.md) records licenses, gated access, and redistribution restrictions, but says the inventory snapshot is from September 2026 and must be rechecked before use or score publication.

These are owner-authored engineering mechanisms, not an independent evaluation of gBench's results. This pass read documentation only. It did not inspect the implementation, execute a stress run, validate the CV threshold, or audit each dataset license.

### Meta's published comparison method

Meta's [Muse Spark evaluation methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) makes per-benchmark result provenance explicit. It prefers a common official leaderboard when available; otherwise it uses internal runs or provider self-reports. It notes that some models were unavailable for direct testing, and says third-party model results use best-effort common settings that are not necessarily provider-optimal. For OSWorld-Verified it uses a 361-task split, excludes Google Drive-dependent tasks, runs four attempts per task, and retains model-specific coordinate conventions. Those decisions are transparent and operationally consequential: reader-facing leaderboard columns do not all have the same source or setup.

This methodology is useful as a disclosure example, not a neutral independent audit. A future comparison matrix should capture the source class and harness per cell, “not evaluated” reasons, task split, retries, model-specific configuration, and whether a result is internal, official, or self-reported.

## Research discovery snapshot

- On the current fetch, [The Latest in AI's homepage](https://thelatestinai.com/) showed 120.8K papers and “Newest paper November 6,” while its [papers page](https://thelatestinai.com/papers) showed 122.2K papers and a newest item dated November 9. An earlier papers-page capture in the companion note showed an older date. These are observed page snapshots, not a measured service delay; the count and date mismatch needs a route/cache/version explanation before using either as a freshness guarantee.
- [AlphaXiv](https://www.alphaxiv.org/) surfaced papers dated November 9 and supported targeted extraction of paper pages. Its ranked/feed output is a discovery window, not a completeness guarantee or a canonical version record.
- arXiv's [RSS documentation](https://info.arxiv.org/help/rss.html) exposes category and multi-category feeds. For freshness and version questions, compare portal records to the canonical arXiv item and version, then follow the linked artifact.
- The 19-lab tracker described in the companion note remains a partial US/China-focused seed. It cannot stand in for a global lab census. English-language arXiv, GitHub and selected conference pages also leave regional repositories, non-English papers, private artifacts, and non-arXiv venues thin.

## Candidate dimensions for later synthesis; no gates chosen

These findings support keeping separate observations for:

1. Final requested behavior and all explicitly linked side effects, states, users, interfaces, and close/open triggers.
2. Repository norms: explicit policy versus inferred convention, evidence, applicability, counterexamples, confidence, version, and lifecycle owner.
3. Test-oracle strength: what property is asserted, whether an adversarial mutation would be caught, whether old tests still pass, and whether the test is independent of the patch under review.
4. Change history: immediate completion, inherited failures, regression preservation, future-task cost, correction/revert, and a clearly defined follow-up horizon.
5. System boundary: one function, package, repository, dependency graph, multi-repository product, deployed service, or long-running experiment.
6. Domain result: numerical correctness, security, performance under workload, resource limits, output quality, or other separately observed property.
7. Execution and evidence provenance: model/configuration, scaffold, task and data version, environment image, seed/repetitions, run receipts, grader version, cost, missing results, and source class.
8. Evaluator independence and access: control of task design, infrastructure, data, repeat execution, publication, and continuation.
9. Change and retrieval freshness: source snapshot age, artifact health, license and access status, region/language, failed fetches, and record/version reconciliation.

These are research candidates, not requirements for every repository. A profile must first explain why each property applies, which evidence supports it, what remains unknown, and what a check can falsely pass or falsely fail.

## Open work

- Verify newest papers against canonical arXiv or venue records, then follow available code, datasets, tests, Docker images, grading scripts, benchmark manifests, and licenses. Several 2026 preprints have a paper URL but no verified GitHub release or a currently failing repository link.
- Inspect RepoNorm's implementation and release manifest, not just its README and design docs; compare its norm extraction/checkers with SWE-CC policy checkers and NITR structural oracles without executing benchmarks.
- Trace CrossSWE dataset images, licenses, commit pinning, gold patches, and evaluation contracts across sampled tasks. The dataset card is rich but no task was run.
- Resolve Infrathon's GitHub 404 through another primary route; distinguish paper, dataset, container, code release, and current maintenance state.
- Check whether DeepResearch RewardBench's code/data have been released since the page snapshot; the observed repository says “coming soon.”
- Revisit SWE-Maintain with the paper's full threats and artifact status; test its conclusion against other languages and structural-quality benchmarks before generalizing.
- Expand current work beyond code agents: model-training and dataset curation, robotics, scientific instruments, simulation, compilers, browsers, firmware, operating systems, deployed APIs, and high-consequence systems; map regional labs and publication routes in their own languages.
- Continue the user-requested community failure search and the broader role/system map. The final role list and Computer System Atlas coverage remain open inputs.

**Coverage boundary:** this is a deliberately selected frontier pass, not an exhaustive AI-lab review, source-platform census, benchmark comparison, replication, or final framework. No repository tests, benchmarks, model evaluations, stress runs, or external writes were performed.
