# DCF L3561: Lost K or lost gene? The sea urchin and acorn worm channels belong to the E-type NAV2 family, so the K-type NAV1 gene was lost, which points to one origin of the K (1 of 1)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Lead:** [Lost or gained twice]. The novel step is to compare **gene families**, not just one letter.

---

## The question
| lineage | K-type (NAV1) | E-type (NAV2) |
|---|---|---|
| annelid *Capitella* | ✓ (R7TMI4) | ✓ (R7TCA7) |
| lancelet | ✓ (13) | ✓ (A0A9J7HQP1) |
| sea urchin, acorn worm | ✗ | E-type only |

- **The annelid and the lancelet each carry *two* sodium-channel genes:** a K-type (NAV1) and an E-type (NAV2).
- **So the E-type in the sea urchin and acorn worm could be either:**
  - **H1:** their NAV2, with the NAV1 gene lost; or
  - **H2:** their NAV1, with the K changed back to E.

## Test (pre-registered, `PREREGISTERED_L3561_navfamily.txt`)
**Method:** alignment-free similarity (shared 4-letter pieces) of each urchin/acorn-worm channel to reference NAV1s and NAV2s. All references come from files already graded:
- **NAV1:** brachiopod, annelid, lancelet, sea squirt, fly para, human SCN2A;
- **NAV2:** annelid and lancelet E-type paralogs.

**Prediction N1 (H1):** all four query channels are closer to NAV2.

| query | best NAV1 | best NAV2 | family |
|---|---|---|---|
| acorn worm A0ACM8CKW0 | 0.126 | **0.156** | NAV2 |
| sea urchin A0A7M7N9I2 | 0.106 | **0.136** | NAV2 |
| sea urchin A0A7M7SUY6 | 0.106 | **0.136** | NAV2 |
| sea urchin A0A7M7SV24 | 0.107 | **0.136** | NAV2 |

**The control is informative:** NAV1 genes resemble each other (≥ 0.194) more than any NAV1 resembles a NAV2 (≤ 0.139).

**N1: PASS (1 of 1).**

## Reading
- **The sea urchin and acorn worm did not turn their K back into E.** They **lost the whole K-type NAV1 gene** and kept the older E-type NAV2.
- **NAV1 with K is present in both protostomes (annelid) and chordates (lancelet).** So the simplest history is:
  1. **NAV1 arose once, by gene duplication,** with its K appearing before protostomes and deuterostomes split;
  2. **it was then lost in the echinoderm + acorn-worm branch.**
- **This favours "one origin plus a gene loss"** over "K invented twice."
- **Caveats:**
  - margins are modest (about 0.03);
  - the method is alignment-free;
  - a proper phylogenetic tree (alignment + maximum likelihood) would make this firm.

## Record
**+1 passed. 420 of 575 passed, plus 3 split.** Audit: **92 of 109** for the nerve-chemistry blind tests. Manuscript 2 is at **v0.9** (§3.9 updated).

## Summary
- **The sea urchin and acorn worm sodium channels belong to the E-type NAV2 family,** not to the K-type NAV1 family, as predicted.
- **Their lineage lost the NAV1 gene;** it did not undo the K.
- **The best-supported history is now one origin of the K-type nerve sodium channel** in the ancestor of all bilaterians except acoels, then its loss in echinoderms and acorn worms.

## Potential leads for future research
- **[Tree]** A real alignment-based phylogeny of NAV1/NAV2 across all the lineages we have. This needs an alignment tool. The package install was blocked in this session, so it needs Gary's approval or another route.
- **[Acoel and cnidarian channels]** Are the acoel and sea-anemone E-type channels NAV2-like, or ancestral to both families? Same method, pre-registered.
- **[Manuscript 2]** v0.9 for an outside reader.
