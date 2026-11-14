# DCF L3433: The Kv7 gap and the muscle sodium channel fixed (development); a blind test in a fish is pre-registered; the phone gets menu 34, nerve channels by metal ion
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Leads:** [Kcnq], [Scn4a], [Phone], [Second species]. Everything here is development on files already seen. **No predictions graded.**

---

## 1. [Kcnq] Kv7 channels: a voltage sensor with one charge swapped
- **What Kv7 channels are:** the KCNQ family, the brain's "M-current" brake on repeated firing.
- **Why they were missed:** their voltage sensor reads **R-F-L-Q-I-L-R-M-V-R-M-D-R**. A **glutamine (Q)** sits where the frozen sensor motif needs a fourth R or K, so the five-charge rule never sees them.
- **New Kv7 route:** a protein under 1,500 aa that has the sensor **R-x-x-Q-x-x-R-x-x-[RH]** together with the potassium filter **[TS]-[VI]-G-Y-G-D**.
- **Development result:** all five mouse Kcnq genes and human KCNQ5 are now called potassium, with no new false calls. The new route alone, without the filter, would also catch ZDHHC13 and Tedc2; requiring the filter excludes them.

## 2. [Scn4a] The muscle sodium channel
- **Why it was undecided:** Scn4a has one extra match to the calcium ring, **T-N-S-Q-E-S-W**, in the outer loop of domain I, outside the pore.
- **The fix:** order the rule. If the **sodium lysine loop** (the K of DEKA) is present and the ring count is ≤ 2, call sodium. Only otherwise does a ring of ≥ 3 mean calcium.
- **The check:** no calcium channel in human or mouse has the lysine loop.

## 3. v3 on all seen data (development)
| set | channel calls | wrong | family genes found |
|---|---|---|---|
| human files 1–4 | 22 | **0** | 22 of 27 |
| mouse files 1–3 | 56 | **0** | 56 of 64 |

**Remaining misses:**
- the Kcng silent subunits;
- three "elk" channels (Kcnh3, 4, 8);
- SCN7A/Scn7a (Naₓ, a sodium sensor, not a spike channel).

## 4. [Second species] Pre-registered blind test in zebrafish (fish, ~450 million years from mammals)
- **Pre-registration:** `PREREGISTERED_L3433_zebrafish.txt`, frozen and pushed with the v3 script hash, before any fish file exists here.
- **Predictions Z1–Z6:** the same thresholds as the mouse test (calcium, sodium, potassium/HCN precision; recall ≥ 75%; K2P precision and recall).
- **Truth rules allow zebrafish paralog names** (e.g. scn8aa, scn4ab). Beta subunits are excluded.

## 5. [Phone] Bundle 6.10: menu 34
- **New menu 34, "nerve channels by metal ion":** pick an mRNA file (for example `mouse.3.rna.fna.gz`). It lists the sodium, potassium, calcium, HCN pacemaker and K2P leak channels by name.
- **New companion file `dcf_nerve.py`** carries exactly the rules that passed blind (v2 and K2P). v3 waits for the fish test.
- **Self-test 264/264.** The new row checks synthetic calcium, sodium, potassium and K2P proteins.
- **Install:** copy all **eight** `.py` files from `dcf_phone_bundle_6.10.zip` into one folder, open `dcf_phone_6.10.py`, and press Run.

## Action for Gary: two zebrafish files
1. https://ftp.ncbi.nlm.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.1.rna.fna.gz
2. https://ftp.ncbi.nlm.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.2.rna.fna.gz

**Keep the file names. If a link doesn't work, just send the one that does:** a missing file is dropped, not replaced.

## Record
No predictions graded. **335 of 473 passed, plus 3 split.** Six predictions (Z1–Z6) are waiting.

## Summary
- **The rule's two known gaps are closed in development:**
  - the Kv7 "brake" channels, whose voltage sensor has a glutamine in place of one charge;
  - the muscle sodium channel, which has an extra calcium-like loop outside the pore.
- **On all human and mouse data so far, the improved rule made 78 channel calls with none wrong.**
- **The next test is a fish:** whether metal-ion gates read from mRNA hold across 450 million years of evolution.
- **The phone can now do this:** menu 34 lists a file's nerve channels by the metal each one carries.

## Potential leads for future research
- **[Zebrafish]** Grade Z1–Z6 when the files arrive.
- **[Elk]** Why Kcnh3/4/8 lack a matching voltage sensor; inspect them on the seen data.
- **[Neuro iron]** The iron enzymes that make dopamine and serotonin (tyrosine and tryptophan hydroxylase).
- **[NMDA metals]** The magnesium-block and zinc sites of glutamate receptors.
- **[Insect]** A third, more distant test: fruit fly channels (Shaker, the first potassium channel cloned, para, cac).
