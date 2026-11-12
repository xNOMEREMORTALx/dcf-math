# DCF L3353: the iron ladder ranks eukaryotes too. Anaerobic parasites *Giardia* and *Entamoeba* read 4.4× above four aerobic protists, on the same enzymes as bacterial tier 3 (PFOR, Fe-hydrogenase, ferredoxin); the bacterial cuts do not transfer (2 of 3)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** `protist.zip`, six Ensembl Protists `pep.all.fa.gz` files. *Trichomonas vaginalis* was not included. *Entamoeba* is strain HM-1:IMSS-A, a subline of the pre-registered HM-1:IMSS.

**Pre-registrations:**
- `PREREGISTERED_L3345_eukaryotes.txt` (`2e40f492…`);
- the amendment for the missing file and strain (`8893c79a…`), frozen before scanning.

**Tool:** `dcf_motif_scan.py` (hash `7f8dd785…` matches the ledger's L3345 state). Scan output hashed (`6c8765d7…`).

---

## 1. Results
| organism | group (fixed in advance) | proteins with a ladder | ladder /1000 aa |
|---|---|---|---|
| *Entamoeba histolytica* | anaerobe | 18 | **0.0094** |
| *Giardia intestinalis* | anaerobe | 20 | **0.0089** |
| *Tetrahymena thermophila* | aerobe | 38 | 0.0029 |
| *Phytophthora infestans* | aerobe | 14 | 0.0021 |
| *Thalassiosira pseudonana* | aerobe | 8 | 0.0021 |
| *Dictyostelium discoideum* | aerobe | 4 | 0.0009 |

| id | prediction | result | verdict |
|---|---|---|---|
| **EU1** | both anaerobes above every aerobe | 0.0089 and 0.0094 vs ≤ 0.0029 | **PASS** |
| **EU2** | anaerobe median ≥ 3× aerobe median | 0.00915 / 0.0021 = **4.4×** | **PASS** |
| EU3 | bacterial cuts: anaerobes ≥ 0.023, aerobes < 0.023 | anaerobes 0.009 | **FAIL** |

## 2. Which proteins carry the ladders [after grading]
- ***Giardia*:**
  - **pyruvate:flavodoxin/ferredoxin oxidoreductase** (2);
  - **ferredoxins** Fd1, Fd2 and others (3);
  - **Fe-hydrogenase-1**;
  - a nitroreductase–ferredoxin fusion;
  - a 4Fe-4S binding domain protein;
  - 8 undescribed.
- ***Entamoeba*:**
  - **pyruvate:ferredoxin oxidoreductase**;
  - **iron hydrogenase**;
  - 4Fe-4S domain proteins (3);
  - an RNase L inhibitor (ABCE1);
  - plus a cysteine-rich surface protein and a zinc finger (probable false positives).
- **Aerobes:**
  - the mitochondrial **housekeeping set**: complex I 23 kDa subunit (NDUFS8), succinate dehydrogenase Fe–S subunit, ABCE1, DPYD;
  - cysteine-rich look-alikes (transporters, hypothetical proteins; 23 in *Tetrahymena*);
  - the diatom also carries two hydrogenase-like proteins.

**Reading.**
- **Across the tree of life the ladder points at the same machinery.** Anaerobic eukaryotes that took up PFOR and iron hydrogenase read 3–10× higher than aerobic eukaryotes, as tier-3 bacteria do.
- **The absolute scale is set by proteome size and background.** Eukaryotic proteomes are large and carry cysteine-rich look-alikes, so the bacterial cuts don't apply. The human warning (L3349) predicted this before the data arrived.

## Record
**This round:** 3 graded, 2 passed (EU1 and EU2 passed; EU3 failed).

**Total: 314 of 448 pre-registered predictions passed, plus 3 split.**

## Summary
- **The iron ladder works outside bacteria and archaea, as a ranking.** The oxygen-free gut parasites *Giardia* and *Entamoeba* read 4.4 times higher than four oxygen-breathing protists. Their ladders sit on the same enzymes as in hydrogen-fermenting bacteria: PFOR, iron hydrogenase and ferredoxins.
- **The bacterial tier numbers don't carry over.** Eukaryote protein sets are bigger and noisier, so they would need their own scale.
- **The manuscript is updated to v0.3** with this as a new section, a genuine extension of the finding to eukaryotes.

## Potential leads for future research
- **[Trichomonas]** Add *Trichomonas vaginalis* (Ensembl Protists, `trichomonas_vaginalis_g3/pep/`) to re-report EU1–EU3 on all three anaerobes.
- **[Eukaryote scale]** Pre-register a eukaryote-specific cut (e.g. 0.006, midway between groups) and test it on fresh protists: anaerobic *Blastocystis*, *Cryptosporidium*, *Spironucleus* or *Monocercomonoides*; aerobic *Chlamydomonas*, *Leishmania*, *Naegleria*.
- **[Ladder-P]** The stricter C-x₂-C-x₂-C-x₃-C-P motif may remove eukaryote look-alikes; develop on these six (now graded) and on human proteins.
- **[Metagenome tier]** Community energy metabolism from metagenome assemblies (novel).
