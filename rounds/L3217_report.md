# DCF L3217: why the start fix lost genes (it shrank some to fragments), a guarded fix, and blind_18 frozen to test the ferredoxin reading by lineage-matched pairs
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [G-starts c], [Fe-Fd], [Sec-O].

**Pre-registration:** `PREREGISTERED_L3217.txt`, SHA-256 `6fff72c90b4b0979cd6711024b66c1018f49582bf30307338365d0c0b69e6623`, commit `9868ca6`, pushed before download.

---

## 1. [G-starts c] What the v2.32 candidate lost
**Method.** I compared the annotated genes found by v2.31 but missed by v2.32c in the two genomes that failed T3 (L3213). Both genomes are now seen, so this is development.

| genome | lost | gained | what happened |
|---|---|---|---|
| *Ruminococcus albus* 7 | 23 | 3 | the start was moved so far downstream that the gene became a **fragment**: 432 → 24 nt, 324 → 42 nt, 183 → 42 nt |
| *Nitrosospira* | 22 | 6 | the same: 462 → 117 nt, 912 → 9 nt, 1164 → 117 nt |

**Cause.** With heavy GTG/TTG penalties, the re-pick sometimes chose the only ATG left, close to the stop codon. Nothing stopped a start from leaving a gene shorter than the tool's own minimum gene length.

**Fix (v2.32b candidate).** A re-picked start must leave at least the minimum gene length (240 nt; 180 nt at GC > 0.55). If no candidate qualifies, all are allowed, as before.

**Development check (full runs):**

| genome | v2.31 found / start | v2.32c found / start | **v2.32b found / start** |
|---|---|---|---|
| *Ruminococcus* | 90.8 / 89.5 | 90.2 / 89.8 | **90.9 / 89.7** |
| *Nitrosospira* | 89.3 / 74.0 | 88.8 / 77.0 | **90.0 / 77.5** |
| *Chlorobaculum* | 89.7 / 75.1 | 89.7 / 81.0 | **90.0 / 81.3** |
| *Bordetella* | 95.3 / 79.0 | 95.4 / 84.7 | **95.7 / 84.8** |

- **Genes found are now at or above v2.31 in all four,** and the start gains are kept.
- **Correct was unchanged** except *Ruminococcus* (−0.1).

**Status.** These four genomes were used to make the fix, so the result is development only. v2.32b (`dev/dcf_genefinder_v2.32b_candidate.py`, SHA-256 `69cc0a61…892e`) is frozen and re-tested blind on blind_18 (D4–D6).

## 2. [Fe-Fd] Lineage-matched pairs
L3213's ferredoxin reading was formed after the fact, and its groups differed in lineage (Clostridia vs Lactobacillales). This test pairs organisms **within one phylum**.

| pair | ferredoxin-based member | partner (same phylum) |
|---|---|---|
| P1 | NC_013173 *Desulfomicrobium baculatum* (sulfate reducer) | NC_008095 *Myxococcus xanthus* DK 1622 (aerobe) |
| P2 | NC_009253 *Desulfotomaculum reducens* MI-1 (sulfate/metal reducer) | NC_006322 *Bacillus licheniformis* ATCC 14580 |
| P3 | NC_012115 *Nautilia profundicola* (reductive TCA, H2) | NC_009850 *Arcobacter butzleri* RM4018 |

**Predictions:**
- **D1:** the first member reads higher in 3 of 3 pairs.
- **D2:** first members > 0.50, partners < 0.50.
- **D3 [Sec-O]:** any Sec codon in a partner sits in a formate dehydrogenase. Graded only if one exists.

**Checks.** None of the six is in either seen list. Three accessions are confirmed directly; *Desulfomicrobium*, *Nautilia* and *Arcobacter* are confirmed only by organism/genome-paper pages, so the LOCUS check decides.

## 3. Action for Gary: blind_18.zip (6 files)
1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_013173&rettype=gbwithparts&retmode=text
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_008095&rettype=gbwithparts&retmode=text
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009253&rettype=gbwithparts&retmode=text
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_006322&rettype=gbwithparts&retmode=text
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_012115&rettype=gbwithparts&retmode=text
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_009850&rettype=gbwithparts&retmode=text

## Record
No predictions graded this round. **274 of 357 passed, plus 3 split;** D1–D6 will take it to 363.

## Summary
- **The start fix's one failure is understood.** When it penalised the rare start codons, it sometimes picked an ATG so close to the end that a real gene shrank to a meaningless fragment. A one-line guard (never shorter than the tool's own minimum gene) removes the loss and keeps the start gains, in development.
- **The guarded version is frozen for a fresh blind test.**
- **The new ferredoxin idea gets a fairer test.** Three pairs of related organisms, each pairing a ferredoxin-based anaerobe with an oxygen-using relative from the same phylum, so ancestry is held roughly constant.

## Potential leads for future research
- **[Blind 18]** Grade D1–D6 when `blind_18.zip` arrives.
- **[Fe-cut]** Add a 0.45–0.55 grey zone to the reading label after blind_18 (`dcf_metals.py`).
- **[Sec-3b]** A GC-rich second filter for the selenocysteine finder.
- **[Note H v0.4]** Fold in the pair test; check the ferredoxin reading against Andreini 2017's energy-category breakdown.
