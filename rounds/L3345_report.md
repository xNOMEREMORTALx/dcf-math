# DCF L3345: does the iron ladder work in eukaryotes? Anaerobic parasites vs aerobic protists, frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Lead:** [Eukaryote check]. **Pre-registration:** `PREREGISTERED_L3345_eukaryotes.txt` (`2e40f492…b279`), pushed before any download.

---

## 1. The idea
- **Some single-celled eukaryotes live without oxygen:** *Giardia* (gut parasite), *Trichomonas* (urogenital parasite), *Entamoeba* (amoebic dysentery).
- **They run their energy metabolism the way tier-3 bacteria do:** pyruvate:ferredoxin oxidoreductase (PFOR) and ferredoxins, and in *Trichomonas* and *Entamoeba* also iron hydrogenases. Their mitochondria are reduced to "hydrogenosomes" or "mitosomes".
- **Aerobic protists respire oxygen in full mitochondria**, so they should read low: *Dictyostelium*, *Phytophthora*, the diatom *Thalassiosira*, *Tetrahymena*.
- **Method change:** eukaryote genes have introns, so the gene finder can't be used. The test runs the frozen motif scanner on Ensembl's ready-made protein files.

## 2. Predictions
| id | prediction |
|---|---|
| EU1 | every anaerobe reads higher than every aerobe |
| EU2 | the anaerobes' median is ≥ 3× the aerobes' |
| EU3 (risky) | with the bacterial cuts, anaerobes ≥ 0.023 and aerobes < 0.023 |

**Declared risks:**
- large eukaryotic proteomes dilute the density;
- *Trichomonas* has a very large proteome;
- the diatom carries plant-type 2Fe-2S ferredoxins, which are not counted.

## Action for Gary (two ways)
**A. Quickest:** send me this URL in a message and approve the page when asked; I'll find the exact files:
`https://ftp.ensemblgenomes.ebi.ac.uk/pub/protists/current/fasta/`

**B. By hand:**
1. Open that folder in your browser.
2. For each species folder below, open `pep/` and download the file ending **`.pep.all.fa.gz`**.
3. Zip all seven as **`protists.zip`**.

Species folders:
- *Giardia intestinalis* (WB / assemblage A)
- *Trichomonas vaginalis* (G3)
- *Entamoeba histolytica* (HM-1:IMSS)
- *Dictyostelium discoideum*
- *Phytophthora infestans*
- *Thalassiosira pseudonana*
- *Tetrahymena thermophila*

## Record
No predictions graded. **312 of 445 passed, plus 3 split.**

## Summary
- **The first test outside bacteria and archaea is frozen.** If the iron ladder reflects ferredoxin-based energy metabolism, the oxygen-free parasites *Giardia*, *Trichomonas* and *Entamoeba* should read higher than four aerobic protists. That would extend the manuscript to eukaryotes.
- **Seven protein files are needed from Ensembl Protists.** Approving the page lets me find them; otherwise they can be downloaded by hand.

## Potential leads for future research
- **[Eukaryote check]** Grade EU1–EU3 when the files arrive.
- **[Venue]**, **[Independent review]**: carried.
