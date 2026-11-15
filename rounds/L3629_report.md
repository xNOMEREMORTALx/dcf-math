# DCF L3629: Sodium-channel loss is not general in moulting animals. Horseshoe crab, spider mite and priapulid all keep a lysine sodium channel; 4 of 5 passed, and the priapulid's channel was missed by the rule (T-W-K-G-W)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Data:** Gary's three files (`29Horseshoe_crab.gz`, `30Spider_mite.gz`, `31Priapulid_worm.gz`), each a single organism:

| organism | proteins |
|---|---|
| *Limulus polyphemus* (horseshoe crab) | 31,562 |
| *Tetranychus urticae* (spider mite) | 17,840 |
| *Priapulus caudatus* (priapulid) | 18,486 |

**Procedure:**
1. **Frozen files:** the pre-registration (`PREREGISTERED_L3625_nr1_tree_ecdysozoa.txt`, part B), `dcf_battery_L3609.py` and `dcf_nerve_v2_L3549.py`. All three hashes matched the ledger.
2. **Tool output:** `rounds/L3629_tool_output.txt`. It read only Entry and Sequence, and was pushed before any protein name was read.
3. **Grading:** `rounds/L3629_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| E1 | horseshoe crab ≥ 1 Na call | **17 calls: PASS** |
| E2 | spider mite ≥ 1 Na call | **4 calls: PASS** |
| E3 | priapulid ≥ 1 Na call | **0 calls: FAIL** |
| E4 | horseshoe crab ratio > 1.8 | **142 / 18 = 7.89: PASS** |
| E5 | spider mite ratio > 1.8 | **27 / 9 = 3.00: PASS** |

**4 of 5 passed.** The priapulid's ratio (31 / 5 = 6.20) was not predicted, but it is also in the neural range.

## Descriptive, after grading
- **Horseshoe crab:**
  - All 17 sodium calls are named "Sodium channel protein" and align nearest mouse Scn4a, Scn5a or Scn11a (scores 3,100–3,900). They are isoform entries of a few genes; the horseshoe crab genome is also duplicated.
  - Further sodium-channel entries were not called: fragments, one T-F-E-G-W (NAV2-type) entry, and NALCN.
  - The many calcium calls are L-, T- and P/Q-type channels, all named so.
- **Spider mite:**
  - All 4 sodium calls are named "Sodium channel / Voltage-gated sodium channel alpha subunit" and align nearest Scn8a.
  - The 1,068-aa entries named sodium channel are partial cDNAs, which is why they were not called.
- **Priapulid (the failure):**
  - **A0ABM1DYP7 (2,027 aa) is named "Sodium channel protein" and aligns nearest mouse Scn8a** (score 3,170).
  - **Its domain-III loop reads Q-V-A-T-W-K-G-W.** Mouse Scn8a reads Q-V-A-T-F-K-G-W.
  - **The lysine (K), the "K" of DEKA, is present.** Phenylalanine is replaced by tryptophan, and the rule [TS]-[FY]-[KR]-[GA]-W does not allow W.
  - **So the tool missed a real lysine sodium channel.** The failure stands; the rule is too narrow at position 2.
- **NALCN** (sodium leak channel) is present in all three, aligning nearest mouse Nalcn.

## Reading
**Scoreboard, all moulting animals tested:**

| animal | size | voltage-gated Na⁺ channel | battery ratio |
|---|---|---|---|
| nematode (*C. elegans*) | 1 mm | **none** | low |
| tardigrades (2 species) | < 1 mm | **none** (NALCN only) | 1.53–1.54 |
| spider mite | 0.5 mm | **yes** (K type) | 3.00 |
| fruit fly | 3 mm | yes | 3.5 |
| priapulid | cm | **yes** (K type, T-W-K-G-W) | 6.20 |
| horseshoe crab | 50 cm | **yes** (K type, many copies) | 7.89 |

- **Small size does not explain the loss.** The spider mite is smaller than a tardigrade, yet it keeps its sodium channel and a neural-range ratio.
- **Sodium loss, so far, is specific to two lineages, nematodes and tardigrades.** They are not each other's closest relatives within Ecdysozoa, so the loss probably happened twice independently (convergent).
- **The battery ratio tracks the loss.** Every moulting animal *with* sodium channels has a ratio above 1.8; the two *without* are below it. The ratio cut-off of 1.8 holds once the sodium-loss lineages are explained.

## Record
**+4 passed, 1 failed. 456 of 619 passed, plus 3 split.** Nerve-chemistry audit **123 of 146.**

## Summary
- **All three moulting animals tested keep a lysine (DEKA-type) sodium channel:** horseshoe crab, spider mite and priapulid.
- **Sodium-channel loss is therefore not a general feature of small moulting animals.** So far it is seen only in nematodes and tardigrades.
- **Score:** 4 of 5 predictions passed.
- **The one failure is a real rule miss.** The priapulid's channel reads T-**W**-K-G-W, and the sodium rule allows only F or Y at that place.
- **Battery ratios:** 7.89 for the horseshoe crab, 3.00 for the mite and 6.20 for the priapulid, all in the neural range.

## Potential leads for future research
- **[Sodium rule v3]** Widen the sodium loop to [TS]-[FYW]-[KR]-[GA]-W in development across all species seen, check for new false calls, then test blind.
- **[Twice lost?]** Map NAV loss with more Ecdysozoa: other nematode-like lineages (Nematomorpha), velvet worm (Onychophora), kinorhynch, if proteomes exist. The prediction: velvet worms keep it.
- **[Calcium makes up for it?]** Do the sodium-less lineages carry extra calcium channels? Compare Cav counts per genome against relatives that kept sodium.
- **[Manuscript 2]** §3.14–3.16: tardigrade 2, NR1 tree, moulting-animal sodium; the scoreboard table as a figure.
