# DCF L3653: The NALCN "leak channel" ring across the tree (4 of 5). Spiralians and sea urchins carry the domain-II lysine (E-K-E-E); arthropods, tardigrades and vertebrates carry the domain-III lysine (E-E-K-E); the lancelet reads E-E-E-E
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Lead:** [NALCN lysine exon] (from L3649).

**Background:** published work explains the rotifer's two NALCN loop versions.
- **Senatore et al. 2013** (*PLoS ONE*; [PMC3557258](https://pmc.ncbi.nlm.nih.gov/articles/PMC3557258)) found that a single NALCN gene uses mutually exclusive exons to switch its ion-selecting ring:
  - **domain II:** EEEE or EKEE, in flatworms, molluscs, annelids, echinoderms and hemichordates;
  - **domain III:** EEEE or EEKE, in chelicerates and myriapods.
- **Chordates, insects and nematodes lack the alternative pairs.** Vertebrates carry EEKE.
- **The rotifer's T-N-E-G-W / T-Q-K-G-W pair (L3649) is the domain-II EEEE/EKEE switch,** in a group the paper did not sample.

**Files:**
- **Pre-registration:** `PREREGISTERED_L3653_nalcn_ring.txt`, frozen from the paper's claims before any ring was read outside the rotifer.
- **Script:** `rounds/dcf_nalcn_ring_L3653.py`.
- **Tool output:** `rounds/L3653_tool_output.txt`, committed before grading.

**Method:**
1. **Find NALCN:** 4-domain proteins whose nearest mouse channel (local aligner) is Nalcn, with the standing **score floor of 1,000**.
2. **Read the ring:** each of the four ring residues is located by an ungapped BLOSUM62 window around the mouse ring word.
3. **Control:** mouse Nalcn reads **E-E-K-E**, as expected.

---

## Results
| # | prediction | result |
|---|---|---|
| Q1 | chordates: every NALCN entry E-E-K-E | **FAIL:** zebrafish and chicken E-E-K-E, but the **lancelet reads E-E-E-E** (human and Ciona sets: no NALCN found) |
| Q2 | spiralians + ambulacrarians: no domain-III K | **PASS:** 15 entries, all E-K-E-E or E-E-E-E |
| Q3 | E-K-E-E in ≥ 3 of them | **PASS:** 8 organisms |
| Q4 | chelicerates: no domain-II K | **PASS** (mite E-E-K-E; no horseshoe-crab entry passed the filter) |
| Q5 | fly and worm: E-E-K-E | **PASS** on the fly. The worm set (4,487 proteins) is below the frozen 5,000 size rule, so it was not scanned. |

**4 of 5 passed.**

## The ring map (all entries found)
| lineage | organisms | ring (DI-DII-DIII-DIV) |
|---|---|---|
| **spiralians** | sea hare, annelid *Capitella*, brachiopod, *Dimorphilus*, 3 rotifers | **E-K-E-E** (rotifer *B. calyciflorus* also E-E-E-E) |
| | leech | E-E-E-E (the other exon) |
| **ambulacrarians** | sea urchin (4 entries) | **E-K-E-E** |
| **ecdysozoans** | fly, spider mite, **both tardigrades** | **E-E-K-E** |
| **chordates** | zebrafish, chicken, mouse | **E-E-K-E** |
| | **lancelet** | **E-E-E-E** |
| **acoel** | *Hofstenia* | E-E-E-E and E-E-K-E |
| **cnidarians, sponge** (descriptive) | Hydra, sea anemone, *Amphimedon* | E-E-E-E (sea anemone also E-D-E-E) |

## Reading
- **Where the lysine sits splits the bilaterians cleanly:**
  - **domain II (E-K-E-E)** in spiralians and the sea urchin, as the paper reported for molluscs, annelids and echinoderms;
  - **domain III (E-E-K-E)** in ecdysozoans (fly, mite, tardigrades) and vertebrates.
- **The tardigrades (new, not in the paper) side with the arthropods.**
- **Rotifers (new) side with the other spiralians,** with both exon forms present in *B. calyciflorus*.
- **The non-bilaterian hits all read E-E-E-E,** the calcium-like form.
  - **Caution:** the Hydra entries are named "Calcium-channel protein CCH1". My reference set has no CCH1-family channel, so these may be NALCN's sister family rather than NALCN itself.
  - If they are NALCN, **the calcium-like E-E-E-E ring is the ancestral form.** The sodium-like lysine was added later, at two different positions in two bilaterian branches.
- **The lancelet failure:**
  - Its only entry reads **E-E-E-E** where vertebrates read E-E-K-E (domain III S-L-**E**-G-W vs mouse S-L-**K**-G-W).
  - **Two explanations:**
    - the lancelet keeps a domain-III EEEE/EEKE exon pair like arthropods, and UniProt lists the EEEE exon;
    - or the lancelet never added the lysine.
  - **Either way, "chordates are E-E-K-E only" does not hold** for this invertebrate chordate in UniProt.

**Connection to the battery:**
- **NALCN sets the resting "leak"** that drives pacemaking and rhythm.
- **An E-E-E-E ring passes calcium-like current; a lysine ring passes sodium-like current.**
- **So one gene, by splicing, can switch the resting leak between two metals.** That is another metal-choice switch, like DEKA vs EEEE in the spike channels.

## Record
**+4 passed, 1 failed. 472 of 638 passed, plus 3 split.** Nerve-chemistry audit **139 of 165.**

## Summary
- **The rotifer's alternative NALCN loops match a published splicing switch** (Senatore et al. 2013).
- **Tested across 31 proteomes, 4 of 5 predictions from that paper held:**
  - spiralians and the sea urchin carry the lysine in domain II;
  - arthropods, tardigrades and vertebrates carry it in domain III.
- **New observations:**
  - tardigrades follow arthropods;
  - rotifers follow spiralians;
  - cnidarian and sponge hits read the calcium-like E-E-E-E.
- **The lancelet reads E-E-E-E,** against the "chordates E-E-K-E" prediction.

## Potential leads for future research
- **[Lancelet exon]** Does the lancelet NALCN gene carry a second domain-III exon? This needs the genome (RefSeq gene model) or more UniProt isoforms.
- **[CCH1 vs NALCN]** Add a fungal CCH1 reference (e.g. yeast Cch1) to the reference set. Then test whether the cnidarian and sponge E-E-E-E hits are NALCN or CCH1.
- **[Worm NALCN]** Rerun on a full *C. elegans* proteome (nca-1, nca-2) to grade the nematode half of Q5.
- **[Manuscript 2]** §3.19 NALCN rings and a ring-map figure.
