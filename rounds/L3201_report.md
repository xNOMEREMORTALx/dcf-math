# DCF L3201: the F₁₇ minimum is a 21-digit prime from the repunit tables (checked here); Note G brought up to date; the old selenocysteine counts can't be rechecked from Drive
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads pursued:** [R5d], [Sec-recount], [Note G update].

**Still waiting:** `blind_16.zip` (6 links in `L3189_report.md`) and `blind_17.zip` (8 links in `L3197_report.md`).

---

## 1. [R5d] The smallest q with period F₁₇ = 1597
**The setup.** 1597 is prime, so every prime factor of the repunit R₁₅₉₇ = (10¹⁵⁹⁷ − 1)/9 has period exactly 1597. Conversely, every q with period 1597 is built only from such primes. **So the minimum is the smallest prime factor of R₁₅₉₇.**

**Direct search is hopeless.** A prime p ≡ 1 (mod 3194) has 10 of order 1597 with probability only about 1597/(p − 1). My search above 10⁸ was stopped.

**External source (untrusted until checked).** The stdkmd repunit factor table (page R1501–R1600) lists two known prime factors of R₁₅₉₇ plus a 1539-digit composite cofactor (3.62% factored).

**Checked here [V].** Both listed factors are prime, ≡ 1 (mod 3194), and divide 10¹⁵⁹⁷ − 1:
- **232159532264041847249** (21 digits)
- 30817019975627818877405998694224895213 (38 digits)

**Result [V, conditional].** **min q(F₁₇) = 232,159,532,264,041,847,249**, provided the unfactored cofactor has no smaller prime factor. Decades of ECM work on repunits make a missed factor below 21 digits very unlikely, but it is not proved.

**The table now reads:**

| Fₙ | 1597 | 2584 | 4181 | 6765 | 10946 | 17711 | 28657 | 46368 | 75025 |
|---|---|---|---|---|---|---|---|---|---|
| min q | **2.32 × 10²⁰** | 25841 | 8363 | 40591 | 21893 | 141689 | 1547479 | **47 × 2017** | > 10⁸ (open) |

**F₂₅ = 75025 is still open.** It needs the smallest primes of period 3001·k (from R₃₀₀₁'s factors) combined with 21401 (period 25). The table page for R₃₀₀₁ could not be read this round.

## 2. [Sec-recount] Not possible from Drive
- **The Drive code zips hold tool outputs only.** That is by rule: no genomes and no counting scripts. So the L3137–L3173 selenocysteine counts cannot be rechecked without re-downloading those genomes.
- **Risk assessment:**
  - The double-count adds the tRNA-Sec lines (1–3 per genome) **only in genomes that already use selenocysteine**.
  - So "carries Sec / does not" flips only if a genome had a tRNA-Sec but no selenoprotein, which is rare.
  - Correlations (L3145 ρ = 0.84; L3165 ρ = −0.10) could shift slightly; no verdict looks close enough to flip.
- **Status:** open, low risk, logged in Note G §6.

## 3. [Note G update] Note G v1.1
Pushed as `docs/NoteG_label_free_gene_finder_draft_v1.1.md` (dcf-genefinder):
- v2.31 and its rule;
- the code record **114 of 117**, with the *Gluconobacter* error explained;
- blind sets 9–15 (§3i);
- a new §5c on the metal profile and selenocysteine finder, with their limits and the Andreini 2017 prior art;
- corrections 6 (selenocysteine double-count) and 7 (the seen-list gap).

## Record
No predictions graded this round. **264 of 344 passed, plus 3 split.**

## Summary
- **The F₁₇ minimum is a 21-digit prime, 232159532264041847249**, taken from the repunit factor tables and verified here. It is the smallest *known* factor of R₁₅₉₇, which makes it the minimum unless the unfactored part hides a smaller one (very unlikely, not proved).
- **The old selenocysteine counts can't be rechecked from Drive.** The saved zips hold outputs only. The risk of a changed verdict is low and is logged.
- **Note G (the gene-finder paper draft) is current again:** version 2.31, 114/117 genetic codes, seven new blind sets, and an honest section on the metal and selenocysteine tools.

## Potential leads for future research
- **[Blind 16 + 17]** Grade Fe-rTCA, Fe-ferment H2 and Sec-3 together when the zips arrive.
- **[R5e]** F₂₅ = 75025: read R₃₀₀₁'s known factors (stdkmd page 31), verify them, and compute the cheapest cover with 21401.
- **[Sec-recount b]** If Gary re-downloads the Sec-carrying genomes of L3137–L3173 (about 10 files), recount from `transl_except`.
- **[Submission G]** Note G is close to a software-note draft. Next: a short methods comparison with Prodigal on one frozen genome set, and a JOSS-style README.
