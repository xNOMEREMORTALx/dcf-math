# DCF L3913: skeletal muscle shows the potassium-channel excess once Hi-C loops are restricted to CTCF sites (2 of 2)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3913_muscle_split.txt`.
- **Script:** `rounds/dcf_ctcfsplit_L3913.py`, the L3909 script with seed 3913.
- **Output:** `L3913_tool_output.txt`, committed before grading.
- **Grading:** `L3913_grade_output.txt`.

**Maps:** ENCFF735TXQ and ENCFF509PNA, scored together. The reference CTCF sites are the H1 + HFFc6 proxy, as in L3909.

## Results
| # | prediction | result |
|---|---|---|
| D1 | CTCF-anchored loops: pore-forming K⁺ p_upper < 0.05 | **PASS**, p = 0.010 |
| D2 | CTCF-anchored loops: K⁺ channels p_upper < 0.05 | **PASS**, p = 0.028 |

Each cell gives the family share, then the matched-gene null mean, then p_upper.

| muscle | loops | K⁺ (96) | pore K⁺ (79) | all 139 | K⁺ auxiliary |
|---|---|---|---|---|---|
| all loops (L3893) | 13,869 | 0.240 vs 0.203, p 0.18 | p 0.042 | p 0.21 | n.s. |
| CTCF-anchored (L3913) | 8,309 | 0.182 vs 0.121, **p 0.028** | 0.203 vs 0.120, **p 0.010** | 0.162 vs 0.122, p 0.064 | 0.088 vs 0.124, p 0.74 |

**The fixed interpretation applies (D1 and D2 pass):** muscle behaves like the other Hi-C positives once loops are restricted to CTCF sites. The weak muscle result in L3893 came from mixing in non-CTCF loops.

## Record
- **+2 passed:** 597 of 825.
- **Audit:** 264 of 352.

## Summary
- **Restricted to CTCF-anchored loops, skeletal muscle shows the K⁺ excess** (pore-forming p = 0.010, all K⁺ p = 0.028).
- **So every Hi-C map tested (motor neurons, astrocytes, colon, muscle) carries the excess at CTCF-anchored loops.**

## Potential leads for future research
- **[Target-cell CTCF]** Use CTCF peaks from the same samples instead of the H1/HFFc6 proxy.
- **[Primary ChIA-PET negatives]** Which K⁺ genes are at anchors in the positives but not in T cells, HUVEC and HMEC? This would be a gene-level comparison, pre-registered.
- **[Manuscript 3 v1.7]** Done: §3.17 now covers L3909 and L3913.
