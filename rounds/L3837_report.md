# DCF L3837: the calcium-channel exception does not extend to the auxiliary subunits (0 of 2). If the dip is real, it belongs to the pore genes alone. Figure 1 updated with SK-N-SH
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 18 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3837_calcium_set.txt`.
- **Script:** `rounds/dcf_calcium_L3837.py`.
- **Grader:** `rounds/dcf_grade_L3837.py`, frozen with the pre-registration.
- **Output:** `rounds/L3837_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3837_grade_output.txt`.
- **Figure:** `figures/L3841_manuscript3_fig1_v2.png` and `.py`.

**Blindness:** not blind to the three cell types (used in L3725/L3825) or to CACNA1 (seen). **Blind to the 16 auxiliary calcium subunits** (CACNB1–4, CACNA2D1–4, CACNG1–8), which had never been looked at.

---

## Results
| cell | auxiliary (16) | all calcium (26) | other genes | D_ca | p (lower) |
|---|---|---|---|---|---|
| H1 | 0.25 | 0.19 | 0.24 | −0.043 | 0.18 |
| HFFc6 | 0.19 | 0.15 | 0.24 | −0.084 | **0.023** |
| SK-N-SH | **0.50** | 0.38 | 0.33 | +0.053 | 0.56 |

| # | prediction | result |
|---|---|---|
| C1 | auxiliary share below other genes in all three cell types | **FAIL:** below only in HFFc6 |
| C2 | full calcium set significantly below in ≥ 2 of 3 | **FAIL:** only HFFc6 (p = 0.023) |

**0 of 2 passed.** As fixed in the pre-registration, this means **the calcium exception is a pore-gene (CACNA1) property, not a property of the whole calcium-channel complex.** With 10 pore genes, that exception may still be chance.

## Record
**+0 passed, 2 failed. 556 of 766 passed, plus 3 split.** Audit **223 of 293** (entry "calcium channel set").

## Figure 1 v2
- **Panel A now has a third bar per family,** SK-N-SH (green).
- **Panel B has a third null,** recomputed with seed 3825.
- **The figure script stops unless both recomputed summaries match the committed L3725 and L3825 outputs exactly.** They do.
- While building it, I first carried the H1/HFFc6 shift range into the SK-N-SH run, and the check caught the mismatch. That was fixed before any figure was saved.

## Summary
- **The calcium-channel helper subunits do not share the pore genes' low CTCF-anchor share;** in the neural line they are well above baseline.
- **The broad "calcium channels avoid CTCF anchors" idea fails.** A narrower, pore-gene-only effect remains, unproven.
- **Manuscript 3 Figure 1 now shows all three cell types.**

## Potential leads for future research
- **[CACNA1 alone, new cells]** Pre-register CACNA1 below baseline in new ENCODE CTCF ChIA-PET cell types. Each test is small (10 genes), so pool across several cell types.
- **[Many ENCODE cell types]** Run N1–N4 of L3825 on more biosamples (GM12878, K562, HepG2 and others).
- **[Mature neurons]** Still the decisive test of the "poised" idea.
