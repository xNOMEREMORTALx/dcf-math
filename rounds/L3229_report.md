# DCF L3229: *Nautilia* completes blind_18 — the ferredoxin member wins all 3 lineage pairs, the start fix passes blind and is released as v2.32; iron's nuclear numbers (26, 30, 56) show no pattern in protein distances or start positions
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:**
- [Nautilia]: finishing L3217's D1, D4–D6 and the L3221 island test;
- **[Z-match]**, Gary's request: metal proton/neutron/electron counts as distances and start/stop positions;
- [v2.32 release].

**Data.** Gary's attachment was the *Nautilia profundicola* AmH GenBank file. It was saved with an `.html` name but is plain GenBank text: LOCUS NC_012115, 1,676,444 bp, one record ending with `//`.

**Tool numbers** were hashed before the annotation was read: SHA-256 `da4bdb93a78a737c843f426195d9ad7474d5695c460aa402e8f86cc5edfa08b6`.

**Pre-registrations:**
- `PREREGISTERED_L3217.txt` (`6fff72c9…`);
- `PREREGISTERED_L3229_Z.txt` (`ad72b1c3…d343`), pushed before computing.

---

## 1. Lineage-matched pairs, complete [Fe-Fd]
| pair (same phylum) | ferredoxin-based member | partner |
|---|---|---|
| P1 | *Desulfomicrobium* **0.96** | *Myxococcus* 0.42 |
| P2 | *Desulfotomaculum* **0.89** | *B. licheniformis* 0.31 |
| P3 | *Nautilia* (rTCA, H2) **0.75** | *Arcobacter* 0.57 |

| id | prediction | result | verdict |
|---|---|---|---|
| **D1** | first member higher in 3 of 3 pairs | **3 of 3** | **PASS** |
| D2 | members > 0.50, partners < 0.50 | *Arcobacter* 0.57 | FAIL (graded in L3221) |
| D3 | partner Sec only in formate dehydrogenase | *Myxococcus* Sec in a thiol reductase | FAIL (graded in L3221) |

**Reading.** With ancestry held roughly constant, the ferredoxin-based organism reads higher every time. The fixed 0.50 cut does not transfer across lineages: Campylobacterota sit high overall, and *Nautilia* sits higher still. **Relative position within a lineage is the robust signal.**

## 2. Start fix, complete — v2.32 released [G-starts c]
| genome | exact start v2.31 → v2.32b | found change |
|---|---|---|
| *Desulfomicrobium* | 80.5 → 86.0 | +0.32 |
| *Myxococcus* | 75.1 → 80.4 | +0.32 |
| *Desulfotomaculum* | 84.7 → 85.4 | +0.48 |
| *B. licheniformis* | 86.4 → 86.5 | +0.28 |
| *Arcobacter* | 93.9 → 95.0 | +0.04 |
| *Nautilia* | 91.5 → 92.6 | +0.46 |

| id | prediction | result | verdict |
|---|---|---|---|
| **D4** | mean exact-start gain ≥ +1.0 | **+2.3** | **PASS** |
| **D5** | no genome loses > 1.0 | none lost | **PASS** |
| **D6** | found/correct change < 0.5 everywhere | max +0.48 | **PASS** |

**Release.** Under the frozen rule, gene finder **v2.32 is released** in dcf-genefinder (SHA-256 `fa30258b…297c`). Its logic is identical to the tested candidate, with byte-identical output checked on *Nautilia*. Combined blind evidence:
- L3213: +2.2 on 13 genomes;
- L3229: +2.3 on 6 genomes;
- up to +6 points in GC-rich genomes.

## 3. Island finder, regraded with *Nautilia* [Fe-island]
**This regrade corrects a step in L3221.** That round graded I1–I3 before *Nautilia* arrived, although the pre-registration included it "if it arrives".

| id | 5 genomes (L3221) | **6 genomes (with *Nautilia*)** | verdict |
|---|---|---|---|
| I1 every genome ≥ 2.0× | *Myxococcus* 1.2×, *Bacillus* 1.5× | unchanged (*Nautilia* 6.5×) | FAIL |
| I2 pooled ≥ 3.0× | 4.7× | **5.1×** | PASS |
| I3 ≥ 50% of islands with a keyword gene | 43% | **48%** (36 of 75) | FAIL |

