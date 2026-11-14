# DCF L3485: Number audit for Manuscript 2 (67/81 confirmed), a first full draft, and a pre-registered sodium/calcium test on unseen vertebrate channels
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Audit 2], [Manuscript 2], [v7 test]. **No predictions graded.**

---

## 1. [Audit 2]
**What it does:** `rounds/L3485_audit2.py` reads the committed grade outputs of all seven nerve-chemistry blind tests and recomputes the tally, with no hand-entered numbers.

**Result:** the tally is **67 of 81**, matching the hand-kept tally exactly. Per test: mouse 10/10, zebrafish 10/11 and 7/10, chicken 13/14, fly 5/13, nematode 9/9, all other animals 13/14.

## 2. [Manuscript 2] Draft v0.1
**File:** `notes/Manuscript_nerve_metals_draft_v0.1.md`.

**Contents:**
- abstract, methods (final rules, protocol, truth rules), results and discussion;
- a breakdown of all 14 failures by cause: 6 were limits of the name-based truth rules, and 8 were real rule errors, each followed by a frozen fix.

## 3. [v7 test] Pre-registered: the sodium/calcium decision on unseen sequences
- **Pre-registration:** `PREREGISTERED_L3485_navcav.txt`.
- **Data:** unreviewed UniProt (TrEMBL) vertebrate proteins of 1,500–3,500 aa named "sodium channel protein" or "calcium channel subunit alpha," from every species except the four seen vertebrates.
- **Truth:** UniProt's automatic names.
- **Predictions:**
  - **V1:** swaps ≤ 1%;
  - **V2:** sodium recall ≥ 90%;
  - **V3:** calcium recall ≥ 90%;
  - **V4:** v7 swaps fewer than v6.

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=(reviewed:false)+AND+(taxonomy_id:7742)+AND+(length:[1500+TO+3500])+AND+((protein_name:%22sodium+channel+protein%22)+OR+(protein_name:%22calcium+channel+subunit+alpha%22))+NOT+(organism_id:9606)+NOT+(organism_id:10090)+NOT+(organism_id:7955)+NOT+(organism_id:9031)

**Size:** probably 5–30 MB.

## Record
No predictions graded. **392 of 544 passed, plus 3 split.** V1–V4 are waiting.

## Summary
- **The Manuscript 2 numbers are confirmed by script (67 of 81),** and a complete first draft exists.
- **The lysine-first fix faces its own blind test:** thousands of unreviewed sodium and calcium channel sequences from vertebrates the tool has never seen.

## Potential leads for future research
- **[V-test]** Grade V1–V4.
- **[Figures 2]** Three figures for Manuscript 2.
- **[Before nerves]** Sponge, placozoan and comb-jelly proteomes.
