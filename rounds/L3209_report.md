# DCF L3209: why the gene finder misses starts in GC-rich genomes, and a fix (+2.4 points held-out, +5 in GC-rich) frozen for a blind test
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Lead pursued:** [G-starts] (L3205 found exact starts about 7 points behind Prodigal, worst in GC-rich genomes).

**Pre-registration:** `PREREGISTERED_L3209.txt`, SHA-256 `179e7593f1905ac39dedb6315ece61616cb2535742f3d87b93c7b495a0663afa`, commit `162fc6a`, pushed before blind_16/17 are downloaded.

**Still waiting:** `blind_16.zip` and `blind_17.zip`. This round adds one more test to grade on them.

---

## 1. Diagnosis [development, blind_14/15 genomes]
**Method.** For every gene whose stop the finder gets right but whose start is wrong, I checked the direction of the error and which start codon was involved.

| genome | GC | exact | too long | **too short** | of the misses, Prodigal exact |
|---|---|---|---|---|---|
| *Bordetella* | 0.68 | 79.0% | 309 | **703** | 59% |
| *P. protegens* | 0.63 | 83.3% | 426 | **557** | 67% |
| *Cupriavidus* | 0.66 | 80.0% | 308 | **389** | 63% |
| *Desulforapulum* | 0.49 | 79.7% | 304 | **555** | 57% |
| *C. ljungdahlii* | 0.31 | 91.0% | 121 | **234** | 44% |

**Errors are mostly "too short":** the finder picks a start downstream of the real one. The commonest pattern is annotated **ATG** replaced by a downstream **TTG or GTG** (*Bordetella*: ATG → TTG 193, ATG → GTG 112).

**The cause.** The learned start-codon weights come from the tool's own earlier picks, so they are circular. They penalise TTG and GTG too little. Together with the coding-score term, that lets a later rare start win.

## 2. Fix and development test
**The change.** Two parameters in the learned start re-pick:
- weight the coding term by 0.75 instead of 1;
- add fixed penalties of **GTG −4 and TTG −5** to the learned codon scores.

**Procedure.**
1. Every candidate's score parts were dumped once per genome.
2. 240 settings were swept offline.
3. The settings were checked **leave-one-genome-out:** tuned on 7 genomes, scored on the 8th.

| held-out genome | v2.31 | tuned without it |
|---|---|---|
| *Bordetella* | 79.0 | **84.0** |
| *P. protegens* | 83.3 | **88.0** |
| *Cupriavidus* | 80.0 | **84.6** |
| *Desulforapulum* | 79.7 | **82.4** |
| *A. woodii* | 86.9 | 88.3 |
| *Hydrogenobacter* | 81.1 | 82.0 |
| *L. acidophilus* | 88.8 | 89.1 |
| *C. ljungdahlii* | 91.0 | 90.9 |
| **mean gain** | | **+2.4** (worst −0.1) |

**Full-run check** (the offline sweep skips the relearning pass):
- *Bordetella* **79.0 → 84.7**;
- *Desulforapulum* 79.7 → 82.3;
- *C. ljungdahlii* 91.0 → 91.1.

Genes found and correct were unchanged (± 0.1).

**This closes about half to three quarters of the start gap to Prodigal in the GC-rich genomes** (*Bordetella*: Prodigal 88.9).

## 3. What is frozen
- **Candidate file:** `dev/dcf_genefinder_v2.32_candidate.py` (dcf-genefinder), SHA-256 `e2e9c793…d42a`. It is **not** the released tool; v2.31 stays the default.
- **Blind test on blind_16 + blind_17:**
  - **T1:** mean exact-start gain ≥ +1.0 point.
  - **T2:** no genome loses more than 1.0 point.
  - **T3:** found and correct move by less than 0.5 point.
- **Declared risk:** lineages that genuinely use many GTG/TTG starts. None of these was in development.

## Record
No predictions graded. **264 of 344 passed, plus 3 split.**

## Summary
- **The start errors have one main cause.** In GC-rich genomes the gene finder too often picks a rare start codon (TTG or GTG) downstream of the true ATG, because it learned its start-codon preferences from its own earlier choices.
- **Adding fixed penalties for the rare codons** raised exact starts by 2.4 points on genomes held out from tuning, and by about 5 points in GC-rich ones, with no loss elsewhere.
- **The change is frozen as a candidate.** It will be tested blind on the next two downloads before it replaces the released version.

## Potential leads for future research
- **[Blind 16 + 17]** Grade Fe-rTCA, Fe-ferment H2, Sec-3 and now G-starts (T1–T3) together.
- **[G-starts b]** Find a genome set rich in genuine GTG starts (e.g. some Actinobacteria) for a regression test before release.
- **[Grader unify]** After blind_16/17, make the built-in comparison line use `dcf_grade.py`'s definitions. It is held until then, because it would change the frozen tool's hash.
- **[G-short]** The other gap (sensitivity, about 6 points) is short genes. Same method: diagnose the misses by length and context on blind_14/15.
