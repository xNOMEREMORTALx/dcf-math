# DCF L3825: nerve-metal genes sit at CTCF loop anchors in a neural cell line too (4 of 4, blind). Calcium channel genes are again the exception
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 18 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3825_ctcf_neural.txt`.
- **Amendment:** `AMENDMENT_L3825_a.txt` (density rule, made before data).
- **Note:** `NOTE_L3825_files.txt` (which file, from Gary's ENCODE file graph and pipeline readme).
- **Script:** `rounds/dcf_ctcf_neural_L3825a.py`.
- **Grader:** `rounds/dcf_grade_L3825.py`.
- **Output:** `rounds/L3825_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3825_grade_output.txt`.

**Data:** Gary's zip "filemap": ENCODE CTCF in-situ ChIA-PET loops for SK-N-SH, experiment ENCSR514HBO, Ruan lab.

| file | replicate | loops | MD5 | use |
|---|---|---|---|---|
| ENCFF775DIU.bedpe.gz | 2, ENCODE default | 1,271,184 | ac039ab4… | **graded** (the larger, by the frozen rule) |
| ENCFF072FCN.bedpe.gz | 1 | 776,470 | 172292f8… | descriptive check |

- **Format:** 7 columns, column 7 = PET count, all intra-chromosomal, chr-prefixed names.
- **Density:** the strongest 28,270 loops were kept, as in H1 (PET ≥ 25 at the cut).

---

## Results
| # | prediction | result |
|---|---|---|
| N1 | pooled D > 0, genome-shift p < 0.05 | **PASS:** D = 0.0999, p = 0.0010 (null mean 0.007, 95th 0.059) |
| N2 | K⁺ channels above other genes | **PASS:** 0.44 vs 0.33 |
| N3 | NMDA receptors above other genes | **PASS:** 0.57 vs 0.33 |
| N4 | Ca²⁺ channels below other genes | **PASS:** 0.20 vs 0.33 |

**4 of 4 passed.**

## Three cell types side by side
| family | n | H1 stem cells | HFFc6 fibroblasts | **SK-N-SH neuroblastoma** |
|---|---|---|---|---|
| K⁺ (KCN) | 96 | 0.34 | 0.28 | **0.44** |
| Na⁺ (SCN) | 10 | 0.50 | 0.40 | 0.50 |
| Ca²⁺ (CACNA1) | 10 | 0.10 | 0.10 | **0.20** |
| HCN | 4 | 0.25 | 0.50 | 0.50 |
| NMDA (GRIN) | 7 | 0.57 | 0.57 | **0.57** |
| Na⁺/K⁺ pump (ATP1A) | 4 | 0.00 | 0.25 | 0.50 |
| Ca²⁺ pumps (ATP2A/B) | 7 | 0.57 | 0.29 | 0.43 |
| **all other genes** | 19,884 | 0.24 | 0.24 | **0.33** |
| pooled D (p) | | 0.110 (0.001) | 0.057 (0.018) | **0.100 (0.001)** |

**Replicate 1 (descriptive):** D = 0.073, p = 0.011; KCN 0.34, GRIN 0.57 and CACNA1 0.20, against 0.29 for other genes. Same directions.

## What it means
- **The CTCF-anchor excess of nerve-metal genes is not a quirk of stem cells or fibroblasts.** It repeats, blind, in a neural-like cancer line with a different lab method (in-situ ChIA-PET).
- **The "poised, silent gene" reading is weakened,** because the pattern also holds where neural genes can be active. A simpler reading: these genes sit in CTCF-bounded neighbourhoods in many cell types.
- **Calcium channel genes are below the genome-wide share in all three cell types.** That is consistent, but with only 10 genes it is still small.

## Record
**+4 passed. 556 of 764 passed, plus 3 split.** Audit **223 of 291** (entry "CTCF anchors, neural SK-N-SH").

## Summary
- **Blind in a neural cell line, the nervous system's metal-battery genes again sit at CTCF loop anchors more than other genes** (D = 0.100, p = 0.001).
- **Potassium channels and NMDA receptors lead; calcium channels are the exception in all three cell types.**
- **Manuscript 3 is updated to v0.4,** with a third cell type and a weaker "poised" interpretation.

## Potential leads for future research
- **[Calcium channel subunits]** Pre-register a larger calcium set (CACNA1 plus CACNB, CACNA2D, CACNG): below baseline in new cell types.
- **[Many ENCODE cell types]** The same frozen script can run on any ENCODE CTCF ChIA-PET loop file. Pre-register N1–N4 across several new biosamples (e.g. GM12878, K562, HepG2, a neural progenitor if available).
- **[Mature neurons]** The decisive test of the "poised" idea remains a loop map from mature neurons.
- **[Figure]** Add an SK-N-SH column to Figure 1A.
