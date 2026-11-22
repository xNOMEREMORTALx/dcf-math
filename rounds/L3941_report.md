# DCF L3941: in neurons, astrocytes, colon and muscle, the potassium excess is carried by the Kir, K2P and KCa families, and least by the voltage-gated Kv family (2 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 22 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3941_ksub_hic.txt`.
- **Script:** `rounds/dcf_ksub_L3941.py`, seed 3941.
- **Output:** `L3941_tool_output.txt`, committed before grading.
- **Grading:** `L3941_grade_output.txt`.

**Graded:** group B, the nine CTCF-anchored Hi-C maps. Subfamily shares had not been computed there before.

**Reference only:** group A, the ten cell lines. It was re-run and reproduces L3873.

## Results
| # | prediction | result |
|---|---|---|
| U1 | all four subfamilies above matched genes in the Hi-C maps | **PASS** |
| U2 | Kv p_upper < 0.05 | **FAIL**, p = 0.19 |
| U3 | Kir p_upper < 0.05 | **PASS**, p = 0.012 |

**2 of 3 passed.** The failure stands.

Each cell gives the excess over matched genes, then p_upper.

| subfamily | genes | ten cell lines | nine Hi-C maps |
|---|---|---|---|
| Kv, voltage-gated | 40 | +0.061, p = 0.10 | +0.029, p = 0.19 |
| K2P, two-pore "leak" | 15 | +0.129, **p = 0.040** | +0.114, **p = 0.019** |
| Kir, inward rectifier | 16 | +0.115, p = 0.059 | +0.119, **p = 0.012** |
| KCa, calcium/sodium-activated | 8 | +0.171, p = 0.069 | +0.109, p = 0.053 |

## What it means
**The fixed reading (U1 passes):** the excess is spread across all four K⁺ pore families in tissues and neurons, as in the cell lines.

**The strength is uneven, and the same order shows in both groups (descriptive):**
- **Weakest: Kv,** the voltage-gated family that fires action potentials.
- **Two to four times stronger:** K2P, Kir and KCa, the families that set and hold the resting potential (leak and inward-rectifier channels) or respond to calcium.

**So the anchor signal follows "resting-potential and housekeeping" K⁺ channels more than the spike-shaping Kv channels.**
- **This is a pattern, not yet a test:** the subfamilies are small (8–16 genes).

## Record
- **+2 passed, 1 failed:** 607 of 842.
- **Audit:** 274 of 369 (entry "K+ subfamilies, Hi-C").

## Summary
- **All four K⁺ pore families sit above matched genes at CTCF anchors in neurons, glia, gut and muscle.**
- **The leak (K2P), inward-rectifier (Kir) and calcium-activated (KCa) families are strong** (excess +0.11–0.12). The voltage-gated Kv family is weak (+0.03) and not significant.
- **The same ordering is seen in the ten cell lines.**

## Potential leads for future research
- **[Kv vs non-Kv, formal]** Pre-register, on new maps, that non-Kv pore genes (39) exceed Kv (40) in anchor excess. This is a paired difference with matched nulls.
- **[Resting-potential genes beyond K⁺]** Do other resting-potential genes (Na⁺/K⁺-ATPase ATP1A1–4 and ATP1B1–4, and the chloride channel CLCN2) show the same excess? ATP1A were in the 139-gene set; their per-family shares are already in the earlier outputs, but they would need a new blind set.
- **[Manuscript 3 v2.2]** Done: §3.22 is added.
