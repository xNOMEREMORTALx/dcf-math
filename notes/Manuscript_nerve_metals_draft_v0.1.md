# Reading the metal chemistry of nervous systems from sequence alone: pre-registered blind tests across animals
### Manuscript 2, draft v0.1 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026
*Draft for internal review. Every number below is recomputed by `rounds/L3485_audit2.py` or quoted from a committed grade output.*

## Abstract
Nerve signalling is metal chemistry:
- pumps spend ATP to store Na⁺, K⁺ and Ca²⁺ gradients;
- voltage-gated channels release them as impulses.

Each protein chooses its ion with a short loop:
- the potassium filter T-V-G-Y-G;
- the sodium DEKA ring;
- the calcium EEEE/EEDD ring;
- the P-type pump helix-4 loop.

We wrote transparent, label-free rules that read these loops from protein or mRNA sequence. We tested them in **seven pre-registered blind tests**. Each rule was hashed before testing, and each tool output was committed before any label was read.

**Results:**
- **Overall:** **67 of 81** gradeable predictions passed.
- **Against an independent reference** (UniProt's curated protein families, 58,949 reviewed animal proteins from all species not used in development):
  - 13 of 14 predictions passed;
  - 345 of 351 class calls agreed with UniProt;
  - none of 919 nematode proteins was called a sodium channel (nematodes lack them).
- **Failures were concentrated in one place:** the fruit fly (5 of 13), where finer motifs tuned on vertebrates broke. These were the NMDA gate, the flanks of the iron-hydroxylase site, the K2P limits, and a length cut.
- **The core loops held in every lineage tested.**

## 1. Introduction
- Ion selectivity is set by short, structurally defined loops.
- **The gap:** annotation of new genomes relies on names and homology transfer. A rule set that is readable, small and testable is useful for poorly annotated genomes, and lets one ask how far the chemical "words" are conserved.
- **We frame the nervous system as a battery:**
  - **chargers** (P-type pumps, sorted here by metal);
  - **dischargers** (channels).

## 2. Methods
### 2.1 Sequences
- **mRNA:** RefSeq; longest ATG ORF per gene.
- **Protein:** UniProt TSV; only Entry and Sequence are read by the tool.

### 2.2 Rules (final frozen versions)
**Channels:**
1. **Gate:** a channel needs a voltage sensor S4 (five R/K at spacing 3), or the weak-sensor route: a K filter (T/S-V/I-G-Y-G-D, S-V-G-F-G-N or C-I-G-Y-G) plus four charges.
2. **4-domain branch:** ≥ 1,500 aa with S4 and either a calcium ring or the sodium lysine.
   - the sodium lysine loop [TS]-[FY]-[KR]-[GA]-W → **Na**;
   - otherwise ≥ 3 calcium-ring matches [TS]-x-[ED]-x-W → **Ca**.
3. **1-domain branch:**
   - C-I-G-Y-G → **HCN**;
   - [TSC]-[VITL]-G-[YF]-G → **K**.

**Other finders:**
- **K2P:** < 1,100 aa, no S4, two filters [TS]-[TSV]-[IVT]-G-[YFL]-G.
- **iGluR:** Y-T-A-N-L-A-A.
- **Iron hydroxylase core:** [CVI]-H-E-[LI]-[LM]-G-H (two of the three iron ligands, H-x₄-H).
- **Pumps:** signature D-K-T-G-T-[LIVM]-[TI], then:
  - [NY]-V-P-E-G-L → Na⁺/K⁺;
  - [AS]-[IV]-P-E-G-L → Ca²⁺;
  - C-P-C + 2 × G-M-x-C-x-x-C → Cu.

### 2.3 Protocol
- **Before each test:** a pre-registration and the script are hashed into a public ledger.
- **Data:** files are identified by headers. A missing file is dropped, not replaced.
- **Grading:** tool output is pushed before names are read.
- **Amendments:** only before data. Failed predictions are never regraded.

### 2.4 Truth
- **v1–v3:** names and descriptions, written by us. **Their limits are part of the results.**
- **v4:** UniProt "Protein families", which is independent of us.

## 3. Results
| test | data | truth | passed |
|---|---|---|---|
| mouse | RefSeq mRNA file 3 | names | **10/10** |
| zebrafish | RefSeq curated / predicted | names | **10/11**, **7/10** |
| chicken | RefSeq annotation RNA | names + descriptions | **13/14** |
| fruit fly | RefSeq annotation RNA | names + descriptions | **5/13** |
| nematode | Swiss-Prot reviewed *C. elegans* | UniProt families | **9/9** |
| all other animals | Swiss-Prot reviewed Metazoa (58,949) | UniProt families | **13/14** |
| **total** | | | **67/81** |

- **3.1 The core loops.** The rules recover the textbook rings: EEEE in L-type, EEDD in T-type, DEKA in sodium. Duplicated fish genes kept their metal in both copies.
- **3.2 Failures by cause.** Of the 14 failures:
  - **6 were truth-rule limits** (real channels, receptors or pumps not credited by the name rules);
  - **8 were real rule errors:**
    - **fly:** the NMDA motif (×2), the iron flank, the K2P rule (×2) and the length cut, which misfiled Shab;
    - **zebrafish:** a chance NMDA match;
    - **all animals:** a calcium-like repeat in the Scn4a outer loop.
  
  Each real error led to a frozen fix, tested on the next blind set.
- **3.3 Negative controls.**
  - **Nematodes:** zero sodium calls in 4,489 *C. elegans* proteins and in 919 other nematode proteins.
  - **Vertebrates:** no sodium↔calcium swaps among vertebrate Na/Ca channels, apart from the Scn4a case.
- **3.4 Battery balance (descriptive).** Metal pumps are few and conserved, while channels (mainly K⁺) multiply in vertebrates: 4–6 channels per pump, against 3.5 in the fly.

## 4. Discussion
- **What carries across ~600 million years:** the selectivity loops themselves.
- **What does not:** flanking residues and family-specific limits.
- **Limitations:**
  - silent subunits, sodium sensors (Naₓ), divergent K2P and insect IR receptors are missed;
  - our own name-based truth rules undercounted correct calls;
  - sequence cannot address higher-level questions such as consciousness, although the parts list of excitability (pacemakers, T-type calcium, leak channels targeted by anaesthetics) is now readable.

## 5. Data and code availability
- **dcf-math:** pre-registrations, ledger, rounds, grade outputs, and `rounds/L3485_audit2.py`.
- **dcf-genefinder:** `dcf_nerve.py`, `dcf_pump.py`.
- **Phone:** menu 34.
- **Before submission:** Zenodo DOIs.

## Summary
- **A first full draft of Manuscript 2.** Its central claim, recomputed from committed outputs: the metal-selecting loops of nervous systems can be read from sequence across animals, 67 of 81 blind predictions overall and 13 of 14 against UniProt's independent classification.

## Potential leads for future research
- **[V-test]** Add the lysine-first Na/Ca test (L3485) as §3.5.
- **[Figures]** Fig. 1, motif panel; Fig. 2, per-test bars; Fig. 3, battery balance.
- **[Outside reader]** As with Manuscript 1.
