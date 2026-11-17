# DCF L3741–L3745: Dimension was not the limit (HD tuning 0 of 3); an exact 6-letter word index wins (blind 3 of 3) and is now phone menu 36 (bundle 6.16, self-test 269/269)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [HD tuning], [Phone: HD index] from L3737.

---

## 1. Tuning the hyperdimensional index (`PREREGISTERED_L3741_hd_tuning.txt`)
| # | prediction | result |
|---|---|---|
| T1 | D = 20,000, K = 4: ≥ 90% at 15% substitutions | **89.75%: FAIL** (10,000 dimensions gave 89.5%) |
| T2 | D = 20,000, K = 3: ≥ 90% at 10% + 5%/5% indels | **34.9%: FAIL** |
| T3 | K = 3 better than K = 4 there | **34.9% vs 80.2%: FAIL** |

**0 of 3 passed.**

**Lesson:**
- **Doubling the dimension changed almost nothing.**
- **Shorter words were much worse.** Only 64 three-letter words exist, so every 137-letter strand contains most of them and the strands look alike.
- **The limit is the information carried per word, not the number of dimensions.**

## 2. Development: exact word indexes (`rounds/L3741_kmer_dev.txt`, same reads as L3737)
**The exact index:** for each strand, count its K-letter words. A read goes to the strand with the highest cosine similarity of word counts. This is what a hyperdimensional vector *approximates*, computed exactly.

| method | 5% | 5% + indels | 15% | 10% | 10% + 5%/5% indels |
|---|---|---|---|---|---|
| HD vectors, K = 4 (L3737) | 100% | 99.55% | 89.5% | 98.95% | 79.95% |
| exact 4-letter words | 100% | 99.95% | 92.3% | 99.45% | 84.3% |
| exact 5-letter words | 100% | 100% | 98.9% | 99.95% | 96.1% |
| **exact 6-letter words** | **100%** | **100%** | **99.75%** | **100%** | **97.9%** |

## 3. Blind confirmation on fresh data (`PREREGISTERED_L3745_dna_index.txt`; new strands and reads, seed 3745)
| # | prediction | result |
|---|---|---|
| I1 | ≥ 99% at 15% substitutions | **99.8%: PASS** |
| I2 | ≥ 95% at 10% substitutions + 5% insertions + 5% deletions | **98.4%: PASS** |
| I3 | ≥ 99.5% at 5% + 2.5%/2.5% indels | **100%: PASS** |

**3 of 3 passed.**

## 4. Phone bundle 6.16 (`phone/dcf_phone_bundle_6.15.zip` → `dcf_phone_bundle_6.16.zip`, 11 files)
- **New companion `dcf_dna_index.py`** (pure Python, no numpy): `Index(strands, K=6).find(read)`.
- **New menu 36, "DNA data store":**
  1. it encodes your text (or a file) into DNA strands with the existing codec;
  2. it simulates damaged reads at the rates you choose;
  3. it reports how many reads found their strand.
- **Example:** your name gives 3 strands of 137 nt, and 60 of 60 damaged reads were found.
- **Self-test: 269/269**, with a new row: the exact read finds itself, and ≥ 48 of 50 noisy reads are found.
- **Disclosed:** my first version of that row built test strands with a fresh random generator per letter, which made only 4 distinct strands (TTTT…, CCCC…). It failed; I fixed the *test*, not the index, and it now passes.

## Record
**+3 passed, 3 failed. 515 of 706 passed, plus 3 split.** Audit **182 of 233.**

## Summary
- **More dimensions did not help the hyperdimensional DNA index;** shorter words made it much worse (0 of 3).
- **The exact version of the same idea, matching reads by their 6-letter words, finds the right strand:**
  - **99.8%** of the time with 15% wrong letters;
  - **98.4%** with 10% wrong letters plus 10% insertions and deletions;
  - confirmed blind (3 of 3).
- **It is now menu 36 on the phone (bundle 6.16, self-test 269/269).** The DNA codec stores data, and the new index finds each damaged read's strand.

## Potential leads for future research
- **[Full DNA-store round trip]** Combine the index with the error-correcting code (`dcf_dna_ecc.py`). Cluster noisy reads by strand, take a per-position consensus, decode, and measure the byte error rate. That is a complete store-and-retrieve test.
- **[Cryptochrome tetrad]** Still needs the robin CRY4 sequence: https://rest.uniprot.org/uniprotkb/stream?format=tsv&fields=accession,organism_name,protein_name,sequence&query=gene:CRY4%20AND%20organism_id:9172
- **[Clock genes across the tree]** Where 24-hour timekeeping machinery appears; use a finder with measured sensitivity.
