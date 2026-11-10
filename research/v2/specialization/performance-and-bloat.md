# Performance, lean design, and bloat: research track

**Started:** 2026-11-10. This is research in progress, not a universal optimization policy. Source links identify what was actually examined and what remains to be assessed.

## The question

For a specific artifact and workload, what resources does the system consume, what design or implementation contributes to waste, and which changes improve outcomes while preserving required behavior and remaining maintainable? A general framework needs a core vocabulary and specialized knowledge for each applicable language, framework, runtime, platform, workload, and deployment environment.

## Distinguish kinds of bloat

- **Source/design:** duplicated logic, unused features, unreachable paths, unnecessary abstractions, deep dependency layers, generated or vendored material mistakenly shipped, convoluted ownership, and accidental complexity.
- **Dependencies:** unused direct or transitive packages, duplicated versions, unnecessary capabilities, optional features enabled by default and supply-chain burden. A required dependency may not be used in the observed workload.
- **Build and distribution:** slow compilation, unnecessary rebuilds, oversized binaries or images, debug symbols, duplicated assets, unused frontend bundles, packaging and cold-start overhead.
- **Runtime:** excess CPU, allocations, garbage collection, copies, synchronization, syscalls, I/O, network transfers, serialization, cache misses and expensive queries.
- **Specialized environments:** GPU occupancy/transfer overhead, memory bandwidth, model inference and training costs, embedded flash/RAM/power, browser network/rendering, mobile battery and startup, databases and storage, distributed tail latency and cloud cost.
- **Maintenance and cognitive load:** unnecessary complexity, difficult interfaces, implicit coupling and over-generalization. Fewer lines or fewer abstractions are not automatically clearer.

## Evidence chain for a proposed improvement

1. State behavior and compatibility to preserve, users/workloads, hardware/runtime, build settings and data distribution.
2. Inventory entry points and uncertainty: plugins, reflection, dynamic loading, feature flags, generated code, conditional compilation, rare error paths, external consumers and public APIs.
3. Measure baseline costs with suitable tools: size, startup, throughput, latency distributions, CPU, memory, allocations, I/O, power, build time, network or cost as applicable. Separate microbenchmark from end-to-end behavior.
4. Profile representative conditions to locate bottlenecks; capture sampling method, profiler overhead and attribution limits.
5. Form and evaluate candidate changes, including algorithm/data structure, architecture, dependency choice, compiler/runtime optimizations, caching and resource management. Consider complexity, portability, accessibility, compatibility and operational tradeoffs.
6. Compare baseline and change using repeatable runs, warmup, noise controls, equivalent environments, variance or confidence where meaningful, realistic input sizes and edge conditions. Recheck correctness, public contracts and representative uses. Keep raw results and provenance.
7. Only propose a context-specific gate after choosing a relevant baseline, threshold, ownership, cost budget, noise/flake policy and exception path. No universal line-count, dependency-count, CPU threshold or score follows from this research.

## Initial evidence and mechanisms

- [Knip FAQ](https://github.com/webpro-nl/knip/blob/main/packages/docs/src/content/docs/reference/faq.md) describes graph-based detection of unused files, dependencies and exports and how it interprets dynamic imports and configuration. Need audit specific plugin and dynamic-entry limitations; output is a candidate, not proof of safe deletion.
- [cargo-machete](https://github.com/bnjbvr/cargo-machete) describes its Rust dependency detection as fast and imprecise; its source explicitly warns automatic removal may include false positives. Keep uncertain results for review.
- [cargo-bloat](https://github.com/RazrFalcon/cargo-bloat) attributes executable space, not general speed or code quality. Its own README cautions that attribution is approximate and says WASM is not supported.
- [Go PGO documentation](https://go.dev/doc/pgo) describes feeding CPU profiles from representative application runs into compilation. This is a workload-dependent optimization mechanism; a reported improvement for a benchmark set is not a guaranteed improvement for another workload.
- [NVIDIA Nsight Compute](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) documents profiling overhead, replay and clock/cache controls that can affect observed duration. GPU systems profiling and kernel profiling have different purposes; compare like with like.
- The [2025 CommonJS dependency study](https://doi.org/10.1016/j.jss.2025.112509) reports a trace-based method and an evaluation on 91 packages with strong test suites. Its estimates and outcome are bounded by the selected packages and exercised behavior; the publisher page returned 403 on direct open here, so this remains an abstract/search-result lead until the full study is read.
- A [2025 Java debloating benchmark preprint](https://arxiv.org/abs/2510.20679) reports evaluation of three tools on 59 constructed cases; its abstract identifies dynamic class loading as a source of unsoundness. This is evidence of a specific failure mode, not a blanket claim that every tool or removal is unsafe.
- A [2026 ground-truth debloating preprint](https://arxiv.org/abs/2604.17717) reports evaluating eight tools and questions proxy measures for performance/security. Only the abstract was opened; sample, benchmark construction and publication status require review.
- A [2026 study on agents and performance PRs](https://doi.org/10.1145/3793302.3793564) surfaced as a relevant lead on optimization validation; direct access returned 403. Do not rely on search-result claims until the paper and methods are opened.

## Research work still needed

Audit each tool's actual implementation, supported versions, configuration, false positives/negatives and current maintenance. Read full studies and independent comparisons. Investigate benchmark reproducibility, compiler and linker options, language-specific runtime behavior, dependency use, workload diversity, newer research and failure reports. The companion ecosystem and tooling catalogs are seeds, not endorsements or complete inventories.
