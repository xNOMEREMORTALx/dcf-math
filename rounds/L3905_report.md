# DCF L3905: inside one assay (Hi-C), the potassium-channel excess follows CTCF-bound anchors and vanishes at CTCF-free ones (3 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3905_ctcf_bound_hic.txt`, hashed before either subset was counted.
- **Script:** `rounds/dcf_assay_L3905.py` (L3901 script, seed 3905).
- **Outputs:** `L3905_tool_output_BOTH.txt` and `_NONE.txt`, committed before grading.
- **Grading:** `L3905_grade_output.txt`.

**Cells:** H1 + HFFc6, 4DN union loops, not blind. Hi-C loops are split by whether their anchors overlap a CTCF ChIA-PET anchor from the same file.

---

## Results
| # | prediction | result |
|---|---|---|
| B1 | Hi-C, both anchors at CTCF anchors: pore-forming K⁺ p_upper < 0.05 | **PASS**, p = 0.013 |
| B2 | Hi-C, no anchor at a CTCF anchor: pore-forming K⁺ p_upper ≥ 0.05 | **PASS**, p = 0.96 |
| B3 | Hi-C, both anchors at CTCF anchors: K⁺ channels p_upper < 0.05 | **PASS**, p = 0.039 |

**3 of 3 passed.**

Each cell gives the family share, then the matched-gene null mean, then the p-value.

| Hi-C subset (H1 / HFFc6 loops) | K⁺ (96) | pore K⁺ (79) | all 139 | K⁺ auxiliary (17) |
|---|---|---|---|---|
| CTCF-bound, 16,494 / 20,476 | 0.250 vs 0.187, **p 0.039** | 0.279 vs 0.186, **p 0.013** | 0.245 vs 0.190, **p 0.034** | 0.118 vs 0.188, p 0.85 |
| CTCF-free, 10,045 / 12,219 | 0.156 vs 0.227, p 0.99 | 0.171 vs 0.227, p 0.96 | 0.137 vs 0.226, p 1.00 | 0.088 vs 0.229, p 0.98 |

## What it means
**The pre-registered reading applies (B1 and B2 pass):** within one assay, the excess follows CTCF binding.

**This explains L3897:**
- **All Hi-C loops together showed nothing** because they mix two opposite groups.
- **CTCF-bound Hi-C loops are above matched genes.**
- **CTCF-free Hi-C loops are below them.** For all 139 genes, the lower-tail p is 0.0004 (not predicted, descriptive).

**The pattern is symmetric:**
- **Nerve-metal genes are drawn to CTCF-bound loop ends.**
- **They are kept away from loop ends without CTCF.** Those are often promoter–enhancer contacts, which fits these genes being silent in H1 and HFFc6 (compare L3717: fewer active-promoter loops).

**Caveat:** the CTCF-bound subset overlaps the ChIA-PET anchors by construction, so it is not independent evidence. What it adds is the within-assay contrast.

**Auxiliary K⁺ subunits are below matched genes in both subsets.** That is the eighth loop set in which they never show the excess.

## Record
- **+3 passed:** 593 of 820.
- **Audit:** 260 of 347 (entry "CTCF-bound vs CTCF-free Hi-C").

## Manuscript 3, v1.6
- **New §3.16 "Same cells, different assays"** collects L3897, L3901 and L3905.
- **Fixes:** the section order (3.12–3.15) is fixed, and the title now says "CTCF-bound".
- **The conclusion now reads:** the primary-cell ChIA-PET negatives are best read as cell-type differences, not assay artefacts.
- **Updated:** the Discussion limitations, Summary and leads are brought up to date.

## Summary
- **Hi-C loops at CTCF anchors carry the potassium-channel excess** (pore-forming K⁺ p = 0.013); Hi-C loops away from CTCF do not, and there the genes are depleted.
- **The signal is about CTCF-bound loop ends, not the mapping method.**
- **Manuscript 3 v1.6 states this.**

## Potential leads for future research
- **[CTCF split in neurons, astrocytes, colon]** Apply the same split to the Hi-C positives using ENCODE CTCF ChIP-seq peaks for those samples. Prediction: the excess concentrates in CTCF-bound loops. This needs the CTCF peak files (bed narrowPeak) for motor neurons, astrocytes and transverse colon.
- **[Depletion at CTCF-free loops]** Pre-register that channel genes sit below matched genes at CTCF-free Hi-C loops in other cells. This is the mirror of the main result.
- **[Pore vs auxiliary, formal]** A paired test on new cell sets.
- **[Same cells, two assays]** HUVEC/HMEC Hi-C with released loops.
