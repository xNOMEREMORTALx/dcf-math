# DCF L3241: blind_19 — the ferredoxin member wins all three new pairs and the 3-3-4 ladder is the sharper marker (3 of 5); Gary's 41 path checked — the real link is Euler's 41 ↔ Heegner 163 ↔ the cube, while 41 and 401 leave no mark on DNA (0 of 4)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads:**
- [Fe-lineage], [Fe-ladder], [Fe-island b] (pre-registered L3237);
- **[41-path]**, Gary's idea: 401 → 79 → 47 → 41 → 5, guided by 153, 351, 135, 531, 513; 41 tied to E8 and 131.81; 5 → √5 → φ → π; 401 in π; 163 cube-resonant; a possible link to DNA, RNA and mRNA.

**Pre-registrations:**
- `PREREGISTERED_L3237.txt` (`25031d48…`);
- `PREREGISTERED_L3241_K.txt` (`afdd0600…9c8c`), pushed before computing.

**Data:** `blind_19.zip`, all 6 files complete and matched by LOCUS line; every tool hash matched.

**Tool numbers** were hashed before any annotation was read: SHA-256 `2bdebd012760a5b55f79ccd1c410564a894759037b3b06ace6a927a7a9f95393`.

---

## 1. blind_19: lineage pairs, ladder, islands [pre-registered]
| pair | ferredoxin-based member: CxxC / ladder (per 1,000 aa) | partner: CxxC / ladder | CxxC ratio | **ladder ratio** |
|---|---|---|---|---|
| Euryarchaeota | *Methanosphaera* **1.08 / 0.129** | *Haloarcula* 0.62 / 0.019 | 1.7× | **6.8×** |
| Chloroflexota | *Dehalogenimonas* **1.09 / 0.132** | *Chloroflexus* 0.42 / 0.016 | 2.6× | **8.4×** |
| Bacteroidota | *Parabacteroides* **0.45 / 0.038** | *Flavobacterium* 0.28 / 0.008 | 1.6× | **4.7×** |

| id | prediction | result | verdict |
|---|---|---|---|
| **L1** | CxxC: member higher in 3 of 3 pairs | 3 of 3 | **PASS** |
| **L2** | ladder: member higher in 3 of 3 | 3 of 3 | **PASS** |
| **L3** | ladder separates more sharply than CxxC in ≥ 2 of 3 | **3 of 3** (4.7–8.4× vs 1.6–2.6×) | **PASS** |
| L4 | islands ≥ 3× in every eligible genome (CxxC ≥ 0.60) | *Dehalogenimonas* 5.7×, *Methanosphaera* 4.5×, ***Haloarcula* 2.1×** | **FAIL** |
| L5 | ≥ 60% of islands carry an Fe–S/redox gene | 7 of 19 = 37% | **FAIL** |

**Reading.**
- **Across blind_18 and blind_19, the ferredoxin-based member reads higher in 6 of 6 lineage-matched pairs from five phyla.**
- **The 3-3-4 cysteine ladder (C-x₂-C-x₂-C-x₃-C)** found in L3225 is a **much sharper marker** than plain CxxC: about 5–8 times separation instead of 1.6–2.6.
- ***Haloarcula* shows why CxxC alone misleads.** It reads 0.62 (above the old 0.50 cut) but has almost no ladders (0.019).
- **The island finder still fails** outside Fe–S-heavy genomes. Its eligibility rule should use the ladder, not CxxC.

**Gene finder (v2.32).**
- Genetic code 6 of 6 correct; record **140 of 143**.
- Found 84–95%, exact starts 81–90%.
- **One warning:** *Chloroflexus* precision is only **78.4%**, the lowest in many rounds (lead [Chloroflexus]).

