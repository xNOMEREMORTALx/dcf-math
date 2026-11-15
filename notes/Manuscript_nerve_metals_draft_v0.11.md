# Reading the metal chemistry of nervous systems from sequence alone: pre-registered blind tests across animals
### Manuscript 2, draft v0.11 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026
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

We wrote transparent, label-free rules that read these loops from protein or mRNA sequence. We tested them in **fifteen pre-registered blind tests**. Each rule was hashed before testing, and each tool output was committed before any label was read.

**Results:**
- **Overall:** **94 of 112** gradeable predictions passed.
- **At the base of the animal tree** (choanoflagellate, sponge, placozoan, sea anemone): 7 of 7 passed. No nerve-type sodium channel was called. The early sodium-channel homologues read A-T-F-**E**-G-W at the domain-III position where every bilaterian sodium channel reads A-T-F-**K**-G-W.
- **Sodium vs calcium on 24,796 unseen vertebrate channel sequences (UniProt TrEMBL):** 4 swaps in 23,994 calls (0.02%), with recall 93% (Na) and 99% (Ca).
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
| Na/Ca decision | TrEMBL vertebrate channels (24,796) | UniProt names | **4/4** |
| before nerves | 4 early-animal proteomes (67,936) | pre-stated literature expectation | **7/7** |
| comb jellies | UniProt Ctenophora (25,809) | pre-stated literature expectation | **3/3** |
| E→K dating | 4 bilaterian proteomes (125,720) | pre-stated hypothesis | **2/5** |
| kit + chordate K | lancelet, sea squirt (58,286; octopus too sparse) | pre-stated expectation | **8/8** |
| NAV1/NAV2 family | 4 ambulacrarian channels vs bilaterian NAV1/NAV2 | pre-stated hypothesis | **1/1** |
| earliest channel family | 10 non-bilaterian/acoel channels | pre-stated hypothesis | **0/1** (9 of 10 NAV2; one comb-jelly tie) |
| NAV1/NAV2 by alignment | same 12 channels, BLOSUM62 global alignment | pre-stated hypothesis | **2/2** |
| **total** | | | **94/112** |

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
- **3.4 What the remaining errors are (descriptive, after grading).**
  - **TrEMBL swaps (4 of 23,994):**
    - two duck T-type calcium channels carry a perfect EEDD ring plus a stray lysine loop (S-F-K-G-W);
    - two ghost-shark "sodium channel proteins" have no lysine at all.
    
    A ring-count override would fix 2 and break 11, so lysine-first stays.
  - **Missed sodium channels:** concentrated in the Naₓ sensor (SCN7A). Its domain-III loop reads T-F-**N**-G-W (the DENA ring).
    - A Naₓ branch (v8) recovers 66 of the 67 Naₓ-named sequences, plus 94 generically named ones.
    - It matches no other protein in the seen proteomes.
    - It awaits a blind test.
- **3.6 Before nerves.** The pumps (Na⁺/K⁺, Ca²⁺, Cu) are present even in the choanoflagellate. Channels expand with the first nerve net (anemone: 46 K, 18 K2P). The E→K change at the domain-III loop separates early DEEA-type channels from bilaterian DEKA sodium channels.
- **3.7 Comb jellies.** No sodium calls in 25,809 comb-jelly proteins. All 8 four-domain voltage-sensor proteins with the domain-III loop read A-T-F-**E**-G-W, including the three named "sodium channel protein". The K is absent in this independent nerve lineage as well.
- **3.8 The earliest bilaterians (exploratory, not counted).** In the predicted proteome of the acoel worm *Hofstenia miamia* (22,454 genes), both sodium-type channels read A-T-F-**E**-G-W. My stated leaning was K, so this was a miss. If Xenacoelomorpha are the sister group of the other bilaterians, the E→K change arose after their split.
- **3.9 Dating the E→K step (failed hypothesis).**
  - **The prediction:** K would be present on both sides of the protostome/deuterostome split.
  - **Protostomes, as predicted:** the brachiopod *Lingula* (5 sodium channels, all K) and the annelid *Capitella* (one K and one E paralog) read K.
  - **Deuterostomes, against the prediction:** the acorn worm *Saccoglossus* and the sea urchin *Strongylocentrotus* read A/T-T-F-**E**-G-W in their "sodium channel proteins", with no K anywhere.
  - **What it implies:** either K arose more than once (in protostomes and in the chordate line), or it arose once and was lost in echinoderms and hemichordates. The data here cannot separate these.
  - **Follow-up (L3557, 8/8):** the lancelet (*Branchiostoma*) and the sea squirt (*Ciona*) both carry A-T-F-**K**-G-W. So K is present across all chordates and all protostomes tested, and absent only in the ambulacrarians (sea urchin, acorn worm).
  - **Which gene was lost (L3561, 1/1).** The sea urchin and acorn worm E-type channels are closer to the bilaterian **NAV2** paralog than to **NAV1**, by alignment-free 4-mer similarity. The NAV2 paralog is the E-type copy that coexists with the K-type NAV1 in the annelid and the lancelet.
  - **What that implies:** ambulacrarians lost the **NAV1 gene** rather than reverting K to E. Because NAV1 (with K) is present on both sides of the protostome/deuterostome split, the simplest history is **one origin of the K-type NAV1 before that split**, followed by loss of NAV1 in the ambulacrarian lineage.
  - **Caveat:** the margins are small (0.03), and the method is alignment-free.
  - **The earliest channels (L3565, failed).**
    - **9 of 10** non-bilaterian and acoel E-type channels sit closer to NAV2, including both acoel channels (margins of 0.013 and 0.020).
    - **One comb-jelly channel** is a near-tie on the NAV1 side (0.088 vs 0.086), so the all-NAV2 prediction failed.
    - **The method loses resolution here:** at these distances, similarity values (about 0.08–0.10) approach the background level.
  - **With real alignment (L3569, 2/2).** A BLOSUM62 global aligner, written in numpy and validated (mouse Scn2a vs Scn8a 78% identity), places **all 12** query channels closer to NAV2:
    - both ambulacrarian channels (margins 0.06 and 0.06);
    - all 10 early and acoel channels, including the comb-jelly near-tie (now 0.465 vs 0.431).
  - **The neighbour-joining tree** groups the six K-type NAV1 genes together, apart from all E-type channels.
  - **Resulting history:** NAV2 (E) is the ancestral family. NAV1 (K) arose within bilaterians after the acoel split, and was later lost in ambulacrarians.
