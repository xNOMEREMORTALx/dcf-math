# DCF L3669: A second placozoan (3 of 5). Its full-length NALCN reads the calcium-like E-E-E-E, supporting the "calcium leak first" hypothesis; its glutamate receptors are all kainate-like (no NR1); its battery ratio of 3.25 breaks the 1.8 cut
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Data:** *Trichoplax* sp. H2 (proteome UP000253843), three tries:

| try | file | outcome |
|---|---|---|
| 1 | UniProtKB file | **empty** (58 bytes): UniProtKB holds no entries for this organism |
| 2 | `stream.gz` | **wrong organism** (*Trichomonas vaginalis*, 50,190 entries): **dropped, nothing run** |
| 3 | `stream_1.gz` | **correct:** UniParc FASTA, 12,150 `UPI` sequences (the proteome lists 12,174; UniParc stores identical sequences once) |

**Procedure:**
1. **Amendment before data:** `AMENDMENT_L3669_placozoa_H2.txt` switched the data source to UniParc, converted by `rounds/fasta_to_tsv_L3669.py`. Predictions and script unchanged.
2. **Frozen files:** all hashes matched the ledger.
3. **Tool output:** `rounds/L3669_tool_output.txt`, pushed before grading.
4. **Grading:** `rounds/L3669_grade_output.txt`.
5. **No protein names exist in UniParc FASTA,** so the descriptive part uses the tool's classes only.

---

## Results
| # | prediction | result |
|---|---|---|
| T1 | ≥ 1 NALCN | **PASS:** 1, full-length (1,855 aa, score 2,933) |
| T2 | NALCN E-E-E-E | **PASS:** **E-E-E-E** |
| T3 | ≥ 1 NR1 call | **FAIL:** 8 glutamate receptors, all nearest **kainate** (Grik1/2/5) |
| T4 | ratio < 1.8 | **FAIL:** 13 / 4 = **3.25** |
| T5 | no Na call | **PASS** |

**3 of 5 passed.**

## Descriptive, after grading
| | *T. adhaerens* (L3613) | *T.* sp. H2 |
|---|---|---|
| proteins | 11,520 | 12,150 |
| K channels | 5 | 7 |
| leak K2P | 1 | 3 |
| Ca channels (L/P type, T-type) | 1 + 1 | 2 + 1 |
| **channels** | **8** | **13** |
| Na/K, Ca, Cu pumps | 1, 3, 1 | 1, 2, 1 |
| **metal pumps** | **5** | **4** |
| **ratio** | **1.60** | **3.25** |

- **Glutamate receptors:** the first placozoan's receptors were fragments (L3625). H2's are full length (691–947 aa), and **still none is NR1-like.** All 8 align nearest kainate receptors.
  - **The L3625 failure was therefore not a fragment artefact.** Placozoans appear to lack NR1.
  - **NR1 then first appears in cnidarians in these data.** Placozoans, which lack neurons, have only kainate-like receptors.

## Reading
- **The calcium-leak-first hypothesis passed its test.** The placozoan's full-length NALCN reads **E-E-E-E**, like the sponge's and the cnidarians'.
  - **In every non-bilaterian tested, the leak channel is calcium-like.** The sodium-like lysine appears only in bilaterians, at two positions.
- **The battery cut (1.8) has now failed on a non-neural animal.**
  - **Placozoans have no nervous system, but H2 scores 3.25** with only 4 metal pumps. One pump more or less moves the ratio between about 2.6 and 4.3.
  - **The ratio is unstable when pump counts are this small.** Battery-ratio predictions have now passed **12 of 14** blind tests:
    - 4 of 5 in L3613 (*Hypsibius* the miss);
    - the second tardigrade, predicted *below* the cut as a sodium-less animal;
    - 7 in the moulting animals, spiralians and rotifers;
    - this placozoan, which failed.
  - **It is not a reliable classifier for small genomes.
  - **The ratio should be reported with its counts,** and a rule based on channel *types* (for example a sodium channel or NR1 present) may separate the groups better than a ratio.
- **NR1 vs nerves holds up:** sponges, comb jelly and both placozoans have no NR1; cnidarians and all bilaterians tested except the sea urchin and Ciona have it.

## Record
**+3 passed, 2 failed. 478 of 649 passed, plus 3 split.** Nerve-chemistry audit **145 of 176.**

## Summary
- **A second placozoan, read from UniParc after two bad downloads, passed 3 of 5 predictions.**
- **Its full-length NALCN leak channel reads E-E-E-E (calcium-like).** Every non-bilaterian NALCN tested is calcium-like, which supports the idea that the sodium-like leak evolved later, in bilaterians.
- **Its full-length glutamate receptors are all kainate-like.** Placozoans really lack the NMDA NR1 subunit; it was not a fragment problem.
- **Its battery ratio (3.25, from only 4 pumps) breaks the 1.8 cut.** The ratio is fragile when pump counts are small.

## Potential leads for future research
- **[Battery v2]** Pre-register a classifier that does not depend on a small denominator. Candidates:
  - "NR1 present";
  - "lysine sodium channel or NR1 present";
  - a ratio with a minimum pump count.
  
  Test it on all organisms seen, then blind.
- **[Manuscript 2]** §3.21 placozoan H2. Revise the battery-ratio claim in the abstract and §3.12 to state its fragility honestly.
- **[RefSeq NR1 / lancelet exon]** These are still open, and both need RefSeq protein files.
