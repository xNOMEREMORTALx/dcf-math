# Note H: an iron–sulfur signature of ferredoxin-based (low-potential) metabolism, visible in raw genomes
### Draft v0.6 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**v0.6 adds:**
- the photosynthesis test (blind_22, §4h): oxygenic cyanobacteria read tier 2 (4 of 4), and the 4Fe-4S-based *Heliobacterium* reads tier 4;
- the rubredoxin and microaerophile results (§4g);
- **the closest prior art found so far, Campbell, Bennett & Silberg 2019 (§4e).**

**v0.5: the four-tier scale passed its blind test.** On blind_20 (16 fresh genomes, seven phyla, labels and cuts frozen before download) the ladder put **14 of 16** in the right tier, Spearman ρ = 0.96, all five predictions passed (L3269/L3273). Zinc's structural Cys₄ site, counted the same way, climbs only 2.3× across the tiers against iron's 64× (§4f, Figure 1). The tool is released as `dcf_redox.py` (dcf-genefinder) and phone menu 30.

**v0.4 changes the marker.** The main measure is now the **3-3-4 ferredoxin ladder** (C-x₂-C-x₂-C-x₃-C per 1,000 aa, §1b), which separated every blind lineage pair 3–8 times more sharply than plain CxxC (L3241). Readings fall on a **four-tier scale** (§4d), which passed its blind test (§4d-bis). A dedicated literature check (L3265, §4e) found no published motif-based (Fe–S/CuA) classifier of microbial energy metabolism.

**v0.3 changed the headline.** L3213 showed that hydrogen use *as such* does not raise the reading in Calvin-cycle aerobes. The v0.2 title ("…of hydrogen metabolism") is withdrawn; the reason is in §4c.

**Status.** Draft. Every number is from the cited pre-registered round. The reports are in Drive (`11-3-2026 handoff`) and in `dcf-math/rounds/` from L3181 on. Failures are kept.

---

## 1. Method (label-free)
1. **Find genes** with `dcf_genefinder_mobile.py` v2.31. It self-trains on the genome and uses no annotation.
2. **Translate** the predicted genes.
3. **Count C-x-x-C motifs per 1,000 amino acids** (`dcf_metals.py`). Two cysteines spaced this way are the usual ligand pair of iron–sulfur clusters (and of many zinc and redox sites).
4. **Cut:** 0.50, frozen in L3141 before any later test.

## 1b. The sharper marker: the 3-3-4 ladder (L3225, frozen L3237)
- **Motif:** C-x₂-C-x₂-C-x₃-C, counted overlapping, per 1,000 aa of the predicted proteome (`rounds/dcf_ladder_L3237.py`, SHA-256 `68c51f7b…7d91`).
- **Why:** this is the spacing of the cysteines that bind a 4Fe-4S cluster in bacterial ferredoxins and in the ferredoxin-like domains of hydrogenases, CODH, PFOR and heterodisulfide reductase. Plain CxxC also counts zinc fingers, thioredoxins and many other sites.
- **Example of the difference:** *Haloarcula* reads 0.62 on CxxC (above the old 0.50 cut) but only 0.019 on the ladder (L3241).

Annotation is read only after the tool numbers are written and hashed. It is used to grade, and to count annotated selenocysteine (Sec) codons.