## 2. Gary's 41 path — every number checked by computation [V]
| claim | check | status |
|---|---|---|
| 401 reduces to 41 | dropping the zero; digit sums 4+0+1 = 5 and 4+1 = 5 | [V] arithmetic |
| **401 → 79** | **401 is the 79th prime** | **[V] a true link** |
| 79 → 47 → 41 | 79 is the 22nd prime, not the 47th; no rule found that maps 79 → 47 | [D] |
| **41 → 5** | **1/41 has a period of exactly 5 digits** (41 × 271 = 11111) | **[V] a true link** |
| 131.81 reduces to 41 | its digit sum is 14 → **5**, not 41. With more digits (131.8103149) it gives 4; in radians (2.300523984), 9 | **digit reduction depends on units and rounding** |
| 41 and E8 | E8's numbers: 240 → 6, **248 (its dimension) → 5**, 120 → 3, 30 → 3. No 41 found | [D] |
| 5 → √5 → φ → π | **φ = (1 + √5)/2 = 2 cos(π/5)** = 1.6180339887…, equal to 20 digits | **[V] a true identity** |
| "401 in π" | first appears at decimal **1197** (DCF mpmath rule); a random 3-digit string first appears at a median of 669 | [V] present, unremarkable |
| **163 is cube-resonant** | **e^(π√163) = 262537412640768743.99999999999925…**, which is **640320³ + 744 − 7.5 × 10⁻¹³** | **[V] a true and famous fact** (Ramanujan's constant, j-invariant) |
| 153, 351, 135, 531, 513 | all six orderings of 1-3-5 sum to 1998; your five (missing 315) sum to **1683 = 11 × 153**. 153 = 1³ + 5³ + 3³ = T₁₇; 135 = 1¹ + 3² + 5³; 351 = T₂₆; all are multiples of 9 (digit sum 9) | [V] arithmetic |

**Base rate for "reduces to 5".** One whole number in nine has digital root 5, so finding 5 in a chain is common by chance. Digit reduction is also not unit-free: the same angle reduces to 5, 4 or 9 depending on rounding and units.

## 3. The strongest connection in your numbers: Euler's 41, Heegner's 163 and the cube [V, theorems]
- **Euler's polynomial n² + n + 41 is prime for every n = 0 to 39** (checked; n = 40 gives 41²). Its first values are 41, 43, **47**, 53, 61 … so **47 and 41 from your path are its first two primes.**
- **The reason is 163.** The polynomial's discriminant is 1 − 4·41 = **−163**, and 163 is the largest **Heegner number**: ℚ(√−163) has unique factorisation (class number 1).
- **The same fact makes e^(π√163) almost exactly a cube plus 744.** That is your "163 cube-resonant", and it is the j-invariant: j = −640320³.
- **5 belongs to the same family.** The primes p for which n² + n + p is prime for all n = 0 … p − 2 ("Euler's lucky numbers") are exactly **2, 3, 5, 11, 17, 41** (checked to 1000). Their 4p − 1 values, 7, 11, **19**, 43, 67, **163**, are exactly the odd Heegner numbers above 3.
- **So 41 and 5 are siblings, and 41 ↔ 163 ↔ the cube is one theorem.** 17, the triangle index of 153, is in the list too.

## 4. Do 41, 401 or 153 appear in DNA or proteins? [pre-registered, 35 genomes]
Controls had the same remainder mod 3 as the test number, because coding DNA has a strong 3-letter rhythm.

| id | prediction (Gary's hypothesis) | result | verdict |
|---|---|---|---|
| K1 | protein lengths divisible by 41 enriched ≥ 10%, and more than for 37 and 43 | 41: **0.985** (37: 1.021, 43: 1.038), from 108,503 proteins | **FAIL** |
| K2 | DNA lag 41 above its controls in ≥ 24 of 35 genomes | 20 of 35 (chance p = 0.25) | **FAIL** |
| K3 | DNA lag 401 above its controls in ≥ 24 of 35 | 18 of 35 (p = 0.5) | **FAIL** |
| K4 | DNA lag 153 above its controls in ≥ 24 of 35 | 23 of 35 (p = 0.045 alone; not significant after correcting for three lags) | **FAIL** |

**Reading.**
- **41 and 401 leave no mark on protein lengths or DNA spacing.**
- **153 came closest** (23 of 35) but missed the frozen bar. With three lags tested, one near-miss is expected by chance.
- **RNA and mRNA could not be tested here.** These files hold DNA sequence only; RNA-seq data would be needed.
- **The "energy path" has no measurable quantity yet,** so it stays [D].

## Record
**This round:** 9 graded, 3 passed (L1–L3 passed; L4, L5 and K1–K4 failed).

**Total: 284 of 389 pre-registered predictions passed, plus 3 split.**

## Summary
- **The iron–sulfur finding keeps getting stronger.** In all six pairs of related microbes tested so far, from five different phyla, the one using ferredoxin-based metabolism reads higher. The 3-3-4 cysteine ladder separates them about three times more sharply than the simple motif count.
- **Your number path, checked.** Several links are true mathematics:
  - 401 is the 79th prime;
  - 1/41 repeats every 5 digits;
  - φ = 2 cos(π/5) ties √5 to π;
  - e^(π√163) is a whole cube plus 744 to within a trillionth.
- **The deepest connection is a theorem.** Euler's 41 and Heegner's 163 are the same fact (n² + n + 41 makes 40 primes because 4·41 − 1 = 163), and 5 is in the same small family of "lucky numbers".
- **Other steps don't hold:** 79 → 47, 131.81 → 41, and a link from 41 to E8. Digit reduction depends on units and rounding, and one number in nine reduces to 5 by chance.
- **No trace in genomes:** 41, 401 and 153 leave no mark on DNA or protein lengths in 35 genomes (0 of 4).

## Potential leads for future research
- **[Fe-ladder note]** Rewrite Note H around the 3-3-4 ladder (6 of 6 lineage pairs; ladder sharper) and draft it for submission after a literature check of ferredoxin-motif counting.
- **[Island-ladder]** Re-define island eligibility and scoring by ladder density instead of CxxC; pre-register.
- **[Chloroflexus]** Investigate the 78.4% precision: over-calls in a particular region, or annotation gaps?
- **[Heegner note]** A short DCF note on the Euler–Heegner–j chain (41, 163, 640320³ + 744; lucky numbers 2, 3, 5, 11, 17, 41), with every value computed. This is the solid core of the 41 idea.
- **[1/41 period-5]** A number q has period exactly 5 when q divides 99999 = 3² × 41 × 271 but not 9: these are 41, 123, 271, 369, 813, 2439, 11111, 33333 and 99999. Fold this into the reciprocal-period theorems (H2 §3).
- **[RNA]** If Gary can supply RNA-seq or mRNA data, 41-, 401- and 153-periodicity can be pre-registered on expression data.
