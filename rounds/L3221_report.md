# DCF L3221: blind_18 — sulfate reducers beat their relatives, but *Arcobacter* reads high; selenocysteine is not only a formate-enzyme trait; the start fix holds; the new island finder works where Fe–S metabolism exists
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads graded:** [Fe-Fd], [Sec-O], [G-starts c] (L3217), and the new **[Fe-island]** (L3221).

**Data:** `blind_18.zip` held 5 of the 6 pre-registered genomes. *Nautilia profundicola* (NC_012115) was missing, and *S. thermophilus* (NC_006448, already used in blind_17) was in its place and was set aside. All five were matched by LOCUS line. Renamed but the same strains:
- *Desulforamulus reducens* MI-1;
- *Aliarcobacter butzleri* RM4018.

**Tools:** all hashes matched the frozen versions.

**Tool numbers** were hashed before any annotation was read: SHA-256 `5f755921dcb73c36010e02878e0acf15095ad7ee40827e450bd2b547f0572485`.

**Pre-registrations:**
- `PREREGISTERED_L3217.txt` (`6fff72c9…`);
- `PREREGISTERED_L3221_islands.txt` (`2b194ac6…`). Its script is `rounds/dcf_islands_dev_L3221.py`, SHA-256 `4ae338ab…b1f9`, and it was confirmed unchanged before running.

---

## 1. Lineage-matched pairs [Fe-Fd]
| pair | ferredoxin-based member | CxxC/1000 aa | partner | CxxC/1000 aa |
|---|---|---|---|---|
| P1 | *Desulfomicrobium* (sulfate reducer) | **0.96** | *Myxococcus xanthus* | 0.42 |
| P2 | *Desulfotomaculum* (sulfate/metal reducer) | **0.89** | *Bacillus licheniformis* | 0.31 |
| P3 | *Nautilia* (rTCA, H2) | *file missing* | *Arcobacter butzleri* | **0.57** |

| id | prediction | result | verdict |
|---|---|---|---|
| D1 | first member higher in 3 of 3 pairs | 2 of 2 so far | **PENDING** (needs *Nautilia*) |
| D2 | first members > 0.50 and partners < 0.50 | *Arcobacter* 0.57 | **FAIL** (determined whatever *Nautilia* reads) |
| D3 | any Sec codon in a partner sits in a formate dehydrogenase | *Myxococcus*: 1 Sec, in a **TlpA thiol-disulfide reductase** | **FAIL** |

**Reading.**
- **Within the same phylum, the sulfate reducers read more than twice their relatives' density.** This is the clearest lineage-controlled support so far.
- ***Arcobacter* read 0.57.** Campylobacterota, even oxygen-tolerant ones, rely on ferredoxin-dependent 2-oxoacid oxidoreductases and several anaerobic respirations, so my "oxidative partner" label was too simple. The risk was declared; the failure stands.
- **Selenocysteine is not only a formate-enzyme trait.**
  - *Myxococcus* uses it in a thiol redox protein.
  - *Desulfomicrobium* uses it in peroxiredoxin and CXXC selenoproteins.
  - *Desulfotomaculum* uses it in hydrogenase subunits and formate dehydrogenase.
  - So [Sec-O] in its formate form is **closed**.

## 2. Start fix, v2.32b [G-starts c]
| genome | exact start v2.31 → v2.32b | found change | correct change |
|---|---|---|---|
| *Desulfomicrobium* | 80.5 → **86.0** | +0.32 | 0.00 |
| *Myxococcus* | 75.1 → **80.4** | +0.32 | +0.03 |
| *Desulfotomaculum* | 84.7 → 85.4 | +0.48 | +0.06 |
| *B. licheniformis* | 86.4 → 86.5 | +0.28 | −0.05 |
| *Arcobacter* | 93.9 → 95.0 | +0.04 | 0.00 |

- **Mean start gain is +2.5 so far,** with no genome losing starts. Genes found now go **up** slightly everywhere, which fixes L3213's loss.
- **D4–D6 were frozen on 6 genomes, so they stay pending** until *Nautilia* arrives. No genome so far breaks them.