## 2. Results in order, including the failures
| round | test | result |
|---|---|---|
| L3117 | 11 methanogens vs 7 aerobes | median density 1.07 vs 0.32 (3.4×); R 7.4 vs 3.8, p = 6 × 10⁻⁵ — **3/3 pass** |
| L3137 | anaerobes vs aerobes, blind | anaerobes above aerobes in 9 of 9 pairs — **4/4 pass** |
| L3145 | does Sec follow Fe–S? | ρ = 0.84; anaerobes 49 Sec, aerobes 0 — **4/5 pass** |
| L3165 | Fe–S predicts Sec **within** anaerobes | ρ = −0.10 — **failed** (2/5) |
| L3173 | Fe–S as an oxygen meter (facultatives in between) | fermenting anaerobes read **low** — **failed** in part (2/4) |
| L3181/L3185 | hydrogen handlers vs fermenters and non-H2 aerobes | all 5 H2 handlers above all 5 others; p = 1/252 — **5/5 pass** |
| **L3213 (blind_16)** | **carbon fixation vs hydrogen** | green sulfur (rTCA) high; pHG1 plasmid high; **but the Calvin + H2 aerobe *Xanthobacter* read low (0.35) and a Calvin non-H2 aerobe read 0.51 — 3/5** |
| **L3213 (blind_17)** | **H2-evolving vs lactic fermenters** | **4 H2 fermenters 0.56–0.77, 4 lactic 0.16–0.29; 16/16 pairs, p = 1/70 — 4/4 pass** |
| L3221 (blind_18) | lineage-matched pairs | sulfate reducers above their phylum partners (0.96 vs 0.42; 0.89 vs 0.31); but aerotolerant *Arcobacter* read **0.57** (D2 failed); *Nautilia* pending |
| **L3229/L3241 (blind_18–19)** | **six lineage-matched pairs, five phyla** | **ferredoxin-based member higher in 6 of 6** (blind_19: 1.08 vs 0.62, 1.09 vs 0.42, 0.45 vs 0.28); the 3-3-4 ladder separates every blind_19 pair more sharply than CxxC (4.7–8.4× vs 1.6–2.6×) |
| L3257 | label-free three-way call (Fd / O2 / neither) from ladder ≥ 0.06 plus copper CuA, 23 held-out genomes | **18 of 23** correct (baseline 13); O2 3 of 4; lactic 6 of 6 — **2 of 3 pass**; misses were H2 fermenters at 0.02–0.06, revealing the four tiers (§4d) |

## 3. The L3185 table (blind, 10 genomes)
| group | genome | CxxC per 1,000 aa | Sec |
|---|---|---|---|
| H2, anaerobe | *Desulforapulum autotrophicum* | 0.93 | 26 |
| H2, **aerobe** | ***Hydrogenobacter thermophilus*** | 0.86 | 1 |
| H2, anaerobe | *Acetobacterium woodii* | 0.82 | 1 |
| H2, anaerobe | *Clostridium ljungdahlii* | 0.77 | 9 |
| H2, aerobe | *Cupriavidus necator* chr 1 | 0.40 | 0 |
| aerobe | *Pseudomonas protegens* Pf-5 | 0.33 | 0 |
| aerobe | *Bordetella bronchiseptica* | 0.32 | 0 |
| fermenter | *Streptococcus mutans* | 0.25 | 0 |
| fermenter | *Lactobacillus acidophilus* | 0.22 | 0 |
| fermenter | *Leuconostoc mesenteroides* | 0.14 | 0 |

Sec = annotated selenocysteine codons (`transl_except`), corrected in L3197; the first count also included tRNA-Sec anticodon lines.

## 4. Reading
**The claim this supports.** The density measures how much of a proteome is built for **Fe–S-heavy energy chemistry**. Hydrogen metabolism is its clearest driver:
- methanogens, acetogens and sulfate reducers read high;
- an oxygen-breathing hydrogen oxidiser reads high too;
- fermenters read low, even though they live without oxygen.

**What it is not.**
- **Not an oxygen meter** (L3173).
- **Not a predictor of Sec within anaerobes** (L3165).

**Known biology this is consistent with.** Hydrogenases, ferredoxins and formate dehydrogenases are Fe–S proteins. The point here is only that the signal is visible **from raw DNA with a phone-sized pipeline**, and was tested blind.

