# DCF L3853: the CTCF-anchor family pattern is not a gene-length artefact (4 of 4). Long genes sit at anchors less often, but K⁺, NMDA and Ca²⁺-pore genes still differ from length-matched controls
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3853_length_matched.txt`.
- **Script:** `rounds/dcf_lengthmatch_L3853.py`.
- **Grader:** `rounds/dcf_grade_L3853.py`.
- **Output:** `rounds/L3853_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3853_grade_output.txt`.

**Blindness:** not blind to the ten loop sets. Blind to every length-matched comparison, which had never been computed.

**Method:**
- Each family gene gets its 20 nearest non-channel genes by log₁₀ length as controls.
- The medians match closely: KCN 47.8 kb vs 47.8 kb; GRIN 51.3 vs 51.3; **CACNA1 183 kb vs 182 kb**.

---

## Results
| # | prediction (≥ 7 of 10 cells) | result |
|---|---|---|
| L1 | K⁺ channels above their length-matched control | **PASS:** 10 of 10 |
| L2 | Ca²⁺ pores below their length-matched control | **PASS:** 9 of 10 (HepG2 +0.065) |
| L3 | NMDA receptors above their length-matched control | **PASS:** 9 of 10 (MCF 10A −0.150) |
| L4 | longest tenth of ordinary genes below the ordinary-gene share | **PASS:** 10 of 10 |

**4 of 4 passed.**

## Δ = family share − length-matched control share
| cell | KCN | GRIN | CACNA1 | longest 10% vs all ordinary |
|---|---|---|---|---|
| H1 | +0.109 | +0.314 | −0.110 | 0.221 vs 0.235 |
| HFFc6 | +0.033 | +0.364 | −0.120 | 0.236 vs 0.238 |
| SK-N-SH | +0.089 | +0.286 | −0.065 | 0.274 vs 0.332 |
| K562 | +0.058 | +0.171 | −0.135 | 0.220 vs 0.283 |
| HepG2 | +0.021 | +0.193 | **+0.065** | 0.242 vs 0.310 |
| IMR-90 | +0.058 | +0.136 | −0.065 | 0.249 vs 0.286 |
| HEK293 | +0.068 | +0.436 | −0.035 | 0.215 vs 0.293 |
| MCF 10A | +0.034 | **−0.150** | −0.185 | 0.259 vs 0.298 |
| BJ | +0.075 | +0.307 | −0.070 | 0.231 vs 0.316 |
| RWPE1 | +0.014 | +0.329 | −0.035 | 0.233 vs 0.299 |

## What it means
- **Long genes really do sit at CTCF loop anchors less often** (L4, 10 of 10). Calcium-pore genes are long (median 183 kb), so **part** of their dip is a length effect.
- **Length does not explain the pattern.** Against genes of the same length:
  - potassium-channel genes are still above in every cell type;
  - NMDA-receptor genes are above in 9;
  - calcium-pore genes are below in 9.
- **As fixed in advance, L2 passing means the calcium dip is not only a length effect.**
- **Still uncontrolled:** local gene density and chromosome position.

## Record
**+4 passed. 567 of 778 passed, plus 3 split.** Audit **234 of 305** (entry "length-matched control").

## Summary
- **The family pattern survives a gene-length control in ten cell types.** Manuscript 3 is updated to v0.7.

## Potential leads for future research
- **[Gene density control]** Match on the number of genes within ±1 Mb as well as length. Pre-register before computing.
- **[Combined statistic]** One pre-registered, Stouffer-combined, genome-shift test across all ten cells for each family contrast.
- **[Figure]** A 10-cell dot plot of Δ for Manuscript 3.
