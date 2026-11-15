# DCF L3557: Lancelet and sea squirt. 8 of 8 pass; both chordates carry the full excitability kit and the sodium K. K is now found in every protostome and every chordate tested, and is missing only in the sea urchin and acorn worm
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `26`, a gzipped UniProt TSV of 58,339 proteins.
- **Included:** *Branchiostoma floridae* (lancelet, 39,280) and *Ciona intestinalis* (sea squirt, 19,006).
- **Dropped:** *Octopus bimaculoides* had only **53** entries in UniProt, so its four predictions (K1, K4, K7, K10) are **ungradeable**, as pre-stated.

**Procedure:**
1. Hashes matched.
2. The frozen `dcf_nerve` v2 output was committed and pushed before organisms were attached.
3. **Output:** `rounds/L3557_grade_output.txt`.

---

## Results (PREREGISTERED_L3553_kit_chordates_octopus)
| # | prediction | result |
|---|---|---|
| K2, K3 | HCN pacemakers in sea squirt, lancelet | **3, 5: PASS** |
| K5, K6 | K2P leak channels | **4, 28: PASS** |
| K8, K9 | iron hydroxylase | **2, 10: PASS** |
| K11 | lancelet DEKA sodium channel | **13: PASS** |
| K12 | sea squirt DEKA sodium channel | **3: PASS** |
| K1, K4, K7, K10 | octopus | ungradeable (53 proteins) |

**8 of 8 gradeable pass.**

## Reading
**The chordate K.**
- **Both chordates read A-T-F-K-G-W:**
  - lancelet LSLFQV A-T-F-**K**-G-W, in 11 of its sodium channels;
  - sea squirt LALLQV A-T-F-**K**-G-W.
- **Other letters also occur:**
  - the lancelet also has Q-type channels (A-T-F-**Q**-G-W, called as Naₓ-like sensors);
  - the sea squirt has one T-type (A-T-F-**T**-G-W).
- **K is now found in every protostome** (brachiopod, annelid, fly, nematodes) **and every chordate** (lancelet, sea squirt, vertebrates).
- **It is missing only in the ambulacrarians** (sea urchin, acorn worm) and in all non-bilaterians.
- **The open question stays open:** the two scenarios ("one gain, lost in ambulacrarians" vs "gained twice") both need two events.

**The kit.**
- **Both chordates have every part:** pacemakers, T-type calcium (lancelet 15, sea squirt 1), leak channels, glutamate receptors and iron hydroxylases.
- **The lancelet's iron enzymes are named by UniProt** as tryptophan 5-hydroxylase 2, tyrosine hydroxylase and phenylalanine hydroxylase: serotonin and dopamine synthesis are both present.
- **The sea squirt's two calls are phenylalanine hydroxylases.**

**Figure 4** (`figures/L3557_EtoK.png`) now has the lancelet and sea squirt rows.

## Manuscript 2 v0.8 and audit
- **Audit:** **91 of 108.**
- **Draft:** `notes/Manuscript_nerve_metals_draft_v0.8.md` adds the chordate follow-up to §3.9 and the T-type check as §3.10.

## Record
**+8 passed. 419 of 574 passed, plus 3 split.**

## Summary
- **In the lancelet and the sea squirt, all 8 gradeable predictions passed.** Both carry the full rhythm-and-arousal kit, and both have sodium channels with the K.
- **The K of the fast nerve sodium channel is now seen in every protostome and every chordate tested.** It is absent only in the sea urchin and acorn worm (and in all earlier animals).
- **The octopus could not be tested:** UniProt holds only 53 of its proteins.

## Potential leads for future research
- **[Octopus]** The *Octopus bimaculoides* genome's predicted proteome (outside UniProt, like *Hofstenia*) would let K1, K4, K7 and K10 be graded.
- **[Ambulacrarian loss]** If K was lost in ambulacrarians, their E-type channels may show traces: e.g. a codon one step from K (GAA/GAG → AAA/AAG). Compare codons (descriptive; needs mRNA).
- **[Outside reader]** Manuscript 2 v0.8.
