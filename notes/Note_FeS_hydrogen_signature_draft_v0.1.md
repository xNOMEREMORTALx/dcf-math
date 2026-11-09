# Note H: an iron–sulfur signature of hydrogen metabolism, visible in raw genomes
### Draft v0.1 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

**Status.** Draft. Every number is from the cited pre-registered round. The reports are in Drive (`11-3-2026 handoff`) and in `dcf-math/rounds/` from L3181 on. Failures are kept.

---

## 1. Method (label-free)
1. **Find genes** with `dcf_genefinder_mobile.py` v2.31. It self-trains on the genome and uses no annotation.
2. **Translate** the predicted genes.
3. **Count C-x-x-C motifs per 1,000 amino acids** (`dcf_metals.py`). Two cysteines spaced this way are the usual ligand pair of iron–sulfur clusters (and of many zinc and redox sites).
4. **Cut:** 0.50, frozen in L3141 before any later test.

Annotation is read only after the tool numbers are written and hashed. It is used to grade, and to count annotated selenocysteine (Sec) codons.

## 2. Results in order, including the failures
| round | test | result |
|---|---|---|
| L3117 | 11 methanogens vs 7 aerobes | median density 1.07 vs 0.32 (3.4×); R 7.4 vs 3.8, p = 6 × 10⁻⁵ — **3/3 pass** |
| L3137 | anaerobes vs aerobes, blind | anaerobes above aerobes in 9 of 9 pairs — **4/4 pass** |
| L3145 | does Sec follow Fe–S? | ρ = 0.84; anaerobes 49 Sec, aerobes 0 — **4/5 pass** |
| L3165 | Fe–S predicts Sec **within** anaerobes | ρ = −0.10 — **failed** (2/5) |
| L3173 | Fe–S as an oxygen meter (facultatives in between) | fermenting anaerobes read **low** — **failed** in part (2/4) |
| **L3181/L3185** | **hydrogen handlers vs fermenters and non-H2 aerobes** | **all 5 H2 handlers above all 5 others; p = 1/252 — 5/5 pass** |

## 3. The L3185 table (blind, 10 genomes)
| group | genome | CxxC per 1,000 aa | Sec |
|---|---|---|---|
| H2, anaerobe | *Desulforapulum autotrophicum* | 0.93 | 27 |
| H2, **aerobe** | ***Hydrogenobacter thermophilus*** | 0.86 | 2 |
| H2, anaerobe | *Acetobacterium woodii* | 0.82 | 2 |
| H2, anaerobe | *Clostridium ljungdahlii* | 0.77 | 12 |
| H2, aerobe | *Cupriavidus necator* chr 1 | 0.40 | 0 |
| aerobe | *Pseudomonas protegens* Pf-5 | 0.33 | 0 |
| aerobe | *Bordetella bronchiseptica* | 0.32 | 0 |
| fermenter | *Streptococcus mutans* | 0.25 | 0 |
| fermenter | *Lactobacillus acidophilus* | 0.22 | 0 |
| fermenter | *Leuconostoc mesenteroides* | 0.14 | 0 |

## 4. Reading
**The claim this supports.** The density measures how much of a proteome is built for **Fe–S-heavy energy chemistry**. Hydrogen metabolism is its clearest driver:
- methanogens, acetogens and sulfate reducers read high;
- an oxygen-breathing hydrogen oxidiser reads high too;
- fermenters read low, even though they live without oxygen.

**What it is not.**
- **Not an oxygen meter** (L3173).
- **Not a predictor of Sec within anaerobes** (L3165).

**Known biology this is consistent with.** Hydrogenases, ferredoxins and formate dehydrogenases are Fe–S proteins. The point here is only that the signal is visible **from raw DNA with a phone-sized pipeline**, and was tested blind.

## 5. Open confounds
- **Carbon fixation.** *Hydrogenobacter* also uses the Fe–S-rich reductive TCA cycle. L3189 (blind_16) separates the two:
  - green sulfur bacteria: reductive TCA cycle without being mainly H2-driven;
  - *Xanthobacter*: Calvin cycle plus H2;
  - Calvin-cycle aerobes without H2 metabolism.
- **Plasmids.** *Cupriavidus*'s hydrogenases are on megaplasmid pHG1. L3189 reads it separately.
- **Sample size.** Groups are 3–11 genomes, hand-chosen from the literature.
- **Literature check needed** before any novelty claim. Genome-wide CxxC or Fe–S-domain counts by lifestyle may already be published.

## Summary
- **A phone-sized, label-free pipeline sees iron–sulfur energy chemistry in raw DNA.**
- **The best-supported reading after six pre-registered rounds:** the signal tracks hydrogen metabolism, not oxygen. It is high in hydrogen users whether or not they breathe oxygen, and low in fermenters.
- **Two earlier, simpler readings failed blind and are kept on record:** oxygen meter, and Sec predictor within anaerobes.

## Potential leads for future research
- **[Fe-rTCA]** Grade L3189 (blind_16): carbon fixation vs hydrogen.
- **[Lit-FeS]** Literature search for genome-wide Fe–S or CxxC content by energy metabolism, before any submission.
- **[Fe-domain]** Replace the motif count with a small built-in Fe–S domain matcher (ferredoxin CxxCxxCxxxCP), to see if the signal sharpens.
- **[Fe-H2 n]** A larger blind set (20+ genomes, chosen by a rule rather than by hand).
