# Data and code: iron-ladder manuscript (v0.11)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework

This file maps every table and figure in `notes/Manuscript_FeS_ladder_draft_v0.9.md` to the script that produced it, the frozen pre-registration, and the committed raw output. SHA-256 hashes of every frozen script are in `preregistrations/LEDGER.md`.

## Tools (repository `dcf-genefinder`)
| file | role |
|---|---|
| `dcf_genefinder_mobile.py` (v2.32) | label-free gene calls from GenBank nucleotide sequence (writes `.gff3`) |
| `dcf_redox.py` | per-genome ladder (overlapping), CxxC, CuA, zinc ribbon, tier call |
| `dcf_motif_scan.py` | protein/mRNA/genome motif scanner; presets `fd_ladder` (non-overlapping, frozen), `fd_ladder_ov`, `ladder_p` |
| `seen_accessions.txt`, `seen_names.txt` | every genome used, checked before each blind test |

**Typical run (prokaryote):**
```
python3 -I dcf_genefinder_mobile.py genome.gb --table auto --out genome.gff3
python3 -I dcf_redox.py genome.gb genome.gff3
```

## Manuscript items → scripts → data (repository `dcf-math`)
| manuscript item | pre-registration | script | committed output |
|---|---|---|---|
| §3.1 lineage pairs | `PREREGISTERED_L3237.txt` | `rounds/dcf_ladder_L3237.py` | `rounds/L3241_report.md` |
| §3.2 blind_20 tiers | `PREREGISTERED_L3265_blind20.txt` (+ amendment) | `rounds/dcf_ladder_L3237.py` | `rounds/L3269_tool_numbers.txt`, `rounds/L3273_tool_numbers_gasseri.txt` |
| §3.2 blind_21 controls, §3.6 rubredoxin | `PREREGISTERED_L3281_blind21.txt` | `rounds/dcf_rubredoxin_L3281.py` | `rounds/L3285_tool_numbers.txt` |
| §3.2–3.3 blind_22 photosynthesis | `PREREGISTERED_L3289_blind22.txt` | `dcf_redox.py` | `rounds/L3293_tool_numbers.txt` |
| §3.2, §3.4 blind_23 + small-ferredoxin comparison | `PREREGISTERED_L3321_blind23.txt` | `rounds/dcf_campbell_L3321.py` | `rounds/L3333_tool_numbers.txt` |
| §3.2 totals, Figure 3, number audit | — | `figures/L3341_all_blind.py` | `rounds/L3341_audit.txt` |
| §3.5 mechanism, Figure 2 (development) | — | `rounds/L3329_enzyme_map5.py` | `rounds/L3329_fam_counts.json` |
| §3.6 iron vs zinc, Figure 1 | `PREREGISTERED_L3273_zinc.txt` | `rounds/dcf_zinc_ribbon_L3273.py` | `rounds/L3273_zinc_ribbon.txt` |
| §3.7 protists (first set) | `PREREGISTERED_L3345_eukaryotes.txt` (+ amendment) | `dcf_motif_scan.py` (`fd_ladder`) | `rounds/L3353_protist_scan.txt`, `rounds/L3357_trichomonas_scan.txt` |
| §3.7 eukaryote cut | `PREREGISTERED_L3361_eukscale.txt` | `dcf_motif_scan.py` (`fd_ladder`) | `rounds/L3365_protist2_scan.txt` |
| §3.7 Ladder-P | `PREREGISTERED_L3397_ladderp.txt` | `rounds/dcf_ladderp_L3397.py` | `rounds/L3401_ladderp_output.txt` |
| §3.7 all 24 protists, Figure 4 | L3397, L3413 (blind part) | `rounds/dcf_ladderp_L3397.py`, `figures/L3421_protists_ladderp.py` | `rounds/L3421_all24_ladderp.txt` |
| §3.7 proline fingerprint (development) | — | `rounds/L3373_proline_dev.py` | `rounds/L3373_report.md` |
| §5 failures | as listed in §5 | as listed | round reports L3213, L3241, L3257, L3273, L3285, L3293, L3353, L3365 |

## Input data
- **Genomes:** public NCBI RefSeq records. Accessions are in each pre-registration file and in `seen_accessions.txt`.
- **Protist proteomes:**
  - Ensembl Protists `pep.all.fa.gz` (*Giardia*, *Entamoeba histolytica*, *Dictyostelium*, *Phytophthora*, *Thalassiosira*, *Tetrahymena*);
  - UniProt reference proteomes (UP IDs in `PREREGISTERED_L3361_eukscale.txt`, `PREREGISTERED_L3397_ladderp.txt`; *Trichomonas* UP000001542).
- **Raw genome files are not redistributed;** they can be re-downloaded from the accessions.

## Reproducing a blind test
1. Read the pre-registration and check the script's SHA-256 against `preregistrations/LEDGER.md`.
2. Download the listed accessions.
3. Identify each file by its LOCUS/DEFINITION line.
4. Run the script.
5. Compare with the committed output file.

## Permanent identifiers
Before submission, both repositories should be released on Zenodo. The DOIs replace Git URLs in the manuscript.

Not for medical use.
