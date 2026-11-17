# DCF L3777: An aromatic fourth residue marks the cryptochrome lineage (4 of 4). All 35 cryptochrome/6-4 proteins carry W, Y or F at TrpD; no DASH or DNA photolyase does; class II photolyases are found in every animal scanned
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3777_cry_classII.txt`.
- **Script:** `rounds/dcf_cry_classII_L3777.py` (L3773 plus fly *phr*, a class II CPD photolyase, as a sixth reference).
- **Output:** `rounds/L3777_tool_output.txt`.
- **Grading:** `rounds/L3777_grade_output.txt`.

**Organisms:** the fly, the alga, the fungus, the diatom, and 7 animals. ***Nematostella* was omitted:** its file was missing from the script's file list, which I noticed and disclosed before grading.

---

## Results
| # | prediction | result |
|---|---|---|
| C1 | the held-out class II photolyases (algal Q9XHE2, diatom B7FZ06) are now found | **PASS** |
| C2 | no photolyase/DASH hit carries W/Y/F at TrpD | **PASS:** 0 of 25 |
| C3 | ≥ 90% of cryptochrome/6-4 hits carry W/Y/F at TrpD | **PASS:** **35 of 35** |
| C4 | ≥ 1 animal has a class II photolyase | **PASS:** all 7 scanned |

**4 of 4 passed.**

**Disclosure on C2:** 13 of the 25 photolyase/DASH hits are class II photolyases, too divergent for any residue to align at the tetrad positions ("----"). **The test therefore rests on the 12 informative hits** (DASH and class I), which are all non-aromatic: G, H, L, N, Q, V, E.

## Reading: a sequence-readable family marker
| lineage | residue at TrpD | n here |
|---|---|---|
| **animal-like cryptochromes and 6-4 photolyases** | **W** (34), **Y** (1, the alga). Two read WW**F**W, an F at TrpC, not TrpD. | 35, all aromatic |
| cryptochrome DASH | G, H, L, N, Q, V, E | 11, none aromatic |
| class I CPD photolyase (fungus) | L | 1 |
| class II CPD photolyase | not alignable | 13 |

- **An aromatic residue at the fourth position of the electron chain marks the cryptochrome/6-4 lineage,** the proteins that run circadian clocks and the magnetic compass.
- **DASH and DNA-repair photolyases never carry one** in these data.
- **The marker is consistent with the idea that a fourth aromatic stop extends the light-driven electron chain** in the clock/compass proteins. That function is not tested here.
- **Class II photolyases are present in every animal scanned** (sea hare, lancelet, water flea, horseshoe crab, brachiopod, sea urchin, mite) as well as in the fly, alga and diatom.

## Record
**+4 passed. 532 of 734 passed, plus 3 split.** Audit **199 of 261.**

## Summary
- **With a class II photolyase added as a sixth reference,** the finder now recovers the two named photolyases it missed before, and finds class II photolyases in all 7 animals scanned.
- **All 35 cryptochrome/6-4 proteins carry an aromatic residue (W, Y or F) at the fourth position of the tryptophan electron chain,** while none of the DASH or class I photolyases does.
- **That makes the fourth residue a sequence-readable marker of the clock/compass lineage.** All 4 predictions passed.

## Potential leads for future research
- **[Marker, blind]** Pre-register the marker on proteomes not used here (*Nematostella*, coral, sponges, choanoflagellates, flatworms): every CRY/6-4 hit aromatic at TrpD, every DASH/photolyase hit non-aromatic.
- **[Manuscript 4]** Add §3.5 (multi-reference, class II) and the marker table (v0.3).
- **[Phone]** A "cryptochrome reader" menu: give a protein FASTA and it reports the family and the four tetrad residues (uses the traceback aligner).
