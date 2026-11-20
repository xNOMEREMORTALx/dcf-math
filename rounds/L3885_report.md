# DCF L3885: geometry and harmonics in the metal work. Channels really come as triangles, squares, pentagons and hexagons, but their CTCF-anchor tilt does not scale with symmetry (1 of 4). The DNA-tone and 528 Hz claims, checked
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 19 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3885_symmetry.txt`, frozen before computing.
- **Script:** `rounds/dcf_symmetry_L3885.py`.
- **Grader:** `rounds/dcf_grade_L3885.py`.
- **Output:** `rounds/L3885_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3885_grade_output.txt`.

---

## 1. Real geometry in the metal biology (well-established structural facts)
**Ion channels are built with whole-number symmetry around the pore:**

| shape | symmetry | channel families | metal / ion |
|---|---|---|---|
| **triangle** | 3-fold trimers | ASIC and ENaC (acid/sodium channels), P2X (ATP-gated) | Na⁺, Ca²⁺ |
| **square** | 4-fold tetramers | K⁺ channels (Kv, Kir, K2P dimers of 2 pores, KCa), HCN, NMDA/AMPA receptors; Na⁺ and Ca²⁺ channels are one chain folded into 4 repeats | K⁺, Na⁺, Ca²⁺ |
| **pentagon** | 5-fold pentamers | nicotinic, GABA-A, glycine, 5-HT3 receptors (the Cys-loop family) | Na⁺/K⁺ or Cl⁻ |
| **hexagon** | 6-fold hexamers | connexins (gap junctions), ORAI (store-operated Ca²⁺ channel) | Ca²⁺ and small ions |

**The metals themselves sit in exact polyhedra:**
- **K⁺ in the selectivity filter:** surrounded by **8 oxygen atoms at the corners of a twisted cube** (a square antiprism), copying the water shell it sheds. Four such sites are stacked along the pore.
- **Ca²⁺ in EF-hand proteins:** sits in a **pentagonal bipyramid**, 7 oxygens with a pentagon around the waist.
- **Zn²⁺ in zinc fingers (CTCF has 11):** **tetrahedral**, from 2 cysteines and 2 histidines.
- **Mg²⁺ (and Na⁺ in water):** **octahedral**, 6 neighbours.

**DNA's own geometry, from your numbers:**
- **Rise:** 0.34 nm per base pair.
- **Twist:** about 10.5 base pairs per turn, so **360°/10.5 ≈ 34.3° per step.** A 10-step idealised turn would be 36°, the pentagon/decagon angle, which is why idealised B-DNA seen end-on is drawn as a decagon.
- **Pitch/width:** 3.4 / 2.0 = **1.70**. The popular "golden ratio" version uses 34 Å / 21 Å = 1.619 ≈ φ (1.618), but measured B-DNA is closer to 1.7.
- **Length:** 3.1 × 10⁹ bp × 0.34 nm ≈ **1.05 m** per haploid genome, as you said.

## 2. The DNA-tone and 528 Hz claims, checked
**Alexjander and Deamer (Sequencia):**
- **Method:** infrared absorption bands of the four bases (600–3,000 cm⁻¹, about 15–18 bands each, 60 in all) were halved 36 times (÷ 2³⁶ = 68,719,476,736) to land in the hearing range.
- **The published C# centres:** A 545.6, G 550.0, T 543.4, C 537.8 Hz (average 544.2).
- **Working back, these correspond to infrared bands near 1,233–1,261 cm⁻¹** (the phosphate and C–N region).
- **The four tones lie within 39 cents of each other,** less than half a semitone.
- **This is an artistic octave transposition.** DNA does not emit these sounds, and infrared differences ("heterodynes") between bands are still infrared (~10¹² Hz), not audible.

**528 Hz:**
- **It lies 52 cents below the DNA average,** about half a semitone, so it is **not** one of the DNA tones by Alexjander's own data.
- **The "DNA repair" claim traces to a 1999 self-published book and numerological "Solfeggio" frequencies.** No peer-reviewed study shows 528 Hz repairs DNA.
- **D 288 / A 432:** 432/288 = **1.5**, an exact perfect fifth, true of any frequencies in a 3:2 ratio.

## 3. The test: does CTCF-anchor tilt scale with channel symmetry? (1 of 4)
Gene resampling matched for length and local gene density, ten original cells scored together (the L3869 method).

| group | genes | share | matched null | Δ | p (upper) | prediction | result |
|---|---|---|---|---|---|---|---|
| triangle (ASIC, ENaC, P2X) | 16 | 0.425 | 0.349 | +0.076 | 0.18 | Y2 excess | **FAIL** |
| square (pore-forming K⁺) | 79 | 0.368 | 0.274 | +0.094 | 0.002 | (seen before) | — |
| pentagon (Cys-loop receptors) | 45 | 0.271 | 0.261 | +0.011 | 0.39 | Y1 excess | **FAIL** |
| hexagon (connexins, ORAI) | 23 | 0.417 | 0.297 | +0.120 | **0.034** | Y3 excess | **PASS** |
| scaling with 3 → 4 → 5 → 6 | — | — | — | +0.08, +0.09, +0.01, +0.12 | — | Y4 monotonic | **FAIL** |

**1 of 4 passed.** One count was off: the pre-registration said 22 hexamer genes, but the frozen gene rule gives 23 (GJA10 included). The rule, not the count, was frozen.

**Reading:**
- **There is no scaling law:** the tilt does not rise or fall with the number of sides.
- **"All pore-forming channels are anchored" also fails:** the large pentameric receptor family shows no excess at all.
- **The hexagonal channels lean toward anchors,** in a group of only 23 genes, in the same cell lines where the T-cell test later failed. It needs a fresh test.

## Record
**+1 passed, 3 failed. 580 of 802 passed, plus 3 split.** Audit **247 of 329** (entry "channel symmetry order").

## Summary
- **The metal biology is full of real geometry:**
  - channels built as triangles, squares, pentagons and hexagons;
  - K⁺ held in a cube-like cage of 8 oxygens;
  - Ca²⁺ in a pentagonal bipyramid;
  - Zn²⁺ in a tetrahedron.
- **No scaling factor links that geometry to where the genes sit in 3D chromatin:** pentamers show nothing, and the trend with symmetry order is not monotonic.
- **The DNA-sound claims, checked:**
  - Alexjander's DNA tones are infrared bands transposed down 36 octaves, all within half a semitone of C#;
  - 528 Hz is not among them and has no evidence for DNA repair.

## Potential leads for future research
- **[Geometry that is physics]** The cube-like K⁺ cage and the Ca²⁺ pentagonal bipyramid set real numbers (coordination numbers 8 and 7; metal–oxygen distances about 2.8 Å for K⁺ and 2.4 Å for Ca²⁺). A DCF-style test could ask whether channel selectivity sequences across species keep the residues that build these cages, using our existing proteomes.
- **[Hexamers, fresh cells]** Pre-register the hexamer excess on new cell types (L3881 cells).
- **[Sound, honestly]** If wanted: a pre-registered test of whether Alexjander's 60 transposed DNA tones contain more simple-ratio intervals than random tone sets in the same range. That needs her full list of 60 values from the original figures.
