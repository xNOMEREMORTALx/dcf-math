# DCF L3205: the gene finder head-to-head with Prodigal — level on precision, behind on sensitivity and starts
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [Submission G], [R5e].

**Still waiting:** `blind_16.zip` (6 links in `L3189_report.md`) and `blind_17.zip` (8 links in `L3197_report.md`).

---

## 1. [Submission G] DCF v2.31 vs Prodigal on 10 genomes
**Setup.**
- The 10 genomes of blind sets 14–15, now seen.
- Both tools graded by the same `dcf_grade.py` against each file's own annotation.
- Prodigal run through **pyrodigal 3.7.1** (single-genome mode, table 11).

| genome | DCF found / correct / exact start | Prodigal found / correct / exact start |
|---|---|---|
| *Bordetella bronchiseptica* (GC 0.68) | 95.3 / 99.1 / 79.0 | 98.7 / 99.3 / 88.9 |
| *Pseudomonas protegens* (0.63) | 92.8 / 97.4 / 83.3 | 98.3 / 99.0 / 92.8 |
| *Cupriavidus* chr 1 (0.66) | 92.2 / 98.6 / 80.0 | 97.3 / 98.8 / 89.8 |
| *Desulforapulum* (0.49) | 86.0 / 95.5 / 79.7 | 96.3 / 96.3 / 88.6 |
| *Hydrogenobacter* (0.44) | 93.0 / **99.2** / 81.1 | 98.5 / 99.1 / 92.7 |
| *Acetobacterium* (0.39) | 92.3 / 98.2 / 86.9 | 98.3 / 98.4 / 92.7 |
| *Leuconostoc* (0.38) | 92.8 / **98.8** / 90.0 | 98.9 / 98.4 / 94.4 |
| *S. mutans* (0.37) | 89.7 / 98.5 / 88.5 | 96.5 / 98.6 / 93.6 |
| *L. acidophilus* (0.35) | 90.7 / 98.6 / 88.7 | 97.7 / 98.9 / 93.2 |
| *C. ljungdahlii* (0.31) | 92.7 / **98.8** / 91.0 | 98.7 / 98.8 / 92.5 |
| **mean** | **91.8 / 98.3 / 84.8** | **97.9 / 98.6 / 91.9** |

**Reading.**
- **Precision is level.** DCF's calls are right 98.3% of the time against Prodigal's 98.6%, and DCF is equal or better in 3 of 10 genomes.
- **Sensitivity trails by about 6 points** (short genes, as in Note G §7).
- **Exact starts trail by about 7 points,** most in GC-rich genomes (79–83% vs 89–93%). The gap is smallest in AT-rich Firmicutes (*C. ljungdahlii*: 91.0 vs 92.5).
- **Caveat:** both tools are graded against NCBI's own predicted annotation, not experimental truth.
- This is now **Note G §3j** (dcf-genefinder, `docs/NoteG_label_free_gene_finder_draft_v1.1.md`).

**A grader correction found on the way.** L3185 had quoted the gene finder's built-in comparison line, which uses a different grader. With `dcf_grade.py`, *L. acidophilus* "correct" is 98.6%, not 93.3%. Correction notes are added to the L3185 report and to Note G §3i. No prediction depended on these numbers.

## 2. [R5e] F₂₅ — blocked
- The repunit factor site served the wrong page for R₃₀₀₁ on three attempts (it returned R1501–1600 and R299901–300000).
- Without R₃₀₀₁'s known factors, the F₂₅ = 75025 minimum stays open.

## Record
No predictions graded. **264 of 344 passed, plus 3 split.**

## Summary
- **First like-for-like comparison with the standard gene finder.** On 10 genomes the DCF phone tool is as precise as Prodigal (98.3% vs 98.6% of calls correct). It finds about 6% fewer genes and gets about 7% fewer starts exactly right.
- **This is the honest headline for Note G:** equal precision from a numpy-only, self-training tool, with known gaps in sensitivity and starts.
- **A small grading inconsistency in L3185 was found and corrected;** no verdict was affected.
- **Biology leads are waiting on the two downloads.**

## Potential leads for future research
- **[Blind 16 + 17]** Grade Fe-rTCA, Fe-ferment H2 and Sec-3 when the zips arrive.
- **[G-starts]** Starts in GC-rich genomes are the largest gap (about 10 points). Develop on *Bordetella* / *Cupriavidus* / *Desulforapulum*, which are now seen, and test blind.
- **[G-compare all]** Run the same head-to-head on every future blind set, so the comparison grows with each round.
- **[Grader unify]** Make the gene finder's built-in comparison line call `dcf_grade.py`'s logic, so only one grader exists.
- **[R5e]** Retry R₃₀₀₁ later, or ask Gary to open the page (stdkmd.net, repunit table, page 31).
