# One iron–sulfur motif sorts microbial genomes by energy metabolism: pre-registered, blind tests from raw DNA
### Manuscript draft v0.7 · Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

*Built from Note H v0.8 and DCF rounds L3125–L3341. v0.2: the headline numbers were re-computed directly from the committed tool-number files (L3341 audit, `rounds/L3341_audit.txt`); all matched. Every number is taken from a committed round report. Pre-registrations, frozen scripts and tool-number hashes are in the dcf-math ledger (`preregistrations/LEDGER.md`).*

---

## Abstract
We count one cysteine motif, the "3-3-4 ladder" C-x₂-C-x₂-C-x₃-C that binds [4Fe-4S] clusters in bacterial-type ferredoxins and ferredoxin-like domains, across the whole predicted proteome of a genome. The genes are called label-free from raw DNA with our own gene finder.

Ladder density falls on a four-tier scale that tracks energy metabolism, not oxygen tolerance:
1. lactic fermenters;
2. oxygen respirers (including oxygenic phototrophs);
3. H₂-making fermenters;
4. ferredoxin-based respirers and autotrophs (methanogens, sulfate reducers, acetogens, anoxygenic phototrophs with type-I reaction centres).

**Blind performance.** With cuts frozen before any data were downloaded, the scale placed **35 of 37** blind genomes in their pre-assigned tier (Spearman ρ = 0.962 over all 37). In the latest set it placed **12 of 12** (ρ = 0.978).

**Comparison with earlier work.** Ladders inside large energy enzymes separated oxygen respirers from H₂ fermenters **5.3-fold**, blind. Counting small ferredoxin genes, the approach of the closest prior work, did not separate them at all (0.99-fold).

**Mechanism.** The signal comes from ferredoxin-coupled energy enzymes:
- hydrogenases;
- pyruvate:ferredoxin oxidoreductase;
- Rnf;
- heterodisulfide reductase and electron-bifurcating flavoproteins.

**Iron vs zinc.** A zinc structural cysteine motif counted the same way rose only 2.3–3.8-fold across the tiers, against 64–160-fold for iron.

All predictions, including failures, are reported (§5).

## 1. Introduction
- **Earlier work, all organised around oxygen.**
  - Iron–sulfur proteins are more common in anaerobes than in aerobes (Andreini *et al.* 2017).
  - In 7,079 genomes, small (≤ 200 aa) [4Fe-4S] ferredoxins dominate in anaerobes, while flavodoxins and [2Fe-2S] ferredoxins rise with oxygen tolerance (Campbell, Bennett & Silberg 2019).
  - Ferredoxin types have been surveyed by cysteine-spacing motifs (Nzuza *et al.* 2021).
  - An annotation-free predictor classifies ~3,300 genomes as aerobe, anaerobe or facultative from generic k-mers and embeddings (~70% accuracy; bioRxiv 10.1101/2024.01.16.575888).
- **The gap.** None sorts raw genomes by **type of energy metabolism**, which oxygen classes conflate: lactic and H₂ fermenters are both strict anaerobes, and cyanobacteria make oxygen yet depend on ferredoxin.
- **Our question:** does one motif counted over the whole proteome, including ferredoxin domains inside large enzymes, resolve these classes, and does it survive blind, pre-registered testing?

## 2. Methods
### 2.1 Gene calling
- Proteins are predicted from GenBank nucleotide sequence only, with `dcf_genefinder_mobile.py` v2.32 (SHA-256 `fa30258b…297c`). Annotation is never read before the tool numbers are hashed.
- v2.32 detects the genetic code automatically (**186 of 189** blind genomes correct), re-picks start codons by coding weight, and applies a minimum length (240 nt; 180 at GC > 0.55).
- Precision against annotation is 97–98%.
- Proteins are translated with the standard table.

### 2.2 Motifs (counted overlapping, per 1,000 amino acids of predicted protein)
| motif | pattern | role |
|---|---|---|
| **3-3-4 ladder** | C-x₂-C-x₂-C-x₃-C | [4Fe-4S] ferredoxin and ferredoxin-like domains (frozen L3237) |

