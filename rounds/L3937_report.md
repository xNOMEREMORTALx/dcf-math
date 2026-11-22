# DCF L3937: other four-fold channels do not share the potassium excess (blind, 1 of 3). The signal is potassium-specific, not a symmetry effect
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 21 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3937_tetramers.txt`.
- **Script:** `rounds/dcf_tetra_L3937.py`, seed 3937.
- **Output:** `L3937_tool_output.txt`, committed before grading; it includes the per-gene list.
- **Grading:** `L3937_grade_output.txt`.

**Blind:** none of the 37 genes had been looked at in any map.

**TETRA4 (37 genes):** non-potassium channels built, like K⁺ channels, from four subunits around a central pore:
- **TRP channels:** TRPC, TRPV, TRPM, TRPA1, mucolipins and polycystin-2 types.
- **Cyclic-nucleotide-gated channels:** CNGA/B.
- **Sperm CatSper channels:** CATSPER1–4.

**Maps:**
- **A:** ten cell lines.
- **B:** nine Hi-C maps (CTCF-anchored loops).

## Results
| # | prediction | result |
|---|---|---|
| S1 | ten cell lines: TETRA4 p_upper < 0.05 | **FAIL**, 0.216 vs 0.285, p = 0.93 |
| S2 | nine Hi-C maps: TETRA4 p_upper < 0.05 | **FAIL**, 0.057 vs 0.093, p = 0.89 |
| S3 | TETRA4 excess smaller than the K⁺ pore excess (cell lines) | **PASS**, −0.069 vs +0.095 |

**1 of 3 passed.** The failures stand.

Each cell gives the family share, then the matched-gene null mean, then the excess.

| set | ten cell lines | nine Hi-C maps |
|---|---|---|
| pore-forming K⁺ (79) | 0.368 vs 0.273, **+0.095**, p = 0.002 | 0.165 vs 0.093, **+0.071**, p = 0.001 |
| other four-fold channels (37) | 0.216 vs 0.285, **−0.069**, p = 0.93 | 0.057 vs 0.093, **−0.036**, p = 0.89 |

## What it means
**The fixed reading (S1 and S2 fail):** the excess is specific to potassium channels, not to four-fold pores.
- **The other tetrameric channels lean the opposite way.** They sit at anchors less often than matched genes in both groups (p_lower 0.08 and 0.12).

**So the "square pore" geometry raised in L3925 is not what links these genes to CTCF anchors.** Two individual genes do stand out in both groups (descriptive): PKD2L1 and TRPC6.

**Together with L3885 (no scaling with symmetry order), the symmetry line is now closed:**
- **Three-fold:** no excess.
- **Five-fold:** no excess.
- **Six-fold:** weak.
- **Four-fold:** only the K⁺ channels.

## Record
- **+1 passed, 2 failed:** 605 of 839.
- **Audit:** 272 of 366 (entry "non-K tetramers, blind").

## Summary
- **Blind test of 37 non-potassium four-fold channel genes: no excess at CTCF anchors** (p = 0.93 and 0.89), if anything a deficit.
- **The potassium pore excess re-runs at p = 0.002 and 0.001** in the same maps.
- **The pattern is about potassium channel genes,** not about pore symmetry.

## Potential leads for future research
- **[Within potassium]** Which feature of K⁺ genes matters? Pre-register Kv vs Kir vs K2P vs KCa excess, using the dependence-aware test on the nineteen positive maps.
- **[Gene-family age]** K⁺ channels are among the oldest channel families. Test whether gene age (e.g. Ensembl gene-tree age) predicts anchoring across all channel genes. This needs a gene-age table.
- **[Manuscript 3 v2.1]** Done: §3.21 is added.
