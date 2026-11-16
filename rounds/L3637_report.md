# DCF L3637: Blind test of sodium rule v3 on three spiralians (6 of 7). The leech, the rotifer and even the 1 mm *Dimorphilus* keep a lysine sodium channel; v3 ships in phone 6.15 and dcf-genefinder
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Data:** Gary's three files (`Leech_.gz`, `Dimorphilus.gz`, `Rotifer_Brachionus.gz`), each a single organism:

| organism | proteins |
|---|---|
| *Helobdella robusta* (leech) | 23,370 |
| *Dimorphilus gyrociliatus* (miniaturised annelid) | 16,152 |
| *Brachionus calyciflorus* (rotifer) | 24,535 |

**Procedure:**
1. **Frozen files:** the pre-registration (`PREREGISTERED_L3633_spiralia_rotifer.txt`), dcf_nerve v3, battery v3 and `dcf_l3633_blind.py`. All four hashes matched the ledger.
2. **Tool output:** `rounds/L3637_tool_output.txt`. It read only Entry and Sequence, and was pushed before any name was read.
3. **Grading:** `rounds/L3637_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| R1 | leech ≥ 1 Na call | **5: PASS** |
| R2 | *Dimorphilus* ≥ 1 Na call | **0: FAIL** |
| R3 | rotifer ≥ 1 Na call | **1: PASS** |
| R4 | leech ratio > 1.8 | **61 / 22 = 2.77: PASS** |
| R5 | *Dimorphilus* ratio > 1.8 | **34 / 9 = 3.78: PASS** |
| R6 | rotifer ratio > 1.8 | **29 / 15 = 1.93: PASS** |
| R7 | every Na call nearest a mouse Scn | **6 of 6: PASS** |

**6 of 7 passed.**

**Grader bug, disclosed:**
- **The bug:** the first grading pass printed R7 FAIL. My grading code read field 3 of each tool line (the word "nearest") instead of field 4 (the receptor name).
- **What the tool output shows:** all six calls are nearest Scn3a, Scn4a, Scn8a or Scn9a.
- **The fix:** I corrected the parse; the original output is kept as `L3637_grade_output_parsebug.txt`. The prediction and the tool output were not changed. This is the same kind of fix as the L3581 parse fix.

## Descriptive, after grading
- **Leech:** all 5 Na calls are named "Sodium channel protein" (domain-III loop T-F-K-G-W). It also has calcium channels of the L-, P/Q- and T-type families, and NALCN.
- **Rotifer:**
  - **one sodium channel** (T-F-K-G-W, nearest Scn3a);
  - **three NALCN-like leak channels**;
  - L-type and T-type calcium channels.
- ***Dimorphilus* (the failure):**
  - **A0A7I8V7K0 is named "Sodium channel protein".** It carries **T-F-K-G-W**, has 4 voltage sensors and aligns nearest **Scn2a** (score 2,052), but it is only **923 aa**.
  - **A0A7I8W837 (1,226 aa) is named "Sodium channel protein" too,** with a T-F-E-G-W loop and nearest Scn3a.
  - **Both are pieces of channel genes.** The 4-domain rule needs ≥ 1,500 aa, so neither was called.
  - **So *Dimorphilus* does carry a lysine sodium channel,** split in its annotation. The failure stands as a fragment limit of the rule.
- **v3's new clause (T-W-K-G-W) did not fire on any of the three animals.** This test shows v3 causes no harm on new data. It does not yet confirm the clause itself, which so far rests on the priapulid alone.

## Reading
| animal | size | sodium channel (lysine) | ratio |
|---|---|---|---|
| nematode | 1 mm | none | low |
| tardigrades | < 1 mm | none | 1.5 |
| spider mite | 0.5 mm | yes | 3.00 |
| ***Dimorphilus*** | **~1 mm** | **yes** (fragment) | **3.78** |
| rotifer | 0.2–0.5 mm | yes | 1.93 |
| leech | cm | yes | 2.77 |
| priapulid | cm | yes | 6.40 (v3) |
| horseshoe crab | 50 cm | yes | 7.89 |

- **Animals as small as nematodes and tardigrades, a spider mite, a miniaturised annelid and a rotifer, all keep the lysine sodium channel.** Size does not predict sodium-channel loss in either branch of the animal tree.
- **The loss is so far specific to nematodes and tardigrades.**
- **The battery cut-off holds once those two lineages are set aside.** Every animal with a sodium channel and a nervous system in this series is above 1.8 (the rotifer only just, at 1.93). Both sodium-less lineages are below it.

## Tools updated (v3 passed blind)
- **Phone bundle 6.15** (`phone/dcf_phone_bundle_6.15.zip`, 10 files):
  - `dcf_nerve.py` v3;
  - a new self-test: the T-W-K-G-W sodium channel is Na, and a T-type calcium channel with S-W-R-A-W stays T-type calcium;
  - **268/268 passed.**
- **dcf-genefinder:** `dcf_nerve.py` v3 and a CHANGELOG entry, pushed.

## Record
**+6 passed, 1 failed. 462 of 626 passed, plus 3 split.** Nerve-chemistry audit **129 of 153.**

## Summary
- **Score:** sodium rule v3 passed 6 of 7 blind predictions on a leech, a miniaturised 1 mm annelid and a rotifer. All six sodium calls align nearest a mouse sodium channel.
- **The one failure** is *Dimorphilus*, whose lysine sodium channel is split into fragments below the rule's length cut. It does have one.
- **Size does not predict sodium-channel loss;** so far only nematodes and tardigrades have lost it.
- **v3 now ships** in phone 6.15 (self-test 268/268) and dcf-genefinder.

## Potential leads for future research
- **[Fragment rescue]** Pre-register: proteins 800–1,500 aa with ≥ 4 S4 sensors and a lysine loop → "Na (partial)". Development on all sets seen first.
- **[T-W-K-G-W elsewhere]** Search all sets for the W-variant lysine loop. Is the priapulid unique, or is it a wider priapulid/scalidophoran trait?
- **[Rotifer NALCN ×3]** Three leak-channel copies in a rotifer is unusual. Do other rotifers (Adineta, Rotaria; UniProt has many proteomes) also carry several?
- **[RefSeq NR1]** Still waiting for the sea-urchin and Ciona RefSeq protein files.
- **[Manuscript 2]** Add §3.13–3.17 (sea hare, tardigrade 2, NR1 tree, moulting animals, spiralians) and the size-vs-sodium table as a figure.
