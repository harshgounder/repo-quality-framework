# Freshness and specialized depth

**Working protocol, 2026-11-10.** A claim that the project has found every current or cutting-edge practice cannot be established by a fixed search. Maintain a dated, repeatable surveillance process with explicit blind spots.

## Capture separately

For each source: first publication date, most recent substantive revision, version/commit and release date, access date, applicable ecosystem/runtime/platform version, source type, venue and review/publication status, independent replications, implementation availability, measured outcome and limits. Distinguish a recent webpage crawl or new blog post from a new method; distinguish preprint, accepted publication, released tool, roadmap, abandoned prototype and current production practice. Version drift reopens applicable cells.

## Search from several directions

- Recent research: conference proceedings, preprints, bibliographies, citation trails, artifact-evaluation results, reproducibility packages and benchmark datasets.
- Tool and platform evolution: release notes, changelogs, proposals/RFCs, compiler and runtime mailing lists, issue trackers, open pull requests and deprecation notices.
- Specialized communities: language ecosystems, framework maintainers, embedded/real-time, database, GPU/HPC, mobile, web performance, scientific computing, graphics/game, safety and security.
- Empirical and operational evidence: benchmarks, incident reports, performance regressions, maintainers' case studies, user studies and counterexamples, including failures and negative results.
- Historical foundations: retain older work when still relevant; compare with the newest revision and independent replications. Do not rank by novelty, stars, publicity, result count or vendor assertions.

## Specialization model

An assessment can compose a general core with multiple conditional packs, rather than one exclusive template. Example: Rust + WASM + browser + accessibility + security-critical + small volunteer team. Packs add applicable responsibilities, terminology, evidence methods, compatibility constraints, specialists and authoritative sources; they may conflict and need a documented precedence and resolution path. A project can have many artifacts and runtime/deployment targets. Host or repository language detection alone is insufficient to infer all of them.

Inspect hard cases: optional features and architecture targets, public APIs, plugins and dynamic entry points, reflection, generated code, mixed runtimes, monorepos, proprietary environments, unusual language versions and end-of-life systems. Record unknown rather than guessing a pack or applying every available rule.

## Cadence and output

Each campaign records search interval, native publication dates, ranking/filters, languages, venues, exact queries, selected sources and access gaps. Before each synthesis or release, refresh changes since the last search and spot-check version-sensitive claims. User-requested ongoing monitoring or alerts would require a separate automation; this document itself schedules nothing. Planned queries and routes are not completed searches.
