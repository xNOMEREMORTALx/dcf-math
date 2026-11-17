# DCF L3785: blind test of the cryptochrome family marker, 2 of 4. Fourteen of 17 new cryptochromes are aromatic at TrpD, and no photolyase is. The three exceptions are weak hits, and the frog's class II photolyase was not found
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3781_cry_marker_blind.txt`, frozen before download.
- **Script:** `rounds/dcf_cry_marker_blind_L3781.py`, the L3777 scan unchanged.
- **Output:** `rounds/L3785_tool_output.txt`, committed before grading.
- **Grader:** `rounds/dcf_grade_L3785.py`, committed before the output was read.
- **Grading:** `rounds/L3785_grade_output.txt`.

**Data:** Gary's zip "cryptochrome_marker", identified by content:

| species | proteome | proteins | MD5 |
|---|---|---|---|
| honeybee *Apis mellifera* | UP000005203 | 19,057 | 121add60… |
| Pacific oyster *Magallana gigas* | UP000005408 | 57,874 | 85984d21… |
| frog *Xenopus tropicalis* | UP000008143 | 37,713 | ec214e08… |

The script and pre-registration hashes matched `LEDGER.md` before the run.

---

## Results
| # | prediction | result |
|---|---|---|
| B1 | every CRY4/6-4-family hit reads W, Y or F at TrpD | **FAIL:** 14 of 17 |
| B2 | no photolyase/DASH hit reads W, Y or F at TrpD | **PASS:** 0 of 6 |
| B3 | each species has ≥ 1 CRY4/6-4-family hit | **PASS:** bee 4, oyster 6, frog 7 |
| B4 | the frog has a class II photolyase hit | **FAIL:** none |

**2 of 4 passed. Both failures stand.**

## What failed, and why it matters
**The B1 exceptions:**

| protein | species | score | tetrad | UniProt name |
|---|---|---|---|---|
| A0A8W8KH86 | oyster | 415 | WWW**R** | Photolyase/cryptochrome alpha/beta domain-containing protein |
| A0A8W8KKK9 | oyster | 415 | WWW**R** | (same, 726 aa) |
| A0A6I8QP63 | frog | 406 | WWW**H** | Uncharacterized protein LOC100486741 |

**Not graded (seen after the result):** all three exceptions sit just above the 350 hit floor. **All 14 hits scoring 973 or more are aromatic at TrpD.** So the marker may hold for confident cryptochromes and break for weak, divergent family members. That idea was formed after seeing the data. It must be pre-registered and tested blind before it counts.

**B4:** the frog's only protein named "CPD photolyase-like" (A0A8J0QEV2) is 157 residues, a fragment outside the scan's 400–900 residue window. The failure is probably about annotation, not biology, but it stands as pre-registered.

**B2 detail:** of the 6 photolyase/DASH hits, 4 are class II photolyases that cannot be aligned at the tetrad positions ("----"). The 2 informative hits are both DASH: oyster H and frog X (an unknown residue in the UniProt sequence). **So B2 rests on only 2 informative proteins.**

## Record
**+2 passed, 2 failed. 534 of 738 passed, plus 3 split.** Audit **201 of 265** (`L3485_audit2.py`, entry "cryptochrome marker blind").

## Summary
- **The aromatic-TrpD marker passed 4 of 4 on the data it was found in (L3777), but only 2 of 4 blind.**
- **14 of 17 new cryptochrome/6-4 proteins in honeybee, oyster and frog carry W at TrpD,** and no DASH or photolyase does. The three exceptions (R, R, H) are the weakest hits.
- **The frog's class II photolyase was not found:** its only candidate is a 157-residue fragment.
- **The marker is a strong tendency, not yet a rule.** A confidence cut is the next pre-registered test.

## Potential leads for future research
- **[Marker v2, blind]** Pre-register "hits scoring ≥ 900 are aromatic at TrpD; hits below may not be" and test it on unseen proteomes (coral, *Nematostella*, choanoflagellates).
- **[Oyster R proteins]** A0A8W8KH86/KKK9 are a duplicated pair with an arginine at TrpD. Ask whether they are a mollusc-specific 6-4-like subfamily (a tree with the other mollusc hits).
- **[Frog class II]** A full-length frog CPD photolyase from RefSeq/Ensembl would separate annotation from biology for B4.
- **[Magnetite, L3789]** The magnetite branch of magnetoreception is now pre-registered and running: are "magnetosome gene homologs" in animals magnetite-specific, or generic families?
- **[Phone]** Cryptochrome reader menu (carried).
