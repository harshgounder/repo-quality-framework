# Candidate source universe

This is a **seed map, not an exhaustive inventory**. Inclusion does not mean a source has been checked for current activity, authority, accessibility, or relevance. For each source eventually record region, language, access method, primary/secondary role, update recency, and actual coverage. Add discoveries rather than treating this list as closed.

The structured working list is [`../research/source-register.csv`](../research/source-register.csv). Search results in the first pass surfaced local/regional hosted services, federated/emerging forges, Chinese-language developer communities, and more evaluator types than the initial list. Those are kept as separate candidates in the register; a search snippet alone does not verify them.

## Code forges and source collaboration

### Broadly used hosted forges

- GitHub
- GitLab.com
- Bitbucket Cloud
- Azure Repos

### Open-source or self-hostable forge ecosystems

- Codeberg / Forgejo
- Gitea-hosted instances
- SourceHut
- Gerrit-based projects
- Pagure
- Savannah
- Launchpad
- SourceForge
- Radicle

### Regional or country-specific candidates to verify

- Gitee
- GitCode / AtomGit
- Other regional public forges discovered during research

The first discovery pass surfaced a mix of regional services and region-hosted instances. Official pages describe AtomGit/GitCode as code-hosting services undergoing integration; European search results include Forgejo-powered hosted offerings; and Entire advertises code-hosting regions including India and Singapore. These are different service models and maturity states, and promotional claims require corroboration. They are logged as candidates rather than evidence of a stable regional platform landscape.

Inspect more than repository pages: issue and discussion areas, pull/merge requests, CI/workflows, security advisories, release pages, package registries, organization policy, project templates, and platform documentation. Distinguish what is a platform feature from what is a project requirement.

## Social networks, discussion venues, and communities

### General and developer-oriented networks

- X
- Reddit and relevant subreddits
- Hacker News
- Stack Overflow and other Stack Exchange communities
- Lobsters
- DEV Community
- Hashnode
- LinkedIn
- Bluesky
- Mastodon and other federated communities

### Forums, Q&A, chat, and long-form discussion

- Public Discourse forums
- Project/community forums
- Public mailing lists and archives
- Public Slack, Discord, and Matrix spaces where accessible and appropriate
- Issue trackers and project discussions on code hosts
- Conference Q&A, talks, and recorded panels

### Regional/language-specific candidates

- Zhihu, V2EX, CSDN, Juejin, OSChina, Bilibili
- Qiita and Zenn
- Habr
- Other region/language communities found through translated discovery queries

The first pass found Korean developer-community directories and an active OKKY community page, plus Japanese Q&A/community discovery pages. The second pass opened Open edX and SustainOSS Discourse discussions and screened a Rust-language forum checklist. These are qualitative, context-specific sources; broad merged queries against Hacker News, Stack Exchange, and Lobsters did not provide strong hits in the returned windows. These directories are discovery aids, not authorities; verify each destination and include local-language searches in later matrix cells.

Social content is often ephemeral and context-poor. Capture post/thread date, author/context when relevant, replies, and the underlying source. Do not treat a viral claim as a standard or validated result.

## Standards bodies and public guidance

Candidate bodies and ecosystems include ISO/IEC, IEEE, IETF, W3C, ECMA International, NIST, CISA, OWASP, OpenSSF, CNCF, Linux Foundation projects, OASIS, SPDX, CycloneDX, CHAOSS, FORCE11, and Research Data Alliance. Also identify national standards bodies, regulators, public procurement guidance, and domain-specific authorities as research reveals relevance.

Potential topic areas include software/system quality, secure development, web accessibility, identity and privacy, software supply-chain security, build provenance, SBOMs, licensing, research software, data stewardship, API compatibility, documentation, governance, sustainability, and AI/ML model or dataset practice.

## Research literature and scholarly infrastructure

- ACM Digital Library
- IEEE Xplore
- arXiv
- OpenAlex
- Crossref
- Semantic Scholar
- Conference and journal proceedings in software engineering, security, HCI, scientific computing, open source, and software operations
- University repositories, theses, and research group pages

The first empirical seed set now includes context-sensitive OSS sustainability indicators, QA-badge usage, organizational intake interviews, repository-stability metrics, code-metric construct validity, a multi-dimensional quality dataset, and a review of OSS evaluation indicators, badge signaling research, popularity-proxy validation, and a tertiary review of code-metric evidence. Second-pass standards discovery surfaced product-quality, quality-evaluation, data/ML quality, secure-development, and research-evidence standards. These are different populations and study designs; the citations and scope limits are in [`../research/mechanism-audit.md`](../research/mechanism-audit.md) and `../research/source-register.csv`.

Use scholarly indexes for discovery, then inspect the paper and its methods. Track publication date, study population, outcome measure, limitations, replication/data/code availability, and whether claims generalize beyond the study.

## Practitioner and operational evidence

- Engineering handbooks, architecture decision records, design reviews, and public engineering blogs
- Public postmortems, security advisories, incident reports, audit reports, and reliability reviews
- Maintainer guides and governance/contribution handbooks
- Conference talks, workshops, podcasts, and interviews
- Public procurement and organizational engineering standards
- High-quality project documentation and repository policy examples

Identify authorship and context; distinguish a case study from a universal rule.

## Repository raters, badges, and adjacent tools

Initial candidates include OpenSSF Scorecard, OpenSSF Best Practices Badge, OSPS Baseline, CLOMonitor, LFX Health Score, GitHub Community Profile, REUSE, pre.dev codebase/licensing estimator, Repository Standards, Microsoft Agent Readiness Check (AgentRC), and eyebrow. The first discovery pass added inspect.software, RepoPulse, RepoHealth, heff/repo-health, Apereo OSS Rubric, OpenSSF Criticality Score, CHAOSS metrics, and Gitee OSS Compass. They span distinct constructs: hygiene, health, maturity, community measurement, component selection, criticality, security, and agent readiness. The [`rater-inventory.csv`](../research/rater-inventory.csv) records these separately with verification state and open mechanism questions. Also discover ecosystem/package health dashboards, CI policy packs, documentation/accessibility checks, reproducibility tooling, and organization-specific maturity models.

For each candidate, trace from marketing/introduction to the actual rule set, source code, scoring logic, version history, evidence provenance, and adoption/validation evidence. Classify its intended target accurately; an adjacent or narrow tool is not automatically a general repository quality rater.

## Queries to grow the map

Search for local hosting networks and forge software, regional social platforms, language-specific developer forums, domain-specific quality regimes, overlooked professional roles (such as security, SRE, accessibility, privacy, UX, release engineering, technical writing, governance, and research data stewardship), and communities representing small or under-resourced maintainers. Log discoveries and selection decisions in the matrix/ledger.