## 4b. Prior art (found in L3193) and a caveat on "fermenters"
**Prior art.** Andreini, Rosato and Banci (PLoS ONE 2017, e0171279) predicted Fe–S proteins in 434 prokaryotic genomes from Pfam profiles.
- **Their numbers:** aerobes 1.8 ± 0.6% of genes; high-content anaerobes 4.7 ± 1.0%. They also define low-content aerotolerant anaerobes (< 3%; mean 2.2 ± 0.4%, 36 genomes).
- **Their explanation:** the extra Fe–S proteins are mostly in energy production and conversion.
- **So the anaerobe-versus-aerobe contrast, and the existence of low-Fe–S anaerobes, are already known.**
- **What this note adds is narrower:**
  - the signal is recovered label-free from raw DNA with a phone-sized pipeline;
  - it was tested blind;
  - aerobic hydrogen oxidisers read like anaerobes (L3185). The paper does not discuss hydrogenases.

**Caveat on "fermenters".** The fermenters in L3185 are lactic acid bacteria, which do not make H2.
- **H2-evolving clostridial fermenters read above the cut** in L3165: *C. kluyveri* 0.72 and *L. phytofermentans* 0.64.
- **The low readers of L3173** were *Fusobacterium* and *Treponema*.
- **So "fermenters read low" holds for lactic fermenters; it is not general.** That fits the hydrogen reading, but it was noticed after the fact and is [D] until tested (lead [Fe-ferment H2]).

## 4c. L3213: what the two new blind sets show
| group | genome | CxxC per 1,000 aa | Sec |
|---|---|---|---|
| rTCA, anaerobe (green sulfur) | *Chlorobaculum tepidum* | **0.69** | 0 |
| rTCA, anaerobe (green sulfur) | *Chlorobium chlorochromatii* | **0.61** | 0 |
| H2-evolving fermenter | *Ruminococcus albus* 7 | **0.77** | 0 |
| H2-evolving fermenter | *Caldicellulosiruptor saccharolyticus* | **0.66** | 0 |
| H2-evolving fermenter | *Clostridium beijerinckii* | **0.60** | 0 |
| H2-evolving fermenter | *Caldanaerobacter tengcongensis* | **0.56** | 3 |
| Calvin, non-H2 aerobe | *Nitrosospira multiformis* | 0.51 | 0 |
| Calvin, non-H2 aerobe | *Halothiobacillus neapolitanus* | 0.43 | 0 |
| **Calvin + H2, aerobe** | ***Xanthobacter* Py2** | **0.35** | **1** |
| lactic fermenter | *S. thermophilus* | 0.29 | 0 |
| lactic fermenter | *L. delbrueckii* | 0.27 | 0 |
| lactic fermenter | *P. pentosaceus* | 0.23 | 0 |
| lactic fermenter | *O. oeni* | 0.16 | 0 |
| plasmid | *Cupriavidus* pHG1 (hydrogenase plasmid) | 0.90 | 0 |

**The revised reading.**
- **Hydrogen use alone does not do it.**
  - *Xanthobacter* oxidises H2 with oxygen yet reads like an ordinary aerobe (0.35).
  - *Cupriavidus* chromosome 1 read only 0.40 (L3185).
  - The one aerobe that read high, *Hydrogenobacter*, also runs the reductive TCA cycle.
- **What reads high is ferredoxin-based, low-potential metabolism:**
  - the reductive TCA cycle (green sulfur bacteria, *Hydrogenobacter*);
  - the Wood–Ljungdahl pathway (acetogens);
  - sulfate reduction;
  - methanogenesis;
  - ferredoxin-dependent hydrogen *production* in fermenters (*Ruminococcus*, *Caldicellulosiruptor*, *Clostridium*).
- **Lactic fermenters,** which use no ferredoxin-based energy step, read lowest.
- **pHG1 reads 0.90.** The hydrogenase genes concentrate Fe–S proteins locally, but a few such operons barely move a whole-genome average.
- **Selenocysteine:** *Xanthobacter* carries one Sec codon, a second aerobe with Sec. Both such aerobes (*Hydrogenobacter*, *Xanthobacter*) are H2/formate users, consistent with Sec riding on formate dehydrogenase rather than on oxygen-free life as such [D].

