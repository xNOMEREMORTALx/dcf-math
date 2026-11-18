# The cryptochrome tryptophan chain predates nervous systems: a pre-registered sequence survey from single-celled relatives to birds
### Manuscript 4 (short note), draft v0.5 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026
*Every number comes from a committed output (`dcf-math/rounds/` L3753–L3797). Pre-registrations are hashed in `preregistrations/LEDGER.md`. Failures are reported.*

## Abstract
**Background:** in the European robin's cryptochrome 4, light drives an electron along four tryptophans (TrpA–D) to the flavin. This forms radical pairs whose quantum spin dynamics make the protein magnetically sensitive (Xu et al., *Nature* 2021).

**What we did:** we read the residues at these four positions by traceback alignment.
- **Birds:** 615 full-length bird cryptochromes.
- **Animals and relatives:** cryptochromes and photolyases found by a full alignment scan of 48 proteomes, from single-celled relatives of animals to vertebrates.

**Results:**
1. **All four tryptophans are conserved** in bird CRY1 (394/398), CRY2 (101/102) and named CRY4 (4/4). Cryptochrome DASH carries glycine at TrpD.
2. **Every sponge tested** (4 species) carries CRY1/CRY2-like proteins with all four tryptophans. **The chain is older than nervous systems.**
3. **An aromatic Y or F replaces TrpD** in the cryptochromes of single-celled relatives (*Monosiga*, *Salpingoeca*, *Capsaspora*), a free-living flatworm and rotifers. These proteins are nearest CRY1/CRY2, not photolyases.
4. **Placozoans' only family members are photolyase-like,** with the chain broken (L at TrpC/TrpD).

**A family marker, and its blind test:** with six references, all 35 cryptochrome/6-4 proteins carry an aromatic residue at TrpD, against none of 12 DASH and class I photolyases (L3777). **A blind test on honeybee, oyster and frog passed 2 of 4 (L3785):** 14 of 17 cryptochrome/6-4 hits were aromatic, and no DASH or photolyase hit was. The three exceptions are all weak, borderline hits. **With a pre-registered confidence cut (score ≥ 900), the marker passed blind in monarch, salmon and limpet (L3797: 17 of 17).** For confident hits it now stands at 31 of 31 across seven unseen animals.

**Validation:** the final scan recovered all 9 known control cryptochromes. An earlier shortcut version recovered 7 of 9 and was discarded (reported).

## 1. Introduction
- **Cryptochromes** are flavoproteins of the photolyase family that serve in circadian clocks and, in birds, as candidate magnetoreceptors.
- **The tetrad:** in robin CRY4, an electron hops TrpA (395) → TrpB (372) → TrpC (318) → TrpD (369). Successive flavin–tryptophan radical pairs carry the magnetic effect.
- **Question:** how widespread is the tetrad across animals and their relatives, and what sits at TrpD where it is absent?

## 2. Methods
- **Reference:** robin CRY4 (UniProt A0A2I4SZI9). **The four positions were confirmed as W before any mapping** (pre-registered check, L3753 Q1).
- **Mapping:** Smith–Waterman (BLOSUM62, gap 8) with traceback; the residue aligned to each tetrad position is read.
- **Birds (L3753):** 717 UniProt bird cryptochromes, 615 full length (≥ 450 aa). Class from the UniProt name.
- **Animal tree (L3761):** every protein of 400–900 aa in 48 proteomes aligned to robin CRY4 (local score ≥ 350).
  - **Family:** the nearest of robin CRY4, mouse Cry1/Cry2, fly cry, fly 6-4 photolyase, or zebrafish cry-dash.
  - **Must-find controls:** mouse Cry1/Cry2, fly cry, zebrafish cry1a/cry1b/cry4/cry-dash, and chicken CRY1/CRY2.
- **Pre-registration:** all predictions were frozen and hashed before each run.

## 3. Results
### 3.1 Birds (L3753; 3 of 3 gradeable)
| family | full length | WWWW |
|---|---|---|
| CRY1 | 398 | 394 |
| CRY2 | 102 | 101 |
| CRY4 (named) | 4 | 4 |
| cryptochrome DASH | ~45 | 0: **WWW-G** |

**The tetrad is not unique to the compass candidate:** the clock cryptochromes carry it too.

### 3.2 Across 48 proteomes (L3761; 4 of 6; controls 9/9)
| group | tetrad |
|---|---|
| sponges (4 species) | **WWWW** (10 proteins) |
| comb jelly; sea anemone; coral | WWWW |
| bilaterians with hits (vertebrates, lancelet, echinoderms, brachiopod, annelid, mollusc, arthropods) | mostly WWWW |
| single-celled relatives (*Monosiga*, *Salpingoeca*, *Capsaspora*) | **WWW-Y / WWW-Y / WWW-F** |
| *Macrostomum* (flatworm), rotifers | **WWW-F / WWW-Y** |
| placozoans | photolyase-like, **WW-LL** |
| DASH proteins (zebrafish, rotifers, sea anemone) | WWW-G |

**Failed predictions:**
- **"Every bilaterian has a hit":** none was detected in 18 bilaterians, including the nematode, most flatworms, the tardigrades and Ciona.
- **"The aromatic-fourth proteins are photolyases":** 2 of 11.

### 3.3 Outside animals (L3769; 2 of 4)
| organism | protein | tetrad |
|---|---|---|
| diatom *Phaeodactylum* | CPF1 (cryptochrome photolyase family 1) | **WWWW** |
| green alga *Chlamydomonas* | animal-like cryptochrome (A8J8W0) | **WWW-Y** |
| green alga | cryptochrome DASH | WWW-G |
| fungus *Neurospora* | none detected | |

