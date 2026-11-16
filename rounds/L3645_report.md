# DCF L3645: Two unseen rotifers (6 of 7). The new partial-sodium rule rescues *B. plicatilis*'s channel blind; multiple NALCN copies are not a rotifer-wide trait
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Data:** Gary's two files, which match the two proteomes exactly:

| file | organism | proteins |
|---|---|---|
| `Brachionus_plicatilis.gz` | *B. plicatilis* (UP000276133) | 52,387 |
| `stream_26.gz` | *Adineta ricciae* (UP000663828) | 64,111 |

**Procedure:**
1. **Frozen files:** `PREREGISTERED_L3641_rotifers.txt` and `dcf_l3641_blind.py`; the hashes matched the ledger.
2. **Tool output:** `rounds/L3645_tool_output.txt`, pushed before names were read.
3. **Grading:** `rounds/L3645_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| F1 | every Na_partial call nearest a mouse Scn | **1 of 1 (Scn1a): PASS** |
| F2a | *B. plicatilis* ≥ 1 Na or Na_partial | **1 Na_partial: PASS** |
| F2b | *A. ricciae* ≥ 1 Na or Na_partial | **5 Na: PASS** |
| N1a | *B. plicatilis* ≥ 2 nearest NALCN | **1: FAIL** |
| N1b | *A. ricciae* ≥ 2 nearest NALCN | **PASS** (5 literal; 2 real, see below) |
| B1 | *B. plicatilis* ratio > 1.8 | **18 / 7 = 2.57: PASS** |
| B2 | *A. ricciae* ratio > 1.8 | **85 / 28 = 3.04: PASS** |

**6 of 7 passed.**

**Disclosure:** the frozen NALCN count had **no score floor.**
- **Graded literally,** *A. ricciae* has 5 proteins nearest Nalcn. Three of them score only 54–61, which is noise: unrelated large proteins whose best match among the references happens to be Nalcn.
- **With a floor of 1,000, it has 2.** The outcome of N1a and N1b is the same either way.
- **Future NALCN counts will use a score floor.**

## Descriptive, after grading
- ***B. plicatilis*:**
  - **Sodium channel:** **A0A3M7P5C0 (1,497 aa, "Sodium channel protein", nearest Scn1a) is just 3 aa under the 1,500-aa cut.** Only the new partial rule caught it. **Without the L3641 rule, F2a would have failed.**
  - **Other channels:** one T-type calcium channel; **one NALCN** ("Sodium leak channel non-selective").
- ***A. ricciae*:**
  - **Sodium channels:** 5 called. They come in near-identical pairs, as expected for a bdelloid's doubled genome.
  - **One possible partial miss:** A0A814K322 (1,479 aa, nearest Scn3a) is an uncalled sodium-like fragment with fewer than 4 voltage-sensor matches.
  - **NALCN:** **two copies** (A0A814EKK9 and A0A815B8G0, each 1,730 aa), again a pair.
  - **Calcium channels:** L-type, T-type and an IQ-domain type, also in pairs.

## Reading
| rotifer | sodium channel | NALCN copies | ratio |
|---|---|---|---|
| *B. calyciflorus* (L3637) | yes | **3** | 1.93 |
| *B. plicatilis* | yes (partial) | **1** | 2.57 |
| *A. ricciae* (bdelloid, doubled genome) | yes (pairs) | **2** (one pair) | 3.04 |

- **All three rotifers keep the lysine sodium channel,** and all are above the 1.8 battery cut.
- **Multiple NALCN copies are not a rotifer trait.**
  - *B. calyciflorus* has 3.
  - Its close relative *B. plicatilis* has 1.
  - *Adineta*'s 2 are a homeolog pair from genome doubling.
  - The three *B. calyciflorus* copies are a lineage-specific expansion, or possibly gene-model splitting. That stays open.
- **The partial-sodium rule's first blind use rescued a real sodium channel,** with precision 1 of 1.
  - That is thin evidence, so the rule stays in research scripts. It ships in the tools after more blind calls.

## Record
**+6 passed, 1 failed. 468 of 633 passed, plus 3 split.** Nerve-chemistry audit **135 of 160.**

## Summary
- **Two unseen rotifers passed 6 of 7 predictions.**
- **The partial-sodium rule** caught the marine rotifer's sodium channel, a protein 3 amino acids under the old length cut, and was correct.
- **Both rotifers keep sodium channels and are above the battery cut.**
- **Multiple NALCN leak-channel copies turned out not to be general:** the marine rotifer has one, and the bdelloid's two are a genome-doubling pair.
- **Disclosed weakness:** the frozen NALCN count lacked a score floor (same outcome either way).

## Potential leads for future research
- **[Partial rule, more blind calls]** Pool the partial rule into the next blind tests (any new genome). Ship it to the phone/genefinder after ≥ 5 blind calls at full precision.
- **[NALCN floor]** Adopt a score floor of 1,000 for every nearest-reference count; pre-register it before use.
- **[*B. calyciflorus* NALCN ×3]** Compare the three copies' pore rings and the genome positions (RefSeq/Ensembl gene IDs). Are they real genes or split models?
- **[RefSeq NR1]** Still waiting for the sea-urchin and Ciona RefSeq protein files.
- **[Manuscript 2]** §3.13–3.18 and the size-vs-sodium figure. The nerve chapter now spans blind-tested proteomes from protists to chordates.
