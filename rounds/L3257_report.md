# DCF L3257: a "redox-age" reading from raw DNA — the iron ladder plus a copper (CuA) marker sorts 18 of 23 held-out genomes (needed 19; 2 of 3 pass) and reveals a four-step scale; NCBI blocks automated mRNA access, so the mRNA set comes by browser
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [Fe-Cu 3] (copper counter), turned into a new **[Redox-age]** lead; [IRE-wide] access.

**Pre-registration:** `PREREGISTERED_L3257_redoxage.txt` (`c71de4c9…711d`). It freezes `rounds/dcf_redoxage_L3257.py` (`f2d17142…0417`) and was pushed before the held-out run.

---

## 1. Access to the human mRNA set
Gary approved the request, but both routes are refused **by NCBI's own robots rules**: the FTP folder and the E-utilities search both return `robots_disallowed`. That is a site restriction, not a permission one, so it is respected and not routed around.

**The mRNA set has to come through Gary's browser** (see "Action for Gary").

## 2. A copper marker [development, 12 seen genomes]
**Method.** Each motif was scored against the annotated products of 12 seen genomes (8 aerobes, 3 ferredoxin-based anaerobes, 1 lactic fermenter).

| motif | hits | hits on copper proteins | verdict |
|---|---|---|---|
| **CuA: C-x-E-x-C-x₃-H-x₂-M** (cytochrome oxidase II, N₂O reductase) | 10 | **10 (100%)** | **kept**: present in 7 of 8 aerobes, 0 of 4 others |
| type-1 blue copper C-x₂₋₄-H-x₃₋₄-M | 472 | 31 (7%) | too loose |
| CuB region HPEV[YF] | 26 | 9 (35%) | also in a methanogen |
| HxH…HxH (multicopper oxidase) | 100 | 5 (5%) | too loose |
| HMA GM[TS]CxxC | 20 | 0 counted* | binds several metals |

\* NCBI names these "heavy-metal-translocating ATPases", not copper proteins, so their copper role cannot be scored this way.

## 3. The redox-age call [pre-registered, 23 held-out genomes]
**Rule** (cut 0.06 set on the development genomes only):
- 3-3-4 iron ladder ≥ 0.06 per 1,000 aa → **Fd** (ferredoxin-based, oxygen-free core);
- otherwise, CuA present → **O2** (oxygen respiration);
- otherwise → **neither** (fermenter).

| label | genomes | correct |
|---|---|---|
| Fd | 13 | **9** (missed: *Ruminococcus* 0.021, *Caldanaerobacter* 0.038, *Parabacteroides* 0.038 (pre-declared), *Caldicellulosiruptor* 0.058) |
| O2 | 4 | **3** (*B. licheniformis*, *Chloroflexus*, *Haloarcula*; missed *Arcobacter*, no CuA, pre-declared) |
| lactic fermenters | 6 | **6** (ladder 0–0.002, no CuA) |

| id | prediction | result | verdict |
|---|---|---|---|
| RA1 | ≥ 19 of 23 correct (majority baseline 13) | **18 of 23** | **FAIL** (by one) |
| RA2 | ≥ 3 of 4 O2 genomes called O2 | 3 of 4 | **PASS** |
| RA3 | ≥ 5 of 6 lactic fermenters called "neither" | **6 of 6** | **PASS** |

**What the misses show [D, after the fact].** The ladder is not a switch but a **scale**. Across all 35 genomes the readings fall in four tiers:

| tier | ladder per 1,000 aa | who |
|---|---|---|
| 1 | 0–0.002 | lactic fermenters (no ferredoxin step) |
| 2 | 0.007–0.025 | oxygen respirers |
| 3 | 0.021–0.058 | H2-making fermenters and *Parabacteroides* (ferredoxin used for H2 or pyruvate) |
| 4 | 0.063–0.132 | ferredoxin-based respirers and autotrophs (sulfate reducers, acetogens, methanogens, rTCA bacteria, organohalide respirers) |

*Arcobacter* (0.046) sits with tier 3; Campylobacterota run on ferredoxin enzymes even when microaerophilic (L3221).

**CuA, a bonus [D].** It appeared in *Hydrogenobacter* (4; an aerobe that also uses rTCA) and *Desulfomicrobium* (1; plausibly N₂O reductase). The ladder rule took precedence, as frozen.

**Why this may be new.** Andreini *et al.* (2017) counted Fe–S proteins with profile models. A two-motif, label-free call (one iron, one copper) that sorts raw genomes into ferredoxin, oxygen and fermentative metabolism was not found in this round's or earlier literature checks. A dedicated search is needed before any claim ([Lit-redox]).

## Record
**This round:** 3 graded, 2 passed.

**Total: 289 of 406 pre-registered predictions passed, plus 3 split.**

## Summary
- **From raw DNA, two small motifs read a microbe's metabolic "age":** the iron–sulfur ladder of the oxygen-free world and the copper site of oxygen respiration.
- **Tested on 23 genomes held out from its design,** it got 18 right (one short of the frozen bar). It caught every lactic fermenter and 3 of 4 oxygen breathers.
- **Its misses were hydrogen-making fermenters** that read just under the cut. Together these show the iron ladder is a four-step scale, from lactic fermenters through oxygen breathers and hydrogen fermenters up to the sulfate reducers, acetogens and methanogens of the oldest metabolisms.
- **The human mRNA set must come by browser,** because NCBI blocks automated access.

## Potential leads for future research
- **[Redox-age b]** Pre-register a four-tier version (cuts from the 35 genomes now seen) and test it on a fresh blind set of 12–16 genomes with all four tiers represented.
- **[Lit-redox]** Literature check: label-free Fe–S/Cu motif classifiers of microbial metabolism.
- **[Cu-cbb3]** Add a cbb3-oxidase marker so microaerophiles like *Arcobacter* get an O2 call; develop on seen genomes.
- **[IRE-wide + Metal-mRNA]** Grade W1–W3 when the human mRNA file arrives.
- **[Fe-ladder note]** Rewrite Note H around the ladder scale (6 of 6 lineage pairs; the four tiers).

## Action for Gary: the human mRNA file (by browser)
**Option A (preferred).** Open this folder in your browser and tap **`human.1.rna.fna.gz`** (or `human.1.rna.gbff.gz`):

https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/

**Option B.** Open this NCBI search, then choose **Send to → File → Format: FASTA → Create file**:

https://www.ncbi.nlm.nih.gov/nuccore/?term=Homo+sapiens%5Borgn%5D+AND+refseq+select%5Bfilter%5D+AND+biomol_mrna%5Bprop%5D

That is about one mRNA per human gene. The file may be tens of MB.

Send the file as it comes; the frozen script reads FASTA or GenBank, compressed or not.
