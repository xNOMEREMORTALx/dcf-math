# DCF L3373: proline marks the real iron ladder (68–85% in microbes, 0% in human look-alikes); acetylcholine's receptors and cholinesterases found label-free in human mRNA (development); mouse test frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Leads:** Gary's request to **track proline and acetylcholine**; [Ladder-P].

**Pre-registration:** `PREREGISTERED_L3373_ach_mouse.txt` (`d801876d…9a81`) and the script `dcf_ach_L3373.py`, pushed before any mouse file is downloaded.

---

## 1. Proline: the fingerprint of a genuine ferredoxin ladder [development]
**Residue right after the 4th cysteine of C-x₂-C-x₂-C-x₃-C:**

| ladders in… | n | proline | next most common |
|---|---|---|---|
| prokaryotes, tier 2 | 187 | **85%** | E 3%, D 3% |
| prokaryotes, tier 3 | 296 | **68%** | K 8%, S 5% |
| prokaryotes, tier 4 | 976 | **78%** | A 3%, K 3% |
| anaerobic protists (6) | 232 | 50% | C 7%, K 5% |
| aerobic protists (7) | 127 | 35% | L 10%, S 7% |
| **human look-alikes** | 12 | **0%** | E 17%, R 17% |

**Reading.**
- In bacterial-type [4Fe-4S] ferredoxins the cluster-binding loop ends **C-P**; the proline helps shape the loop around the cluster.
- **About three quarters of microbial ladders keep it, while cysteine-rich look-alikes (integrins, metallothionein, zinc fingers, choline transporter-like SLC44A1) never do.**
- The proline share is lower in protists, especially aerobic ones, whose few ladders include more look-alikes. **This is the structural reason the stricter Ladder-P motif works for eukaryotes** (L3369). Added to manuscript v0.7.

## 2. Acetylcholine: the machinery, label-free [development, human files 1–4]
| target | motif | result |
|---|---|---|
| **acetylcholine and related receptors** (ligand-gated ion channels) | Cys-loop C-x₄₋₆-[FY]-**P**-[FYWM]-D-x₃-C (corrected after L3293) | 10 hits, **all 10 true** (CHRNA9, CHRNB3, CHRNG; GABRD, E, G1, G3, P; HTR3A, E); recall 10/14 |
| **cholinesterases** (destroy acetylcholine at the synapse) | serine site **F-G-E-S-A-G** | **ACHE and BCHE both found**; also carboxylesterases CES1, CES5A (same enzyme family) and FAM177A1 |
| choline transporter-like (SLC44) | — | SLC44A1 carries one ladder **without** proline (a look-alike) |

**Reading.**
- From mRNA sequence alone, the tools now find **both halves of acetylcholine signalling**: the receptor that responds to it and the enzyme that ends it.
- **The receptor's signature carries a proline too** (the F/Y-P-x-D at the tip of the Cys-loop). Proline marks the working core of both the iron ladder and the acetylcholine receptor loop.
- The GABA-A receptors missed in L3293 are now caught by the corrected motif.
- **Development only.** The fair test is mouse mRNA.

## 3. Mouse test [pre-registered]
| id | prediction |
|---|---|
| AC1 | Cys-loop precision ≥ 0.75 and recall ≥ 0.60 |
| AC2 | F-G-E-S-A-G finds every *Ache*/*Bche* present, with ≤ 5 other hits |

## Action for Gary
From **https://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/** download **`mouse.1.rna.fna.gz`** and **`mouse.2.rna.fna.gz`**. Zip them as **`mouse_rna_1_2.zip`**. It's the same folder layout as the human files you sent before.

## Record
No predictions graded. **316 of 451 passed, plus 3 split.**

## Summary
- **Proline is the mark of a real iron ladder.** About 3 in 4 microbial ladders end with a proline after the last cysteine; the human look-alikes never do. That's why the stricter motif works for eukaryotes.
- **Acetylcholine, tracked:**
  - the receptor motif found 10 receptor genes with no false hits;
  - the enzyme motif found both cholinesterases;
  - the receptor's signature also turns on a proline.
- **A fresh test on mouse mRNA is frozen.**

## Potential leads for future research
- **[Mouse ACh]** Grade AC1–AC2 when the mouse files arrive.
- **[Proline blind]** Pre-register the proline share as a real-vs-look-alike classifier on fresh genomes (e.g. ≥ 60% P after ladders in bacteria; < 20% in mammalian proteomes).
- **[ACh evolution]** Do bacteria have the cholinesterase site (F-G-E-S-A-G)? Scan the 37 graded genomes (development).
- **[Ladder-P blind]**, **[Venue]**: carried.
