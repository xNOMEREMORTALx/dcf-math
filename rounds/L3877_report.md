# DCF L3877: the blind confirmation failed. In five primary CD4⁺ T-cell maps there is no channel-gene excess at CTCF loop anchors (1 of 4)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3877_confirm.txt`, frozen before any file map.
- **Note:** `NOTE_L3877_files.txt`, with the file maps and the biosamples, recorded before the run.
- **Script:** `rounds/dcf_confirm_L3877.py`, smoke-tested on old cells beforehand.
- **Grader:** `rounds/dcf_grade_L3877.py`.
- **Output:** `rounds/L3877_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3877_grade_output.txt`.

**Data:** ENCODE CTCF in-situ ChIA-PET, Ruan lab, primary CD4⁺ αβ T cells. The largest loop file of each experiment was used, keeping its strongest 28,270 loops.

| experiment | cells | file | loops |
|---|---|---|---|
| ENCSR106INW | memory T, 43 y | ENCFF786NNV | 622,390 |
| ENCSR345UIQ | T cells, 20 y | ENCFF937PTH | 1,669,861 (largest of 3) |
| ENCSR154MAJ | activated memory T, 43 y | ENCFF031DPV | 666,061 |
| ENCSR093CTT | activated T, 20 y | ENCFF316XYJ | 1,080,823 |
| ENCSR962FFY | activated T (IL-2 + beads), 20 y | ENCFF939ZKJ | 749,263 |

**Method:** the frozen L3869 dependence-aware test. 10,000 gene sets matched for length and local gene density are drawn, and all five cells are scored together.

---

## Results
| # | prediction | share | matched null (sd) | p | result |
|---|---|---|---|---|---|
| T1 | K⁺ channels (96), p_upper < 0.05 | 0.308 | 0.315 (0.037) | 0.58 | **FAIL** |
| T2 | all 139 genes, p_upper < 0.05 | 0.301 | 0.318 (0.031) | 0.72 | **FAIL** |
| T3 | pore-forming K⁺ (79), p_upper < 0.05 | 0.322 | 0.324 (0.040) | 0.52 | **FAIL** |
| T4 | K⁺ auxiliaries (17), no excess | 0.247 | 0.273 (0.082) | 0.63 | PASS |

**1 of 4 passed.** T4 passes trivially, because nothing shows an excess here. The failures stand.

## What it means
- **This was the clean, fully blind test, and it did not reproduce the result.** In primary T cells, channel and potassium-channel genes sit at CTCF loop anchors **no more often than matched ordinary genes**.
- **Two readings remain, and this test cannot choose between them:**
  1. **The tilt is cell-type specific.** The first ten were mostly transformed or long-cultured cell lines (stem cells, fibroblasts, cancer lines). These are fresh primary immune cells.
  2. **The earlier effect was smaller or less general than it looked,** even after the length, density and dependence controls.
- **The five T-cell sets are closely related** (one lineage, two donors), so they count as roughly one or two independent samples, not five.

## Record
**+1 passed, 3 failed. 579 of 798 passed, plus 3 split.** Audit **246 of 325** (entry "confirmatory, CD4 T cells").

## Summary
- **The pre-registered out-of-sample test failed:** no channel-gene or potassium-channel excess at CTCF anchors in five primary CD4⁺ T-cell maps.
- **Manuscript 3 (v1.1) now limits its claim to the cell types where the effect was found,** and reports this failure prominently.

## Potential leads for future research
- **[Primary vs cell line]** Pre-register: other primary, non-immune cells show no excess either (if ENCODE has CTCF ChIA-PET in primary non-immune cells), versus more cell lines showing it.
- **[Expression]** Channel genes are silent in T cells and in most of the first ten lines alike, so silence alone does not explain the difference. A test using expression (ENCODE RNA-seq of the same biosamples) could separate the two readings.
- **[Manuscript 3 framing]** Consider whether the manuscript should become a short report of a cell-type-dependent, partly replicated pattern, with the T-cell failure as a main result.
