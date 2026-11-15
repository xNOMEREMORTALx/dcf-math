# DCF L3549: Gene finder and phone advanced. The nerve tool v2 adds T-type calcium, the Naₓ sensor, protein inputs, the battery ratio and an "excitability kit" read across animals
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Phone], [genefinder], Gary's themes (tracing consciousness, energy storage and retrieval). **No predictions graded.**

---

## 1. New in `dcf_nerve.py` v2 (phone menu 34 and dcf-genefinder)
- **Channel rules:** the same as v8, which has been tested blind across animals.
  - **lysine first:** T-F-K-G-W → DEKA sodium;
  - **Naₓ sensor:** T-F-N-G-W, DENA;
  - **weak-sensor route,** for Kv7, KCNH and HCN.
- **T-type calcium split (development):** a calcium channel with ≥ 2 ring sites carrying D (the EEDD pattern) is called T-type.
  - On human, mouse, zebrafish, chicken and fly: **14 of 15 T-type genes called; 0 of 30 L/N/P/Q/R-type miscalled** (zebrafish cacna1ha has only one D site).
  - **Why it matters:** T-type channels drive rhythmic bursting, including the thalamic rhythms of sleep spindles.
- **Inputs:** RefSeq mRNA (non-coding NR_/XR_ records now skipped), **protein FASTA** (e.g. Ensembl `pep.all`) or **UniProt TSV**.
- **Two new summary lines:**
  - **BATTERY:** channels (dischargers) per metal pump (chargers);
  - **EXCITABILITY KIT:** HCN pacemakers, T-type calcium, K2P leak channels, the iron enzymes that make dopamine, noradrenaline and serotonin, and glutamate receptors. *It is a parts list, not a measure of consciousness.*
- **Sodium spike type:** DEKA present or absent.

**Phone bundle 6.12:** `phone/dcf_phone_bundle_6.12.zip`, **self-test 265/265.** It adds a T-type row to the synthetic-protein self-test.

## 2. The excitability kit across lineages (descriptive; `rounds/L3549_nerve_v2_examples.txt`)
| data | sodium spike | HCN | T-type Ca | K2P | Fe enzymes (DA/NA/5-HT) | glutamate rec. | channels per pump |
|---|---|---|---|---|---|---|---|
| choanoflagellate + sponge + placozoan + anemone | none (E-type) | 4 | 2 | 23 | 3 | 17 | 3.9 |
| **comb jelly** | none (E-type) | **0** | **0** | 19 | **0** | 29 | **13.3** |
| acoel worm *Hofstenia* | none (E-type) | 3 | 1 | 14 | 3 | 15 | 5.0 |
| brachiopod + annelid + acorn worm + sea urchin | DEKA (protostomes) | 16 | 20 | 65 | 18 | 45 | 4.2 |
| mouse (mRNA file 3) | DEKA | 3 | 1 | 7 | 3 | 8 | 3.0 |

**Reading:**
- **The comb jelly stands apart.**
  - It has no HCN pacemakers, no T-type calcium channels, and **no iron hydroxylase** (no dopamine/serotonin synthesis enzyme found).
  - Instead it has a huge potassium-channel set (13 channels per pump).
  - This is consistent with published reports that comb jellies lack the classic monoamine transmitter pathways. If those reports hold, they built their nervous system with a different chemistry.
- **Every other lineage, including the acoel worm, already has the pacemaker + T-type + monoamine iron-enzyme combination,** the parts that rhythm and arousal circuits use in vertebrates.

## 3. Storage and retrieval: where the pieces sit
- **Energy storage and retrieval:** the pumps store ATP energy as ion gradients, and the channels retrieve it as impulses. The BATTERY line now measures that balance for any genome.
- **Information storage:** the glutamate receptors (including NMDA, the vertebrate learning switch) are counted in the kit.
- **The phone's DNA codec** (`dcf_dna_codec.py`, `dcf_dna_ecc.py`, bundled unchanged) remains the DCF's data-storage tool.

## Record
No predictions graded. **411 of 566 passed, plus 3 split.**

## Summary
- **The gene finder's nerve tool reached v2, and the phone 6.12:**
  - the rules tested blind across animals;
  - T-type calcium (14 of 15 in development) and the Naₓ sensor;
  - protein and UniProt inputs;
  - two summaries: the nerve battery ratio, and an excitability parts list (pacemakers, T-type calcium, leak channels, monoamine iron enzymes, glutamate receptors).
- **Read across animals, the kit separates the comb jelly:** no pacemakers, no T-type channels, no monoamine iron enzymes, and three times more channels per pump. Every other lineage, even the acoel worm, already carries the vertebrate-style rhythm-and-arousal parts.

## Potential leads for future research
- **[Kit test]** Pre-register the kit for an unseen lineage, e.g. a tardigrade, an octopus or a tunicate: predict HCN ≥ 1, T-type ≥ 1, Fe enzymes ≥ 1. Octopus is an interesting case, with an independently enlarged brain.
- **[T-type blind]** A blind test of the T-type rule on TrEMBL calcium channels named "T-type" vs "L-type".
- **[Comb-jelly monoamines]** Confirm by sequence that comb jellies lack tyrosine/tryptophan hydroxylase, e.g. by searching the iron core with looser flanks (H-x₄-H in an AAAH-length protein).
