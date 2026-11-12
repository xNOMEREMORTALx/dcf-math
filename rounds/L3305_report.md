# DCF L3305: your SHH coordinates are verified to the base (chr7:155,799,980–155,812,463, 3 exons, minus strand); the hedgehog motif finds human and mouse SHH but misses DHH (3 of 5)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** the five SHH files (four attachments, plus mouse Shh NM_009170.4 pasted into the message). All headers match. Both chromosome slices are exactly the requested length (22,484 and 20,442 bp).

**Pre-registration:** `PREREGISTERED_L3297_shh.txt` (`2220db21…a7b3`). Graded with the frozen tool versions retrieved from git (`dcf_exonmap.py` `02fe1bb1…`, `dcf_motif_scan.py` `21d6ecc0…`; hashes match the ledger).

---

## 1. Where SHH sits on chromosome 7 [S3, S4]
| exon | mRNA positions | chromosome 7 (GRCh38) | length |
|---|---|---|---|
| 1 | 1–641 | 155,811,823–155,812,463 | 641 nt |
| intron 1 | — | GT … AG | 5,265 bp |
| 2 | 642–903 | 155,806,296–155,806,557 | 262 nt |
| intron 2 | — | GT … AG | 2,569 bp |
| 3 | 904–4,650 | 155,799,980–155,803,726 | 3,747 nt |

- **The gene spans 155,799,980–155,812,463, exactly the coordinates your source gave, to the base at both ends.**
- 100% of the mRNA is placed; **minus strand**; both introns have canonical GT…AG splice signals.
- This is the first external numerical claim in this series to be **verified by our own computation**, from raw sequence.

**Mouse Shh (chromosome 5, GRCm39).**
- Three exons, at 28,671,459–28,672,099, 28,666,320–28,666,581 and 28,661,838–28,663,601; minus strand; GT…AG.
- The span (28,661,838–28,672,099) lies **inside** your source's 28,661,813–28,672,254. The claimed range is 25 bp and 155 bp wider, most likely because NCBI's gene record covers the longest transcript variant.

**A finding along the way [V].** Human and mouse exons 1 and 2 have **identical lengths (641 and 262 nt)** after about 90 million years of separate evolution. Only exon 3, which carries the long untranslated tail, differs (3,747 vs 1,764 nt).

## 2. The hedgehog motif [S1, S2]
| id | prediction | result | verdict |
|---|---|---|---|
| S1 | motif hits SHH, DHH and mouse Shh | SHH ✓, mouse Shh ✓, **DHH ✗** (2 of 3) | **FAIL** |
| S2 | SHH G-C-F site at aa 197 | the tool reported **aa 200** | **FAIL** |
| **S3** | every SHH exon inside the claimed span, ≥ 95% placed | inside, exact to the base, 100% placed | **PASS** |
| **S4** | 3 exons, minus strand | 3 exons, minus strand | **PASS** |
| **S5** | every mouse Shh exon inside the claimed span | inside | **PASS** |

**Diagnosis (after grading).**
- **S1:** DHH's zinc site reads H-Y-E-G-R-A-**L**-D. The motif, built on IHH alone, allowed only V or I there. This is the same narrow-fitting lesson as the Cys-loop and K⁺ filter. A corrected preset `hedgehog2` ([VIL]) is added to the scanner, marked **untested**.
- **S2:** the SHH mRNA has an in-frame ATG three codons before the real start, with no stop between. The longest-reading-frame rule therefore began the protein at M-G-E-M… instead of RefSeq's M-L-L-L….
  - Counted from the real start, the protein is **462 aa** (the RefSeq length) and **G-C-F is at 197**, as predicted.
  - The grade stays FAIL because the frozen tool reported 200. **Tool lesson:** the longest-ORF rule can overshoot the true start by an upstream in-frame ATG.
- The **self-cutting site G-C-F is present in all three hedgehogs** (human SHH, DHH, mouse Shh) and in IHH. Only the zinc-site spelling varies.

## Record
**This round:** 5 graded, 3 passed (S3, S4 and S5 passed; S1 and S2 failed).

**Total: 309 of 439 pre-registered predictions passed, plus 3 split.**

## Summary
- **Your SHH location is right, exactly.** Placed from raw sequence, SHH's three exons cover chr7:155,799,980–155,812,463 on the reverse strand, matching both ends to the base. Mouse Shh also sits within its stated range on chromosome 5.
- **The hedgehog finder found human and mouse SHH but missed DHH,** whose zinc site uses leucine where the motif expected V or I. A corrected version is in the scanner, untested.
- **SHH's cholesterol cutting site is at residue 197 once the right start codon is used.** The tool started three codons too early and reported 200, so that prediction is counted as failed.
- **Human and mouse SHH keep identical exon 1 and 2 lengths** (641 and 262 nt) after about 90 million years apart.

## Potential leads for future research
- **[ORF start]** Fix the longest-ORF rule: when an in-frame upstream ATG lies in a GC-rich 5′ leader, also report the next ATG, and test against RefSeq protein lengths on the human files (development), then pre-register.
- **[Exon conservation]** Use the exon mapper on more human–mouse pairs (PAX6, OTX2, FOXG1) and test whether coding exon lengths are conserved more often than chance. This needs chromosome slices; pre-register first.
- **[hedgehog2]** Test the corrected motif on fresh hedgehog genes (zebrafish shha/shhb, chicken SHH; RefSeq mRNA links).
- **[SHH enhancer]** SHH's limb enhancer (ZRS) lies about 1 Mb away inside the LMBR1 gene. Mapping it is a natural next exon-map exercise (needs a larger slice).
