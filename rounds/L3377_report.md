# DCF L3377: acetylcholine receptors found in mouse with no false hits (1 of 2); the energy path meets data storage: "information iron" in DNA repair is a switch, "energy iron" is a dial; blind_24 frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** `mouse_rna_1_2`: RefSeq mouse.1 and mouse.2 RNA files (36,054 NM transcripts; 15,858 genes, one transcript each).

**Pre-registrations:**
- `PREREGISTERED_L3373_ach_mouse.txt` (`d801876d…`); script `dcf_ach_L3373.py` (`6598203b…` matches the ledger); output hashed (`c1cc9ed3…`) before grading;
- **new:** `PREREGISTERED_L3377_blind24.txt` (`4fefb609…db95`).

**Leads:** [Mouse ACh]; Gary's new lead: **the energy path linked to data storage and retrieval in biological systems**.

---

## 1. Mouse acetylcholine test
| id | prediction | result | verdict |
|---|---|---|---|
| **AC1** | Cys-loop precision ≥ 0.75, recall ≥ 0.60 | **18 hits, all 18 true** (precision 1.00), recall 18/23 = 0.78 | **PASS** |
| AC2 | F-G-E-S-A-G finds every *Ache*/*Bche*, ≤ 5 other hits | *Ache* ✓ *Bche* ✓, but **9 other hits** | **FAIL** |

- **AC1:** found *Chrna2, a3, a4, a5, a6, b1, b4* (7 acetylcholine receptors); GABA-A *Gabra1, a3, a4, g1, g3, p, q*; glycine *Glra1, a3, a4, Glrb*. Missed: *Gabrb1–3*, *Gabrr1*, *Gabrr3*.
- **AC2:** all 9 extra hits are **carboxylesterases** (*Ces1a, d, e, f, g; Ces2b, e, g; Cel*). These are the same enzyme family, which is greatly expanded in mice. F-G-E-S-A-G marks the cholinesterase/carboxylesterase family, not acetylcholine-specific enzymes.

## 2. The energy path and biological data storage [development, 37 graded genomes]
**The biology.**
- The machines that **store, copy, read and repair DNA** also carry 4Fe-4S iron clusters: DNA primase, DNA polymerases, helicases, and the repair glycosylases endonuclease III and MutY.
- Barton and colleagues proposed that repair enzymes use these clusters to signal through DNA by electron transfer, to locate damage.
- **This "information iron" sits in a different motif from the energy ladder:** the EndoIII/MutY "FCL" loop, C-x₆-C-x₂-C-x₅-C.

**Measured:**
| per 1,000 genes | tier 1 lactic | tier 2 O₂ | tier 3 H₂ ferm | tier 4 Fd-based | ρ with tier |
|---|---|---|---|---|---|
| **energy iron** (3-3-4 ladder) | 0 | 4.5 | 14.6 | 40.8 | 0.960 |
| **information iron** (FCL loop proteins) | **0** | 0.48 | 0.56 | 1.08 | 0.741 |

- **Validation** (annotation, after counting): FCL proteins are endonuclease III (22 + 6 domain proteins) and **MutY** (11). Also **CRISPR Cas6** endoribonucleases (5) and a few others, about 65% repair glycosylases.
- **Lactic fermenters: 8 of 9 have no information-iron protein at all. All 28 iron-using genomes have at least one.**

**Reading.**
- **Information iron behaves like a switch:** present in every iron-using cell, about twice as common from tier 2 to tier 4.
- **Energy iron behaves like a dial:** it rises about 9-fold over the same range.
- **Cells that abandon iron (lactobacilli are famous for needing almost none) drop it from both their energy path and their DNA-repair path.**
- **The CRISPR link:** CRISPR is the bacterial immune system's **stored memory** of past viruses. Cas6 cuts the stored array into guide RNAs, so it is the retrieval step. Some Cas6 and Cas4 proteins carry iron–sulfur clusters. So iron chemistry touches energy, DNA repair, and the retrieval of stored immune memory.

## 3. blind_24 [pre-registered]
| group | genomes |
|---|---|
| lactic | *Lactobacillus brevis*, *Leuconostoc citreum*, *Lactobacillus casei*, *Streptococcus sanguinis* |
| iron users | *Geobacillus kaustophilus* (O₂), *Kineococcus radiotolerans* (O₂), *Methanosaeta thermophila* (Fd), *Desulfatibacillum alkenivorans* (Fd) |

| id | prediction |
|---|---|
| IF1 | ≥ 3 of 4 lactic genomes have **no** information-iron protein |
| IF2 | all 4 iron users have at least one |
| IF3 | among iron users, energy iron varies more (max/min) than information iron (the dial vs the switch) |

## Action for Gary: blind_24 (8 links)
Zip all 8 as **`blind_24.zip`**.

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008497
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_010471
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008526
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009009
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_006510
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009664
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008553
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_011768

## Record
**This round:** 2 graded, 1 passed (AC1 passed; AC2 failed).

**Total: 317 of 453 pre-registered predictions passed, plus 3 split.**

## Summary
- **Mouse confirms the receptor finder:** 18 receptor genes found from sequence alone, every one correct, including 7 acetylcholine receptors. The enzyme motif finds both cholinesterases but also mice's large carboxylesterase family, so it marks the family, not acetylcholine specifically.
- **Energy and information share iron, but differently:**
  - the iron that repairs DNA (endonuclease III, MutY) is a **switch**, present in every iron-using microbe;
  - the iron that powers energy metabolism is a **dial**, rising about 9-fold with ferredoxin metabolism;
  - lactic bacteria, which live almost without iron, have neither.
- **CRISPR's memory-retrieval enzyme Cas6 also appeared among the iron-repair hits.** blind_24 is frozen to test the switch/dial idea on 8 fresh genomes.

## Potential leads for future research
- **[blind_24]** Grade IF1–IF3 when the zip arrives.
- **[CRISPR iron]** Count CRISPR arrays (repeat–spacer structure, label-free) and Cas4/Cas6 iron motifs across tiers. Does immune-memory capacity track energy metabolism? Develop on graded genomes first.
- **[Polymerase iron]** Eukaryotic DNA polymerases α, δ and ε and primase carry the CysB 4Fe-4S site. Find a label-free signature in the human and mouse files (development).
- **[Che specificity]** Add the acyl-pocket residues that separate cholinesterases from carboxylesterases; test on human vs mouse.
