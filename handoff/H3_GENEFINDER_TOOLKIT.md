# DCF Handoff 3 of 8: the genome toolkit (repo `xNOMEREMORTALx/dcf-genefinder`), "the DCF sequence reader"
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 24 November 2026 (after L3997)

**What it is.** A set of small, label-free Python tools: no Biopython and no internet; numpy where noted. They run on a phone (Pydroid 3) and on a computer.
- **They read raw DNA** (GenBank) to call genes, the genetic code, read-through amino acids, promoters, and the metal and energy profile.
- **They read proteins and mRNA** to sort nerve channels and pumps by ion, find cryptochromes, align sequences and place an mRNA on a chromosome.
- **It is not a lab sequencing machine.** It *reads* sequences that a sequencer has produced.

---

## 1. Tools (all MIT; "Not for medical use")
| tool | version / round | what it does | needs |
|---|---|---|---|
| `dcf_genefinder_mobile.py` | **v2.32** (L3229), SHA-256 `fa30258b…` | label-free spectral gene finder; automatic genetic code; learned start signal; GC-rich start fix | — |
| `dcf_grade.py` | L2993/L3069 | found / correct / exact start against the file's own annotation | — |
| `dcf_promoters.py` | L3049 | learns the genome's own −35/−10 boxes; E17 self-check | — |
| `dcf_pylflag.py` | L3073/L3089 | TAG/TGA read-through joins (pyrrolysine / selenocysteine genes) | — |
| `dcf_secflag.py` | L3161/L3197 | selenocysteine candidates; `--coding T` filter (AUC 0.87 in development) | — |
| `dcf_metals.py` | L3125/L3189 | CxxC (Fe–S) density, R, C2H2 zinc fingers; R-floor warning | — |
| `dcf_redox.py` | L3277, SHA-256 `4aecee5c…` | energy-metal profile: 3-3-4 ladder, CuA, zinc ribbon/knuckle, **four-tier energy call** (cuts 0.0045 / 0.023 / 0.060) | — |
| `dcf_motif_scan.py` | L3297/L3405 | protein-family motifs (hedgehog, voltage sensor, ladder, `ladder_p`, zinc …) | — |
| `dcf_exonmap.py` | L3297 | places an mRNA on a chromosome (exons, introns, strand) | — |
| `dcf_neurometal.py` | L3425 | sorts voltage-gated channels by the metal ion they pass | — |
| `dcf_k2p.py` | L3425 | K2P "leak" channels (anaesthetic targets) | — |
| `dcf_pump.py` | L3449 | P-type pumps by metal (Na/K, Ca, Cu) | — |
| `dcf_nerve.py` | **v3** (L3637), SHA-256 `2e5c56fd…` | nerve chemistry by metal; battery ratio; excitability kit; T-type Ca; Naₓ; sodium K/E letter | — |
| `dcf_align.py` | L3569 | global protein alignment (BLOSUM62) | numpy |
| `dcf_localalign.py` | L3585 | local alignment (Smith–Waterman) | numpy |
| `dcf_cryreader.py` | L3801/L3813/**L3829 (unreleased)** | cryptochrome/photolyase family (six references), TrpA–D chain, **family rule** (aromatic TrpD = cryptochrome-type) | numpy + both aligners |

**Supporting files:**
- `seen_accessions.txt` (201 genomes used);
- `seen_names.txt` (organism names used);
- `CHANGELOG.md`;
- `docs/NoteG_label_free_gene_finder_draft_v1.2.md`;
- `dev/` (the v2.32 candidates).

## 2. Usage (computer)
```
python3 -I dcf_genefinder_mobile.py genome.gb --table auto --out pred.gff3
python3 -I dcf_grade.py     genome.gb pred.gff3
python3 -I dcf_redox.py     genome.gb pred.gff3        # energy tier
python3 -I dcf_metals.py    genome.gb pred.gff3
python3 -I dcf_pylflag.py   genome.gb pred.gff3
python3 -I dcf_secflag.py   genome.gb pred.gff3 [--coding 0.05]
python3 -I dcf_promoters.py genome.gb pred.gff3
python3 -I dcf_nerve.py     proteins.fasta|mrna.fasta|uniprot.tsv
python3 -I dcf_cryreader.py proteins.fasta
```
**GenBank reader (all tools):** IUPAC letters become N, so coordinates stay aligned (fix L3069).

On the phone, these run through the bundle menus (H4 §3).

## 3. Blind records (unseen data, pre-registered)
| measure | record |
|---|---|
| **Genetic code** | **140 of 143** unseen genomes (L3241) |
| Genes found / correct | typically 86–95% found, 91–99% correct; level with Prodigal on precision, behind on sensitivity and starts (L3205) |
| Exact starts | v2.32 start fix: +2.2–2.3 points blind, no genome lost starts (L3213, L3229) |
| Pyrrolysine genes | **48/48** in 9 species |
| Energy tier (iron ladder) | **35 of 37** blind genomes, ρ = 0.962; protists with Ladder-P **10/10** |
| Nerve chemistry | **149 of 181** predictions in 29 blind tests; Na vs Ca: 4 swaps in 23,994 calls |
| Cryptochrome family rule | 2,527 / 2,564 (98.6%); 40/40 confident cryptochromes blind |
| Zinc-finger counter | 8/8 human proteins |

## 4. Known weaknesses (honest list)
1. **Code decision** in genomes < 2.5 Mb with an ORF-length ratio > 1.6 is unprotected.
2. **Selenocysteine finder:** too many candidates without the coding filter. Recall ~57% at GC < 0.45.
3. **Exact starts** in GC ≥ 0.65 genomes.
4. **Promoters:** label-free promoter calls fail in Proteobacteria.
5. **README version line:** corrected to 2.32 on 24 November 2026.
6. **Fragments:** gene fragments hide genes in nerve-channel absence calls (rules 4–6).

## 5. The blind-round protocol (copy this)
1. **Choose data.** Check against `seen_accessions.txt` **and** `seen_names.txt`, and grep earlier reports for the organism name.
2. **Pre-register** `PREREGISTERED_L####.txt` with predictions, risks and controls. Hash it into `LEDGER.md`, then commit and push **before** links are sent.
3. **Send links.**
   - **NCBI efetch:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=ACC&rettype=gbwithparts&retmode=text`.
   - **ENCODE direct downloads:** `https://www.encodeproject.org/files/ENCFF…/@@download/ENCFF….bedpe.gz`.
   - **UniProt:** stream/TSV links.

   Gary zips and attaches them.
4. **Extract and match.** Unzip into a fresh `L####/d/` directory and identify each file by its content.
5. **Run first.** Run the tools, commit the tool output, **then** read labels or annotation and grade.
6. **Update the records.**
   - Add an audit entry (`rounds/L3485_audit2.py`) and the round report.
   - Update the seen lists.
   - Note README/CHANGELOG changes if code changed.
   - Commit and push.

## 6. Ideas to make it a better "sequence reader" (see also H8)
- **[dcf_anchor]** Package the chromatin matched-gene test (H2 §B5) as `dcf_anchor.py`. Input: a gene list, loops/peaks files and a GTF. Output: the excess, the null, p-values and the partner fraction.
- **[Code-3]** A GC-adjusted ORF-length ratio for the code decision.
- **[Long reads]** Test the gene finder on raw nanopore-assembled genomes. Accuracy on error-rich assemblies is unknown.
- **[Metagenome bins]** Run the energy-tier call on metagenome-assembled genomes. That gives an energy-lifestyle reading for unculturable microbes.
- **[Release v1.3.0]** Ship the cryreader family-rule change, which is already committed and unreleased.

## Summary
- **Sixteen phone-sized tools** read DNA, mRNA and proteins label-free.
- **Strongest blind results:** genetic code 140/143, pyrrolysine 48/48, the energy-tier ladder 35/37, nerve chemistry 149/181, and the cryptochrome family rule at 98.6%.
- **The protocol:** freeze, hash, run and commit, then grade.

## Potential leads for future research
- **[dcf_anchor tool]**, **[Code-3]**, **[Long reads]**, **[Metagenome bins]** and **[v1.3.0 release]**, as above.
