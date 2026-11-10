# Modal path equivalence: evidence and test design

**Date:** 2026-11-10 (Asia/Kolkata)
**Status:** standards-backed, targeted research note for the supplied settings-panel example, now cross-referenced with repository-maintainability benchmark and field-study evidence. This is not a universal UI requirement, a browser test run, or evidence that the video application's root cause was duplicated code.

## What the transcript establishes

The supplied transcript reports two user triggers for closing a settings panel: its close control and Escape. It says Escape runs the exit animation while clicking the close control does not. The speaker hypothesizes duplicated close logic. The actual video URL, source code, browser, reproduction and fix are unavailable here, so the symptom and causal explanation remain a reported example and a speaker hypothesis.

A close-button and Escape mismatch is a behavioral-path discrepancy worth testing. It is not by itself proof of code duplication: native browser dialog semantics, animation teardown, focus restoration, framework state, event cancellation, and rendering timing can also produce path-specific outcomes.

## Browser and accessibility contracts

The [WHATWG HTML dialog specification](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element) defines a close request that first fires a cancel event; if that request is not canceled, the dialog then closes. It defines HTMLDialogElement.requestClose() as a helper to consolidate cancellation and closing logic by having non-close-request affordances call the same method. In contrast, HTMLDialogElement.close() directly closes the dialog and does not first create that cancellable request path. This is a concrete browser API distinction that can explain divergent animation or unsaved-change behavior if the application routes Escape and the close button differently.

