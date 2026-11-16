# DCF L3673: A count-free "neural kit" rule (NR1 or a lysine sodium channel) separates animals with nerves from those without in 34 of 36 organisms; a five-organism blind test is frozen; Manuscript 2 v0.19
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Leads:** [Battery v2], [Manuscript 2]. Development and writing only. **No predictions graded.**

---

## 1. Development: the neural kit (`rounds/L3673_dev_features.txt`)
**The rule:** **kit present = NR1 ≥ 1 OR a lysine sodium channel (v3 call or partial).**

**Data:** all 36 organisms seen.
- NR1 counts were taken from the committed L3625 and L3669 outputs where available, and computed by the same method for the rest.

| group | organisms | kit present | correct |
|---|---|---|---|
| **no nerves** | 4 sponges, 2 placozoans, 2 choanoflagellates, *Capsaspora* | **0 of 9** | **9 / 9** |
| **nerves** | 27 animals, from cnidarians to vertebrates | **25 of 27** | **25 / 27** |

- **Misses:** the **comb jelly** and the **sea urchin.** Neither has NR1 or a lysine sodium channel; both carry only NAV2-type (E-loop) channels.
- **Why "NAV2 present" cannot be added:** choanoflagellates and placozoans also carry NAV2-type channels (L3501).

**Comparison with the battery ratio (cut 1.8) on the same organisms:**
- The ratio misclassifies the two tardigrades and placozoan H2.
- The kit catches all three:
  - the tardigrades have NR1;
  - H2 has neither feature.

**Reading:**
- **The two parts of the kit are the two signatures of fast neural signalling** in these data:
  - the NMDA "coincidence detector" (NR1);
  - the sodium spike channel with the lysine.
- **Every animal tested has at least one, except two:**
  - **comb jellies,** which built nerves independently;
  - **the sea urchin,** which lost NAV1 (L3561).

## 2. Pre-registered blind test (`PREREGISTERED_L3673_neural_kit.txt`, `rounds/dcf_kit_L3673.py`)
| # | organism | group | prediction |
|---|---|---|---|
| K1 | *Sphaeroforma arctica* | ichthyosporean, no nerves | kit **absent** |
| K2 | *Stylophora pistillata* | coral | kit present |
| K3 | *Schistosoma mansoni* | flatworm (parasite) | kit present |
| K4 | *Daphnia pulex* | water flea | kit present |
| K5 | *Acanthaster planci* | crown-of-thorns starfish | kit **absent**, the sea-urchin pattern; **this predicts a miss of the rule itself** |

**Download links** (by proteome):
1. ***Sphaeroforma*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000054560
2. ***Stylophora*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000225706
3. ***Schistosoma*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000008854
4. ***Daphnia*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000000305
5. ***Acanthaster*:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=proteome%3AUP000694845

**Check before sending:** if a file is only a few hundred bytes, UniProtKB has no entries for that proteome (as with H2). Tell me, and I'll give the UniParc link.

## 3. Manuscript 2 v0.19
- **§3.12 revised:** the battery ratio is fragile with few pumps (12 of 14 later ratio predictions passed; the placozoan H2 failed at 3.25 with 4 pumps). It is now framed as descriptive, and the count-free kit rule is introduced as under test.
- **§3.21 added:** placozoan H2.
- **Totals:** the table and abstract read **145/176**, matching the audit.
- **Reader brief:** updated to v0.19.

## Record
No predictions graded. **478 of 649 passed, plus 3 split.** Nerve-chemistry audit **145 of 176.**

## Summary
- **A count-free nervous-system test,** "NR1 or a lysine sodium channel present", is right for 34 of 36 organisms seen:
  - all 9 without nerves have neither;
  - 25 of 27 with nerves have one.
- **The two misses are explained:** comb jellies, an independent nerve lineage, and the sea urchin, which lost its sodium channel.
- **A blind test on five new organisms is frozen.** It includes an honest prediction that a starfish will be a miss.
- **Manuscript 2 now states the battery ratio's fragility.**

## Potential leads for future research
- **[Kit blind test]** Grade K1–K5 when the files arrive.
- **[Echinoderm kit]** If the starfish also lacks the kit, ask what echinoderm nerves use for fast signalling. Candidates: NAV2-type channels, calcium spikes, other glutamate receptor classes.
- **[RefSeq NR1 / lancelet exon]** These are still open, and both need RefSeq protein files.
