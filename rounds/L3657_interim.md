# DCF L3657 (interim): A CCH1 vs NALCN test and the worm's NALCN rings are frozen; Manuscript 2 v0.17 and the reader brief are updated
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [CCH1 vs NALCN], [Worm NALCN], [Manuscript 2], [Reader brief]. **No predictions graded.**

---

## 1. Frozen test (`PREREGISTERED_L3657_cch1_worm.txt`, `rounds/dcf_cch1_L3657.py`)
- **Script:** reuses the frozen L3653 definitions by reading that file, so the NALCN rule and ring reader are unchanged.
- **Part C:** each L3653 NALCN hit is scored against **yeast Cch1** and against **mouse Nalcn**.
  - **C1–C3:** the Hydra, sponge and sea-anemone hits are nearer Cch1 (my expectation; only Hydra's are *named* CCH1).
  - **C4 (control):** every bilaterian hit is nearer Nalcn.
- **Part W:** the full *C. elegans* proteome.
  - **W1:** ≥ 2 NALCN hits (nca-1, nca-2).
  - **W2:** all read E-E-K-E.

**Files needed:**
1. **References (yeast Cch1 + human NALCN):** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=accession%3AP50077%20OR%20accession%3AQ8IZF0
2. **Worm proteome:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000001940

## 2. Manuscript 2 v0.17 (`notes/Manuscript_nerve_metals_draft_v0.17.md`)
- **Abstract:** 26 tests, **139 of 165**, plus the NALCN finding.
- **Table:** a new row. **It sums to 139/165, matching the audit.**
- **New section:** §3.19 NALCN rings.

## 3. Reader brief (`notes/Reader_brief_Manuscript2.md`) → v0.17
- **Counts:** 139 of 165, 26 failures listed.
- **New findings** in the summary paragraph.
- **The reviewer questions** now point at §3.16 and §3.19, and ask "one paper or two?".
- **A new known limit:** one isoform per gene in UniProt.

## Record
No predictions graded. **472 of 638 passed, plus 3 split.** Nerve-chemistry audit **139 of 165.**

## Summary
- **A test of whether the non-bilaterian E-E-E-E leak-channel hits are true NALCN or the related CCH1 family is frozen,** together with the worm's NALCN rings. It waits on two small downloads.
- **Manuscript 2 (v0.17) and its reader brief now include the NALCN result,** with every count matching the audit.

## Potential leads for future research
- **[CCH1 / worm]** Grade C1–C4 and W1–W2 when the files arrive.
- **[Lancelet exon]** The RefSeq gene model for lancelet NALCN.
- **[RefSeq NR1]** The sea-urchin and Ciona RefSeq proteins.
- **[Outside reader]** The brief is ready to send to a reader.
