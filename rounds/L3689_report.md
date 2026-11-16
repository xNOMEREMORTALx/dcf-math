# DCF L3689: Flatworms (4 of 6). The sodium spike channel is lost in flukes, not in all parasites (the tapeworm keeps one); and flatworm NR1s exist but score just under the 1,000 floor
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Data:** Gary's zip (`NR1_a_parasite`), four files. Each was identified by header, and each count matches its proteome exactly:

| organism | lifestyle | proteins |
|---|---|---|
| *Macrostomum lignano* | free-living | 52,448 |
| *Fasciola hepatica* | liver fluke | 11,190 |
| *Echinococcus multilocularis* | tapeworm | 10,472 |
| *Schistosoma japonicum* | blood fluke | 14,733 |

**Procedure:**
1. **Frozen files:** the pre-registration (`PREREGISTERED_L3685_flatworms.txt`), `dcf_flatworm_L3685.py` and the floored NR1 caller; all hashes matched.
2. **Tool output:** `rounds/L3689_tool_output.txt`, pushed before grading.
3. **Grading:** `rounds/L3689_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| F1 | *Macrostomum* kit present | **PASS** (7 lysine Na channels) |
| F2 | *Macrostomum* ≥ 1 NAV-family channel | **PASS** (8) |
| F3 | liver fluke kit absent | **PASS** |
| F4 | tapeworm kit absent | **FAIL:** 1 lysine Na channel (A0A087VY10, named "Sodium channel protein", nearest Scn2a) |
| F5 | *S. japonicum* kit absent | **PASS** |
| F6 | the three parasites: 0 NAV-family | **FAIL:** the tapeworm has 1 |

**4 of 6 passed.**

## Descriptive, after grading
| flatworm | NAV-family | lysine Na | best Grin1-nearest score | named NMDA subunits |
|---|---|---|---|---|
| *Macrostomum* (free-living) | **8** | 7 | 648 | none |
| tapeworm | **1** | 1 | 839 | "NMDA receptor subunit" (nearest Grin2a) |
| liver fluke | **0** | 0 | 459 | "NMDA subunit epsilon" (Grin2d) |
| *S. japonicum* | **0** | 0 | **953** | **"NMDA receptor subunit 1" (Grin1, 953)**; NMDA 2A |
| *S. mansoni* (L3677) | **0** | 0 | **941** | putative NMDA (Grin2a) |

## Reading
**1. The sodium spike channel is lost in flukes, not in all parasites.**
- All three flukes have no NAV-family channel: two blood flukes and the liver fluke, which are all trematodes.
- The tapeworm, a cestode and also a parasite, keeps one.
- The free-living *Macrostomum* has eight.
- **On these data, the loss belongs to the trematode lineage,** not to parasitism as such. This is the third independent sodium-channel loss seen in this series, after nematodes and tardigrades.

**2. Flatworm NR1s exist, but score just under the floor.**
- *S. japonicum* has a protein UniProt names "NMDA receptor subunit 1", nearest mouse Grin1 at **953**. *S. mansoni*'s best is 941; the acoel's dropped call was 962.
- **The 1,000 floor was set between noise (≤ 80) and known NR1s (≥ 1,600). It is too high for divergent lineages:** true but divergent NR1s score about 940–960.
- **Consequences:**
  - **The flukes' "kit absent" calls rest partly on this floor.** With a lower floor, both blood flukes would have NR1, and their kits would be present.
  - **The L3681 recount's flatworm flip** (present → absent) **was the floor removing a real, divergent NR1, not noise.**
- ***Macrostomum*'s best is only 648**, with many NR2-like and kainate-like receptors. It may truly lack NR1, or carry a very divergent one.
- **A better floor needs calibration on named positives and negatives,** pre-registered, rather than a round number.

## Record
**+4 passed, 2 failed. 486 of 660 passed, plus 3 split.** Nerve-chemistry audit **153 of 187.**

## Summary
- **Free-living vs parasitic flatworms:** 4 of 6 predictions passed.
- **The flukes all lack the sodium spike channel,** but the tapeworm keeps one and the free-living flatworm has eight. So the loss is a fluke (trematode) trait rather than a parasite trait: the third independent loss seen, after nematodes and tardigrades.
- **Flatworms do have NMDA NR1 subunits.** They are divergent enough to score just under the 1,000 floor (941–953), so the floor is too strict for distant lineages and needs proper calibration.

## Potential leads for future research
- **[Floor calibration]** Pre-register a calibration. Collect every iGluR call whose nearest is Grin1 across all organisms seen. Positives: UniProt-named "NMDA receptor subunit 1 / zeta-1". Negatives: everything else. Choose the floor that best separates them, then test it blind.
- **[Fluke sodium loss]** A pre-registered test on more trematodes (*Clonorchis*, *Opisthorchis*, *Paragonimus*) and cestodes (*Taenia*, *Hymenolepis*). Prediction: trematodes have 0 NAV-family channels, cestodes have ≥ 1.
- **[Manuscript 2]** §3.23 (flatworms) and a revision of the kit section for the floor issue.
