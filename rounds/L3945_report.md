# DCF L3945: other resting-potential genes show the excess in cell lines but not in neurons, glia, gut and muscle (blind, 1 of 2)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 22 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3945_resting_set.txt`.
- **Script:** `rounds/dcf_rest_L3945.py` (L3937 script, seed 3945).
- **Output:** `L3945_tool_output.txt`, committed before grading.
- **Grading:** `L3945_grade_output.txt`.

**Blind:** none of the 20 genes had appeared in any earlier set.

**REST20 (20 genes, the non-channel machinery that sets the resting potential):**
- **ATP1B1–4:** Na⁺/K⁺ pump β subunits.
- **FXYD1–7:** pump regulators.
- **SLC12A1–9:** the chloride cotransporters, including NKCC1 and KCC2.

## Results
| # | prediction | result |
|---|---|---|
| R1 | ten cell lines: REST20 p_upper < 0.05 | **PASS**, 0.470 vs 0.338, excess +0.132, p = 0.032 |
| R2 | nine CTCF-anchored Hi-C maps: REST20 p_upper < 0.05 | **FAIL**, 0.122 vs 0.098, excess +0.024, p = 0.27 |

**1 of 2 passed.** The failure stands.

The pore-forming K⁺ genes re-run in the same maps at p = 0.003 and 0.001.

## What it means
**The result is split, a case the fixed interpretation did not cover (it covered both pass or both fail).** So neither reading applies, and the extension is **not established**.
- **In the cell lines,** the resting-potential set sits at anchors more than matched genes, about as strongly as K⁺ channels.
- **In the Hi-C maps from neurons, astrocytes, colon and muscle,** it does not.

**Unlike K⁺ channels, these genes do not show the excess across both groups.** The robust signal stays with the K⁺ pore genes.

**Genes that stand out (descriptive):**
- **Cell lines:** FXYD3, FXYD1 and SLC12A9.
- **Hi-C maps:** SLC12A7 (KCC4) and SLC12A3.
- **Both groups:** SLC12A5 (KCC2, the neuronal chloride extruder) is high in both.

## Record
- **+1 passed, 1 failed:** 608 of 844.
- **Audit:** 275 of 371 (entry "resting-potential set, blind").

## Summary
- **Blind test of 20 non-channel resting-potential genes:** excess in the ten cell lines (p = 0.032), none in the nine tissue/neuron Hi-C maps (p = 0.27).
- **The K⁺ channel excess remains the only pattern present in both groups.**

## Potential leads for future research
- **[Kv vs non-Kv, formal]** This still needs new maps: any further ENCODE CTCF ChIA-PET or Hi-C loops files you can find.
- **[KCC2 (SLC12A5)]** It is high in both groups. A single-gene follow-up could check whether its anchor is the same CTCF site across maps.
- **[Manuscript 3 v2.3]** Done: §3.23 is added.
