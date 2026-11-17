# DCF L3789: the "magnetosome genes" of animals are ordinary protein families (4 of 5). An alga, a fungus and a diatom with no magnetite carry them as strongly as bee, oyster and frog
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3789_magnetite_genes.txt`, frozen before the references were downloaded.
- **Script:** `rounds/dcf_magnetite_L3789.py`.
- **References:** `data/L3789_magnetosome_refs.tsv`, as Gary supplied it.
- **Output:** `rounds/L3789_tool_output.txt`, committed before grading.
- **Grader:** `rounds/dcf_grade_L3789.py`, committed before the output was read.
- **Grading:** `rounds/L3789_grade_output.txt`.

**References** (lengths checked against UniProt's Length column):
- **From the magnetotactic bacterium *Magnetospirillum gryphiswaldense* MSR-1:**
  - MamB, V6F510, 297 aa, the iron transporter;
  - MamE, V6F2B6, 772 aa, the protease;
  - MamK, Q6NE59, 360 aa, the actin-like filament;
  - MamP, Q93DZ0, 270 aa, the magnetochrome.
- **Human ISCA1, Q9BUE6, 129 aa,** the protein proposed as "MagR".

---

## Why magnetite
**Animals may sense magnetic fields in two ways:**
1. **The cryptochrome radical pair,** the light-driven chemistry tested in L3753–L3785.
2. **Magnetite (Fe₃O₄) crystals,** tiny iron-oxide magnets that are ferrimagnetic at body temperature and could pull on a nerve ending.

**Magnetite facts used here:**
- **Structure:** an inverse spinel, with Fe²⁺ and Fe³⁺ sharing octahedral sites and Fe³⁺ on tetrahedral sites.
- **Two transitions:** the Verwey transition near 120–125 K and the Curie point near 580 °C. Below the Curie point it stays magnetic.
- **A stable natural compass:** a single magnetic domain holds only within a crystal-size window of tens of nanometres. The 30–60 nm particles reported in salmon olfactory cells (Bellinger et al. 2022) fall in that window.

**Three claims bear on sequence data:**
- **Bellinger et al., PNAS 2022:** reported 11 "universal magnetosome gene homologs" in eukaryotes, including MamA, MamB, MamE and MamK. They said MamP is absent. They also noted that the homology is "distant" and that their enrichment test was not significant (P = 0.0675).
- **Qin et al., Nature Materials 2016:** proposed MagR (ISCA1) bound to cryptochrome as a magnetic compass. Friis et al., Sci. Rep. 2017, found the iron-sulfur clusters 30–50 Å from the cryptochrome's tryptophans. That distance is too far for useful electron transfer.
- **Nemoto et al., Science 2025:** RTMP1 directs iron-oxide (magnetite) deposition in chiton teeth. It is the first known iron-oxide-forming protein in a eukaryote.

**L3789 tests the first claim's logic:** if organisms with no magnetite carry the same homologs just as strongly, the homologs cannot mark magnetite making.

## Results
| # | prediction | result |
|---|---|---|
| G1 | MamB, MamE, MamK each hit in all 3 non-animals | **PASS** |
| G2 | MamB, MamE, MamK each hit in all 3 animals | **PASS** |
| G3 | MamP hits nothing in any of the 6 | **FAIL:** 6–80 weak hits in each |
| G4 | ISCA1 (MagR) hits in all 6 | **PASS** |
| G5 | each animal's best MamB hit is a zinc/cation transporter | **PASS:** ZnT2 (bee, oyster), SLC30A4 (frog) |

**4 of 5 passed.**

## Best hit per reference (score, and the calibrated floor in brackets)
| reference | bee | oyster | frog | alga | fungus | diatom |
|---|---|---|---|---|---|---|
| **MamB** (iron transporter) | 114 [63] ZnT2 | 133 [54] ZnT2 | 137 [55] SLC30A4 | 143 [56] unnamed | 139 [62] mito metal transporter | **201** [55] cation efflux |
| **MamE** (protease) | 235 [68] HTRA2 | 239 [52] PDZ | 283 [65] HTRA1 | **303** [100] PDZ | 100 [67] nma111 (HtrA) | 290 [60] PDZ |
| **MamK** (actin-like) | 96 [55] Arp1 | 110 [50] actin | 120 [58] Arp T2 | 103 [59] actin | 100 [53] actin | 91 [52] HSP70 |
| **MamP** (magnetochrome) | 68 [54] | 65 [54] | 66 [63] | 83 [59] | 73 [54] | 66 [55] |
| **ISCA1** (MagR) | 485 [53] | 470 [42] | **594** [45] | 210 [53] | 81 [46] | 279 [49] |

**Reading:**
- **The strongest MamB and MamE matches are in the diatom and the alga,** which have no reported magnetite. The "magnetosome homologs" are:
  - zinc/cation transporters (CDF, SLC30) for MamB;
  - HtrA/PDZ serine proteases for MamE;
  - actin and its relatives for MamK.
  
  Every cell has these. **Homology to them cannot show that an animal makes magnetite.**
- **ISCA1/MagR is a housekeeping iron-sulfur protein found everywhere.** It is strongest in animals, weak in the fungus (81).
- **The G3 failure is a floor problem, not a MamP signal.** Every MamP "hit" scores 65–83, barely above its floor, and the best partners are unrelated proteins (RAD23, a glucanase, a vomeronasal receptor, an MFS transporter). This fits MamP being absent, but the pre-registered rule called them hits, so G3 fails and stands.

## Method lesson (proposed rule 17)
**The floor here was the maximum over 300 shuffled proteins.** That is too lenient for proteomes of 10,000–58,000 proteins: it let hundreds of noise hits through (908 for MamE in the oyster). **Future floors should scale with proteome size:**
- shuffle as many proteins as are scored (or fit an extreme-value tail and use an E-value);
- or require the best hit to exceed the floor by a pre-set margin.

## Record
**+4 passed, 1 failed. 538 of 743 passed, plus 3 split.** Audit **205 of 270** (entry "magnetosome genes specificity").

## Summary
- **The bacterial magnetite genes MamB, MamE and MamK match zinc transporters, HtrA proteases and actin** in honeybee, oyster and frog. They match just as strongly in an alga, a fungus and a diatom that make no magnetite. **These "homologs" are not magnetite markers.**
- **MagR (ISCA1) is present in all six,** consistent with a housekeeping role.
- **MamP, the magnetite-specific heme protein, has no real match anywhere.** It still failed its prediction because the noise floor was too lenient.
- **For magnetite in animals, the genuine molecular lead is the chiton tooth protein RTMP1** (Science 2025), not the bacterial genes.

## Potential leads for future research
- **[RTMP1, magnetite-specific]** Pre-register: RTMP1 (chiton) has no confident homolog in oyster, bee or frog. It is "conserved across chitons" and may be chiton-specific. Needs the RTMP1 sequence from UniProt/NCBI.
- **[Rule 17]** Add a size-scaled noise floor (E-value or a match-count of shuffles) to the standing methods rules, and re-run G3 under it as a descriptive check.
- **[Cryptochrome × iron]** Cryptochrome (radical pair) and magnetite are rival compass models. A testable cross-link is whether magnetite-reporting animals (bee, salmon, pigeon) share any cryptochrome tetrad feature that non-reporting animals lack.
- **[Phone]** Add MamB/E/K/P and ISCA1 to the phone's reference set, with the size-scaled floor.
