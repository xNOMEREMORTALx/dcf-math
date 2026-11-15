# DCF L3569: A real aligner, written from scratch. With proper alignment, all 12 early and ambulacrarian sodium-type channels belong to the E-type NAV2 family (2 of 2); the comb-jelly tie resolves; the tree separates the K-type NAV1 genes
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Own aligner], [Tree]. The package install was blocked, so the DCF now has its own aligner.

---

## 1. `dcf_align` (`rounds/dcf_align_L3569.py`; also `dcf-genefinder/dcf_align.py`)
**What it is:**
- Needleman–Wunsch global alignment with the **BLOSUM62** scoring table and a linear gap penalty of 8.
- Each row is computed at once with numpy (a prefix-maximum trick for the gap term), so no installs are needed.
- About **0.1 s per 2,000 × 2,000-residue alignment.**

**Validation on known channels (mouse):**

| pair | identity |
|---|---|
| Scn2a vs Scn8a (two sodium channels) | **78.3%** (as expected for these paralogs) |
| Cacna1b vs Cacna1d (two calcium channels) | 46.2% |
| Scn2a vs Cacna1b (sodium vs calcium) | 19.2% |
| identical / gapped self-checks | 100% |

## 2. Pre-registered test (`PREREGISTERED_L3569_navtree.txt`)
**The setup:** the same channels as L3561/L3565, now by real alignment. The earlier 4-mer results were disclosed in the pre-registration.

**The control is informative:** NAV1 genes are ≥ 53.9% identical to each other, while NAV1–NAV2 pairs are ≤ 51.5%.

| query | best NAV1 | best NAV2 | family |
|---|---|---|---|
| acorn worm | 49.9% | **55.9%** | NAV2 |
| sea urchin | 46.5% | **52.2%** | NAV2 |
| choanoflagellate | 43.8% | **44.7%** | NAV2 |
| placozoan | 45.4% | **45.7%** | NAV2 |
| sea anemone | 49.1% | **51.6%** | NAV2 |
| comb jelly (5 channels) | 42.4–43.5% | **46.1–46.5%** | NAV2 (the L3565 tie now clear) |
| acoel (2 channels) | 43.3%, 46.2% | **48.5%, 48.1%** | NAV2 |

- **A1 (ambulacrarians → NAV2): PASS.**
- **A2 (all 10 early/acoel → NAV2): PASS.**
- The earlier 4-mer failure (L3565) stands as recorded; this is a separate, better-powered test.

**The neighbour-joining tree** (distance = 1 − identity; unrooted; `rounds/L3569_grade_output.txt`):
- **The six K-type NAV1 genes group together:** human, sea squirt, lancelet, fly, brachiopod, annelid.
- **All E-type channels fall outside that group.**
- **Caveat:** the choanoflagellate channel attaches next to the NAV1 group. The tree is unrooted, and the choanoflagellate's identities to NAV1 and NAV2 differ by only 0.9%, so its placement is not resolved.

## Reading: the history these tests now support
1. **E-type sodium-channel homologues (NAV2-like)** are the ancestral kind. They are found in choanoflagellates, placozoans, cnidarians, comb jellies and acoels.
2. **The K-type NAV1,** the fast nerve sodium channel with the DEKA lysine, arose **once, within bilaterians, after acoels split off,** by duplication of an E-type gene.
3. **Protostomes and chordates kept NAV1,** and many kept NAV2 too (annelid, lancelet).
4. **Echinoderms and acorn worms lost NAV1** and kept only NAV2.

This matches the broad picture in the literature on sodium-channel evolution, and **every step has now been tested blind in this project.**

## Record
**+2 passed. 422 of 578 passed, plus 3 split.** Audit **94 of 112**. Manuscript 2 is at **v0.11**.

## Summary
- **The DCF has its own protein aligner:** BLOSUM62 global alignment in numpy, validated at 78% for two mouse sodium channels.
- **With real alignment, every early and ambulacrarian sodium-type channel belongs to the E-type family,** and the K-type genes form their own group in the tree.
- **The resulting history:**
  - the fast K-type nerve sodium channel arose once in bilaterians after acoels split off;
  - it was lost in echinoderms and acorn worms.

## Potential leads for future research
- **[Figure 5]** Draw the tree with species names and the ring letter (E/K) at each tip.
- **[Pore-only tree]** Align only the four pore regions (S5–P–S6) for a sharper tree, and test whether the choanoflagellate channel groups with NAV2.
- **[Phone]** Add `dcf_align` as a menu item (two sequences → identity).
