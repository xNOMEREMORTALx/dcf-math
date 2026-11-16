# DCF L3641: The partial-sodium-channel rule is 9 of 9 in development, the T-W-K-G-W loop is unique to the priapulid channel, and a two-rotifer blind test is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [Fragment rescue], [T-W-K-G-W elsewhere], [Rotifer NALCN ×3]. Development only. **No predictions graded.**

---

## 1. [Fragment rescue] (`rounds/L3641_dev.txt`)
**The rule "Na_partial":**
- the protein is 800–1,499 aa;
- it has ≥ 4 voltage-sensor (S4) matches;
- it carries the v3 lysine loop;
- it is not already a v3 sodium call.

**Across every protein set seen,** it fires on **9 proteins, and all 9 are named sodium channels:**

| organism | calls | what they are |
|---|---|---|
| spider mite | 7 | the 1,034–1,068 aa partial cDNAs, "Voltage-gated sodium channel alpha subunit isoform k/l" |
| horseshoe crab | 1 | A0ABM1SIX9, 1,455 aa, "Sodium channel protein" |
| *Dimorphilus* | 1 | **A0A7I8V7K0, 923 aa: the L3637 miss** |

**Precision 9/9 in development.** Disclosure: the rule was built after seeing the *Dimorphilus* fragment.

## 2. [T-W-K-G-W elsewhere]
- **24 proteins of ≥ 800 aa carry [TS]-W-K-[GA]-W.** They include Notch4, Ctnnd2, dynein heavy chains, a helicase and an acyltransferase.
- **Only one is a channel call: the priapulid sodium channel.** None of the other 23 has a voltage sensor, so the channel gate excludes them.
- **Two readings:**
  - The W-variant lysine loop is, in all data seen, **unique to the priapulid channel**.
  - The v3 clause is safe because the voltage-sensor gate comes first.

## 3. Pre-registered blind test (`PREREGISTERED_L3641_rotifers.txt`)
**Script:** `rounds/dcf_l3641_blind.py`.

**Sanity check on the seen rotifer *B. calyciflorus* (not a test):** 1 sodium channel, **3 NALCN-nearest proteins**, ratio 1.93.

**The two unseen rotifers:**
- ***Brachionus plicatilis*** (marine, same group as *B. calyciflorus*);
- ***Adineta ricciae*** (bdelloid, an ancient asexual lineage).

**Disclosure:** bdelloids carry doubled gene copies, which makes N1b easier.

**Predictions:**

| # | prediction |
|---|---|
| F1 | every Na_partial call is nearest a mouse Scn (precision) |
| F2a, F2b | each rotifer has ≥ 1 Na or Na_partial call |
| N1a, N1b | each rotifer has ≥ 2 NALCN-nearest proteins |
| B1, B2 | each ratio > 1.8 |

**Download links** (by proteome, which avoids duplicate assemblies):
- ***B. plicatilis:*** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000276133
- ***A. ricciae:*** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000663828

## Record
No predictions graded. **462 of 626 passed, plus 3 split.** Seven predictions (F1–B2) are waiting.

## Summary
- **A partial-sodium-channel rule catches gene fragments** such as the *Dimorphilus* channel. In development it made 9 calls, and every one is a named sodium channel.
- **The priapulid's T-W-K-G-W loop is unique among all channels seen.** The 23 other proteins with that word are not channels and are excluded by the voltage-sensor gate.
- **Next blind test, two unseen rotifers:** it asks whether the partial rule stays precise, whether rotifers keep their sodium channel, and whether multiple NALCN leak-channel copies are a rotifer trait.

## Potential leads for future research
- **[Rotifers]** Grade F1–B2 when the two files arrive.
- **[NALCN and rhythm]** NALCN sets the resting "leak" that drives pacemaking and rhythm (it is part of the excitability kit). If rotifers carry several copies, compare their pore rings. Are the copies alike, or has each specialised?
- **[RefSeq NR1]** Still waiting for the sea-urchin and Ciona RefSeq protein files.
- **[Manuscript 2]** §3.13–3.17 and the size-vs-sodium figure.
