# DCF L3953: T-cell Hi-C shows the potassium excess at CTCF-anchored loops. The T-cell exception was an assay effect, and the cell-type reading is withdrawn (2 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 23 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3953_tcell_hic.txt`.
- **Script:** `rounds/dcf_tcellhic_L3953.py` (L3909 script, seed 3953).
- **Outputs:** `L3953_tool_output_BOTH.txt` and `_ALL.txt`, committed before grading.
- **Grading:** `L3953_grade_output.txt`.

**Data (Gary's downloads, ENCODE intact Hi-C, CD4⁺ T cells):**

| experiment | cells | loops file | loops | CTCF-anchored kept |
|---|---|---|---|---|
| ENCSR335JYP | resting | ENCFF749LFC (MD5 e363179d…) | 39,071 | 14,168 |
| ENCSR836MWK | activated 36 h | ENCFF169BLJ (MD5 a6de57b2…) | 112,110 | 26,291 |

ENCSR421CGL has no loops file (void).

## Results
| # | prediction (from the cell-type reading) | result |
|---|---|---|
| X1 | CTCF-anchored loops: pore K⁺ shows **no** excess (p ≥ 0.05) | **FAIL**: 0.317 vs 0.224, p = 0.021 |
| X2 | all loops: pore K⁺ shows no excess | **PASS**: 0.449 vs 0.642, p_upper = 1.00 (a strong deficit) |
| X3 | CTCF-anchored loops: all 139 genes show no excess | **PASS**: p = 0.057 |

**2 of 3 passed.** The key prediction, X1, failed, and that failure stands.

Each cell gives the family share, then the matched-gene null mean, then the p-value.

| T-cell Hi-C (2 maps) | K⁺ (96) | pore K⁺ (79) | all 139 | K⁺ auxiliary (17) |
|---|---|---|---|---|
| CTCF-anchored loops | 0.297 vs 0.225, **p 0.041** | 0.317 vs 0.224, **p 0.021** | 0.281 vs 0.227, p 0.057 | 0.206 vs 0.228, p 0.64 |
| all loops | 0.438 vs 0.635, p_lower 0.0001 | 0.449 vs 0.642, p_lower 0.0001 | 0.450 vs 0.647, p_lower 0.0001 | 0.382 vs 0.604, p_lower 0.019 |

## What it means
**The fixed interpretation for an X1 failure applies.**
- **In T cells, the potassium excess is present at CTCF-anchored loops** when the map is Hi-C.
- **So the T-cell ChIA-PET negatives (L3877) were an assay effect, and the cell-type reading (L3917–L3933) is withdrawn.**
- **HUVEC and HMEC have no Hi-C test yet,** so their status is open.

**The same two-sided pattern as H1/HFFc6 (L3905) appears in T cells:**
- **At CTCF-anchored loops:** pore K⁺ genes are above matched genes.
- **Across all loops:** they are far below. Most T-cell Hi-C loops are not CTCF-anchored (63–77%), and those loops avoid these genes, which are silent in T cells.

**A likely reason the T-cell ChIA-PET maps missed it (fits L3929, not tested):** their anchors sit nearer gene starts. So the "CTCF" ChIA-PET loops in primary T cells may include many promoter-tied, non-structural contacts, which dilute the CTCF-boundary signal.

**Auxiliary K⁺ subunits show no excess here either.** That makes eleven loop sets in a row.

## Record
- **+2 passed, 1 failed:** 613 of 850.
- **Audit:** 280 of 377 (entry "T-cell Hi-C").

## Summary
- **CD4⁺ T-cell Hi-C (resting + activated):** pore-forming K⁺ genes sit at CTCF-anchored loops more than matched genes (0.317 vs 0.224, p = 0.021).
- **The "T-cell exception" was the assay, not the cell type.** The pre-registered cell-type prediction failed.
- **Across all T-cell loops, these genes are strongly depleted,** as at CTCF-free loops in H1/HFFc6.

## Potential leads for future research
- **[HUVEC/HMEC Hi-C]** The last primary-cell negatives. Find ENCODE Hi-C with released loops for endothelial or mammary epithelial cells.
- **[Why T-cell ChIA-PET misses it]** Pre-register: restrict the T-cell ChIA-PET loops to anchors that overlap the reference CTCF set (both ends). Prediction: the excess appears.
- **[Non-Kv vs Kv in T cells]** Check the subfamily ordering in the T-cell Hi-C CTCF-anchored loops.
- **[Manuscript 3 v2.5]** Done: the abstract conclusion and summary are rewritten; §3.25 is added.