*Nautilia*: 7 of 8 islands carry Fe–S/redox genes, at 6.5× its background. No verdict changed.

## 4. [Z-match] Iron's nuclear numbers as protein distances and start positions [pre-registered]
**Gary's request.** Look for metal proton, neutron and electron counts in distances and start/stop positions.

**The numbers tested.** Iron has **26 protons** (and 26 electrons in the neutral atom); iron-56 has **30 neutrons** and **mass number 56**.

**Predictions.** Each was stated as Gary's hypothesis, with neighbouring numbers as controls. I wrote down in advance that chemistry predicts a null.

| id | prediction (11 Fe–S-rich proteomes) | result | verdict |
|---|---|---|---|
| Z1 | cysteine pairs at distance **26** exceed neighbours (24, 25, 27, 28) by ≥ 10% in ≥ 8 of 11 | **2 of 11** (Fe–S-poor: 5 of 12) | **FAIL** |
| Z2 | same at distance **30** | **4 of 11** (poor: 2 of 12) | **FAIL** |
| Z3 | same at distance **56** | **1 of 11** (poor: 5 of 12) | **FAIL** |
| Z4 | first CxxC starts at residue **26** at ≥ 1.5× its neighbours | **0.90×** (counts 21, 21, **22**, 28, 28 at positions 24–28) | **FAIL** |

**Base rate (measured).** Any distance from 20 to 58 clears +10% in 17% of rich-genome comparisons and 29% of poor-genome ones. Iron's numbers do no better than random distances.

**Reading.**
- **The metal "step" in proteins is chemical, not nuclear.** The 3-3-4 ligand ladder (L3225) is set by how four cysteines wrap a cubane cluster.
- **Neither the proton count, the neutron count nor the mass number of iron leaves any mark** on distances or start positions.
- **The one "start/stop" link to metals that does exist is biochemical.** Selenocysteine (and pyrrolysine) are inserted at **stop codons** (TGA, TAG), and in these genomes selenocysteine sits mainly in Fe–S, hydrogenase and formate enzymes. That is tested and on record (L3145–L3221).

## 5. Other
- **Genetic code:** *Nautilia* table 11 correct; record **134 of 137**.
- ***Nautilia* carries 1 selenocysteine codon.**

## Record
**This round:** 8 graded, 4 passed (D1, D4, D5, D6 passed; Z1–Z4 failed).

**Total: 280 of 373 pre-registered predictions passed, plus 3 split.**

## Summary
- **The ferredoxin idea passed its fairest test.** In all three pairs of related microbes, the one running ferredoxin-based, low-potential metabolism had the higher iron–sulfur reading. The fixed cut doesn't transfer between lineages, but the ranking within a lineage held 3 for 3.
- **The improved gene-start finder passed blind and is now released as v2.32:** about 2–6 points more exact starts, with no loss of genes.
- **Iron's atomic numbers leave no pattern in proteins.** Distances of 26, 30 and 56 residues and start position 26 are no more common than their neighbours. The metal patterns in genomes are chemical (the 3-3-4 cysteine ladder; selenocysteine at stop codons), not nuclear counts. This null is kept on record.

## Potential leads for future research
- **[Fe-lineage]** Score genomes relative to their lineage, e.g. CxxC density minus the median of seen relatives in the same phylum. Pre-register on a fresh set with ≥ 4 phyla.
- **[Fe-ladder]** Pre-register the 3-3-4 ladder count as an iron–sulfur marker on the next blind set.
- **[Note G v1.2]** Fold v2.32 (both blind start tests) into Note G; re-run the Prodigal head-to-head with v2.32.
- **[Fe-island b]** Self-set eligibility for the island finder (genome CxxC density ≥ 0.6), then test blind.
- **[Z-other]** If Gary wants other metals tested the same way (Cu 29, Zn 30, Mo 42, Ni 28, Se 34), the method is ready. Pre-register first; the expected result is null.
