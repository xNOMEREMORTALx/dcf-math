# DCF L3929: primary-cell CTCF loop anchors sit nearer gene starts. This explains the higher baseline that hid the potassium excess (2 of 2)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3929_promoter.txt`.
- **Script:** `rounds/dcf_promoter_L3929.py`.
- **Output:** `L3929_tool_output.txt`, committed before grading.
- **Grading:** `L3929_grade_output.txt`.

**Measure:** the fraction of loop anchors whose midpoint lies within 5 kb of a protein-coding gene start. Each map uses 56,540 anchors.

## Results
| # | prediction | result |
|---|---|---|
| P1 | median fraction higher in the primary cells | **PASS**: 0.221 vs 0.166 |
| P2 | one-sided Mann-Whitney p < 0.05 | **PASS**: p = 0.007 |

| group | maps | fraction of anchors near a gene start |
|---|---|---|
| eight cell lines | SK-N-SH 0.194, K562 0.162, HepG2 0.167, IMR-90 0.124, HEK293 0.156, MCF 10A 0.165, BJ 0.197, RWPE1 0.181 | median **0.166** |
| seven primary-cell maps | T cells 0.235, 0.185, 0.251, 0.221, 0.292; HUVEC 0.186; HMEC 0.171 | median **0.221** |

## What it means
**The fixed interpretation applies:** the primary-cell baseline reflects promoter-proximal CTCF anchoring.

**About a third more anchors sit at gene starts in primary cells, mostly the T cells.** Every gene then has a higher chance of being "at an anchor". The K⁺ genes keep their rank (L3917) but no longer stand out. That closes the chain:
- **L3917:** same genes, higher matched-gene baseline.
- **L3921:** the higher baseline is not anchor width.
- **L3929:** it is promoter proximity.

**HUVEC and HMEC overlap the cell lines (0.186, 0.171).** Their null is therefore only partly explained this way. The T cells carry most of the effect.

## Record
- **+2 passed:** 603 of 833.
- **Audit:** 270 of 360 (entry "promoter proximity, primary cells").

## Summary
- **CTCF loop anchors in primary cells, especially T cells, sit nearer gene starts** (median 22% vs 17%, p = 0.007).
- **That raises every gene's chance of being anchored.** It explains why the same K⁺ genes no longer stand out there.

## Potential leads for future research
- **[Promoter-excluded test]** Pre-register: drop anchors within 5 kb of any gene start other than the tested gene's, and rerun the T-cell maps. Prediction: the K⁺ excess appears.
- **[HUVEC/HMEC]** Their null is not explained by promoter proximity, so look for another cause (cell-type biology).
- **[Manuscript 3]** Add §3.20.
