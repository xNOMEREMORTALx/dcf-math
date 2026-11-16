# DCF L3701: Flukes vs tapeworms (3 of 5); the "4D DNA" report checked; and zinc in the fourth dimension: CTCF, the zinc-finger loop architect, appears with the bilaterians (6 of 8)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Gary's request:** "Pursue leads and the harmonics, four metals, in relation to the 4th dimension", with two attachments: a zip of flatworm proteomes and `4D_DNA.txt`.

---

## Part A. Flukes vs tapeworms (`PREREGISTERED_L3697_trematode_cestode.txt`)
**Data:** the zip held **four** files, not five. *Opisthorchis* was missing, so **G2 is void** (dropped, not replaced). The other four matched their proteomes exactly.

| # | organism | NAV-family | NR1 (floor 941) | prediction | result |
|---|---|---|---|---|---|
| G1 | *Clonorchis* (fluke) | 0 | 1 | 0 NAV | **PASS** |
| G2 | *Opisthorchis* (fluke) | — | — | — | **void** |
| G3 | *Paragonimus* (fluke) | 0 | 0 | 0 NAV | **PASS** |
| G4 | *Taenia* (tapeworm) | **1** | 0 | ≥ 1 NAV | **PASS** |
| G5 | *Hymenolepis* (tapeworm) | **0** | 0 | ≥ 1 NAV | **FAIL** |
| G6 | NR1 in ≥ 3 of 5 | | 1 of 4 | | **FAIL** |

**3 of 5 passed.**

**Reading:** across this round and L3689, the sodium channel's presence by flatworm group is:

| group | organisms | NAV-family channel |
|---|---|---|
| **flukes** | 5 tested | **none** (0 of 5) |
| **tapeworms** | *Echinococcus*, *Taenia* | yes |
| | *Hymenolepis* | no |
| **free-living** | *Macrostomum* | yes (8) |

- **The fluke loss is consistent.** Tapeworms vary; *Hymenolepis* has lost it too.
- **NR1, even with the calibrated floor, is found in only 1 of these 4 flatworms.** Flatworm NR1s are scarce or very divergent.

## Part B. The "4D DNA" report (`4D_DNA.txt`): checked under the standing rule
**What the file is:** a long research report on the 4D Nucleome Project, with an add-on "original data audit" and code.

**Treated as untrusted, per the rule: "any new numerical claim from any source … gets run through a check before it touches a manuscript draft."**

| claim | check | status |
|---|---|---|
| Paper: "An integrated view of the structure and function of the human 4D nucleome", *Nature*, Dec 2025 / Jan 2026 | 4DN Data Portal record: *Nature*, published 17 Dec 2025, PMID 41407856 | **verified** |
| "> 140,000 loops per cell type", H1 and HFFc6 | portal abstract: "more than 140,000 looping interactions per cell type"; H1 and HFFc6 | **verified** |
| exact counts **141,365** (H1) and **146,140** (HFFc6) | not in the abstract; the full text was blocked (PMC browser check) | **not yet verified** |
| Zenodo record 17451616 with MD5 `6b186943…` (H1) and `1faf1181…` (HFFc6) | Zenodo page lists both files with exactly these MD5s | **verified** |
| all other figures (14,321 / 12,804 genes, 173 kb, 80.3%, 1,000 structures at 200 kb, the "audit" fractions, trajectory statistics) | not checked | **untrusted** |

**What "4D" means here:** the fourth dimension in the 4D Nucleome is **time**: 3D genome folding followed through the cell cycle and development. It is not a fourth spatial dimension.

**To verify the exact loop counts myself,** I need the two BEDPE files (19 MB). My shell cannot reach Zenodo.

## Part C. Zinc and the 4th dimension: CTCF across the tree (`PREREGISTERED_L3701_ctcf_tree.txt`)
**Bridge from the report to our metal work:**
- **The loops** in the 4D Nucleome are anchored by **CTCF**, a protein with **11 zinc fingers**, held with **cohesin**.
- **Zinc is therefore the metal of 3D/4D genome architecture,** alongside our nerve metals: Na, K and Ca for signalling, Cu and Fe in enzymes.

**Finder** (`rounds/dcf_ctcf_L3701.py`, reciprocal best hit):
1. Among proteins with ≥ 9 zinc fingers, take the top match to mouse CTCF.
2. Align that protein to all 365 mouse multi-zinc-finger proteins; its nearest must be CTCF or CTCFL.

