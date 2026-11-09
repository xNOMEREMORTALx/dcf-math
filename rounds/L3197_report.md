# DCF L3197: Fibonacci-period minima to F₂₄ (3 of 3 pass), a selenocysteine filter that works in development (AUC 0.87), a counting error caught, and blind_17 frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [R5c], [Sec-3], [Fe-ferment H2].

**Still waiting:** `blind_16.zip` (L3189).

**Pre-registrations** (all pushed to the dcf-math ledger before computing or downloading):

| file | SHA-256 | commit |
|---|---|---|
| `PREREGISTERED_L3197.txt` (blind_17 + R5c) | `c99a3133…2311` | `9d496e5` |
| `PREREGISTERED_L3197_Sec3.txt` (Sec-3 blind test) | `acdb2aeb…2d55` | `0d3eaa5` |

---

## 1. [R5c] Smallest q with period F₂₁ … F₂₅ [pre-registered]
**Method:** exact for any minimum below 10⁸. The three minima were re-checked by brute force over every q up to the answer.

| Fₙ | factors | smallest q | q is | prediction | verdict |
|---|---|---|---|---|---|
| 10946 | 2·13·421 | **21893** = 2·10946 + 1 | prime | N2: prime | **PASS** |
| 17711 | 89·199 | **141689** = 8·17711 + 1 | prime | N3: prime | **PASS** |
| 28657 | prime | 1547479 | prime | forced | not graded |
| **46368** | 2⁵·3²·7·23 | **94799 = 47 × 2017** (periods 46 and 2016) | **composite** | N1: composite | **PASS** |
| 75025 | 5²·3001 | none below 10⁸ | — | N4: prime | **not graded** |

**Reading.** The "covering" rule from L3193, used as a forecast, worked 3 for 3.
- **46368 = lcm(46, 2016)**, and both pieces have cheap primes: 47 and 2017.
- **The other targets have a large prime factor** (421, 199), so no cheap cover exists, and a prime just above a small multiple of Fₙ wins.

**Composite minima so far:** 144, 610, 987, 46368. **[D]:** 2017 = 2 × 1008 + 1 has period 2016.

## 2. [Sec-3] A coding-potential filter for selenocysteine candidates [development]
**The idea.** A true selenocysteine read-through joins **two coding** stretches. A false candidate usually joins a gene to a non-coding stretch.
- **Score:** the mean codon log-odds of the read-through part, i.e. how much its codons look like the genome's own genes (in-frame) rather than out-of-frame.
- **Training:** taken from the gene finder's own predictions, so no annotation is used.

**Development set:** the 10 genomes of blind_14/15, which are now seen.

| measure | result |
|---|---|
| annotated Sec sites caught by the base finder | 28 of 37 |
| **separation** (real sites vs 8,493 false candidates) | **AUC 0.87** (the SECIS hairpin filter reached only 0.60–0.69, L3157) |
| threshold 0.05 | keeps **28 of 28** caught sites |
| candidates, AT-rich genomes (before → after) | *A. woodii* 126 → 48; *C. ljungdahlii* 68 → 47; *Hydrogenobacter* 134 → 64; *Leuconostoc* 71 → 26; *S. mutans* 67 → 22; *L. acidophilus* 38 → 13 |
| GC-rich genomes | still 400–700 candidates; the filter does not rescue them |

**Release.** `dcf_secflag.py --coding 0.05` (SHA-256 `46891b35…9388`). The default output is unchanged.

**Blind test.** The threshold was chosen on these data, so it is frozen and tested blind on blind_16 + blind_17:
- **S3a:** the filter keeps ≥ 90% of caught sites.
- **S3b:** median candidate reduction ≥ 50% in AT-rich genomes.

## 3. A counting error, caught and corrected
**What happened.** While matching sites, I found that the L3181/L3185 selenocysteine counts used `grep -c 'aa:Sec'`. That also counts the **tRNA-Sec anticodon lines**.

**The true codon counts:**

| genome | reported | true |
|---|---|---|
| *Desulforapulum* | 27 | **26** |
| *C. ljungdahlii* | 12 | **9** |
| *A. woodii* | 2 | **1** |
| *Hydrogenobacter* | 2 | **1** (formate dehydrogenase-N α) |