This reading is formed **after** L3213. It is [D] until tested blind (lead [Fe-Fd]).

**L3221 update.** Within two phyla, the ferredoxin-based member read far above its relative (2 of 2 pairs so far). *Arcobacter*, labelled aerotolerant and oxidative, read 0.57. Campylobacterota, even microaerophiles, run ferredoxin-dependent 2-oxoacid oxidoreductases and several anaerobic respirations, so the label was too simple. That risk was declared in advance; the failure is kept.

## 4d. The four-tier scale (found after the fact in L3257; blind test pending)
| tier | ladder per 1,000 aa (35 genomes) | who |
|---|---|---|
| 1 | 0–0.002 | lactic fermenters (no ferredoxin step) |
| 2 | 0.007–0.025 | oxygen respirers |
| 3 | 0.021–0.058 | H2-making fermenters (ferredoxin feeds a hydrogenase), *Parabacteroides*, *Arcobacter* (0.046) |
| 4 | 0.063–0.132 | ferredoxin-based respirers and autotrophs (sulfate reducers, acetogens, methanogens, rTCA, organohalide respirers) |

- **Tiers 2 and 3 overlap** (0.021–0.025); the frozen blind_20 cuts are 0.0045, 0.023 and 0.060.
- **Reading [D]:** the ladder density rises with how central ferredoxin is to a cell's energy budget: absent (lactic), present for housekeeping (aerobes), one energy step (H2 fermenters), the core of the energy pathway (tier 4).
- **Test:** blind_20 (16 fresh genomes, 4 per tier, pre-registered L3265 before download).

## 4d-bis. Blind test of the scale (blind_20, L3265 → L3269/L3273)
| tier | genomes (ladder per 1,000 aa) | median |
|---|---|---|
| 1 lactic | *L. rhamnosus* 0.0024, *S. agalactiae* 0.0016, *L. salivarius* 0.0039, *L. gasseri* 0.0000 | 0.0020 |
| 2 O2 | *Paracoccus* 0.0110, *Halomonas* 0.0139, *Burkholderia* 0.0158, *Azotobacter* 0.0226 | 0.0149 |
| 3 H2 fermenters | *R. cellulolyticum* 0.0352, *Fervidobacterium* 0.0426, *A. thermocellus* 0.0441, ***C. botulinum* 0.0601 ✗** | 0.0433 |
| 4 Fd-based | ***Sulfurihydrogenibium* 0.0474 ✗**, *Thermodesulfovibrio* 0.1093, *Syntrophobacter* 0.1464, *Methanobrevibacter* 0.2177 | 0.1278 |

- T1–T5 all passed (14 of 16 correct; chance ≈ 4).
- Both misses sit at a boundary: *C. botulinum* is over the cut by 0.0001; *Sulfurihydrogenibium* is a microaerophile (declared risk), like *Arcobacter* (0.046) before it. A microaerophile test is pre-registered (blind_21, L3281).
- *Fervidobacterium* (Thermotogota) is the first tier-3 genome outside the Firmicutes and reads squarely in tier 3.

## 4f. Iron vs zinc (L3273, Figure 1)
- Zinc ribbon C-x₂-C-x₉₋₂₀-C-x₂-C (ladder cysteines masked): tier medians 0.038 / 0.034 / 0.059 / 0.089; tier 4 / tier 1 = **2.3×**, against the ladder's **64×** (Zn1 passed). It does not separate tiers 1 and 2.
- It still rises in tiers 3–4 (ρ = 0.74; Zn2 failed). **Correction (L3281):** the rubredoxin explanation given in L3273 is not supported. Ribbon matches split by knuckle type climb about 2× in both halves; the 9–20 spacing cannot match a classic rubredoxin (~29 residues). The rise is smaller than the background C-x-x-C rise (about 4×).
- **The classic rubredoxin spacing (C-x₂-C-G-x₂₄₋₃₂-C-x₂-C-G, an iron site) behaves like iron:** 21× across the tiers in development (seen genomes); a blind test is pre-registered (L3281).
- **Chemistry:** Zn²⁺/Zn −0.76 V lies outside biological reach, so zinc sites are structural; [4Fe-4S] ferredoxins work near −0.41 V, the H⁺/H₂ potential at pH 7.

