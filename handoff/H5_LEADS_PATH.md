# DCF Handoff 5 of 8: the lead path (prioritised), data to re-download, closed leads, and what waits on Gary
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 24 November 2026 (after L3997)

---

## 1. Recommended path (in order)
| # | lead | thread | type | what to do |
|---|---|---|---|---|
| 1 | **[T-cell activation]** | Manuscript 3 | blind | Gary downloads ENCSR731OFF (T cells, 36 h activation): loops **ENCFF483FUL**, peaks **ENCFF258BCQ**. Pre-register that the K⁺ excess rises with activation time: resting/36 h no excess, 7-day excess (L3979, p = 0.011). |
| 2 | **[HUVEC Hi-C]** | Manuscript 3 | blind | Gary downloads **ENCFF108FUH** (dilution Hi-C, ENCSR008UIB) and **ENCFF174NVV** (intact Hi-C, ENCSR788FBI; also on GEO GSE238026). Run all loops plus three CTCF references, as for the tissues. |
| 3 | **[Release v1.4.0 / v1.3.0]** | repos | admin | H4 §5. |
| 4 | **[Manuscript 3 → outside reader]** | Manuscript 3 | writing | Freeze v3.0 after leads 1–2. Write a reader brief (like `Reader_brief_Manuscript2.md`). Then bioRxiv. |
| 5 | **[dcf_anchor tool]** | toolkit | code | Package the matched-gene loop-anchor test (H2 §B5) for any gene list. |
| 6 | **[Loop partners: who?]** | Manuscript 3 | blind | Are the non-promoter partner ends enhancers (H3K27ac) or CTCF-only sites? Needs an H3K27ac narrowPeak from one Hi-C tissue (e.g. transverse colon or motor neuron). |
| 7 | **[Pore vs auxiliary, pooled]** | Manuscript 3 | test | Pre-registered paired test of pore minus auxiliary excess across all maps (it has been positive every time). |
| 8 | **[Kv vs non-Kv, pooled]** | Manuscript 3 | blind | On the next new maps (leads 1–2): non-Kv (K2P, Kir, KCa) excess > Kv. |
| 9 | **[Heart Hi-C / KCNMA1]** | mitochondria | blind | KCNMA1 (mitoBK) is the most-anchored K⁺ gene. Test it in heart/muscle Hi-C (needs a heart loops file). |
| 10 | **[Phone 6.21]** | phone | code | Visual microphone as menu 38; validate with a real 60–100 Hz tone at 240 fps. |
| 11 | **[Fish H/Y blind test]** | Manuscript 4 | blind | Predict TrpD (H or Y) for unseen fish photolyases (*Sander*, *Pungitius*, *Trematomus*, *Morone*, *Sebastes*, *Epinephelus*). Needs NCBI/UniProt protein downloads. |
| 12 | **[Period-24 test]** | math | test | Pre-register a statement about triangular numbers with given reciprocal periods in a new range (e.g. periods 30, 36, 40), before computing. |
| 13 | **[Manuscript 2 split]** | Manuscript 2 | writing | Methods paper plus evolution paper; rule audit against standing rules 4–8. |
| 14 | **[Manuscript 1 outside reader]** | Manuscript 1 | writing | The submission plan is ready: bioRxiv → PCI Microbiology. |
| 15 | **[INTEGRATION refresh]** | repo | writing | Add the nerve, cryptochrome and chromatin threads. |

**Other open leads, carried:**
- **[Code-3]** A GC-adjusted ORF ratio.
- **[Long reads] / [Metagenome bins]** for the gene finder (H3 §6).
- **[Λ isotopes]**, **[N2]** OEIS check, **[R5]** composite Fibonacci minima rule.
- **[CTCF v2 blind]** The relaxed CTCF finder on new proteomes.
- **[Fragment-rescue rule]** Partial sodium channel.
- **[Gear speed dial]** S4 tooth count vs activation speed.
- **[Information iron, cryptochromes]** Do DNA-repair [4Fe-4S] and cryptochrome FAD chains co-occur?
- **[A-form 11]** Only if RNA-structure work begins: 11 bp/turn is the measured anchor.

## 2. Manuscript 3: what is established and what is open (for planning)
**Established:**
- **Pore-forming K⁺ genes sit at CTCF loop anchors more than matched genes:**
  - ten cell lines (p = 0.002–0.008);
  - WTC11 iPSC (blind, p = 0.006);
  - a 7-day-activated T-cell sample (p = 0.011);
  - CTCF-anchored Hi-C loops in motor neurons, astrocytes, colon and muscle under three independent CTCF references (p = 0.0008, 0.005, 0.0009).
