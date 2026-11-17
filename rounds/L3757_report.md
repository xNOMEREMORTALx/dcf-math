# DCF L3757: The cryptochrome tetrad across the animal tree (1 of 4 gradeable). The finder's own sensitivity control failed, and the 3-mer shortlist fails for the third time; what was found still shows WWWW in animals and an aromatic fourth residue in single-celled relatives
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Lead:** [Tetrad across animals] (L3753).

**Files:**
- **Pre-registration:** `PREREGISTERED_L3757_cry_tree.txt`.
- **Script:** `rounds/dcf_cry_tree_L3757.py`.
- **Output:** `rounds/L3757_tool_output.txt`.
- **Grading:** `rounds/L3757_grade_output.txt`.

**Method:**
1. For each of the 48 proteomes, take the 20 proteins (400–900 aa) sharing the most 3-letter words with robin CRY4.
2. Keep those with a local score ≥ 600.
3. Read the tetrad by traceback alignment.

**Built-in sensitivity control (P1):** 9 known cryptochromes must be found.

---

## Results
| # | prediction | result |
|---|---|---|
| P1 | 9 of 9 known cryptochromes recovered | **FAIL:** 7 of 9. Missed fly cry and zebrafish cry-dash. |
| T1 | every bilaterian has ≥ 1 hit | **FAIL:** 16 bilaterians have none |
| T2 | mouse, zebrafish and chicken have a WWWW hit | **PASS** |
| T3 | zebrafish cry-dash reads G at TrpD | **ungradeable** (not found) |
| T4 | the sponge *Amphimedon* has a hit | **FAIL** (0; the sponge *Geodia* has 2) |
| T5 | fly cry keeps W at A, B, C | **ungradeable** (not found) |

**1 of 4 gradeable predictions passed.**

## Why the controls were missed (descriptive, after grading)
| protein | shortlist rank | local score (floor 600) | missed because |
|---|---|---|---|
| fly cry | 81 of 4,899 | 817 | **shortlist** (only the top 20 kept) |
| zebrafish cry-dash | 2,407 of 10,608 | 440 | shortlist **and** floor |
| fly phr6-4 (6-4 photolyase) | 1 | 1,181 | found |

**This is the third failure of 3-letter-word shortlists at deep distances:**
- L3565 (4-mers);
- L3633 (NR1);
- now L3757.

**Standing lesson:** for divergent families, scan by alignment, or use a motif-based prefilter whose sensitivity is measured first. **All 16 zero-hit bilaterians are "not detected", not "lost".**

## What was found (descriptive)
| group | hits | tetrad |
|---|---|---|
| vertebrates, lancelet (8), sea urchin, starfish, brachiopod, annelid, sea hare, horseshoe crab, mite, water flea, coral, sea anemone (5), sponge *Geodia* | 1–8 each | **WWWW** throughout |
| **choanoflagellate *Salpingoeca*** | 1 | **WWW-Y** |
| ***Capsaspora*** | 1 | **WWW-F** |
| **rotifers** (*B. calyciflorus*, *B. plicatilis*) | 1–2 | **WWW-Y**, **WWW-F** |
| ***Macrostomum*** (flatworm) | 1 | **WWW-F** |
| ***Sphaeroforma*** | 1 | WWWW |

**The fourth position comes in three types:**
1. **W** in most animal cryptochromes and photolyases;
2. **G** in cryptochrome DASH (L3753);
3. **an aromatic Y or F** in single-celled relatives (choanoflagellate, *Capsaspora*), rotifers and a flatworm.

**Why that matters:** tyrosine can also relay electrons. So the "aromatic fourth" could still extend the chain, while DASH's glycine cannot. This is a lead, not a result. It has not been tested.

## Record
**+1 passed, 3 failed, 2 ungradeable. 520 of 716 passed, plus 3 split.** Audit **187 of 243.**

## Summary
- **Tracing the cryptochrome tryptophan chain across 48 proteomes failed its own sensitivity control** (7 of 9 known cryptochromes found). The short-word shortlist missed the fly's cryptochrome. Absences are therefore unreliable.
- **Where cryptochromes were found, animals carry all four tryptophans (WWWW),** from sea anemones and coral to vertebrates.
- **Single-celled relatives, rotifers and one flatworm carry an aromatic tyrosine or phenylalanine at the fourth position** instead: possibly a different electron-relay design.
- **The 3-letter-word shortcut has now failed three times.** It is retired for deep-distance searches.

## Potential leads for future research
- **[Alignment scan]** Rerun with no shortlist: align every 400–900 aa protein to robin CRY4 (about 4,000–10,000 per proteome). This is slow but sensitive. Pre-register with the same 9 controls, plus fly cry and cry-dash as must-finds.
- **[Aromatic fourth]** Test whether the Y/F-at-TrpD proteins are photolyases or cryptochromes (nearest of mouse Cry1/Cry2, fly cry/phr6-4, zebrafish cry-dash).
- **[Retire the 3-mer shortcut]** Record it in the methods notes as a standing rule.