**Figure 1.** `figures/L3277_iron_zinc_tiers.png`: blind_20 iron ladder and zinc ribbon by tier, with medians and the frozen cuts.

## 4g. Rubredoxin, zinc and low-oxygen genomes (blind_21, L3285)
- **The rubredoxin iron knuckle (C-x₂-C-G-x₂₄₋₃₂-C-x₂-C-G) behaves like iron, blind:** absent in lactic fermenters, highest in tier-4 controls, ρ = 0.73 with the ladder. The zinc ribbon climbed under 4×, against the ladder's 160× (second blind confirmation).
- **Low-oxygen respirers did not form a separate band inside tier 3** (M1, M2 and later E1, E2 failed). They read 0.046–0.089. Lifestyle labels ("microaerophile") failed three times; labels should come from enzymes.

## 4h. Photosynthesis (blind_22, L3293)
| genome | photosynthesis type | ladder |
|---|---|---|
| *Gloeobacter*, *Nostoc*, *Thermosynechococcus*, *Synechococcus* | oxygenic, plant-type [2Fe-2S] ferredoxin | 0.013–0.021 (tier 2, 4 of 4) |
| *Heliobacterium modesticaldum* | anoxygenic, type-I reaction centre with [4Fe-4S] clusters | **0.095 (tier 4)** |

**The ladder therefore measures the 4Fe-4S ferredoxin chemistry,** not "uses ferredoxin" or "does photosynthesis". *Prochlorococcus*, run by Gary on his phone (development), read 0.015.

## 4e. Literature check (L3265, L3317)
- **Closest prior art: Campbell, Bennett & Silberg 2019** (*Frontiers in Energy Research* 7:79, "Evolutionary relationships between low potential ferredoxin and flavodoxin electron carriers").
  - They mined 7,079 genomes for small electron-carrier genes (≤ 200 aa).
  - They found that **[4Fe-4S] ferredoxins dominate in anaerobes, while flavodoxins and [2Fe-2S] ferredoxins rise in relative abundance with oxygen tolerance**, though "[4Fe-4S] Fd usage is not abolished in aerobes".
  - Our photosynthesis result (§4h) agrees with this.
- **What this note adds beyond Campbell 2019:**
  1. a **motif density over the whole predicted proteome**, which includes the ferredoxin-like domains inside large enzymes (hydrogenases, CODH, PFOR, Hdr), computed **label-free from raw DNA** with our own gene calls;
  2. **energy-metabolism tiers, not oxygen classes:** the ladder separates lactic fermenters from H₂-making fermenters, both anaerobes, about 20-fold, which an oxygen-tolerance classification cannot;
  3. **blind, pre-registered tests** (blind_20: 14 of 16 tiers, ρ = 0.96; photosynthesis 2 of 2; six lineage pairs).
- **Nzuza *et al.* 2021** ("Diversification of Ferredoxins across Living Organisms", *Curr. Issues Mol. Biol.* 43(3):1374–1390), read in L3321:
  - they mined 468 genomes (241 Alphaproteobacteria, 227 Firmicutes) **chosen for carrying P450s**, and classified ferredoxins by cluster type with variable cysteine-spacing motifs (e.g. 4Fe-4S C-x₂₋₅-C-x₂₋₃-C-x₃₀₋₄₅-C-P);
  - **they do not classify genomes by energy metabolism or measure oxygen use.** Their anaerobe/aerobe statements cite Campbell 2019.
  - Not overlapping prior art for the tier scale.
