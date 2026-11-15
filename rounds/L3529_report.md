# DCF L3529: The acoel copper pump has one copper repeat; a pre-registered test of when K arose
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Hofstenia copper pump], [E→K dating]. **No predictions graded.**

---

## 1. [Hofstenia copper pump] (descriptive; `rounds/L3529_hofstenia_cu.txt`)
- **Why none was called:** *Hofstenia* has one P-type pump with the copper **C-P-C** site (HMIM002426, 1,091 aa), but only **one** G-M-x-C-x-x-C copper-binding repeat. The rule asks for ≥ 2, so it was filed "other."
- **What it probably is:** the worm's ATP7 copper pump. Either its gene has a single repeat or the gene model is incomplete.
- **This is a known kind of miss,** not a new error type. A rule needing one repeat with C-P-C could be tested on the next blind set.

## 2. [E→K dating] Pre-registered (`PREREGISTERED_L3529_EK_dating.txt`)
**The hypothesis**, from the E-readers so far (choanoflagellate, placozoan, sea anemone, comb jelly, acoel worm) and the K-readers (fly, nematode lineage, vertebrates): **K arose in the ancestor of the protostomes and deuterostomes.**

**The test** uses four new bilaterians, two on each side of that split:

| species | group | side |
|---|---|---|
| *Lingula anatina* | brachiopod | protostome |
| *Capitella teleta* | annelid worm | protostome |
| *Saccoglossus kowalevskii* | acorn worm | deuterostome |
| *Strongylocentrotus purpuratus* | sea urchin | deuterostome |

**Predictions:**
- **D1–D4:** each has at least one sodium (DEKA) call.
- **D5:** each has at least one A-T-F-**K**-G-W loop.
- E-type paralogs may coexist. They are reported, not graded.

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A7574%20OR%20organism_id%3A283909%20OR%20organism_id%3A10224%20OR%20organism_id%3A7668

**Size:** probably 30–60 MB. **If it errors:** search `organism_id:7574 OR organism_id:283909 OR organism_id:10224 OR organism_id:7668` on uniprot.org and download it as TSV.

## Record
No predictions graded. **406 of 558 passed, plus 3 split.** D1–D5 are waiting.

## Summary
- ***Hofstenia*'s copper pump is present** but carries one copper repeat instead of two, so the rule passed it over.
- **A frozen test now asks whether the K appears on both sides of the protostome/deuterostome split** (brachiopod, annelid, acorn worm, sea urchin). That would date the fast nerve sodium channel to their common ancestor.

## Potential leads for future research
- **[E→K dating]** Grade D1–D5.
- **[Cu pump rule]** C-P-C plus one repeat (development on all data, then blind).
- **[Outside reader]** For both manuscripts.
