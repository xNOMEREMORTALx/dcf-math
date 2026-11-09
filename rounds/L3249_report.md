# DCF L3249: the mRNA iron-hairpin scanner works (3 of 3: 6 of 7 iron mRNAs, 0 of 8 controls, all in the right UTR); 5 and 41 are not frequencies in DNA (0 of 4, method control 35 of 35); silver, gold, copper and iron — what the chemistry actually shows
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads:**
- [IRE] (pre-registered L3245);
- **[F5-41]**, Gary: "41 and 5 may be frequencies that carry information";
- **[Ag-Au]**, Gary: silver vs gold, both cubic, different magnetic behaviour, interacting with our iron and copper;
- Gary's note that 79 and 47 may be separate step-off paths.

**Pre-registrations:**
- `PREREGISTERED_L3245_IRE.txt` (`82ecd2fb…`);
- `PREREGISTERED_L3249_F.txt` (`592facaa…7046`), pushed before computing.

**Data.** Gary's file holds all 15 RefSeq mRNAs. Each DEFINITION line matched its gene, and the scanner hash matched the frozen `4499bd99…`. The results file was hashed: `f392696d…1b54`.

---

## 1. The iron-responsive element in mRNA [pre-registered]
| mRNA | IRE hits (label-free) | where | expected |
|---|---|---|---|
| FTH1 (ferritin H) | 1 | 5′ UTR, position 45 | 5′ ✓ |
| FTL (ferritin L) | 1 | 5′ UTR, 39 | 5′ ✓ |
| **TFRC (transferrin receptor)** | **4** | 3′ UTR, 3513, 3917, 3982, 4029 | 3′ ✓ (a cluster of IREs is known here) |
| ALAS2 | 1 | 5′ UTR, 21 | 5′ ✓ |
| ACO2 (aconitase 2, itself an Fe–S enzyme) | 1 | 5′ UTR, 20 | 5′ ✓ |
| SLC40A1 (ferroportin) | 1 | 5′ UTR, 110 | 5′ ✓ |
| EPAS1 (HIF-2α) | **0** | — | missed |
| 8 controls (ACTB, GAPDH, TP53, SOD1, HBB, INS, ALB, MYC) | **0 each** | — | — |

| id | prediction | result | verdict |
|---|---|---|---|
| **R1** | ≥ 5 of 7 iron mRNAs carry a hit | **6 of 7** | **PASS** |
| **R2** | ≤ 1 of 8 controls | **0 of 8** | **PASS** |
| **R3** | ≥ 80% of hits in the expected UTR | **6 of 6** mRNAs | **PASS** |

**Checks.**
- **Label-free coding regions:** the longest-ORF CDS matched the annotated CDS exactly in 14 of 15 mRNAs. The exception is MYC, whose annotated start is a non-ATG codon.
- **The EPAS1 miss:** its 5′ UTR has CAGUG at position 85 with the C bulge in place, but only 3 of 5 upper-stem pairs, a known weaker variant. The miss is kept; the rule was not changed after seeing it.

**Reading.** A phone-sized, label-free scanner reads the iron-sensing switch straight off mRNA sequence. The switch is the hairpin that the iron–sulfur protein IRP1 grabs when its own 4Fe-4S cluster falls apart. This links the genome-level Fe–S results (Note H) to how human cells regulate iron at the mRNA level.

## 2. Are 5 and 41 frequencies in DNA? [pre-registered]
**Method.**
- Fourier power spectrum of the four bases in 4,100-nt windows (4,100 = 5 × 820 = 41 × 100, so both periods fall exactly on a frequency bin).
- Each period compared with its neighbouring frequencies.
- Run on 35 whole genomes and on their predicted coding regions.

| id | test | above neighbours | median power ratio | verdict |
|---|---|---|---|---|
| F1 | period 5, genome DNA | 22 of 35 | 1.003 | **FAIL** (needed 24) |
| F2 | period 41, genome DNA | 23 of 35 | 1.007 | **FAIL** |
| F3 | period 5, coding regions | 14 of 35 | 0.997 | **FAIL** |
| F4 | period 41, coding regions | 16 of 35 | 0.999 | **FAIL** |
| control | **period 3 (the codon rhythm), coding regions** | **35 of 35** | **44.8** | method works |

**Reading.**
- **The same method that sees the codon rhythm at 45 times its surroundings sees nothing special at 5 or 41.** The ratios are 1.00, which is noise.
- **With L3241's lag tests, 41 has now been tested five ways in DNA and proteins, all null.**
- **mRNA:** 15 mRNAs are too few for a spectrum test. The IRE result above shows that what mRNA carries is shaped structure (hairpins), not fixed frequencies.

