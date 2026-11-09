# DCF L3225: the helix, spin and the metals — what the physics supports, what our genomes show (1 of 3 pass), and the "step phase" that is really there: the 3-3-4 ladder of the iron–sulfur cluster
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Lead (Gary):** "The helix as a polarized lattice structure for information storage, connectivity to magnetic moments, and step-phase relationship to the metallics exhibited in our tests."

**Pre-registration:** `PREREGISTERED_L3225.txt`, SHA-256 `e7eb6241…ff36`, commit `089b72f`, pushed before computing.

---

## 1. The physics, checked [V where cited; links D]
**The DNA helix is chiral, and chirality polarizes electron spin.** This is the chirality-induced spin selectivity (CISS) effect. Göhler *et al.* (Science 2011) passed photoelectrons through a monolayer of 78-bp double-stranded DNA on gold and measured spin polarizations of about **−55% to −61%**, depending on the light's polarization [V, Evers *et al.* 2021 review]. A helix can therefore act as a **spin filter**: it favours electrons whose magnetic moment points one way. This is the solid, published version of "a polarized lattice connected to magnetic moments".

**Its limits.**
- DNA itself is diamagnetic; it carries no permanent magnetic moment.
- CISS is about electrons moving through the helix.
- **No accepted theory explains its size:** spin-orbit calculations fall short of experiment by up to several orders of magnitude [V].

**Where the metals come in.** The Fe–S clusters our genome tests count are electron carriers with net electron spin (reduced [4Fe-4S]⁺ is commonly S = 1/2). A biological chain that passes electrons through chiral proteins and DNA past spin-carrying Fe–S clusters is exactly where CISS researchers look for biological roles. **Whether it matters in living cells is open.**

**"Information storage".** DNA stores information in its base sequence, which the DCF codec already uses (`dcf_dna_codec.py`). No evidence was found that the helix stores information in spin or magnetic form.

## 2. Test A — does the DNA helix "step" track metal chemistry? [exploratory, not graded]
**Method.** The gene finder measures each genome's DNA helical rhythm (AA/TT dinucleotides recurring every ~10–11 bp). I compared it with the CxxC iron–sulfur density on all 28 graded chromosomes. Both columns were already visible in the logs, so this is **description, not a test**.

| comparison | Spearman ρ | p |
|---|---|---|
| rhythm strength vs Fe–S density | **0.00** | 0.99 |
| rhythm period vs Fe–S density | 0.05 | 0.79 |
| rhythm strength vs GC | **−0.70** | < 0.001 |

**Reading.**
- **No link.** The DNA helical step does not track the metal chemistry at all. Its strength is set by base composition.
- **A measurement warning:** 7 of 28 genomes sit at 8.00 bp, the bottom of the scan range, so the rhythm is weak or absent in many genomes (lead [Helix-scan]).

## 3. Test B — the cysteine "step spectrum" of metal binding [pre-registered]
**Why proteins.** Metals are bound by cysteines placed at fixed steps along a protein chain, and an α-helix turns every 3.6 residues. So the place a "step phase" could join helix and metal is the **spacing of cysteine pairs**.

**Method.**
- Every cysteine pair at distance d = 1–24 in the label-free predicted proteomes, as observed/expected for each protein's own cysteine count.
- Groups fixed from the hashed tool numbers: 11 Fe–S-rich (density ≥ 0.60) vs 12 Fe–S-poor (≤ 0.40).

**Median observed/expected:**

| d | 1 | 2 | **3** | **4** | 5 | **6** | **7** | 8 | 9 | **10** | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fe–S-rich | 0.98 | 1.02 | **3.89** | **1.84** | 1.14 | **1.63** | **1.73** | 1.11 | 1.06 | **1.41** | 1.09 | 1.05 |
| Fe–S-poor | 1.07 | 1.12 | 4.52 | 1.31 | 1.47 | 1.51 | 1.49 | 1.17 | 1.08 | 1.18 | 1.19 | 1.08 |

| id | prediction | result | verdict |
|---|---|---|---|
| Q1 | ferredoxin ladder: rich > poor at **both** d = 6 and d = 10 | d = 10: 1.41 vs 1.18, **p = 0.0014**; d = 6: 1.63 vs 1.51, p = 0.26 | **FAIL** (half) |
| Q2 | helical phase: more power at period 3.6 in rich (ferredoxin motifs masked) | rich 4.1 vs poor 12.6, the **opposite** direction (p = 0.99) | **FAIL** |
| Q3 | lysine control shows no difference | p = 0.64 | **PASS** |

**What the spectrum shows [D, read after the test].**
- **The Fe–S-rich proteomes peak at d = 3, 4, 6, 7 and 10,** and dip at 5. These are exactly the pair distances of the 4Fe-4S ferredoxin ligand pattern C-x₂-C-x₂-C-x₃-C, with steps 3, 3, 4:

  | pair | C1–C2 | C2–C3 | C3–C4 | C1–C3 | C2–C4 | C1–C4 |
  |---|---|---|---|---|---|---|
  | distance | 3 | 3 | 4 | 6 | 7 | 10 |

- **So the "step phase" tied to the metals is real, but it belongs to the iron–sulfur cluster's own geometry,** four cysteines spaced 3-3-4 around a cubane, not to an α-helix or to the DNA helix.
- **The pre-registered α-helix reading (Q2) failed outright.**

## Record
**This round:** 3 graded, 1 passed.

**Total: 276 of 365 pre-registered predictions passed, plus 3 split.**

## Summary
- **The physics behind the idea is real.** A DNA helix filters electrons by spin (about 55–61% polarization measured in 2011), and iron–sulfur clusters carry electron spin. How strong the effect is in living cells, and why, is still unexplained.
- **Our genomes don't show the DNA helix tracking the metals.** Across 28 genomes the helix rhythm is unrelated to iron–sulfur content; it follows base composition instead.
- **The "step phase" of the metals is in the proteins, not the DNA.** Iron–sulfur-rich proteomes carry cysteines at steps 3, 4, 6, 7 and 10, the exact fingerprint of the ferredoxin cluster's 3-3-4 ligand ladder. An α-helical 3.6-residue phase was predicted and not found.

## Potential leads for future research
- **[Fe-ladder]** Use the 3-3-4 ladder (C-x₂-C-x₂-C-x₃-C) as a sharper label-free Fe–S measure than CxxC alone. Pre-register on the next blind set: does it separate ferredoxin-based genomes better than CxxC (fewer grey-zone cases such as *Arcobacter* or *Nitrosospira*)?
- **[CISS-bio]** Literature lead: are CISS measurements reported on ferredoxins or Fe–S electron-transfer proteins specifically? If so, the ladder spacing could be compared with measured spin selectivity.
- **[Helix-scan]** The helical-rhythm scan hits its lower bound (8.00 bp) in a quarter of genomes. Widen the scan and add a null amplitude so "no rhythm" is reported honestly.
- **[Spin-store]** If the information-storage idea is to be pursued, the testable form is physical (spin-polarized transmission vs sequence), which needs lab data; it cannot be tested from sequence alone.
- **Carried:** [Nautilia] to finish blind_18, then the v2.32 release decision.