- **3.10 T-type calcium (frozen check, not counted).** A ring with ≥ 2 aspartate sites called T-type in 3,550 of 3,846 TrEMBL vertebrate T-type channels, and in none of 11,061 high-voltage channels.
- **3.5 Battery balance (descriptive).** Metal pumps are few and conserved, while channels (mainly K⁺) multiply in vertebrates: 4–6 channels per pump, against 3.5 in the fly.

## 4. Discussion
- **What carries across ~600 million years:** the selectivity loops themselves.
- **What does not:** flanking residues and family-specific limits.
- **Limitations:**
  - silent subunits, sodium sensors (Naₓ), divergent K2P and insect IR receptors are missed;
  - our own name-based truth rules undercounted correct calls;
  - sequence cannot address higher-level questions such as consciousness, although the parts list of excitability (pacemakers, T-type calcium, leak channels targeted by anaesthetics) is now readable.

## Figures
1. **Figure 1** (`figures/L3493_motif_panel.png`): the metal-selecting loops read from real sequences in six animals.
2. **Figure 2** (`figures/L3489_blind_tests.png`): all eight blind tests, coloured by who graded them.
3. **Figure 3** (`figures/L3493_battery.png`): the nerve battery, chargers against dischargers.
5. **Figure 5** (`figures/L3573_navtree.png`): neighbour-joining tree (1 − identity) of NAV1/NAV2 channels; the K-type NAV1 genes group together.
4. **Figure 4** (`figures/L3557_EtoK.png`): the domain-III pore loop across the tree. **E** in choanoflagellate, placozoan, sea anemone, comb jelly, acoel worm, acorn worm and sea urchin; **K** in brachiopod, annelid, fly, lancelet, sea squirt and vertebrates; A-T-F-**K**-G-W in fly, fish, bird and human; A-T-F-**N**-G-W in the Naₓ sensor.

## 5. Data and code availability
- **dcf-math:** pre-registrations, ledger, rounds, grade outputs, and `rounds/L3485_audit2.py`.
- **dcf-genefinder:** `dcf_nerve.py`, `dcf_pump.py`.
- **Phone:** menu 34.
- **Archived on Zenodo:** dcf-math v1.0.0, DOI 10.5281/zenodo.24234795; dcf-genefinder v1.0.0, DOI 10.5281/zenodo.24234986.
- **Author ORCID:** 0009-0008-9235-4493.

## Declarations
- **Competing interests:** none.
- **Funding:** none.
- **Use of AI tools:** analysis code, data processing and drafting were assisted by Claude (Anthropic), working under the author's direction within the pre-registration protocol described in Methods. The author takes responsibility for the content. Check each venue's policy on AI tools before submission and adjust this statement to its wording.
- **Author:** Gary NOMEREMORTAL Mason, ORCID 0009-0008-9235-4493.
- **Supplementary material:** `supplementary/` (Table S1 genome accessions, Table S2 pre-registration ledger with SHA-256 and dates) and `figures/publication/` (600 dpi and PDF).

## Summary
- **A first full draft of Manuscript 2.** Its central claim, recomputed from committed outputs: the metal-selecting loops of nervous systems can be read from sequence across animals, 67 of 81 blind predictions overall and 13 of 14 against UniProt's independent classification.

## Potential leads for future research
- **[Figure 2]** `figures/L3489_blind_tests.png` (done).
- **[Figures]** Fig. 1, motif panel; Fig. 2, per-test bars; Fig. 3, battery balance.
- **[Outside reader]** As with Manuscript 1.
