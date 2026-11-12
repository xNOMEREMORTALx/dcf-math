# DCF L3301: the nervous system's electrical parts list from raw human mRNA (19 of 19 channels sorted correctly by shape); the potassium filter's blind spot found (Kv3/Kv4 T-T-L-G-Y-G); the intein link does not work with short motifs (1 of 20); shh.zip held the wrong files
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Data:**
- `shh.zip` held five **blind_22 genomes** (NC_010337, NC_013512, NC_009662, NC_009663, NC_005090; 5–8 MB each), not the five SHH files.
- The SHH test (L3297) is still waiting; nothing was graded.

**Leads pursued:** [Neuro map], [Hint/intein]. All work here is development on data already seen; no new predictions were graded.

---

## 1. [Neuro map] The nervous system's electrical parts list [development, descriptive]
**Method.**
- Human mRNA files 1–4, 9,632 genes, one transcript each.
- Every protein carrying the **voltage sensor** (the motif that passed blind in L3293) is sorted **by shape only**:
  - 4-domain (≥ 1,500 aa) = sodium/calcium type;
  - one domain with a K⁺ filter = potassium type;
  - the filter C-I-G-Y-G = HCN type.
- Gene names were read only afterwards, to check.

| class (by shape) | genes | by name afterwards |
|---|---|---|
| **Na/Ca 4-domain** | 9 | **6 calcium** (CACNA1B, D, E, G, H, I), **3 sodium** (SCN2A, SCN7A, SCN11A) |
| **K-type** | 9 | **9 potassium** (KCNB2, KCNF1, KCNH1, H5, H6, H7, KCNS1, S2, S3) |
| **HCN-type** | 1 | **HCN3** (the "pacemaker" channel) |
| other | 5 | 3 potassium (KCNC2, KCNC4, KCND1), 2 not channels (DDX47, ZNF670) |

**Reading.**
- **All 19 shape-sorted proteins are in the right class, and 22 of the 24 voltage-sensor proteins are real ion channels.**
- **From mRNA sequence alone, the tool lays out the excitable-membrane machinery:**
  - the calcium channels that release neurotransmitter at synapses (CACNA1B = N-type, CACNA1E = R-type);
  - the T-type calcium channels behind rhythmic firing (CACNA1G, H, I);
  - the sodium channel of brain neurons (SCN2A) and of pain nerves (SCN11A);
  - potassium channels that reset the membrane after each impulse, and the HCN pacemaker.
- **Why three K⁺ channels fell into "other":** Kv3 and Kv4 channels (KCNC2, KCNC4, KCND1) have the filter **T-T-L-G-Y-G**. Leucine sits where the frozen filter only allows V/I/T. This explains part of the L3293 N1 shortfall.
- The corrected filter **[TSC]-[VITL]-G-[YF]-G** is added to the motif scanner as a new preset `k_filter2`, marked **untested**. The frozen `k_filter` is unchanged.

## 2. [Hint/intein] The hedgehog–intein bridge [development, failed]
- Hedgehog's self-cutting half has the same fold (Hint) as inteins, the self-splicing protein pieces of bacteria and archaea.
- **Test:** 31,401 annotated proteins from nine seen genomes, 20 of them annotated as intein-related. A short-motif signature built from the classic intein blocks (N-terminal C/S, T-x-x-H, H-N-C/S/T) was scanned across them.
- **Result:** at best **1 of 20 found**; the loose version made 28 false hits.
- **Why:**
  - several "intein" annotations are split halves (trans-splicing DnaE) or "intein-prone" helicases with no intein;
  - the Hint fold is too varied for short exact motifs, and needs a profile (HMM) method.
- **Closed for the motif approach.** The bridge stays a literature fact (shared Hint fold), not a DCF tool.

## 3. Tools
- **`dcf_motif_scan.py`** gains preset `k_filter2` (SHA-256 `70081f8f…a08c`). The hedgehog preset used for the frozen SHH test (S1) is unchanged.
- **Phone bundle `dcf_phone_bundle_6.09b.zip`:** the same 6.09 toolkit (263/263) with the updated scanner.

## Action for Gary: the SHH files again
The zip contained older downloads with similar names. The five SHH files are **small (about 3–25 KB each)**. Each saves as a text file starting with `>`, not `LOCUS`.
1. Open each link below once.
2. In the **Files** app, open **Download** and **sort by date (newest first)**.
3. Select the **5 newest files**; each is under 30 KB. Zip them as **`shh.zip`**.

Links:
1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NM_000193
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NM_021044
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NM_009170
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NC_000007.14&seq_start=155794980&seq_stop=155817463
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=fasta&retmode=text&id=NC_000071.7&seq_start=28656813&seq_stop=28677254

**Tip:** deleting old `.pending-…sequence.gb.txt` files from Download first makes the new ones easy to spot.

## Record
No predictions graded this round. **306 of 434 passed, plus 3 split.**

## Summary
- **We can now list the nervous system's electrical parts from raw human mRNA.** The voltage-sensor motif found 24 proteins, 22 of them real ion channels. Sorting them by shape alone put all 19 sortable ones in the right family: calcium, sodium, potassium and the HCN pacemaker.
- **The potassium filter's blind spot is found:** a family of K⁺ channels (Kv3/Kv4) uses leucine in the filter. A corrected version is in the scanner, untested.
- **The hedgehog–intein bridge cannot be built with short motifs** (1 of 20 found). Closed for this method.
- **The SHH test is still waiting:** the zip held five old genome files. The five SHH files are small, so sorting Download by newest makes them easy to find.

## Potential leads for future research
- **[SHH]** Grade S1–S5 when the correct `shh.zip` arrives.
- **[Neuro b]** Pre-register `k_filter2` and the corrected Cys-loop on **mouse** mRNA (RefSeq M_musculus/mRNA_Prot files 1–2), with the shape classes as predictions.
- **[Neuro map +]** Add the Na⁺ vs Ca²⁺ split label-free from the pore loops (sodium DEKA vs calcium EEEE selectivity rings); develop on files 1–4.
- **[Enzyme labels]** Carried: freeze an enzyme-based label rule before the next band test.