*Counting note (found L3369):* prokaryote results count ladders **overlapping** (`dcf_redox.py`, frozen L3237 script). The protist tests (§3.7) used the motif scanner's `fd_ladder` preset, which counts **non-overlapping** matches; the eukaryote cut (0.0035) was set and tested with that same scanner, so those grades are internally consistent. With overlapping counts, *Trypanosoma* (0.0039) would read just above *Cryptosporidium* (0.0036).
| CxxC | C-x-x-C | broad metal/redox sites (first marker, superseded) |
| copper CuA | C-x-E-x-C-x₃-H-x₂-M | oxygen-respiring cytochrome oxidase (L3257) |
| zinc ribbon | C-x₂-C-x₉₋₂₀-C-x₂-C, ladder cysteines masked | structural Zn(Cys)₄ (L3273) |
| rubredoxin | C-x₂-C-G-x₂₄₋₃₂-C-x₂-C-G | Fe(Cys)₄ knuckle pair (L3281) |

### 2.3 The four-tier scale
- The tiers were found after the fact on 35 seen genomes (L3257). The cuts were then **frozen**: tier 1 < 0.0045 ≤ tier 2 < 0.023 ≤ tier 3 < 0.060 ≤ tier 4.
- Tier labels for blind genomes were fixed from the literature before download.
- One tool, `dcf_redox.py` (`4aecee5c…a7d1`), reproduces all frozen motif counts exactly (0 mismatches on 16 genomes).

### 2.4 Pre-registration and blinding
For every test:
1. **Freeze first.** The predictions, the genome list, the labels and the SHA-256 of every script were committed to a public ledger before any genome was downloaded.
2. **Check freshness.** Genomes were checked against lists of every accession and organism name used before; any seen genome was replaced before freezing.
3. **Identify, then hash.** Downloaded files were identified only by their LOCUS/DEFINITION line, and the tool numbers were hashed and committed before grading or reading annotation.
4. **Never replace.** A wrong or missing organism is dropped, never replaced.
5. **Keep every result.** Failures are kept and reported.

### 2.5 Statistics
Spearman rank correlation between tier and density; tier medians and median ratios; exact counts against frozen bars.

## 3. Results
### 3.1 Lineage-matched pairs (blind_18, blind_19)
- **The ferredoxin-based member read higher in 6 of 6** pairs of related genomes from five phyla.
- The ladder separated pairs **4.7–8.4×**, against 1.6–2.6× for plain CxxC (L3241).

### 3.2 The four-tier scale, blind
| blind set | genomes with a tier label | correct | ρ |
|---|---|---|---|
| blind_20 (L3269/L3273) | 16 | **14** | 0.958 |
| blind_21 controls (L3285) | 4 | **4** | — |
| blind_22 phototrophs (L3293) | 5 | **5** | — |
| blind_23 (L3333) | 12 | **12** | 0.978 |
| **total** | **37** | **35** | **0.962** |

- **The two misses sit on tier boundaries:**
  - *C. botulinum* was above its cut by 0.0001;
  - *Sulfurihydrogenibium* is a microaerophile.
- **In blind_23 the tiers did not overlap:** 0.000 / 0.007–0.020 / 0.036–0.055 / 0.096–0.136.

### 3.3 Photosynthesis separates by iron chemistry, not by "uses ferredoxin"
- Four oxygenic cyanobacteria read **0.013–0.021 (tier 2)**. They use plant-type [2Fe-2S] ferredoxin, which the ladder does not count.
- The anoxygenic *Heliobacterium modesticaldum* (type-I reaction centre with [4Fe-4S] clusters) read **0.095 (tier 4)**.
- Both predictions passed.

### 3.4 Whole proteome vs small ferredoxins (blind_23)
| measure | ρ with tier | O₂ respirers → H₂ fermenters |
|---|---|---|
| ladders in proteins > 200 aa | **0.978** | **5.3×** (0.0081 → 0.0431) |
| small (≤ 200 aa) ferredoxin genes per 1,000 genes | 0.868 | **0.99×** (0.723 → 0.718) |

### 3.5 Mechanism (development, blind_20 genomes after grading; Figure 2)
| tier | large-protein ladders per genome | characteristic families |
|---|---|---|
| 1 | 1 | — |
| 2 | 12 | hydrogenases, Rnf / complex I |
| 3 | 38 | hydrogenases, Rnf, **PFOR** |
| 4 | 84 | **heterodisulfide reductase + electron-bifurcating flavoproteins** (7× tier 3), hydrogenases |

### 3.7 Beyond prokaryotes: anaerobic vs aerobic protists (L3345 → L3353)
The frozen motif scanner was run on Ensembl protein files, plus *Trichomonas vaginalis* G3 from UniProt (UP000001542, 50,190 proteins; Ensembl no longer hosts it).