- **The same genes carry it everywhere** (rank ρ 0.66–0.78).
- **The non-voltage-gated families** (K2P, Kir, KCa) lead; Kv is weakest.
- **Auxiliary subunits never show it.**
- **Specificity:** none of these show it:
  - non-K⁺ tetramers (blind);
  - resting-potential transporters (in tissues);
  - six-fold channels;
  - mitochondrial OXPHOS genes (blind).
- **Loop partners:** K⁺-gene loops end at other gene starts half as often as matched genes' loops in Hi-C (p = 0.0001, replicated blind in T cells).
- **Loop length is ordinary.**

**Open:**
- T cells are mixed and sample-dependent.
- HUVEC and HMEC have not been tested by Hi-C.
- The partner identity is unknown.

## 3. Closed leads (do not reopen without a new idea)
| lead | why closed |
|---|---|
| Six-fold channel (connexin/ORAI) excess | failed in new ChIA-PET (L3989) and under the T-cell reference (L3993) |
| Symmetry-order scaling of the anchor excess | L3885, L3937 (non-K⁺ tetramers blind p = 0.93/0.89) |
| "Neural-lineage only" reading | colon and muscle also show it (L3893, L3913) |
| "Assay creates the excess" | within-cell split: CTCF ChIA-PET yes, CTCF-free Hi-C no (L3897–L3905) |
| Anchor width / promoter loops explain primary-cell null | L3921, L3933 |
| K⁺ loops are longer (boundary-scale) | L3965 (p = 0.47, 0.89) |
| 7/78/79/401 patterns in K⁺ results | definition- and threshold-dependent (L3925) |
| Cryptochrome score cut as the marker | replaced by the family rule (L3809) |
| Magnetosome genes in animals | ordinary families (L3789, L3793) |
| Earlier closed list (pre-L3173) | iron predicts Sec within anaerobes; SECIS hairpin filter; "long 3′ UTR → brain"; *E. coli* promoters label-free; helical-harmonic gene lengths; 13/37; p53/SOD1 numerology; Kozak −3 rule (L3313); 9-letter voltage-sensor rhythm beyond the sensor (L3453) |

## 4. Data to re-download (not in the repositories)
**Annotation:** GENCODE v49 GTF (`gencode.v49.annotation.gtf.gz`).

**4DN union loops:** `H1ESC.union-loops.bedpe` and `HFFc6.union-loops.bedpe` (Gary's L3705 upload; column 7 lists the supporting assays).

**ENCODE CTCF ChIA-PET loops (top 28,270 by PET count):**

| cells | file |
|---|---|
| SK-N-SH | ENCFF775DIU |
| K562 | ENCFF118PBQ |
| HepG2 | ENCFF743ZWY |
| IMR-90 | ENCFF816ATV |
| HEK293 | ENCFF432WRY |
| MCF 10A | ENCFF310MTX |
| BJ | ENCFF253KLV |
| RWPE1 | ENCFF479KLF |
| WTC11 | ENCFF455CNF |
| CD4 T (L3877) | ENCFF786NNV, ENCFF937PTH, ENCFF031DPV, ENCFF316XYJ, ENCFF939ZKJ |
| HUVEC | ENCFF377RDA |
| HMEC | ENCFF436NFY |
| CD4 T, 7-day | ENCFF840AQR, with peaks ENCFF416VKW and ENCFF478NWL |

**ENCODE Hi-C loops:**

| cells | files |
|---|---|
| motor neurons | ENCFF215XMY, ENCFF638CCE, ENCFF836TQT |
| astrocytes | ENCFF886EVV, ENCFF424KFY |
| transverse colon | ENCFF008FXM, ENCFF259LCX |
| skeletal muscle | ENCFF735TXQ, ENCFF509PNA |
| CD4 T, resting | ENCFF749LFC |
| CD4 T, activated | ENCFF169BLJ |

**Direct-download form:** `https://www.encodeproject.org/files/<ACC>/@@download/<ACC>.bedpe.gz` (peaks: `.bed.gz`).

## 5. What waits on Gary
- **Downloads:** ENCFF483FUL, ENCFF258BCQ, ENCFF108FUH, ENCFF174NVV (leads 1–2). Later: an H3K27ac peak file from colon or motor neurons; a heart Hi-C loops file.
- **Releases:** dcf-math v1.4.0 and dcf-genefinder v1.3.0 (H4 §5). Also check the v1.3.0 Zenodo DOI.
- **Outside readers** for Manuscripts 1, 2 and 3.
- **Phone:** try `dcf_visualmic.py` with a real 60–100 Hz tone at 240 fps and report the result.

## Summary
- **Next:** the two decisive data tests (T-cell activation, HUVEC Hi-C), then the releases and the Manuscript 3 outside reader.
- **Closed lines are listed** so they are not repeated, and every data file needed is listed by accession.

## Potential leads for future research
- **The table in §1 is the lead list,** in recommended order. Applications and long-range directions are in H8.
