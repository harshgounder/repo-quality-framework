# Search and access log

**Date:** 2026-11-10, Asia/Kolkata. This is discovery pass 1. The tool result counts are not counts of unique sources or exhaustive coverage. Search-result snippets were not counted as opened pages. Full/primary excerpts are separately identified as fetched below.

## Access checks

### Agent Reach

- **Operation:** `agent-reach doctor --json`
- **Result:** command not found (exit 127). No Agent Reach platform searches were run. The command was unavailable in the prior session as well.
- **Working routes used:** connected Exa web search/fetch; Parallel web search/fetch; connected X search. The user also authorized their Brave browser for X, but this pass used the connected X search route.

### Parallel web research

- **Prior-session operation:** Parallel `web_research`; exact request payload was not preserved.
- **Result:** insufficient-credit response, HTTP 402. Ordinary Parallel web search/fetch worked in this pass.

## Search calls

### P-001 — global and regional code-forge discovery

- **Tool/run:** Parallel `web_search`, `search_f23bb9872d7be176b6eee22f339705e2`
- **Objective:** Map public and regional code hosting and collaboration platforms beyond GitHub. Prefer platform-owned pages, credible current directories, and country/language-specific sources; separate hosting software, hosted services, and regional instances.
- **Exact queries:** `regional code hosting platforms forge`; `China Gitee GitCode AtomGit platforms`; `global software development forges regions`.
- **Returned/screened:** 10/10 search results; 0 direct pages opened in this call; 8 candidate leads retained.
- **Leads:** Codeberg/Forgejo, Tangled, Entire, AtomGit/GitCode, Radicle, Codey, and other forge/service examples. See `source-register.csv`.
- **Next:** Verify on first-party pages; distinguish software, host, regional instance, and early-stage product.

### P-002 — developer community and archive discovery

- **Tool/run:** Parallel `web_search`, `search_4af5209fc6810b8af6554036a648a443`
- **Objective:** Map Q&A, forums, federated social, mailing lists, and public developer communities across regions and languages; note access constraints.
- **Exact queries:** `developer community platforms global regions`; `programming forums Q&A communities worldwide`; `open source mailing list archives directory`.
- **Returned/screened:** 10/10; 0 direct pages opened; 7 candidate leads retained.
- **Leads:** Apache, Python, and PostgreSQL public mailing-list archives, plus general community-platform examples.
- **Next:** Expand by language and project domain; mailing-list archives are a distinct source for design rationale and governance history.

### P-003 — standards and framework discovery

- **Tool/run:** Parallel `web_search`, `search_2806fe89694d502cbea9d4e3029e4002`
- **Objective:** Find authoritative standards and frameworks for software quality, secure development, open-source health, accessibility, research software, and sustainability.
- **Exact queries:** `software quality standards repository assessment`; `secure software development framework official`; `research software sustainability standards`.
- **Returned/screened:** 10/10; 0 direct pages opened; 8 candidate sources retained.
- **Leads:** NIST SSDF, OpenSSF OSS evaluation guidance, software quality standards, and criteria-based research-software assessment.
- **Next:** Build a versioned catalog with normative status, intended scope, and source edition.

### E-001 — evaluator discovery

- **Tool:** Exa `web_search_exa`, 8 results requested and returned.
- **Exact query:** `official documentation repository project health score evaluator criteria scoring mechanism open source project health badge maintainability community AI agent readiness`
- **Objective:** Find primary documentation for criteria, scoring, scope, and assurance limits.
- **Returned/screened:** 8/8 search-result documents; 0 separately fetched in this call.
- **Leads:** inspect.software health index, arun-gupta/RepoPulse, spbuilds/RepoHealth, heff/repo-health, and Apereo OSS Rubric.
- **Next:** Audit implementation, data, applicability, and validation; do not treat first-party claims as independent evidence.

### E-002 — regional host discovery

- **Tool:** Exa `web_search_exa`, 8 results requested and returned.
- **Exact query:** `regional developer code hosting platforms China Japan Korea India Russia Europe official Gitee GitCode Codeberg`
- **Objective:** Identify regional developer-hosting examples using current primary pages.
- **Returned/screened:** 8/8; 0 separately fetched in this call.
- **Leads:** Codeberg and AtomGit/GitCode material among other regional or hosting-related pages.
- **Next:** Search regional languages and distinguish platform from hosting region/provider.

### X-001 — repository health score discussion

- **Tool/route:** connected X search, account route `main`, Top results.
- **Exact query:** `"repository health" (score OR badge OR checklist) lang:en`
- **Returned/screened:** 7/7; 0 separate post opens; 3 useful leads retained.
- **Leads:** OpenAlternative's age-factor note and other score claims. The search had substantial irrelevant cryptocurrency/token-health noise.
- **Next:** Follow links to product sources and search for maintainer criticism, counterexamples, and score design rationale.

### P-004 — Asia regional hosting discovery

- **Tool/run:** Parallel `web_search`, `search_499f46aa3296317a8a326523fb167a69`
- **Exact queries:** `China public code hosting Gitee AtomGit GitCode`; `Japan Korea regional Git code hosting platform`; `India regional code hosting platform software forge`.
- **Returned/screened:** 10/10; 0 direct pages opened; 5 candidate leads retained.
- **Leads:** AtomGit/GitCode, Entire's India/Singapore pages, and adjacent AI/agent forge launches.
- **Next:** Native-language queries; check legal entity, active service, service model, and product status.

### P-005 — Europe/Russia regional hosting discovery

- **Tool/run:** Parallel `web_search`, `search_bab886576858af7408f48c1b16b5e3bf`
- **Exact queries:** `Russia GitFlic GitVerse code hosting`; `European regional code hosting forge platform`; `France Germany Spain Git code hosting services`.
- **Returned/screened:** 10/10; 0 direct pages opened; 8 candidates retained for verification.
- **Leads:** CodeFloe, Codey, gitbuild.dev, Codebahn, Pushin.eu, Vault42, fremforge, and Forge Simply. Search results mix live products, early access, waitlists, and promotional claims.
- **Next:** Verify activity/access, terms, hosting jurisdiction, and whether each is a service or forge implementation.

### P-006 — regional developer community discovery

- **Tool/run:** Parallel `web_search`, `search_d0c3ec18c45460374a13ad87dc56764a`
- **Exact queries:** `Japan developer Q&A community Qiita Zenn teratail`; `Korea developer community forum OKKY GeekNews`; `Brazil developer community forum software programming`.
- **Returned/screened:** 10/10; 0 direct pages opened; 7 leads retained.
- **Leads:** OKKY, Korean community directories, Japanese Q&A/community discovery pages, and KLDP. Some hits are directories or user-curated lists, not primary sources.
- **Next:** Verify current activity and run Korean, Japanese, and Portuguese native-language queries.

### P-007 — repository-health evaluator discovery

- **Tool/run:** Parallel `web_search`, `search_c75028177307501291c1a380bef31094`
- **Exact queries:** `repository health score GitHub project quality rater`; `open source project health metrics assessment tool`; `repository quality score rubric software project`.
- **Returned/screened:** 10/10; 0 direct pages opened; 9 candidate leads retained.
- **Leads:** spbuilds/RepoHealth, heff/repo-health, OpenSSF Criticality Score, CHAOSS metrics, Apereo OSS Rubric, arun-gupta/RepoPulse, and OSS Compass.
- **Next:** Classify by construct and mechanism; fetch primary material.

### X-002 — rater/mechanism discussion

- **Tool/route:** connected X search, account route `main`, Top results.
- **Exact query:** `"repository health" (score OR scoring OR metric OR rater) lang:en`
- **Returned/screened:** 9/9; 0 separate post opens; 4 leads retained.
- **Leads:** social claims about Git Health/GenLayer and RepoPulse by 3li3. Crypto/token-health content also appeared.
- **Next:** Inspect linked code/docs; do not merge RepoPulse projects with similar names.

### X-003 — AI-generated repository quality discussion

- **Tool/route:** connected X search, account route `main`, Top results.
- **Exact query:** `("AI-generated" OR "AI coding") repository quality standards checklist`
- **Returned/screened:** 15/15; 0 separate post opens; 2 adjacent leads retained.
- **Leads:** AI skill/repository lists and a code-review product; little direct evidence about generalized repo-quality frameworks.
- **Next:** Search role-specific language for review, architecture, accessibility, operations, and documentation.

### P-008 — CHAOSS primary-source discovery

- **Tool/run:** Parallel `web_search`, `search_89b7970f38847e137f61281911879190`
- **Exact queries:** `site:chaoss.community metrics community health`; `site:github.com/chaoss metrics model`; `CHAOSS software project analytics metrics`.
- **Returned/screened:** 10/10; 0 direct pages opened in this call; 8 leads retained.
- **Leads:** official Metrics Handbook, `chaoss/metrics`, metric approval process, metric models, and project charter.
- **Next:** Map metric governance and implementation-specific variations.

### P-009 — OSS Compass primary-source discovery

- **Tool/run:** Parallel `web_search`, `search_fffc50971d9f2b3ddc8b8a63c16f9725`
- **Exact queries:** `site:compass.gitee.com software evaluation metrics`; `Gitee OSS Compass assessment model`; `OSS Compass open source evaluation service`.
- **Returned/screened:** 10/10; 0 direct pages opened in this call; 8 leads retained.
- **Leads:** official software selection service, metric models, and criticality score pages.
- **Next:** Audit metric catalog, lineage, LLM role, scope, and explainability.

### P-010 — inspect.software method and validation discovery

- **Tool/run:** Parallel `web_search`, `search_0598a1b5fe2af63b3d608b2a2c6b7b10`
- **Exact queries:** `inspect.software health index methodology`; `inspect.software open source health index validation`; `inspect software repository score source code`.
- **Returned/screened:** 10/10; 0 direct pages opened in this call; 8 leads retained.
- **Leads:** first-party methodology, FAQ, insights, and reports; the targeted search did not establish independent validation.
- **Next:** Find/open scanner source and compare code to method; assess cohort, coverage, and independent outcome validity.

## Fetches and mechanism excerpts

### F-001 — evaluator repositories and guidance

- **Tool/extract:** Parallel `web_fetch`, `extract_36e733cba4d8db5312606405acae2728`.
- **Requested:** spbuilds/RepoHealth; heff/repo-health; ossf/criticality_score; guessed `chaoss/metrics-2`; apereo/oss-rubric; arun-gupta/repo-pulse; OSS Compass Criticality Score; inspect.software health-index wiki; OpenSSF concise evaluation guide.
- **Result:** 8 documents returned and screened; one URL returned HTTP 404 (`https://github.com/chaoss/metrics-2`). Correct CHAOSS URL later found as `https://github.com/chaoss/metrics`.
- **Use:** First-party descriptions were summarized in `rater-inventory.csv`; no full code audit completed.

### F-002 — methodology and official metric docs

- **Tool:** Parallel `web_fetch`; 8 URLs, 8 result excerpts, no fetch errors.
- **URLs:** inspect.software methodology/FAQ/wiki/about/insights; OSS Compass selection guide; CHAOSS metrics handbook and `chaoss/metrics`.
- **Use:** Confirmed what the primary pages state about weighting, missing data, intended scope, community metrics, and selection service. These are self-published method descriptions, not independent validations.

## Coverage boundary after this pass

- Searched multiple source families, but did not systematically search each named platform, every region/language, every artifact type, or compound matrix cell.
- Search-result counts are bounded by each tool's result window and ranking. A `searched` status applies only to the recorded query/method.
- No cell is saturated. No source family is complete.


# Discovery round 2 — 2026-11-10 (Asia/Kolkata)

**Search timing:** Search tools did not expose per-request timestamps. These calls were completed before the 11:43 Asia/Kolkata clock check; this log was compiled at 12:02 Asia/Kolkata. The individual request times are unavailable.

## E-003 — practitioner venue and community discovery
- **Tool:** Exa web_search_exa; 8 results returned and screened; 0 direct page opens in search call; 8 candidates retained.
- **Exact natural-language query:** Where practitioners discuss software repository quality standards, maintenance practices, engineering checklists, repository health, and quality gates across forums, mailing lists, and regional developer communities
- **Filters:** English-oriented relevance; requested primary community indexes and regional venues; result count 8.
- **Result examples:** Open edX repo best-practices thread; Sustain Open Source Forum template discussion; Stan Forums PR review standards; Geomys Standard of Care; Zalando release process.
- **Outcome:** Useful practitioner/forum leads; rankings also included irrelevant material. Four pages were opened in F-004. These are context-specific, not consensus evidence.

## E-004 — code forge alternatives and regional hosting
- **Tool:** Exa web_search_exa; 8 results returned/screened; 0 direct page opens in search call; 8 leads retained.
- **Exact natural-language query:** Official documentation for major code hosting platforms and forge alternatives including GitLab, Codeberg, SourceHut, Gitee, GitCode, Bitbucket, Gitea, and regional hosting ecosystems; repository metadata, CI, security, governance features
- **Filters:** Prefer official platform docs/current status pages; 8 results.
- **Results:** GitLab Docs; Gitea docs/comparison; Bitbucket code-repository page; Gitee repository help center; other hosting pages.
- **Outcome:** Leads only. Direct Gitee, Gitea, and Codeberg docs were opened in F-003/F-005. Result presence does not establish host activity or comparative quality.

## E-005 — cross-domain standards and research evidence
- **Tool:** Exa web_search_exa; 10 results returned/screened; 0 direct page opens in search call; 10 candidates retained.
- **Exact natural-language query:** Primary standards and frameworks for software product quality, secure development, accessibility, documentation quality, data quality, research software reproducibility, machine learning systems, and infrastructure as code
- **Filters:** Prefer primary bodies/specifications and current official pages; 10 results.
- **Results included:** NIST SSDF; ISO/IEC 25020, 25040, 5259-related pages; ACM SIGSOFT Empirical Standards; research software and ML guidance.
- **Outcome:** Demonstrates a wider standards universe than repository hygiene files. Standards have distinct units and roles; public pages provide metadata/abstracts, but complete ISO text is not included in these extracts.

## P-011 — broad community venue discovery
- **Tool/run:** Parallel web_search, search_45ea9b89a0205bfe468d68a5f829c802; 10 results returned/screened.
- **Objective:** Identify practitioner discussion venues and evidence, prioritizing primary community sources and regional/non-English coverage.
- **Exact queries:** repository quality communities forums; software maintainer discussions; regional code hosting platforms.
- **Filters:** Three related queries in one search; ranked 10-result window.
- **Outcome:** Leads included a GitHub Discussions adoption study, platform discussion docs, a Forgejo/Codeberg issue, and forum examples. One suspicious generic OpenCode result was not opened or trusted. Broad query was insufficient for platform-specific coverage.

