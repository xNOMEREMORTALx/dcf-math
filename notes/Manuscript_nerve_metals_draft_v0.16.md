# Reading the metal chemistry of nervous systems from sequence alone: pre-registered blind tests across animals
### Manuscript 2, draft v0.16 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026
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

We wrote transparent, label-free rules that read these loops from protein or mRNA sequence. We tested them in **twenty-five pre-registered blind tests**. Each rule was hashed before testing, and each tool output was committed before any label was read.

**Results:**
- **Overall:** **135 of 160** gradeable predictions passed.
- **At the base of the animal tree** (choanoflagellate, sponge, placozoan, sea anemone): 7 of 7 passed. No nerve-type sodium channel was called. The early sodium-channel homologues read A-T-F-**E**-G-W at the domain-III position where every bilaterian sodium channel reads A-T-F-**K**-G-W.
- **Sodium vs calcium on 24,796 unseen vertebrate channel sequences (UniProt TrEMBL):** 4 swaps in 23,994 calls (0.02%), with recall 93% (Na) and 99% (Ca).
- **Against an independent reference** (UniProt's curated protein families, 58,949 reviewed animal proteins from all species not used in development):
  - 13 of 14 predictions passed;
  - 345 of 351 class calls agreed with UniProt;
  - none of 919 nematode proteins was called a sodium channel (nematodes lack them).
- **Where the NMDA "learning switch" begins:** across 21 proteomes, its obligatory NR1 subunit is found first in cnidarians, and is absent from sponges, single-celled relatives and the comb jelly (12 of 15).
- **Sodium-channel loss is lineage-specific:** nematodes and tardigrades lack voltage-gated sodium channels, but animals as small as a spider mite, a 1 mm annelid and rotifers keep them (18 of 21 across four tests).
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
   - the sodium lysine loop [TS]-[FY]-[KR]-[GA]-W, or (v3, L3633) [TS]-W-K-[GA]-W → **Na**;
   - otherwise ≥ 3 calcium-ring matches [TS]-x-[ED]-x-W → **Ca**.
3. **1-domain branch:**
   - C-I-G-Y-G → **HCN**;
   - [TSC]-[VITL]-G-[YF]-G → **K**.

**Research rules (not yet in the released tools):**
- **Na (partial):** 800–1,499 aa, ≥ 4 S4 matches, a lysine loop (L3641; 9/9 in development, 1/1 blind).
- **Nearest-reference naming:** local alignment (Smith–Waterman, BLOSUM62) against mouse references; NR1 = nearest Grin1.

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
| naming unnamed genes | zebrafish unnamed channels, local aligner | UniProt / NCBI names | **1/1** |
| comb-jelly naming | 141 channel calls, local aligner | pre-stated hypothesis | **2/2** |
| anemone naming | 46 K calls, local aligner | pre-stated hypothesis | **2/2** |
| battery ratio | 5 new organisms, cut 1.8 | nervous system yes/no | **4/5** |
| sea-hare NMDA | *Aplysia* iGluRs, local aligner | pre-stated hypothesis | **2/2** |
| tardigrade 2 | *Ramazzottius* (22,945) | pre-stated hypothesis | **2/2** |
| NR1 on the tree | 21 proteomes, local aligner | pre-stated expectation | **12/15** |
| moulting animals | horseshoe crab, spider mite, priapulid | pre-stated hypothesis | **4/5** |
| spiralians (rule v3) | leech, *Dimorphilus*, rotifer | pre-stated hypothesis + alignment | **6/7** |
| rotifers (partial rule) | *B. plicatilis*, *A. ricciae* | pre-stated hypothesis + alignment | **6/7** |
| **total** | | | **135/160** |

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
- **3.11 What the comb jelly expanded (L3585, 2/2).** A local aligner (Smith–Waterman, BLOSUM62; validated 39/40 on named zebrafish channels) names the comb jelly's 141 distinct channel calls by their nearest mouse channel:
  - **104 are Kv1 (Shaker)**, plus 9 Kv4, 3 Kv3 and 1 Kv2;
  - all 19 K2P calls are nearest a mouse K2P.
  
  Its excitability is built largely on one channel subfamily, Shaker.
  - **Contrast, the sea anemone (L3589, 2/2):** its 46 K calls spread over Kv1 (17), Kv4 (9), Kv3 (8), KCNH (8) and Kv2 (2). The largest share is 37%. So the comb jelly's single-subfamily expansion is specific to that lineage.
- **3.12 The battery ratio (L3609, L3613).** Channels per metal pump:
  - 0.05–1.60 in 6 organisms without nerves;
  - 2.00–14.25 in 11 with nerves (Figure 7).
  
  A blind test on five new organisms with the cut frozen at 1.8 passed 4 of 5. The tardigrade (nerves, ratio 1.54) failed; it also lacks a DEKA channel in its proteome, consistent with tardigrade gene loss.
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
- **3.13 The sea hare's learning receptors (L3617, 2/2).** Local alignment sorts *Aplysia*'s 33 glutamate-receptor calls into 9 NMDA (4 nearest Grin1), 15 AMPA and 9 kainate. Every one agrees with UniProt's own name, although the short NMDA motif had failed outside vertebrates (L3465).
- **3.14 A second tardigrade (L3621, 2/2).** *Ramazzottius* has a battery ratio of 1.53 (*Hypsibius* 1.54) and no voltage-gated sodium channel. Its only sodium-lysine protein aligns nearest NALCN, the leak channel, which lacks a full voltage sensor. The L3613 "exception" is therefore a real pattern.
- **3.15 NR1 across the tree (L3625, 12/15; Figure 9).**
  - **Not found:** no glutamate-receptor gate in protists or sponges; receptors but no NR1 in the comb jelly.
  - **Found:** NR1 in both cnidarians, the acoel and all protostomes tested.
  - **The three failures:**
    - **Trichoplax:** its UniProt receptors are fragments.
    - **Sea urchin and Ciona:** no NR1. A full alignment of every 600–1,600 aa protein to Grin1, with Hydra as a working positive control, confirms the absence in UniProt (best scores 475–545, against 1,616–2,137 for true NR1s). Gene loss and missing annotation are not yet separated.
- **3.16 Sodium loss is not about size (L3629, L3637, L3645; Figure 8).**
  - **Animals that keep the lysine sodium channel:** the horseshoe crab, spider mite, priapulid, leech, the 1 mm annelid *Dimorphilus* and three rotifers.
  - **Animals that lack it:** only nematodes and tardigrades, two lineages that are not sister groups. So the loss probably happened twice.
  - **The battery ratio follows sodium, not size:** all animals with the channel are above 1.8, and both sodium-less lineages are below it.
- **3.17 Rule repairs found by these tests.**
  - **The priapulid sodium channel reads T-W-K-G-W.**
    - **A first fix,** allowing W at that position whenever K or R followed, made 2 false calls on horseshoe-crab T-type calcium channels (S-W-R-x-W) and was rejected before testing.
    - **v3 accepts W only with the lysine K.** It changes exactly one call across every protein set seen, and passed blind in L3637.
  - **Sodium-channel fragments below 1,500 aa** (*Dimorphilus*, a marine rotifer) are caught by the partial rule. Its first blind call was correct.
  - **Disclosed during grading:** a parsing bug in one grader (L3637), and an NALCN count frozen without a score floor (L3645). Neither changed an outcome.
- **3.18 NALCN copies (descriptive, L3649).** The three NALCN entries of *B. calyciflorus* are 98.5–100% identical where they align. They differ only in a domain II/III loop word (T-N-E-G-W vs T-Q-K-G-W), so they are variants of one gene rather than three genes. Each rotifer therefore carries one NALCN gene, two as a homeolog pair in the bdelloid.
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
7. **Figure 7** (`figures/L3609_battery_ratio.png`): channels per metal pump in 17 organisms; animals with and without nerves separate.
6. **Figure 6** (`figures/L3593_kfamilies.png`): voltage-gated K subfamilies by lineage. The comb jelly is 85% Kv1; the sea anemone, the placozoan (no neurons) and mouse spread across families.
5. **Figure 5** (`figures/L3573_navtree.png`): neighbour-joining tree (1 − identity) of NAV1/NAV2 channels; the K-type NAV1 genes group together.
8. **Figure 8** (`figures/L3649_size_sodium.png`): battery ratio in 10 nerve-bearing animals tested blind. The lysine sodium channel is present in all above the 1.8 cut and absent in both tardigrades, whatever the body size.
9. **Figure 9** (`figures/L3649_nr1_tree.png`): NR1 calls in 21 proteomes, ordered on the tree. The first NR1 appears in cnidarians.
4. **Figure 4** (`figures/L3557_EtoK.png`): the domain-III pore loop across the tree. **E** in choanoflagellate, placozoan, sea anemone, comb jelly, acoel worm, acorn worm and sea urchin; **K** in brachiopod, annelid, fly, lancelet, sea squirt and vertebrates; A-T-F-**K**-G-W in fly, fish, bird and human; A-T-F-**N**-G-W in the Naₓ sensor.

## 5. Data and code availability
- **dcf-math:** pre-registrations, ledger, rounds, grade outputs, and `rounds/L3485_audit2.py`.
- **dcf-genefinder:** `dcf_nerve.py` (v3), `dcf_pump.py`.
- **Phone:** menu 34 (bundle 6.15).
- **Archived on Zenodo:** dcf-math v1.0.0, DOI 10.5281/zenodo.24234795; dcf-genefinder v1.0.0, DOI 10.5281/zenodo.24234986.
- **Author ORCID:** 0009-0008-9235-4493.

## Declarations
- **Competing interests:** none.
- **Funding:** none.
- **Use of AI tools:** analysis code, data processing and drafting were assisted by Claude (Anthropic), working under the author's direction within the pre-registration protocol described in Methods. The author takes responsibility for the content. Check each venue's policy on AI tools before submission and adjust this statement to its wording.
- **Author:** Gary NOMEREMORTAL Mason, ORCID 0009-0008-9235-4493.
- **Supplementary material:** `supplementary/` (Table S1 genome accessions, Table S2 pre-registration ledger with SHA-256 and dates) and `figures/publication/` (600 dpi and PDF).

## Summary
- **Draft v0.16 adds §3.13–3.18 and Figures 8–9:**
  - the sea hare's NMDA receptors;
  - a second tardigrade;
  - the NR1 subunit across 21 proteomes (first in cnidarians);
  - sodium-channel loss tested against body size (lineage-specific, not size-driven);
  - the v3 and partial-channel rule repairs;
  - the rotifer NALCN variants.
- **Every pass/fail count is from `rounds/L3485_audit2.py`: 135 of 160.**

## Potential leads for future research
- **[Outside reader]** As with Manuscript 1; update `notes/Reader_brief_Manuscript2.md` to v0.16.
- **[Length]** At 25 tests the Results section is long. Consider splitting it: a methods/benchmark paper (§3.1–3.12) and an evolution paper (E→K, NR1, sodium loss).
- **[RefSeq NR1]** The sea-urchin and Ciona RefSeq proteins would close the open question in §3.15.
