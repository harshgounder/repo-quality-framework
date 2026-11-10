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
