# Open-world systems atlas and historical failures: research direction

## Mission clarification, 2026-11-11

The primary goal is the user’s generalized repository and system-quality framework, practices and eventually context-sensitive gates. The historical bugs, fixes and discussions below are **one source of evidence** for that goal, not an instruction to make a universal bug-solving database the main product. Positive practices, expert roles, standards, design, efficiency, user experience and the complete lifecycle are equally part of the research. See the [mission and product direction](../../../docs/project-mission-and-product-direction.md).

## User correction and full attachment read

The user wants every relevant part of every kind of system explored recursively, with deep continuing research—not a fixed selection of example products. They also want the project to learn from historical bugs, loopholes, mistakes, incidents, discussions and fixes across open-source projects and technical communities, including Stack Overflow, and scale the candidate pools into thousands per relevant class and beyond. This is an open-ended coverage goal, not a claim that all public, private, deleted or future data can be accessed or audited. Existing video and system examples are illustrations, not scope.

The newly supplied attachment is 6,263 lines / 116,037 bytes. A byte comparison found it is exactly one leading blank line followed by the previously supplied 6,262-line / 116,036-byte attachment; no other content differs. Two independent Luna reviewers reread the new attachment in consecutive bounded sections: lines 1–3132 and 3133–6263, respectively. Both read full text, not headings alone. The parent confirmed byte identity. These reads do not establish that its claims, external citations or the shared external conversation have been independently verified.

## What the attachment actually adds to the task

The first half spans mathematical and algorithmic foundations, data structures, compilers and runtimes, hardware and OS, protocols, cryptography and identity, user interfaces and accessibility, media, databases, distributed systems, AI, operations and the full range of product workflows. It includes concrete product families and their internal pipelines: for example payment authorization and accounting, ride dispatch and mapping, media ingestion and playback, source collaboration, moderation, administration and support. These are entry points for discovery, not a closed universe. The second half adds end-to-end request and data flows, system-specific operating constraints, and a deep expansion of computational foundations and specialist engines: exact and arbitrary-precision arithmetic, numerical stability, sparse linear algebra, graph and string structures, geometric predicates, approximation, optimization, SAT/SMT, compression, error correction, formal verification and related engines.

The essential distinction is **primitive/algorithm → implementation/engine → component → subsystem → whole system and operational workflow**, with many-to-many links rather than an obligatory linear stack. The same primitive can support multiple products; quality depends on input data, representation, constraints, environment, users and downstream consequences. Alongside those relationships are developer, operator and user workflows; data movement and lifecycle; failure modes; safety, performance, security, accessibility, cost, governance and recoverability. A repository can expose only part of the needed evidence. Even this detailed atlas is a set of discovery leads, not a complete or validated list of all relevant systems and techniques.

## Research object: full evidence chain

For every candidate, the target record is not just an issue title or source file. Where material exists, trace:

1. **Context:** system and component, environment, version, workload, data, assumptions, stakeholder and observed consequence.
2. **Problem:** the original report, reproducer, failing behavior, affected contract, preconditions and counterexamples; distinguish suspected cause from demonstrated cause.
3. **History:** relevant issue and discussion, incident or Q&A, project, branch/release, cross-references, competing diagnoses, reopenings and duplicates.
4. **Change:** proposed and accepted patches, commits and reviews; distinguish merged, rejected, reverted, partial, superseded, workaround and unknown. A link between an issue and PR is not proof of a fix.
5. **Evidence of behavior:** regression tests, expected result/oracle, prior test gaps, build and CI evidence, reproduction or independent validation when practical. Record when unavailable; a test added to a PR is not proof it was run.
6. **Transfer:** generalizable mechanism and proposed check, its applicable contexts, input and output, limitations, false positives/negatives, performance and operational cost, counterexample and evidence strength. Proposed checks are not universal mandatory gates.
7. **Follow-through:** release and deployment, residual damage, backports, alternative solutions, user/operator recovery and later rediscoveries or regressions.

