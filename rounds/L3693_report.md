# DCF L3693: The NR1 score floor, calibrated on 41 named receptors (941; perfect separation, but thin on negatives); a trematode-vs-cestode sodium test is frozen with it
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [Floor calibration], [Fluke sodium loss]. Calibration and pre-registration. **No predictions graded.**

---

## 1. Calibration (`PREREGISTERED_L3693_nr1_calibration.txt` → `rounds/L3693_calibration_output.txt`)
**Method** (frozen before running):
- **Data:** every glutamate-receptor call nearest mouse Grin1, in every organism seen (50 calls).
- **Labels:**
  - **positive:** named NR1 / zeta-1 / Grin1 / Nmdar1;
  - **negative:** any other informative name;
  - **excluded:** unnamed or "domain-containing" entries (9).
- **The floor:** the threshold with the best balanced accuracy, with ties going to the lowest score.

| group | n | scores |
|---|---|---|
| **named NR1** | 38 | 953 … 4,874 (the lowest: *S. japonicum* 953; then 1,113, 1,294, 1,370 …) |
| **named non-NR1** | 3 | 459 (liver-fluke "iGluR"), 553 (coral ribosomal protein), 839 (tapeworm "Nmda type glutamate receptor") |

**Result: floor = 941. Balanced accuracy 1.0** (all 38 positives above, all 3 negatives below).

**Disclosures:**
- **Only 3 negatives.** The calibration is thin on that side; any floor from 840 to 953 separates the labelled data equally well.
- **The tie rule picked 941,** the lowest *observed* score in that gap. It belongs to an *unlabelled* call (*S. mansoni* A0A5K4F3J7, "ANF receptor domain-containing"), which now counts as NR1.
- **The tapeworm's "Nmda type glutamate receptor" (839) was labelled negative,** because its name does not say NR1. It could be a divergent NR1. The name rule decided, as frozen.

**New caller:** `rounds/dcf_nr1_L3693.py` (FLOOR = 941), hashed into the ledger. **It replaces the 1,000 floor in all future tests.**

**Descriptive effect on earlier organisms (no grade changes):**
- **Floor 941 restores NR1** in *S. mansoni* (941), *S. japonicum* (953) and the acoel's dropped call (962).
- **The blood flukes' kits become present again.**
- **The liver fluke** (best 459) and ***Macrostomum*** (648) stay without NR1.

## 2. Frozen test (`PREREGISTERED_L3697_trematode_cestode.txt`, `rounds/dcf_flatworm2_L3697.py`)
**The question:** is the loss of the sodium spike channel a fluke (trematode) trait?
- **Check on the seen *S. japonicum* (not a test):** NR1 1, NAV-family 0, kit present.

| # | organism | group | prediction |
|---|---|---|---|
| G1 | *Clonorchis sinensis* | fluke | 0 NAV-family |
| G2 | *Opisthorchis viverrini* | fluke | 0 NAV-family |
| G3 | *Paragonimus westermani* | fluke | 0 NAV-family |
| G4 | *Taenia asiatica* | tapeworm | ≥ 1 NAV-family |
| G5 | *Hymenolepis diminuta* | tapeworm | ≥ 1 NAV-family |
| G6 | all five | | NR1 (floor 941) in ≥ 3 |

**Download links** (zipping them works well):
1. ***Clonorchis*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000008909
2. ***Opisthorchis*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000054324
3. ***Paragonimus*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000324629
4. ***Taenia*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000282613
5. ***Hymenolepis*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000321570

## Record
No predictions graded. **486 of 660 passed, plus 3 split.** Nerve-chemistry audit **153 of 187.**

## Summary
- **The NR1 floor is now calibrated on named receptors instead of being a round number:**
  - **941:** all 38 named NR1s (as low as 953) sit above it, and all 3 named non-NR1s (up to 839) sit below.
  - **Caveats:** only 3 negatives, and the exact value was set by a tie rule at an unlabelled score.
- **The calibrated floor restores the divergent flatworm and acoel NR1s.**
- **A five-flatworm test is frozen with it,** asking whether flukes, and only flukes, lost the sodium spike channel.

## Potential leads for future research
- **[Trematodes vs cestodes]** Grade G1–G6 when the files arrive.
- **[More negatives]** Strengthen the calibration with more named non-NR1 Grin1-nearest calls as they appear in new organisms; recalibrate only by a new pre-registration.
- **[Manuscript 2]** §3.23 flatworms and §3.24 calibration; revise §3.22 for the floor change.
