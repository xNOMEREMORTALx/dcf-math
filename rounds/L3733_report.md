# DCF L3733: "Higher dimensions" that genuinely touch DNA and RNA; selenium and zinc read from sequence (3 of 5); the genetic code as a 6-dimensional cube, computed
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Gary's request:** "Pursue leads, and any information you can find that links our work to other higher dimensions that we can integrate with our DNA and RNA work; also any other metals or elements."

---

## Part A. Higher dimensions: what is established, and what is not
**Extra spatial dimensions** (string theory, branes) have **no established link** to DNA or RNA biology. I found nothing reliable to integrate there and will not invent a connection.

**Higher-dimensional mathematics is used legitimately in DNA/RNA work, in four ways:**

| idea | what it is | link to our work |
|---|---|---|
| **4D Nucleome** | 3D genome folding plus **time** | L3701–L3729: the loop files verified; nerve-metal genes at CTCF (zinc) anchors |
| **The genetic code as a 6-dimensional cube** | the 64 codons as corners of a 6-D binary hypercube; neighbours differ by one "bit" of base chemistry; Gray-code order (Jiménez-Montaño et al., *BioSystems* 39:117–125, 1996) | computed below (Part C) |
| **Hyperdimensional computing** | DNA sequences encoded as vectors in thousands of dimensions, for fast, error-tolerant search (e.g. BioHD) | a natural method for Gary's **DNA data storage** and the phone's DNA codec (lead below) |
| **High-dimensional sequence space** | each protein of length L is a point in a 20ᴸ-dimensional space; evolution moves through it | our aligners measure distances in that space (Manuscript 2) |

## Part B. Two more elements, read from sequence (`PREREGISTERED_L3733_se_zn.txt`)
**Selenium:** selenocysteine, the 21st amino acid, is encoded by **UGA**, normally a stop codon. It is a true recoding of the RNA message. UniProt writes it as "U".

**Zinc:** proteins with ≥ 3 C2H2 zinc fingers, the family of CTCF.

| # | prediction | result |
|---|---|---|
| S1 | worm ≤ 2 selenoproteins | **PASS** (2) |
| S2 | 8 aquatic animals each ≥ 10 | **FAIL:** acorn worm 24, brachiopod 14, lancelet 13; sea hare 6; sea anemone, sponge, sea urchin and *Capitella* 0 |
| S3 | water flea > mite | **FAIL:** both 0 |
| Z1 | mouse has the highest zinc-finger share | **PASS:** 3.02%, just above the lancelet (2.90%) |
| Z2 | mouse > 2 × fly | **PASS:** 643 vs 232 |

**3 of 5 passed.**

**Reading:**
- **Selenium:** "U" appears only where the gene-prediction pipeline encodes selenocysteine. Many pipelines stop the protein at UGA.
  - The organisms showing selenoproteins (acorn worm, brachiopod, lancelet, Hydra, sea hare, horseshoe crab, priapulid, starfish) mostly have RefSeq-based annotations.
  - **A zero means "not annotated", not "no selenium".** This is the same lesson as the cohesin control (L3713).
  - **The failures stand; the biology is not tested by these files.**
- **Zinc:** zinc-finger proteins are 3% of the mouse and lancelet proteomes, 2.9% of zebrafish, and under 0.3% of sponges and single-celled relatives.
  - **The zinc "language" of gene regulation expanded with the bilaterians and again in chordates,** echoing CTCF (L3701).

## Part C. The genetic code as a 6-dimensional cube (`rounds/L3733_code_geometry.txt`)
**Computed for the standard code:**
- **64 codons = 2⁶:** 61 sense codons, 3 stops, 20 amino acids.
- **Every codon has exactly 9 single-letter neighbours** (3 positions × 3 alternatives). The mutation graph has **288 = 4 × 72 edges.**

| mutation-edge class | count |
|---|---|
| synonymous (same amino acid) | **67** |
| missense (amino acid changes) | **196 = 14²** |
| to or from a stop | 23 |
| stop to stop | 2 |

- **The third letter is the code's "silent" axis:** 63 of the 67 synonymous edges change position 3. Position 1 gives 4, and position 2 gives 0.
- **As a 6-cube** (one illustrative 2-bit base code: C = 00, T = 01, G = 10, A = 11), there are 192 edges, 6 per codon, of which 48 are synonymous.

**Status:** exact arithmetic. The tidy values (9 neighbours, 4 × 72, 14²) were noticed after computing, so they are **facts, not evidence** of anything beyond the code's structure.

## Elements now covered in this series
| element | biological role read from sequence | where |
|---|---|---|
| Na, K, Ca | channels and pumps (selectivity loops) | Manuscript 2 |
| Cu | P-type copper pumps | Manuscript 2 |
| Fe | aromatic hydroxylases (dopamine, serotonin) | Manuscript 2 |
| Zn | CTCF and zinc-finger proteins; genome loops | L3701–L3733 |
| Se | selenocysteine (UGA recoding) | L3733 (annotation-limited) |

## Record
**+3 passed, 2 failed. 509 of 696 passed, plus 3 split.** Audit **176 of 223.**

## Summary
- **No reliable link exists between extra spatial dimensions and DNA.** Four legitimate higher-dimensional ideas do touch our work:
  - the 4D Nucleome (time);
  - the genetic code as a 6-dimensional cube;
  - hyperdimensional DNA encoding;
  - sequence space.
- **Zinc and selenium, from sequence:**
  - zinc-finger proteins expanded with bilaterians and chordates (3 of 5 predictions passed);
  - selenoprotein counts mostly reflect annotation pipelines, not biology.
- **The genetic code's geometry, computed:**
  - 9 neighbours per codon;
  - 288 mutation edges, of which 67 synonymous, 196 missense, 23 stop-linked and 2 stop-to-stop;
  - the third letter is the silent axis.

## Potential leads for future research
- **[Hyperdimensional DNA codec]** Add a hyperdimensional encoder to the phone's DNA tools (dcf_dna_codec): random ±1 vectors for A/C/G/T, binding by rotation, bundling by sum. Then measure error tolerance against the current codec. This is a concrete, testable integration with DNA data storage.
- **[Selenium properly]** Retest the selenoproteome with RefSeq protein files (which encode U) for a few organisms that showed 0 (sea urchin, sea anemone).
- **[Molybdenum]** The Mo-cofactor enzymes (sulfite oxidase, xanthine dehydrogenase, aldehyde oxidase, mARC) and their synthesis genes (MOCS1–3, gephyrin). Gephyrin also anchors inhibitory synapses, a molybdenum–nerve link. Testable across our proteomes with the mouse references.
- **[Cobalt]** Vitamin B12 enzymes (methylmalonyl-CoA mutase, methionine synthase): which animals kept them?
- **[Code geometry and mutation]** Compare which of the 196 missense edges change an amino acid's metal-binding residue (C, H, D, E), the "metal-sensitivity" of the code.