- **Development (L3321):** about three quarters of ladders sit in proteins over 200 aa. Large-protein ladders separate oxygen respirers from H₂ fermenters 2.9-fold; Campbell-style small-ferredoxin counts only 1.25-fold. Blind test pre-registered (blind_23).
- **Andreini *et al.* 2017** (above) remains the closest prior art for the Fe–S contrast.
- **An annotation-free oxygen-use predictor** (bioRxiv 10.1101/2024.01.16.575888) classifies ~3,300 genomes three ways (aerobe / anaerobe / facultative) at ~70% from amino-acid 3-mers, nucleotide 5-mers and protein-language embeddings. It does not use or mention Fe–S motifs, ferredoxin, CxxC, copper or CuA. Its classes are oxygen classes, which this note found the ladder does **not** track (L3173).
- **No paper was found** that sorts raw genomes by ferredoxin-based metabolism from one iron motif and one copper motif. Absence of a search hit is not proof of novelty; a specialist check (e.g. ferredoxin-family surveys, Fd-dependent metabolism reviews) is still needed before submission.

## 5. Open confounds
- **Phylogeny.** Partly addressed: the ferredoxin-based member is higher in **6 of 6 lineage-matched pairs from five phyla** (L3229, L3241). Tier 1 vs tier 3 is still largely Lactobacillales vs Clostridia; blind_20 adds Fervidobacterium (Thermotogota) to tier 3.
- **The 0.50 cut is not a sharp boundary.** *Nitrosospira* (Calvin, non-H2 aerobe) read 0.51.
- **Sample size.** Groups are 3–11 genomes, hand-chosen from the literature.
- **Literature:** see §4b. The anaerobe/aerobe contrast is published (Andreini et al. 2017); only the label-free, blind and hydrogen-specific parts may be new.

## Summary
- **A phone-sized, label-free pipeline sees iron–sulfur energy chemistry in raw DNA.**
- **The best-supported reading after eight pre-registered rounds:** the signal tracks **ferredoxin-based, low-potential metabolism.** That covers the reductive TCA cycle, Wood–Ljungdahl, sulfate reduction, methanogenesis and H2-producing fermentation. It does not track oxygen, and it does not track hydrogen use as such.
- **The v0.2 hydrogen headline was revised by its own blind test** (L3213: *Xanthobacter* 0.35).
- **v0.4–0.5: the 3-3-4 ferredoxin ladder is the sharper measure** (6 of 6 lineage pairs; 3–8× separation), and its four-tier scale **passed blind: 14 of 16 fresh genomes, ρ = 0.96**. Zinc's structural site climbs 28 times less steeply.
- **Three simpler readings failed blind and are kept on record:** oxygen meter, Sec predictor within anaerobes, and hydrogen use as such.

## Potential leads for future research
- **[Fe-Fd]** Pre-register the ferredoxin reading on lineage-matched pairs (e.g. a Clostridium that ferments with H2 vs a non-H2 Clostridium; an rTCA aerobe vs a Calvin aerobe in one phylum).
- **[Lit-FeS b]** Compare per-genome numbers with Andreini et al. 2017's table for any shared organisms (does CxxC density track their Fe–S percentage?).
- **[Fe-domain]** Done in v0.4 as the 3-3-4 ladder (§1b). Next: test whether adding the trailing P (CxxCxxCxxxCP) sharpens it further.
- **[blind_21]** Microaerophile band and the rubredoxin knuckle (pre-registered L3281).
- **[Lit-redox b]** Partly done (L3317): cite Campbell 2019; still to read the 2021 CIMB ferredoxin survey.
- **[Fe-H2 n]** A larger blind set (20+ genomes, chosen by a rule rather than by hand).
