# DCF L3457: Blind test in a bird. Nerve chemistry by metal (channels, pumps, NMDA receptors, iron enzymes) passes 13 of 14 in chicken
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_rna.fna.gz`.
- 74.8 MB: 8,379 NM_ and 60,291 XM_ records, all *Gallus gallus*.
- 18,011 genes, one transcript per gene (the longest reading frame).
- This source was set by amendment 2, **before** the file arrived.

**Procedure:**
1. Five frozen hashes checked against `LEDGER.md` (all matched).
2. Tool output without names or descriptions committed and pushed first (`rounds/L3457_tool.txt`).
3. Graded with the frozen truth rule v2 (symbol or description): `rounds/L3457_grade.py` → `rounds/L3457_grade_output.txt`.

---

## Results (PREREGISTERED_L3449_chicken)
| # | prediction | result |
|---|---|---|
| C1 | calcium-channel calls correct (≥ 90%) | **9/9 PASS** |
| C2 | sodium-channel calls correct (100%) | **8/9 FAIL** |
| C3 | potassium/HCN calls correct (≥ 90%) | **38/38 PASS** |
| C4 | voltage-gated channel genes found (≥ 80%) | **52/56 = 93% PASS** |
| C5 | K2P leak calls correct | **12/12 PASS** |
| C6 | K2P genes found (≥ 70%) | **12/13 PASS** |
| C7 | glutamate-receptor calls correct | **16/16 PASS** |
| C8 | glutamate receptors found | **16/17 PASS** |
| C9 | NMDA7 calls correct | **4/4 PASS** |
| C10 | NMDA receptors found | **4/4 PASS** |
| C11 | iron-hydroxylase calls correct | **5/5 PASS** |
| C12 | iron hydroxylases found | **4/4 PASS** |
| C13 | pump calls (Na/K, Ca, Cu) correct | **11/11 PASS** |
| C14 | named pumps given their own metal | **11/11 PASS** |

**13 of 14 pass; none ungradeable.**
- **Precision:** 103 of 104 calls correct across all classes.
- **Recall:** every class at or above its bar.

## What the bird shows
- **Every metal gate read in mammals and fish reads the same in a bird** (about 310 million years from mammals):
  - **Calcium channels:** 9, all correct.
  - **Potassium and pacemaker channels:** 38, all correct.
  - **Leak channels:** all 12 calls correct, and 12 of the 13 leak genes found.
  - **Glutamate receptors:** all 16 calls correct.
  - **NMDA receptors:** 4 of 4. The corrected NMDA motif, failed in fish at 6 letters and fixed to 7, is clean.
- **Iron enzymes for dopamine and serotonin:** 5 calls, all correct. The widened iron site (C or V) found all 4 named genes.
- **The nerve battery's chargers:** every named pump got its own metal.
  - **Calcium pumps:** 7 (SERCA, PMCA, SPCA).
  - **Copper pumps:** 2 (ATP7A, ATP7B).
  - **Na⁺/K⁺-type pumps:** 2 (ATP1A1, ATP12A).
  - **19 lipid flippases** were correctly left without a metal.
- **The one failure (C2):**
  - **What happened:** the ninth sodium call is LOC395944, which NCBI describes as **"voltage-gated sodium channel SNS"**. SNS (sensory-neuron-specific) is the old name of Na_v1.8, the pain-nerve sodium channel.
  - **Why it failed:** the frozen description pattern did not include the word order "voltage-gated sodium channel", so the call counts as wrong.
  - **What it is:** the protein is a sodium channel by its own description. As with the fish failures, **the error is in the truth rule's wording, not the biology.** It stays a failure as frozen.
- **The four missed channel genes** are KCNG1–4. These are silent subunits that cannot form channels on their own, and they have been missed in every species.

## Phone bundle 6.11
- **Menu 34** now also lists:
  - **pumps** by metal (Na⁺/K⁺, Ca²⁺, Cu);
  - **glutamate and NMDA receptors**;
  - the **iron hydroxylases** that make dopamine, noradrenaline and serotonin.
- It reads predicted (XM_) records too.
- **Self-test 265/265.**
- **Install:** copy all eight `.py` files from `dcf_phone_bundle_6.11.zip` into one folder and open `dcf_phone_6.11.py`.
- **`dcf-genefinder`** gains `dcf_pump.py`, and the updated `dcf_nerve.py`.

## Running tally of the nerve-chemistry blind tests
| species (distance from mammals) | round | gradeable passed |
|---|---|---|
| mouse | L3429 | 10/10 |
| zebrafish, curated | L3441 | 10/11 |
| zebrafish, predicted | L3445 | 7/10 |
| **chicken** | **L3457** | **13/14** |
| **total** | | **40/45** |

**All five failures share one cause:** a real channel or receptor that the name/description rule did not credit. The exception is one chance NMDA match, since fixed and clean in chicken.

## Record
**+13 passed, 1 failed. 365 of 508 passed, plus 3 split.**

## Summary
- **In a bird, the frozen rules read the nervous system's metal chemistry from mRNA with 103 of 104 calls correct:**
  - sodium, potassium, calcium and pacemaker channels;
  - leak channels;
  - glutamate and NMDA receptors;
  - the iron enzymes that make dopamine and serotonin;
  - the pumps that charge the nerve battery, each sorted by its metal.
- **The single failure is a sodium channel the truth rule's wording didn't recognise.**
- **The phone now carries all of it** in menu 34.

## Potential leads for future research
- **[Insect]** The next jump: fruit fly (~600 million years). Same frozen rules, plus a truth rule that knows fly names (para, Shaker, cac, Nmdar1).
- **[Truth rule v3]** Freeze a description pattern that accepts any word order ("sodium" and "channel" and "voltage" within one name), before the next test.
- **[Battery balance]** Pump-to-channel ratio across species: protists and animals now, bacteria via the gene finder.
- **[Manuscript 2]** The nerve-chemistry results (four species, 40/45, with every failure explained) are enough for a second short paper. Draft an outline.
- **[Copper brain]** A copper-enzyme finder for DBH/PAM, to pair with the copper pumps.
