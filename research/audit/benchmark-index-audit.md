# Benchmark index structural audit — 2026-11-10

Source: `research/v2/benchmarks/candidate-index-leads.csv` at this audit's repository snapshot. Reproduce with `python research/audit/check_benchmark_index.py`; its output is `benchmark-index-structure.txt`. `benchmark-repeated-paper-urls.csv` lists every exact repeated nonempty paper/reference URL with the associated record IDs and labels.

| Field | Present | Empty | Distinct exact nonempty values | Repeated exact values | Rows participating in repeats |
|---|---:|---:|---:|---:|---:|
| Benchmark name group | 612 | 0 | 533 | 78 | 157 |
| Primary paper/reference URL | 588 | 24 | 549 | 37 | 76 |
| Code repository URL | 144 | 468 | 140 | 4 | 8 |
| Dataset URL | 117 | 495 | 112 | 4 | 9 |

These are exact-string and field-population counts of source-index rows. They are not unique benchmark identities, estimates of catalog coverage, proof that 468 repositories or 495 datasets do not exist, or evidence that any source was properly read. Links can occur in other fields, use aliases, point at different versions, or refer to unrelated objects. The CSV is an identification queue, not an automatically deduplicated canonical list.

A useful counterexample to URL-only deduplication appears in four rows pointing to https://arxiv.org/abs/2505.07897: ACB-022 and H2B-012 label LongCodeBench; ACB-048 labels LongSWE-Bench; ACB-112 labels LongCodeQA. The [paper's abstract](https://arxiv.org/abs/2505.07897v3) describes LongCodeBench as an overall benchmark containing LongCodeQA and LongSWE-Bench task families. Treating the identical URL as proof that all four rows are the same assessment unit would erase the suite-versus-task-family distinction. ACB-002 and ACB-041 both label HWE-Bench and share a URL; those are duplicate candidates, but record/version/role identity still needs adjudication.

Further work: resolve paper ↔ suite ↔ task family ↔ dataset ↔ version as explicit relationships; inspect official manifests and licenses; retain multiple legitimate names and aggregation units; record matching decision, evidence and reviewer before consolidating.

An independent Luna reviewer reproduced the exact-field counts and examined two further paper groups. ACB-129 and ACB-208 both identify [CodeScope](https://arxiv.org/abs/2311.08588) but appear under different index categories; the paper describes one multilingual benchmark with multiple tasks, so these are likely duplicate suite leads with distinct index annotations, pending detailed source-row/version adjudication. ACB-151 identifies [Code-Vision](https://arxiv.org/abs/2502.11829) while H2B-126 identifies HumanEval-V against the same paper; that paper describes HumanEval-V as a subset of Code-Vision. Preserve the suite/subset relationship rather than treating the labels as exact duplicates. This review does not establish identities of the remaining rows.
