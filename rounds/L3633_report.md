# DCF L3633: Sodium rule v3 (T-W-K-G-W) is fixed with one change and no new false calls; a blind spiralian test is frozen; the sea urchin and Ciona have no NR1 in UniProt by full alignment
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [Sodium rule v3], [Sea urchin / Ciona NR1], [Twice lost?], [Calcium makes up for it?]. Development and descriptive work only. **No predictions graded.**

---

## 1. [Sodium rule v3] (development, `rounds/L3633_dev_sodium.txt`)
**Starting point:** the priapulid sodium channel reads T-**W**-K-G-W (L3629). Rule v2, [TS]-[FY]-[KR]-[GA]-W, did not allow W.

| try | sodium loop | changes across every set seen* | verdict |
|---|---|---|---|
| a | [TS]-[FYW]-[KR]-[GA]-W | 3: the priapulid channel → Na ✓; **2 horseshoe-crab T-type calcium channels → Na ✗** | rejected |
| b (**v3**) | [TS]-[FY]-[KR]-[GA]-W **or** [TS]-W-**K**-[GA]-W | **1: the priapulid channel → Na ✓** | kept |

\* Every set seen: human, mouse, zebrafish, chicken, fly, worm, Swiss-Prot Metazoa, and all UniProt files from L3501 to L3629.

- **Why try (a) failed:** both false calls matched S-W-**R**-[AG]-W in another part of the T-type channel, an arginine rather than the pore lysine.
- **Rule v3:** W is allowed only with the true **K** of DEKA.
- **Disclosure:** this is tuned on one priapulid channel plus two counter-examples. It needs the blind test below.
- **Files:**
  - `rounds/dcf_nerve_v3_L3633.py`;
  - `rounds/dcf_battery_v3_L3633.py` (the L3609 ratio with v3);
  - `rounds/dcf_l3633_blind.py`.

## 2. Pre-registered blind test of v3 (`PREREGISTERED_L3633_spiralia_rotifer.txt`)
**The animals:** three spiralians, unseen, including one miniaturised animal:
- *Helobdella* (leech, 6412);
- *Dimorphilus* (a ~1 mm annelid that has shrunk in evolution, 2664684);
- *Brachionus* (rotifer, 104777).

**Predictions:**
- **R1–R3:** each has ≥ 1 Na call.
- **R4–R6:** each ratio is above 1.8.
- **R7:** every Na call aligns nearest a mouse Scn rather than a calcium channel or NALCN.

**The question:** does size predict sodium loss outside moulting animals?

**Download links:**
- **Leech:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A6412
- **Dimorphilus:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A2664684
- **Rotifer:** https://rest.uniprot.org/uniprotkb/stream?format=tsv&compressed=true&fields=accession,organism_name,protein_name,sequence&query=organism_id%3A104777

## 3. [Sea urchin / Ciona NR1] (descriptive, after the L3625 grading)
| method | file | outcome |
|---|---|---|
| top 25 by shared 3-letter words with Grin1 | `L3633_nr1_search_v1_flawed.txt` | **flawed:** favoured giant proteins (titin, dyneins); **the Hydra positive control failed** |
| 600–1,600 aa, ranked by shared words per residue | `L3633_nr1_search.txt` | Hydra control **passed** (both full-length NR1s found), but the prefilter **missed even the known AMPA/kainate receptors** in the sea urchin and Ciona, so it is uninformative |
| **full alignment of every 600–1,600 aa protein to Grin1** | `L3633_nr1_full.txt` | **Ciona: 2,360 aligned; best Grin1 score 475. Sea urchin: 10,540 aligned; best 545.** |

**Reference scores against Grin1:**
- **true NR1s:** Hydra 1,616–1,766; sea hare about 2,120;
- **AMPA/kainate receptors:** the best sea-urchin and Ciona hits (475–545) are their known AMPA/kainate receptors.

**Conclusion:** **no NR1 exists in the UniProt proteomes of the sea urchin or Ciona.**
- **Either both lost it, or the gene is missing from the annotation.** Their relatives, the acorn worm and lancelet, do have NR1.
- **Telling these apart needs the genome-based RefSeq protein or mRNA files.** NCBI pages (assembly accessions as far as I know; tell me if a page is not found):
  - **Sea urchin:** https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000002235.5/ (Spur_5.0);
  - **Ciona:** https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000224145.3/ (KH).
  - On each page, "Download" → RefSeq **protein** FASTA is enough.

**Method lesson:** k-mer prefilters fail at this evolutionary distance, as in L3565. **Full local alignment, with a positive control, is the reliable search.**

## 4. [Twice lost?] and [Calcium makes up for it?]: status
- **Twice lost?** UniProt has **no proteome** for a velvet worm, nematomorph or kinorhynch, so the test cannot be run from UniProt.
  - The spiralian test (§2) asks the related size question outside moulting animals instead.
- **Calcium makes up for it?** UniProt files list isoforms as separate entries (e.g. the horseshoe crab has 20+ entries for few calcium genes), so channel counts per *gene* cannot be read from them.
  - **From L3621, by alignment:** the tardigrade carries Cav1, Cav2 and Cav3, one family each, like other invertebrates.
  - **There is no sign of extra calcium-channel families.** Gene-level counts need RefSeq.

## Record
No predictions graded. **456 of 619 passed, plus 3 split.** R1–R7 are waiting.

## Summary
- **Sodium rule v3** adds the T-W-K-G-W loop. Across every protein set seen, it changes exactly one call: the priapulid sodium channel. A broader first try made two false calls and was rejected.
- **A blind test of v3 is frozen** on a leech, a miniaturised annelid and a rotifer.
- **No NR1 in UniProt for the sea urchin or Ciona,** by a full alignment search with a working positive control. Loss or missing annotation is still open; the RefSeq protein files would settle it.
- **Two cheap search shortcuts failed and are recorded.**

## Potential leads for future research
- **[Spiralia]** Grade R1–R7 when the three files arrive.
- **[RefSeq NR1]** Sea-urchin and Ciona RefSeq protein FASTA; rerun the full Grin1 alignment.
- **[Phone v3]** Put dcf_nerve v3 into the phone bundle (6.15) and dcf-genefinder after it passes blind.
- **[Gene-level counts]** For [Calcium makes up for it?], collapse isoforms using RefSeq gene IDs.
