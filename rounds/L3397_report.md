# DCF L3397: the stricter Ladder-P motif goes to a blind test on five fresh protists
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Lead:** [Ladder-P blind]. **Pre-registration:** `PREREGISTERED_L3397_ladderp.txt` (`e73ea5f4…a6ea`) and the script `dcf_ladderp_L3397.py`, pushed before download. The script reproduces the development values exactly.

---

## 1. Why
- In development (L3369, L3373), adding the proline after the last cysteine (C-x₂-C-x₂-C-x₃-C-**P**):
  - removed all 12 human look-alikes;
  - opened a clean gap between oxygen-free and oxygen-breathing protists (lowest anaerobe 0.0020 vs highest aerobe 0.0014). The plain ladder overlapped.
- **About 3 in 4 real microbial ladders end in C-P;** look-alikes never do.
- **This test checks whether that holds on protists the motif has never seen.**

## 2. The test
| group | proteome (UniProt reference, verified) |
|---|---|
| oxygen-free | *Entamoeba invadens* IP1; *Entamoeba dispar* SAW760 |
| oxygen-breathing | *Toxoplasma gondii* ME49; *Plasmodium falciparum* 3D7; *Paramecium tetraurelia* |

| id | prediction |
|---|---|
| LP1 | the Ladder-P cut (0.0017) sorts all 5 correctly |
| LP2 | Ladder-P separates the groups more widely than the plain ladder |

**Declared limitations:**
- both oxygen-free species are *Entamoeba* (genus already seen through *E. histolytica*);
- *Plasmodium* blood stages lean on glycolysis but keep a respiring mitochondrion;
- my candidate ID for *Monocercomonoides* turned out to be *Streblomastix*, a non-reference set, and was excluded.

## Action for Gary: 5 downloads
Zip as **`protists3.zip`**:
1. *E. invadens*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000014680
2. *E. dispar*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000008076
3. *Toxoplasma*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000001529
4. *Plasmodium*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000001450
5. *Paramecium*: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000000600

## Record
No predictions graded. **321 of 459 passed, plus 3 split.**

## Summary
- **The proline-ending ladder, which cleaned up eukaryotes in development, now gets a fair test** on five protists it has never seen: two oxygen-free amoebae, and three oxygen-breathers (the parasites behind toxoplasmosis and malaria, plus *Paramecium*).
- **Its weakness is stated up front:** both oxygen-free species come from one genus.

## Potential leads for future research
- **[Ladder-P blind]** Grade LP1–LP2 when the files arrive.
- **[More anaerobes]** Find verified UniProt sets for anaerobes outside *Entamoeba* (*Monocercomonoides*, *Mastigamoeba*, *Trimastix*) for a stronger follow-up.
- **[Lineage map]**, **[Venue]**: carried.