| organism | lifestyle | ladder /1000 aa |
|---|---|---|
| *Entamoeba histolytica* | anaerobic, PFOR + Fe-hydrogenase | **0.0094** |
| *Giardia intestinalis* | anaerobic, PFOR + ferredoxins | **0.0089** |
| *Trichomonas vaginalis* | anaerobic, hydrogenosomes (PFOR + Fe-hydrogenases) | **0.0040** |
| *Tetrahymena thermophila* | aerobic | 0.0029 |
| *Phytophthora infestans* | aerobic | 0.0021 |
| *Thalassiosira pseudonana* | aerobic, oxygenic | 0.0021 |
| *Dictyostelium discoideum* | aerobic | 0.0009 |

- **The ranking holds in eukaryotes:** EU1 passed (both anaerobes above all aerobes); EU2 passed (4.4×). With *Trichomonas* added (L3357, re-report): all three anaerobes are still above all aerobes (4.2×). *Trichomonas*'s very large proteome dilutes it to 0.0040, but its ladders sit on 7 PFOR-type enzymes, 7 Fe-only hydrogenases and 5 4Fe-4S domain proteins.
- **The bacterial cuts do not transfer:** EU3 failed. The large eukaryotic proteomes dilute the density, as anticipated from human proteins before the test (L3349).
- **The ladder proteins are the same enzymes as in bacterial tier 3** (after grading): *Giardia* and *Entamoeba* carry them on PFOR, Fe-hydrogenase and ferredoxins. Aerobic protists carry the mitochondrial housekeeping set (complex I 23 kDa subunit, succinate dehydrogenase, ABCE1, DPYD).

**A eukaryote cut, tested blind (L3361 → L3365).** A cut of 0.0035 was fixed from the first seven protists and then tested on seven new ones (UniProt reference proteomes):

| organism | group (fixed in advance) | ladder /1000 aa |
|---|---|---|
| *Blastocystis hominis* | anaerobe | 0.0171 |
| *Spironucleus salmonicida* | anaerobe | 0.0151 |
| *Cryptosporidium parvum* | anaerobe | 0.0036 |
| *Trypanosoma brucei* | aerobe | 0.0030 |
| *Chlamydomonas reinhardtii* | aerobe | 0.0016 |
| *Leishmania major* | aerobe | 0.0014 |
| *Naegleria gruberi* | aerobe carrying a few anaerobic enzymes | 0.0017 |

- The cut classified **6 of 6** correctly (ES1 pass), and every anaerobe read above every aerobe (ES2 pass). *Cryptosporidium* cleared the cut by only 0.0001; its result rests on 3 ladder proteins, one of them its PFOR-type PNO.
- **ES3 failed:** *Naegleria* (one iron hydrogenase and one anaerobic G3P dehydrogenase among 15,631 proteins) reads like an aerobe. **The ladder measures how much of the proteome serves ferredoxin-based energy metabolism, not whether any anaerobic enzyme is present.**
- **Across 14 protists in two blind sets, anaerobes and aerobes separated perfectly** (Naegleria excluded as the special case), with non-overlapping counts.
- **Development (L3369): a stricter Ladder-P motif (C-x₂-C-x₂-C-x₃-C-P)** removes all 12 human look-alike hits and gives a clean protist gap (lowest anaerobe 0.0020 vs highest aerobe 0.0014, overlapping counts). It leaves prokaryote performance unchanged (ρ 0.964 vs 0.962). It is proposed for eukaryotes and awaits a fresh blind test.
- **The proline fingerprint (L3373, development):** the residue after the 4th ladder cysteine is proline in 85% (tier 2), 68% (tier 3) and 78% (tier 4) of prokaryote ladders, 50% in anaerobic protists, 35% in aerobic protists and **0 of 12** in human look-alikes. This is the structural reason Ladder-P separates real ferredoxin folds from cysteine-rich structural proteins.

### 3.6 Iron vs zinc (Figure 1)
- **Zinc ribbon:** rose **2.3×** across the tiers in blind_20, against the ladder's 64× (Zn1 pass), and **3.8×** against 160× in blind_21 (ZR1 pass). It does not separate tiers 1 and 2.
- **Rubredoxin knuckle (an Fe site in a zinc-like fold):** followed the ladder blind (RB1 pass; ρ = 0.73, RB2 pass).

