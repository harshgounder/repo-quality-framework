# Worked example: investigating a browser implementation

**Purpose:** demonstrate how the model generates work from a complex system. This is a first-pass research map, not an implementation specification, exhaustive browser architecture, or established conformance claim.

## 1. Brief and unknowns

Example brief: build a browser from scratch. Before setting requirements, identify intended operating systems and devices, whether existing engine components are allowed, supported web standards and extensions, accessibility expectations, offline behavior, threat model, privacy and data handling, expected user scale, release/update model, performance targets and resources. A browser shell embedding an existing engine, an independent engine, and an experiment implementing a subset have different boundaries. Until the brief is known, mark these unknown.

## 2. Recursive decomposition

Illustrative system graph:

- **Application and interaction:** windows, tabs, navigation, downloads, settings, history, bookmarks, password handling, permissions, extension UI, accessibility and localization.
- **Web content pipeline:** URL loading, character decoding, HTML parsing and tree construction, DOM, CSS parsing and cascade, style computation, layout, painting, compositing, graphics backend and display.
- **Execution:** JavaScript parsing/execution or compilation, runtime memory management, event loop, web APIs, workers, timers and cross-context messaging.
- **Network and data:** DNS, proxy handling, HTTP and TLS, cache, cookies, storage, service workers, request lifecycle and offline behavior.
- **Security and privacy:** origin and site boundaries, sandbox/process isolation, permissions, certificate validation, unsafe input handling, update integrity and privacy controls.
- **Media and platform integration:** images, fonts, audio/video, codec and DRM choices where relevant, input methods, clipboard, GPU drivers, platform accessibility APIs, printing and OS integration.
- **Engineering and operations:** build system, continuous integration, testing infrastructure, release channels, crash reporting with consent, vulnerability handling, updates, compatibility triage and long-term maintenance.

Each node can be split again: for example, CSS has parsing, selector matching, cascade, layout-related properties, animation and invalidation; media has containers, codecs, timing, hardware decode, captions and device-specific behavior. The list does not establish that every browser has the same architecture or features.

## 3. Component × contract × evidence examples

| Interaction | Questions | Candidate evidence / source families | Explicit gap |
|---|---|---|---|
| HTML parser → DOM → JavaScript | Is the tree and script-visible behavior correct under malformed input and specified ordering? | Versioned web specifications, Web Platform Tests, parser reference cases, differential testing across independent engines | No specification or suite has been fully mapped here |
| CSS cascade → layout → rendering | Are style and geometry consistent across writing modes, fonts, screen sizes and devices? | CSS specs, interoperability tests, rendering reference images, accessibility review, GPU/device matrix | No target support matrix or rendering oracle established |
| Origin → storage → process isolation | Can untrusted pages cross intended boundaries? What happens across crashes and permission changes? | Web security specifications, browser threat models, sandbox tests, fuzzing and independent review | Architectural and threat decisions remain open |
| Network → cache → service worker | Are requests and offline behavior consistent across failures, redirects, cache states and updates? | Protocol specs, conformance tests, controlled network failure experiments and privacy review | No workload or failure matrix researched |
| Media → codec → hardware → accessibility | Do playback, timing, captions and fallbacks behave on intended devices and networks? | Codec standards and test vectors, device coverage, accessibility/user studies, media performance tests | Patent/license, hardware and content rights require context |
| Engine → platform → assistive technology | Are exposed semantics and keyboard/screen-reader interactions useful for real users? | Accessibility standards, platform API guidance, automated checks and studies with disabled users | No single automated pass establishes usable access |
| Update → existing profiles → recovery | Can users safely upgrade, retain data and recover after interruption? | migration tests, rollback and interrupted-update cases, release and operational evidence | No data model or update policy specified |

## 4. Specialist and source discovery

Potential expertise includes web standards, browser architecture, parsing and programming languages, rendering and graphics, networking, OS security and sandboxing, cryptography, privacy, accessibility, internationalization, codecs and media, performance, quality engineering, release engineering, incident response, product design and legal/licensing. A person may cover multiple responsibilities; a small experiment does not automatically need a large organization.

For each component and critical edge, search official specs and their version histories, conformance tests, mature implementations and issue trackers, security advisories and postmortems, research papers and benchmarks, browser and standards communities, practitioner discussions and user studies. Search by the component's vocabulary, not only “browser best practices.” Record route, query, language, result screening, version and source limitations.

## 5. Quality and performance tradeoffs

Measure relevant behavior under realistic page sets, devices and network conditions: startup, page responsiveness, memory, CPU, battery, rendering smoothness, compatibility and accessibility. Establish baselines and distributional results before considering regression thresholds. Removing a rarely used standards feature could reduce code but break compatibility; a security boundary can add overhead; a performance change must be evaluated alongside correctness and user outcomes.

## 6. Repeat the same process for a different system

For a compiler, the chain might be source language → parser → type system → intermediate representation → optimization passes → backend → ABI/runtime, with semantic preservation and target-specific differential tests. For an exchange, it might be order entry → risk checks → matching → ledger → clearing and reconciliation, with invariants, ordering, failure recovery and applicable market rules. Their deep questions, specialists, operating evidence and sources differ; the common method is recursive decomposition and evidence discovery.

## 7. What this proves and does not prove

This map shows how the model can generate concrete research questions. It does not establish a complete browser specification, identify every standard, or provide a finished gate. The next step is to select individual nodes and interactions, locate primary specifications and specialist experience, record actual search runs, then refine this map from evidence.