## P-012 — cross-domain standards search
- **Tool/run:** Parallel web_search, search_95c63ddfda0783cbcc2d1cb49e0898fa; 10 results returned/screened.
- **Objective:** Find authoritative standards/guidance across software, data, research, and ML; distinguish standards from adoption guidance and empirical work.
- **Exact queries:** ISO software product quality standards; research software reproducibility guidelines; data quality machine learning standards.
- **Filters:** Three related queries; ranked 10-result window.
- **Results:** ISO/IEC 25010:2023, 25040:2024, 5259 parts, and ACM SIGSOFT Empirical Standards.
- **Outcome:** Official metadata and selected excerpts opened in F-003/F-006. Distinguish product-quality, evaluation-process, data-quality, secure-development, and research-evidence standards.

## P-013 — signal validity, failures, and gaming
- **Tool/run:** Parallel web_search, search_4cb03d73cf5c16b2187d52079462bda5; 10 results returned/screened.
- **Objective:** Find empirical/operational critiques or counterexamples about badges, stars, repo scores, and quality measures.
- **Exact queries:** software quality metrics Goodhart effect; open source badge false assurance; repository score metric validity.
- **Filters:** Three related queries; ranked result window.
- **Results:** 2018 ICSE badge study; 2024 QA badge study; 2024 NDSS GitHub-stars study; tertiary review of code metrics; 2026 supply-chain trust-signal preprint.
- **Outcome:** Mixed evidence. The badge study is positive counter-evidence within npm; the stars study is about importance/use and finds language-specific proxy variation; preprint requires follow-up.

## X-004 — repository health, standards, and gate discussion
- **Tool/route:** Connected X search; account route main; product Latest; limit 20.
- **Exact query:** ("repo quality" OR "repository health" OR "project health") (standards OR checklist OR score OR gates)
- **Returned/screened:** 20/20; one adjacent AI-repository-cleanup lead retained; no validated general-framework evidence.
- **Outcome:** High noise and irrelevant content. This query does not characterize X as a whole.

## X-005 — badge and metric gaming
- **Tool/route:** Connected X search; account route main; product Latest; limit 20.
- **Exact query:** (badge OR score OR checklist) (Goodhart OR gaming OR "false assurance") software
- **Returned/screened:** 20/20; 0 reliable leads retained.
- **Outcome:** Mostly unrelated results. Search vocabulary or X indexing may be a poor route; do not interpret as no discussion.

## P-014 — direct venue queries (Reddit, Hacker News, Stack Exchange, Lobsters)
- **Tool/run:** Parallel web_search, search_c4e3a4df30d1d314f511b334e1632392; 10 result rows across 4 queries.
- **Objective:** Search named practitioner communities for repository standards and quality experience; treat posts as anecdotal.
- **Exact queries:** site:news.ycombinator.com repository quality standards; site:reddit.com repository quality checklist; site:stackoverflow.com repository best practices; site:lobste.rs software project quality.
- **Outcome:** Results included Reddit checklist/git-practice threads, a software-quality opinion thread, and an individual Rust repo checklist. No strong HN, Stack Exchange, or Lobsters item appeared in the top window. No original thread was opened in this cell. Separate venue queries are needed because combined ranking hides recall.

## P-015 — regional and alternative forge features
- **Tool/run:** Parallel web_search, search_a0092e50bd00650a34b208319a6ddee9; 10 results across 4 queries.
- **Objective:** Verify alternatives and regional hosting using official docs on collaboration features/current service descriptions.
- **Exact queries:** site:help.gitee.com repository management docs; site:atomgit.com code hosting docs; site:docs.codeberg.org collaboration forge; site:docs.gitea.com compared other hosting.
- **Outcome:** Surfaced Gitee help center, Codeberg docs, Forgejo, Gitea comparison. Gitee/Gitea pages opened in F-003; Codeberg docs opened in F-005. AtomGit did not appear in retained results; current state remains open.

## P-016 — standards verification
- **Tool/run:** Parallel web_search, search_b4caa7f369f20e48c5076e3623842a68; 10 results across 4 queries.
- **Objective:** Find current primary standard editions and evidence standards.
- **Exact queries:** ISO IEC software quality framework; NIST SSDF secure development official; data ML quality standards; research software reproducibility standards.
- **Outcome:** ISO 25010:2023, 25040:2024, ISO 5259, ACM SIGSOFT, and NIST SSDF surfaced. Direct pages fetched in F-003/F-006.

## E-006 — empirical validity search
- **Tool:** Exa web_search_exa; 8 results requested/returned/screened; 0 direct page opens in search call; 8 leads retained.
- **Exact natural-language query:** Empirical evidence on whether repository badges, stars, health scores, and code metrics predict software quality, maintenance, security, or sustainability; include null findings, limitations, and metric gaming critiques
- **Outcome:** Included 2018 npm badge study, 2024 badge study, context-sensitive sustainability study, GitHub stars/importance study, tertiary code-metrics review, and 2026 preprint trust-signal review.

## X-006 — exact repository-health phrase search
- **Tool/route:** Connected X search; account route main; product Top; limit 20.
- **Exact query:** "repository health" (score OR metrics OR checklist) lang:en
- **Returned/screened:** 14/14; 0 substantive general quality-framework leads retained.
- **Outcome:** Results unrelated or tool-specific. No claim about X coverage follows.

## X-007 — named standards discussion search
- **Tool/route:** Connected X search; account route main; product Top; limit 20.
- **Exact query:** (Scorecard OR CHAOSS OR OSPS) repository standards lang:en
- **Returned/screened:** 9/9; 0 substantive repository-quality leads retained.
- **Outcome:** Results unrelated. The connected route works, but this query is low-yield.

## F-003 — primary standards, forum, and forge pages
- **Tool/extract:** Parallel web_fetch, extract_5b5efaab708f8286b822bfa98f826fdf.
- **Requested/opened:** 8 URLs; 8 extracts; no errors.
- **URLs:** NIST SSDF; ISO/IEC 25040:2024; ISO/IEC 5259-4:2024; ACM SIGSOFT Empirical Standards; Gitee repository docs; Gitea hosting comparison; Open edX repo-requirements discussion; SustainOSS template discussion.
- **Use:** Captured official page metadata/excerpts and direct discussion text. ISO full standard texts not retrieved.

## F-004 — practitioner practice and release process
- **Tool:** Exa web_fetch_exa; 4 URLs returned in combined response; connector did not expose fetch ID or error list.
- **URLs:** Geomys Standard of Care; Zalando open-source release process; Open edX forum thread; SustainOSS forum thread.
- **Use:** Read four first-party pages. Open edX thread shows tension between undocumented requirements, autonomy, tool choice, and capacity. Zalando page defers monitoring/graduation details.

## F-005 — badge, stars, metric, and Codeberg sources
- **Tool/extract:** Parallel web_fetch, extract_fabe2f66eaeaddbe7a52a15c2e4e352b; 6/6 returned; no errors.
- **URLs:** ICSE 2018 badge study PDF; NDSS 2024 GitHub-stars paper PDF; ACM tertiary code-metric review; Codeberg FAQ; Codeberg overview.
- **Use:** Read primary excerpts for sample/mechanism/scope. The badge abstract reports many badges as reasonably reliable signals in its npm sample, a counterpoint to broad claims that all badges are empty; Codeberg describes its community-driven, non-profit Forgejo-based host.

## F-006 — focused empirical and standards extraction
- **Tool/extract:** Parallel web_fetch, extract_9e9a89d6e134cc1ccce81b6aba89968b; 4/4 returned; no errors.
- **URLs:** ICSE 2018 badge study; NDSS 2024 stars; ACM tertiary code metrics; ISO/IEC 25010:2023.
- **Use:** Confirmed abstract-level methods/results and ISO product-quality scope/version.

## F-007 — full text extraction of stars study
- **Tool/extract:** Parallel web_fetch, extract_95a485e38fa8f641efdfd3660e6737db; 1/1 returned; 42,617 characters extracted; no errors.
- **URL:** NDSS 2024, The Fault in Our Stars.
- **Outcome:** Abstract reports 925,978 observations across PHP, Ruby, and JavaScript; stars/download correlations vary by language (0.47 PHP to 0.14 JavaScript); stars and downloads correlate 0.61 and 0.63 with detected deployment for JavaScript libraries. The paper is about importance/use proxies, not overall software quality.

## Tool/access status
- **Agent Reach:** agent-reach doctor --json and agent-reach check-update each returned command-not-found.
- **Parallel:** ordinary search and fetch functioned; dedicated web_research had previously returned HTTP 402 and was not retried.
- **X:** connected account route main available; the four searches in this round were noisy or weakly relevant.

# 2026-11-10 — v2 source and model discovery

The web tool returned combined results; the tool output was truncated and did not expose dependable per-query result or screening counts in the retained session. Counts are recorded as unknown, not reconstructed. Search calls took place before the 12:13 Asia/Kolkata clock check; individual call times are unavailable.

## V2-S01 — source families, archives, competency frameworks
- Tool: web search, four queries, unfiltered ranked results; individual results/screening counts unavailable.
- Exact queries: repository assessment tools open source quality maturity model QSOS OpenBRR OSS evaluation tools; software repository research data hardware scholarly archive platform zenodo software heritage osf dataverse; developer communities global programming forums China Japan Korea India Latin America open source; software engineering standards body of knowledge SWEBOK architecture usability accessibility reliability operations.
- Selected leads: Eclipse QSOS, IEEE SWEBOK, research archives and institutional repositories. Selected links were opened in V2-F01; the remaining results require screening.

## V2-S02 — metrics, research software and policy
- Tool: web search, four queries, unfiltered ranked results; individual results/screening counts unavailable.
- Exact queries: site:chaoss.community metrics model project health diversity risk; site:github.com software maturity assessment oss-review-toolkit repository quality tooling; site:fair-software.eu recommendations research software repositories; site:research-software-directory.org research software quality assessment.
- Selected leads: CHAOSS, research software guidance and software assessment tooling; further screening and primary-source audits needed.

## V2-S03 — evaluators, communities, roles and failures
- Tool: web search, four queries, unfiltered ranked results; individual results/screening counts unavailable.
- Exact queries: software repository assessment tools sustainability reproducibility software quality model engineering scorecards; site:reddit.com repository health score maintainers quality metrics; site:news.ycombinator.com software repository quality checklist maintainers; open source repository quality framework design role governance usability documentation security.
- Selected leads: RSMM, reproducibility models, UN policy, community threads and professional-role materials. Search results are discovery, not independently validated findings.

## V2-F01 — six primary URL open attempts
- Tool: web open, six requested URLs; QSOS owner page and RSMM arXiv abstract returned. IEEE SWEBOK and UN policy PDF returned HTTP 403; FAIR software URL inaccessible; Software Heritage returned HTTP 502.
- URLs: https://qsos.org/ ; https://www.computer.org/education/bodies-of-knowledge/software-engineering ; https://fair-software.eu/recommendations/ ; https://opensource.un.org/sites/default/files/2025-07/common_policy_framework.pdf ; https://arxiv.org/abs/2406.01788 ; https://www.softwareheritage.org/.
- Use: QSOS method and RSMM author abstract recorded in research/v2/first-findings.md; inaccessible sources remain leads.

## V2-F02 — user-provided estimator source
- Tool: curl, 2026-11-10, exact per-call time unavailable; URL https://api.pre.dev/api/code-licensing/estimate.mjs; 16,139 bytes downloaded to a temporary local path. SHA-256 208c9f43972ef81469cd43a37299190c1e3040e91895ed51dc9f1299b638dc23.
- Statically read selected source sections; did not execute. See research/v2/first-findings.md. File is an author-supplied executable; its vendor and backend claims remain unverified.

## Access checks
- Agent Reach doctor: command not found. The current research used web search/open and local static inspection. Native access to each listed social source has not been established in this pass.

# 2026-11-10 — specialized performance, bloat and research freshness

Individual request timestamps were not exposed; the following calls were completed before the 12:24 Asia/Kolkata clock check. Search results were returned as combined ranked output and some were truncated; returned and screened counts cannot be reliably reconstructed.

## PERF-S01 — debloating and environment-specific performance
- Tool: web search, eight queries, ranking and date filters unspecified.
- Exact queries: software bloat detection debloating dynamic loading reflection false positives empirical study 2025 2026; site:github.com cargo bloat cargo llvm lines unused dependencies machete; site:docs.python.org profiling cProfile timeit measurement python; site:github.com knip unused exports dependencies dynamic imports limitations; site:go.dev profiling pprof benchmarks allocation performance; site:llvm.org BOLT post link optimizer profile guided optimization; site:docs.nvidia.com nsight systems profiling GPU performance; site:kernel.org perf tools performance analysis documentation.
- Findings retained for follow-up include 2025 CommonJS dependency analysis, 2025 Java debloating benchmark and 2026 ground-truth debloating preprints, tool documentation, GPU profiling, and observed profiling overhead. Returned/screened/retained total: unknown.

## PERF-S02 — language and tool mechanisms
- Tool: web search, eight queries, ranking and date filters unspecified.
- Exact queries: site:github.com/RazrFalcon/cargo-bloat readme rust binary size; site:go.dev/blog pprof profiling go programs performance; site:llvm.org BOLT binary optimizer profile guided optimization; site:pyperf.readthedocs.io system tuning benchmark stability; site:github.com google benchmark user guide; site:docs.python.org timeit garbage collection benchmark; site:github.com google bloaty size profiler; site:github.com rust-lang cargo unused dependencies cargo machete.
- Owner documentation surfaced for Rust size attribution and dependency detection, Go profiling and PGO, Google Benchmark and LLVM BOLT. Search snippets are leads until opened and analyzed.

## PERF-S03 — recent research and specialist workflows
- Tool: web search, eight queries, ranking and date filters unspecified.
- Exact queries: 2026 performance engineering research debloating static dynamic benchmark ground truth program optimization; 2026 compiler auto optimization code size latency performance engineering research profile guided; site:arxiv.org 2026 software bloat energy efficiency repository code optimization; site:github.com profiling flamegraph eBPF performance analysis parca py-spy; site:github.com unimported knip vulture dead code dynamic python; site:web.dev measure core web vitals bundle size performance budgets; site:docs.kernel.org bloat-o-meter kernel size; site:perf.wiki.kernel.org perf tutorial linux kernel profiling.
- Leads include 2026 compiler optimization, autotuning and agent optimization research, web/runtime profiling and prior debloating comparisons. A date in a query is not an exhaustive date filter; verify publication and version individually.

