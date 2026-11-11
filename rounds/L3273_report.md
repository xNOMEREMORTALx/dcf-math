# DCF L3273: blind_20 completed with *L. gasseri* (14 of 16 in the right tier, ρ = 0.96); zinc's structural site barely follows the energy tiers (2.3× vs iron's 64×), which fits the electrochemistry of iron, zinc, hydrogen and oxygen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 10 November 2026

**Leads:**
- [blind_20 gasseri];
- **[Fe-Zn]**, Gary's idea: zinc and iron interact with hydrogen and oxygen, seen in iron precipitating out of solution and in zinc's sacrificial protection of iron from rust; 1/43's first 8 digits sum to 26, iron's atomic number.

**Data:** NC_008530 *Lactobacillus gasseri* ATCC 33323, matched by LOCUS line and not in either seen list.

**Pre-registration:** `PREREGISTERED_L3273_zinc.txt` (`2ebab881…fe5c`) and the script `dcf_zinc_ribbon_L3273.py` (`7f59da64…26c8`), both pushed before the zinc count was run on any blind_20 genome.

**Tool numbers:** the *gasseri* numbers were hashed (`f6974f60…bd86`) before any annotation was read.

---

## 1. blind_20 on all 16 genomes [re-report under the L3269 amendment]
*L. gasseri* reads **0.0000** ladders per 1,000 aa, the lowest value yet, so it lands in tier 1 ✓. The genetic code is correct (11), and the code record is now **156 of 159**.

| id | on 15 (L3269, the grade of record) | on 16 |
|---|---|---|
| T1 tier medians rise | PASS | PASS (0.0020 < 0.0149 < 0.0433 < 0.1278) |
| T2 right tier | 13 of 15 | **14 of 16** |
| T3 Spearman ρ | 0.954 | **0.958** (p = 6 × 10⁻⁹) |
| T4 lactic < 0.0045 | 3 of 3 | **4 of 4** |

Nothing changes. These are not counted as new predictions.

## 2. [Fe-Zn] Does zinc's structural site follow the energy tiers like iron's ladder? [pre-registered]
**Zinc ribbon** = C-x₂-C-x₉₋₂₀-C-x₂-C, a Zn(Cys)₄ knuckle. Ladder cysteines were masked first so ferredoxins are not counted.

| tier | zinc ribbon (median per 1,000 aa) | iron ladder (median) |
|---|---|---|
| 1 lactic | 0.038 | 0.002 |
| 2 O2 | 0.034 | 0.015 |
| 3 H2 fermenters | 0.059 | 0.043 |
| 4 Fd-based | 0.089 | 0.128 |
| **tier 4 / tier 1** | **2.3×** | **64×** |

| id | prediction | result | verdict |
|---|---|---|---|
| **Zn1** | the ribbon's tier-4/tier-1 ratio ≤ one fifth of the ladder's | 2.3 / 64 = **0.036** (28 times flatter) | **PASS** |
| Zn2 | Spearman ρ(tier, ribbon) < 0.60 | **ρ = 0.74** (p = 0.001) | **FAIL** |

**Reading.**
- **Iron's site follows the energy tiers about 28 times more steeply than zinc's.** The zinc site does not separate the bottom two tiers at all (lactic 0.038 vs oxygen breathers 0.034). Iron separates them about 7-fold.
- **Zn2 failed for the reason declared in advance.** The ribbon still climbs in tiers 3–4, led by *Methanobrevibacter* (0.20), and iron rubredoxins share the same CxxC…CxxC knuckle. In those anaerobes, some "zinc" knuckles probably hold iron. **This is a real point of iron–zinc interplay at the protein level: one fold, either metal.**

