# DCF L3521: The earliest bilaterians answer "E." The acoel worm *Hofstenia*'s sodium-type channels read A-T-F-E-G-W, not K (exploratory; my stated leaning, K, was wrong)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** Gary's `Hofstenia_miamia.HmiaM1.pep.all.fa.gz`, the predicted proteome of the three-banded panther worm, 22,454 genes (longest protein per gene).

**Procedure:**
1. A note was added to the exploratory pre-registration **before scanning.**
2. The frozen v7 `calls()` was applied through a small FASTA wrapper.
3. **Output:** `rounds/L3521_hofstenia.txt`.

**Status: exploratory, not counted.**

---

## Result
| protein | length | domain-III loop | ring matches | tool call |
|---|---|---|---|---|
| HMIM006045 | 1,628 aa | LALFQV **ATF E GW** MEVMES | T-L-D-H-W, T-F-E-G-W | other (no K, ring < 3) |
| HMIM019623 | 1,429 aa | LALFQV **ATF E GW** IEVMAD | T-L-D-F-W, T-F-E-G-W | other |
| HMIM003197 | 1,939 aa | (none) | T-M-E-G-W, T-G-E-D-W, T-F-E-G-W, T-G-E-A-W | **Ca** (L-type ring) |
| HMIM021651 | 2,277 aa | (none) | S-L-E-G-W, T-G-E-D-W, T-Q-E-A-W, S-K-D-G-W, T-G-D-N-W | **Ca** (with T-type loops) |

**The answer:**
- ***Hofstenia*'s two sodium-type channels read E.** They match the comb jelly, the sea anemone, *Trichoplax* and the choanoflagellate, not the fly or human.
- **No sodium call was made** in 22,454 proteins.
- **My leaning, written in advance, was K, and it was wrong.**

**What it suggests.** Xenacoelomorpha are often placed as the **sister group of all other bilaterians**. If so, and if these gene models are complete, the E → K change happened **after** they split off: in the common ancestor of the other bilaterians (insects, worms, vertebrates).
- **Two cautions:**
  - Xenacoelomorph placement is still debated;
  - a secondary loss of K in this lineage can't be excluded from one genome.
- **The way to check:** read *Xenoturbella*'s full gene set when available, and early-branching protostomes and deuterostomes.

**Descriptive, everything else:**
- **Channels:** 2 calcium channels (one L-type ring, one with T-type loops), 16 potassium, 3 HCN, 14 K2P, 15 glutamate receptors.
- **Pumps:** Na⁺/K⁺ (2) and calcium (5). There is no copper-pump call, which is worth checking.
- **Iron enzymes:** 3, the tryptophan hydroxylases already seen in UniProt.

## Zenodo
- **Metadata files added and pushed:** `.zenodo.json` (title, creator, license, description, keywords) in both `dcf-math` and `dcf-genefinder`. Zenodo reads them automatically when it archives a release.
- **Steps for Gary:** see the reply.

## Record
No predictions graded. **406 of 558 passed, plus 3 split.**

## Summary
- **The earliest-branching bilaterian tested, the acoel worm *Hofstenia*, carries E, not K, in its sodium-type channels.** If acoels are the sister of all other bilaterians, the K of the fast nerve sodium channel arose after they split off.
- **This was exploratory,** and my stated leaning (K) was wrong. Both facts are recorded.
- **Both repositories now carry Zenodo metadata,** ready for archiving.

## Potential leads for future research
- **[E→K dating]** A pre-registered test on early protostomes and deuterostomes with full proteomes (e.g. a brachiopod, a hemichordate, an arrow worm). The prediction from this result: K present in all of them.
- **[Figure 4]** Add *Hofstenia* (E) as the row between the comb jelly and the fly.
- **[Copper pump]** Check *Hofstenia* for an ATP7 gene the rule missed.
- **[Zenodo]** Releases, then DOIs into both manuscripts.