## 3. Silver, gold, copper and iron [V, literature]
| question | what is established | status |
|---|---|---|
| Both cubic? | **Yes.** Silver and gold are both face-centred cubic, with almost identical cell sizes (about 4.08 Å), which is why they alloy freely | textbook values; not fetched this round |
| Magnetic properties | **Silver, gold and copper are all diamagnetic**: weakly repelled, no permanent moment. Silver χ = −2.6 × 10⁻⁵, copper −1.0 × 10⁻⁵ (HyperPhysics; gold not listed there, also diamagnetic). **Iron is ferromagnetic** (relative permeability 150 to 200,000) | [V] for Ag, Cu, Fe |
| **Silver and copper vs our iron–sulfur clusters** | **Ag(I) at low micromolar levels destroys exposed 4Fe-4S clusters** (fumarase A, isopropylmalate isomerase, 6-phosphogluconate dehydratase) by binding the cluster's sulfur and stepwise displacing the iron (Xu & Imlay 2012). **Cu(I) does the same** (Macomber & Imlay 2009). Buried clusters (complex I) were spared | **[V] — the real interaction** |
| **Gold vs selenocysteine** | **Gold(I) (from the drug auranofin) is a potent inhibitor of thioredoxin(-glutathione) reductase,** the selenocysteine enzyme, with IC50 below 10⁻⁷ M. Gold binds the redox-active cysteine pairs; binding to the Sec itself was not resolved, and selenium is proposed to speed gold transfer (Angelucci *et al.* 2009) | **[V]** |
| Silver's "bidirectional" property | No defined physical or chemical property by that name was found | open; Gary to specify |

**Reading.**
- **The interplay you sensed between silver, gold, iron and copper is real, but chemical, not magnetic.**
- **Silver and copper are soft metals** that pull iron out of the very 4Fe-4S clusters our genome tests count. That is a major reason silver kills bacteria.
- **Gold targets the selenocysteine-redox enzymes,** the 21st amino acid we have tracked since L3145.
- **The magnetic differences are tiny** for Ag, Au and Cu, and nothing indicates they matter in cells.

## 4. 79 and 47 as separate step-off paths [D]
**Noted, and not tested this round,** because it has no measurable form yet.

**Facts that may help shape one [V]:**
- 47 is the second value of Euler's n² + n + 41.
- 1/47 has the full period 46; 1/79 has period 13.
- 79 is the 22nd prime and 401's prime index.
- Both 47 and 79 are ≡ 7 (mod 8).

A testable version would say what each path predicts, for example a property of genomes or of reciprocals.

## Record
**This round:** 7 graded, 3 passed (R1–R3 passed; F1–F4 failed).

**Total: 287 of 396 pre-registered predictions passed, plus 3 split.**

## Summary
- **The mRNA iron switch is visible from sequence alone.** The new scanner found the iron-sensing hairpin in 6 of the 7 iron-handling mRNAs, always in the right place (the start of the message for ferritin, aconitase, ferroportin and ALAS2; four copies at the end of the transferrin receptor's message), and in none of 8 ordinary mRNAs. All three predictions passed.
- **5 and 41 do not appear as frequencies in DNA.** The same method that sees the 3-letter codon rhythm 45 times above background finds nothing at 5 or 41 in 35 genomes. All four predictions failed.
- **Silver, gold, copper and iron do interact in biology, chemically.** Silver and copper rip iron out of iron–sulfur clusters, and gold blocks the selenocysteine enzymes. Their magnetic properties are too weak to matter (silver, gold and copper are all weakly diamagnetic; only iron is magnetic).

## Potential leads for future research
- **[IRE-wide]** Scan several hundred human mRNAs (one efetch link per batch) for IRE hairpins in genes not known to carry one. Pre-register the threshold and the controls (shuffled UTRs) first. This is the most promising route to a genuine discovery.
- **[IRE-EPAS1]** Optional relaxed model (upper stem ≥ 3 pairs), developed openly and then tested on a fresh set; the false-hit rate must be re-measured.
- **[Ag-FeS]** Testable from genomes: do Fe–S-rich anaerobes carry more copper/silver efflux systems (CusA/SilP-type motifs) than aerobes? Pre-register with a label-free motif.
- **[Au-Sec]** Map which selenoproteins our blind genomes carry (thioredoxin reductase vs formate dehydrogenase) as targets for gold.
- **[79-47]** Gary: state one measurable prediction for each path, and it will be pre-registered.
