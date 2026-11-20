# DCF L3901: trimming Hi-C anchors does not bring the potassium signal back. Micro-C shows it for pore-forming K+ channels only (1 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 20 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3901_resolution.txt`.
- **Script:** `rounds/dcf_assay_L3901.py`, the L3897 script with seed 3901. `TAG@W` trims each anchor to its central W bp.
- **Outputs:** `L3901_tool_output_TRIM.txt` and `_MICRO.txt`, committed before grading.
- **Grading:** `L3901_grade_output.txt`.

**Cells:** H1 + HFFc6, 4DN union loops. Not blind to the cells.

---

## Results
| # | prediction | result |
|---|---|---|
| R1 | Hi-C, anchors trimmed to 1 kb: K+ p_upper < 0.05 | **FAIL**, p = 0.50 |
| R2 | Micro-C: K+ p_upper < 0.05 | **FAIL**, p = 0.18 |
| R3 | Micro-C: pore-forming K+ p_upper < 0.05 | **PASS**, p = 0.043 |

**1 of 3 passed.** The failures stand.

Each cell gives the family share, then the matched-gene null mean, then p_upper.

| loop set (H1 + HFFc6) | K+ (96) | pore K+ (79) | all (139) | K+ auxiliary (17) |
|---|---|---|---|---|
| CTCF ChIA-PET (L3897) | 0.313 vs 0.233, **p 0.022** | 0.329 vs 0.236, **p 0.015** | 0.320 vs 0.236, **p 0.006** | 0.235 vs 0.227, p 0.51 |
| Micro-C, 50,273 / 79,625 loops | 0.635 vs 0.595, p 0.18 | 0.677 vs 0.597, **p 0.043** | 0.608 vs 0.604, p 0.48 | 0.441 vs 0.586, p 0.95 |
| Hi-C (L3897) | 0.453 vs 0.456, p 0.56 | 0.475 vs 0.455, p 0.35 | 0.439 vs 0.463, p 0.77 | 0.353 vs 0.461, p 0.89 |
| Hi-C, trimmed to 1 kb | 0.427 vs 0.425, p 0.50 | 0.443 vs 0.424, p 0.36 | 0.414 vs 0.430, p 0.69 | 0.353 vs 0.430, p 0.89 |

## What it means
**R1 fails, so the pre-registered reading applies:** the Hi-C null in H1/HFFc6 is not just anchor width. Trimming to 1 kb barely changed the baseline (0.46 → 0.43), because the TSS ±5 kb window is wider than the anchor anyway. Hi-C loops simply land on a different set of places than CTCF ChIA-PET loops.

**Micro-C sits in between.** The pore-forming K+ channels are about 8 points above matched genes (p = 0.043), but the full K+ set and the all-channel set are not.

**One pattern holds in all four loop sets:**
- **Pore-forming K+ genes always come out above auxiliary K+ subunits:** 0.33 vs 0.24, 0.68 vs 0.44, 0.48 vs 0.35, 0.44 vs 0.35.
- **Auxiliary K+ subunits are never above matched genes.**

**The strongest form of the result is therefore the CTCF ChIA-PET one.** It concerns CTCF-bound loop anchors specifically, rather than any chromatin contact.

## Record
- **+1 passed, 2 failed:** 590 of 817.
- **Audit:** 257 of 344 (entry "resolution, trimmed Hi-C and Micro-C").

## Summary
- **Trimming Hi-C anchors did not restore the K+ excess,** so the Hi-C null is about which loops Hi-C finds, not resolution.
- **Micro-C, a high-resolution assay without CTCF pull-down, shows a weak excess for pore-forming K+ channels only (p = 0.043).**
- **The effect is clearest at CTCF-bound anchors,** and it is always pore-forming channels rather than auxiliary subunits.

## Potential leads for future research
- **[CTCF-bound Hi-C anchors]** Pre-register: keep only Hi-C loops whose two anchors both overlap a CTCF-ChIAPET anchor. If the excess returns, the signal is CTCF-specific.
- **[Pore vs auxiliary, formal]** Pre-register a paired test, pore share minus auxiliary share, across all 18 cell/assay sets so far. It has been in the same direction every time, but it is not yet tested.
- **[Tissue Hi-C rethink]** The colon/astrocyte/motor-neuron Hi-C positives coexist with the H1/HFFc6 Hi-C null. So the Hi-C result varies by cell, which is worth a pre-registered Hi-C-only cell panel.
- **[Manuscript 3 v1.6]** Add §3.16–3.17 (assay split, resolution). Revise the conclusion: the signal is clearest at CTCF-bound anchors and is a pore-channel property.