## PERF-F01 — primary sources and access failures
- Tool: web open; 10 URLs requested. Seven returned pages: https://arxiv.org/abs/2604.17717 ; https://arxiv.org/abs/2510.20679 ; https://github.com/bnjbvr/cargo-machete ; https://github.com/webpro-nl/knip/blob/main/packages/docs/src/content/docs/reference/faq.md ; https://go.dev/doc/pgo ; https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html ; https://github.com/RazrFalcon/cargo-bloat .
- Three failed: https://www.sciencedirect.com/science/article/pii/S0164121225001773 (403); https://doi.org/10.1145/3793302.3793564 (403); https://github.com/llvm/llvm-project/tree/main/bolt (restricted URL).
- Extent read: selected official documentation sections and paper abstracts. No full implementation audit, reproduced benchmarks, tool execution, exhaustive recent-literature scan or peer-review determination for the preprints. See research/v2/specialization/performance-and-bloat.md.

# 2026-11-10 — open-ended systems and domain-specific assurance

Individual request timestamps are unavailable; calls completed before the 12:30 Asia/Kolkata clock check. Three web searches returned combined results; some output was truncated. Per-query counts and screening totals are unknown. No complete standard, test suite or implementation was audited in this pass.

## SYS-S01 — systems engineering and lifecycle sources
- Tool: web search; four queries; no date or language filters specified.
- Exact queries: site:sebokwiki.org systems engineering life cycle stakeholder requirements architecture verification validation; site:computer.org swebok software engineering body of knowledge architecture construction operations; site:nist.gov systems security engineering life cycle systems engineering 800-160; site:nasa.gov systems engineering handbook technical processes.
- Selected sources surfaced: NASA Systems Engineering Handbook and NIST systems security engineering. These are primary publication pages/PDF excerpts from search results, not a full document audit.

## SYS-S02 — browser, operating system, compiler and media assurance
- Tool: web search; four queries; no date or language filters specified.
- Exact queries: site:w3.org Web Platform Tests interoperability browser engines testing; site:source.android.com compatibility test suite operating system vendors; site:llvm.org docs testing guide compiler correctness llvm test suite; site:ffmpeg.org fate tests multimedia codecs testing.
- Selected sources surfaced: W3C testing policy, Android CTS and MLIR testing guide. The FFmpeg FATE query needs a separate targeted search and primary read; no FATE result is treated as verified in this pass.

## SYS-S03 — geospatial, trading, security and aviation sources
- Tool: web search; four queries; no date or language filters specified.
- Exact queries: site:ogc.org standards geospatial data APIs maps; site:fixtrading.org standards FIX trading protocol; site:owasp.org application security verification standard ASVS; site:faa.gov RTCA DO-178C airborne software assurance.
- Selected sources surfaced: FIX Protocol, OWASP ASVS and FAA AC 20-115D. Their scopes differ; the FAA page calls the AC an acceptable means and says it is not itself a regulation. The OGC query needs separate primary-source screening.


# 2026-11-10 — research-methods validation and subtle failure-pattern evidence

**Time window:** approximately 13:30–13:37 Asia/Kolkata (2026-11-10); exact per-call timestamps were not exposed by the connectors. Do not infer more precise timestamps. Parallel ranked searches returned 10-result windows per call; result-window counts are not unique-source totals or venue coverage.

## METH-S01 — evidence mapping and secondary-study methods

- **Tool/run:** Parallel `web_search`; `search_8fc87ddff0430ef854837cdb140f4ee4`.
- **Exact queries:** `software engineering evidence map methods`; `grey literature appraisal software reviews`; `PRISMA S reporting systematic searches`.
- **Filters:** no language, date, or venue filter; ranked search window.
- **Returned:** 10 results. **Screened:** titles/excerpts were inspected selectively; a complete count is not claimed because the tool output is ranked and excerpt-oriented.
- **Outcome:** surfaced SEGRESS, systematic evidence-map method papers, grey-literature review work and the software-engineering multivocal-review guidelines. Followed with direct fetches recorded at METH-F01.

## METH-S02 — sequential and model-based testing methods

- **Tool/run:** Parallel `web_search`; `search_ba0866131259df2d91d3fb02eabf1897`.
- **Exact queries:** `property based stateful testing bugs`; `model based testing event sequences`; `modal Escape regression test issue`.
- **Filters:** no language, date, or venue filter; ranked search window.
- **Returned:** 10 results. **Screened:** partial title/excerpt review; no exhaustive screening total claimed.
- **Outcome:** found Hypothesis stateful-testing documentation and primary work on stateful greybox fuzzing and model-based API tests. Hypothesis and USENIX source pages are linked in `research/v2/failure-patterns/initial-evidence-batch.md`.

## FAIL-S01 — retries, cancellation, race and stale-result issue discovery

- **Tool/run:** Parallel `web_search`; `search_8815d9b0e1d8834854ddbe59dd62305e`.
- **Exact queries:** `idempotency retry duplicate side effects issue`; `cancellation race regression test GitHub`; `stale async response race issue fix`.
- **Filters:** no language/date filter; ranked search window.
- **Returned:** 10 results. **Screened:** candidate titles and excerpts were reviewed selectively; selected issue/PR chains were followed up in FAIL-F02. No source-population count is claimed.
- **Outcome:** surfaced detailed issue reports and merged fixes. Retained confirmed cases include go-redis PR #4143 and .NET runtime issue/PR #131249/#132241; open/unverified cases remain separately marked.

## FAIL-S02 — clone detection and duplication counterevidence

- **Tool/run:** Parallel `web_search`; `search_4491a6de1211cdd4ac1ea77c60e24c69`.
- **Exact queries:** `code clone detector false positives evaluation`; `semantic clone detection precision recall`; `intentional duplication abstraction tradeoff study`.
- **Filters:** no language/date filter; ranked search window.
- **Returned:** 10 results. **Screened:** title/excerpt review of candidate studies; count of unique eligible studies not established.
- **Outcome:** identified empirical work on clone detector precision/recall, clone removals and intentional clone motivations. Primary links and inference limits appear in `research/v2/failure-patterns/initial-evidence-batch.md`.

## FAIL-S03 — indexed forum and Q&A discovery

- **Tool/run:** Parallel `web_search`; `search_5914b5827c0feecb0ada6d01f31e7af9`.
- **Exact queries:** `site:reddit.com software bug different input paths tests`; `site:stackoverflow.com modal keyboard click different behavior`; `site:news.ycombinator.com duplicate logic abstraction bug`.
- **Filters:** the site restrictions shown in the exact queries; English was not separately constrained; ranked search window.
- **Returned:** 10 results. **Screened:** visible titles/excerpts were reviewed; only selected direct threads are retained. Search-engine indexing is not native Reddit, Stack Overflow or Hacker News coverage.
- **Outcome:** surfaced a Stack Overflow modal event/focus report and HN practitioner disagreement on duplication vs wrong abstraction. The HN material is counterargument/lead evidence, not an empirical estimate.

## X-008 — action paths and duplicated logic discussion

