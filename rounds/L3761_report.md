# DCF L3761: The full cryptochrome scan (4 of 6, with the sensitivity control passing 9/9). The four-tryptophan chain predates nervous systems: every sponge carries it
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Lead:** [Alignment scan] (L3757).

**Files:**
- **Pre-registration:** `PREREGISTERED_L3761_cry_full.txt`.
- **Script:** `rounds/dcf_cry_full_L3761.py`.
- **Output:** `rounds/L3761_tool_output.txt`.
- **Grading:** `rounds/L3761_grade_output.txt`.

**Method:**
- **Scan:** every 400–900 aa protein in 48 proteomes was aligned to robin CRY4, with **no shortlist** (the L3757 failure, Standing rule 7). Hit = score ≥ 350.
- **Tetrad:** read by traceback.
- **Family:** the nearest of robin CRY4, mouse CRY1/CRY2, fly cry, fly 6-4 photolyase, or zebrafish cry-dash.

---

## Results
| # | prediction | result |
|---|---|---|
| P1 | sensitivity control: 9 of 9 known cryptochromes found | **PASS** (fly cry and zebrafish cry-dash now found) |
| T1 | every bilaterian has ≥ 1 hit | **FAIL:** 18 bilaterians have none |
| T2 | sponge *Amphimedon* has ≥ 1 hit | **PASS** (2, both WWWW) |
| T3 | zebrafish cry-dash reads G at TrpD | **PASS** (WWWG) |
| T4 | fly cry keeps W at A, B, C | **PASS** (WWWW) |
| T5 | most Y/F-at-TrpD hits are photolyases (nearest fly 6-4) | **FAIL:** 2 of 11. Most are nearest CRY1/CRY2. |

**4 of 6 passed.**

## The tetrad across the tree (descriptive)
| group | hits | tetrad |
|---|---|---|
| **sponges** (*Amphimedon*, *Geodia*, *Ephydatia*, *Oopsacas*) | 2–3 each, CRY1/CRY2-like | **WWWW in all 10** |
| comb jelly | 1 | WWWW |
| **placozoans** (both) | 2–3, nearest 6-4 photolyase | **WW-LL / WWW-L**: chain broken at C and/or D |
| cnidarians | sea anemone 7, coral 2, Hydra 1 | WWWW (sea anemone, coral); Hydra a DASH with N at D |
| vertebrates, lancelet, starfish, sea urchin, brachiopod, *Capitella*, sea hare, horseshoe crab, mite, water flea | 2–8 each | mostly WWWW |
| **single-celled relatives** (*Monosiga*, *Salpingoeca*, *Capsaspora*) | 1 each, CRY1/CRY2-like | **WWW-Y, WWW-Y, WWW-F** |
| *Sphaeroforma* | 1 | WWWW |
| **free-living flatworm *Macrostomum*** | 4, CRY1/CRY2-like | **WWW-F** in all 4 |
| rotifers | 2–3 | **WWW-Y, WWW-F** (plus DASH WWWG) |
| **none found** (18) | | the nematode (known to lack cryptochromes), all 9 parasitic and other flatworms except *Macrostomum*, both tardigrades, the leech, *Dimorphilus*, the priapulid, the acoel, the acorn worm, and Ciona |

## Reading
- **The four-tryptophan electron chain is older than nervous systems.** All four sponges, which have no neurons, carry CRY1/CRY2-like proteins reading WWWW. So the light-driven radical-pair machinery was in place before nerves evolved.
- **The fourth position varies at the base of the tree:**
  - single-celled relatives read **Y or F** (an aromatic residue that can still relay electrons);
  - sponges and most animals read **W**;
  - DASH reads **G**;
  - placozoans' photolyase-like hits have lost the chain (L at C and D).
- **T5 failed in an informative way.** The "aromatic fourth" proteins are mostly **CRY1/CRY2-like cryptochromes**, not photolyases, in the single-celled relatives, *Macrostomum* and the rotifers.
  - **One possible history (a hypothesis):** the ancestral cryptochrome may have had an aromatic Y/F at TrpD, with W fixed later in animals.
  - ***Sphaeroforma*'s WWWW** shows the picture is not simple.
- **Absences:** the finder found all 9 controls, but its sensitivity for fast-evolving lineages is unmeasured. The 18 zero-hit bilaterians are **"not detected"** (Standing rule 5).
  - Only the nematode matches a published loss, as far as I know.
  - The run of absences across flatworms, tardigrades and others is a lead, not a finding.

## Record
**+4 passed, 2 failed. 524 of 722 passed, plus 3 split.** Audit **191 of 249.**

## Summary
- **Aligning every candidate protein, with no shortcut, found all 9 known cryptochromes** and passed 4 of 6 predictions.
- **Every sponge carries the full four-tryptophan chain (WWWW),** so the light-driven quantum radical-pair machinery predates nervous systems.
- **Single-celled relatives, a free-living flatworm and rotifers carry cryptochromes with an aromatic tyrosine or phenylalanine at the fourth position.** These are not photolyases, so my prediction failed.
- **Placozoans' only hits are photolyase-like, with the chain broken.**
- **No cryptochrome was detected in 18 bilaterians,** including the nematode, most flatworms and the tardigrades.

## Potential leads for future research
- **[Aromatic fourth, tested]** Pre-register: across more choanoflagellate and filasterean proteomes, cryptochromes read Y/F at TrpD, and animal cryptochromes read W.
- **[Placozoan photolyase]** Placozoans are light-sensitive animals with no neurons. Which photoreceptors do they use, if their cryptochrome chain is broken?
- **[Absent in fast lineages]** Is the absence real in tardigrades and flatworms? Use RefSeq or genome-based proteins for one species of each.
- **[Manuscript 4?]** "Light and time before nerves": sponge cryptochromes, the tetrad, and the clock. Possibly a short note.
