# DCF L3293: photosynthesis confirms the ladder blind (cyanobacteria tier 2, *Heliobacterium* tier 4); the Campylobacterota read tier 4, not a separate band; the nervous system's voltage sensor is found label-free in human mRNA (11 of 13, 100% precise), but the Cys-loop motif was fitted too narrowly
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 11 November 2026

**Leads:**
- [blind_22];
- Gary's new question: **"can we try to locate systems like the central nervous system?"**

**Pre-registrations:**
- `PREREGISTERED_L3289_blind22.txt` (`2028d9bd…be04`);
- **new:** `PREREGISTERED_L3293_neuro.txt` (`058324cf…cf93`) with the script `dcf_neuro_motifs_L3293.py` (`af1b2b6b…c15f`), pushed before the motifs were run on the test files.

**Tool numbers:** blind_22 numbers were committed (SHA-256 `b286eb34…7a34`) before any annotation was read. All 9 files matched by LOCUS; NCBI now names two of them *Heliomicrobium* and *Thermosynechococcus vestitus*.

---

## 1. blind_22: photosynthesis and the ferredoxin ladder [pre-registered]
| group (label fixed in advance) | genome | ladder | CxxC |
|---|---|---|---|
| oxygenic phototroph | *Gloeobacter violaceus* | 0.0130 | 0.39 |
| oxygenic phototroph | *Nostoc* sp. PCC 7120 | 0.0135 | 0.35 |
| oxygenic phototroph | *Thermosynechococcus* | 0.0190 | 0.44 |
| oxygenic phototroph | *Synechococcus elongatus* | 0.0212 | 0.46 |
| **anoxygenic phototroph** | ***Heliobacterium modesticaldum*** | **0.0947** | 0.87 |
| Campylobacterota | *Sulfurovum* | 0.0532 | 0.71 |
| Campylobacterota | *Sulfurospirillum* | 0.0731 | 0.76 |
| Campylobacterota | *Nitratiruptor* | 0.0755 | 0.74 |
| Campylobacterota | *Wolinella* | 0.0892 | 0.75 |

| id | prediction | result | verdict |
|---|---|---|---|
| **P1** | ≥ 3 of 4 cyanobacteria < 0.023, median < 0.023 | **4 of 4**, median 0.016 | **PASS** |
| **P2** | *Heliobacterium* > 0.060 | **0.0947** | **PASS** |
| E1 | ≥ 3 of 4 Campylobacterota in 0.040–0.070 | 1 of 4 (three read 0.073–0.089) | **FAIL** |
| E2 | their median in 0.040–0.070 | 0.074 | **FAIL** |

**Reading.**
- **Photosynthesis split exactly as predicted.**
  - All four oxygen-making cyanobacteria read like oxygen breathers (0.013–0.021). This includes *Nostoc*, which fixes N₂ (a declared risk). Their photosynthesis runs through the plant-type [2Fe-2S] ferredoxin, which the ladder does not count.
  - ***Heliobacterium*, whose reaction centre and enzymes use 4Fe-4S clusters, reads 0.095, solidly tier 4.**
  - **The ladder therefore tracks the 4Fe-4S ferredoxin chemistry, not "uses ferredoxin" or "does photosynthesis".**
- **The low-oxygen band failed again.** Three of four Campylobacterota read tier 4, not 0.040–0.070.
  - In hindsight these four are mostly **anaerobic** respirers: *Wolinella* runs on fumarate, and *Nitratiruptor* and *Sulfurospirillum* on nitrate or sulfur. On that reading tier 4 is the expected place.
  - **The same lesson as L3285:** labels from lifestyle ("low-oxygen") keep failing. The scale itself keeps working on clear-cut metabolisms.
- **Code 9 of 9 correct (table 11); code record 174 of 177.**

## 2. Can we locate the central nervous system? [development + pre-registered test]
**What is possible.**
- A genome carries every tissue's genes, so we can't point to "the brain" in it.
- **What we can locate label-free is the nervous system's electrical machinery: the ion channels that fire nerve impulses.** These are K⁺, Na⁺ and Ca²⁺ proteins, which ties straight to the alkali-metal ladder (L3277).
- Three motifs, read from human mRNA with one transcript per gene:

| motif | what it is | pattern |
|---|---|---|
| **K** | potassium selectivity filter: lets K⁺ through but not Na⁺ | [TSC]-[VIT]-G-[YF]-G |
| **S4** | the voltage sensor: a helix with a positive charge every third residue that moves when the membrane voltage changes | 5 × (R/K + two hydrophobic residues) |
| **CL** | Cys-loop: the signature of neurotransmitter-gated channels (acetylcholine, GABA, glycine, serotonin) | C-x₄₋₆-[FY]-P-[FYW]-D-x₃-C |

