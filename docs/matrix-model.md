# Multidimensional research matrix

**Status:** model for organizing research coverage; it does not claim complete coverage.

## What the matrix represents

Let each research axis have a candidate value set, D1 through Dn. The theoretical search space is their Cartesian product:

    Ω = D1 × D2 × ... × Dn

The project is interested in combinations from Ω, not only a list of platforms or best-practice words. Each selected cell therefore records a tuple across source family and instance, region and language, evidence role, query family and exact wording, artifact, responsibility, lifecycle, risk and maturity context, evaluation mechanism, unit, time/version, access, and observed outcome.

Not every theoretical combination is meaningful. Define F as the subset of combinations that are applicable and feasible to research. For example, accessibility checks apply to user-facing artifacts; deployed operational evidence applies only when an artifact is operated; a forge feature is evidence about a platform's capabilities, not a hosted project's conformance. Record applicability as a finding, never silently as missing evidence.

The 18 seeded axes and the current row schema are in the dimension catalog and matrix template. They remain expandable as the research finds missing distinctions.

## How combinations are covered

The register is a sparse, evidence-backed tensor rather than an enormous unfiltered spreadsheet. It preserves the full axis model while explicitly selecting cells. Selection uses these lenses:

1. **Axis coverage:** ensure each source family, region/language, artifact, responsibility, lifecycle stage, and mechanism has at least a discovery path.
2. **Pairwise coverage:** deliberately examine important pairs such as artifact × lifecycle, responsibility × evidence method, platform × access, and context/risk × gate strictness.
3. **Compound coverage:** add triples or higher-order cells when the interaction changes applicability, burden, risk, incentives, or interpretation. Examples include solo-maintainer × security-critical library × release gate; research dataset × reproducibility × archival; and user-facing website × accessibility × public release.
4. **Counterexample coverage:** search combinations where a check passes before failure, a check fails for an irrelevant reason, a high score conflicts with direct evidence, or a justified exception is necessary.
5. **Gap-driven selection:** prioritize under-covered languages/regions, non-GitHub hosts, private/self-hosted access, non-code artifacts, marginalized user needs, and responsibilities with weak evidence.
6. **Stopping:** mark saturation only for the exact query strategy, language, time window, access mode, and selected cell after targeted variants stop producing material novelty. Never mark a whole platform or framework globally complete from a narrow cell.

For each chosen cell, record why it was selected and what it can and cannot establish. A result count is not a coverage score; a search may return a bounded, ranked sample and the tool may omit relevant sources.

## Reading and generating views

The CSV is the evidence ledger. Views can later pivot it by platform family, language/region, evidence role, artifact, responsibility, lifecycle, context, mechanism, and status. Coverage should be reported both by individual axis and by selected pairs/triples. Keep a separate list of unselected or currently infeasible combinations so the theoretical scope does not disappear just because a first sample is small.

The final research matrix must expose, at minimum:

- searched cells and exact query/filter histories;
- evidence returned, screened, opened, and retained as separate counts;
- source and claim links;
- applicability, unknown, not-applicable, inaccessible, conflicting, and no-evidence states;
- the reason for selecting the cell and the next action;
- underrepresented or inaccessible dimensions and important compound interactions.

Do not combine the axes into one rank or overall repository score during research. A future framework could present separate evidence-backed views or context-specific gates, but that is an open design question.

## Current coverage boundary

The current filled rows are deliberate samples, not the full Cartesian product. The first cells audit scoring, baselines, badges, project health checks, and empirical indicators. The next cells broaden to standards, regional forge documentation, community discussions, and independent signal-validity studies. The most important unfilled work remains native-language and region-specific searches, host-by-host verification, domain-specific non-code artifacts, operational incidents, practitioner roles, and prospective or causal validation.
