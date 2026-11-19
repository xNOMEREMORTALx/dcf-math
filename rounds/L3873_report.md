# DCF L3873: the potassium excess is spread across all four pore-forming K⁺ subfamilies, but not their helper subunits, and NMDA does not extend to glutamate receptors (1 of 4)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3873_glur_ksub.txt`.
- **Amendment:** `AMENDMENT_L3873_a.txt`. The frozen script crashed while building the auxiliary set, before computing any share; the recursion fix is the only change.
- **Script:** `rounds/dcf_sets_L3873a.py`.
- **Grader:** `rounds/dcf_grade_L3873.py`, unchanged.
- **Outputs:** `rounds/L3873_tool_output.txt` (the crash) and `rounds/L3873a_tool_output.txt`, both committed before grading.
- **Method:** the L3869 dependence-aware test: gene resampling matched for length and local gene density, all ten cells scored together, 10,000 sets, seed 3873.

---

## Results
| # | set | genes | ten-cell share | null mean | p (upper) | result |
|---|---|---|---|---|---|---|
| Q1 | ionotropic glutamate receptors (GRIN + GRIA + GRIK + GRID) | 18 | 0.328 | 0.268 | 0.19 | **FAIL** |
| Q2 | Kv voltage-gated K⁺ | 40 | 0.343 | 0.283 | 0.10 | **FAIL** |
| Q3 | ≥ 3 of 4 pore-forming K⁺ subfamilies above null | — | all 4 | — | — | **PASS** |
| Q4 | K⁺ auxiliary subunits above null | 17 | 0.235 | 0.257 | 0.62 | **FAIL** |

**The four pore-forming subfamilies:**

| subfamily | genes | share | null | p |
|---|---|---|---|---|
| Kv | 40 | 0.34 | 0.28 | 0.10 |
| K2P | 15 | 0.40 | 0.27 | 0.04 |
| Kir | 16 | 0.38 | 0.26 | 0.06 |
| KCa | 8 | 0.43 | 0.25 | 0.06 |

**1 of 4 passed.**

## What it means
- **The potassium-channel excess is not one subfamily.** All four pore-forming families sit above their matched controls by similar margins. Each alone is too small to be significant, but together they make the significant K⁺ result of L3869.
- **The helper subunits sit at baseline:** potassium auxiliaries here, calcium auxiliaries in L3837. A pattern seen after the fact, and only descriptive: the CTCF-anchor tilt belongs to **pore-forming channel genes**, not to the proteins that modulate them. Calcium pores are the exception, sitting *below*.
- **The NMDA excess does not generalise to glutamate receptors.**

## Record
**+1 passed, 3 failed. 578 of 794 passed, plus 3 split.** Audit **245 of 321** (entry "glutamate receptors and K+ subfamilies").

## Summary
- **All four pore-forming potassium-channel families lean toward CTCF loop anchors; their auxiliary subunits do not.**
- **Glutamate receptors as a group do not.** Manuscript 3 is now v1.0.

## Potential leads for future research
- **[Pore vs auxiliary]** Pre-register, on fresh cell types: pore-forming K⁺ genes above matched controls, K⁺ auxiliaries not.
- **[Fresh cells, L3877]** The fixed confirmatory test for K⁺ channels and the pooled set on ENCODE T-cell CTCF sets.
