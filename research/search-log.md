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
