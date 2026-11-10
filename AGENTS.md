# Working instructions

Before doing work, read `RESEARCH_STATE.md`, then the relevant protocol/source/decision files. This file is here to preserve scope when work resumes in a later session or is performed by an AI agent.

## Scope discipline

- The goal is a generalized framework for repositories used across kinds of work. Do not silently narrow it to GitHub, public open source, application code, one language, AI-generated repositories, or security alone.
- The current phase is research design and evidence gathering. Do not claim the framework, dimensions, scoring, gates, or source coverage are settled unless a decision is recorded with evidence.
- Do not equate file-presence checks with quality. Investigate the mechanism, what it observes, what it misses, and whether the check fits the artifact and context.
- Preserve disagreement and negative evidence. Do not resolve a conflict by counting search results or repeating a popular claim.

## Continuity and evidence

- Update `RESEARCH_STATE.md` at the end of each meaningful work session: what changed, what was actually searched/read, what remains, and the next action.
- Add every new search to `research/search-ledger.csv` with date/time and timezone, platform/tool, exact query or a clearly marked API operation, filters, result/screening counts when available, outcome, and follow-up.
- Add source records and claims with direct links in the appropriate research note. Distinguish direct source evidence from interpretation and from social-media leads.
- Never upgrade a lead into a fact without opening the underlying primary source where possible. Record access failures and why coverage is incomplete.
- Mark retrospective searches as retrospective. If the original exact query is unavailable, say so; never reconstruct it as if it were verbatim.
- Use dates and versions. Standards, platform features, and tool behavior change.

## Matrix discipline

- Treat the project as a multidimensional coverage problem, not as an unchecked exhaustive Cartesian crawl. Preserve every dimension in the model, then use declared sampling and prioritization to cover combinations.
- A matrix cell is defined by its actual dimension values and scope. Record the search method and evidence count before changing status.
- Use the status definitions in `README.md`. `Saturated` is local to a cell, query strategy, language, access level, and date range. It never means globally exhaustive.
- Keep `unknown`, `not applicable`, `not searched`, `inaccessible`, and `no evidence found` distinct.
- Log interaction findings where dimensions compound (for example, artifact type × lifecycle phase × risk level), not only one-axis summaries.

## Avoid premature product decisions

Do not publish or implement a universal score, badge, mandatory gate, template, or “best practices” checklist until the research documents applicability, evidence quality, automation limits, tradeoffs, incentives/gaming risks, and validation plans. Ask the user about material direction changes, but continue independent research that does not depend on that answer.