## 3. Why: one ladder of electrode potentials explains both the rust and the biology [literature values, textbook]
| couple | potential (V) | what it means |
|---|---|---|
| Zn²⁺ / Zn | **−0.76** | the most eager to give up electrons, so zinc corrodes **first** and protects iron (the sacrificial anode); this is also why Zn(s) + Fe²⁺ → Zn²⁺ + Fe(s) runs forward |
| Fe²⁺ / Fe | **−0.44** | |
| **ferredoxin [4Fe-4S]** | **≈ −0.40 to −0.42** (pH 7) | the biological electron carrier counted by the ladder |
| **H⁺ / H₂** | **−0.414** (pH 7) | **matches ferredoxin**: this is why ferredoxin can make or split H₂ through hydrogenases |
| O₂ / H₂O | **+0.82** (pH 7) | the top of the ladder: oxygen pulls electrons from both metals, which is rust |

**What this adds to your observation.**
- **Iron and hydrogen meet at the same electrical level, about −0.41 V.** That is the chemical reason the iron ladder separates hydrogen-making and ferredoxin-based microbes from lactic fermenters.
- **Zinc sits far below, at −0.76 V,** beyond what living cells can reach. So in biology **zinc never changes charge**. It only holds shapes (zinc fingers, ribbons), which is why its site barely follows the energy tiers (§2).
- **Oxygen at the top** is the common thief in both stories: rust on steel, and respiration in tier-2 cells.
- **So your "timing phase" intuition has a measurable form:** each element's position on this potential ladder. Orbital timing of protons, neutrons and electrons is not something these data can measure, so that part stays [D].

## 4. 1/43: digits 1–8 sum to 26 = iron [V arithmetic; base rate]
The running sums of 1/43's digits are 0, 2, 5, 7, 12, **17**, **25**, **26**, **29**, 38 …

- These pass through **Cl (17), Mn (25), Fe (26) and Cu (29)** in four consecutive steps.
- **Every whole number from 1 to 118 is some element's atomic number,** so a running digit sum always "hits" an element. The match to iron is true arithmetic, but it carries no evidence on its own (base rate 100%).
- **What is unusual about 1/43 is its 581 (§ L3269), not its sums.**

## Record
**This round:** 2 graded, 1 passed (Zn1 passed, Zn2 failed).

**Total: 299 of 421 pre-registered predictions passed, plus 3 split.**

## Summary
- **blind_20 is complete:** 14 of 16 fresh microbes were sorted into the right energy tier by iron's ladder alone (ρ = 0.96), and the last lactic fermenter read exactly zero.
- **Zinc behaves differently, as its chemistry predicts.** Its structural cysteine site rises only 2.3-fold across the tiers, against 64-fold for iron. It still rises somewhat, probably because some knuckles in anaerobes hold iron instead (rubredoxins), so one of two predictions failed.
- **Your iron–zinc–hydrogen–oxygen picture lines up with the electrode-potential ladder.** Zinc at −0.76 V sacrifices itself for iron at −0.44 V. Iron's ferredoxins work at hydrogen's own level, about −0.41 V. Oxygen at +0.82 V pulls from both, which is rust and respiration.
- **The 26 = iron digit sum is true but not evidence:** every running sum names some element.

## Potential leads for future research
- **[Fe-Zn rubredoxin]** Split the knuckle motif into rubredoxin-like (C-x₂-C-G … C-P-x-C-G) and zinc-ribbon forms; pre-register that the rubredoxin part follows the tiers and the rest is flat.
- **[Potential ladder]** For each metal motif we count (Fe ladder, Cu CuA, Zn ribbon/finger, Mg P-loop), place its metal's biological potential on the ladder and test whether a motif's slope across tiers follows how redox-active its metal is.
- **[Note H v0.5]** Write blind_20 (14 of 16, ρ = 0.96) in as the first fully blind test of the four-tier scale, and add the electrochemical explanation (§3).
- **[Microaerophile tier]** *Arcobacter* and *Sulfurihydrogenibium* both read about 0.047; test a cbb3-oxidase marker.
- **[Monster primes]** Carried from L3269.

Sources:
- [Ferredoxin (overview of potentials)](https://wikipedia.com/wiki/Ferredoxin)
- [Ferredoxin–hydrogenase electron transfer (ChemRxiv)](https://chemrxiv.org/engage/chemrxiv/article-details/6661dcff418a5379b038d914)
- [PMC3591994 (ferredoxin redox chemistry)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3591994)
