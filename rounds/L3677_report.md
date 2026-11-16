# DCF L3677: Neural-kit blind test, 4 of 5. The starfish has NR1 (so my "echinoderm miss" prediction failed); a missing score floor is disclosed, under which the flatworm would also fail
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Data:** Gary's zip (`proteome`), five files. Each was identified by header, and each count matches its proteome exactly:

| organism | proteins |
|---|---|
| *Sphaeroforma arctica* | 18,649 |
| *Stylophora pistillata* (coral) | 23,873 |
| *Schistosoma mansoni* (flatworm) | 10,766 |
| *Daphnia pulex* (water flea) | 30,137 |
| *Acanthaster planci* (starfish) | 25,685 |

**Procedure:**
1. **Frozen files:** the pre-registration (`PREREGISTERED_L3673_neural_kit.txt`) and `dcf_kit_L3673.py`; all hashes matched.
2. **Tool output:** `rounds/L3677_tool_output.txt`, pushed before grading.
3. **Grading:** `rounds/L3677_grade_output.txt`.

---

## Results
| # | organism | NR1 | lysine Na | kit | prediction | result |
|---|---|---|---|---|---|---|
| K1 | *Sphaeroforma* (no nerves) | 0 | 0 | absent | absent | **PASS** |
| K2 | coral | 2 | 0 | present | present | **PASS** |
| K3 | flatworm | 1 | 0 | present | present | **PASS** (see disclosure) |
| K4 | water flea | 1 | 1 | present | present | **PASS** |
| K5 | starfish | **1** | 0 | **present** | absent | **FAIL** |

**4 of 5 passed, as frozen.**

**K5:** this failure is my biological prediction, not the rule. The starfish has nerves, and the rule called its kit present. Its NR1 call (A0A8B8A3N6, score 1,996) is named **"Glutamate [NMDA] receptor subunit 1"**.

## Disclosure: the NR1 score floor was missing from the frozen script
- **The standing rule:** since L3649, every nearest-reference count needs a **score floor of 1,000**, stated in the pre-registration. **I did not write it into this test.** The test is graded as frozen.
- **Effect of the floor:**
  - **Coral:** 2 → 1 NR1. The dropped call is a ribosomal protein, score 553; the real one is named "NMDA receptor subunit 1", score 2,196. **The coral's kit is still present.**
  - **Flatworm:** 1 → 0. Its only call (A0A5K4F3J7, 941, "ANF receptor domain-containing") falls under the floor, so **the kit would be absent and K3 would fail.**
  - **So under the standing floor this test scores 3 of 5.** The audit records 4 of 5 (as frozen), with this note.
- **Earlier rounds checked:**
  - Of 19 NR1 calls in L3625, one is below 1,000 (*Hofstenia*, 962).
  - *Hofstenia* keeps two others, so no earlier outcome changes.
- **From now on, the floor is built into the shared NR1 code** rather than left to each pre-registration.

## Descriptive, after grading
- **Starfish:** it has NR1 and an NMDA 3B-like subunit, plus an entry named "Sodium channel protein" that was not called lysine-type.
  - **The sea urchin's missing NR1 (L3625, L3633) is therefore not an echinoderm trait.** The urchin either lost it on its own lineage, or UniProt's set lacks it.
  - **The case for a RefSeq check of the urchin is now stronger.**
- **Coral:** several entries are named NMDA 1 and NMDA 2A, and two "Sodium channel protein" entries carry no lysine loop (cnidarian NAV2-type).
- **Flatworm:**
  - An entry named "Putative glutamate receptor, NMDA" (A0A3Q0KPC6) was not called by the iGluR gate. Its single NR1-nearest call is weak.
  - No lysine sodium channel was called. **Flatworm channels need a closer look.**
- **Water flea:** both kit features are present: NR1 (2,046) and a lysine sodium channel (E9GGF2), plus "Nach" entries, which are a different (ENaC-type) family.
- ***Sphaeroforma*:** neither feature, and only 4 channels, against 3 pumps.

## Reading
- **The kit rule passed on four of five new organisms as frozen,** and on three of five under the standing floor.
- **Its cleanest results are the single-celled *Sphaeroforma* (absent) and the water flea (present).**
- **The starfish result rescues echinoderms.** The rule's development "miss" (the sea urchin) looks urchin-specific.
- **The flatworm is the weak case:**
  - its NR1 evidence sits just under the floor;
  - it has no lysine sodium channel call.
  - **Platyhelminth channels should be examined before the rule is relied on there.**

## Record
**+4 passed, 1 failed (as frozen). 482 of 654 passed, plus 3 split.** Nerve-chemistry audit **149 of 181.**

## Summary
- **Score:** the count-free neural-kit rule passed 4 of 5 blind predictions.
- **The one failure was my own expectation that a starfish would lack the kit.** It has a named NMDA receptor subunit 1, so the sea urchin's absence looks lineage-specific or an annotation gap.
- **Disclosed:** I left the standing score floor out of this frozen script. Applied, it would remove the flatworm's only NR1 call and make the score 3 of 5.
- **From now on, the floor is built into the NR1 code.**

## Potential leads for future research
- **[NR1 floor in code]** Freeze a shared NR1 caller with the floor built in. Recheck every NR1 count with it, descriptively.
- **[Flatworm channels]** Why no lysine sodium channel in *Schistosoma*? Check its "sodium channel" entries and the NMDA-named receptor missed by the gate.
- **[Urchin NR1]** RefSeq protein for *S. purpuratus* (the starfish has NR1, so the urchin gap may be annotation).
- **[Manuscript 2]** §3.22: the kit blind test with the floor disclosure.
