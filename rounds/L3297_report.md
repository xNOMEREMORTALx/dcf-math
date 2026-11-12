# DCF L3297: a hedgehog finder (found IHH alone among 26,088 human transcripts, nothing in 70 microbes) and an exon mapper that places an mRNA on a chromosome; both in phone 6.09 and the gene-finder repo; SHH and its claimed coordinates frozen for testing
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 11 November 2026

**Lead:** Gary's request to map Sonic hedgehog (SHH; claimed GRCh38 chr7:155,799,980–155,812,463, 7q36.3) through our genomes, and to work it into DCF phone and the gene finder.

**Pre-registration:** `PREREGISTERED_L3297_shh.txt` (`2220db21…a7b3`), pushed before any SHH or chromosome file is downloaded.

---

## 1. What our data can and cannot show
- **SHH itself is not in human RNA files 1–4**: they hold about half the RefSeq transcripts, and SHH (NM_000193) is in a later file.
- **Its sister gene IHH (Indian hedgehog, NM_002181) is in file 2.** The three human hedgehogs (Sonic, Indian, Desert) share the same architecture.
- **Our human files are mRNA, not chromosomes,** so they carry no chromosome coordinates. Checking "chr7:155,799,980–155,812,463" needs a slice of chromosome 7, which NCBI can serve as a small file (links below).
- **Bacteria have no hedgehog genes,** so the microbial genomes act as a clean negative control.

## 2. A label-free hedgehog finder [development]
In IHH (411 aa), read from its mRNA alone:
- **zinc site H-Y-E-G-R-A-V-D at aa 145**, the conserved signalling half;
- **self-cutting site G-C-F at aa 202.** Here the protein cuts itself in two and attaches **cholesterol** to the signalling half. That is the step that lets hedgehog spread through tissue and pattern the brain, spinal cord and limbs.

**Motif:** H[YF]EGRA[VI]D, then 40–80 aa, then GCF. **Development result:**

| data | proteins scanned | hits |
|---|---|---|
| human mRNA files 1–4 | 26,088 NM_ transcripts | **IHH only** |
| microbial genomes | 70 genomes | **0** |

This is development: IHH was used to design the motif. The fair test is SHH, DHH and mouse Shh (S1).

## 3. An exon mapper: placing an mRNA on a chromosome
`dcf_exonmap.py` (new, gene-finder repo):
- It finds where each piece (exon) of an mRNA sits on a chromosome slice, on either strand.
- It reports intron lengths and GT…AG splice signals, and converts everything to chromosome coordinates.
- **Synthetic test:** IHH split into 3 exons on the minus strand inside random DNA came back with **exact span (1,004,001–1,014,481), exact exon lengths (700/800/973), strand −, both introns GT…AG.**
- **One fix made during testing:** a boundary base that matches on both sides of a junction was first given to the wrong exon. The mapper now slides such boundaries to the GT…AG position.

## 4. Integration
| place | new |
|---|---|
| **gene-finder repo** | `dcf_exonmap.py` (`02fe1bb1…`), `dcf_motif_scan.py` (`21d6ecc0…`): ten preset motifs, each with its test record, plus any custom pattern, on a genome, an mRNA FASTA or a protein FASTA |
| **phone 6.09** | **menu 32** motif scan (runs the gene finder first on a genome); **menu 33** exon map; self-test **263/263** (2 new rows: hedgehog motif on IHH, exon mapper on a synthetic minus-strand gene). Seven .py files in the bundle |

**Preset motifs:**
- hedgehog (dev);
- ferredoxin ladder, CuA, zinc ribbon, rubredoxin (blind-tested);
- C2H2 zinc finger;
- CCHC knuckle (dev);
- voltage sensor (passed L3293);
- K⁺ filter (just failed L3293);
- Cys-loop (corrected after its L3293 failure, **untested**).

## 5. The SHH test [pre-registered]
| id | prediction |
|---|---|
| S1 | the hedgehog motif hits SHH, DHH and mouse Shh (3 of 3) |
| S2 | in SHH the G-C-F site is at aa 197 (G197–C198) |
| S3 | every SHH exon lies inside your claimed span chr7:155,799,980–155,812,463, with ≥ 95% of the mRNA placed |
| S4 | SHH has 3 exons on the minus strand |
| S5 | every mouse Shh exon lies inside chr5:28,661,813–28,672,254 (as fetched from NC_000071.7, GRCm39) |

The slices extend 5 kb beyond each claimed end, so a wrong coordinate shows up as exons outside the span rather than as "not found".

## Action for Gary: 5 small files
Open each link (each is a small text file) and zip all five as **`shh.zip`**:
1. human SHH mRNA: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NM_000193
2. human DHH mRNA: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NM_021044
3. mouse Shh mRNA: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NM_009170
4. human chromosome 7 slice (claimed span ± 5 kb, about 22 kb): https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NC_000007.14&seq_start=155794980&seq_stop=155817463
5. mouse chromosome 5 slice (claimed span ± 5 kb, about 20 kb): https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NC_000071.7&seq_start=28656813&seq_stop=28677254

**On the phone (6.09):** put the files in Download/DCF.
- **Menu 33:** pick the chromosome slice, then the SHH mRNA, to see SHH's exons on chromosome 7.
- **Menu 32:** pick an mRNA file and choose `hedgehog`.

## Record
No predictions graded this round. **306 of 434 passed, plus 3 split.**

## Summary
- **SHH is not in our four human files, but its sister IHH is.** From IHH we built a hedgehog finder (zinc site plus the self-cutting G-C-F site where cholesterol is attached). It picked out IHH alone among 26,088 human transcripts and found nothing in 70 bacterial and archaeal genomes.
- **A new tool places an mRNA on a chromosome:** exons, introns, strand and coordinates. It recovered a synthetic gene exactly, and it is what will check your SHH coordinates.
- **Both are now in the phone (6.09, menus 32 and 33, 263/263) and the gene-finder repo.**
- **The SHH test is frozen:** five small downloads will show whether the motif finds SHH, DHH and mouse Shh, and whether SHH really sits where your source says.

## Potential leads for future research
- **[SHH]** Grade S1–S5 when `shh.zip` arrives.
- **[Hint/intein]** Hedgehog's self-cutting half (the Hog/Hint domain) shares its fold with **inteins**, the self-splicing protein elements in bacteria and archaea. That is a real bridge from hedgehog to our microbial genomes. Design a label-free intein finder (the N-terminal C/S and C-terminal H-N motifs) on seen genomes.
- **[Brain genes]** With the exon mapper, any brain-development gene (PAX6, OTX2, EMX2, FOXG1) can be placed on its chromosome from a slice link; good first examples for menu 33.
- **[Neuro b]**, **[Enzyme labels]**: carried.