MDN documents the cancel event as a close request that may be prevented and the close event as a non-cancelable notification after closure: [cancel event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/cancel_event), [close event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close_event), and [dialog element guidance](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog). The current Chrome guidance recommends deliberate dismissal policy, using requestClose for cancellation logic, and relies on native modal behavior for Escape, focus containment, inert background and focus return when using showModal(): [Chrome dialog guidance](https://developer.chrome.com/docs/modern-web-guidance/guides/ui-components/dialog).

The [WAI-ARIA Authoring Practices modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) describes keyboard focus moving into the dialog; Tab and Shift+Tab staying within it; Escape closing it; and focus returning to the invoker or another logical workflow target when the invoker no longer exists. It also recommends a visible close button. The [W3C HTML dialog technique](https://www.w3.org/WAI/WCAG21/Techniques/html/H102) is a documented WCAG technique, not the only way to satisfy normative WCAG criteria.

For CSS transitions, MDN's [dialog animation guidance](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog#animating_dialogs) describes transitions involving display and the top-layer overlay, including discrete transition behavior. A panel that is removed, hidden, unmounted, or loses top-layer participation before its exit animation can render may look different depending on the close path. This is a test hypothesis to check in the target implementation, not a diagnosis of the supplied video.

## A browser path-divergence counterexample

Chromium [issue 41484805](https://issues.chromium.org/issues/41484805) reports a Chrome 120 / Edge 120 case where Escape immediately after opening a native dialog fired close but not cancel unless the user had interacted with the dialog first. The reporter listed Safari and Firefox as passing for the reported case. The issue record and discussion are historical, version-specific and not a current cross-browser reproduction; its present status and modern browser behavior were not independently established here.

The current Material Web dialog source contains a compatibility path referencing a Chrome 120 Escape/cancel issue: [dialog implementation](https://github.com/material-components/material-web/blob/main/dialog/internal/dialog.ts). This independently shows a mature component accounting for event-path differences. It does not establish the status of Chromium issue 41484805 or prove that the supplied video shares this cause.

The case adds an important sequence dimension: pressing Escape immediately after opening can differ from pressing Escape after a click or focus move. A test that opens a dialog, interacts with it, and only then presses Escape can miss the reported path.

### Conformance-test and standards-change evidence

The [WPT dialog requestClose test](https://github.com/web-platform-tests/wpt/blob/master/html/semantics/interactive-elements/the-dialog-element/dialog-requestclose.html) asserts the event order directly: requestClose fires cancel synchronously; close is scheduled and fires later. The test also varies opening method and closedby state, and covers close requests after changing closedby while the dialog is already open. This means an assertion only checking dialog.open can miss event-order or duplicate-callback defects.

The [WPT dialog closedby/reentrancy test](https://github.com/web-platform-tests/wpt/blob/master/html/semantics/interactive-elements/the-dialog-element/dialog-closedby-start-open.html) includes a deliberately unusual sequence: closing restores focus, focusin immediately reopens the dialog, then another close and Escape must still work. It is a concrete example of testing callbacks that synchronously change component state during lifecycle cleanup.

The WPT [CloseWatcher user-activation test notes](https://github.com/web-platform-tests/wpt/blob/master/close-watcher/user-activation/README.md) explain that grouped HTML dialogs queue close events but fire cancel events synchronously. As a result, multiple dialogs can emit both cancel events before either close event, unlike CloseWatcher events. The tests preserve this surprising but specified ordering. Nested/stacked close behavior therefore needs sequence-aware assertions rather than assumptions about per-dialog event pairs.

A newer standards-history trace also matters: WHATWG [issue #11230](https://github.com/whatwg/html/issues/11230) about requestClose and CloseWatcher lifecycle is closed. The merged [PR #11326](https://github.com/whatwg/html/pull/11326) adjusted dialog setup/cleanup around open-attribute changes and connectedness, and made requestClose return early for disconnected or not-fully-active documents. Its discussion cites the WPT suite as coverage, but also describes the cases as organically grown and not neatly organized. Earlier [WPT PR #52020](https://github.com/web-platform-tests/wpt/pull/52020) added crash tests for disconnected dialogs and documents without a browsing context after a Chrome crash report. These are conformance and lifecycle edge cases, not evidence of the original app bug.

The current standard page should be read together with issue and test history: an API description can look straightforward while a race/reentrancy edge drives spec changes, implementation crashes and new regression cases.

### Event-sequence testing research

Yuan, Cohen and Memon's [GUI Interaction Testing: Incorporating Event Context](https://cse.unl.edu/~myra/papers/YuanCohenMemon.pdf) treats GUI interactions as event sequences whose position and surrounding history matter. It notes that earlier approaches often stop at length-two/three interactions or use random longer sequences, then proposes combinatorial coverage over relationships between events in different sequence positions. The paper illustrates the scale problem: even a GUI with four events has 36 length-two sequences, more than 7,500 length-five sequences and over 60 million length-ten sequences. This is an older GUI testing method paper, not direct evidence about modern HTML dialogs or a claim that all event sequences should be run. Its useful contribution here is to justify explicit risk/interaction coverage and sequence-history modeling rather than assuming a few happy-path clicks cover stateful behavior.

The source was fetched as a primary research paper in `UI-SEQ-F01`; paper details beyond the targeted event-context/sequence excerpts have not been fully appraised.

## Behavioral contract to define before testing

For one modal feature, write down:

- Which triggers are supported: close button, Escape, platform Back, backdrop/light dismiss, a form action, programmatic close, or any product-specific trigger.
- Which triggers express the same intent and therefore share the same outcome, and which intentionally differ (for example, destructive confirmation versus cancellation, a prevented close due to unsaved changes, or a backdrop that is deliberately not dismissive).
- Expected lifecycle: open, close request, cancellation or acceptance, exit transition, final hidden/removed state, callback count, return value, and cleanup.
- Focus and accessibility: initial focus, tab order, focus containment, accessible name, Escape behavior, background inertness, and focus restoration.
- Animation policy: normal and reduced motion, animation completion/cancellation, top-layer/display timing, and what happens if the dialog reopens before the exit finishes.
- Environment boundary: target browsers, versions, OS/mobile navigation behavior, assistive technologies and rendering mode.

Do not require exact event traces to be identical for every trigger when the semantics are intentionally different. Compare the contract at the meaningful boundary: for triggers that represent the same close intent and are not prevented, verify equivalent externally observable terminal state, side effects, focus behavior and animation completion.

## High-value sequence matrix for this case

| Sequence | Why it is high value | Primary oracle |
|---|---|---|
| Open → close button | Exercises the reported route | One close transition; expected exit animation and final closed state |
| Open → Escape before any interaction | Exercises the Chromium-reported sequence | Correct cancellation/close lifecycle, final state, event count and focus |
| Open → focus or interact → Escape | Compares close-request path after activation | Same intended result as the no-prior-interaction Escape case |
| Open → Escape, then reopen before exit completes | Exercises transition ownership and stale completion | New open state survives; old completion does not close or corrupt it |
| Open → close button, then reopen before exit completes | Compares rapid-reopen behavior across routes | Same intended state and animation lifecycle as the Escape route |
| Two stacked dialogs → Escape | Exercises ownership and stack depth | Only the top actionable dialog closes; remaining dialog and focus are correct |
| Unsaved form → request close / Escape | Exercises cancellable close request | Prevented close remains open; visible explanation and focus are sensible |
| Backdrop click | Exercises configured light-dismiss policy | Closes only when policy permits; otherwise remains open without side effects |
| Reduced motion on/off | Exercises alternate animation configuration | Correct final state and accessibility behavior in both modes |
| Programmatic close and native form close | Exercises alternate APIs and framework integration | Documented return value, callback and cleanup semantics |

This list is a targeted risk sample. It is not a mandate to test all rows for every dialog: choose rows based on actual supported behavior, framework/browser semantics and harm if the path fails.

## Candidate deterministic and generative checks

A suitable implementation may use one semantic transition function or reducer, but source-code deduplication is not the contract. The durable requirement is that every supported trigger reaches the documented state machine and that equivalent intent preserves its invariants. A static clone detector can identify suspicious similarity or divergence; it cannot decide that two blocks should be shared.

A focused test approach is:

1. Model states such as closed, opening, open, close-requested, closing and closed, with an explicit cancellation branch.
2. Represent triggers as actions and mark which actions are semantically equivalent.
3. For each equivalence group, run the same preconditions and compare final visible state, animation completion, callbacks/effects, focus target and return value.
4. Generate short action sequences including immediate Escape, repeated Escape, click then Escape, Escape then click, reopen during exit, stack depth, canceled close and reduced motion.
5. In browser tests, pin browser/version and collect event traces. Keep traces as diagnostic evidence; assert user-visible outcomes as the main oracle.
6. If a bug is found, preserve a minimal reproducer and a regression test that fails before and passes after the fix where practical.

This extends the existing stateful-test and path-matrix research. It does not establish that this exact test should be a mandatory universal gate.

The WPT cases provide a particularly useful test-oracle pattern for this example: record the event list, assert synchronous state changes separately from queued close notification, and explicitly include interactions that alter dialog ownership during focus restoration. Use browser-controlled key input for Escape rather than calling the event handler directly when browser close-request semantics are under test. This is an inference from the conformance test structure; the project has not run WPT or a browser suite.

## Related repository-quality evidence, without root-cause attribution

The [NITR benchmark](../agent-quality/ai-generated-repository-maintainability-and-lab-artifacts-2026-11.md) makes behaviorally passing but structurally poor edits an explicit evaluation category. Its first 21 C++ cases include reuse/refactor probes; the authors report 64 of 483 outcomes that passed functional tests but failed structural oracles. The [More Code, Less Reuse MSR 2026 study](https://doi.org/10.1145/3793302.3793622) examines semantic redundancy in AI-authored pull requests and reports more redundant code in its selected AI sample. A separate [post-merge quality study](https://doi.org/10.1145/3793302.3793615) reports that successful merge does not guarantee quality in its sample.

These studies support investigating the transcript's proposed failure family—parallel implementations or entry paths that can drift while current behavior tests pass. They do not establish the modal application's cause, prove that a clone detector would find it, or show that every structurally similar implementation should be consolidated. For this example, the invariant remains: triggers that express the same allowed close intent should satisfy the same documented observable close contract, with appropriate input-specific focus and accessibility behavior.

## Sources and evidence boundary

Search IDs, all nine exact queries, the fetch ID and screening counts are recorded under UI-DIALOG-S01 and UI-DIALOG-F01 in research/search-log.md and research/search-ledger.csv. Eight primary/owner URLs were fetched, with no fetch errors. The additional AI-code studies and repository inspection are logged under AI-MAINT-* and GH-T3-F01. This was a focused English-language search. No browser automation, assistive-technology testing, cross-browser lab, accessibility audit, original-video reproduction, or current issue-status verification was performed.
