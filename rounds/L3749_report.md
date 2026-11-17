# DCF L3749: The voltage sensor's "gear teeth" (1 of 3 as frozen, because toxins slipped into the channel set); the true channels carry a charge every third residue in 90% of cases; CRY4 alternative links
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [S4 gear] (L3737), [Cryptochrome tetrad] (new download links).

---

## 1. The S4 "gear" (`PREREGISTERED_L3749_s4gear.txt`, `rounds/dcf_s4gear_L3749.py`)
**Background:**
- **The voltage sensor (S4 helix) carries a positive charge, K or R, on every third residue.** When voltage changes, it moves through the membrane with a screw-like motion, the molecular "gear" that couples voltage to opening.
- **The DCF channel rules assume this spacing,** so testing it on our own calls would be circular. **The test uses UniProt's curated family labels instead** (58,949 reviewed animal proteins).

| # | prediction | result |
|---|---|---|
| G1 | ≥ 90% of labelled channels have ≥ 4 K/R at spacing 3 | **19.8%: FAIL** |
| G2 | ≤ 30% at spacing 2, and ≤ 30% at spacing 4 | **7.2% and 13.2%: PASS** |
| G3 | spacing-3 share ≥ 5 × other proteins | **2.2 ×: FAIL** |

**1 of 3 passed.**

**Disclosed flaw:**
- **My family filter "Sodium channel" also caught scorpion toxins.** UniProt calls their family "Sodium channel inhibitor"; there were 446 of them, small proteins with no S4. It also caught the auxiliary SCN1B subunit.
- **Those swamped the 582-entry "channel" set.** The failures stand as graded.

**Descriptive, after grading** (toxins, auxiliary and β subunits removed: 124 true pore-forming channels):

| set | ≥ 4 K/R at spacing 2 | spacing 3 | spacing 4 |
|---|---|---|---|
| true channels | 33.1% | **90.3%** | 34.7% |
| all other proteins | 9.0% | 8.9% | 8.6% |

- **Spacing 3 is about 10 times background in true channels** and present in 90% of them.
- **Spacings 2 and 4 are also raised** (about 3.7 ×). Channels are long and charge-rich, so some runs appear by chance; the spacing-3 excess is about three times larger.

**Teeth (the longest run of K/R at spacing 3) by family:**

| family | median | max |
|---|---|---|
| Na channels | **8** | 8 |
| Ca channels (α1) | 6 | **8** |
| Shaker (Kv1) | 7 | 7 |
| Shab, Shal, S, V, Eag | 5 | 5 |
| **KQT (Kv7, KCNQ)** | **3** | 3 |

- **Kv7 channels have only three teeth.** That is the known weak voltage sensor, and the reason the DCF rules needed a separate "weak-sensor" route for them (Manuscript 2).
- **The gear is real, family-specific, and conserved in the reviewed set.**

## 2. CRY4: alternative download links
1. **Website search** (then Download → FASTA or TSV): https://www.uniprot.org/uniprotkb?query=cryptochrome+4+AND+taxonomy_id:8782
2. **All bird cryptochromes, FASTA:** https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28protein_name%3Acryptochrome%29%20AND%20%28taxonomy_id%3A8782%29
3. **Robin only, by name:** https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28organism_name%3A%22Erithacus%20rubecula%22%29%20AND%20%28protein_name%3Acryptochrome%29

## 3. DNA-store round trip: status
- **The existing ECC module already has a full unlabelled pipeline:** 20-mer clustering → gapped consensus → Reed–Solomon decode. Its own notes record success at 12% error with 25 reads per strand (L2784).
- **The new 6-mer index needs the original strands as a reference,** which a real decoder does not have, so it does not replace that clustering.
- **Both are complementary:**
  - the index identifies reads against a known library;
  - the ECC pipeline decodes without one.

## Record
**+1 passed, 2 failed. 516 of 709 passed, plus 3 split.** Audit **183 of 236.**

## Summary
- **Testing the voltage sensor's "gear teeth" against UniProt's own channel labels failed as frozen (1 of 3),** because scorpion toxins named "sodium channel inhibitors" entered my channel set.
- **On the 124 true channels, 90% carry a charge every third residue,** about 10 times background.
- **Teeth counts fit physiology:** sodium channels 8, Shaker 7, and the weak-sensor Kv7 channels only 3.
- **Three alternative links for the bird CRY4 sequences are given.**

## Potential leads for future research
- **[Gear test, corrected]** Pre-register the corrected filter (pore-forming families only, toxins and auxiliary subunits excluded) on the TrEMBL channel file (L3489, ~25,000 channels) as a fresh blind set.
- **[Gear and timing]** Relate teeth count to channel speed. Na channels (8 teeth) are the fastest, Kv7 (3) the slowest. Is the tooth count a sequence-readable "speed dial"? This needs published activation time constants per family.
- **[Cryptochrome tetrad]** Grade a four-tryptophan conservation test once the CRY4 file arrives.
