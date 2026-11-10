# Research start plan

**Version:** 0.1
**Started:** 2026-11-10 (Asia/Kolkata)
**Status:** active research plan; the framework and its gates remain undecided.

## Purpose

Build an evidence-backed account of what repository-quality systems can reliably observe, what they infer from those observations, and what decisions those inferences can support across different kinds of work.

The work starts with evaluation mechanisms because they expose assumptions clearly. Source and community mapping continues alongside it across regions, languages, code hosts, social networks, forums, standards, research venues, and practitioner communities. The first rater sample is a sequencing choice based on accessible primary materials; it does not define the eventual platform or project scope.

## The first framing model

For every candidate rule or score, trace this chain:

> **Target entity → intended property → observable evidence → inference or transformation → decision → observed outcome**

Keep the following entities distinct: repository, released artifact/package, team or community, organization, deployed product/service, and research/data artifact. A repository can be easy to inspect while the product is unsafe; a healthy community signal does not prove implementation quality; a source-code metric does not automatically establish usability or operational reliability.

Do not assume that one “quality” value can combine all these properties. First identify when properties can be evidenced together, when they conflict, and which decisions each property can support.

## Workstreams

### 1. Keep widening the source map

Maintain the source register across:

- global, regional, self-hosted, federated, and domain-specific code forges;
- social networks, Q&A, developer forums, mailing-list archives, issue trackers, public chats, conference talks, and video/podcast sources;
- standards bodies, government guidance, foundations, scholarly indexes, proceedings, postmortems, and practitioner handbooks;
- region and language, with access, indexing, and search limitations recorded.

For each platform family, distinguish its own policies from the projects hosted there and distinguish the platform's software from any hosted instance.

### 2. Build a mechanism atlas

Audit representative examples of different mechanisms:

- automated probes and check scores;
- maturity-level requirements and security baselines;
- self-assessment badges with automation, spot checks, and appeals;
- file-presence and platform-generated project profiles;
- human rubrics and organization intake assessments;
- implementation-agnostic metric libraries and dashboards;
- weighted composite indices and percentile/rank models;
- component criticality, popularity, or selection signals that are often mistaken for quality;
- domain-specific checks such as accessibility, API compatibility, reproducibility, licensing, or research-software readiness.

For each system record the construct, unit, evidence sources, rules, aggregation, unknown/non-applicable behavior, profile/context handling, versioning, validation, false-result risks, maintenance cost, and assurance boundary.

### 3. Test the measures against independent evidence

Use empirical papers, systematic reviews, practitioner intake studies, case studies, and incident reports to ask whether signals measure their intended construct and predict useful outcomes. Record sample, time window, population, method, findings, limitations, and the kinds of claims the study cannot support. Treat a paper's conclusions in proportion to its design and population.

### 4. Map responsibilities to artifacts and lifecycle

Use role-based lenses to find missing responsibilities: maintainer/project owner, user/dependency consumer, domain expert, QA/testing, security, privacy/legal/licensing, accessibility/UX/design, release/build engineering, SRE/operations, documentation, governance/community, data/research stewardship, and incident response. These are discovery lenses, not a final list of required roles.

Cross them with artifact type and lifecycle. Candidate interactions include:

- library/package × release × compatibility and provenance;
- service/infrastructure × deployment × reliability and incident response;
- research software/data/model × publication × reproducibility, citation, and data stewardship;
- website/application × user journey × accessibility, privacy, and safety;
- small or volunteer-maintained project × any requirement × maintainer burden and realistic evidence.

### 5. Seek counterexamples and incentives

For each promising indicator, find examples where it disagrees with the outcome: a high-scoring project that failed, a low-scoring project with justified reasons, a missing file that did not imply a missing practice, or a badge/check that could be gamed. Record selection bias, Goodhart effects, popularity incentives, and harm from false assurance.

### 6. Synthesize only after the gaps are visible

The synthesis may eventually describe profiles, conditional requirements, advisory findings, gates, or user-defined policy. No universal score, mandatory checklist, or gate should be proposed until applicability, evidence, errors, cost, exceptions, and validation have been examined.

## First research tranche

The first tranche combines two lines of evidence:

1. **Mechanism representatives:** OpenSSF Scorecard, OSPS Baseline, OpenSSF Best Practices Badge, CLOMonitor, CHAOSS, a broad health index, a local repository-hygiene scorer, and an OSS health intake rubric.
2. **Measurement and practice studies:** context-sensitive OSS sustainability indicators, QA badge use, practitioner intake needs, repository stability measures, code-metric construct validity, and multi-dimensional software-quality datasets.

This is not a popularity ranking. The candidates were chosen to contrast different claims and evaluation methods. A source may be included as a useful comparison without being considered a general repository rater.

## First-tranche deliverables

- A readable mechanism card for each representative system, with primary links and version date.
- Selected filled matrix cells that record exact queries, filters, platform, evidence role, artifact/context scope, result screening, and remaining gaps.
- A small evidence map distinguishing tool-owner claims, normative requirements, empirical results, and practitioner findings.
- An explicit list of conflicts, unknowns, inaccessible sources, language/region gaps, and unchecked domains.
- A next-batch selection based on unanswered high-impact questions, not on which search results were easiest to find.

## Decision gate before framework design

For any proposed requirement or gate, the research must be able to state:

1. what property it targets and at what unit;
2. why the property matters and which source supports that claim;
3. when it applies and how to represent unknown or not-applicable cases;
4. what evidence is used and what can be automated;
5. what false positives, false negatives, gaming, and burden it creates;
6. what validation exists, or that it remains an unvalidated proxy;
7. how exceptions, corrections, version updates, and appeals work.

## Current start point

The first mechanism and empirical evidence is summarized in [`../research/mechanism-audit.md`](../research/mechanism-audit.md). The source universe and query protocol remain in progress; see [`../RESEARCH_STATE.md`](../RESEARCH_STATE.md) and [`../research/search-log.md`](../research/search-log.md).
