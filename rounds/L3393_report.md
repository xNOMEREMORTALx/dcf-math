# DCF L3393: blind_25 passes 1 of 3. Endonuclease III's iron loss is lineage-specific, not a general lactic trait; MutY's loss holds; iron users keep both
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Data:** `blind_25.zip`, all 8 genomes, matched by LOCUS. NCBI renames: *Limosilactobacillus reuteri* / *fermentum*, *Latilactobacillus sakei*, *Exiguobacterium artemiae* (same accessions).

**Pre-registration:** `PREREGISTERED_L3389_ligandloss.txt` (`fac8514b…ae16`); script `dcf_ligandloss_L3389.py` (`b5e5fe14…`, matches the ledger). Output committed (`9900ad79…3b8b`) before grading.

---

## 1. Results
| genome | group | endonuclease III | MutY |
|---|---|---|---|
| *L. reuteri* | lactic | 5 C, **loop kept** | — |
| *L. sakei* | lactic | 6 C, **loop kept** | 2 C, lost |
| *L. crispatus* | lactic | 1 C, lost | — |
| *S. suis* | lactic | 5 C, lost | 0 C, lost |
| *L. fermentum* | lactic | none annotated | none annotated |
| *S. haemolyticus* | iron user | 8 C, kept | 4 C, kept |
| *Exiguobacterium* | iron user | 6 C, kept | 4 C, kept |
| *L. welshimeri* | iron user | 8 C, kept | 4 C, kept |

| id | prediction | result | verdict |
|---|---|---|---|
| LL1 | ≥ 4 gradable lactic genomes without the loop | 2 of 4 (*fermentum* ungradable) | **FAIL** |
| **LL2** | every control keeps it | 3 of 3 | **PASS** |
| LL3 | median cysteines lactic ≤ 2, controls ≥ 4 | lactic 3.5, controls 5 | **FAIL** |

## 2. Reading
- **The endonuclease III loss is real but lineage-specific.** Across development and blind data it is:
  - **lost** in *L. gasseri*, *johnsonii*, *helveticus*, *crispatus* (the acidophilus group) and *L. rhamnosus*;
  - **partly lost** in streptococci;
  - **kept** in *L. salivarius*, *reuteri* and *sakei*.
- **I generalised from development to all lactic bacteria, and the blind test corrected that.**
- **MutY:** every lactic MutY seen lacks the loop (0 of 8 in development, 0 of 2 blind), matching the known Lactobacillales clade. **Iron users keep both enzymes' clusters.**
- **A caveat for the earlier information-iron switch:** *L. reuteri* and *L. sakei* keep an iron-cluster endonuclease III, so on the label-free count they would read "on". The switch held in blind_24, whose four lactic genomes had none, but these two are known exceptions.
- **Note v0.3** carries the corrected reading.

## Record
**This round:** 3 graded, 1 passed (LL2 passed; LL1 and LL3 failed).

**Total: 321 of 459 pre-registered predictions passed, plus 3 split.**

## Summary
- **The blind test cut my claim down to size:**
  - endonuclease III loses its iron cluster in only some lactic lineages (the *acidophilus* group and *L. rhamnosus*), not all; *L. reuteri* and *L. sakei* keep it;
  - MutY's iron loss does hold across every lactic genome seen;
  - the iron-using relatives keep both.
- **So the new finding is narrower but cleaner:** iron-free endonuclease III is a trait of particular *Lactobacillus* lineages.

## Potential leads for future research
- **[Lineage map]** Map endonuclease III cluster loss onto the Lactobacillaceae tree (acidophilus, casei, reuteri, sakei, salivarius groups) and test whether loss tracks known iron-independence (e.g. MRS growth without iron, Mn-based superoxide dismutation).
- **[Switch exceptions]** Re-check the information-iron switch with the lactic lineages that keep the cluster; refine the claim to "absent or lineage-reduced".
- **[Venue]**, **[Ladder-P blind]**, **[Polymerase iron]**: carried.
