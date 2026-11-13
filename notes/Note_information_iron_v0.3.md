# Information iron is a switch, energy iron is a dial: DNA-repair [4Fe-4S] clusters vs the ferredoxin ladder across microbial genomes
### Note draft v0.3 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

*Companion to the iron-ladder manuscript. Every number comes from the DCF round reports L3377–L3385; pre-registrations and hashes are in the dcf-math ledger.*

## Question
- Cells use iron–sulfur clusters for two jobs:
  - moving **energy** (ferredoxins and ferredoxin-coupled enzymes, counted by the 3-3-4 ladder C-x₂-C-x₂-C-x₃-C);
  - guarding **stored information**: the DNA-repair glycosylases endonuclease III and MutY carry a [4Fe-4S] cluster in the "FCL" loop C-x₆-C-x₂-C-x₅-C, proposed to let them signal through DNA by charge transport (Barton and co-workers).
- Do the two uses scale together across genomes?

## Method
- **Gene calls:** label-free from raw DNA (`dcf_genefinder_mobile.py` v2.32).
- **Per genome:**
  - proteins carrying the FCL loop ("information iron");
  - ladders per 1,000 genes ("energy iron").
- **Script:** `dcf_infoiron_L3377.py`, frozen and hashed before the blind test.

## Results
**Development (37 graded genomes, L3377):**
| per 1,000 genes | lactic | O₂ | H₂ fermenters | Fd-based |
|---|---|---|---|---|
| energy iron | 0 | 4.5 | 14.6 | 40.8 |
| information iron | 0 | 0.48 | 0.56 | 1.08 |

FCL hits were mainly endonuclease III and MutY (validated from annotation after counting).

**Blind test (blind_24, 8 fresh genomes, L3381): 3 of 3 predictions passed.**
- **IF1:** all 4 lactic genomes have no FCL protein.
- **IF2:** all 4 iron users have 1–3.
- **IF3:** among the iron users, energy iron spans **41-fold** (1.15–46.7 per 1,000 genes); information iron spans only **1.4-fold** (0.46–0.66).

**Combined:** information iron is present in **32 of 32** iron-using genomes and absent from **12 of 13** lactic genomes.

**Why it is absent in lactic bacteria (L3385, annotation of graded genomes).** The enzymes are still there (endonuclease III in 9 of 13 lactic genomes, MutY in 8 of 13), but **their cluster cysteines are gone:**
| enzyme | lactic genomes | others |
|---|---|---|
| endonuclease III with the FCL loop | 1 of 9 (median 4 cysteines; *Lactobacillus* 0–1) | 57 of 64 (median 6) |
| MutY with the FCL loop | 0 of 8 (median **0** cysteines) | 32 of 38 (median 6) |

- **Streptococcal endonuclease III** keeps 2 of the 4 cluster cysteines.
- **Iron-free repair partners** (Fpg/MutM, UDG, Exo III, UvrABC, MutS/L, RecA) are present in all 13 lactic genomes.

## Prior art
- **Iron-free MutY homologues are known:**
  - Trasviña-Arenas *et al.* 2016, *FEBS J.* (doi 10.1111/febs.13608);
  - the 2025 MutYX structure from *Eggerthella* (PMC11722440), which notes a clusterless MutY clade "restricted to Lactobacillales" and proposes, as a hypothesis, that losing iron was an adaptation to very low iron.
- **Not found in the sources checked:**
  - **cluster-free endonuclease III in *Lactobacillus*** (0–1 cysteines);
  - a **genome-wide, blind test** showing that information iron is switched off exactly where energy iron is absent, and stays nearly constant where energy iron varies 41-fold.
- **Wider search (L3389):** no report of endonuclease III losing its cluster in lactic bacteria was found. The closest are the Pfam EndIII_4Fe-2S cluster domain, studies of the cluster's role in *E. coli*, *Deinococcus* and *Thermococcus* endonuclease III, the iron-free MutY papers, and Archibald 1983 ("*Lactobacillus plantarum*, an organism not requiring iron"). A blind test is pre-registered (L3389).

## Blind test of the cysteine loss (blind_25, L3389 → L3393): 1 of 3
| genome | endonuclease III (cysteines, iron loop) | MutY (cysteines, iron loop) |
|---|---|---|
| *Limosilactobacillus reuteri* | 5, **loop kept** | — |
| *Latilactobacillus sakei* | 6, **loop kept** | 2, lost |
| *Lactobacillus crispatus* | 1, lost | — |
| *Streptococcus suis* | 5, lost (partial) | **0**, lost |
| *Limosilactobacillus fermentum* | none annotated | none annotated |
| controls *Staphylococcus*, *Exiguobacterium*, *Listeria* | 6–8, loop kept (3/3) | 4, loop kept (3/3) |

- **LL1 FAIL** (2 of 4 gradable lactic genomes lost the loop); **LL2 PASS**; **LL3 FAIL** (lactic median 3.5 cysteines).
- **Revised reading.** Loss of the endonuclease III cluster is **lineage-specific**, not a general lactic trait:
  - lost in the *L. acidophilus*-group lactobacilli (*gasseri*, *johnsonii*, *helveticus*, *crispatus*) and in *L. rhamnosus*;
  - partly lost in streptococci;
  - **kept** in *L. salivarius*, *L. reuteri* and *L. sakei*.
- **MutY's cluster** was lost in every lactic MutY seen so far (development 0 of 8 with the loop; blind 0 of 2), consistent with the known Lactobacillales clade.

## Interpretation
- **Information iron is a switch.** A cell that uses iron keeps a nearly fixed, small set of repair clusters.
- **Energy iron is a dial,** tuned to the energy metabolism.
- **Lactic bacteria,** which grow with almost no iron, turned **both** off: they replaced their energy chemistry and stripped the iron ligands from their repair enzymes.

## Summary
- **Two uses of iron behave differently:** steady in DNA repair, variable in energy. This passed 3 of 3 blind predictions.
- **Some iron-free lactic bacteria keep their repair enzymes but have removed the iron-binding cysteines.** For MutY this was known and holds in every lactic MutY seen. For endonuclease III it is **lineage-specific** (blind test 1 of 3): lost in the acidophilus group and *L. rhamnosus*, kept in *L. reuteri*, *sakei* and *salivarius*.

## Potential leads for future research
- **[Lit-infoiron]** A broader literature search on endonuclease III cluster loss before submission.
- **[Ligand-loss blind]** Pre-register: in fresh Lactobacillales genomes, endonuclease III and MutY have ≤ 1 FCL cysteine motif, while iron users keep it.
- **[CRISPR]** Immune-memory arrays follow neither the switch nor clearly the dial (development, L3385); the thermophile confound must be separated first.
