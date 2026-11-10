# Initial evidence batch: behavioral-path drift and adjacent failure classes

**Date:** 2026-11-10 (Asia/Kolkata)
**Status:** first sourced batch; discovery continues. It is not a prevalence study, complete taxonomy, or universal test mandate.

## Starting example supplied by the user

The supplied video transcript reports a settings panel that animates on Escape but not when its close button is clicked. The speaker hypothesizes that multiple handlers were added over time and one path omitted later animation logic. The source video URL, application code and exact reproduction are not in this repo. Therefore:

- **Observed in supplied transcript:** two exit routes reportedly differ.
- **Speaker's root-cause hypothesis:** duplicated close logic.
- **What is not established:** whether handlers were duplicated; whether animation state, teardown timing, focus, event propagation, rendering, or another cause explains it.
- **New standards context:** the HTML dialog API distinguishes a close request (which fires a cancellable cancel event) from direct close. The HTML Standard says requestClose() can consolidate cancellation and closing logic by routing non-close-request affordances through it. See the targeted [modal path-equivalence note](modal-path-equivalence.md). This supports investigating shared semantics, while leaving the video's root cause open.

The research question is broader and more useful than “find duplicate code”: **when multiple triggers are intended to express the same user/system intent, what contract must remain invariant, which differences are allowed, and how can tests exercise the routes and their sequences?**

## Evidence cards

### FP-01 — Escape closes the wrong nested React Native Web modal when animation is enabled

