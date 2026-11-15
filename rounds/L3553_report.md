# DCF L3553: The T-type rule checked on 14,907 calcium channels (100% precise, 92% recall); a correction: comb jellies do have an iron hydroxylase (PAH); and a pre-registered test of the kit and the K letter in an octopus, a sea squirt and a lancelet
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [T-type blind], [Comb-jelly monoamines], [Kit test].

---

## 1. T-type calcium rule: frozen check, not counted (`rounds/L3553_ttype_check_out.txt`)
**The data:** the TrEMBL vertebrate channels from L3489 (human, mouse, zebrafish and chicken removed).
- **Not counted, because this file was opened in L3489.** But the T-type rule had never been applied to it. The rule hash was pushed before running.
- **Truth:** UniProt's subtype names.

| UniProt name | called T-type | called high-voltage Ca | other |
|---|---|---|---|
| T-type (3,846) | **3,550** | 268 | 28 |
| L/N/P-Q/R-type (11,061) | **0** | 10,942 | 119 |

- **Precision 100%** (no high-voltage channel ever called T-type).
- **Recall 92.3%.**
- **The EEDD ring separates the rhythm-generating T-type channels** from the transmitter-release channels across ~3,800 unseen vertebrate sequences.

## 2. Correction to L3549: comb jellies do have an iron hydroxylase (`rounds/L3553_ctenophore_monoamine.txt`)
- **What L3549 said:** "no iron hydroxylase" in comb jellies.
- **What a looser search finds:** **six phenylalanine 4-monooxygenase (PAH)** proteins whose iron site reads **C-H-E-L-I-G-H**. The I falls outside the frozen core [CVI]-H-E-[LI]-**[LM]**-G-H, so the tool missed them.
- **What it was a miss of:** the tool, not the biology.
- **What still holds:** no protein named tyrosine or tryptophan hydroxylase was found. So the comb jelly appears to lack the *dopamine and serotonin* enzymes but has the phenylalanine one.
- **The L3549 table** should read "Fe enzymes: PAH only (missed by the core rule)." Fix for a future rule: [LMI] at that position. That needs a blind test before use.

## 3. Pre-registered (`PREREGISTERED_L3553_kit_chordates_octopus.txt`)
**The animals:**

| species | group |
|---|---|
| **octopus** (*Octopus bimaculoides*) | protostome with an independently large brain |
| **sea squirt** (*Ciona intestinalis*) | chordate |
| **lancelet** (*Branchiostoma floridae*) | chordate |

**Predictions:**
- **K1–K9:** each has HCN pacemakers, K2P leak channels and an iron hydroxylase (the excitability kit).
- **K10:** the octopus has a DEKA sodium channel.
- **K11–K12:** the lancelet and the sea squirt have DEKA sodium channels. This tests where the chordate-line K begins, the question L3533 left open.

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A37653%20OR%20organism_id%3A7719%20OR%20organism_id%3A7739

**If it errors:** search `organism_id:37653 OR organism_id:7719 OR organism_id:7739` on uniprot.org and download it as TSV.

## Record
No predictions graded (the T-type check is not counted). **411 of 566 passed, plus 3 split.** K1–K12 are waiting.

## Summary
- **On ~15,000 vertebrate calcium channel sequences, the EEDD rule called T-type with no false calls** and found 92% of them. That makes it a reliable marker of the rhythm-generating calcium channel (not counted, because the file had been opened before).
- **Correction:** comb jellies do have a phenylalanine hydroxylase (C-H-E-L-I-G-H) that the iron rule missed. They still show no dopamine or serotonin enzyme.
- **The next blind test asks two things:**
  - do an octopus and two simple chordates carry the full rhythm-and-arousal kit;
  - do the chordates already have the sodium K that the sea urchin and acorn worm lack?

## Potential leads for future research
- **[K1–K12]** Grade when the file arrives.
- **[Iron core v3]** [LMI] at the fifth position. Development on all data, then a blind test.
- **[Manuscript 2]** Add the T-type split as a descriptive result.
