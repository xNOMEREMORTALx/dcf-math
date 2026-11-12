# DCF L3321: the 2021 ferredoxin survey is not overlapping work; development shows the energy signal lives in ferredoxin domains inside large enzymes, which small-ferredoxin counts miss; blind_23 frozen to test it
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Leads pursued:** [Lit-redox c] (page approved by Gary), [Campbell comparison].

**Pre-registration:** `PREREGISTERED_L3321_blind23.txt` (`2e986e01…4cf8`) and the script `dcf_campbell_L3321.py`, pushed before download.

---

## 1. [Lit-redox c] Nzuza *et al.* 2021, *Curr. Issues Mol. Biol.* 43(3):1374–1390
- **What they did:** mined 468 genomes (241 Alphaproteobacteria, 227 Firmicutes), all **chosen because they carry P450 enzymes**, and classified ferredoxins by cluster type. They used variable cysteine-spacing motifs, e.g. 4Fe-4S C-x₂₋₅-C-x₂₋₃-C-x₃₀₋₄₅-C-P.
- **What they did not do:** classify genomes by fermentation, respiration, autotrophy or photosynthesis, or measure oxygen use. Their "4Fe-4S in anaerobes" statements cite Campbell 2019.
- **Verdict: not overlapping prior art** for the energy-tier scale. Note H v0.6 §4e is updated.

**Literature position of Note H (complete for now):**
- Andreini 2017: Fe–S proteins vs oxygen;
- Campbell 2019: small ferredoxins vs oxygen tolerance;
- Nzuza 2021: ferredoxin types in P450 genomes;
- no prior work sorts raw genomes into energy-metabolism tiers from one motif.

## 2. [Campbell comparison] Where does the signal live? [development, blind_20 genomes now seen]
| measure | ρ with tier | median: lactic / O₂ / H₂ ferm / Fd-based | O₂ → H₂ fermenters |
|---|---|---|---|
| whole-proteome ladder (/1000 aa) | **0.958** | 0.0020 / 0.0148 / 0.0434 / 0.1279 | **2.9×** |
| ladders in large proteins > 200 aa | **0.958** | 0.0020 / 0.0117 / 0.0338 / 0.0988 | **2.9×** |
| small ferredoxin genes ≤ 200 aa (/1000 genes, Campbell-style) | 0.843 | 0 / 0.86 / 1.07 / 4.53 | 1.25× |
| ladders in small proteins (/1000 aa) | 0.880 | 0 / 0.0038 / 0.0059 / 0.0247 | 1.6× |

**Reading.**
- **About three quarters of all ladders sit in large proteins:** hydrogenases, CODH, PFOR, heterodisulfide reductase and other enzymes with built-in ferredoxin domains.
- **That part separates oxygen respirers from hydrogen fermenters about 3-fold; small ferredoxins barely do (1.25×).**
- Both approaches see the extremes (lactic fermenters have none; tier 4 has many). **Only the whole-proteome view resolves the middle tiers.** This is the contribution beyond Campbell 2019, and it needs a blind test.

## 3. blind_23 [pre-registered]
| tier | genomes |
|---|---|
| 1 lactic | *Lactobacillus helveticus*, *Streptococcus mitis*, *Weissella koreensis* |
| 2 O₂ | *Ralstonia solanacearum* chr, *Rhizobium etli* chr, *Bacillus pumilus* |
| 3 H₂ fermenters | *Clostridium novyi*, *Thermosipho melanesiensis*, *Clostridium cellulovorans* |
| 4 Fd-based | *Methanocella paludicola*, *Desulfobacca acetoxidans*, *Acetohalobium arabaticum* |

| id | prediction |
|---|---|
| C1 | ρ(tier, large-protein ladders) > ρ(tier, small ferredoxin genes) |
| C2 | from O₂ to H₂ tier: large-protein ladders ≥ 2× **and** small ferredoxin genes < 2× |
| C3 | the whole ladder puts ≥ 9 of 12 in the right tier (a third replication of the scale) |

## Action for Gary: blind_23 (12 links)
Zip all 12 as **`blind_23.zip`**. These are large GenBank files, about 3–15 MB each; sort Download by newest first to pick them.

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_010080
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_013853
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_015759
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_003295
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007761
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009848
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008593
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009616
9. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_014393
10. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_013665
11. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_015388
12. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_014378

## Record
No predictions graded this round. **309 of 442 passed, plus 3 split.**

## Summary
- **The 2021 ferredoxin survey doesn't overlap ours:** it classified ferredoxin types in genomes chosen for P450 enzymes and never sorted them by how they make energy. The literature check for the iron note is complete for now.
- **New development result:** most of the iron ladder sits inside large enzymes. That part tells oxygen breathers from hydrogen fermenters about 3-fold, whereas counting small ferredoxin genes, the older method, barely can (1.25-fold).
- **blind_23 is frozen** to test this on 12 fresh microbes, and to replicate the four-tier scale a third time.

## Potential leads for future research
- **[blind_23]** Grade C1–C3 when the zip arrives.
- **[Note H draft]** If C1–C2 pass, the note has a clear "what's new" section and is ready for a methods draft (Figure 1 iron vs zinc, Figure 2 small vs large proteins).
- **[Enzyme map]** Name which large-enzyme families carry the tier-3/4 ladders (hydrogenase, PFOR, CODH, Hdr), using annotation only after hashing.
