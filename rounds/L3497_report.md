# DCF L3497: A finder for the sodium sensor Naₓ (the "N" of the DENA ring), and Manuscript 2 at v0.3
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Naₓ finder], [Manuscript 2 v0.3]. This is development on data already graded. **No predictions graded.** The before-nerves test (S1–S7) is still waiting for its file.

---

## 1. [Naₓ finder] (`rounds/L3497_nax_dev.txt`)
**The search:** sequences present in ≥ 90% of the 67 Naₓ-named TrEMBL proteins, and in none of the 15,530 other named sodium/calcium channels.

**The answer is in the pore:** **A-T-F-N-G-W**. It sits where every spike-firing sodium channel has A-T-F-**K**-G-W.
- In Naₓ the lysine (K) of the DEKA ring is replaced by an asparagine (N), giving a **DENA** ring.
- That is why Naₓ senses sodium concentration instead of firing impulses, and why the lysine rule never called it.

**v8 rule (`rounds/dcf_neurochem6_L3497.py`, frozen for a future test):** in the 4-domain branch, T-F-[N/Q]-G-W → sodium (sensor).

**Development:**
- **TrEMBL:** 66 of 67 Naₓ-named proteins carry it. So do 94 of the generically named "sodium channel protein" entries that v7 missed.
- **Other channels:** no calcium-named or other named channel carries it.
- **Seen proteomes:** it appears only in human SCN7A and mouse Scn7a, which v8 now calls sodium.

## 2. Manuscript 2 v0.3
**File:** `notes/Manuscript_nerve_metals_draft_v0.3.md`.

**New in this version:**
- **§3.4, the remaining errors:**
  - the duck calcium channels with a stray lysine;
  - the ghost-shark proteins without one;
  - why a ring cut would be worse;
  - the Naₓ explanation for the missed sodium channels.
- **A Figures section,** listing Figures 1–3.

## Action for Gary (still needed): the four early-animal proteomes
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000007879%20OR%20proteome%3AUP000009022%20OR%20proteome%3AUP000001593%20OR%20proteome%3AUP000001357

## Record
No predictions graded. **396 of 548 passed, plus 3 split.**

## Summary
- **The sodium channels the tool kept missing are explained by one letter.** The sensor Naₓ has N where firing channels have K (DENA instead of DEKA).
- **A one-motif branch now finds 66 of the 67 Naₓ-named proteins in development,** with no hits on any other channel type.
- **The second paper is at v0.3** with its figures and error analysis.

## Potential leads for future research
- **[Before nerves]** Grade S1–S7 when the file arrives.
- **[v8 blind]** Test the Naₓ branch on unseen sequences, e.g. TrEMBL Naₓ from reptiles and amphibians, with all four seen vertebrates excluded.
- **[DEKA origin]** In the before-nerves file, print every 4-domain channel's four pore loops, to show where the ring letters sit before the lysine appears (descriptive).
