# Repository Quality Framework Research

This repository is the working home for research toward a **general-purpose, evidence-based framework for making software repositories dependable, usable, maintainable, and fit for their purpose**.

The intended reach is broad: repositories made by people or AI, across different languages, domains, sizes, maturity levels, and hosting platforms. The project must account for the fact that a library, a research artifact, a website, an infrastructure repo, a data project, and a small script do not have identical obligations. The eventual framework may therefore need profiles, conditional requirements, and evidence-based gates instead of one undifferentiated checklist.

## Current phase

**Research design and source mapping.** The repository is deliberately not yet a product specification, scoring system, template repo, or implementation. The earlier reconnaissance is a starting set of leads, not a completed survey. Read [`RESEARCH_STATE.md`](RESEARCH_STATE.md) before continuing; update it whenever research advances or a decision changes.

## Working principles

- Cover practices that materially affect repository outcomes, including engineering, security, operations, governance, accessibility, documentation, user experience, release quality, and stewardship.
- Separate normative standards, platform rules, empirical research, expert practice, tool checks, and community opinion. They are different kinds of evidence.
- Record sources and claims at the smallest useful level, including date, scope, method, limitations, and conflicts.
- Treat missing evidence as unknown. A search result, badge, or passing automated check is not proof of overall quality.
- Design for applicability: a requirement should say when it applies, how it can be evidenced, and who bears the cost.
- Keep the source universe and research coverage visible. “Searched,” “saturated,” and “complete” are not interchangeable.
- Do not turn the research notes into a universal gate before examining false positives, burden, gaming, context, and failure modes.

## Repository map

- [`RESEARCH_STATE.md`](RESEARCH_STATE.md): continuity ledger and exact current status.
- [`AGENTS.md`](AGENTS.md): instructions for future contributors and AI agents working here.
- [`docs/research-protocol.md`](docs/research-protocol.md): research dimensions, evidence handling, sampling, and stopping rules.
- [`docs/source-universe.md`](docs/source-universe.md): candidate platform and source families; seeds are explicitly unverified and non-exhaustive.
- [`docs/decisions.md`](docs/decisions.md): settled directions and open decisions.
- [`research/preliminary-findings.md`](research/preliminary-findings.md): early leads with scope cautions and source links.
- [`research/search-ledger.csv`](research/search-ledger.csv): search activity log; exact query strings are required for all new work.
- [`research/matrix-template.csv`](research/matrix-template.csv): schema for multidimensional coverage tracking.

## Status language

Use `unplanned`, `queued`, `searched`, `thin`, `inaccessible`, `conflicting`, or `saturated` for matrix cells. `Saturated` means additional targeted searches are producing little new evidence **for the recorded cell and search method**; it does not mean the whole platform or topic is exhausted. Reserve `complete` for a defined deliverable whose acceptance criteria have been checked and recorded.
