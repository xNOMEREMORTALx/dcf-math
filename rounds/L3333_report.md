# DCF L3333: blind_23 passes 3 of 3; the scale places 12 of 12 fresh genomes, and large-enzyme ladders separate the middle tiers where small-ferredoxin counts cannot (5.3× vs 0.99×)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:** `blind23.zip`. All 12 pre-registered genomes, matched by LOCUS and DEFINITION (*Ralstonia* is now named *R. pseudosolanacearum*). Four old blind_22 files in the same zip were set aside unused.

**Pre-registration:** `PREREGISTERED_L3321_blind23.txt` (`2e986e01…4cf8`); script `dcf_campbell_L3321.py` (hash `ae13f196…` matches the ledger).

**Tool numbers** were committed (SHA-256 `f0219ac6…186f`) before grading or reading any annotation.

---

## 1. Results
| tier (fixed in advance) | genome | whole ladder | large-protein ladders | small Fd genes /1000 genes |
|---|---|---|---|---|
| 1 lactic | *Lactobacillus helveticus* | 0.0000 | 0.0000 | 0.00 |
| 1 lactic | *Streptococcus mitis* | 0.0000 | 0.0000 | 0.00 |
| 1 lactic | *Weissella koreensis* | 0.0000 | 0.0000 | 0.00 |
| 2 O₂ | *Bacillus pumilus* | 0.0067 | 0.0067 | 0.00 |
| 2 O₂ | *Rhizobium etli* | 0.0121 | 0.0081 | 0.72 |
| 2 O₂ | *Ralstonia pseudosolanacearum* | 0.0202 | 0.0163 | 0.92 |
| 3 H₂ fermenters | *Clostridium cellulovorans* | 0.0361 | 0.0320 | 0.72 |
| 3 H₂ fermenters | *Clostridium novyi* | 0.0510 | 0.0482 | 0.45 |
| 3 H₂ fermenters | *Thermosipho melanesiensis* | 0.0552 | 0.0431 | 2.15 |
| 4 Fd-based | *Acetohalobium arabaticum* | 0.0963 | 0.0805 | 2.71 |
| 4 Fd-based | *Desulfobacca acetoxidans* | 0.1314 | 0.1076 | 4.38 |
| 4 Fd-based | *Methanocella paludicola* | 0.1361 | 0.0958 | 5.83 |

| id | prediction | result | verdict |
|---|---|---|---|
| **C1** | ρ(tier, large-protein ladders) > ρ(tier, small ferredoxin genes) | **0.978 vs 0.868** | **PASS** |
| **C2** | O₂ → H₂ tier: large-protein ladders ≥ 2× and small ferredoxin genes < 2× | **5.3×** (0.0081 → 0.0431) vs **0.99×** (0.723 → 0.718) | **PASS** |
| **C3** | whole ladder ≥ 9 of 12 in the right tier | **12 of 12** (ρ = 0.978) | **PASS** |

The genetic code was correct in 12 of 12 (table 11); the code record is now **186 of 189**.

## 2. Reading
- **The best blind result in the Fe–S line:** every genome landed in its tier, and the tiers don't overlap. Lactic 0.000; O₂ 0.007–0.020; H₂ fermenters 0.036–0.055; Fd-based 0.096–0.136.
- **What our method adds beyond Campbell 2019, now shown blind:** counting small ferredoxin genes cannot tell oxygen respirers from hydrogen fermenters (0.72 vs 0.72 per 1,000 genes). The ladders inside large energy enzymes separate them 5.3-fold.
- **Running total:** across all blind genomes given a four-tier label in advance, the frozen cuts placed **35 of 37** correctly:
  - blind_20: 14/16;
  - blind_21 controls: 4/4;
  - blind_22 phototrophs: 5/5;
  - blind_23: 12/12.

  Low-oxygen sets labelled by lifestyle are reported separately (they failed as a band).
- Note H is now **v0.8**, with this as §4d-ter.

## Record
**This round:** 3 graded, 3 passed.

**Total: 312 of 445 pre-registered predictions passed, plus 3 split.**

## Summary
- **A clean sweep:** all 12 fresh microbes landed in the right energy tier, with no overlap between tiers.
- **The comparison with the 2019 method passed blind.** Counting small ferredoxin genes, as the earlier study did, can't separate oxygen breathers from hydrogen fermenters (identical values). The iron ladder in large enzymes separates them more than 5-fold.
- **Across all blind tests so far, the four-tier scale has placed 35 of 37 labelled genomes correctly.** Note H is at v0.8 and ready for a methods draft.

## Potential leads for future research
- **[Methods draft]** Write the Note H methods section and assemble a submission-style draft (abstract, results with Figures 1–2, methods, the pre-registration ledger as supplementary data).
- **[Bifurcation marker]** A label-free tier-4 marker (ladder plus FAD-binding G-x-G-x-x-G in one protein); develop on seen genomes, then pre-register.
- **[Eukaryote check]** Do anaerobic eukaryotes (*Giardia*, *Trichomonas*, *Entamoeba*, which use PFOR and ferredoxin) read high on the ladder, and aerobic ones low? A first step outside bacteria and archaea.