- **Tool/route:** Connected X search, account route `main`, product `Latest`, limit 20; `lang:en` query operator.
- **Exact query:** `("same action" OR "different code path" OR "duplicate logic") (bug OR regression OR tests) lang:en`.
- **Returned:** 20 tweets. **Screened:** first 12 returned items were inspected; 2 firsthand/social leads retained: [same action on two input paths behaves differently](https://x.com/ceroribi/status/2119645692746756228) and [review patches duplicate logic already owned elsewhere](https://x.com/Sergey_Rura/status/2119943998597181441). Both are anecdotes/opinions and remain uncorroborated.
- **Access limits:** connected X search only; not a representative sample or a full X archive. No posts, replies, likes, or messages were made.

## METH-F01 — primary methods sources

- **Tool/extract:** Parallel `web_fetch`; `extract_94bd305db2a3a8919f1c8257875eb8af`.
- **Requested/opened:** 5 URLs; 5 extracts; no extraction errors. Relevant excerpts reviewed, not a line-by-line full-text audit.
- **URLs:** Wohlin snowballing guidelines; Garousi/Felderer/Mäntylä multivocal-review guidelines; Kitchenham/Charters SLR report v2.3; Miake-Lye et al. evidence-map review; SEGRESS reporting guidelines.
- **Outcome:** informed the distinction between a broad map and question-focused synthesis; complementary citation chaining; source-specific grey-literature appraisal; and reporting guidance vs methodological validity. Method note: `research/v2/methods/evidence-research-methods.md`.

## FAIL-F02 — project issue/fix and community-source verification

- **Tool/extract:** Parallel `web_fetch`; `extract_87ade39049c8a3aad79110b59fd8fdb0`.
- **Requested/opened:** 10 URLs; 10 extracts; no extraction errors. Relevant excerpts were inspected; no repository tests were run locally.
- **URLs:** react-native-web issue #1817 and linked commit `6138fccc`; go-redis PR #4143; .NET runtime issue #131249 and PR #132241; Composio issue #3654; Stack Overflow question 72670917; react-native-paper issue #4140; Reanimated issue #4422; Chainlit issue #2598.
- **Status discipline:** confirmed project-specific fix histories are distinguished from open issue reports and community claims. Search/fetch evidence does not establish global prevalence or independent reproduction. See evidence cards in `research/v2/failure-patterns/initial-evidence-batch.md`.

## Platform and method coverage limits

- Agent Reach remains unavailable (`agent-reach doctor --json`: command not found, recorded earlier); X was accessed through its connected search route.
- Reddit, Stack Exchange-wide search, native HN/Lobsters, regional-language sources, mailing lists and other platforms were not natively queried in this batch. Indexed `site:` results are low-recall discovery only.
- This batch opens selected source pages and records a first set of mechanisms; no matrix cell is marked saturated. Counts of search results do not show how much of a platform, community or literature exists.


## SYS-S04 — compiler correctness and differential/targeted testing

- **Tool/run:** Parallel `web_search`; `search_8d2cad135be8e3105e9d5b66eef101ab`.
- **Exact queries:** `compiler miscompilation optimization regression test`; `LLVM wrong code optimization issue reproducer`; `compiler differential testing paper`.
- **Filters:** no date or venue filter; ranked result window.
- **Returned:** 10. **Screened:** result titles/excerpts reviewed selectively; only the PLDI 2025 primary paper was opened in follow-up F-03.
- **Outcome:** surfaced research on differential compiler testing and optimization-directed fuzzing. The paper reports a specific prior optimizer defect missed by then-existing tests and tool results on known miscompilations. Scope and numerical limits are recorded in the failure-pattern note.

## FAIL-S04 — payment, webhook and duplicate-effect reports

- **Tool/run:** Parallel `web_search`; `search_b56ea944921d38cee355ce1f127596e1`.
- **Exact queries:** `payment duplicate charge retry issue`; `webhook delivery duplicate event GitHub`; `idempotency key regression test fix`.
- **Filters:** no date/language filter; ranked result window.
- **Returned:** 10. **Screened:** candidate titles/excerpts reviewed selectively; nine original project/paper URLs were fetched in FAIL-F03 and seven were revisited for status in FAIL-F04.
- **Outcome:** surfaced an Odoo Adyen idempotency-key fix whose issue description says the duplicate-charge scenario was not reproduced in its test environment; PRAHO's sender-retry/failed-status edge case; and reports about database index and webhook-event identity. Self-reported or unverified mechanisms remain labeled as such.

## FAIL-S05 — stale asynchronous response and write ordering

- **Tool/run:** Parallel `web_search`; `search_760b151a7028d70035c014df5b633f33`.
- **Exact queries:** `stale async response race issue fix`; `out of order request UI regression GitHub`; `cancel request stale state bug`.
- **Filters:** no date/language filter; ranked result window.
- **Returned:** 10. **Screened:** selective title/excerpt review; VueUse and Magento project records fetched in FAIL-F03/FAIL-F04. A search result hosted on a mirror was replaced with the original repository URL before use.
- **Outcome:** VueUse issue #5571 and merged PR #5574 directly document a slow older success response overwriting newer state after the error branch had already been guarded. Magento issue #40529 contains mixed reproduction status across verification attempts; treat it as conflicting/environment-bounded evidence until its fix history is inspected.

## TEST-S01 — test-fixture determinism and scheduler-sensitive regressions

- **Tool/run:** Parallel `web_search`; `search_8fc9592c86f13977743883867bb61d93`.
- **Exact queries:** `deterministic concurrency regression test GitHub`; `race detector stress test flaky regression issue`; `fault injection production bug test fix`.
- **Filters:** no date/language filter; ranked result window.
- **Returned:** 10. **Screened:** selective result-title/excerpt review; one merged project fix was opened in TEST-F01.
- **Outcome:** llxprt-code PR #3100 traces a flaky transport canary to a test fixture that assumed event-loop ordering across separate processes. The merged test waits for downstream observation before injecting the reset. Other results included deterministic scheduling tools and reports; they are not yet audited.

## X-009 — fresh search for retry/race reports

- **Tool/route:** Connected X search; account route `main`, product `Latest`, limit 20.
- **Exact query:** `(retry OR race OR stale response OR duplicate event) (bug OR regression) (test OR reproduction) lang:en`.
- **Returned:** 20 tweets; eight items were inspected. **Retained:** 0 as evidence because the visible results were mostly unsupported model/tool claims, hype or irrelevant material. They are not repeated as facts.
- **Limit:** low-yield English Latest result window only; not evidence of no X discussion.

## FAIL-F03 — original project records and compiler paper

- **Tool/extract:** Parallel `web_fetch`; `extract_36369327788124a5fe143f473cc88c55`.
- **Requested/opened:** 9 URLs; 9 extracts; no extraction errors. Relevant excerpts reviewed, not complete file/history audits.
- **URLs:** PRAHO issue #234; Vexa issue #519; Open Mercato issue #7155; Magento issue #40529; VueUse issue #5571; Heo et al. Optimuzz PLDI 2025 paper; loom issue #4547; llxprt-code PR #3100; Odoo PR #153792.
- **Outcome:** used only selected original project records and the primary PLDI paper. The loom issue, Vexa issue and other detailed leads remain unverified; a page being accessible does not establish its author or claims are correct.

## FAIL-F04 — fix status and regression-test follow-up

- **Tool/extract:** Parallel `web_fetch`; `extract_f3481827b1aab74982b020eb4191e1b3`.
- **Requested/opened:** 7 URLs; 7 extracts; no extraction errors. Relevant issue/PR excerpts reviewed.
- **URLs:** VueUse issue #5571 and PR #5574; Magento issue #40529; PRAHO issue #234; Open Mercato issue #7155; Odoo PR #153792; llxprt-code PR #3100.
- **Outcome:** confirmed VueUse and llxprt-code PRs as merged and captured their fixes; Odoo PR describes adding an idempotency key but explicitly notes the original incident was not reproducible with the available provider test account. Magento has conflicting repro statements. PRAHO and Open Mercato issue closure was not enough to establish the exact linked fix; those remain attributed reports.

**Time window for SYS-S04 through FAIL-F04:** approximately 13:38–13:48 Asia/Kolkata on 2026-11-10; exact per-call timestamps were not exposed. All result totals are connector windows, not unique-source coverage.


## REDDIT-001 — direct Brave searches and original community threads

- **Tool/route:** user-authorized Brave browser, direct Reddit search pages, read-only; 2026-11-10, approximately 13:48–13:54 Asia/Kolkata. Exact per-navigation timestamps unavailable.
- **Exact query 1:** `modal Escape click animation bug`.
- **Exact query 2:** `retry duplicate payment webhook idempotency`.
- **Filters/window:** Reddit search links used `type=link`; defaults otherwise. Each visible result page showed seven posts; no total result count was exposed. For query 2, Reddit initially autocorrected `idempotency` to `identity`; the UI exposed a link for the exact spelling, which was followed. Search showed relevance/all-time controls; no date bound was selected.
- **Opened originals:** [r/webdev modal/CSS animation report](https://www.reddit.com/r/webdev/comments/uup45b/anyone_know_why_my_modal_is_causing_my_css/); [r/brdev idempotency/payment-webhook question](https://www.reddit.com/r/brdev/comments/1wt7s58/como_voc%C3%AAs_garantem_idempot%C3%AAncia_em_webhooks_de/).
- **Screening:** two original posts opened. The r/webdev post is a first-person symptom, approximately five years old per Reddit display, with a CSS fragment and no comments on the inspected page; no cause/fix confirmed. The r/brdev post is a Portuguese-language design question, approximately one month old per display; Reddit showed 11 votes and 20 comments at retrieval. The post asks about duplicate D+3 payouts when a webhook or cron may run twice. A loaded subset of comments was read; ideas include durable unique-key/status records, outbox/advisory locks, and handling out-of-order events. They remain community suggestions, not verified engineering conclusions.
- **Search feature caveat:** Reddit displayed an AI-generated answer panel with synthesized advice and links to posts/comments. It was not treated as a primary source; the linked original post and visible comments were inspected. Search ranking, spell correction and that answer feature can shape the result set.
- **Outcome:** adds first-hand symptoms and practitioner vocabulary, including a Portuguese venue sample, while preserving that the modal thread is unresolved and the payment thread is a question rather than an incident. This is two threads, not broad Reddit coverage.

## STRIPE-F01 — first-party webhook and idempotency documentation

- **Tool/extract:** Parallel `web_fetch`; `extract_5e7265a7076613657bea3c58a1437d3d`.
- **Requested:** 3 URL fragments; **returned:** 2 canonical page extracts; no extraction errors. The two webhook fragments resolve to the same documentation page.
- **URLs:** [Stripe webhook event delivery/duplicate handling](https://docs.stripe.com/webhooks#handle-duplicate-events), [Stripe webhook event ordering](https://docs.stripe.com/webhooks#event-ordering) (same canonical page), and [Stripe API idempotent requests](https://docs.stripe.com/api/idempotent_requests).
- **Relevant sections reviewed:** delivery retries, event ordering, duplicate-event guidance, API v1 vs v2 idempotency, saved-result boundary, parameter matching and key pruning.
- **Outcome:** supports only Stripe-specific documented behavior. In particular, webhook duplicates and out-of-order delivery are expected; API v1 idempotency has explicit execution, parameter and expiry semantics. It does not establish that every provider shares those contracts or that a Reddit user's proposed design works.

# Retrospective extraction provenance recovered after context compression

**Date:** 2026-11-10, Asia/Kolkata. These are direct page-extraction records reconstructed from retained tool IDs and the current project notes; exact per-call times and the original search queries that produced some URLs were not preserved. Do not manufacture them. Excerpts were reviewed selectively, not every full paper or issue history.

## RETRO-AI-F01 — earlier agent-PR empirical studies

- **Tool/run:** Parallel `web_fetch`; `extract_97be7e68b88f283a6692436e9f02bec6`.
- **Operation:** direct fetch of four research pages; 4 requested, 4 extracted, no reported extraction error.
- **Recovered URLs:** [MSR study DOI 10.1145/3793302.3793622](https://dl.acm.org/doi/full/10.1145/3793302.3793622); [arXiv 2601.20109 HTML](https://arxiv.org/html/2601.20109v1); [arXiv 2603.13724 HTML](https://arxiv.org/html/2603.13724); [arXiv 2601.15195](https://arxiv.org/abs/2601.15195).
- **Outcome:** excerpts contributed AI-generated PR quality/redundancy leads. Original exact search strings and per-URL screening decisions are not retained; later direct work is separately logged as `AI-S01`/`AI-F01`.

## RETRO-METHOD-F02 — test, dialog and animation references

- **Tool/run:** Parallel `web_fetch`; `extract_183ca6f0419310147694defa620a3607`.
- **Operation:** 5 requested URLs, 5 returned extracts, no reported extraction error. Exact timestamp and original query list not preserved.
- **Recovered source set:** Stryker Mutator docs; MDN HTML dialog reference; Hypothesis stateful testing guide; a Chrome CSS animation guide; and the W3C ARIA Authoring Practices Guide modal-dialog pattern. The tool URL list is incomplete in the retained trace, so only the titles/hosts should be cited as recovered provenance for this run. Canonical links used in later notes are direct source links.
- **Outcome:** selected excerpts support candidate mutation-testing, stateful-sequence and dialog interaction questions. They are not evidence that a given repository is adequately tested.

## RETRO-AI-F02 — additional agent/build quality and performance studies

- **Tool/run:** Parallel `web_fetch`; `extract_24514be6318fc1bb2c09da6c68e97d3c`.
- **Operation:** 5 requested URLs, 5 returned extracts, no reported extraction error. Exact timestamp and original search strings not preserved.
- **Recovered URLs:** [arXiv 2603.13724](https://arxiv.org/abs/2603.13724); [arXiv 2601.16839 HTML](https://arxiv.org/html/2601.16839v1); [arXiv 2603.28592 v3](https://arxiv.org/html/2603.28592v3); [Software Quality Journal article](https://www.sciencedirect.com/science/article/pii/S0950584925002745); [arXiv 2605.06464 v2](https://arxiv.org/html/2605.06464v2).
- **Outcome:** retained only as prior discovery/extraction provenance. The current evidence card links studies only where their scope and limitations were rechecked in the current `AI-F01` extraction.

# 2026-11-10 — cross-system failure, artifact and workload research

**Time window:** approximately 14:00–14:10 Asia/Kolkata; exact per-call timestamps were not exposed. Search result windows are ranked discovery samples, not population coverage. All reads were read-only.

## SYS-S05 — persistent transaction and index state

- **Tool/run:** Parallel `web_search`; `search_f2b69fcadc9533b0f897ab4ed97bb9f8`.
- **Exact queries:** `site:github.com issue transaction index corruption regression test merged`; `site:github.com issue stale sequence cursor transaction fix`; `site:github.com SQL update race lost update regression`.
- **Filters:** no date/language filter; ranked results.
- **Returned:** 10 results. **Screened:** first six displayed result summaries.
- **Outcome:** selected ArcadeDB issue #4935/PR #4964 for direct verification. Other leads included SQL `UPDATE`/`SELECT` atomicity, stale event-sequence recovery, a SurrealDB index-build/write window and SQLite index/persistence reports; those are not all verified or retained as confirmed cases.

## SYS-S06 — embedded storage, reset and recovery paths

- **Tool/run:** Parallel `web_search`; `search_3d3b2d310b9bf006b67391157fa1e937`.
- **Exact queries:** `site:github.com firmware issue watchdog reset persistent state fix`; `site:github.com embedded power loss filesystem corruption fix`; `RTOS scheduler race bug regression test firmware`.
- **Filters:** no date/language filter; ranked results.
- **Returned:** 10. **Screened:** first six displayed result summaries.
- **Outcome:** selected Meshtastic #10851/#10873 for linked fix and hardware-repro evidence, plus OpenWrt mt76 #1148 as an explicitly unresolved, source-pinned lead. Other flash/power-loss reports remain candidate leads.

## SYS-S07 — release artifacts and generated/deployed consistency

- **Tool/run:** Parallel `web_search`; `search_39b7530ad94be8270b3ff65495e5be54`.
- **Exact queries:** `site:github.com reproducible build regression issue fix`; `supply chain dependency update regression incident primary`; `deployment config drift outage postmortem primary source`.
- **Filters:** no date/language filter; ranked results.
- **Returned:** 10. **Screened:** first six displayed result summaries.
- **Outcome:** selected Pydantic AI #7397/#7414 for release artifact validation and Microsoft APM #1716/#1714 for deployed-copy drift. Other CI/config/dependency drift leads were not validated.

## PERF-S04 — runtime regression, bloat and workload measurement

- **Tool/run:** Parallel `web_search`; `search_df823bda0934a1280ad0f75458d5a075`.
- **Exact queries:** `site:github.com memory regression issue profiling fix`; `code bloat dead code removal regression empirical study`; `benchmark optimization regression workload profiling paper`.
- **Filters:** no date/language filter; ranked results.
- **Returned:** 10. **Screened:** first six displayed result summaries.
- **Outcome:** selected Erlang/OTP issue #8322 and PR #8347 to inspect a downstream-workload performance regression; the other returned studies became primary-source candidates for the separate debloating/AI evidence note.

## AI-S01 — recent empirical research on agent changes, test oracles and bloat

- **Tool/route:** Exa `web_search_exa`; three independent requests, each asked for up to 8 results. The combined connector output was truncated and did not preserve a reliable per-request result total or search IDs. Do not treat the requested limit as a returned or screened count.
- **Exact queries and objectives:**
  1. Query: `Empirical studies evaluating AI-authored code quality in real pull requests, with sampling and measurement limitations`. Objective: find recent peer-reviewed primary studies and preprints (2024–2026) comparing AI-generated and human-authored code in real repositories; prioritize methods, dataset selection, outcomes, replication artifacts and validity threats; exclude opinion pieces.
  2. Query: `Research on whether generated tests catch real semantic regressions and subtle path inconsistencies`. Objective: find primary research/evaluation datasets about oracle weakness, missed bugs, stateful/multi-path behavior and testing coding-agent patches; prioritize measured false negatives, scope and artifacts.
  3. Query: `Current research on source-code bloat, dependency bloat and workload-based performance validation`. Objective: find 2024–2026 primary studies about software bloat/debloating, dependency removal, energy/performance and correctness/maintainability tradeoffs; prioritize ground truth and limits.
- **Screening:** the returned Exa text was too large for reliable full result enumeration. Selected primary-paper leads were fetched directly in `AI-F01`; search-result snippets alone are not used as final evidence.
- **Outcome:** direct extraction confirms recent papers on post-merge agent PR outcomes, agent-authored build files, debloating soundness and workload-specific runtime caches. See `research/v2/agent-quality/empirical-evidence-batch.md`.

## SYS-F05 — direct project and release source excerpts

- **Tool/run:** Parallel `web_fetch`; `extract_9c3a348e4551278ca10f5b7dda4a7af8`.
- **Requested/opened:** 9 URLs, 9 extracts, no extraction errors. Selected issue/PR excerpts reviewed, not complete repository histories.
- **URLs:** ArcadeDB issue #4935 and PR #4964; Meshtastic issue #10851 and PR #10873; Microsoft APM issue #1716; Pydantic AI issue #7397 and PR #7414; Erlang/OTP issue #8322; OpenWrt mt76 issue #1148.
- **Outcome:** surfaced issue reports and linked fix descriptions for the confirmed cards; PR/issue status and relevant test/workload details were cross-checked via the GitHub connector in `GH-F01`.

## GH-F01 — read-only GitHub issue and pull-request verification

- **Tool/route:** connected GitHub read endpoints. Eleven fetch calls were made, including repeat compact reads of three PRs; eight unique records were inspected.
- **Unique records:** ArcadeDB PR #4964; Meshtastic PR #10873; Pydantic AI PR #7414; Erlang/OTP PR #8347; Microsoft APM issue #1716 and PR #1714; Erlang/OTP issue #8322; OpenWrt mt76 issue #1148.
- **Screening:** issue bodies, PR descriptions, selected diffs and available comments were reviewed. No issue/PR edits, comments or reactions were made.
- **Outcome:** confirmed the ArcadeDB and Pydantic PR status and test/gate descriptions; the Meshtastic report revises the issue's proposed root cause and documents a hardware before/after check; the APM PR re-synced deployed files but does not establish that the requested durable drift test landed; Erlang's merged PR explicitly reports improvement without complete performance restoration; OpenWrt remains an open, unconfirmed reporter diagnosis.

## AI-F01 — primary agent-quality and debloating papers

- **Tool/run:** Parallel `web_fetch`; `extract_2716726f291e42f295840ebdb7ffc95b`.
- **Requested/opened:** 6 URLs, 6 extracts, no extraction errors. Method, result and validity excerpts were reviewed, not every full paper line by line.
- **URLs:** arXiv HTML `2609.17598`, `2601.20109v1`, `2601.16839`, `2312.13274v2`, `2607.02618`; ACM DOI `10.1145/3660821`.
- **Outcome:** added a scoped paper appraisal to `research/v2/agent-quality/empirical-evidence-batch.md` and follow-up evidence to `research/v2/specialization/performance-and-bloat.md`. Preprint/review status and replication-package execution remain open for several papers; static metrics and selected workloads are not overall quality or proof of equivalence.

## Coverage and method observations

This pass added cross-artifact consistency, transaction history, release validation, hardware reset sequencing and downstream workload performance to the failure map. It did not survey every code forge, social network, forum, language or hardware/software domain. Native platform coverage was not broadened here; Reddit and X evidence remains the small prior sample, while Stack Overflow/Hacker News were reached via indexed discovery with only selected thread follow-up. Agent Reach remains unavailable in this environment. No cell is saturated and no universal quality score/gate is proposed.

# 2026-11-10 — direct venue API discovery on Hacker News and Stack Overflow

**Time window:** approximately 14:20–14:35 Asia/Kolkata; exact request times were not exposed. These are read-only public API calls. The HN search route is Algolia's HN content index, not the HN site UI; original stories/comments were opened through Hacker News' Firebase item API. Stack Overflow search and thread content used the public Stack Exchange API. No account key was used.

## HN-NATIVE-001 — search-query families and result windows

- **Hacker News Algolia API**, first tested the relevance endpoint with exact queries and filters:
  - `modal escape click animation`, `tags=story`: 0 results.
  - `duplicate code paths tests regression`, `tags=story`: 0 results.
  - `modal`, `tags=comment`: 712,358 indexed hits; first 10 returned, first 5 snippets screened; noisy (music/editor/modal usage).
  - `animation`, `tags=comment`: 63,577 indexed hits; first 10 returned, first 5 screened; mostly unrelated or low-specificity.
  - `duplicate code`, `tags=comment`: 6,360 indexed hits; first 10 returned, first 5 screened; included general debate about duplication and abstraction, not a systematic defect sample.
  - `idempotency`, `tags=comment`: 5,275 indexed hits; first 10 returned, first 5 screened; broad and mixed.
  - `code quality`, `tags=story`: 2,648 indexed hits; first 10 returned, first 5 screened; included AI/code-quality stories.
- **Follow-up HN Algolia `search_by_date` exact queries** (each with `hitsPerPage=10`; first six results inspected):
  - `AI generated code quality`, `tags=story`: 240 indexed matches; 10 returned; relevant candidate threads included IDs 49934037 and 50139584.
  - `code review duplication`, `tags=comment`: 185 matches; 10 returned; first six included current AI/coding discussions, not a clean sample of duplication defects.
  - `modal animation`, `tags=comment`: 2,286 matches; 10 returned; first six were largely unrelated; no direct modal bug retained from this window.
  - `idempotency webhook`, `tags=comment`: 67 matches; 10 returned; the first window included comment 50414339 on thread 50412646, which describes concerns about concurrent SQLite/D1 read-then-write behavior in AI-generated app code.
  - `test suite regression`, `tags=comment`: 863 matches; 10 returned; first six included current testing-agent and product discussion.
- **Limits:** Algolia hit totals describe the index and query semantics, not unique defects or platform coverage. Broad terms create substantial noise; results vary by tags, ranking/sort and terms. The two exact targeted story queries returned zero, while broader/date-ranked comment searches surfaced relevant threads; the exact zero is local to those queries and filters only.

## HN-THREAD-001 — original stories and sampled discussion

- **Tool/route:** public Hacker News Firebase item API, `https://hacker-news.firebaseio.com/v0/item/{id}.json`.
- **Opened stories:** [Ask HN: Is anybody producing good code with coding agents?](https://news.ycombinator.com/item?id=49934037), [Ask HN: Why people keep posting AI-generated projects around the Internet?](https://news.ycombinator.com/item?id=50139584), [Launch HN: Momentic – Agents that catch bugs by using your app](https://news.ycombinator.com/item?id=50339913), and [Show HN: No more code reviews. Fuzz instead](https://news.ycombinator.com/item?id=50412646).
- **Thread metadata at retrieval:** descendant counts were 48, 16, 134 and 1 respectively. **Sampled:** 5, 6, 5 and 1 top-level comments respectively, plus nested reply 50422230 (18 comments total sampled). Not all comments/replies were read.
- **Outcome:** the first thread contains opposing anecdotes about review burden, change size, specs, architecture and end-to-end/integration verification. The AI-project-sharing thread includes both concerns about expertise/review quality and arguments for experimentation and sharing. The Momentic thread raises the difference between executing flows and finding unique verified bugs, plus deduplication, reproducibility, evidence and triage cost. The fuzzing-first thread has one comment listing race-prone read-then-write SQL and unbounded subrequests as checks a tool should target.
- **Evidence class:** practitioner discussion and, for Momentic, product-pitch/commentary. These are leads and evaluation questions, not measured defect rates or verified detector performance.

## SO-NATIVE-001 — Stack Overflow API search

- **Tool/route:** public Stack Exchange API v2.3 `search/advanced`, `site=stackoverflow`, `sort=relevance`, `order=desc`, `pagesize=10`; no date or language filter.
- **Exact queries:** `modal escape click animation`; `duplicate webhook retry idempotency payment`.
- **Results:** first query returned 10 items with `has_more=true`; second returned 1 with `has_more=false`. The API reported remaining quotas 299 and 298 after the respective calls. These are query windows, not Stack Overflow coverage counts.
- **Follow-up selection:** opened modal question #79787635 and webhook question #79998813 through the Stack Exchange API, recorded in `SO-THREAD-001`.

## SO-THREAD-001 — original questions, answers and comment status

- **Modal question:** [#79787635](https://stackoverflow.com/questions/79787635/why-does-this-dialog-modals-css-slide-out-animation-jump-to-the-top-of-the-page), created 2025-10-10 UTC; score 1 and two answers at retrieval. The report says Escape uses native dialog closure while a separate backdrop click handler calls `dialog.close()` and causes the exit animation to jump. Chrome and Edge 141 were reported; Firefox was uncertain. The accepted answer suggests waiting for `animationend`; no question comments or author-confirmed follow-up were present in the inspected API response.
- **Webhook question:** [#79998813](https://stackoverflow.com/questions/79998813/how-can-i-prevent-duplicate-webhook-events-from-being-processed-in-laravel), created 2026-08-27 UTC; score 0, two answers, no accepted answer. It asks about concurrent duplicate delivery. Answers suggest event-ID storage/unique constraints; the sampled snippets do not establish the full atomic claim, external-effect and failure-recovery semantics. One comment clarifies idempotent final state versus processing each event only once.
- **Screening total:** two question bodies, four answers, one comment inspected. No answer was independently tested, and no corresponding source-code patch was opened.

## Coverage boundary

These APIs improve direct access to HN and Stack Overflow content, but do not replace native UI/session routes or exhaust either platform. Reddit/X samples remain separate; indexed queries, Algolia HN search, Stack Exchange API search, original project trackers, and papers must remain distinct routes and evidence classes. No saturation decision was made.


## 2026-11-10 — evaluator mechanism audit, batch RAT

**Local time:** approximately 14:33–14:37 Asia/Kolkata; exact per-call times unavailable. All actions were read-only.

**Purpose:** inspect first-party mechanisms, not merely enumerate names: observable inputs, rule/score computation, missing/unknown and N/A behavior, profile/applicability, freshness/versioning, governance and known validation boundaries. Search windows were bounded; they do not establish field saturation.

### Parallel search runs

- **RAT-S01** — 3 calls, each returned 10 ranked result summaries (30 displayed in total; overlap not deduplicated). Queries:
  1. `site:github.com/ossf/scorecard scorecard checks score unknown`
  2. `site:github.com/ossf/scorecard docs checks permissions token`
  3. `site:github.com/ossf/scorecard scorecard score 10 scoring`
  4. `site:bestpractices.dev criteria scoring badges unknown not applicable`
  5. `site:github.com/coreinfrastructure/best-practices-badge API criteria validation`
  6. `site:bestpractices.dev criteria list tests`
  7. `CLOMonitor checks configuration unknown score repository official`
  8. `OpenSSF Criticality Score formula repository official`
  9. `inspect.software repository quality mechanism official documentation`
  Search IDs: `search_6a183c2a07db5401cfab029e784e0ac5`, `search_9f3e4972b2c291d726ccb6666a4eae0e`, `search_b7a6fba4ccc254178eb1100c4b039d29`. Retained owner docs and public code sources; no unique-result denominator inferred.
- **RAT-S02** — 3 calls, 10 ranked summaries each. Queries:
  1. `site:inspect.software/methodology health index score missing data weights`
  2. `site:github.com inspect.software health index source scanner`
  3. `inspect.software repository health methodology limitations validation`
  4. `site:github.com/arun-gupta/repo-pulse score weighting code`
  5. `RepoPulse README 2400 repositories calibration source code`
  6. `repository health score GitHub baseline dataset methodology`
  7. `site:compass.gitee.com/docs metrics model software artifact community robustness`
  8. `site:github.com Gitee OSS Compass metric model methodology`
  9. `Gitee OSS Compass software selection evaluation three dimensional mechanism`
  Search IDs: `search_3fc0a2cba26c231a5de2b8f992c30366`, `search_0b001888462df2373a4a535526798c1b`, `search_a9eb03750b055fb60807a6deaac2a0e1`. Screened owner methodology, project docs and metric-model result summaries; no claim of full result-window screening.
- **RAT-S03** — 3 calls, 10 ranked summaries each. Queries:
  1. `site:github.com/cncf/clomonitor status unknown check score result not applicable`
  2. `site:github.com/cncf/clomonitor "not applicable" check`
  3. `site:clomonitor.io/docs checks result status check set code-lite community docs`
  4. `site:github.com/ossf/criticality_score "2026-08-29" data unavailable scoring config`
  5. `site:github.com/ossf/criticality_score popularity_correlation limitations project types`
  6. `OpenSSF Criticality Score formula weights signals limitations github only`
  7. `site:arun-gupta.github.io/repo-pulse/docs/scoring-and-calibration cohort selection calibration generated config BigQuery`
  8. `site:github.com/arun-gupta/repo-pulse calibration methodology tests score missing data`
  9. `RepoPulse solo project scoring profile missing data algorithm source`
  Search IDs: `search_bb0e8cd31b3fb1f13327f35647545bb5`, `search_98186c171bd47dc0cabbf4213d19bc80`, `search_8b151ce699f69ff2a0d6f9d9026495fe`. This round surfaced primary implementation and pipeline-shutdown evidence.

### Fetches and source inspection

- **RAT-F01:** Parallel web_fetch, 13 URLs requested, 13 extracts returned, no extraction errors. Extracts included Scorecard README/check docs/architecture/policy/annotations; Best Practices criteria/discussion/criteria YAML; CLOMonitor check docs; Criticality README; Linux Foundation criticality methodology.
  Extract ID: `extract_11b856276158b8b879b34faa4f2e8f21`.
- **RAT-F02:** Parallel web_fetch, 13 URLs requested, 13 extracts returned, no extraction errors. Included inspect.software methodology, health index, bands, version history, FAQ and scanner repo; RepoPulse scoring/calibration docs, product definition, calibration issue and signal inventory; OSS Compass scorecard/activity/service docs.
  Extract ID: `extract_3a9f7d6ab768e2a3daa40357364e72b1`.
- **RAT-F03:** Parallel web_fetch, 13 URLs requested, 11 extracts returned; two guessed CLOMonitor source paths returned 404 (`clomonitor-core/src/score.rs`, `clomonitor-core/src/linter.rs`). The actual module paths were then discovered by owner-repo API and fetched below. Extracts included CLOMonitor docs, Scorecard check/annotation guidance, Badge vetting, RepoPulse calibration docs/artifact and Criticality issue #833/issue #8/README.
  Extract ID: `extract_f88a26e173a6b1d549fd4571113b1a9d`.
- **GH-RAT-01:** read-only GitHub connector and contents API source inspection of `cncf/clomonitor`; 6 directory-list API calls identified the actual nested source paths; 3 file reads examined score aggregation, report/missing-check representation, exemptions and disabled external-tool modes. No writes. Actual paths: `clomonitor-core/src/score/mod.rs`, `clomonitor-core/src/linter/report.rs`, `clomonitor-core/src/linter/mod.rs`. Source observations are linked in `research/mechanism-audit.md`; repository default-branch snapshot, not a tagged release review.
- No evaluator was executed against a repo in this batch; no cross-rater benchmark, outcome validation, user-impact study, score reproducibility test, or independent audit was performed.

### Scope and language limits

English owner docs dominated this batch. One English-language OSS Compass model page exposed explicit activity caveats, and Chinese documentation surfaced through discovery, but no systematic Chinese forum or dataset search was run. Candidate selection is intentionally limited to seven existing inventory entries. Results do not establish the best, latest, most-used, or most valid evaluators.

## 2026-11-10 — native modal close paths and accessibility, batch UI-DIALOG

**Local time:** approximately 14:38–14:42 Asia/Kolkata; exact per-call times unavailable. Read-only web search/fetch. No browser lab or assistive-technology tests.

### Search — UI-DIALOG-S01

Three Parallel web_search calls returned ten ranked summaries each (30 displayed; duplicates may overlap). Exact queries:

1. WHATWG HTML dialog cancel event close event escape key close method animation behavior specification
2. site:github.com dialog cancel event animation Escape close button issue html-dialog
3. site:developer.mozilla.org HTMLDialogElement cancel close CSS transitions html-dialog
4. W3C ARIA Authoring Practices modal dialog pattern Escape key focus return keyboard requirements
5. site:github.com dialog cancel event animation Escape close button issue aria-dialog
6. site:developer.mozilla.org HTMLDialogElement cancel close CSS transitions aria-dialog
7. HTML dialog Escape versus close button CSS exit transition browser issue dialog animation close method cancel event
8. site:github.com dialog cancel event animation Escape close button issue close-animation
9. site:developer.mozilla.org HTMLDialogElement cancel close CSS transitions close-animation

Search IDs: search_1ae4758d1999aeca2bcdfd6a0436bc0e, search_92f19138fe8d84a6380382a883f15ea9, search_7b18495a1bcb4d4933130fbc577c8f88. Screening was selective and source-led; no unique-hit total or platform coverage claim.

### Primary fetch — UI-DIALOG-F01

Parallel web_fetch requested eight URLs and returned eight extracts with no extraction errors. Extract ID: extract_fdc308fc2cfcbfeed5f1e4529ad427ca. Sources: WHATWG HTML dialog spec; W3C APG modal pattern and WCAG technique; MDN dialog/cancel/close and animation documentation; Chromium issue 41484805; current Material Web dialog source; Chrome developer dialog guidance.

The HTML Standard directly states that requestClose dispatches cancel before closing if not prevented and that it can consolidate cancelation/closing logic by having non-close-request affordances call it. Direct close has a different event path. WAI-ARIA APG specifies Escape and focus behavior for its modal-dialog pattern; its technique/examples are guidance rather than the only permissible WCAG solution. Chromium issue 41484805 is a report tied to Chrome 120 / Edge 120 and a specific interaction history. Current status and modern browser reproduction were not established. Material Web source retains a compatibility reference to a Chrome 120 issue, not proof that the exact historical behavior remains in current browsers.

The targeted synthesis and sequence matrix are in research/v2/failure-patterns/modal-path-equivalence.md; FP-28 was added to the larger evidence batch. The evidence still does not explain the supplied video's implementation.

## 2026-11-10 — WPT sequence tests and dialog spec history, batch UI-DIALOG-S02

**Local time:** approximately 14:42–14:48 Asia/Kolkata; exact per-call times unavailable. All calls were read-only.

### Parallel search

Three web_search calls returned ten ranked summaries each (30 displayed; overlaps possible; selective screening only). Exact queries:

1. site:github.com/web-platform-tests/wpt dialog requestClose cancel event Escape test
2. site:wpt.fyi dialog Escape cancel close close watcher tests
3. web platform tests dialog close request cancel event no user interaction
4. model-based testing web applications user event sequences state machine empirical study
5. stateful testing GUI asynchronous animations race conditions web applications paper
6. systematic UI testing event sequence generation dialog interaction regression research
7. W3C dialog keyboard focus return testing technique modal accessibility
8. web accessibility automated testing limitations keyboard screen reader user testing primary study dialog
9. ARIA dialog component test keyboard focus browser assistive technology official

Search IDs: search_dfb7a72969358eeedaac372357495d1e, search_426fe8446d92f9f071d8c825967e0e70, search_ecc155b0711bf40d2ab7df876f185b20. Search surfaced WPT requestClose and CloseWatcher tests, a closed WHATWG issue, and GUI testing papers. The stateful-UI and accessibility-research results remain leads; no full-paper appraisal was done in this batch.

### Source fetch and status verification

- **UI-DIALOG-F02:** Parallel web_fetch requested six URLs and returned six extracts without errors; ID extract_e31f9aa0a91de00b3dca7aff8b26a072. Sources: WPT dialog-requestclose, dialog-closedby-start-open, CloseWatcher user-activation README; WHATWG issue #11230; merged WPT PR #52020; WPT dialog-close test.
- **GH-UI-01:** four read-only connected GitHub calls: fetch WHATWG issue #11230, fetch WPT PR #52020, fetch all comments on WHATWG issue #11230, fetch WHATWG PR #11326. Issue #11230 is closed; PR #11326 is merged; WPT PR #52020 is merged. The issue discussion and merged spec patch show setup/cleanup changes around connected open dialogs and an early-return condition for requestClose in disconnected or not-fully-active documents. The WPT PR adds no-crash tests for detached-dialog and document-without-browsing-context cases after browser crashes were reported. No current multi-engine pass matrix was fetched or inferred.

Key test observations are summarized in research/v2/failure-patterns/modal-path-equivalence.md and research/v2/failure-patterns/initial-evidence-batch.md. The WPT source author described the cases as organically grown rather than neatly organized; the repository has more test inventory than we reviewed. No tests were executed.


# 2026-11-10 — AI lab research, cross-domain agent evaluation and research-feed integrity

**Local time:** 2026-11-10 Asia/Kolkata; exact per-call times unavailable. All search, paper and repository accesses below were read-only. No benchmark, agent or repository test was executed.

## AI-LAB-S01 — first-party lab research discovery

- **Tool/run:** Parallel `web_search`; ID `search_1f3e6e49cb2e89b9bb40e41ead656df4`.
- **Objective:** find current official lab research/release routes relevant to agent evaluations, code generation, reliability, safety and benchmarks; prefer primary pages.
- **Exact queries:** `site:openai.com/research evaluations agents benchmarks`; `site:anthropic.com/research evaluation agents safety`; `site:deepmind.google/discover/blog evaluation agents benchmarks`.
- **Returned:** 10 ranked result records. **Screening:** selective result-summary review; a separate exact screened count was not recorded.
- **Leads:** OpenAI Evals hub and coding-evaluation audit; OpenAI's third-party evaluation playbook; LifeVal (2026-11-03); GeneBench-Pro (2026-06-30); OpenAI Alignment research/release feed; other OpenAI safety/evaluation posts.
- **Limit:** results were a single bounded search window, primarily surfaced OpenAI pages, and do not represent all labs or their complete publication output.

## AI-BENCH-S01 — broad evaluation and benchmark discovery; output not retained

- **Tool/run:** Parallel `web_search`; exact search ID and per-query result count were not retained because the aggregated output was truncated.
- **Objective:** independent agent-evaluation, benchmark repositories and evaluation work beyond coding agents, including safety, tool use, robustness, long-horizon work and real-world outcomes.
- **Exact queries:** `AI agent benchmark repository long horizon official 2026`; `LLM evaluation benchmark contamination validity artifact repository`; `AI evaluation framework safety robustness official GitHub`.
- **Screening/use:** no result summaries from this call were used as evidence. Related topics were re-searched with preserved windows in `AI-LAB-S02` and `AI-PORTAL-S01`.

## AI-LAB-S02 — cross-domain lab and independent research leads

- **Tool/run:** Parallel `web_search`; ID `search_2164d42a9c3b99d3bd7bf9d216992849`.
- **Objective:** recent primary work (2025–2026) measuring agent reliability beyond code completion, including scientific workflows, computer use, long-horizon behavior and safety; distinguish lab-authored work from independent studies.
- **Exact queries:** `site:anthropic.com/research benchmark agents evaluation 2026`; `site:microsoft.com/en-us/research publication agent evaluation benchmark 2026`; `site:deepmind.google/discover/blog benchmark agents evaluation 2026`; `site:ai.meta.com/research benchmark agent evaluation 2026`; `site:nvidia.com/en-us/research agent benchmark evaluation 2026`; `site:allenai.org research agent benchmark evaluation 2026`.
- **Returned:** 10 ranked result records. **Screened:** all 10 visible title/excerpt records.
- **Leads followed:** OmicsBench; OSGuard; ATBench; “Towards a Science of AI Agent Reliability”; ReproBAIT; and a research-lifecycle benchmark lead. Do not label these as lab products solely based on search placement; affiliations are separately checked in the paper excerpts.
- **Limit:** domain and venue coverage is small and search-ranked. The results are leads, not a new cross-domain benchmark census.

## AI-PORTAL-S01 — paper and lab-index discovery surfaces

- **Tool/run:** Parallel `web_search`; ID `search_12ad722d9e7ea03d1721132fa7782b10`.
- **Objective:** compare current paper-monitoring sources and trackers for scope, cadence, attribution, provenance and known gaps.
- **Exact queries:** `TheLatestInAI paper feed latest update coverage`; `AlphaXiv discover papers arxiv AI search`; `GitHub frontier AI papers tracker lab coverage collection status`.
- **Returned:** 10 ranked result records. **Screened:** 10 visible result summaries.
- **Leads retained:** The Latest in AI; AlphaXiv; Hugging Face Papers; and the community project `LikeACloud7/awesome-frontier-ai-papers`. Other trackers and summaries were treated as discovery leads only.
- **Limit:** this search does not compare recall or precision across portals; result ranking reflects one retrieval window.

## AI-EXA-S01 — Exa search for research portals and official lab feeds

- **Tool/route:** Exa `web_search_exa`; no stable search ID was exposed in the captured response.
- **Exact query:** `The Latest in AI arXiv paper discovery portal other AI research tracking portals official lab research Github organizations benchmark evaluation 2026`.
- **Returned/screened:** aggregate output was truncated; exact total and full screening denominator were not retained. Selected tracker links were independently opened through GitHub in `AI-TRACK-F01`.
- **Limit:** do not infer portal completeness or counts from this aggregate response.

## GH-AI-S01 — connected GitHub repository search

- **Tool/route:** connected GitHub repository search; five read-only queries. The route returned repository names, with no stable per-call IDs in the captured output.
- **Exact calls and outcomes:**
  1. `AI evaluation benchmark agent model reliability` (no org filter): 8 repositories returned; mixed relevance, including several unrelated user repositories.
  2. `eval benchmark`, `org=openai`: 2 results (`openai/evals`, `openai/MultiLangBench`).
  3. `evaluation benchmark`, `org=anthropics`: 1 result (`anthropics/scone-bench`).
  4. `agent benchmark`, `org=microsoft`: 17 results; selected `microsoft/WindowsAgentArena` for a README-level sample. Other matches were not audited.
  5. `agent evaluation`, `org=google-deepmind`: 0 results through this connector query.
- **Returned total:** 28 listed repository records across the five calls. Repository search is not code search or a complete organization inventory. A zero result is only a property of that exact query/connector window.

## AI-LAB-F01 — OpenAI research/evaluation page extraction

- **Tool/run:** Parallel `web_fetch`; session `session_c1b2039eac4f6c4a9523887d0d043868`.
- **Requested:** four URLs: LifeVal PDF; OpenAI wet-lab science agents page; GeneBench-Pro page; OpenAI third-party evaluation playbook.
- **Returned:** three extracts, one network error (`https://openai.com/index/measuring-how-ai-agents-handle-everyday-wet-lab-science/`). The BioBasicsBench page appeared in the search excerpt dated 2026-11-06, but its full page was not read in this fetch.
- **Screened:** selected methods/results/limitations excerpts from LifeVal, GeneBench-Pro and the playbook; no complete line-by-line paper audit.
- **Limit:** provider-authored claims remain first-party evidence, not independent replication. LifeVal's privacy/consent and full denominator details need separate review.

## AI-ALPHAXIV-F01 — targeted paper-version questions

- **Tool/route:** AlphaXiv paper PDF/page query tool; five independent paper IDs queried, all returned relevant pages.
- **Papers/versions:** OmicsBench `2610.21074v1`; OSGuard `2606.15034v3`; agent reliability `2602.16666v3`; ATBench `2604.02022v4`; ReproBAIT `2610.19810v1`.
- **Questions:** sample/task construction, benchmark split, model/harness count, repetition and resource budgets, graders/oracles, main findings, limitations, code/data availability.
- **Screening:** selected page excerpts rather than every page of each paper. Paper status was captured where explicit (ICML 2026 for the reliability paper; COLM 2026 for ATBench; preprint for the other listed arXiv versions).
- **Limits:** no benchmark execution, replication, source-code audit or cross-paper statistical reanalysis. See `research/v2/agent-quality/cross-domain-ai-evaluation-and-research-routes-2026-11.md` for the scoped appraisal.

## AI-PAPER-F01 — primary paper and benchmark discovery follow-up

- **Tool/run:** Parallel `web_fetch`; extract/session ID `extract_9bb6d2935ed7428599a829f797eac40e` / `session_9bb6d2935ed7428599a829f797eac40e`.
- **Requested/opened:** five URLs (four arXiv HTML papers and the SecureBio ReproBAIT overview); five extracts, no extraction errors.
- **Screened:** selected abstract, benchmark construction, evaluation and limitation sections for the same five papers as `AI-ALPHAXIV-F01`. AlphaXiv queries were used to fill method questions rather than assume title/abstract summaries were enough.
- **Limit:** excerpts are targeted; the study-specific full methods, supplements, code and datasets still require follow-up.

## GH-AI-F01 — lab and benchmark repository README inspection

- **Tool/route:** read-only GitHub contents and metadata endpoints, plus repository-root reads. No write route used.
- **Inspected:** `LikeACloud7/awesome-frontier-ai-papers` README, `docs/COVERAGE.md`, `public/data/collection_health.json`, `public/data/company_papers.json`, and `.github/workflows/update-papers.yml`; `openai/evals/README.md`; `anthropics/scone-bench/README.md`; `microsoft/WindowsAgentArena/README.md`; and tracker repository metadata.
- **Selected source snapshots:** `openai/evals` README blob `b6d57c76ee5b1361834b415ffbb63bb9c5f3ff68`; Scone-Bench README blob `98b3be11b6c831589ee89b474a3f0e644f2ae9d8`; Windows Agent Arena README blob `d4b26caff094a182d686b33232843fafe6ac070d`; tracker coverage document blob `e470110073887afc8e9df60c7603455d04ffcb18`; tracker workflow blob `5806981fde49c14371617623b04a20f3932dfc1e`; collection-health blob `a14df97927669e2e5abe557c7e9ac059e0f53e9e`.
- **Observed:** OpenAI Evals README positions a registry plus custom/private evals and flags data rights/licensing and API costs; Scone-Bench labels itself unmaintained and describes an objective, reset-before-grade DeFi exploit verifier; Windows Agent Arena documents an OS VM snapshot and local/cloud resource burden. The tracker describes 19 configured labs and a daily multi-source collector.
- **Collection-health snapshot at fetch:** `partial`, 111 sources: 64 ok, 43 partial, 4 failed; 35 sources contain errors (31 partial + 4 failed); 1,359 records pending metadata; newest source check `2026-11-05T11:23:30Z`. The daily workflow configuration is not evidence a fresh run occurred on retrieval day. The large `company_papers.json` contents endpoint returned an empty payload, so item-level freshness could not be checked.
- **Limits:** all repository claims are README/docs-level unless stated; no code, CI workflow run, task, test, dataset or model was executed. The tracker covers a configured 19-lab US/China set and explicitly does not claim complete recall.

## AI-TRACK-F01 — tracker collection policy and health snapshot

- **Tool/route:** read-only connected GitHub file and repository metadata reads for `LikeACloud7/awesome-frontier-ai-papers`.
- **Files read:** `README.md`, `docs/COVERAGE.md`, `public/data/collection_health.json`, `.github/workflows/update-papers.yml`; the default-branch metadata was also requested. Blob IDs for the coverage, workflow and health files are in `GH-AI-F01`.
- **README snapshot:** 34,646 indexed publications, 19 configured labs (9 US and 10 China), archive start 2024, displayed latest snapshot 2026-11-05, 35 sources needing attention and 1,359 pending metadata records.
- **Policy described by the project:** daily collection from official catalogs/feeds, OpenAlex, Hugging Face and rotating repository/affiliation routes; only one lab is historically reconciled per run in an approximately 19-day cycle. The tracker distinguishes research posts, reports and model/system cards from peer-reviewed papers; an affiliation or source artifact is required for lab attribution; unresolved records are queued; collection errors are surfaced rather than presented as a clean empty success.
- **Health file snapshot:** status `partial`, 111 source records (64 `ok`, 43 `partial`, 4 `failed`), 35 records with errors (31 partial plus 4 failed), 1,359 records pending metadata; latest source check `2026-11-05T11:23:30Z`. The workflow has a daily schedule, but the dataset/health snapshot retrieved on 2026-11-10 was five days old. This distinction is retained: schedule is configuration; snapshot time is observed state.
- **Access limit:** `public/data/company_papers.json` could not be read through the contents API; the returned content was empty due to its size. Item-level freshness, duplication and attribution were therefore not assessed. The README totals and health JSON are owner-maintained project outputs, not independently re-collected counts.
- **Interpretation:** this repository is both a useful candidate discovery index and a concrete example of explicit scope, attribution evidence, retry queues, partial-state reporting and freshness debt. It tracks a configured US/China lab universe, not all AI research or all countries.


## 2026-11-10 — repair of the AI-lab batch provenance

The preceding research turn had added C24, Q206–Q258 and PC92–PC98, but its cell-query links, cell-run links, source-route/source-register records and search-log/ledger entries did not land. This section restores the trace from the saved exact query bank and retained tool output. Where an earlier tool response had been truncated, counts and search IDs are explicitly marked unknown; they are not reconstructed.

### AI-LAB-S03 — primary lab publication search

- **Tool/run:** Parallel web_search, search ID search_14cd1fb05164921cf0fb9f05992d8139.
- **Exact queries:** site:ai.meta.com/research/publications/ agent benchmark evaluation 2026; site:research.nvidia.com/publication agent evaluation benchmark 2026; site:allenai.org research agent evaluation benchmark 2026; site:deepmind.google/research/publications/ agent evaluation benchmark; site:openreview.net AI agent reliability benchmark evaluation; Shanghai AI Lab OpenCompass agent benchmark 2026 GitHub.
- **Returned/screened:** 10 ranked records; 10 visible summaries. The query bank stores Q206–Q211.
- **Follow-up:** selected paper/project routes were followed to targeted paper and artifact reads. This was a bounded search, not a lab publication census.

### GH-AI-S02 — bounded GitHub organization searches

- **Tool:** connected GitHub repository-search connector; six read-only calls, per-call result counts retained.
- **Exact query + filter and returned count:** benchmark, org=google-deepmind (19); evaluation benchmark, org=facebookresearch (20); evaluation benchmark, org=NVIDIA (3); agent benchmark, org=allenai (0); agent evaluation, org=open-compass (2); evaluation benchmark, org=FlagOpen (0).
- **Total:** 44 listed records; some calls reached their page-size limit. Exact queries are Q212–Q217.
- **Limit:** zero means only that this connector query returned no record. It does not mean the organization has no benchmark repositories.

### AI-RELIABILITY-S01 — repeated-run and leaderboard reliability

- **Tool/run:** Parallel web_search, search_b58fc88d106a24ad8f94082cb316491e.
- **Exact queries:** AI agent benchmark reliability leaderboard task count; agent evaluation reliability repeated runs; benchmark score confidence intervals agent.
- **Returned/screened:** 10 ranked records, 10 summaries. These are Q218–Q220.
- **Follow-up:** reliability paper and the honest-agent-scores public reanalysis were read as separate evidence; no benchmark was run.

### AI-MAINT-S01 — maintainability, duplication and structural quality

- **Tools:** Parallel searches and AlphaXiv discovery/PDF queries.
- **Exact query strings:** Q221 coding agent repository maintenance benchmark; Q222 agent code review benchmark repo; Q223 AI code quality refactoring evaluation; Q224 agent benchmark engineering systems verifier; Q225 AI agent recovery failure benchmark; Q226 scientific workflow agent evaluation benchmark; Q239 AI generated code maintainability benchmark repository; Q240 code agent duplication refactoring regression evaluation; Q241 AI coding maintainability technical debt empirical study; Q248 Needle in the Repo benchmark code github; Q257 Needle in the Repo NITR maintainability benchmark.
- **Counts/IDs:** earlier aggregated search output was truncated; exact per-call totals and some search IDs were not retained. Q221–Q226 and Q239–Q241 remain exact because they are in the query bank.
- **Follow-up:** NITR's ASE paper, official project page, repository evaluator and public cases were inspected; selected code-quality studies were queried separately. Do not infer the user's specific modal failure from these sources.

### AI-CODE-FIELD-S01 — field studies of AI-authored changes

- **Tools/IDs:** Parallel/AlphaXiv; search IDs search_a614142ffc50507954ef87af1e0457d4, search_9d079ae372af3551d0115794cf73c2e9, search_6ed7fb9e04f4b80ab728822ad0510f24.
- **Exact queries:** More Code Less Reuse MSR 2026 AI generated pull requests DOI; Beyond Bug Fixes post-merge code quality agent PR MSR 2026; AI generated code technical debt MSR 2026 study sample; AI generated pull requests reviewer sentiment code reuse MSR 2026; AI coding agent changes reverted empirical study 2026. These are Q249–Q250 and Q254–Q256.
- **Counts:** outputs were partly truncated; per-query result totals were not retained. Selected papers were followed into method sections; counts from different studies were not pooled.

### AI4AI-S01 and regional AI-lab searches

- **Tool/run:** Parallel web_search, search_41ddea931c68dbc6dbc2e11f3076f8d1.
- **Exact queries:** AI4AI Bench Naver Einsia arxiv algorithm design benchmark; AI agent algorithm discovery research benchmark 2026 Github; AI agent engineering benchmark Google AI infrastructure arxiv October 2026 (Q251–Q253).
- **Returned:** 10 in the targeted follow-up; selected AI4AI-Bench paper and repository README were read. No benchmark tasks were run.
- **Regional search:** Parallel search_ebe9317b476fcddd3cea45a5ca078c35; exact queries: Europe AI lab agent evaluation benchmark GitHub 2026; Japan Korea India AI research agent benchmark 2026; Mistral AI2 TII Alibaba Qwen agent evaluation GitHub (Q236–Q238). Ten results were returned in the retained summary; regional affiliation must be confirmed from papers and project pages.

### GH-T3-F01 — X lead and direct codebase inspection

- **X exact queries:** ("AI coding agent" OR "AI-generated code") (duplication OR redundancy OR maintenance OR "code quality") has:links lang:en; ("AI agents" OR "coding agents") (benchmark reliability OR "post-merge" OR regressions) has:links lang:en (Q245–Q246).
- **Returned/screened:** 10 summaries per X query. Selected article claims were treated as leads and followed into code.
- **GitHub query:** T3 Code agent first coding agent workspace (Q258), four low-precision repo records. The resolved source was pingdotgg/t3code.
- **Files read:** AGENTS.md, evals/README.md, evals/mcp-tool-use/README.md, and the Oxlint plugin. The guessed scripts/ci-changes.cjs path returned 404; no test or eval was run.

### AI-PORTAL-S02 and GH-AI-F02 — earlier portal and repository samples

- **Portal queries:** Q227 was the saved Exa natural-language query about current AI research/lab repository discovery. Q228 and Q229 were AlphaXiv recency questions. Q242 The Latest in AI latest papers update coverage; Q243 AlphaXiv paper discovery latest arxiv coverage; Q244 AI research paper aggregator collection freshness coverage. Parallel search_a1fba8c9860013ec2b1ef7006dd73b83e returned 10 visible summaries for Q242–Q244. The earlier portal pages and their observed dates/counts are documented in the companion note.
- **GitHub query family:** Q230 agent evaluation reliability benchmark; Q231 coding agent code quality repository maintenance benchmark; Q232 scientific agent workflow benchmark evaluation; Q233 evaluation benchmark with org=NVIDIA; Q234 evaluation benchmark with org=facebookresearch; Q235 evaluation benchmark with org=google-deepmind. The first aggregate output was truncated; per-query returned counts were not retained. These are bounded repo searches, not an inventory.
- **Selected README reads from this batch:** Google DeepMind gBench, Meta Agents Research Environments, WAGIBench, OpenAI Evals, NVIDIA SkillEvaluator/swe-serve, OpenCompass AgentCompass and other previously linked evaluation projects. Exact file-level claims are cited in the relevant evidence notes.

## 2026-11-10 — fresh lab/research artifact sweep, C25

### AI-LAB-S03-C25 — current lab and artifact discovery

- **Tool/run:** Parallel web_search, search_295d4036d809e9aaa48968c5bae06c07.
- **Objective:** current primary lab publications and official open evaluation repositories; capture dates, affiliations, task/oracle, artifacts and limitations.
- **Exact queries:** AI lab agent evaluation 2026; open source model evaluation repositories; AI research artifact reliability (Q259–Q261).
- **Returned/screened:** 10 result records, 10 visible excerpts. DeltaML-Bench, lab evaluation methods and repository leads were followed to paper and repo pages.

### AI-LAB-S04 — systems and science beyond coding

- **Tool/run:** Parallel web_search, search_4464e4a6d54fe728dcb2904e7f64a6d1.
- **Exact queries:** AI scientific agent benchmark 2026; engineering agent evaluation repository; AI infrastructure benchmark labs (Q262–Q264).
- **Returned/screened:** 10 results, 10 visible summaries. Followed Infrathon, InfraDev, power systems/scientific task and reliability papers. A result is not classified as a lab product from search placement alone; affiliations and primary routes were checked.

### AI-PORTAL-S03 — research source and feed discovery

- **Tool/run:** Parallel web_search, search_8ce9efccda6ab771b32ee1d948da86fc.
- **Exact queries:** The Latest in AI papers indexing; AlphaXiv research feed documentation; Hugging Face Papers arxiv feed (Q265–Q267).
- **Returned/screened:** 10 results, 10 visible summaries. arXiv RSS documentation, AlphaXiv, The Latest in AI and a forum example of stale version metadata were retained as discovery leads, not portal coverage estimates.

### AlphaXiv discovery: AX-DISC-S02 and AX-DISC-S03

- **Tool:** AlphaXiv discover_papers. The initial two calls in this round omitted the required question field and returned schema-validation errors; no search happened in those two calls. The calls were retried with the question included.
- **Q268 exact question:** What is the newest primary research on evaluating AI coding agents and model agents that work in real repositories? Prioritize published artifacts, task/oracle design, structural and post-merge outcomes, repeated-run reliability, and known limitations. Return named papers with IDs, dates, affiliations, and GitHub links when available.
- **Q269 exact question:** What recent research from AI labs or other labs evaluates AI systems beyond chat, including science, infrastructure, robotics, and real workloads? Prioritize repositories and reproducible task/oracle details, report source regions and limitations, and identify paper IDs and dates.
- **Returned/screened:** 16 coding/repository records and 19 cross-domain records were visible and screened by title/abstract. They are recency-ranked, English-indexed discovery samples, not a census or acceptance filter.
- **Follow-up:** selected paper IDs were queried individually. A one-digit transcription error requested 2610.08962 and returned an unrelated Go-deadlock paper. It was rejected by title/author mismatch; corrected paper 2610.08927 was read and is the only source used for Station.

### GH-AI-S03 — bounded AI-lab repository searches

- **Tool:** connected GitHub repository search; per_page=15.
- **Exact query/filter/outcome:** evaluation benchmark with org=openai (1); evaluation benchmark with org=anthropics (1); evaluation benchmark with org=google-deepmind (2); agent evaluation benchmark with org=facebookresearch (6); agent benchmark evaluation with org=NVIDIA (2). These are Q273–Q277.
- **Returned/screened:** 12 repo names/metadata entries. Selected OpenAI Evals, Google DeepMind gBench and Meta/WAGIBench READMEs were followed. This does not inventory any lab's repositories.

### GH-ART-S01 through GH-ART-S03 — paper-to-repository searches

- **Exact global queries/results:** DeltaML-Bench (2); InfraBench AI agents (2); Terminal-Bench-Science (7), Q278–Q280.
- **Named follow-ups:** SWE-CC repository policy compliance (1); CrossSWE cross repository software engineering benchmark (0); InfraDev coding agents AI infrastructure benchmark (0); Infrathon AI infrastructure optimization benchmark (0); eth-sri vulnerability propagation coding agents (0); DeepResearch RewardBench (1), Q281–Q286.
- **Additional queries:** repository norms RepoNorm SYSUSELab (0); All Smoke No Alarm agent authored test code oracle (0); Multi-Condition Requirements AI Coding Benchmarks (0); exact RepoNorm (2), Q287–Q290.
- **Limit:** connector repo search is name/description based and had low-precision or zero-result responses. A zero does not establish absence; exact paper-linked URLs and other hosts were checked where available.

### WEB-S02 — paper and release verification search

- **Tool:** connected web search.
- **Exact queries:** "Infrathon" "github.com" 2611.11995; "InfraDev" "github.com" 2610.36589; "CrossSWE" "github.com" 2611.01484; "DeepResearch RewardBench" 2611.10156 repository (Q291–Q294).
- **Returned/screened:** nine result records and summaries. The ACL Anthology record established the EMNLP Findings venue. A separately surfaced repository page says the paper is available but code/data are coming soon. Direct page-open requests were included in the same call but did not produce a separately retained page transcript; subsequent page, PDF, dataset and connector outcomes are described below.

### AI-PAPER-F02, AI-PAPER-F03 and AI-PAPER-F04 — targeted PDF/page extraction

- **Tool:** AlphaXiv answer_pdf_queries.
- **Exact common questions for six papers:** What exactly is evaluated: tasks, systems, datasets, sample size, execution budget, and comparison baseline? What are the oracle and scoring design, repeated-run or statistical treatment, and stress/recovery checks? What is the paper version/date, author affiliations, public code/data link, and stated limitations or threats to validity?
- **AI-PAPER-F02 papers:** 2611.11455 Coding Agents Propagate Vulnerabilities; 2611.01484 CrossSWE; 2610.06193 SWE-CC; 2611.11995 Infrathon; 2610.36589 InfraDev; 2611.10156 DeepResearch RewardBench. Six responses were screened at the abstract, methods, limitation, and artifact-link passages selected by the query. This was targeted retrieval, not page-by-page full reading.
- **AI-PAPER-F03 papers:** 2610.14768 SWE-Maintain; 2611.03162 Beyond Surface Metrics; 2610.07757 RepoNorm; 2606.18168 All Smoke, No Alarm; 2611.08134 Who Can Evaluate AI Independently? Five targeted responses were screened for sample, method, limitations and release route.
- **AI-PAPER-F04:** corrected Station paper 2610.08927; two questions asked what the benchmark evaluates and what release/date/affiliation/limitations are reported. Three oracle-paper tasks and two no-oracle tasks are reported in the extracted page. No result was reproduced.

### AI-EXA-F02 through AI-DATA-F01 — live page and dataset routes

- **AI-EXA-F02 tool/URLs:** Exa webpage fetch requested the Latest in AI homepage, its /papers route, AlphaXiv homepage, arXiv RSS help page, and an additional related page URL. The consolidated extract showed: homepage 120.8K papers and newest Nov 6; /papers 122.2K and newest Nov 9; AlphaXiv homepage sample included Nov 9 papers. The current /papers route differed from an earlier captured page. Record observed endpoint values; do not infer the delay or completeness of the underlying index.
- **AI-EXA-F03:** fetched the full Meta Muse Spark Open evaluation-methodology page. Its disclosure assigns per-benchmark values to official leaderboards, internal runs or provider self-reports. The OSWorld section describes 361 tasks, a Google Drive exclusion, four attempts, and differing model-native coordinate conventions. This is provider-authored methodology, not an independent rerun.
- **AI-DATA-F01:** fetched CrossSWE-Bench and Infrathon Hugging Face pages. The CrossSWE viewer exposed task, source commit, image reference, evaluation-contract path, gold/test patches, support and license-record fields. Infrathon's page required accepting conditions and showed no dataset card; no conditions were accepted and no files were opened.

### GH-LAB-F03 — first-party model-evaluation repository docs

- **Tool:** GitHub contents connector. Eight selected files: google-deepmind/gbench README; docs/performance.md; docs/results.md; docs/scaffold-versioning.md; docs/THIRD_PARTY_DATASETS.md; docs/quality.md; facebookresearch/WAGIBench README; openai/evals README.
- **Observed mechanisms:** gBench documents repeated-run mean/median/standard deviation and percentiles, a default 5% CV threshold, repeated open-loop stress sweeps, output metadata/failures/sample traces, subject/scaffold separation and dataset licenses/access terms. Its license inventory is dated September 2026 and requires rechecking. WAGIBench distinguishes MCQ from judge-based scoring. OpenAI Evals describes registry and custom/private eval routes.
- **Limit:** README and documentation reads only; no code, CI, model, dataset, evaluation or workload run.

### GH-REPO-F01 and GH-REPO-F02 — release inspection and access failures

- **GH-REPO-F01:** fetched README files from SWE-CC, Infrathon, eth-sri/vulnerability-propagation, NLP2CT/DRRB, AlgorithmicResearchGroup/deltaml-bench-inspect, and AlgorithmicResearchGroup/deltaml-bench-vivaria, plus metadata calls. Four README bodies were substantive; Infrathon and NLP2CT/DRRB returned empty content. GitHub metadata for those two exact repositories returned 404. SWE-CC documents deterministic policy checkers; the security repo documents exploit/PoC scoring; DeltaML's adapters document active/archived task scope, hidden-score variants, scorer trust checks and high resource demands.
- **GH-REPO-F02:** fetched SYSUSELab/RepoNorm README, docs/reproduction.md, docs/acquisition.md, docs/experiments.md, benchmark/README.md and data/README.md, plus repository metadata. The README describes 121 tasks, six Python repos, 14 snapshots and 1,089 released executions. The docs describe evidence and counterexample checks, two-human review samples, hashes, cost records, paired bootstrap intervals and a reproduction path. None of those commands was run.
- **Other observed release states:** a separate web-discovered DRRB repository page says “code” and “data” are coming soon; the article's NLP2CT/DRRB link and that page are not reconciled. CrossSWE has a dataset card even though the connector's GitHub search returned zero. InfraDev's code release was not found in this pass. The paper-linked Infrathon repository returned 404 while its dataset page was gated and lacked a card.

### C25 boundary

This pass added PC99–PC108 and source records for selected papers, datasets, repositories, methods and portals. It did not establish the complete lab universe, global source coverage, benchmark validity, or framework requirements. No tests, benchmarks, model evaluations, stress runs, data downloads, terms acceptance, external writes or social posts were performed.



## Retrospective ledger entries with unrecoverable original search details

### RETRO-001 — initial rater discovery

- The original exact queries, result window, screening count, and individual source links were not preserved. The retrospective ledger retains only 11 candidate families.
- This is a source seed, not a reproducible search and not evidence that those families are exhaustive.

### RETRO-002 — initial standards discovery

- The original exact queries, result window, screening count, and individual source links were not preserved. The retrospective ledger retains only 11 candidate families.
- Treat as unverified route seeds; recover primary standards pages individually before citing an actual requirement.

### RETRO-003 — prior broad research attempt

- **Tool/route:** Parallel web_research.
- **Exact query:** not preserved.
- **Returned/screened:** zero; the request returned HTTP 402 for insufficient credits.
- No research result was used as evidence.

### RETRO-004 — search-route availability check

- **Operation:** Agent Reach health check, not a content search.
- **Outcome:** the command was unavailable in the current environment; no platform health data was returned.
- Existing connected X, GitHub, Parallel, Exa and browser routes were checked separately. This does not establish access to every platform.

### RETRO-005 — social-source leads

- The original query string and screening counts were not preserved. The retrospective ledger records two named leads only.
- Do not treat these as sourced claims; use current exact queries and open the original content if followed up.

### GH-ART-S02 — exact paper-to-repository searches

- See the C25 search section above for each exact query and count. The GitHub connector returned a SWE-CC repository and a DeepResearch RewardBench repository page, and returned zero for CrossSWE, InfraDev, Infrathon and vulnerability-propagation phrase queries.
- Later checks found the CrossSWE dataset on Hugging Face and opened vulnerability-propagation by its exact paper-linked URL. This demonstrates why connector zero-results remain query-local.

### AX-ID-F01 — paper identifier correction

- AlphaXiv was queried with the mistyped identifier 2610.08962 after the discovery output had shown 2610.08927. The returned Go-deadlock paper did not match the discovered title or authors and was excluded.
- The corrected query used 2610.08927 and returned the Station paper. Only the corrected paper informs the current note.

### AI-PORTAL-F02 — current paper-page snapshot

- This ledger pointer aliases AI-EXA-F02 for the earlier planned PC97 row.
- The exact observed routes and values are recorded there: homepage showed 120.8K and Nov 6, while /papers showed 122.2K and Nov 9; a prior /papers snapshot differed. These are page observations, not a measured service-latency claim.


## 2026-11-10 — benchmark landscape, validity and cross-domain suite sweep (C26–C27)

### Logging boundary

This section combines (a) a retrospective handoff for C26 and initial C27 discovery whose exact per-call timestamps or complete result windows were not preserved through context transition, and (b) searches/fetches performed during this session from 17:24 to 17:27 Asia/Kolkata. Retrospective status is explicit; no missing query text, count or remote search ID has been reconstructed as verbatim. Search results are not unique-benchmark counts.

### C26 — cross-domain task/oracle and AI-systems evaluation (retrospective)

- **Exact queries/time:** original payloads and per-call times unavailable. Q298–Q306 describe retrospective source operations, not quoted queries.
- **Source work:** the C26 report follows selected papers and official artifacts for Agents' Last Exam, Physical-Engineering's Last Exam, SCI-AGENT-EXAM, CUA-Recovery, ARIES, MAServeBench, OpenAI Evals, Inspect AI, EleutherAI Harness, MLPerf Inference, gBench, The Latest in AI, AlphaXiv and arXiv RSS. Eight benchmark/system cells PC109–PC116 are linked to this record.
- **Counts/access:** original result windows and source-open counts are unavailable. No benchmark, model, dataset or test suite was run or downloaded. The report separates first-party claims, paper results and interpretation.

### C27 — benchmark catalog and method discovery (initial grouped searches, retrospective reconstruction)

Parallel search was run in eight three-query groups recorded verbatim as Q307–Q330. Four search IDs are recoverable: `search_c6ecdb5ba08c8a48c0141038871293f2`, `search_a0644cf28ecb429dabbbc8e4c7511835`, `search_81b5ad1a6983495ad90d0e703c9020bc`, and `search_fbe62a36301d3e68a397d77ff4e67eb4`. Two other IDs retained in the prior output are `search_b09da77578c3d45c25f29bd3a125fb85` and `search_1c0b097f082b8ecd44b39eea67b99673`; IDs for the remaining calls were not preserved.

Exact Parallel query groups:

1. `code benchmark catalog survey`; `code benchmark quality reliability rigor`; `software testing benchmark catalogue`.
2. `mutation testing benchmark repository`; `code maintainability refactoring benchmark`; `software clone detection benchmark reuse`.
3. `software performance benchmark benchmark suite`; `energy consumption code benchmark suite`; `software bloat debloating benchmark`.
4. `compiler fuzzing benchmark suite`; `operating system reliability benchmark suite`; `browser benchmark webcompat benchmark`.
5. `572 code benchmarks rigor reliability reproducibility`; `672 code benchmarks survey 2014 2025 arxiv 2501.10711`; `code benchmarks 2025 survey benchmark quality data contamination reproducibility`.
6. `Cognition FrontierCode 1.1 benchmark mergeability`; `site:cognition.ai FrontierCode benchmark maintainers rubric`; `site:artificialanalysis.ai FrontierCode 1.1 leaderboard`.
7. `SWE-CI 100 tasks 68 repositories benchmark`; `sequential software evolution coding agent benchmark repository`; `SWE-STEPS benchmark long horizon software maintenance`.
8. `SQuaLity database test suite reuse benchmark`; `mutation testing test suite quality benchmark dataset`; `flaky test benchmark empirical benchmark suite`.

The first four calls each exposed at least seven visible excerpts (28 minimum); full counts and remaining output windows were truncated or not preserved. This is not a total result count or coverage estimate. A separate earlier grouped Exa pass covered code benchmark surveys, repository maintenance, performance/energy/size, and compiler, OS, browser, database, distributed, embedded and HPC systems; its exact query strings/counts were not retained and it is labeled retrospective.

### C27 — X via the user's signed-in Brave browser

- **Route:** Brave browser, signed-in X, Top results. No posts were made and no accounts were contacted.
- **Q331:** `(benchmark OR benchmarks OR evaluation) (mutation testing OR fuzzing OR code quality)`. Three visible posts were screened: generic fuzzing (low-value), EvalPlus, and Cognition/Artificial Analysis FrontierCode 1.1. Leads: [Cognition](https://x.com/cognition/status/2109729058745725037), [Artificial Analysis](https://x.com/ArtificialAnlys/status/2109703511843979391), [EvalPlus](https://x.com/davidwbressler/status/2119961591726711165). Followed claims to primary sources; X remains discovery, not benchmark evidence.
- **Q332:** `("benchmark" OR "evaluation") (compiler OR fuzzing OR "mutation testing" OR performance)`. Zero visible results in the observed window; this is query-local only.

### C27 — pinned catalog extraction

- **Awesome-Code-Benchmark:** pinned GitHub HEAD `cf177a1efc84c1286410200bcf6ec6f7ac4edef2`; README extraction yielded 233 entries in seven categories. Entries remain discovery-index-only.
- **HOW2BENCH:** current v5, revised 2026-07-06, reports analysis of 672 benchmarks. Parsing Appendix F yielded 379 bibliography-linked rows and 393 raw comma-delimited label segments before identity resolution. The 672 analysis units do not map one-to-one to this appendix extraction. Earlier v4 reported 572; the versioned change is preserved.
- **Combined:** 612 source-index rows in `candidate-index-leads.csv`, not 612 unique benchmarks. Repeated labels, grouped entries, paper/benchmark identity, and suite/task units are unresolved. The non-functional survey's 425 records are studies, not benchmark suites, and are not included.

### C27 — fresh Parallel and Exa searches, 2026-11-10 17:24–17:27 Asia/Kolkata

- **C27-PAR-009** — Parallel `web_search`; exact queries: `HOW2BENCH 672 code benchmarks`; `ABC benchmark checklist validity`; `software benchmark quality survey`. Ten results returned and screened. Search ID `search_ee1152f97f2f004cde6cdace896855e5`; primary HOW2BENCH v5/v4 and NeurIPS ABC sources followed.
- **C27-PAR-010** — Parallel `web_search`; exact queries: `TestJack witness test benchmark`; `SWE Mutation benchmark tests`; `BenchChecker benchmark leakage`. Ten results returned and screened; primary pages fetched. Search ID `search_6b55623a00971f2e30337968591adc41`. It also surfaced TestExplora, a proactive repository test-generation benchmark using documentation-derived intent.
- **C27-PAR-011** — Parallel `web_search`; exact queries: `software bloat debloating benchmark`; `compiler fuzzing differential benchmark`; `browser benchmark conformance suite`. Ten results returned and screened; selected USENIX and owner pages followed. Search ID `search_af28139111ef969b48e27682a3c38712`.
- **C27-EXA-002** — Exa exact query is Q342: “A cross-domain survey of software code benchmarks and benchmark quality methodology, including code reliability, repository maintenance, hidden test oracles, mutation testing, fuzzing, maintainability, performance, energy, program size, and code reuse.” Eight results requested; response exposed excerpts in free text without a structured total. The identifiable primary lead was the non-functional software-improvement survey.
- **C27-FETCH-001** — Parallel fetch of the USENIX presentation, its paper PDF and TestExplora v2; 3 requested, 3 extracted. Extract ID `extract_12024d7ce3bd07683a112461f28cbc8b`. The USENIX study describes 20 benchmark programs, 12 metrics, and 17 of 24 tools successfully built/run; only 22% of medium/high-complexity benchmark attempts yielded passable programs, and 13% of attempts were classified sound and robust in that study. TestExplora v2 reports 2,389 tasks across 482 repositories and documentation-derived intent with executable before/after validation. None was rerun here.
- **C27-FETCH-002** — Parallel fetch of BenchChecker, TestJack and NeurIPS ABC; 3 requested, 3 extracted. BenchChecker describes snapshot/similarity checks with false-positive/negative limits. TestJack describes prompt-grounded witness tests checked against a gold solution and reviewer filtering; finite audit budgets can miss trial-specific defects. ABC separates task validity, outcome validity and reporting. Extract ID was not retained in compact output; direct source URLs are in the benchmark report.

### C27 boundary and next work

This is a source-index layer and selected mechanism audit, not a complete benchmark universe or unique-identity count. No benchmark, model, code, workload, test harness or dataset was run. Next: canonicalize aliases and paper/task/dataset identities, then appraise a declared stratified primary-source sample across domain, language, artifact, oracle, lifecycle, risk and measurement. Regional, non-English and community coverage remain open.


### C27-AGENT-001 — Codex parallel candidate research

- **Operation:** three independent Codex research agents were assigned benchmark-method/meta-evaluation, code-quality catalog and systems-specific benchmark discovery. Exact subtask prompt strings and individual run timestamps were not preserved after context transition; therefore this is logged as a non-verbatim operation, not a reconstructed query.
- **Returned:** one methods report with 25 leads, one systems report with 38 named benchmark/conformance/stress/fuzzing/verification/simulation candidates, and one code-quality report with 40+ benchmark families. These denominators differ and overlap each other and the 612-row index.
- **Screening:** all three reports were read; candidate mechanisms were incorporated only where the report retained their scope/limitations or where primary sources could be followed. The result is a candidate pool, not 38 validated suites or a verified 40+ unique count.
- **Follow-up:** deduplicate against primary paper, dataset, repository and version identities before any unique-count claim; follow each system candidate to owner docs, task/oracle and execution boundary.


### C27-WEB-001 — reconcile debloating study counts

- **Tool/time:** built-in web search, 2026-11-10 17:42 Asia/Kolkata. Exact queries: `arXiv 2312.13274 software debloating tools benchmarks metrics`; `site:usenix.org security24 brown 24 tools debloating`. The exact result count was not retained; no new page was opened from these results.
- **Reason:** while reviewing the report, an earlier note called the work “10 tools,” but the C27 primary-paper extraction states that source was obtained for 24 tools and 17 were successfully built/run.
- **Resolution:** the arXiv paper and USENIX page identify the same study. Update the earlier note to “surveys 10 years of work; 20 benchmark programs; 12 metrics; source obtained for 24 tools; 17 successfully built/run.” The full primary paper, not the search snippet, supports the tool counts.
