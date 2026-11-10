# Cross-domain benchmarks and AI-systems lab artifacts

**Reviewed:** 2026-11-10 (Asia/Kolkata)
**Campaign:** C26; planned cells PC109–PC116; query, repository, and paper routes are logged in `research/search-log.md`.
**Scope:** a bounded follow-up across professional-work benchmarks, scientific tasks, computer-use recovery, and AI serving systems, plus selected evaluation-framework repositories. It is not a census of AI labs or a complete standard.

This pass follows several recent AlphaXiv leads to their papers and repositories. It also pins the GitHub snapshot where possible. Paper-reported results, repository claims, and our interpretations are kept distinct. No benchmark, task, model, dataset, or test suite was run or downloaded.

## Why this expands the quality question

The systems named by the user range from software internals to entire services and physical systems. A repository-only score cannot establish whether an agent completed the actual work, preserved system state, satisfied engineering constraints, produced scientifically meaningful outputs, or used resources efficiently. Recent evaluation work splits these questions into different observable units: professional deliverables, verified task outcomes, state-recovery trajectories, agent-serving traces, and hardware-facing workload replay.

The studies below do not collectively cover “everything.” They do provide concrete, different mechanisms that a generalized research framework should be able to discover and compare without collapsing them into one score.

## Task and oracle designs across different kinds of work