- **The fungal result is a finder limit:** its named DASH and photolyase score below the floor against robin CRY4.
- **An aromatic Y at TrpD occurs in a green alga as well as in animals' single-celled relatives.**

### 3.4 More references, and a family marker (L3773: 2 of 4; L3777: 4 of 4)
**L3773, five references** (adding a fungal class I photolyase and a diatom DASH):
- it found the fungal DASH and all animal controls;
- it found nothing new in 17 bilaterians;
- it still missed two named photolyases.

**L3777, with a sixth reference (fly *phr*, class II photolyase):**
- **Recovery:** it recovered both missed photolyases and found class II photolyases in all 7 animals scanned.
- **The marker:**

| lineage | residue at TrpD |
|---|---|
| **cryptochromes and 6-4 photolyases** | **35 of 35 aromatic** (34 W, 1 Y) |
| DASH and class I photolyase | 12 of 12 non-aromatic (G, H, L, N, Q, V, E) |
| class II photolyase | not alignable (13) |

**An aromatic residue at the fourth position of the electron chain marks the clock/compass lineage.**

### 3.5 Blind test of the marker (L3781 → L3785: 2 of 4)
The marker was pre-registered before the honeybee, oyster and frog proteomes were downloaded.

| # | prediction | result |
|---|---|---|
| B1 | every CRY/6-4 hit is aromatic at TrpD | **FAIL:** 14 of 17. The exceptions are oyster A0A8W8KH86 and A0A8W8KKK9 (R) and frog A0A6I8QP63 (H). |
| B2 | no photolyase/DASH hit is aromatic at TrpD | **PASS:** 0 of 6 (2 informative: H, X) |
| B3 | each species has ≥ 1 CRY/6-4 hit | **PASS:** 4, 6, 7 |
| B4 | the frog has a class II photolyase | **FAIL:** none. The frog's only "CPD photolyase-like" entry is a 157-residue fragment, below the 400-residue window. |

**Not graded (seen after the result):** the three B1 exceptions scored 406–415, just above the 350 hit floor. All 14 hits scoring ≥ 973 are aromatic. **The marker may hold only for confident family members.** A score cut must be pre-registered and tested blind before it is used.

### 3.6 Marker v2 with a confidence cut (L3797: 3 of 3 gradeable, coral void)
The cut (score ≥ 900) was taken from L3785 and frozen before download.

| # | prediction | result |
|---|---|---|
| V1 | every confident CRY/6-4 hit is aromatic at TrpD | **PASS:** 17 of 17 |
| V2 | no confident DASH/photolyase hit is aromatic | **PASS:** G (salmon), K (limpet) |
| V3 | monarch has ≥ 2 confident CRY/6-4 hits | **PASS:** CRY1 (fly-type), CRY2 |
| V4 | each species has one | ungradeable: no UniProt proteome for *Acropora millepora* (not substituted) |

### 3.7 A discarded shortcut (L3757)
A pre-filter based on shared 3-letter words recovered only 7 of 9 controls. It missed fly cry (ranked 81st) and zebrafish cry-dash. Its results were not used.

## 4. Discussion
- **The light-driven electron chain that supports radical-pair magnetosensing in birds was already present in sponges,** animals without neurons.
- **The fourth position is variable at the base of the tree:**
  - an aromatic Y/F in single-celled relatives;
  - W in sponges and most animals;
  - G in DASH.
- **A tyrosine can also relay electrons,** so the chain may have been functional before W was fixed. That is untested.
- **Sequence conservation does not show magnetic sensitivity.** The robin's extra sensitivity (Xu et al.) must depend on other residues.

**Limitations:**
- UniProt proteomes vary in annotation.
- Absences are "not detected" (finder sensitivity for fast-evolving lineages unmeasured).
- Family assignment uses six references.
- Bird CRY4 named entries are few.
- **The family marker failed its strict blind test (B1, 14 of 17)** but passed with a confidence cut (L3797, 17 of 17). Weak hits remain unpredicted.

## 5. Data and code
- **Code:** `dcf-math/rounds/dcf_cry_tetrad_L3753.py`, `dcf_cry_tree_L3757.py` (discarded) and `dcf_cry_full_L3761.py`.
- **Outputs and grades:** in `rounds/`.
- **Archive:** dcf-math v1.1.0, Zenodo 10.5281/zenodo.24302678.

## Summary
- **First draft of a short note:** the four-tryptophan electron chain behind the robin's quantum compass is conserved across bird cryptochromes and present in every sponge tested, so it predates nervous systems.
- **Single-celled relatives carry an aromatic tyrosine or phenylalanine at the fourth position.**
- **One shortcut method failed its control and was discarded,** and that is reported.
- **The aromatic-TrpD family marker passed 4 of 4 on known data but 2 of 4 blind:** 14 of 17 new cryptochromes are aromatic, and the 3 exceptions are weak hits.

## Potential leads for future research
- **[Low-score class]** Test whether weak family hits (< 900) are non-aromatic more often than confident ones.
- **[Staghorn coral]** *Acropora cervicornis* (UP001249851) as its own round.
- **[Frog class II]** A full-length frog CPD photolyase from RefSeq/Ensembl would show whether B4 failed on annotation (a fragment) or on biology.
- **[Figure]** A tree-ordered dot plot of tetrad residues per organism.
- **[Outside reader]** As with the other manuscripts.
