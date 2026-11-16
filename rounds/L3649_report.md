# DCF L3649: The rotifer's three NALCN copies are one gene; a score-floor rule; Manuscript 2 v0.16 with Figures 8–9 (135 of 160 audited)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [*B. calyciflorus* NALCN ×3], [NALCN floor], [Manuscript 2]. Descriptive work and writing. **No predictions graded.**

---

## 1. The three *B. calyciflorus* NALCN entries (`rounds/L3649_nalcn_copies.txt`)
| entry | length | pore-ring words [TS]-x-[EDK]-x-W |
|---|---|---|
| A0A813M7M3 | 1,841 | SQEGW, **TQKGW**, SLEGW, TGEDW |
| A0A813MDY4 | 1,892 | SQEGW, **TNEGW**, **TQKGW**, SLEGW, TGEDW |
| A0A813MKV0 | 1,847 | SQEGW, **TNEGW**, SLEGW, TGEDW |
| mouse Nalcn | 1,739 | SQEGW, TQEGW, SLKGW, TGEDW |

- **Pairwise global identity:** **98.5–100%** where the sequences align. Each is about 55% identical to mouse Nalcn.
- **They differ only by carrying T-N-E-G-W, T-Q-K-G-W, or both.** This looks like **alternative exons (or assembly duplicates) of one gene,** not three genes.
- **So each *Brachionus* has one NALCN gene,** which is consistent with *B. plicatilis*' single copy (L3645). The bdelloid's two are a homeolog pair.
- **The L3637 "×3" lead is closed:** it was an annotation effect.
- **New detail:** one exon variant puts a **lysine** into the NALCN ring (T-Q-**K**-G-W), a possible switch in ion preference by splicing. This is speculative; it would need the gene model and expression data.

## 2. [NALCN floor]: a standing rule from now on
**Any count of "proteins nearest reference X" must use a local-alignment score floor of 1,000, stated in the pre-registration.**

**Why:**
- unrelated large proteins always have *some* nearest reference, with scores of about 50–80;
- true hits score 1,600–4,600 in every case so far.

**First used in:** the next pre-registration.

## 3. Manuscript 2, draft v0.16 (`notes/Manuscript_nerve_metals_draft_v0.16.md`)
- **Abstract:** 25 blind tests, **135 of 160**. Two new findings: NR1 first appears in cnidarians; sodium loss is lineage-specific, not size-driven (18 of 21).
- **Methods:**
  - the v3 sodium loop;
  - the research-only rules (partial sodium channel, nearest-reference naming).
- **Results table:** 10 new rows. **The table sums to 135/160, matching `L3485_audit2.py` exactly.**
- **New sections:**
  - §3.13 sea hare NMDA;
  - §3.14 tardigrade 2;
  - §3.15 NR1 on the tree;
  - §3.16 sodium loss and size;
  - §3.17 rule repairs and disclosed grading issues;
  - §3.18 NALCN variants.
- **Figures** (all values checked against the committed outputs):
  - **Figure 8** (`figures/L3649_size_sodium.png`): battery ratio vs sodium channel in 10 animals;
  - **Figure 9** (`figures/L3649_nr1_tree.png`): NR1 across 21 proteomes.
- **Caught before commit:** my first abstract said "20 of 23" for the sodium-loss tests. The four tests sum to **18 of 21**, which is now corrected.

## Record
No predictions graded. **468 of 633 passed, plus 3 split.** Nerve-chemistry audit **135 of 160.**

## Summary
- **The rotifer's three "NALCN copies" are variants of one gene.** They are 98.5–100% identical and differ only by alternative pore-loop words, one carrying a lysine.
- **A score floor of 1,000 is now standard** for nearest-reference counts.
- **Manuscript 2 is updated to v0.16:**
  - six new results sections and two new figures;
  - a table that matches the audit (135 of 160);
  - one wrong summary count caught and corrected before commit.

## Potential leads for future research
- **[NALCN lysine exon]** Is the T-Q-K-G-W exon conserved in other rotifers or animals? Search NALCN sequences for a K in the domain II/III ring.
- **[Split the paper]** Consider a methods paper (§3.1–3.12) and an evolution paper (E→K, NR1, sodium loss, battery).
- **[Reader brief]** Update to v0.16 for the outside reader.
- **[RefSeq NR1]** The sea-urchin and Ciona RefSeq protein files.
- **[Partial rule]** Needs ≥ 5 blind calls before it ships.