## 3. The Fe–S island finder [Fe-island], first blind test
**What it does.** It scans windows of 10 consecutive predicted genes and flags windows whose CxxC density is ≥ 3 SD above the genome's own windows. Annotation is used only to grade.

| genome | islands | with an Fe–S/redox gene | keyword-gene enrichment |
|---|---|---|---|
| *Desulfomicrobium* | 10 | 9 | **6.1×** |
| *Desulfotomaculum* | 10 | 8 | **5.9×** |
| *Arcobacter* | 8 | 5 | **6.6×** |
| *Myxococcus* | 24 | 4 | 1.2× |
| *B. licheniformis* | 15 | 3 | 1.5× |

| id | prediction | result | verdict |
|---|---|---|---|
| I1 | ≥ 2.0× in every genome | *Myxococcus* 1.2×, *Bacillus* 1.5× | **FAIL** |
| I2 | pooled enrichment ≥ 3.0× | 91/1061 island genes vs 383/20843 genome-wide = **4.7×** | **PASS** |
| I3 | ≥ 50% of islands carry a keyword gene | 29 of 67 = 43% | **FAIL** |

**Reading.**
- **In genomes built on Fe–S energy chemistry,** the finder lands on the right operons label-free at about 6× the background (hydrogenases, sulfite reductase, formate dehydrogenase).
- **In Fe–S-poor aerobes it flags other cysteine-rich clusters** (*Myxococcus*: 24 islands, mostly not redox). My 0.8% eligibility threshold was too low.
- **A post-hoc pattern [D]:** it works when the genome's Fe–S/redox share is about 1.5% or more. This needs its own blind test.

## 4. Other
- **Genetic code:** 5 of 5 correct; record **133 of 136**.
- **Note H v0.3** gains the pair result and the *Arcobacter* lesson.

## Record
**This round:** 5 graded, 1 passed (D2, D3, I1, I3 failed; I2 passed). D1, D4, D5 and D6 are pending *Nautilia*.

**Total: 275 of 362 pre-registered predictions passed, plus 3 split.**

## Summary
- **The strongest evidence yet for the ferredoxin reading:** sulfate reducers read more than twice their own phylum's oxygen-using relatives.
- **The simple cut failed again,** because an oxygen-tolerant *Arcobacter* reads high. Its lineage runs on ferredoxin enzymes anyway, so lifestyle labels like "aerobe" are too coarse.
- **Selenocysteine is not tied only to formate enzymes;** that idea is closed.
- **The repaired start fix keeps its gains** (+5 points in GC-rich genomes) and no longer loses genes.
- **The new island finder pinpoints hydrogenase and sulfur-reduction operons from raw DNA** in Fe–S-rich genomes (about 6× enrichment), but not in Fe–S-poor ones. 1 of 3 predictions passed.

## Potential leads for future research
- **[Nautilia]** Send NC_012115 (as `blind_18b.zip`) to finish D1, D4, D5 and D6.
- **[Fe-island b]** Pre-register an eligibility rule set by the tool itself (e.g. genome CxxC density ≥ 0.6), then test blind. Optionally add a hydrogenase/ferredoxin motif matcher to separate redox islands from other cysteine-rich clusters.
- **[Fe-Fd b]** Score lineages, not lifestyles. Predict a genome's density from its nearest seen relative, and test whether metabolism adds anything beyond ancestry.
- **[v2.32 release]** If D4–D6 pass with *Nautilia*, release v2.32 (starts +2–5 points, found unchanged or better) and update Note G.
- **[A003060 b-file]** Our exact values for n = 610 … 46368 lie beyond OEIS A003060's published table (n ≤ 438). Extend the b-file for all n up to about 1000 where the minimum is below 10⁸, and offer it to OEIS (Gary's decision).
- **[N-Λ]** No published digit-agreement law found in three searches. Do a zbMATH search; if nothing turns up, write Note Λ v0.6 for submission.