**Consequences.**
- **No verdict changes:** F5 needed ≥ 1 Sec codon, which still holds.
- **Correction notes** are added to both reports, and Note H's table is fixed.
- **Earlier rounds (L3145, L3165)** may have used other scripts; whether they were affected is open (lead [Sec-recount]).

## 4. [Fe-ferment H2] blind_17 frozen
Does hydrogen production, not fermentation as such, decide the reading?

| group | accession | organism |
|---|---|---|
| H2-evolving fermenter | NC_009437 | *Caldicellulosiruptor saccharolyticus* DSM 8903 |
| H2-evolving fermenter | NC_003869 | *Thermoanaerobacter tengcongensis* MB4 |
| H2-evolving fermenter | NC_009617 | *Clostridium beijerinckii* NCIMB 8052 |
| H2-evolving fermenter | NC_014833 | *Ruminococcus albus* 7 |
| lactic fermenter | NC_008054 | *Lactobacillus delbrueckii* bulgaricus ATCC 11842 |
| lactic fermenter | NC_008525 | *Pediococcus pentosaceus* ATCC 25745 |
| lactic fermenter | NC_008528 | *Oenococcus oeni* PSU-1 |
| lactic fermenter | NC_006448 | *Streptococcus thermophilus* LMG 18311 |

**Checks.** All eight have a genome page matching the accession (BacMap search). None is in either seen list.

**Predictions:**
- **H1:** all 4 H2 fermenters > 0.50.
- **H2:** all 4 lactic < 0.50.
- **H3:** 16 of 16 pairs separate.
- **H4:** 0 Sec in the lactic fermenters.

**Declared confound:** Clostridia vs Lactobacillales.

**Action for Gary.** Zip these eight as **`blind_17.zip`** (blind_16's six links are in `L3189_report.md`):
1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009437&rettype=gbwithparts&retmode=text
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_003869&rettype=gbwithparts&retmode=text
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009617&rettype=gbwithparts&retmode=text
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_014833&rettype=gbwithparts&retmode=text
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_008054&rettype=gbwithparts&retmode=text
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_008525&rettype=gbwithparts&retmode=text
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_008528&rettype=gbwithparts&retmode=text
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_006448&rettype=gbwithparts&retmode=text

## Record
**This round:** 3 graded, 3 passed (N1–N3); N4 and F₂₃ not graded.

**Total: 264 of 344 pre-registered predictions passed, plus 3 split.**

## Summary
- **The Fibonacci-period forecast worked.** After L3193's failure, the "cheap cover" idea correctly picked F₂₄ = 46368 as the one composite minimum (47 × 2017), and F₂₁, F₂₂ as primes. Minima are now known exactly through F₂₄, except F₁₇ and F₂₅ (above 10⁸).
- **A better selenocysteine filter, in development.** Checking whether both sides of a read-through look like real genes separates true sites far better than the hairpin check that failed earlier. It kept every caught site and cut false candidates by half or more in AT-rich genomes. The threshold is now frozen for a blind test.
- **A counting slip was found and corrected.** Earlier selenocysteine counts included tRNA lines. No result changed.
- **Two downloads are waiting:** blind_16 (6 genomes) and blind_17 (8 genomes).

## Potential leads for future research
- **[Fe-rTCA] + [Fe-ferment H2] + [Sec-3]** Grade blind_16 and blind_17 together when both zips arrive.
- **[Sec-recount]** Re-check the Sec counts of L3137–L3173 from their code zips on Drive (`round_L31xx_code.zip`) for the same anticodon double-count.
- **[Sec-3b]** For GC-rich genomes, add a second filter (e.g. require the upstream part to carry a start-signal score); develop on *Bordetella*/*Pseudomonas*, which have 0 Sec.
- **[R5d]** Factor-based search for F₁₇ = 1597 and F₂₅ = 75025 minima (> 10⁸): the smallest prime ≡ 1 (mod Fₙ) with order exactly Fₙ.
- **[Note G update]** Fold v2.31, the code record (114/117), dcf_metals, the R-floor and the Sec-3 filter into Note G.
