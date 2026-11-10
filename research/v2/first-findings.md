# New starting points and primary-source mechanism notes

Status: discovery and limited primary reading, 2026-11-10. Do not interpret this as comprehensive coverage.

## The user's original pre.dev estimator

Fetched, did not execute, https://api.pre.dev/api/code-licensing/estimate.mjs on 2026-11-10. SHA-256: 208c9f43972ef81469cd43a37299190c1e3040e91895ed51dc9f1299b638dc23. This URL can change; the hash identifies the inspected snapshot. The script itself says it is extracted from the production counter and that nothing leaves the machine; those are author claims, not independent confirmation of server behavior.

The inspected script imports Node child_process, fs and path; runs Git commands against local repositories; and prints an estimated non-exclusive license value. Code and text/config extensions are allowlisted; listed vendor/build directories and patterns are skipped. It counts qualifying HEAD blobs and history blobs reachable from all refs, excluding blobs present at HEAD; history is capped at 100 MiB per path. It identifies some minified/bundled content by filename and long-line heuristic. Text bytes counted are capped at ten times code bytes separately for HEAD and history. It approximates tokens by floor(bytes/4), then calculates source tokens × $100/1M + history tokens × $40/1M. It can count local branches not pushed to the remote. A text-only repository can therefore receive zero counted text when counted code is zero.

This is a pricing heuristic, not evidence of quality, license compliance, ownership, originality, usefulness or market price. Extension classification, Git-object enumeration, minification heuristics and history/path cap are material assumptions. We did not execute it, verify all code paths, compare it with the dashboard, inspect production backend, or validate market outcomes. This finding says what the inspected script appears to do, not whether the vendor's broader service has other capabilities.

## Newly discovered methods and sources

- [Eclipse QSOS](https://qsos.org/): the owner page describes define → evaluate → qualify → select; its stated 0–2 assessment scale is subsequently weighted according to the adopter's criteria. It is intended for OSS selection and maturity, a different decision from judging every kind of repository. Owner claims about reproducibility and auditability still need implementation and independent evaluation.
- [RSMM research-software maturity model](https://arxiv.org/abs/2406.01788): the authors' abstract says it combines a literature review and expert interviews to organize 79 practices into 17 capabilities and four focus areas. This is an author claim in a preprint abstract, not independent validation; full methods, rubric and implementation remain to be examined.
- [IEEE SWEBOK](https://www.computer.org/education/bodies-of-knowledge/software-engineering): a candidate source for mapping knowledge areas and overlooked responsibilities. Search excerpts surfaced its 18 knowledge areas; direct fetch returned 403, so inspect an accessible primary copy before mapping its actual contents.
- [UN Open Source United common policy framework](https://opensource.un.org/sites/default/files/2025-07/common_policy_framework.pdf): surfaced as an institutional policy source; direct web fetch returned 403, so policy details are unverified.
- [FAIR software recommendations](https://fair-software.eu/recommendations/): research-software candidate; direct fetch failed, so do not infer its current criteria from snippets.
- [Software Heritage](https://www.softwareheritage.org/), Zenodo, Dataverse, institutional and disciplinary archives are distinct source/archival infrastructure candidates. Direct Software Heritage fetch returned 502. Their presence in the route inventory does not establish that they are interchangeable with Git forges.

Further leads: research software maturity, reproducibility assessment, public-sector procurement, professional competency taxonomies, artifact-evaluation committees, archival repositories, registries and package ecosystems. Need inspect source ownership, versions, evidence and applicability before drawing conclusions.
