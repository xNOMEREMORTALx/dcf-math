# DCF L3253: the body's seven metals (Na, Mg, K, Ca, Fe, Cu, Zn) — their proton, neutron and mass numbers do not appear as intervals in DNA (0 of 7; codon control 35 of 35); the mRNA-wide test frozen with its download
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Lead (Gary):** calcium, iron, magnesium, zinc, copper, sodium and potassium — "their proton, neutron and electrons and energies may play a part in the coding … placing their coding at detectable intervals in DNA or RNA or mRNA."

**Pre-registrations** (pushed before computing or downloading):
- `PREREGISTERED_L3253_metalDNA.txt` (`4c1b4cf8…1cf0`);
- `PREREGISTERED_L3253_mRNA.txt` (`54fa43b0…6b6b`).

---

## 1. The numbers tested
| metal | protons Z (= electrons) | neutrons N (main isotope) | mass number A | role (Gary's list) |
|---|---|---|---|---|
| sodium Na | 11 | 12 (²³Na) | 23 | fluid balance, nerve impulses |
| magnesium Mg | 12 | 12 (²⁴Mg) | 24 | stabilises DNA and ATP |
| potassium K | 19 | 20 (³⁹K) | 39 | nerve impulses |
| calcium Ca | 20 | 20 (⁴⁰Ca) | 40 | bone, muscle, signalling |
| iron Fe | 26 | 30 (⁵⁶Fe) | 56 | haemoglobin, Fe–S energy enzymes |
| copper Cu | 29 | 34 (⁶³Cu) | 63 | electron transfer, iron uptake |
| zinc Zn | 30 | 34 (⁶⁴Zn) | 64 | zinc fingers, DNA synthesis |

**Energies.** Ionization energies are measured in eV or kJ/mol and are not whole numbers, so they have no unit-free interval in nucleotides. They were not tested, as stated in the pre-registration.

## 2. DNA test [pre-registered]
**Method.**
- Fourier power at each of the **15 distinct periods** (11 … 64 nt), in 35 genomes.
- Both whole DNA and predicted coding regions.
- Each period placed exactly on a frequency bin and compared with its neighbouring frequencies.
- **Bar:** beat the neighbours in **≥ 27 of 35** genomes (p < 0.001 each), so the 30 tests together stay under 5% false alarm.

| period | genome DNA (genomes above / median ratio) | coding regions | metals using it |
|---|---|---|---|
| **3 (control)** | **35 / 8.1** | **35 / 41.8** | — |
| 11 | 17 / 1.000 | 20 / 1.001 | Na |
| 12 | 15 / 0.998 | 20 / 1.007 | Na, Mg |
| 19 | 18 / 1.006 | 14 / 0.995 | K |
| 20 | 15 / 0.997 | 13 / 0.991 | K, Ca |
| 23 | 20 / 1.004 | 17 / 1.000 | Na |
| 24 | 16 / 0.998 | 17 / 0.998 | Mg |
| 26 | 23 / 1.007 | 18 / 1.000 | Fe |
| 29 | 20 / 1.001 | **24** / 1.010 | Cu |
| 30 | 20 / 1.005 | 19 / 1.003 | Fe, Zn |
| 34 | 17 / 0.998 | 17 / 0.999 | Cu, Zn |
| 39 | 19 / 1.004 | 14 / 0.993 | K |
| 40 | 16 / 0.996 | 15 / 0.998 | Ca |
| 56 | 17 / 1.000 | 17 / 0.998 | Fe |
| 63 | 10 / 0.989 | 10 / 0.990 | Cu |
| 64 | 14 / 0.994 | 23 / 1.006 | Zn |

| id | metal | verdict |
|---|---|---|
| MD1–MD7 | Na, Mg, K, Ca, Fe, Cu, Zn | **all FAIL**: no period reaches 27 of 35; the best is 24 (copper's 29, coding), at chance level |

**Reading.** The method sees the real codon rhythm (period 3) in every genome, 8–42 times above its surroundings. At every metal number, the power equals the background (ratios 0.99–1.01).

**Running total.** Nuclear numbers have now been tested for **ten metals** as protein spacings (L3229, L3233) and DNA intervals (here). All are null. The genetic material does not encode the atomic numbers of the metals it uses. The metal information that genomes **do** carry is chemical:
- the 3-3-4 cysteine ladder that holds Fe–S clusters;
- zinc-finger and copper-site spacings;
- selenocysteine at stop codons;
- the iron-sensing hairpin in mRNA (L3249).

## 3. RNA and mRNA — frozen, waiting for data
**Why a bigger set is needed.** Testing mRNA needs thousands of transcripts, not 15. The script `mrna/dcf_mrna_wide.py` (SHA-256 `3e08ad67…4285`) is frozen and will:
- **W1:** scan every human mRNA for the iron-sensing hairpin and compare with two-letter-preserving shuffles; real 5′ UTRs should show ≥ 2× the shuffled rate;
- **W2:** confirm the known iron genes present;
- **W3:** run the same metal-number spectrum on human coding regions and UTRs.

**Fix made before freezing.** A smoke test on the 15 mRNAs already seen showed that scanning UTRs on their own clipped ACO2's hairpin, which overlaps the coding edge. The script now scans whole mRNAs and assigns each hit by position, and reproduces the L3249 result exactly.

**Action for Gary.** NCBI's folder could not be opened from here without your approval. Please open it and download the first human mRNA file:

https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/

Take **`human.1.rna.gbff.gz`**, or **`human.1.rna.fna.gz`** if that one is too large for the phone. Send it as it is (already compressed); renaming it `blind_mrna2` is fine. I could not check the file sizes; if both are too large, tell me and I will build a link for a smaller gene list.

## Record
**This round:** 7 graded, 0 passed (MD1–MD7).

**Total: 287 of 403 pre-registered predictions passed, plus 3 split.**

## Summary
- **The seven metals of your list leave no trace of their proton, neutron or mass numbers as intervals in DNA.** The test that detects the 3-letter codon rhythm in all 35 genomes finds nothing above background at any of the 15 metal numbers. All seven predictions failed.
- **With earlier rounds, that makes ten metals tested two ways, all null.** Genomes carry metal information chemically (binding-site shapes, the iron hairpin in mRNA), not as atomic counts.
- **The mRNA test is frozen and waiting.** One human mRNA file from NCBI will let me test your idea on RNA directly, and scan thousands of messages for iron hairpins nobody has catalogued.

## Potential leads for future research
- **[IRE-wide + Metal-mRNA]** Grade W1–W3 when the human mRNA file arrives.
- **[Metal-chem]** Gary's metals by their *chemistry*: label-free counts of Ca-binding EF-hands (DxDxDG…E loop), Mg-binding P-loops (GxxxxGK[ST]), Zn fingers (C2H2, CxxC…CxxC) and Cu sites across the 35 genomes vs lifestyle. Pre-register; this is where metal signals actually live.
- **[K-Na channels]** Potassium and sodium act through ion channels. The K⁺ channel selectivity filter TVGYG is a fixed motif that could be counted label-free (descriptive first).
- **[79-47]** Waiting for Gary's measurable form.
