# DCF L3577: Naming unnamed genes by alignment. 6 of 6 described genes get the right subfamily (1 of 1 pass), and 4 undescribed zebrafish genes now have proposed names
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Lead:** [Naming unnamed genes].
- **Pre-registration:** `PREREGISTERED_L3577_nameunnamed.txt`.
- **Script:** `rounds/dcf_nameunnamed_L3577.py` → `rounds/L3577_grade_output.txt`.

---

## Method
1. **Pick the genes:** unnamed zebrafish genes (LOC/si:) that the v8 rule calls potassium or HCN.
2. **Align:** each one is aligned with `dcf_align` against all 42 mouse voltage-gated K and HCN channels.
3. **Name:** the nearest mouse channel's subfamily becomes the proposed name.
4. **Grade:** where NCBI's description names a subfamily, it serves as the truth.

## Results
| zebrafish gene | nearest mouse channel (identity) | NCBI description | agrees |
|---|---|---|---|
| LOC100004160 | Kcna5 (71%) | K channel subfamily A | ✓ |
| LOC100330283 | Kcna2 (83%) | subfamily A | ✓ |
| LOC100536252 | Kcna2 (79%) | shaker-related (A) | ✓ |
| LOC100537815 | Kcna2 (90%) | subfamily A | ✓ |
| LOC567521 | Kcna2 (68%) | subfamily A | ✓ |
| LOC101885373 | Hcn2 (77%) | hyperpolarization-activated (HCN) | ✓ |

**U1 (≥ 80% agree): 6 of 6, PASS.**

**Proposed names for the four genes NCBI does not describe:**

| gene | nearest mouse channel | proposed identity |
|---|---|---|
| **si:ch73-334d15.4** | **Kcnc3** (51%) | a **Kv3 (Shaw-type)** channel. This is the gene behind the zebrafish failure in L3441; the 4-mer guess (Kcnc) is now confirmed by alignment |
| LOC101882339 ("uncharacterized") | Hcn3 (78%) | an **HCN pacemaker** |
| si:dkey-43k4.5 | Kcns1 (59%) | a **Kv9 (silent modifier)** subunit |
| si:rp71-39b20.4 | Kcnv2 (49%) | a **Kv8 (silent modifier)** subunit |

## Record
**+1 passed. 423 of 579 passed, plus 3 split.** Audit: 95 of 113.

## Summary
- **The DCF aligner can name genes NCBI leaves unnamed.** All 6 described unnamed zebrafish channels got the subfamily NCBI gives them.
- **Four undescribed genes now have proposed identities:** a Kv3 channel, an HCN pacemaker, and two silent modifier subunits.
- **The zebrafish "false call" of L3441 is, by alignment, a Kv3 potassium channel.** That supports the earlier reading that the frozen failure was a naming gap, not a biology error. The failure still stands.

## Potential leads for future research
- **[Annotator]** Add a `--name` option to `dcf_nerve`: every unnamed call gets its nearest reference, with identity.
- **[Comb-jelly 123 K channels]** Name them by nearest mouse/fly channel and see which subfamilies expanded.
- **[Outside reader]** Manuscript 2.
