# DCF L3681: A shared NR1 caller with the score floor; the recount changes 3 counts and 1 kit call (the flatworm); the flatworm has no NAV-family channel in UniProt; Manuscript 2 v0.20
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [NR1 floor in code], [Flatworm channels], [Manuscript 2]. Code, descriptive recounts and writing. **No predictions graded;** no past grade changes.

---

## 1. Shared NR1 caller (`rounds/dcf_nr1_L3681.py`, hashed into the ledger)
**The rule:** NR1 = all three of:
1. dcf_nerve v3 calls it a glutamate receptor;
2. its nearest of the 18 mouse receptors (local aligner) is Grin1;
3. the score is **≥ 1,000**.

**Use from now on:** every future NR1 count uses this file, so the floor cannot be left out again (the L3677 slip).

## 2. Recount of every organism (`rounds/L3681_nr1_recount.txt`)
- **Coverage:** all 41 organisms.
- **Method:** per-call scores were taken from the committed L3625, L3669 and L3677 outputs where they exist; the rest were recomputed with the caller.

| organism | NR1 without floor | with floor | kit status changes? |
|---|---|---|---|
| *Hofstenia* (acoel) | 3 | 2 | no |
| *Stylophora* (coral) | 2 | 1 | no |
| ***Schistosoma* (flatworm)** | **1** | **0** | **yes: present → absent** |
| all 38 others | unchanged | unchanged | no |

**The neural kit across all 41 organisms, with the floor:**
| group | kit present | correct |
|---|---|---|
| no nerves (4 sponges, 2 placozoans, 2 choanoflagellates, *Capsaspora*, *Sphaeroforma*) | 0 of 10 | **10 / 10** |
| nerves | 28 of 31 | **28 / 31** |

**The three misses:** the comb jelly, the sea urchin and the flatworm. None has NR1 or a lysine sodium channel.
- **Graded results stand as frozen:** L3673 development and the L3677 blind score (4 of 5, with the disclosure that the floor makes it 3 of 5).

## 3. The flatworm's channels (`rounds/L3681_flatworm.txt`)
- **Four-domain channels:** all of *Schistosoma*'s are nearest a mouse **calcium** channel (Cacna1a or Cacna1c, scores 2,909–3,798) or **NALCN** (3,460). **None is nearest a sodium channel.** UniProt's *Schistosoma* set therefore holds **no NAV-family channel at all.**
- **Glutamate receptors:** four named "putative kainate" (nearest Grik3) and one named "putative NMDA" (A0A3Q0KPC6), whose nearest is **Grin2a** (842). It is an NR2-type subunit; there is no strong NR1.
- **Correction to L3677:** I wrote that this NMDA-named receptor was "not called by the gate". It *was* called. The L3677 report has been corrected.
- **Reading:** the blood fluke, a parasite, carries a reduced kit in its UniProt set: calcium channels, NALCN, kainate-type and NR2-like receptors, but no NAV and no NR1.
  - **Whether that is parasite-specific loss or missing annotation is open.** A free-living flatworm (*Schmidtea*) would separate the two.

## 4. Manuscript 2 v0.20
- **New section:** §3.22, the neural-kit rule.
  - **Development:** 34/36.
  - **Blind:** 4/5 as frozen (3/5 with the floor, disclosed).
  - **The 41-organism recount:** 10/10 without nerves, 28/31 with nerves; the misses are the comb jelly, the sea urchin and the flatworm.
- **Totals:** the table and abstract read **149/181**, matching the audit.
- **Reader brief:** updated.

## Record
No predictions graded. **482 of 654 passed, plus 3 split.** Nerve-chemistry audit **149 of 181.**

## Summary
- **The NR1 score floor is now built into shared code.**
- **The recount of all 41 organisms changes three NR1 counts and one kit call,** the flatworm's.
- **With the floor, the neural-kit rule is right for all 10 organisms without nerves and 28 of 31 with nerves.**
- **The flatworm's UniProt proteome has no sodium-spike channel and no strong NR1,** a reduced kit that may reflect its parasitic life.
- **One wrong statement in the L3677 report was found and corrected.**

## Potential leads for future research
- **[Free-living flatworm]** Pre-register *Schmidtea mediterranea* (planarian): does a free-living flatworm keep NAV and NR1?
- **[Urchin NR1]** RefSeq protein for *S. purpuratus*. The starfish has NR1, so the urchin gap is suspicious.
- **[Comb jelly]** Its nerves use neither kit part. What do comb-jelly neurons use? Candidates: their own glutamate receptor class, NAV2 channels.
