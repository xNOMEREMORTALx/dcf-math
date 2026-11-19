# DCF L3809: TrpD tells cryptochromes from DNA-repair photolyases in 98.6% of 2,564 proteins (3 of 5). The marker follows the protein family, not the alignment score; both score predictions failed
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 18 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3809_panther_SF18.txt`.
- **Amendment:** `AMENDMENT_L3809_a.txt`, made before download. It covers the query syntax and a disclosed 5-row peek showing that SF18 is the class I CPD photolyase subfamily. It also excluded the reference entries and added P5.
- **Scan:** `rounds/dcf_cry_panther_L3809.py`.
- **Grader:** `rounds/dcf_grade_L3809a.py`.
- **Output:** `rounds/L3809_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3809_grade_output.txt`.

**Data:** Gary's zip "DNA_Repair", identified by content:

| set | proteins | PANTHER label match | MD5 |
|---|---|---|---|
| **SF18**, class I CPD (DNA-repair) photolyases, all organisms | 3,306 | 100% | 279268f1… |
| **SF17**, insect-type (Drosophila-type) cryptochromes | 338 | 100% | 834c90f6… |

Excluded from grading: *Neurospora* P27526, our own reference, and the 5 proteins already seen in L3785/L3805.

---

## Results
| # | prediction | result |
|---|---|---|
| P1 | ≥ 90% of SF18 hits non-aromatic at TrpD | **PASS:** 2,266 of 2,300 (98.5%) |
| P2 | ≥ 90% of SF17 hits aromatic at TrpD | **PASS:** 261 of 264 (98.9%) |
| P3 | ≥ 80% of SF18 hits score < 900 | **FAIL:** 1,364 of 2,300 (59%) |
| P4 | ≥ 90% of SF17 hits score ≥ 900 | **FAIL:** 129 of 264 (49%) |
| P5 | ≥ 50% of SF18 hits nearest the CPD reference | **PASS:** 1,621 of 2,300 (70%) |

**3 of 5 passed.** P3 was flagged as risky in the amendment. Both failures stand.

## What it means
**The residue at TrpD marks the family; the score does not.**

| set | score 350–899 | score ≥ 900 |
|---|---|---|
| SF17 cryptochromes, aromatic at TrpD | **134 of 135** | **127 of 129** |
| SF18 DNA-repair photolyases, aromatic at TrpD | 32 of 1,364 | **2 of 936** |

- **Insect cryptochromes are aromatic at TrpD whether their score is weak or strong.** DNA-repair photolyases are non-aromatic at any score.
- **The "confidence cut" of L3797/L3805 worked only as a stand-in:** in those proteomes the weak hits happened to be photolyases. It is not the real rule.
- **The real rule:** TrpD = W/Y/F → cryptochrome; anything else → class I photolyase. It is right for **2,527 of 2,564 proteins (98.6%)**.

**What sits at TrpD in the photolyases:** leucine in 1,650 of 2,300, then methionine (288), histidine (119) and glutamine (107). So class I photolyases mostly carry a non-redox-active residue where cryptochromes carry the fourth tryptophan.

## The exceptions (descriptive)
**SF18 photolyases with an aromatic TrpD (34):**
- **Mostly tyrosine (29),** in one fish group: perch-like and cichlid fishes (*Perca*, *Labrus*, *Gasterosteus*, *Dissostichus*, *Pundamilia*, killifish).
- **Phenylalanine (5),** including *Trypanosoma* (3).

**Tyrosine is redox-active like tryptophan.** These fish photolyases may have regained a fourth electron-transfer step.

**SF17 cryptochromes without an aromatic TrpD (3):**
- a pair from the soft-shell clam *Mya arenaria* (G);
- one from a salmon louse (gap).

## Record
**+3 passed, 2 failed. 552 of 760 passed, plus 3 split.** Audit **219 of 287** (entry "PANTHER SF18 vs SF17").

## Summary
- **Across 2,564 proteins from hundreds of species, one residue tells a light-sensing cryptochrome from a DNA-repair photolyase 98.6% of the time:** aromatic at TrpD means cryptochrome.
- **The score-cut version of the marker was a proxy and failed both score predictions.** The family rule replaces it.
- **The main exceptions are a tyrosine in one group of fish photolyases,** a candidate regained electron-chain step.

## Potential leads for future research
- **[Fish tyrosine]** Are the perch/cichlid photolyases with Y at TrpD a single lineage? Map them on a tree and pre-register that their nearest relatives (other fish SF18) read L or M.
- **[Reader update, done in L3829, phone 6.20]** Change dcf_cryreader's call to the family rule: aromatic TrpD → "cryptochrome-type chain", non-aromatic → "photolyase-type", with the 98.6% record. The score then only says whether the protein is in the superfamily.
- **[Other PANTHER subfamilies]** Repeat the test on the vertebrate CRY1/CRY2 subfamilies, plant CRY and CRY-DASH. That makes it a superfamily-wide map of TrpD.
- **[Manuscript 4]** v0.7: replace the confidence-cut framing with the family rule.
