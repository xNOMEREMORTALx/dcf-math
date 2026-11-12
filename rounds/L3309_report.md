# DCF L3309: a start-codon rule from ribosome biology (the Kozak −3 purine) fixes SHH in development; a fair test against NCBI's own protein sequences is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Lead:** [ORF start], from L3305. The longest-reading-frame rule started SHH three codons early (465 aa instead of 462), which moved every reported position by 3.

**Pre-registration:** `PREREGISTERED_L3309_orfstart.txt` (`290b44cd…c2e2`) and the script `dcf_orfstart_L3309.py`, pushed before any answer-key file is downloaded.

---

## 1. The rule
- **Rule A (current tools):** take the longest ATG-to-stop frame from its first ATG.
- **Rule K (new):** use the same frame and stop, but walk its in-frame ATGs from the 5′ end and take the first one with a **purine (A or G) three bases before the ATG**. This is the strongest part of the Kozak context that ribosomes use to choose where to start. If no such ATG lies in the first 100 codons, the first ATG is kept.

**Development (4 proteins with known lengths):**
| mRNA | true length | rule A | rule K |
|---|---|---|---|
| human SHH | 462 | 465 (M-G-E-M…) ✗ | **462 (M-L-L-L…)** ✓ |
| human DHH | 396 | 396 ✓ | 396 ✓ |
| mouse Shh | 437 | 437 ✓ | 437 ✓ |
| human IHH | 411 | 411 ✓ | 411 ✓ |

In SHH the false upstream ATG has **T** at −3, and the real start has **G**.

## 2. The test [pre-registered]
- **Answer key:** NCBI's own human protein files. A true protein must end at the same stop codon, so it matches our reading frame as a **suffix**. No annotation is needed to pair them.
- **Test set:** all four human RNA files we already hold.

| id | prediction |
|---|---|
| K1 | rule K is exactly right more often than rule A |
| K2 | where rule A is too long, rule K is exactly right in ≥ 50% |
| K3 | cases rule K breaks are at most half the cases it fixes |

**The risk is real:** a minority of human genes start at an ATG with a pyrimidine at −3, and rule K will move those wrongly. K3 measures that cost.

## Action for Gary
From https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/ download **`human.1.protein.faa.gz`** and **`human.2.protein.faa.gz`**, then zip them together as **`human_protein_1_2.zip`**. They are the protein files in the same folder as the RNA files you sent before.

## Record
No predictions graded this round. **309 of 439 passed, plus 3 split.**

## Summary
- **A biologically grounded fix for the start-codon problem:** prefer the first ATG with A or G three bases upstream, as ribosomes do. It corrects SHH to its true 462 amino acids and leaves IHH, DHH and mouse Shh unchanged.
- **A fair, large test is frozen:** NCBI's own human protein sequences will show whether the rule helps more than it hurts across thousands of genes.

## Potential leads for future research
- **[ORF start]** Grade K1–K3; if the rule passes, build it into the motif scanner, the neuro and hedgehog tools and phone menu 32.
- **[Kozak +4]** If K3 shows many breaks, test adding the second Kozak feature (G at +4) as a tie-breaker, on development data only first.
- **[Exon conservation]** Human–mouse exon-length conservation on PAX6, OTX2 and FOXG1 (needs verified coordinates and slices).
