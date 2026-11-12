# DCF L3357: *Trichomonas* completes the eukaryote test. All three anaerobic parasites read above all four aerobic protists (4.2×), on PFOR and iron hydrogenases
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** UniProt reference proteome UP000001542, *Trichomonas vaginalis* strain ATCC PRA-98 / G3 (identity checked from the UniProt record and all 50,190 headers, OX=412133). Ensembl Protists and the other sources Gary tried did not have it.

**Rule (L3353 amendment):** scanned with the same frozen tool (`dcf_motif_scan.py` `7f8dd785…`). EU1–EU3 are re-reported on 7; the 6-file grade stands as the first grade, so **no new predictions are counted**.

---

## 1. Result
| organism | group | ladder /1000 aa |
|---|---|---|
| *Entamoeba histolytica* | anaerobe | 0.0094 |
| *Giardia intestinalis* | anaerobe | 0.0089 |
| ***Trichomonas vaginalis*** | anaerobe | **0.0040** |
| *Tetrahymena thermophila* | aerobe | 0.0029 |
| *Phytophthora infestans* | aerobe | 0.0021 |
| *Thalassiosira pseudonana* | aerobe | 0.0021 |
| *Dictyostelium discoideum* | aerobe | 0.0009 |

| id | on 6 (L3353, grade of record) | on 7 (re-report) |
|---|---|---|
| EU1 every anaerobe above every aerobe | PASS | **holds** (0.0040 > 0.0029) |
| EU2 median ratio ≥ 3× | 4.4× PASS | **4.2×, holds** |
| EU3 bacterial cuts transfer | FAIL | FAIL |

## 2. *Trichomonas* ladder proteins
Of its 45 ladder proteins:
- **PFOR family** (7: five "pyruvate dehydrogenase (NADP⁺)" and two named PFOR subunits);
- **Fe-only hydrogenases** (7, including TvhydB and the 64 kDa iron hydrogenase);
- **4Fe-4S domain proteins** (5);
- dihydropyrimidine/dihydrothymine dehydrogenases (5);
- 13 uncharacterised.

These are the enzymes of its hydrogenosome, the H₂-making organelle that replaced its mitochondria.

**Reading.**
- **The prediction made before the data held both ways.** *Trichomonas*'s 50,000-protein proteome dilutes the density to the lowest of the three parasites. Yet it still ranks above every aerobe, and its ladders sit on the same H₂-fermentation enzymes as tier-3 bacteria.
- **Across 7 protists, the anaerobe/aerobe ranking is perfect.**

The manuscript is updated to **v0.4**.

## Record
No new predictions graded (re-report). **314 of 448 passed, plus 3 split.**

## Summary
- **The third parasite confirms the eukaryote result.** *Trichomonas* has the most diluted reading because of its huge protein set. It still sits above all four oxygen-breathing protists, and its ladders are on PFOR and iron hydrogenases, the enzymes of its hydrogen-making organelle.
- **All seven protists now sort perfectly by oxygen-free vs oxygen-breathing metabolism.** The manuscript is at v0.4.

## Potential leads for future research
- **[Eukaryote scale]** Pre-register a eukaryote cut (e.g. 0.0035, between 0.0029 and 0.0040) on fresh protists.
- **[Size correction]** Normalise by the number of proteins with any cysteine-rich motif, to remove the proteome-size dilution (development first).
- **[Metagenome tier]**, **[Ladder-P]**: carried.
