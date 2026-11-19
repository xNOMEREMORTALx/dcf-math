# DCF L3845: in three more cell types the nerve-metal gene excess at CTCF anchors is positive but not significant (3 of 4). The family pattern repeats everywhere: K⁺ and NMDA above, Ca²⁺ pores below
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3845_ctcf_multicell.txt`.
- **Amendment:** `AMENDMENT_L3845_a.txt`, made before any download. It covers:
  - GM12878 → IMR-90, since no Ruan-lab CTCF set exists for GM12878;
  - the file maps from Gary's screenshots.
- **Script:** `rounds/dcf_ctcf_neural_L3825a.py`, unchanged.
- **Grader:** `rounds/dcf_grade_L3845a.py`.
- **Outputs:** `rounds/L3845_tool_output_{K562,HepG2,IMR-90}.txt`, committed before grading.
- **Grading:** `rounds/L3845_grade_output.txt`.

**Data:** ENCODE CTCF in-situ ChIA-PET, Ruan lab. The larger replicate in each cell was used, by the frozen rule, keeping its strongest 28,270 loops by PET count.

| cell | experiment | file used | loops | other replicate |
|---|---|---|---|---|
| K562 (erythroleukemia) | ENCSR597AKG | ENCFF118PBQ | 129,669 | ENCFF607PZX, 100,264 |
| HepG2 (liver carcinoma) | ENCSR411IVB | ENCFF743ZWY | 151,730 | ENCFF299NHM, 48,415 |
| IMR-90 (lung fibroblast) | ENCSR076TTY | ENCFF816ATV | 509,630 | ENCFF682YFU, 471,557 |

The upload had a duplicate copy of ENCFF118PBQ (identical MD5); it was ignored.

---

## Results
| # | prediction | result |
|---|---|---|
| M1 | pooled D > 0 with p < 0.05 in each cell | **FAIL:** D positive in all three (0.026, 0.042, 0.053), p = 0.24, 0.18, 0.09 |
| M2 | K⁺ channels above other genes in each | **PASS:** 0.34, 0.33, 0.34 vs 0.28, 0.31, 0.29 |
| M3 | NMDA receptors above other genes in each | **PASS:** 0.43 in all three |
| M4 | Ca²⁺ channel pores below other genes in ≥ 2 of 3 | **PASS:** 0.10, 0.30, 0.20, below in all three |

**3 of 4 passed.** M1 failed and stands.

## Six cell types side by side
| cell | type | D | p | KCN | GRIN | CACNA1 | other |
|---|---|---|---|---|---|---|---|
| H1 | stem cell | **0.110** | **0.001** | 0.34 | 0.57 | 0.10 | 0.24 |
| HFFc6 | fibroblast | **0.057** | **0.018** | 0.28 | 0.57 | 0.10 | 0.24 |
| SK-N-SH | neuroblastoma | **0.100** | **0.001** | 0.44 | 0.57 | 0.20 | 0.33 |
| K562 | leukemia | 0.026 | 0.24 | 0.34 | 0.43 | 0.10 | 0.28 |
| HepG2 | liver cancer | 0.042 | 0.18 | 0.33 | 0.43 | 0.30 | 0.31 |
| IMR-90 | fibroblast | 0.053 | 0.09 | 0.34 | 0.43 | 0.20 | 0.29 |

(H1 and HFFc6 use the 4DN CTCF-tagged loops; the other four use ENCODE in-situ ChIA-PET.)

## What it means
- **The excess is real but modest and varies between cell types.** It is strong in stem cells and the neural line, and weak in the blood and liver lines.
- **D is positive in all six cell types** (sign test, one-sided p = 1/64 ≈ 0.016). This is descriptive, because it mixes rounds whose results I had already seen.
- **The family pattern is the most stable result.** Potassium channels and NMDA receptors are above the genome-wide share in all six cell types. Calcium-channel pore genes are below it in all six.
- **The pooled test lacks power where the effect is small.** With about 28,000 loops, the null's spread (sd ≈ 0.03) is about as large as the effect in K562.

## Record
**+3 passed, 1 failed. 559 of 770 passed, plus 3 split.** Audit **226 of 297** (entry "CTCF anchors, K562 HepG2 IMR-90").

## Summary
- **In three more cell types the nervous system's metal-battery genes again lean toward CTCF loop anchors,** but not significantly. The overall test failed.
- **The family pattern held a fourth, fifth and sixth time:** potassium channels and NMDA receptors above, calcium channel pores below.
- **Manuscript 3's claim should be stated as a modest, cell-type-dependent excess with a stable family pattern.**

## Potential leads for future research
- **[Family-level meta-test]** Pre-register a combined test across new cell types: KCN − other, GRIN − other and CACNA1 − other, each with its own genome-shift null. The family pattern, not the pooled D, is the robust signal.
- **[Why stem and neural cells?]** H1 and SK-N-SH show the largest D. Compare with the remaining Ruan-lab sets (HEK293, MCF 10A, BJ, RWPE1, T cells) before guessing.
- **[Power]** Using all loops with PET ≥ 25 instead of a fixed 28,270 would change the density per cell. Decide in advance, if at all.
- **[Manuscript 3]** v0.5 with the six-cell table.
