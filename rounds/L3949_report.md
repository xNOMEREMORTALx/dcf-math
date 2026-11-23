# DCF L3949: blind in a new cell type (WTC11 iPSC), the potassium excess repeats, and the non-voltage-gated families again lead (3 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 22 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3949_wtc11.txt`.
- **Script:** `rounds/dcf_ksub_L3949.py`, seed 3949.
- **Output:** `L3949_tool_output.txt`, committed before grading.
- **Grading:** `L3949_grade_output.txt`.

**Data:** Gary's "tcells" zip contained:

| file | what it is | used? |
|---|---|---|
| ENCFF455CNF | WTC11 iPSC CTCF ChIA-PET loops (ENCSR779QAB, rep2, Ruan lab), 305,999 loops → top 28,270 | **yes, blind** |
| ENCFF168ZTH | Hi-C loops, 151,208 (ENCSR949ZZD) | **dropped:** cell type could not be confirmed |

**From Gary's screenshots of the T-cell Hi-C experiments:**

| experiment | cells | default loops file |
|---|---|---|
| ENCSR335JYP | resting CD4 T | **ENCFF749LFC** (other: ENCFF146BTS) |
| ENCSR836MWK | activated CD4 T | **ENCFF169BLJ** (other: ENCFF380HFT) |
| ENCSR421CGL | activated CD4 T | none released (only haplotype files): **void** |

The T-cell loops files themselves were not in the zip, so the T-cell test is still pending.

## Results
| # | prediction | result |
|---|---|---|
| V1 | pore-forming K⁺ p_upper < 0.05 | **PASS**: 0.456 vs 0.317, excess +0.139, p = 0.006 |
| V2 | non-Kv excess larger than Kv | **PASS**: +0.180 vs +0.099 |
| V3 | non-Kv p_upper < 0.05 | **PASS**: p = 0.012 |

**3 of 3 passed.**

| subfamily | genes | excess | p |
|---|---|---|---|
| Kv, voltage-gated | 40 | +0.099 | 0.12 |
| non-Kv (K2P + Kir + KCa) | 39 | **+0.180** | **0.012** |
| K2P | 15 | +0.211 | 0.068 |
| Kir | 16 | +0.152 | 0.14 |
| KCa | 8 | +0.186 | 0.21 |

## What it means
**The fixed readings apply.**
- **The excess repeats blind in an iPSC line.**
- **The non-Kv > Kv ordering replicates on data not used to find it.** It has now appeared in the ten cell lines, the nine Hi-C maps and WTC11.
- **The resting-potential and calcium-activated K⁺ families carry the signal more than the voltage-gated spike channels.**

## Record
- **+3 passed:** 611 of 847.
- **Audit:** 278 of 374 (entry "WTC11 iPSC, blind").

## Summary
- **WTC11 iPSC (new, blind):** pore-forming K⁺ genes are at CTCF anchors more than matched genes (p = 0.006).
- **The non-voltage-gated families lead again** (+0.18 vs +0.10).

## Potential leads for future research
- **[T-cell Hi-C, now with known files]** Download ENCFF749LFC (resting) and ENCFF169BLJ (activated). This decides cell type vs method for the T-cell exception.
- **[Kv vs non-Kv, pooled]** A formal paired test across all blind maps once the T-cell files are in.
- **[Manuscript 3 v2.4]** Done: §3.24 is added.