- **Project evidence:** [`react-native-web` issue #1817](https://github.com/necolas/react-native-web/issues/1817) includes a nested-modal reproduction. The report says Escape closes all nested modals with animation enabled but only the topmost with `animationType="none"`.
- **Maintainer/project resolution:** linked [commit `6138fccc`](https://github.com/necolas/react-native-web/commit/6138fccc48cbf8aa4a361cdb3b4fef34cb643d38) closes the issue and changes the animation close callback target. The commit adds code and test changes.
- **Failure mechanism:** the visible key trigger, modal stack, animation callback and component nesting interact. A shared “close” intent can target the wrong owner after an asynchronous animation path.
- **Evidence status:** confirmed project-specific defect and merged fix. The issue and patch establish this case, not every modal implementation.
- **Candidate regression invariant:** for a stack of *n* dialogs, one Escape request closes exactly the top actionable modal; the remaining stack and focus owner match the documented contract, whether animation is enabled or not. Add repeated Escape and close-then-reopen sequences if permitted by product behavior.

### FP-02 — Caller cancellation is lost during Redis TLS dialing

- **Project evidence:** [go-redis PR #4143](https://github.com/redis/go-redis/pull/4143) fixes dialing that did not honor the caller context on TLS handshake paths.
- **Resolution/test:** the PR switches to context-aware TLS dialing while preserving timeout/keepalive behavior. It adds stalled-handshake regression tests for deadline, explicit cancellation without a dial timeout, and timeout enforcement across two paths; the PR reports those targeted tests passed ten times with the race detector and broader checks passed.
- **Failure mechanism:** nearby paths can look equivalent while one drops cancellation semantics. A caller believes an operation is canceled, but an internal blocking stage may continue.
- **Evidence status:** merged fix and explicit regression tests, as represented in the PR record. The PR's own test report is project evidence, not independent reproduction by this research.
- **Candidate regression invariant:** each API path that accepts a deadline/cancellation contract must terminate within that contract even when a lower-level handshake or dependency is stalled. Test both deadline and explicit cancellation; test positive and negative dial-timeout cases.

### FP-03 — .NET background service can skip its work if immediately stopped

- **Project evidence:** [.NET runtime issue #131249](https://github.com/dotnet/runtime/issues/131249) documents a start/stop timing regression associated with passing a cancellation token to `Task.Run`.
- **Resolution/test:** [PR #132241](https://github.com/dotnet/runtime/pull/132241) adds a deterministic test that occupies the only thread-pool worker, then immediately stops/disposes the service and verifies `ExecuteAsync` is invoked exactly once. It also checks pre-canceled startup separately.
- **Failure mechanism:** cancellation meant to ask work to stop was also used to decide whether the delegate starts at all. A narrow schedule exposes behavior that ordinary success-path tests miss.
- **Evidence status:** project issue and PR document the regression and intended fix. Reproducible test design is visible in the PR summary; this research did not rerun the repository suite.
- **Candidate regression invariant:** distinguish “must invoke the operation, which then observes a canceled token” from “must not start the operation.” Exercise immediate stop/dispose and pre-canceled startup under controlled scheduler/thread-pool pressure.

### FP-04 — Retried email operation can duplicate the external side effect after a response timeout

- **Project evidence:** [Composio issue #3654](https://github.com/ComposioHQ/composio/issues/3654) describes a retry-on-read-timeout path for non-idempotent tool calls. It links the scenario to `GMAIL_SEND_EMAIL` timing out on larger attachments, where retry may send the email again.
- **Status, clarified 2026-11-10:** the [linked SDK commit](https://github.com/ComposioHQ/composio/commit/09b552aa037a780cf6ba8797ee3f2830fca82269) disables retries for direct Python `tools.execute` and `tools.proxy` paths as an interim mitigation. The issue's later comments describe additional session paths and retry concerns; do not infer all paths are fixed. Request-level idempotency is separate; no end-to-end duplicate-send reproduction was verified here.
- **Failure mechanism:** a timeout says the client did not receive confirmation; it does not prove the remote service did not perform the action. Retrying a non-idempotent request can convert an uncertain result into two effects.
- **Candidate regression invariant:** inject a lost/late response after the fake or controlled server commits the effect; retry the same operation and assert one externally visible effect and a stable replay result. Also test a retry before the first attempt reaches the server. Keep idempotency-key persistence and expiration semantics in scope.
- **Evidence status:** detailed issue report and code-path claim, not independently reproduced or confirmed as fixed.

### FP-05 — Enter key used to close a modal can bubble to the opener and reopen it

- **Community report:** [Stack Overflow question 72670917](https://stackoverflow.com/questions/72670917/pressing-enter-key-to-close-button-closes-my-modal-but-the-event-is-attached-to) describes an Enter key-up handler on many openers. After closing the modal with Enter, the same event reaches the opener and reopens it.
- **Status:** Q&A report and code context; no maintainer/project fix or independent reproduction is used as evidence here.
- **Failure mechanism:** event propagation and focus restoration can make a single physical key press interact with the next focused control or a handler outside the modal. This is not necessarily duplicated business logic.
- **Candidate regression invariant:** after keyboard close and focus restoration, the closing keystroke must not activate the restored opener unless explicitly intended. Test Enter, Space and Escape separately; assert modal state, focus target and event side effects after the event turn completes.

### FP-06 — IME composition Enter can send a message twice in a specific browser/OS path

- **Project report:** [Chainlit issue #2598](https://github.com/Chainlit/chainlit/issues/2598) gives a step-by-step Korean IME composition case on macOS Chrome. The reporter says pressing Enter to finalize composition also sends the message twice; reported comparison environments did not show it.
- **Status:** issue report/reproducer, not independently reproduced here; the fetched page did not establish a fix.
- **Failure mechanism:** one physical key press has composition and submit semantics; platform/browser event ordering changes which handlers see it. A basic Enter-key unit test can miss it.
- **Candidate regression invariant:** composing text must be committed without submission; a distinct submit action submits once. Include composition-state and platform/browser combinations actually supported by the product. Keep the environment tuple with the test result.

### FP-07 — Backdrop close and Android Back produce different animated modal results

- **Project report:** [react-native-paper issue #4140](https://github.com/callstack/react-native-paper/issues/4140) includes failing test output for backdrop touch: the animation runs but does not fade out, while Android Back has a different result. Assertions also cover `onDismiss` timing.
- **Status:** issue was open/awaiting follow-up when fetched. Do not label it fixed or claim the maintainer confirmed a root cause.
- **Failure mechanism:** close triggers that reach similar state changes may differ in overlay event routing, animation state and dismissal callback timing.
- **Candidate regression invariant:** for each supported close trigger, verify the same declared terminal state and lifecycle callback contract; separately assert any intentionally different accessibility or navigation behavior.

### FP-08 — Modal exit animation can leave Android UI unresponsive

- **Project report:** [Reanimated issue #4422](https://github.com/software-mansion/react-native-reanimated/issues/4422) reports an Android modal with an exiting animated child becoming unresponsive, with a reproduction and a comparison where removing the exiting prop avoids it.
- **Correction, 2026-11-10:** the earlier note missed merged [PR #4776](https://github.com/software-mansion/react-native-reanimated/pull/4776), which explicitly says it fixes #4422. Its test plan uses the example and a maintainer reports successful testing. This audit did not independently reproduce the defect or fix; the reporter's animation/teardown explanation remains separate from verified patch behavior.
- **Candidate checks:** after close, assert focus/input/interaction recovers; test animation enabled/disabled and supported Android/runtime combinations. The failure oracle should test user-visible responsiveness rather than only component state.

### FP-09 — Stale success response overwrites the latest VueUse `useFetch` state

- **Project evidence:** [VueUse issue #5571](https://github.com/vueuse/vueuse/issues/5571) gives a two-request reproduction: request A starts first and is slow; request B starts later and resolves first; then A resolves and overwrites B's state.
- **Path drift detail:** [PR #5574](https://github.com/vueuse/vueuse/pull/5574) says a prior fix guarded the error handler against superseded requests but the success handler lacked equivalent guards. Parsing and `afterFetch` awaits widened the window before assigning response/status/data.
- **Resolution/test:** PR #5574 merged on 2026-08-13. The fix checks the execution counter before each success-state assignment. This is direct project history; no local VueUse tests were run.
- **Failure mechanism:** related success/error branches had inconsistent stale-result protection. This resembles the video’s path-divergence concern, but the duplication diagnosis is not required: the key issue is an incomplete behavioral invariant across asynchronous completion branches.
- **Candidate regression invariant:** once a newer request supersedes an older generation, no completion branch or post-response asynchronous transform from the older request may update user-visible state. Resolve requests in both orders and include a delay during body parsing/hooks.

### FP-10 — Concurrent payment paths and database retry can charge the card more than once

- **Project evidence:** [Odoo payment-Adyen PR #153792](https://github.com/odoo/odoo/pull/153792) describes the notification webhook and payment controller concurrently updating the same row. An SQL concurrency failure triggers a retry; without idempotency, the remote Adyen payment could be issued again.
- **Resolution:** the PR adds an idempotency key derived from transaction reference and database UUID to the payment request.
- **Reproduction limit:** the PR explicitly says the issue was not reproducible against the available Adyen test account. Treat this as a project-reported race and fix rationale, not a confirmed reproduced duplicate charge in this research.
- **Candidate regression invariant:** a database conflict/retry around a remote payment must not create a second charge. Test the local retry boundary with a provider simulator that records effects, then separately validate the real provider’s idempotency contract and key scope.

### FP-11 — A webhook deduplication rule can suppress a legitimate retry after a failed attempt

- **Project report:** [PRAHO issue #234](https://github.com/captainpragmatic/PRAHO/issues/234) says duplicate detection returns HTTP 200 for any previously seen event ID even when its prior handler status is `failed`, so a sender retry is acknowledged without reprocessing.
- **Scope correction in the issue:** its validation update notes that internal retries are separately scheduled; it narrows the claim from permanent data loss to sender-driven redelivery being skipped. Preserve this correction.
- **Status:** fetched page identifies a completed issue, but this pass did not inspect a linked patch or regression test to establish the exact resolution.
- **Failure mechanism:** deduplication must distinguish “effect completed” from “attempt observed.” A blanket duplicate rule can trade duplicate effects for lost work.
- **Candidate regression invariant:** same event ID in `processed` state is idempotently acknowledged; in `failed` or eligible `pending` state it follows the documented recovery path; concurrent claims still produce at-most-once effects.

### FP-12 — A transport test manufactured its own intermittent failure

- **Project evidence:** [llxprt-code PR #3100](https://github.com/vybestack/llxprt-code/pull/3100) fixes a flaky abrupt-response canary. The fixture wrote a partial response then scheduled an upstream socket reset using `setImmediate`; that only ordered one event loop, not the separate Node monitor’s forwarding or the downstream client's parsing.
- **Resolution/test:** merged PR #3100 waits for downstream HTTP 200 and the exact partial body before causing the reset; it rejects clean completion and pre-header errors, then asserts one-request telemetry and cleanup.
- **Failure mechanism:** test fixture timing implied a cross-process ordering guarantee that did not exist, causing a synthetic status 0. The test was nondeterministic because its synchronization point was in the wrong process/event loop.
- **Candidate regression invariant:** synchronize on the observation that makes the next fault meaningful; assert the intended observable failure, not merely local scheduling. Test the harness under varied host scheduling, and check cleanup on every exit path.

### FP-13 — A declared unique database index did not match the migrated database

- **Project report:** [open-mercato issue #7155](https://github.com/open-mercato/open-mercato/issues/7155) reports webhook deduplication failing because the actual database had a plain index while entity metadata and the schema snapshot declared it unique. The report says it reproduced duplicate rows and processing runs on a local `develop` environment and identifies a migration whose `up` direction drops uniqueness.
- **Status:** the fetched page was closed, but this research pass did not inspect the closing patch/history or independently query the database; the diagnosis and reproduction remain attributed to the reporter.
- **Failure mechanism:** source declarations, generated snapshots and deployed/migrated schema drift can disagree while code generation appears clean. Unit tests against mocks or metadata alone may not exercise the actual database constraint.
- **Candidate regression invariant:** after fresh install and upgrade, query the database catalog for the expected unique constraint; concurrently claim the same logical event twice and assert one processing owner. Run this against the supported database engine, not only an in-memory substitute.

### FP-14 — A practitioner asks how to prevent duplicate scheduled payouts

- **Direct community source:** [r/brdev thread](https://www.reddit.com/r/brdev/comments/1wt7s58/como_voc%C3%AAs_garantem_idempot%C3%AAncia_em_webhooks_de/) (Portuguese; Reddit displayed it as about one month old at retrieval). The author asks how to prevent repeated payments in an automatic third-party payout flow scheduled for D+3 when either a webhook or cron can run twice.
- **What replies add:** visible replies suggest a durable intermediary record with a unique key/status, an outbox and/or an advisory lock; one commenter warns that event webhooks can be delayed or out of order and suggests reconciling current provider state. Advice is mixed and not validated by this thread. Only the loaded comments were read; the previously stated total of 20 comments was not independently confirmed during the later audit.
- **Cross-check:** Stripe's [webhook delivery documentation](https://docs.stripe.com/webhooks#handle-duplicate-events) says duplicate deliveries may occur, and events are not guaranteed to arrive in creation order. It recommends event IDs for duplicate-delivery handling and describes retrieving current objects. This verifies Stripe's documented behavior only; it does not establish the Reddit author's exact payment-provider behavior or validate any one architecture.
- **Assessment value:** this is a design question, not a firsthand report of a duplicate payout. Keep it as a practitioner vocabulary/risk lead, not defect-frequency evidence.

### FP-15 — Hover/animation state remains stuck after a video modal closes

- **Direct community report:** [r/webdev thread](https://www.reddit.com/r/webdev/comments/uup45b/anyone_know_why_my_modal_is_causing_my_css/) (Reddit displayed it as about five years old at retrieval). The author reports a card overlay remaining in its hovered position after closing a video modal until they hover and leave again, and includes the related CSS transform/transition.
- **Status:** one user symptom with an implementation fragment; the thread had no comments in the inspected page. No root cause or fix was established.
- **Research value:** close to the supplied video because modal lifecycle and pointer/hover state interact with animation. It still does not establish duplicated close handlers. A focused follow-up would record pointer position, focus, hover target, animation completion, modal unmount and pointer re-entry.

### FP-16 — Repeated writes inside one transaction leave phantom database index entries

- **Project evidence:** [ArcadeDB issue #4935](https://github.com/ArcadeData/arcadedb/issues/4935) and merged [PR #4964](https://github.com/ArcadeData/arcadedb/pull/4964) describe an ordinary transaction that changes one indexed value `original → intermediate → final`. Each save diffed against the committed record buffer, which stays unchanged until commit; the intermediate index entry survived. A unique index could then reject a legitimate insert of the intermediate value, while a non-unique index could return a stale entry.
- **Fix and tests:** the patch keeps the last in-transaction indexed state per record and diffs the next write against that state. The PR includes tests for double/triple updates, unique and non-unique/composite indexes, list deltas, in-place mutation and update-then-delete sequences; the audit inspected the PR test patch but did not rerun it. This is project-level evidence from the merged change; this research did not rerun ArcadeDB's suite.
- **Failure mechanism:** a sequence of individually plausible operations violates the final committed index invariant because each operation's comparison baseline is stale. A test that only inserts once or updates a row once would miss the sequence.
- **Candidate invariant:** after every committed sequence, every index lookup and uniqueness check agrees with the final row state; repeat the assertion after rollback and update/delete histories, with actual index contents checked rather than only successful API returns.

### FP-17 — Firmware factory reset fails only when cleanup runs after Bluetooth shutdown

- **Project evidence:** [Meshtastic issue #10851](https://github.com/meshtastic/firmware/issues/10851) and merged [PR #10873](https://github.com/meshtastic/firmware/pull/10873) document an nRF52 factory-reset failure. The issue proposed a reset-API/SoftDevice mismatch, but the PR's hardware investigation says the reset path still used `NVIC_SystemReset()`; the reproduced failure instead followed `disableBluetooth()` happening before reset cleanup that can perform flash-backed work.
- **Fix and verification:** the patch delays Bluetooth shutdown until cleanup finishes. The PR reports a failed and passing factory-reset attempt on the same nRF52840 bench target, builds and uploads the firmware, and records that the repository's native test script could not run on that macOS checkout. A branch name containing `codex` does not by itself establish how the patch was authored.
- **Unresolved artifact-size signal:** the PR's generated size report says 21 of 22 targets increased, with a net increase of 363,748 bytes versus `develop`. The PR explanation and retrieved diff do not establish that the behavior fix caused that increase; the subsequent audit verified these figures in the PR’s automated size-report comment, not by rebuilding the firmware. Keep it as a release-artifact anomaly to investigate, not a causal claim; compare same-toolchain artifacts and identify changed sections before attributing it.
- **Failure mechanism:** a user-visible reset is a multi-stage path—radio shutdown, cleanup, flash erase, reboot—whose ordering and hardware state matter. Testing only the reset API or a normal reboot misses the failure path. This case also shows why fixing behavior and checking size/resource budgets are separate evidence obligations on firmware.

### FP-18 — Release artifacts failed at publish time although ordinary CI was green

- **Project evidence:** [Pydantic AI issue #7397](https://github.com/pydantic/pydantic-ai/issues/7397) reports a release blocked when an unpinned `hatchling` update changed wheel/sdist metadata to a version rejected by the publishing validator. Ordinary test/lint/typecheck CI did not validate the built artifacts; the failure appeared on a release tag.
- **Fix and tests:** build constraints pinned the incompatible backend range, and merged [PR #7414](https://github.com/pydantic/pydantic-ai/pull/7414) adds `uvx twine check --strict dist/*` after `uv build --all-packages` on each PR/push. This checks artifact metadata against the publish validator; it does not prove the entire live publishing transaction will always succeed.
- **CI-history correction, 2026-11-10 audit:** the issue claimed ordinary CI did not run the all-packages build, but the [PR parent workflow](https://github.com/pydantic/pydantic-ai/blob/0a42080ddb72d7e1610b7ba4ec449a9707c0734d/.github/workflows/ci.yml#L136-L137) already contains `uv build --all-packages`; [PR #7414](https://github.com/pydantic/pydantic-ai/pull/7414) adds artifact validation. This resolves the immediate parent-versus-PR question; it does not establish every earlier branch configuration.
- **Failure mechanism:** repository checks exercised source and package build steps without checking the release artifact's consumer-facing validity. The build was successful while the produced artifacts violated the publication contract.
- **Candidate invariant:** build the same artifact shape used for release, run the relevant validator against it before tagging, and preserve provenance for toolchain inputs. Add publication and installation smoke tests only where their cost and credentials are appropriate.

### FP-19 — Generated/deployed files drifted from their source while the checked gate watched different paths

- **Project evidence:** [Microsoft APM issue #1716](https://github.com/microsoft/apm/issues/1716) records a deployed `.agents/skills/` copy that lacked content present in its `packages/` source. Its report says CI disabled the only install-replay drift check, the committed lockfile tracked another deployment target, and a fallback path watch omitted `.agents/`.
- **Correction, 2026-11-10 audit:** [PR #1714](https://github.com/microsoft/apm/pull/1714) re-synced deployed files as a stopgap. The later merged [PR #1718](https://github.com/microsoft/apm/pull/1718) introduced target-aware drift checking, content-integrity handling and a full `apm audit --ci` gate, and added tests for divergent versus matching deployed skills. Its author reports source/deployed tampering traps and passing checks. The earlier “durable gate unresolved” note missed this PR. This audit inspected the PR and selected test/CI diffs but did not rerun the tests or verify every detail of the issue’s original end-to-end acceptance scenario.
- **Failure mechanism:** repository source, generated/deployed copies, target-specific lockfiles and CI watch paths are separate artifacts. Checking one representation does not prove the one shipped or loaded is current.
- **Candidate invariant:** regenerate or replay each supported target, compare every committed/deployed output against its declared source and target-aware lock data, and include a test that deliberately introduces drift and observes gate failure.

### FP-20 — A runtime upgrade remained slower for an important consumer workload after a partial fix

- **Project evidence:** the Erlang/OTP team discussion in [issue #8322](https://github.com/erlang/otp/issues/8322) reports up to 30% slowdowns in RabbitMQ tests when moving from OTP 26 to OTP 27-era code. Maintainer comments connect part of the regression to virtual-heap accounting and garbage-collection behavior; the issue's history spans multiple fixes and reproductions.
- **Resolution boundary:** merged [PR #8347](https://github.com/erlang/otp/pull/8347) says it improves the affected cases but does **not** fully restore prior performance. Its CI comment reports a large Common Test run with no failures, while the PR body still describes residual slowdown. Passing thousands of tests did not itself demonstrate performance parity for dependent workloads.
- **Failure mechanism:** runtime/compiler changes can interact with application-specific allocation patterns and parameters; a microbenchmark or green functional suite does not cover all consumer workload behavior. Even a regression test may only lock in a local case, not universal performance characteristics.
- **Candidate invariant:** preserve versioned, repeatable end-to-end workloads from representative downstream users and report latency/throughput/resource distributions, environment and uncertainty alongside functional results. Track residual regressions rather than equating issue closure or test count with full restoration.

### FP-21 — A detailed warm-boot driver crash report remains an unverified diagnosis

- **Community/project report:** [OpenWrt mt76 issue #1148](https://github.com/openwrt/mt76/issues/1148) gives a hardware, kernel and firmware configuration for a warm-reboot MCU timeout followed by a NULL dereference in a hardware restart path. It distinguishes a prior WED-related crash from a second crash after WED was disabled, and supplies logs and a source-based explanation.
- **Status and limits:** the issue was open with no comments when retrieved. The reporter explicitly says the fault trace is source-pinned rather than binary-pinned and offers a possible fix rather than a tested patch. The detailed account is valuable for a specialized failure search, but remains a single attributed report with no independently confirmed root cause or fix.
- **Research value:** a workaround can remove one fault signature while exposing another failure in the same initialization/recovery sequence. Preserve trigger, board, firmware, kernel, warm-versus-cold boot, compile configuration and diagnostic uncertainty when devising a reproduction.

### FP-22 — Browser Escape and backdrop click take different native-dialog close paths

- **Direct Stack Overflow report:** [question #79787635](https://stackoverflow.com/questions/79787635/why-does-this-dialog-modals-css-slide-out-animation-jump-to-the-top-of-the-page) describes an HTML `<dialog>` opened with `showModal()`. Escape closes through the browser's native cancel behavior; the separately written backdrop click handler calls `dialog.close()` immediately. The author reports the dialog jumps instead of playing its exit animation on Chrome and Edge 141, especially with rapid open/close, and says the behavior also affects the MDN example.
- **Answer boundary:** the accepted answer delays `close()` until `animationend`; another answer proposes discrete transitions for `display`/`overlay`. The question has no comments or author-confirmed follow-up in the inspected API record, so neither answer is treated as a verified cross-trigger or browser-wide fix.
- **Mechanism:** native Escape/cancel and custom click handlers can bypass one another's lifecycle code. This is a particularly close analogue to the supplied video: both paths are expected to close the same modal, but event origin determines whether the animation finishes.
- **Candidate invariant:** Escape/cancel, backdrop, close button and programmatic closure follow an intentional shared state transition, or explicitly documented variants. Test each path, rapid reopen, cancelled/missing animation events, reduced-motion settings and supported browsers; assert the visible state and focus restoration, not just `open === false`.

### FP-23 — A duplicate-webhook answer may miss concurrency and recovery semantics

- **Direct Stack Overflow question:** [question #79998813](https://stackoverflow.com/questions/79998813/how-can-i-prevent-duplicate-webhook-events-from-being-processed-in-laravel) (created 2026-08-27 UTC) asks how to handle repeated payment webhook delivery reliably when requests can arrive concurrently. It is a design question, not a confirmed duplicate-payment incident; it has two answers and none is accepted.
- **Answer boundary:** answers suggest storing event IDs and using a unique database key. The inspected snippets do not establish atomic coupling between claiming an event and performing its external side effect, safe handling of a uniqueness conflict, or recovery if processing fails after the event row is inserted. A comment distinguishes idempotent final effects from whether the handler executes more than once. These are gaps in the sampled discussion, not proof that the suggested designs fail in every implementation.
- **Candidate invariant:** concurrent deliveries of one logical event cannot create multiple external effects; failure after claim/side effect/acknowledgement follows a defined recovery state machine. Test with parallel requests and injected failure at each boundary, including replay after a failed attempt.

### FP-24 — Developers disagree about AI-generated code quality and how to review it

- **Direct Hacker News discussion:** [“Is anybody producing good code with coding agents?”](https://news.ycombinator.com/item?id=49934037) had 48 descendants at retrieval. The original post describes exhausting review and reduced comprehension; five top-level comments were sampled. Replies differ: some advocate small, reviewable changes and iterative feedback; others emphasize detailed specs, architecture, and end-to-end/integration tests; one describes a harness for understanding system structure.
- **Evidence status:** these are self-selected practitioner accounts, not a measured comparison of agent quality. The variation is useful because it exposes candidate mechanisms and counterarguments: change size, reviewer context, specs, system understanding, verification design and review burden may matter together.

### FP-25 — A fuzzing-first review pitch raises concrete behavior targets but proves no detector accuracy

- **Direct Hacker News thread:** [“No more code reviews. Fuzz instead”](https://news.ycombinator.com/item?id=50412646) had one comment at retrieval. The commenter lists personally encountered examples, including non-atomic read-then-write SQLite/D1 logic that fails under concurrent requests and unbounded subrequests.
- **Evidence status:** this is one comment under a product/demo pitch, not a reproduced defect or benchmark. It contributes candidate workload and stateful fuzzing scenarios; the thread does not establish whether the proposed tool detects them or has adequate precision.

### FP-26 — A bug-finding agent must report verified bugs, not just completed flows

- **Direct Hacker News discussion:** the [Momentic application-testing thread](https://news.ycombinator.com/item?id=50339913) advertises agents that explore apps to find bugs. It had 134 descendants at retrieval; five first-level comments and one nested reply were sampled. Participants question how to distinguish finding a real bug from executing flows, and raise deduplication, replayable evidence, reproducibility, precision/recall and triage cost.
- **Evidence status:** this is product discussion and practitioner feedback, not independent validation of the tool. Numerical precision/cost claims quoted in the thread were not checked against a benchmark or methodology.
- **Candidate evaluator contract:** count unique, independently verifiable defects under a declared budget; retain repro steps, environment and evidence; distinguish “flow executed,” “possible issue,” “reproduced defect,” and “fixed regression”; report duplicate reports and false-positive/triage burden.

### FP-27 — AI-project sharing discussions contain competing quality and participation concerns

- **Direct Hacker News discussion:** [“Why people keep posting AI-generated projects around the Internet?”](https://news.ycombinator.com/item?id=50139584) had 16 descendants at retrieval; six top-level comments were sampled. Comments range from concerns about shallow domain expertise and noisy community review requests to arguments that people enjoy making and sharing projects, including work they could not previously build.
- **Evidence status:** anecdotal and value-laden, not a quality-rate sample. Preserve both sides: a future framework should investigate low-quality public releases and the value of accessible experimentation without assuming one motive or deciding that repository presence implies project intent or maturity.

### FP-28 — Escape close-request event path can differ by interaction history

- **Browser report:** [Chromium issue 41484805](https://issues.chromium.org/issues/41484805) reports that in Chrome 120 and Edge 120, pressing Escape immediately after opening a native dialog could emit close without first emitting cancel; the report says prior interaction changed the result. The reporter listed Safari and Firefox as passing for that version-specific case.
- **Corroborating project implementation:** the current [Material Web dialog implementation](https://github.com/material-components/material-web/blob/main/dialog/internal/dialog.ts) contains a compatibility path referring to a Chrome 120 issue where Escape did not trigger the expected cancel handling.
- **Status and limits:** historical/version-specific report; current browser status and independent reproduction were not established here. It is not evidence of the same cause as the video.
- **Failure mechanism:** behavior can depend on event route and history, and a handler may rely on cancel before initiating a custom exit animation or intent-specific logic.
- **Candidate regression invariant:** compare Escape immediately after open with Escape after pointer/focus interaction; assert the intended close/cancel behavior, single effect, final state, animation lifecycle and restored focus for each supported browser/version. Do not assert one exact event trace across all browsers without a versioned platform contract.

### FP-29 — Coding agents can copy insecure patterns from nearby repository code

- **Primary research:** [Coding Agents Propagate Vulnerabilities in Code Bases](https://arxiv.org/abs/2611.11455) (ETH Zurich, arXiv preprint posted 2026-11-08) compares otherwise related tasks in secure versus insecure repository contexts. It reports effects in 96 backend-generation tasks and 20 paired tasks in real C/C++ projects, including cases where insecure neighbor code increases vulnerable output. The linked [experiment repository](https://github.com/eth-sri/vulnerability-propagation) specifies the task sources, function and exploit checks, `sec_pass` measure, scripts and high storage requirements.
- **Evidence boundary:** a controlled benchmark on selected tasks, frameworks, projects and vulnerability classes; not a population estimate for all agents or codebases. The paper and artifact are new and have not been independently reproduced here.
- **Failure mechanism:** a repository's existing implementation can be a misleading exemplar. “Match local style” can preserve unsafe conventions unless semantic security requirements and the safety of precedent are checked separately.
- **Candidate regression invariant:** for security-sensitive changes, verify that code copied or adapted from neighboring paths satisfies the target invariant; exercise paired safe/unsafe context variants where feasible; and use independent semantic/security oracles instead of assuming a familiar local pattern is safe. Applicability and coverage must be tied to the language, threat model and vulnerability class.

### FP-30 — Functional tests pass while repository contribution policies are violated

- **Primary benchmark:** [SWE-CC](https://arxiv.org/abs/2610.06193) derives checkable contribution rules from 12 repositories and grades both agent trajectories and final artifacts. Its reported study covers 500 tasks and 823 scored policies; the authors report violations on 43.1% of applicable policies and nearly half of violations during intermediate execution, despite functionally correct patches in the benchmark setting.
- **Artifact details and limits:** the [repository datasheet](https://github.com/dangtruong01/swe-cc-arxiv) reports 1,759 extracted policies, 989 in scope, 2,603 authored checker tests, 529 approximate checks, 304 policies never triggered across 8,000 observed runs, and a dual-annotator audit of 150 checkers with 94.0% agreement (κ=0.72; 87.2% accepted). The sample is 12 Python repositories and 500 SWE-bench-derived tasks; some historical traces and checker-audit materials are not released, policies are a point-in-time documentation snapshot, and each configuration was run once.
- **Failure mechanism:** functional correctness is narrower than project-specific contribution quality. The agent may skip a required process, test, style rule or intermediate safety constraint without failing the task's functional tests.
- **Candidate check:** model scoped project rules as separately applicable obligations, distinguish exact/approximate/human-only checks, report triggered/untriggered/ungradable/N/A separately, and evaluate both the trajectory and final artifact where the policy governs process. Do not interpret a policy pass rate as merge readiness.

### FP-31 — Autonomous bug discovery misses many bugs maintainers later repair

- **Primary benchmark:** [PROBE](https://arxiv.org/abs/2610.35987) builds a reference set from 2,457 later-fixed bugs in 20 repositories across Python, JavaScript and TypeScript. The paper reports that its best coding-agent configuration recovers 20.8% of those reference bugs and no tested configuration exceeds 8.1% precision against the reference.
- **Oracle limitation:** the reference contains bugs maintainers chose to fix during a finite future window, not every true defect. The authors estimate that even a perfect finder could achieve only 26–47% precision against that partial reference; a separate human/LLM judgment considers many unmatched reports valid. Exact issue matching, expert validity and operational usefulness are different outcomes.
- **Artifact boundary:** the paper names `LogicStar/probe`, but the bounded GitHub search returned no result and the contents API returned 404. Dataset/repository availability is unresolved and the benchmark was not run.
- **Candidate evaluation:** score recall against a declared reference and separately review unmatched findings for validity, novelty, severity and actionability; report an oracle ceiling/uncertainty when unfixed defects are unobservable. Keep triage burden and reproducibility in the measure.

### FP-32 — Agent quality problems are visible as user correction, not only failed tests

- **Primary observational study:** [How Coding Agents Fail Their Users](https://arxiv.org/abs/2605.29442) analyzes 20,574 IDE/CLI sessions across 1,639 repositories and codes observable developer pushback along symptom, cause, cost and resolution. It reports seven recurring forms, 90.50% of episodes incurring effort/trust cost rather than irreversible damage, and explicit correction in 91.49% of the subset with visible resolution.
- **Evidence boundary:** conversationally visible pushback is the study's unit, not all silent or unobserved errors; it is an observational analysis of selected session corpora, not a causal or universal product comparison. Reported extraction precision, inter-rater agreement and LLM-judge accuracy do not remove selection or labeling uncertainty.
- **Candidate evaluation:** pair task outcome with user correction, review/rework, action constraint, communication accuracy and trust cost; preserve interaction context and follow-up turns. A one-shot benchmark cannot by itself capture changing requirements or whether the developer had to repair the agent's result.

### FP-33 — A sequence of individually plausible changes can fail as a system evolves

- **Benchmark evidence:** [LoopsBench](https://arxiv.org/abs/2608.00267) models dependency-linked development units and retains completed units as regression obligations. [CrossSWE](https://arxiv.org/abs/2611.01484) evaluates coordinated changes across multiple repositories and reports cross-repository inconsistency as a major failure class. [EvoClaw/SWE-Milestone](https://arxiv.org/abs/2603.13428) evaluates continued development across milestone histories and reports much lower performance in its continuous setting than in isolated tasks.
- **Evidence boundary:** these are new benchmark papers with different tasks, models, harnesses and oracles; their percentages cannot be compared directly or treated as production defect rates. The LoopsBench README exposes checksummed tasks and task-validation workflows; code and CI internals were not audited here. EvoClaw's alternate GitHub read route failed and its paper/README repository identity needs reconciliation.
- **Failure mechanism:** flat issue-resolution tests may not preserve obligations created by earlier changes, compatibility across component/repository interfaces, or behavior that must remain correct throughout a long sequence.
- **Candidate evaluation:** retain per-milestone tests and prior regression obligations, record dependency/interface edges, test combinations of adjacent work, and compare final behavior with intermediate state. Build applicability from the actual system graph; a DAG is useful only when dependencies can be represented and validated.

### Practitioner lead — repeated payment submissions and webhook retries are separate boundaries

A connected X thread posted 2026-11-08 uses four rapid checkout clicks as an example of duplicate charging; replies distinguish disabling a button from payment idempotency and note that a retried webhook is a separate duplicate-effect path. This is an anecdotal design discussion, not a verified incident or independent corroboration. It is linked to the stronger, separate project and provider evidence in FP-10 and FP-23 as a vocabulary/source lead only.

### Provider-specific webhook contract observed in official Stripe documentation

The current Stripe pages fetched on 2026-11-10 describe automatic retries for up to three days in live mode, exponential backoff, duplicate deliveries, and no guarantee that generated events arrive in order. They say to track event IDs for duplicate deliveries and to retrieve current objects when needed. These are Stripe's documented semantics, not a global webhook standard.

Stripe's API v1 [idempotent request documentation](https://docs.stripe.com/api/idempotent_requests) further scopes the mechanism: results are saved after endpoint execution begins, repeated parameters must match, and keys can be pruned after at least 24 hours; reusing a pruned key can create a new request. The page distinguishes API v2 behavior. That means a retry test should model key scope, persistence and expiry, concurrent in-progress requests, and provider version instead of assuming the phrase “idempotency key” alone guarantees safe replay forever.

### Platform conformance-test evidence: dialog requestClose and lifecycle

The current [Web Platform Test for dialog.requestClose](https://github.com/web-platform-tests/wpt/blob/master/html/semantics/interactive-elements/the-dialog-element/dialog-requestclose.html) records event order and distinguishes synchronous cancel from queued close; it varies opening method and closedby settings. A second [WPT closedby/start-open test](https://github.com/web-platform-tests/wpt/blob/master/html/semantics/interactive-elements/the-dialog-element/dialog-closedby-start-open.html) exercises focus restoration that synchronously reopens a dialog, followed by additional close requests. The [CloseWatcher test README](https://github.com/web-platform-tests/wpt/blob/master/close-watcher/user-activation/README.md) explains intentionally different event scheduling when several native dialogs are involved.

This is conformance-test evidence, not proof of a product bug. It shows that a meaningful UI test can need event ordering, task scheduling, nested ownership, detached nodes, focus reentrancy and no-crash assertions in addition to checking visible state. The WHATWG requestClose/CloseWatcher discussion was closed after a merged spec change; see [issue #11230](https://github.com/whatwg/html/issues/11230), [merged PR #11326](https://github.com/whatwg/html/pull/11326), and [WPT crash-test PR #52020](https://github.com/web-platform-tests/wpt/pull/52020). Standards, implementation changes and tests must be kept version-aligned.

## Cross-case synthesis

These sources support several **candidate failure families**, not one universal “duplicate code” defect:

1. **Trigger-to-contract drift:** click, key, system Back, timer, API, retry or callback paths do not preserve the same intended result.
2. **State/lifecycle ordering:** teardown, animation completion, mount state, thread-pool scheduling or focus restoration races the event that initiated it.
3. **Propagation and ownership:** an event or callback reaches the wrong layer or owner (nested modal stack, restored opener, background service delegate).
4. **Cancellation/timeout ambiguity:** cancellation may fail to reach an internal operation; timeout may occur after an external side effect already succeeded.
5. **Environment-sensitive semantics:** IME, browser, OS, runtime and build profile alter event or scheduling order.
6. **Persistence/schema drift:** generated declarations, migrations and deployed databases disagree about constraints, so an invariant that looks present in source is absent in operation.
7. **Oracle gaps:** a test may assert that a handler ran while missing duplicate effects, wrong target, residual state, inaccessible focus, or permanently blocked interaction.
8. **History-dependent persistent state:** a transaction that performs several writes may leave an index or event cursor inconsistent even though each individual write appears valid.
9. **Artifact-boundary gaps:** product source, generated/deployed copies, built release artifacts and target-specific metadata can diverge while a different path stays green.
10. **Domain lifecycle and resource tradeoffs:** hardware reset order, flash/power behavior, runtime upgrades and dependency transformations can affect outcomes only under a specific device or downstream workload; behavior, performance, footprint and build cost may move independently.
11. **Test-tool claim drift:** a tool that reports flows executed or raw findings may not establish unique, reproducible defects; deduplication, evidence quality, oracle validity and triage cost are part of the measurement.

The strongest conclusion from this small batch is a **research and test-design inference**: identify the externally meaningful intent and its invariants; enumerate supported triggers and operation histories; then compare the result, side effects, state, timing and environment where relevant. Code-sharing/clone detection may help investigate drift, but it does not prove two paths ought to be identical and cannot substitute for behavioral oracles.

## Candidate test-design recipe (not yet a universal gate)

For one selected behavior, record:

1. **Contract:** preconditions, accepted triggers, allowed differences, state transition, postconditions, side effects and recovery behavior.
2. **Model:** the smallest state machine that captures the relevant states and actions, including cancellation, repeated input, nested/parallel actions, teardown, retry and reopen where applicable.
3. **Path matrix:** entry/exit trigger × current state/depth × animation or asynchronous mode × focus/ownership × cancellation/timeout × supported platform/build. Prune combinations using applicability and risk rather than blindly requiring every product cell.
4. **Oracle:** compare observable behavior and side-effect counts, not only code coverage or that a callback was called.
5. **Sequences:** include competing triggers, rapid/repeated/cancel/reopen, failure after remote commit but before acknowledgement, and schedule-controlled races when those apply.
6. **Regression capture:** when a defect is observed, keep a minimal reproduction and a test that fails before the fix and passes after it, where feasible.
7. **Tool limits:** state the state space explored, runtime/environment, seeds, time budget, unknowns, and whether the test uses mocks that could remove the failure mechanism.

For systems that publish or transform artifacts, add a separate release/deployment path: build the exact target, compare generated/deployed files against their authoritative source, validate the artifact with downstream tooling, and record resource-size/behavior deltas. For upgrades and optimizations, include representative downstream workloads and uncertainty; ordinary functional suite counts do not establish performance parity.

Hypothesis' [stateful testing guide](https://hypothesis.readthedocs.io/en/latest/stateful.html) describes generating action sequences and checking the implementation against a simpler model; this is relevant when failures depend on history, though it is not necessary for every small interaction. Ba et al.'s [USENIX Security 2022 Stateful Greybox Fuzzing](https://www.usenix.org/conference/usenixsecurity22/presentation/ba) explains why reactive protocols may need event/message sequences to reach bug-triggering states and why the absent/weak specification is itself a challenge. These methods need meaningful state models or oracles, resource limits and shrinking/reproducibility; they do not guarantee exhaustive behavior.

Compiler testing gives another example of why high-risk system checks need domain-specific oracles. Heo et al.'s [PLDI 2025 Optimuzz paper](https://kihongheo.kaist.ac.kr/publications/pldi25.pdf) discusses an optimization bug existing unit tests failed to detect for months and evaluates targeted compiler fuzzing/translation validation against known LLVM and TurboFan miscompilations. The authors report reproducing 23 known bugs in one experiment and report new LLVM findings. These numbers describe that paper's tool/benchmark setup, not compiler testing generally. The method implication is to connect each failure class to the domain's semantic oracle (for a compiler, compare program behavior across transformations), rather than reuse a generic repository checklist.

Mutation testing can probe whether tests react to selected changes, but a mutation score is not proof of real-world fault detection. Stryker's [documentation](https://stryker-mutator.io/docs/) explains killed/surviving mutants and the distinction from code coverage; effectiveness also depends on mutant operators, equivalent mutants and test oracles. Consider it as an optional diagnostic, not an automatic pass threshold.

## Duplication evidence and counterevidence

- The video's proposed explanation is plausible, but not proven for that video.
- Bettenburg et al.'s [release-level clone-change study](https://users.encs.concordia.ca/~shang/pubs/bettenburg-wcre09.pdf) studied two OSS Java systems and found only a small number of inconsistent clone changes associated with defects in that sample. Its small, dated, two-project scope prevents broad generalization, but it contradicts “every duplicate is automatically a bug.”
- Kapser and Godfrey's [“Cloning Considered Harmful” Considered Harmful](https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf) describes cases where cloning supports understandability, independent evolution or avoids a poor abstraction. This is reasoned empirical/qualitative work, not proof that clones are low risk.
- Cross-language clone work reports tradeoffs and false positives/negatives for structural and nominal approaches; see [Nichols et al., Structural and Nominal Cross-Language Clone Detection](https://www.cs.ucsb.edu/sites/default/files/documents/nichols19structrual.pdf). A detector’s result depends on its representation, thresholds, language and definition of “clone.”
- A 2026 MSR paper, [More Code, Less Reuse](https://dl.acm.org/doi/full/10.1145/3793302.3793622), reports higher semantic redundancy for AI-authored PRs in its chosen AIDev-derived sample, but performs computational redundancy analysis on a 617-PR CrewAI case subset and uses a proposed metric. Treat the finding as a scoped result requiring methods/validity appraisal, not evidence that all AI code duplicates logic or that a universal clone gate is sound.

Therefore any future clone-oriented gate must specify the clone type, target scope, intended decision, precision/recall evidence, exceptions for generated/vendor/test/forked code, remediation cost and a human review path. First-party or research claims about detector performance still need independent or project-specific validation.

## Sources and research boundary

Detailed run IDs, exact queries, result windows, opened-source counts and route limits are logged in [`../../search-log.md`](../../search-log.md) under `METH-*`, `FAIL-*`, `X-*`, `REDDIT-*` and `STRIPE-*`; the ledger rows point to those sections.

This pass used Parallel's ranked web search/fetch, Exa discovery, official/project pages, one Stack Overflow question, connected X search, and direct read-only Reddit search/thread views in Brave. It did **not** establish complete Reddit or Stack Exchange sampling, or broad language/region coverage. Search result windows are discovery samples; they are not unique-source counts or platform coverage. Reddit's own search surfaced an AI-generated answer panel; it was treated as a lead list and the underlying posts/comments were opened instead. Several issue reports are unresolved or unverified and must stay that way in later synthesis unless their linked history changes the evidence.
