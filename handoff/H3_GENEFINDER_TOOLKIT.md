# DCF Handoff 3 of 6: the gene-finder toolkit (repo dcf-genefinder)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 8 November 2026

---

## 1. Files and SHA-256 (as pushed after L3173)
| file | role | SHA-256 |
|---|---|---|
| `dcf_genefinder_mobile.py` **v2.31** | label-free gene finder | 215898dfd5797589eb3cb0b16b7b104af4b8b1eab89f15fb1380fd9402ff36da |
| `dcf_grade.py` | found / correct / exact start against the file's own annotation | 761bd8a51db82c593de3a76bd91b29f778b33d246efaf94eadddd88d2282da7c |
| `dcf_promoters.py` | learned −35/−10 boxes, E17 self-check | ba61d22174bd2b956ae08882aca0ee59d7804b70449f734a6a2fb117be275ea5 |
| `dcf_pylflag.py` | TAG/TGA read-through joins (Pyl/Sec) | 2952984a1f57d0df45291665097d6ddce70d228d17f5783fb1c22fd1e025a6be |
| `dcf_metals.py` | Fe–S (CxxC) density, R, C2H2 zinc fingers | a640abc9a5c7d8c8fc4ea9444b6956c7c05c8471e8887af3c5b9673e2e34d6b3 |
| `dcf_secflag.py` | selenocysteine candidates (upstream/downstream TGA) | 59e3188bf547114fe11ff0ce85985954b59eb3ea25715ad7886b308efb5d1744 |

## 2. Usage
```
python3 -I dcf_genefinder_mobile.py genome.gb --table auto --out pred.gff3
python3 -I dcf_grade.py    genome.gb pred.gff3
python3 -I dcf_metals.py   genome.gb pred.gff3
python3 -I dcf_pylflag.py  genome.gb pred.gff3
python3 -I dcf_secflag.py  genome.gb pred.gff3
python3 -I dcf_promoters.py genome.gb pred.gff3
```
**GenBank reader (all tools, fixed in L3069):** IUPAC letters become N, so coordinates stay aligned.
```python
seq = re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+', txt.split('\nORIGIN')[1].split('\n//')[0])).upper())
```

## 3. Version history (gene finder)
| version | round | change |
|---|---|---|
| v2.25 | | tiny AT-rich code rule |
| v2.26 | L2969 | best start for GC > 0.55 (regressed the code call and starts) |
| v2.27 | L2973 | best start for all genomes, minimum length 240; best start only in the final self-train |
| v2.28 | L2993 | start search extends back to the previous in-frame stop |
| v2.29 | L3001 | learned start signal (log-odds −20..−1 plus start-codon preference) |
| v2.30 | L3009 | start window 30 nt |
| **v2.31** | **L3149** | **genome-size prior:** when the read-through test says code 11 and the ORF-length ratio says code 4, keep 11 if the genome is > 2.5 Mb. Blind 4/4 (L3153). |

## 4. Blind records (unseen genomes)
| measure | record |
|---|---|
| Genetic code | **104 of 107** |
| Genes found | typically 86–95% |
| Genes correct | 91–99% |
| Exact starts | 52–94% (lowest in GC-rich genomes) |
| Pyrrolysine genes (dcf_pylflag) | **48/48** in 9 species (27 development + 21 blind) |
| Selenocysteine, *E. coli* | 3/3 (fdhF, fdnG, fdoG) |
| Promoters | Firmicutes 17-bp spacer clear (blind 3/3); proteobacteria not (label-free *E. coli* fails) |
| Fe–S cut 0.50, labelled genomes | **20 of 23** blind; misses: *Gluconobacter* (code error), *Fusobacterium*, *Treponema* (fermenters) |
| Methanogens vs aerobes | CxxC 3.4×, p = 6e-5 (L3117) |
| Zinc-finger counter | 8/8 human proteins within ±1 |
| dcf_secflag | recall 65% overall; 57% at GC < 0.45 blind; too many candidates (> 100 per genome even in AT-rich genomes) |

## 5. Known weaknesses
1. **Code decision.**
   - Two tests disagree occasionally; the length ratio inflates in medium-GC Proteobacteria with ~2/3 TGA stops.
   - **Fixed:** genomes > 2.5 Mb.
   - **Still unprotected:** genomes < 2.5 Mb with ratio > 1.6.
2. **Selenocysteine finder precision.** Hairpin-energy filtering (ViennaRNA) failed: AUC 0.60–0.69.
3. **Exact starts** in GC ≥ 0.65 genomes (~72–76%).
4. **Promoters** in Proteobacteria.

## 6. The blind-round protocol (copy this)
1. **Choose genomes.** Check them against `seen_accessions.txt` **and** grep earlier reports for the organism name. Verify each accession by web search, and note any you couldn't verify.
2. **Pre-register.** Write `PREREGISTERED_L####.txt` (genomes, labels, predictions, risks), take its SHA-256, and commit it to dcf-math `preregistrations/` plus `LEDGER.md` **before** links are sent.
3. **Send efetch links.** Gary zips them as `blind_N.zip`.
4. **Extract and match.** Unzip into a fresh `L####/in/`; match files by `^LOCUS       ACCESSION`; copy them to `g/ACC.gb`.
5. **Run the tools first.** Run the tools in parallel, write `tool_numbers.txt` and hash it, **then** read the annotation (e.g. `transl_except … aa:Sec`).
6. **Grade and report.** Grade, write `L####_report.md`, and zip the outputs (no genome files).
7. **Update the record.** Append the accessions to both seen lists, update the record in the dcf-math README and INTEGRATION, and push.

## Summary
- **The toolkit.** Six phone-sized tools in dcf-genefinder: gene finder v2.31 and five add-ons for grading, promoters, read-through (Pyl/Sec), metals and selenocysteine.
- **Strongest blind results:** genetic code 104/107; pyrrolysine 48/48; the Fe–S profile separates Fe–S-heavy anaerobes from aerobes (but not fermenting anaerobes).

## Potential leads for future research
- **[Code-3]** GC-adjusted length ratio (expected ratio from random sequence of the same GC); develop on the logged genomes, then test blind.
- **[Sec-3]** Upstream-part start-signal score as a precision filter for dcf_secflag.
- **[Fe-Cu 3]** A copper-site counter, validated on plastocyanin/azurin first.
- **[Note G update]** Fold v2.31, the code record 104/107 and the metal profile into `docs/NoteG_label_free_gene_finder_draft_v1.0.md`.
