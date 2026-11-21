# DCF L3909: in motor neurons, astrocytes and colon, the potassium-channel excess sits in Hi-C loops anchored at CTCF sites (p = 0.0008). The predicted depletion elsewhere failed (2 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3909_ctcf_split_hic_positives.txt`.
- **Script:** `rounds/dcf_ctcfsplit_L3909.py`. It uses the L3893 method: 50 matched candidates per gene, the seven maps scored together, 10,000 sets, seed 3909.
- **Outputs:** `L3909_tool_output_BOTH.txt` and `_NONE.txt`, committed before grading.
- **Grading:** `L3909_grade_output.txt`.

**Maps:**
- **Motor neurons:** ENCFF215XMY, ENCFF638CCE and ENCFF836TQT.
- **Astrocytes:** ENCFF886EVV and ENCFF424KFY.
- **Colon:** ENCFF008FXM and ENCFF259LCX.

**Reference CTCF sites:** 105,382 CTCF ChIA-PET anchors from H1 + HFFc6.

**Limitation stated in advance:** these are CTCF sites from *other* cells, used as a stand-in for shared ("constitutive") CTCF binding. No CTCF data from the neurons, astrocytes or colon were used.

---

## Results
| # | prediction | result |
|---|---|---|
| C1 | loops with both ends at CTCF sites: pore-forming K⁺ p_upper < 0.05 | **PASS**, p = 0.0008 |
| C2 | loops with neither end at a CTCF site: pore-forming K⁺ p_upper ≥ 0.05 | **PASS**, p = 0.12 |
| C3 | loops with neither end at a CTCF site: all 139 genes p_lower < 0.05 (depletion) | **FAIL**, p_lower = 0.84 |

**2 of 3 passed.** The failure stands.

Each cell gives the family share, then the matched-gene null mean, then p_upper.

| subset (7 maps) | loops kept | K⁺ (96) | pore K⁺ (79) | all 139 | K⁺ auxiliary (17) |
|---|---|---|---|---|---|
| both ends at CTCF sites | 20,015 of 39,445 | 0.141 vs 0.087, **p 0.004** | 0.154 vs 0.086, **p 0.0008** | 0.127 vs 0.086, **p 0.005** | 0.084 vs 0.094, p 0.54 |
| neither end at a CTCF site | 9,198 | 0.033 vs 0.024, p 0.10 | 0.033 vs 0.023, p 0.12 | 0.028 vs 0.023, p 0.20 | 0.034 vs 0.025, p 0.34 |

## What it means
**C1 is the strongest single result in the series for these cells.**
- **At CTCF-anchored Hi-C loops,** pore-forming K⁺ genes sit at anchors 1.8 times as often as matched genes.
- **The fixed interpretation applies:** the CTCF dependence seen in H1/HFFc6 holds in the Hi-C-positive cells, even with CTCF sites borrowed from other cells.

**C2 passes, but weakly.**
- **The CTCF-free subset is small and sparse:** the baseline is only 2.3%, and six of the seven maps keep under 1,200 such loops.
- **So "no excess" there partly reflects low power.**

**C3 fails.**
- **The depletion seen in H1/HFFc6 (L3905) does not repeat here.** If anything, the shares lean slightly upward.
- **So the mirror-image depletion is not a general rule.** It may reflect gene silencing specific to stem cells and fibroblasts.

**One map behaves differently.** Cerebellar astrocytes keep only 1,743 of 10,998 loops as CTCF-anchored, and 6,235 have no reference CTCF site at all. That map may use more non-CTCF contacts (descriptive).

**Auxiliary K⁺ subunits:** no excess, the ninth loop set in a row.

## Record
- **+2 passed, 1 failed:** 595 of 823.
- **Audit:** 262 of 350 (entry "CTCF split, Hi-C positives").

## Summary
- **In motor neurons, astrocytes and colon, the K⁺ excess sits in loops anchored at known CTCF sites** (pore-forming K⁺ 0.154 vs 0.086, p = 0.0008).
- **The CTCF-free loops show no excess,** but they are too few to say much.
- **The depletion predicted from H1/HFFc6 did not repeat** (C3 failed).

## Potential leads for future research
- **[Target-cell CTCF]** Repeat with CTCF ChIP-seq peaks from the same samples (ENCODE motor neuron, astrocyte or colon CTCF narrowPeak). That removes the proxy limitation.
- **[Muscle]** Apply the same split to the two skeletal-muscle maps (L3893: weak, p = 0.04 pore K⁺). Prediction: the excess sharpens in the CTCF-anchored subset.
- **[Primary ChIA-PET negatives]** Do T cells, HUVEC and HMEC lack the excess even though their loops are all CTCF-anchored? That makes them true cell-type exceptions. Next, check which K⁺ genes differ.
- **[Manuscript 3 v1.7]** Add §3.17 (this test) and soften the "depletion at CTCF-free loops" remark to H1/HFFc6 only.
