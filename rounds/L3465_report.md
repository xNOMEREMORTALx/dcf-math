# DCF L3465: Blind test in the fruit fly. The core metal gates hold (calcium, sodium, potassium, pumps), but several vertebrate-tuned motifs break across ~600 million years: 5 of 13 gradeable predictions pass
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Data:** `GCF_000001215.4_Release_6_plus_ISO1_MT_rna.fna.gz`.
- 23.5 MB, 30,789 NM_ records, all *Drosophila melanogaster*.
- 13,864 genes, one transcript per gene (longest reading frame).

**Procedure:**
1. Five frozen hashes matched.
2. Tool output (no names) committed and pushed first.
3. Graded with the frozen truth rule v3: `rounds/L3465_grade.py` → `rounds/L3465_grade_output.txt`.

---

## Results (PREREGISTERED_L3461_fly)
| # | prediction | result | cause of failure |
|---|---|---|---|
| F1 | calcium-channel calls | **3/3 PASS** (cac, Ca-alpha1D, Ca-alpha1T) | |
| F2 | sodium-channel calls | **1/1 PASS** (para, the fly's only Na channel) | |
| F3 | potassium/HCN calls | 7/8 **FAIL** | *truth rule:* the extra call, **Shawl** ("Shaw-like"), is a K channel the frozen list didn't name |
| F4 | channel genes found (≥ 75%) | **11/13 PASS** | |
| F5 | K2P calls | 1/3 **FAIL** | two uncharacterized proteins (CG42340, CG43155); nature unknown |
| F6 | K2P genes found (≥ 50%) | 1/5 **FAIL** | *real:* the fly leak channels break the rule (see below) |
| F7 | glutamate-receptor calls | 11/14 **FAIL** | *truth rule:* Ekar ("eye-enriched **kainate receptor**"), Ir25a (an ionotropic-receptor family member), CG11155 (uncharacterized) |
| F8 | glutamate receptors found | **11/12 PASS** | |
| F9 | NMDA calls | 1/3 **FAIL** | *real:* Ekar and Ir25a also carry A-S-Y-T-A-N-L |
| F10 | NMDA receptors found (100%) | 1/2 **FAIL** | *real:* fly Nmdar2 reads **I**-Y-T-A-N-L |
| F11 | iron-hydroxylase calls | 1 call (Trhn, correct): ungradeable | |
| F12 | iron hydroxylases found | 0/3 **FAIL** | *real* and *truth-list error* (below) |
| F13 | pump calls | 5/6 **FAIL** | *truth rule:* **JYalpha** is a Na⁺/K⁺-pump α paralog (loop A-N-V-P-E-G-L-L, same as Atpalpha), not in the frozen list |
| F14 | named pumps given their own metal | **5/5 PASS** (Atpalpha, SERCA, PMCA, SPoCk, ATP7) | |

**5 of 13 gradeable predictions pass. All 8 failures stand as frozen.**

## Reading: what holds and what breaks across ~600 million years
**What holds (the core metal gates):**
- **Calcium:** all three fly calcium channels read by their EEEE/EEDD rings.
- **Sodium:** the fly's single sodium channel, para, read by its DEKA lysine.
- **Potassium:** eight potassium channels read by their filters: Sh, Shal, Shaw, Shawl, eag, sei, Elk, KCNQ.
- **Pumps:** every named pump got its own metal: Na⁺/K⁺ (Atpalpha, plus JYalpha), calcium (SERCA, PMCA, SPoCk), copper (ATP7).
- **The selectivity loops for K⁺, Na⁺, Ca²⁺ and the pump helix-4 loop are the same kinds in insects and vertebrates.**

**What breaks (five real failures, all in motifs tuned on vertebrates):**
1. **NMDA7 is not NMDA-specific in insects.** The fly kainate receptor Ekar and the ionotropic receptor Ir25a share A-S-Y-T-A-N-L, and fly Nmdar2 has I-Y-T-A-N-L. In insects, the residue before the gate does not separate NMDA from other glutamate receptors.
2. **The iron site has drifted, but its iron ligands have not:**
   - ple (tyrosine hydroxylase): **S**-H-E-L-L-G-H;
   - Hn (henna, phenylalanine hydroxylase): C-H-E-L-**M**-G-H;
   - Trhn (tryptophan hydroxylase): C-H-E-L-L-G-H (found).
   
   The two iron-binding histidines (H-x₄-H) are present in all three. Only the flanking letters changed.
   - **There was also a truth-list error.** I listed "trh" (which is *trachealess*, a transcription factor) instead of **Trhn**. The recall denominator was wrong. With the correct set {ple, Hn, Trhn} the result would be 1/3, still a failure.
3. **The leak (K2P) rule fails in flies:**
   - Ork1 (1,019 aa) and galene (729 aa) exceed the 700-aa limit;
   - sand and Task7 have one filter outside T-[VIT]-G-[YFL]-G (S-S-I-G-F-G, or one filter only).
4. **The length cut misfiled Shab.** Its longest isoform is 1,607 aa, so it went to the 4-domain branch as "undecided," though it is a 1-domain K channel.
5. **Ih (the fly HCN) was missed.** It has C-I-G-Y-G but no full voltage sensor, and the weak-sensor route does not accept the HCN filter.

**Truth-rule failures (3: F3, F7, F13):** Shawl, Ekar/Ir25a and JYalpha are a K channel, glutamate-family receptors and a Na⁺/K⁺ pump by their own descriptions. The frozen fly name list was incomplete. The failures stand.

## Running tally of the nerve-chemistry blind tests
| species | distance | gradeable passed |
|---|---|---|
| mouse | ~90 My | 10/10 |
| zebrafish (curated + predicted) | ~450 My | 17/21 |
| chicken | ~310 My | 13/14 |
| **fruit fly** | **~600 My** | **5/13** |
| **total** | | **45/58** |

**The pattern is clear:** the core selectivity loops carry across all animals, while finer motifs tuned on vertebrates (NMDA, the iron-site flanks, K2P limits) break in insects. That boundary is itself a result for Manuscript 2.

## Record
**+5 passed, 8 failed** (F11 ungradeable). **370 of 521 passed, plus 3 split.**

## Summary
- **The fly confirms the core:** calcium, sodium and potassium channels, and the pumps that charge the nerve battery, are read from mRNA by the same metal loops as in vertebrates, ~600 million years apart. Every calcium, sodium and named-pump call was right.
- **Five finer motifs, all tuned on vertebrates, failed in the insect:**
  - the NMDA motif is shared with insect kainate receptors;
  - the iron-site flanks drifted, though the iron-binding histidines did not;
  - the K2P limits don't fit fly leak channels;
  - one length cut misfiled a long potassium isoform;
  - the fly HCN was missed.
- **Three failures were the frozen name list's fault, and one truth-list entry was wrong** (trh for Trhn). These are lessons for the next truth rule; all failures stand.

## Potential leads for future research
- **[Iron core]** An iron-site finder built only on the conserved **H-x₄-H inside H-E-[LI]-[LM]-G-H**. Develop on mouse, fish, bird and fly, then test on a new lineage (e.g. a nematode or mollusc).
- **[Length-free channels]** Replace the 1,500-aa cut with a count of voltage sensors or pore loops (4-domain = four pore loops), so long isoforms of 1-domain channels are not misfiled.
- **[HCN route]** Let the weak-sensor route accept the C-I-G-Y-G filter.
- **[Insect K2P]** Develop a fly-aware leak-channel rule (two filters, no length limit, S/T-x-I-G-F/Y-G).
- **[Truth from sequence]** Grade future tests against an independent reference (e.g. InterPro/Pfam domain annotations), so the truth no longer depends on hand-written name lists. This is the main lesson of four rounds.
- **[Manuscript 2]** Add the fly as §3.7: "what holds and what breaks."