Not every case has a fix, is software-caused, or can be recovered. Record unknowns and failures to access sources. Preserve competing explanations and the context in which fixes work; do not flatten everything to a single “root cause.”

## Source routes and their units

| Route | Useful unit and relationship | Limits and immediate work |
|---|---|---|
| [GitHub issue timeline](https://docs.github.com/en/rest/issues/timeline), [event types](https://docs.github.com/en/rest/using-the-rest-api/issue-event-types), PR/commit APIs | Issues, comments, close/reopen events, references, patches and tests; closure references and commit mentions are distinct edge types | Per-project labels are inconsistent, links are incomplete, issue closure is not proof of correctness; rate, pagination and access constraints. Existing 1,577 links are unreviewed search leads. |
| [GH Archive](https://www.gharchive.org/) | Timestamped public GitHub events in hourly files since 2011; broad discovery and chronology | Event stream, not complete project snapshots or proof of every issue/fix; changed underlying event APIs and schema. |
| [GitLab issue API](https://docs.gitlab.com/api/issues/), merge-request and commit APIs | Project issues, references, MRs, commits, diffs and available CI | Public/project scoped access and pagination; confidential issues and private data unavailable; issue/MR linkage and test results not guaranteed. Other forges and self-hosted instances need their own adapters. |
| [Stack Exchange public data](https://stackoverflow.com/help/data-dumps), [Stack Exchange API](https://api.stackexchange.com/docs) and [data explorer](https://data.stackexchange.com/help) | Question, answer, revision and comment; sometimes candidate diagnosis or workaround | A forum answer is a claim, not automatically a validated fix; accepted/score is not proof. The current dump requires account access and an affirmation concerning LLM training. No dump was downloaded or terms accepted here. Check current terms, licensing and intended use before acquisition. |
| [Software Heritage data](https://docs.softwareheritage.org/user/using_data/index.html) | Archived origin, revision and source artifacts, when available | Code archive, not an inherent issue/PR/test archive; archival lag, missing/deleted sources and identity complications. Parent web opening was access-denied; search excerpt and other source checks do not establish full current coverage. |
| [SWE-bench dataset guide](https://www.swebench.com/SWE-bench/guides/datasets/) | Curated records with issue, base revision, patch and test-related information | Useful linked examples, not the universe; selection, language and benchmark construction bias. Test patches and benchmark pass do not establish all system qualities. |
| Project trackers, mailing lists, forums, regional forges, advisories, incident archives, manuals and standards | Native reports, patches, discussions, incident evidence and normative constraints | Need source-specific routes, identifiers, translations and access/retention records. GitHub, Stack Overflow and the above are starting points, not a ceiling. |

## Scale and continuity rules

Build separately countable pools for systems/components, reports/incidents, causes/mechanisms, fixes and rejected fixes, tests/oracles, tools, standards, designs, benchmarks, estimates, roles/workflows, communities and further discovered classes. User's thousands-per-class requirement is an ambition for each relevant class; don't fill a quota with generated combinations, repeated files, unsupported estimates or dubious aliases. Track source-specific leads, distinct source objects, resolved entities, opened primary sources, independently appraised relationships, reproduced behaviors and validated checks separately. Record geography/language, dates, skipped partitions, access/retention, query and retrieval windows, and audit samples; no count of one class demonstrates worldwide coverage.

A production ingestion architecture still needs to be designed and verified: resumable source-specific harvesters, immutable source/version provenance, normalized identities and many-to-many evidence links, safe deduplication, explicit uncertainty, rights/attribution, changing data and deletion handling, resource budgets, and independent quality checks. No such universal corpus or pipeline exists yet. Continue extracting and appraising actual cases now while building it; do not substitute the architecture plan for the research itself.

See [the worked issue-to-fix trace](clickhouse-trace.md) for one narrowly investigated example, not a template that defines which systems matter.