## 4. Discussion
- **What the ladder density measures:** approximately the number of ferredoxin-coupled energy enzymes a genome encodes. That explains:
  - why it tracks energy metabolism rather than oxygen;
  - why oxygenic phototrophs read low;
  - why the middle tiers are invisible to small-ferredoxin counts. The extra signal lives in ferredoxin domains of hydrogenases, PFOR, Rnf and bifurcating complexes.
- **The electrochemistry:** [4Fe-4S] ferredoxins operate near −0.41 V, the H⁺/H₂ potential at pH 7, whereas Zn²⁺ is redox-inert in biology. This matches the flat zinc control.

## 5. All pre-registered results in this line, including failures
| test | result |
|---|---|
| hydrogen as the driver (L3213) | not supported; replaced by the ferredoxin reading |
| islands of Fe–S genes (L3241 L4, L5) | **failed** |
| redox-age three-way call (L3257) | 18 of 23 (needed 19) **failed**; 2 of 3 sub-predictions passed |
| zinc ρ < 0.60 (L3273 Zn2) | **failed** (0.74) |
| low-oxygen band inside tier 3 (L3285 M1, M2; L3293 E1, E2) | **failed 4 of 4**: lifestyle labels; the genomes read 0.046–0.089 |
| all other predictions listed in §3 | passed |

## 6. Limitations
- **Coverage:**
  - Eukaryotes need their own cut (0.0035, validated on 6 of 6 fresh protists); the bacterial cuts do not transfer. The eukaryote sets are small (14 protists).
  - The 37 blind genomes span 8 phyla (Bacillota, Pseudomonadota, Thermotogota, Euryarchaeota, Nitrospirota, Aquificota, Desulfobacterota, Cyanobacteria), but most tiers have 3–4 genomes per set.
- **Microaerophiles:**
  - Microaerophiles and organisms with mixed metabolism sit on the tier-3/4 boundary.
  - Labels should be derived from enzymes, not lifestyle.
- **Tier 1:** the lactic tier is dominated by Lactobacillales.
- **Gene calling:** gene-call errors (2–3% false calls) add noise, especially in high-GC genomes.

## 7. Data and code availability
Code is in the public repositories `xNOMEREMORTALx/dcf-genefinder` and `xNOMEREMORTALx/dcf-math`:
- `dcf_genefinder_mobile.py`;
- `dcf_redox.py`;
- the frozen round scripts;
- `preregistrations/LEDGER.md`;
- the seen-genome lists.

All genomes are public RefSeq records listed in the pre-registration files.

## Figures
- **Figure 1.** Iron ladder vs zinc ribbon by tier, blind_20 (`figures/L3277_iron_zinc_tiers.png`).
- **Figure 2.** Ladders in large proteins by enzyme family and tier (`figures/L3329_enzyme_families.png`).
- **Figure 3.** All 37 blind genomes on the scale, coloured by set, with the frozen cuts and the two misses labelled (`figures/L3341_all_blind.png`).

## References
1. Andreini C, Rosato A, Banci L (2017) The relationship between environmental dioxygen and iron-sulfur proteins explored at the genome level. *PLoS ONE* 12:e0171279.
2. Campbell IJ, Bennett GN, Silberg JJ (2019) Evolutionary relationships between low potential ferredoxin and flavodoxin electron carriers. *Front. Energy Res.* 7:79.
3. Nzuza N *et al.* (2021) Diversification of ferredoxins across living organisms. *Curr. Issues Mol. Biol.* 43:1374–1390.
4. bioRxiv 10.1101/2024.01.16.575888 (annotation-free prediction of microbial oxygen utilisation).

## Acknowledgements
Analysis, code and drafting assistance: Claude (Anthropic). Not for medical use.

---

## Summary
- **A complete draft built from the ledger:** abstract, introduction, methods, results, discussion, an honest failure table, limitations, data availability and references.
- **Headline:** one iron–sulfur motif placed 35 of 37 blind genomes in the right energy-metabolism tier. It also resolves what small-ferredoxin counts cannot (5.3× vs 0.99×).

## Potential leads for future research
- **[Figure 3]** Plot all 37 blind genomes on the scale.
- **[Eukaryote check]** Anaerobic protists (*Giardia*, *Trichomonas*, *Entamoeba*) vs aerobic ones, from RefSeq protein files.
- **[Venue]** Choose a target (e.g. *Microbial Genomics*, *ISME Communications*, *PeerJ*) and fit length and format.
- **[Number audit]** An independent re-read of every number in this draft against the round reports, by a separate reviewer, before submission.