**Development:** zebrafish, chicken and fly were called; the worm was not (4 of 4 correct).

| # | prediction | result |
|---|---|---|
| Z1 | sponges: no CTCF | **PASS** (graded on *Amphimedon*; see disclosure) |
| Z2 | placozoans: none | **PASS** |
| Z3 | cnidarians: none | **PASS** |
| Z4 | comb jelly: none | **PASS** |
| Z5 | non-animals: none | **PASS** |
| Z6 | ≥ 80% of other bilaterians have CTCF | **FAIL:** 14 of 29 (48%) |
| Z7 | acoel has CTCF | **PASS** (score 924) |
| Z8 | both tardigrades have CTCF | **FAIL** |

**6 of 8 passed.**

**Disclosure:** the frozen scan script **left out the file holding three sponges** (*Geodia*, *Ephydatia*, *Oopsacas*).
- **Z1 is graded on *Amphimedon* alone.**
- **Run afterwards with the same finder** (descriptive): all three have no CTCF.

**Where CTCF was found** (14): mouse, lancelet, acorn worm, sea urchin, starfish, brachiopod, annelid *Capitella*, *Dimorphilus*, sea hare, horseshoe crab, spider mite, priapulid, water flea, bdelloid rotifer; plus the acoel.

**Where it was not found** (15): Ciona, both tardigrades, the leech, two monogonont rotifers, and all nine flatworms.

**Descriptive, after grading (names):**
- **Ciona has four entries named "CCCTC-binding factor",** and the *Hypsibius* tardigrade has one named "Transcriptional repressor CTCF". They carry only **7–8 detectable zinc fingers**, so the finder's ≥ 9 gate never looked at them.
- **So at least two of the "absences" (Ciona and *Hypsibius*) are finder misses,** not losses. The Z8 failure is mainly a method limit.

**Reading:**
- **Every non-bilaterian tested lacks CTCF:** 4 sponges, 2 placozoans, 3 cnidarians, the comb jelly, and 4 single-celled relatives. All 10 such predictions passed.
- **CTCF appears with the bilaterians,** including the acoel. That fits the published view that CTCF is a bilaterian innovation.
- **Within bilaterians, CTCF is often undetected in fast-evolving lineages** (flatworms, tardigrades, some rotifers, the leech, Ciona). Some are real losses, as in the nematode; some are divergent copies the finder misses.

**The "harmonics" in one line:**
- **The same branch point recurs:** sponges and placozoans lack the bilaterian set, while bilaterians gained fast-signal parts (the lysine sodium channel, NR1 in cnidarians and bilaterians) and the zinc loop-architect.
- **In battery terms:** time-keeping by metals in nerves (Na, K, Ca) and time-keeping of genome folding by a zinc protein became elaborate in the same lineages.
- **This is a pattern, not a mechanism.**

## Record
**+9 passed, 4 failed (G2 void). 495 of 673 passed, plus 3 split.** Audit **162 of 200.**

## Summary
- **Flatworms:** all five flukes tested lack the sodium spike channel; tapeworms vary. 3 of 5, with one prediction void because a file was missing.
- **The 4D Nucleome report:** its paper, its ">140,000 loops per cell type" and its file checksums check out. The exact loop counts and its other numbers are not yet verified.
- **The "fourth dimension" there is time.** The real metal link is **zinc**, through CTCF, the 11-zinc-finger protein that anchors genome loops.
- **CTCF across 40 proteomes:** absent from every non-bilaterian and present in many bilaterians. 6 of 8 predictions passed.
- **Two of the misses** (Ciona, a tardigrade) are named CTCF proteins my finder's zinc-finger gate excluded.

## Potential leads for future research
- **[Verify 4DN counts]** Download the two union-loop BEDPE files from https://zenodo.org/records/17451616 (19 MB). I will check MD5s and count the loops.
- **[CTCF finder v2]** Lower the zinc-finger gate (≥ 6) and keep the reciprocal check. Development on the named Ciona and tardigrade CTCFs, then a blind test.
- **[Cohesin]** The other half of the loop machine (RAD21, SMC1/3). Unlike CTCF, it is expected in every eukaryote. A positive control that 3D folding machinery exists where CTCF is absent.
- **[Zinc in nerves]** Zinc is also released at some synapses and modulates NMDA receptors (a known GluN2A zinc site). Check whether the NR2A zinc-binding residues are conserved in the NR2-like subunits found here.