| Artifact | What is measured | Oracle and trajectory design | Release/access boundary observed on 2026-11-10 |
|---|---|---|---|
| [Agents’ Last Exam (ALE)](https://arxiv.org/abs/2606.05405), [repository](https://github.com/rdi-berkeley/agents-last-exam) | Long-horizon professional workflows across 55 subdomains and 13 industry clusters | Agent acts through its own harness on a real machine; task output artifacts are scored against hidden references and deterministic graders | v1.1 lists 122 active tasks after 30 retirements. Its review covers 57 modified active tasks but explicitly says it is not a complete agent rerun. Software is Apache-2.0 and data CC-BY-4.0. |
| [Physical-Engineering’s Last Exam (PLE)](https://arxiv.org/abs/2610.30537), [Google Research repository](https://github.com/google-research/ple) | 85 long-horizon structural, civil, electrical, and mechanical engineering tasks | Engineering deliverables combine constraint checks, objective scoring, and in some cases LLM-rubric grading; tasks are expert-authored or agent-assisted then expert-validated | 29 public development tasks require accepting the Hugging Face dataset terms; 56 tasks are hidden. The latest repository commit says registrations and submissions are currently closed and organizer-side grading will not run until further notice. |
| [SCI-AGENT-EXAM](https://arxiv.org/abs/2610.32441), [repository](https://github.com/SKYLENAGE-AI/Sci-Agent-Exam) | 120 scientific-workflow tasks across 11 fields and 7 task types; outputs include executable and textual artifacts | Deterministic checks for code/data/schema outputs plus a calibrated, expert-validated LLM judge for scientific meaning; trajectory progress and stability are also analyzed | The repository says it is a compact extract with five complete example tasks; the complete task set and batch runner are omitted. The GitHub metadata did not report a license. |
| [CUA-Recovery](https://arxiv.org/abs/2610.27645), [repository](https://github.com/xu-hu-2002/CUA-Recovery) | Whether desktop agents detect and repair policy-induced errors during long workflows | Verifier-confirmed errors are created from agent rollouts; humans verify 2,250 takeover states over 100 tasks. Takeover happens 0, 5, 10, 15, 20, or 25 steps after the cause, without an error warning | MIT-licensed code is public; the repository says the benchmark dataset release is coming soon. Running the desktop VM requires KVM and about 16.5 GB of image data. |
| [ARIES](https://arxiv.org/abs/2607.29069), [repository](https://github.com/hyscale-lab/ARIES) | End-to-end agent-serving experiments across harness, model, tool bridge, sandbox, task outcome, and resource behavior | Task semantics are kept separate from execution configuration; correlated trajectories and telemetry support comparisons. The repository includes selected production traces | The trace page describes samples from Ant Group production: five engine pods with 24-hour traces, a separate working-hours pod sample, and 24-hour CPU/memory series for 100 harness pods. This is a workload sample, not universal production coverage. |
| [MAServeBench](https://arxiv.org/abs/2610.40293), [paper-linked repository](https://github.com/ShengxuanQiu/MAServeBench) | Serving behavior under different multi-agent collaboration workloads | Composable Spawn, Fork–Join, Refinement Loop, and Debate stages generate native runs; hierarchical semantic traces preserve realized operations and dependencies for frozen replay and architecture simulation | Repository docs distinguish native execution from fixed-work replay and require recording exact hardware/backend versions. GitHub metadata returned no license. |

### Professional work: task validity and version maintenance are part of the benchmark

ALE is useful because it exposes a release lifecycle, not only a score. Its repository pins code, task data, environment images, and release assets together. Version 1.1 retains 122 active tasks after 30 retirements. For 57 modified active tasks the maintainers list the decision, affected material, and validation performed. They distinguish “verified” checks from review-only decisions and warn that the checks do not certify full agent reruns. The review also records changed fairness and correctness details, such as accepting valid equivalent answers, fixing section matching, and correcting the treatment of hard constraints.

That record gives us a concrete research target: when a task or grader changes, capture which contract changed, which environment/data versions match it, what positive and negative verifier cases ran, which native deliverables were not exercised, whether the agent was rerun, and why a task was retired. “Benchmark version” alone is too coarse to explain whether a score remains comparable.

PLE applies a different domain-specific oracle. It scores a task from 0 to 1. For the dev tasks with a design objective, a hard safety or feasibility failure limits the item score to 0.4; otherwise the score combines constraint satisfaction with performance relative to a certified objective and a compliant naive baseline. A missing task result scores zero, and harness crashes, protocol violations, invalid model requests, and six-hour timeouts count as task outcomes. These choices make safety, feasibility, workload quality, and harness reliability visible in the score contract.

The release boundary matters as much as that formula. The public set contains 29 development tasks; 56 test tasks remain hidden, and the public dataset is gated by terms acceptance. On the latest observed commit, PLE had removed earlier promises to register, submit, or run entries on the organizers’ side: details for hidden-task evaluation were still to be announced. So the paper’s benchmark design exists, but an external user could not treat the full hidden leaderboard process as operational on this snapshot.

ALE and PLE cover useful professional-work mechanisms, but neither is a universal system-quality gate. Their task pools, access routes, and expert domains are bounded; their published score is one observable result under a particular task and environment contract.

### Scientific work: heterogeneous outputs need separate evidence

SCI-AGENT-EXAM represents research tasks through two output classes: executable artifacts such as code and tables, and textual artifacts such as reports and explanations. Its described verifier separates deterministic programmatic checks from a calibrated, expert-validated LLM rubric. It also reports run-to-run stability and intermediate progress, rather than only final average score. The paper reports an overall score of 80.9 for its top system while 26.0% of runs achieved a normalized combined score of at least 0.95 (the paper's Pass@0.95 fraction), illustrating how an average can hide lower reliability on demanding tasks.

The public repository is narrower than the benchmark label can suggest: it explicitly describes itself as an extract with five complete example tasks, and says the complete task set and batch runners are omitted. This is an important artifact-availability distinction. A live leaderboard and a runnable example do not establish that all 120 paper tasks, task data, and graders are openly reproducible. The repository’s current metadata also returned no declared license, so reuse rights need separate checking.

The method is a candidate for projects where code execution alone cannot grade the full outcome. A future profile would need to retain the judge model/version, rubric, calibration set, expert adjudication, deterministic component results, missing outputs, and disagreement—not turn a model judge’s score into ground truth.

### Long-horizon recovery: create tests from failures that actually occur

CUA-Recovery is especially relevant to the user’s settings-panel example as a broader testing idea, though it does not measure that UI bug directly. It starts with errors generated by agent policies, checks them against an executable gold lineage, identifies the root cause, repairs unrelated mistakes, and constructs takeover states at increasing delays. The test agent receives no warning that an earlier action was wrong. This asks whether a system can detect latent state corruption after the causal step has left its immediate context.

The paper reports that, across six tested agents and six takeover depths, maximum error-awareness rate was 44.0% and Pass@3 was 25.5%. Fine-tuning on the training suite raised the reported average error-awareness rate from 19.9% to 35.2% on held-out recovery states; those are results from this benchmark and training setup, not a general rate for desktop agents. The repository exposes the synthesis, verifier, annotation, takeover, and training pipeline, including mutation-test settings, repeats, replay-state checks, and a split configuration. However, its README says the dataset release is still coming soon. The code can be inspected without assuming that its evaluated task corpus is currently reproducible.

This suggests a useful method for the framework’s future failure-pattern work: use production-like or policy-generated traces to discover realistic bad states; preserve a state lineage; vary the delay or intervening sequence; independently verify the injected or observed fault; then score both detection and successful repair. This remains a candidate research mechanism, not a generic gate for all repositories.

### AI serving: measure the path the work actually takes

ARIES treats an agent run as a stateful trajectory through several services, not one model request. The paper describes task specifications separated from execution configurations, cross-component trace reconstruction, and correlated system telemetry. The repository’s supported matrix includes multiple harnesses, serving engines, sandboxes, and several benchmark families. It also documents practical constraints: the published quick start requires Linux and a local Docker engine, and mixed/remote Docker deployment modes are not supported in the observed documentation.

The included Ant Group trace note gives explicit sampling boundaries: engine request logs cover five named pods for 24 hours each plus a separate set of working-hours pods sampled from the service; harness CPU and memory traces cover 100 pods over a day. The paper’s central result is that token-centric metrics miss non-inference bottlenecks and that tool sandboxes can alternate long idle spans with short resource bursts. This is evidence for aligning task completion, tool calls, context, queue/latency, and resource telemetry on the same run identity. It is not evidence that every service has the same bottlenecks.

MAServeBench narrows further to multi-agent serving. It makes collaboration topology a controllable workload factor and separates stage composition, task binding, deployment, and offered load. A native execution produces a hierarchical semantic trace; a frozen trace can be replayed to compare serving systems or feed an architecture simulator. Its README identifies contract tests and synthetic golden bundles, versioned state snapshots, backend telemetry adapters, and separate GPU and Ascend paths. Its own notes say driver and backend compatibility choices remain external and exact installed versions must be recorded.

The native/replay distinction should remain explicit in our evidence model: native runs measure the coupled agent-and-serving system; fixed-work replay isolates a realized workload for systems comparison but cannot measure whether a changed agent would have produced that same trace.

## Cross-lab evaluation codebases: related mechanisms, different targets

| Repository | Observed mechanism or scope | Snapshot caveat |
|---|---|---|
| [OpenAI Evals](https://github.com/openai/evals) | Registry plus custom and private evals; JSON/YAML templates; API cost warning; Git LFS holds registry data | GitHub metadata showed its latest commit on 2026-04-14. Its README discusses current dashboard evals, but this code repository is not proof of dashboard/repo feature parity. |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | UK AI Security Institute evaluation framework; prompts, tools, multi-turn dialog, model-graded evals, extensions, and 200+ packaged evaluations; checked-in lockfile and documented lint/test commands | The latest observed commit was 2026-11-09. The breadth of a framework’s component menu does not establish a specific task’s grader validity. |
| [EleutherAI LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) | Configurable few-shot evaluation with task YAML and plugins for model backends, filters, metrics, and aggregations | Its own README marks multimodal support as a prototype and points to a separate project for broader multimodal coverage. Latest observed source commit was 2026-09-14; repository push metadata was 2026-11-04. |
| [MLCommons Inference](https://github.com/mlcommons/inference) | Standardized model-serving speed measurement over deployment scenarios, with versioned submissions, reference implementations, and power measurement rules | The current README identifies MLPerf Inference v6.1 and an earlier submission deadline. This is a performance benchmark suite, not a general correctness or repo-health standard. |
| [Google DeepMind gBench](https://github.com/google-deepmind/gbench) | Repeated measurements, variability thresholds, open-loop load sweeps, and versioned experiment scaffolds that separate model subject from prompt, scoring, data, serving, and load setup | Owner documentation was read in the preceding C25 report; no implementation audit or benchmark run was made. |

The useful comparison unit is therefore a mechanism, not a logo or a single “standard”: task format, system boundary, oracle, model/harness separation, repetitions, variance, environment freeze, run artifacts, cost, access, and validation authority. These repositories answer different questions and should not be pooled into one leader board without an explicit common task and protocol.

## Frontier leads found through AlphaXiv

Two recency-ranked searches surfaced additional directions worth following after this bounded pass:

- [Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868), Adobe Research and UCLA, on building long-horizon environments with intermediate progress signals.
- [Investor’s Last Exam](https://arxiv.org/abs/2610.38342), a finance task where agents must base forecasts on information available at decision time, raising temporal leakage and future-information controls.
- [Embodied First Exam](https://arxiv.org/abs/2611.12177), recent robotics/coding-agent work surfaced on November 9.
- [SCI-AGENT-EXAM](https://arxiv.org/abs/2610.32441), [PLE](https://arxiv.org/abs/2610.30537), and [CUA-Recovery](https://arxiv.org/abs/2610.27645), followed above because their heterogeneous outputs, domain deliverables, or latent-failure methods connect directly to this project.
- [MAServeBench](https://arxiv.org/abs/2610.40293), [ARIES](https://arxiv.org/abs/2607.29069), and other agent-serving papers surfaced in a separate discovery query.

This is a useful discovery snapshot, not recall measurement. AlphaXiv ranks its indexed English-language arXiv material; it does not certify venue status, provide a global census, or guarantee that the highest-ranked paper has a usable artifact. Each lead must be followed to the canonical paper version, affiliation evidence, repository, task/data license, and current release.

## Candidate directions for the generalized research matrix

These results add candidate dimensions to the existing open-ended system and source matrix:

1. **Outcome contract:** required deliverables, hard safety/feasibility constraints, soft objectives, valid equivalents, and downstream acceptance.
2. **Oracle trust:** deterministic properties, judge rubric and calibration, hidden/reference data, human validation, positive and negative examples, grader mutation or gold-solution checks, and known omissions.
3. **Failure chronology:** root cause, preserved state lineage, detection delay, recovery action, cascading side effects, and whether a later event hides the earlier fault.
4. **System and run provenance:** pinned task commit, model and harness, environment image, trace/event identities, dataset split, configuration, seed/repeats, telemetry, output hashes, resource use, and grader version.
5. **Lifecycle comparability:** task edits, migrations, retirements, environment changes, license/access changes, whether agents were rerun, and what evidence supports score comparison.
6. **Evaluation boundary:** code artifact, multi-repository system, desktop workflow, scientific result, physical-engineering deliverable, model-serving stack, or hardware workload; keep native outcome evaluation separate from replay or component-only checks.
7. **Availability and authority:** public versus gated versus hidden tasks, operator-controlled submissions, author self-report versus external validation, regional/language coverage, and who can run and publish evaluations.

Project inference: these records favour a composable evidence framework where a domain profile can declare applicable obligations and required evidence, while a shared run/evidence format preserves provenance. They do not establish a universal score, an always-on mandatory gate set, or a complete role/system taxonomy.

## Limits and next work

- This pass read papers and selected READMEs, release docs, metadata and trace docs. It did not audit implementation code, execute a benchmark, test a verifier, run a model, or download task data.
- Current repository snapshots are mutable. HEAD commit IDs, licenses reported by GitHub, gated resources, and release claims are recorded in the search log; recheck before implementation or redistribution.
- The SCI-AGENT-EXAM repository is an extract with five example tasks; CUA-Recovery says its dataset release is pending; PLE’s hidden evaluation was not accepting submissions on its latest observed commit; MAServeBench did not report a license in fetched repository metadata.
- Exact GitHub repository search for CUA-Recovery returned zero, but following the paper’s direct code link found the repository. This is a measured search miss, not evidence the repo was absent.
- The science, physical engineering, computer-use, serving, and professional-work task sets are all selective. Their results cannot establish broad rates for unrelated system types.
- Continue with embodied systems and robotics, developer- and operator-facing agent failures, task-oracle validation, regional labs and non-English venues, and system-specific evidence generated from the Computer System Atlas. Integrate the user’s pending role list when supplied.