**Development (files 1–2, 5,454 genes).**
- The first attempt failed: the voltage sensor found 1 of 17.
- **One revision:**
  - added HCN (C-I-G-Y-G) and EAG/ERG (S-V-G-F-G) filter variants;
  - required hydrophobic residues between the charges;
  - removed accessory subunits without a pore from the answer list;
  - added KCNF1, a real voltage-gated subunit.
- Results after the revision: K 27/30 recall, 60% precision; S4 12/17, 80%; CL 5/7, 100%; **K + S4 in one protein 10/10 precise.**

**Test (files 3–4, 5,410 genes; motifs never run on them before).**
| id | prediction | result | verdict |
|---|---|---|---|
| N1 | K filter recall ≥ 0.70 and precision ≥ 0.45 | recall **11/13**, precision 11/26 = **0.42** | **FAIL** (precision just under) |
| **N2** | S4 recall ≥ 0.55 and precision ≥ 0.65 | **recall 11/13, precision 11/11** | **PASS** |
| N3 | Cys-loop recall ≥ 0.50 and precision ≥ 0.75 | **0 of 8** | **FAIL** |
| N4 | K + S4 precision ≥ 0.90 (needs ≥ 3 hits) | 1 hit (true) | **ungradable** by its own rule |

**Reading.**
- **The voltage sensor, the part that makes nerve cells electrically excitable, is found label-free with 100% precision** on genes it had never seen. It found **6 calcium channels** (CACNA1B, D, E, G, H, I), **2 sodium channels** (SCN7A, SCN11A) and **3 potassium channels** (KCNC2, KCNC4, KCNH6) from sequence alone.
- **The K⁺ filter finds the right genes** (11 of 13) but also picks up unrelated proteins with a G-Y-G-like stretch, so its precision is just under the bar.
- **The Cys-loop failure is diagnosed** (after grading). Five of the misses are GABA-A receptors, whose loop reads F/Y-P-**M**-D, with methionine where the motif demanded an aromatic. Development had mostly acetylcholine-receptor loops (F-P-F-D), so the motif was fitted too narrowly. *CHRNA5*'s mRNA also gave only a 160-aa reading frame. **The fail stands.** A corrected motif ([FY]-P-[FYWM]-D) needs fresh data, such as mouse mRNA.

## Record
**This round:** 7 graded, 3 passed (P1, P2 and N2 passed; E1, E2, N1 and N3 failed; N4 ungradable and not counted).

**Total: 306 of 434 pre-registered predictions passed, plus 3 split.**

## Summary
- **Photosynthesis passed its blind test.** Oxygen-making cyanobacteria read like oxygen breathers (4 of 4), and the 4Fe-4S-based *Heliobacterium* reads tier 4. The ladder measures one specific iron chemistry, not "ferredoxin use" in general.
- **The low-oxygen band failed for the second time,** and the reason is the same: lifestyle labels. Most of these Campylobacterota are actually anaerobic respirers, and they read tier 4.
- **Nervous system:** we can now find the nervous system's electrical machinery from raw human mRNA.
  - The voltage sensor that lets nerve cells fire was found in 11 of 13 channel genes, with no false hits.
  - The potassium filter finds the right genes but is less precise.
  - The neurotransmitter-receptor motif missed the GABA receptors because I fitted it on acetylcholine receptors. That is an honest failure with a clear fix.

## Potential leads for future research
- **[Neuro b]** Corrected Cys-loop ([FY]-P-[FYWM]-D) and a tighter K⁺ filter (require it within ~30 residues of a hydrophobic pore helix). Test on **mouse** mRNA (RefSeq `M_musculus/mRNA_Prot`, files 1–2) when available.
- **[Neuro map]** Using the voltage sensor, list every excitable-membrane gene in all four human files and group them into Na⁺, K⁺, Ca²⁺ and HCN by their filter. This is a label-free "electrical parts list" of the nervous system.
- **[Alkali link]** Compare channel motif counts across microbes (bacteria have K⁺ channels too, e.g. KcsA T-V-G-Y-G) with the energy tiers; pre-register on seen genomes first as development.
- **[Enzyme labels]** Third time the lifestyle labels failed: freeze a rule that labels genomes from annotated enzymes (POR/OOR, *nif*, hydrogenases, terminal oxidases), and use it for any future band test.
- **[Note H v0.6]** Add photosynthesis (P1, P2) as the cleanest demonstration that the ladder measures 4Fe-4S ferredoxin chemistry.
