# DCF L3265: two literature checks (the zinc-finger rhythm and the iron-ladder reading both look unreported), Note H rewritten around the ladder, and blind_20 frozen to test the four-tier scale
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [Lit-redox], [Lit-ZNF], [Fe-ladder note], [Redox-age b].

**Pre-registration:** `PREREGISTERED_L3265_blind20.txt` (SHA-256 `d898a166…14fb`), pushed to the ledger **before** any download.

---

## 1. Literature check: the 84-nt zinc-finger rhythm [L3261]
- **Howe & Song 2012** (*Nucleic Acids Research*, PMC3561982) surveyed spectral periodicities in coding sequences. It reports the 3-nt codon rhythm and others, but **does not mention an 84-nt (28-amino-acid) rhythm from C2H2 zinc-finger repeats**.
- **Known biology:** C2H2 zinc fingers come in tandem 28-aa repeats, so an 84-nt period in those genes is expected once you look. **What may be new is the observation that the 7/12/14/21/28/42 rhythm family in human mRNA comes entirely from about 436 zinc-finger genes** (period 84 at 5.6×; all other genes ≈ 1.0×).
- **Status:** in development only. The frozen test (`mrna/dcf_seven_znf.py`) waits for human RNA files 3 and 4.

## 2. Literature check: the iron-ladder redox reading [L3257]
- **The nearest modern work** is an annotation-free oxygen-use predictor (bioRxiv 10.1101/2024.01.16.575888). It sorts ~3,300 genomes into aerobe / anaerobe / facultative at about 70% using amino-acid 3-mers, nucleotide 5-mers and protein-language embeddings.
- **It does not use or mention** Fe–S clusters, ferredoxin, CxxC, copper or CuA. Its classes are oxygen classes, which our ladder was shown **not** to track (L3173).
- **Andreini *et al.* 2017** (PLoS ONE e0171279) remains the prior art for "anaerobes carry more Fe–S proteins".
- **Reading:** no published method was found that sorts raw genomes into ferredoxin / oxygen / fermentative metabolism from one iron motif and one copper motif. Not finding it is not proof; a specialist check is still needed before submission.

## 3. Note H v0.4
`notes/Note_FeS_ferredoxin_signature_draft_v0.4.md` (pushed). Changes:
- **the 3-3-4 ladder (C-x₂-C-x₂-C-x₃-C) is now the main marker** (§1b);
- the L3257 three-way call (18 of 23) added to the results table;
- the **four-tier scale** (§4d) and the literature check (§4e);
- the phylogeny confound marked as partly addressed (6 of 6 lineage pairs, five phyla).

Method lessons from L3261 (one transcript per gene; empirical null instead of window bootstrap; shuffler retry) were added to `INTEGRATION.md`.

## 4. blind_20: does the four-tier scale hold on fresh genomes? [pre-registered]
All 16 names and accessions are absent from both seen lists (0 hits each).

| tier | expected ladder per 1,000 aa | genomes |
|---|---|---|
| 1 lactic | < 0.0045 | *L. rhamnosus* GG, *S. agalactiae*, *L. salivarius*, *L. gasseri* |
| 2 O2 | 0.0045–0.023 | *Azotobacter*, *Paracoccus* chr1, *Halomonas*, *Burkholderia thailandensis* chr1 |
| 3 H2 fermenters | 0.023–0.060 | *C. botulinum*, *C. thermocellum*, *Fervidobacterium*, *C. cellulolyticum* |
| 4 Fd-based | > 0.060 | *Methanobrevibacter*, *Thermodesulfovibrio*, *Sulfurihydrogenibium*, *Syntrophobacter* |

| id | prediction |
|---|---|
| T1 | group medians rise strictly from tier 1 to tier 4 |
| T2 | ≥ 11 of 16 in the right tier (chance ≈ 4) |
| T3 | Spearman ρ(tier, ladder) ≥ 0.75 |
| T4 | all 4 lactic genomes < 0.0045 |
| T5 | ≥ 3 of 4 tier-4 genomes > 0.060 |

**Declared risks:** *Azotobacter* (nitrogenase, many ferredoxins) and *Paracoccus* may read high for tier 2; *Sulfurihydrogenibium* breathes oxygen while running rTCA; tiers 2 and 3 overlap at 0.021–0.025.

## Action for Gary: blind_20 (16 links)
Open each link in your browser; it downloads a GenBank text file. Zip all 16 as **`blind_20.zip`** (any file names are fine; I identify them by their LOCUS line).

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_013198
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_004116
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007929
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008530
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_012560
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008686
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_014532
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007651
9. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009495
10. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009012
11. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009718
12. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_011898
13. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009515
14. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_011296
15. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_012438
16. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008554

**Still needed for the zinc-finger test:** `human.3.rna.fna.gz` and `human.4.rna.fna.gz` from https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/ , zipped together.

## Record
No predictions graded this round. **291 of 411 passed, plus 3 split.**

## Summary
- **Both candidate novelties survived a first literature check.** The 84-nt zinc-finger rhythm is not in the main spectral-periodicity survey, and the iron-ladder / copper reading of metabolism is not in the nearest modern classifier, which uses generic k-mers and predicts oxygen use instead.
- **Note H now leads with the 3-3-4 ferredoxin ladder** and its four-tier scale: lactic fermenters, oxygen breathers, hydrogen-making fermenters, and ferredoxin-based respirers and autotrophs.
- **blind_20 is frozen:** 16 fresh genomes, four per tier, five predictions, pushed before download.

## Potential leads for future research
- **[blind_20]** Grade T1–T5 when the zip arrives.
- **[ZNF-84]** Grade Z1–Z3 on human RNA file 3 (or 4) with the frozen script.
- **[Lit-redox b]** Specialist check (ferredoxin-family surveys, Fd-dependent metabolism reviews) before submitting Note H.
- **[Fe-domain P]** Does adding the trailing proline (CxxCxxCxxxCP) sharpen the ladder? Develop on seen genomes only.
- **[Cu-cbb3]** A cbb3-oxidase marker so microaerophiles get an O2 call.
- **[G-short]** Short-call filter for the gene finder's 180–239 nt calls (*Chloroflexus* precision).

Sources:
- [Howe & Song 2012, NAR (PMC3561982)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3561982/)
- [Annotation-free O2-utilization predictor, bioRxiv 2024.01.16.575888](https://www.biorxiv.org/content/10.1101/2024.01.16.575888)
- [Andreini, Rosato & Banci 2017, PLoS ONE e0171279](https://doi.org/10.1371/journal.pone.0171279)
