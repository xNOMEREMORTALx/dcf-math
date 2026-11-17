# DCF L3769: Cryptochromes outside animals (2 of 4). The green alga's animal-like cryptochrome also reads Y at the fourth position, and a robin-only reference misses distant kingdoms
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Data:** Gary's zip (`cryptochrome`), four files. Each was identified by header:
- *Chlamydomonas reinhardtii*, green alga: 18,840 proteins;
- *Neurospora crassa*, fungus: 10,255;
- *Phaeodactylum tricornutum*, diatom: 10,461, **sent twice** (identical MD5), so one copy was used.

**Procedure:**
1. **Frozen files:** `PREREGISTERED_L3765_cry_outgroups.txt`, `rounds/dcf_cry_outgroup_L3765.py` and `rounds/dcf_cry_full_L3761.py`; hashes matched.
2. **Output:** `rounds/L3769_tool_output.txt`. **Grading:** `rounds/L3769_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| O1 | each organism has ≥ 1 hit | **FAIL:** *Neurospora* 0 |
| O2 | *Neurospora* has a DASH-type hit without W at TrpD | **FAIL** (no hit) |
| O3 | the alga has an animal-like cryptochrome with W at A, B, C | **PASS:** A8J8W0 reads **WWW-Y**, nearest mouse CRY2 |
| O4 | ≥ 1 hit reads Y or F at TrpD | **PASS:** the same algal protein |

**2 of 4 passed.**

## Descriptive, after grading
| organism | hit | UniProt name | tetrad | nearest |
|---|---|---|---|---|
| alga | A8J8W0 (595 aa) | uncharacterised (likely the algal "animal-like" cryptochrome) | **WWW-Y** | CRY2 |
| alga | A0A2K3E0E6 | cryptochrome DASH | WWW-G | cry-dash |
| diatom | B7FZ64 | cryptochrome photolyase family 1 (CPF1) | **WWWW** | CRY1 |
| fungus | none | | | |

- **Missed named family members, all with local score below 350 against robin CRY4:**
  - the alga's DNA photolyase and four "photolyase/cryptochrome α/β" proteins;
  - the fungus's DNA photolyase and **"putative cryptochrome DASH"** (Q7SI68);
  - the diatom's DASH, a DNA photolyase and three more.
- **A single animal-cryptochrome reference loses sensitivity in distant kingdoms.** The fungus's "no hit" is a finder limit, not an absence (Standing rule 5).

## Reading
**The fourth position, across eukaryotes so far:**

| lineage | animal-like CRY / CRY1–2-like | DASH |
|---|---|---|
| diatom | W (CPF1) | (missed) |
| green alga | **Y** | G |
| single-celled relatives of animals | **Y, Y, F** | |
| sponges and most animals | **W** | G |

- **An aromatic Y at TrpD now appears in a green alga as well** as in the single-celled relatives of animals. W appears in the diatom's CPF1 and in animals.
- **The fourth position is not a clean animal/non-animal split.** It is either W or an aromatic Y/F in the animal-like cryptochrome lineage, and G in DASH.
- **A tyrosine can relay electrons,** so these may be functional four-step chains of a slightly different design. Untested.

## Record
**+2 passed, 2 failed. 526 of 726 passed, plus 3 split.** Audit **193 of 253.**

## Summary
- **Outside animals:**
  - the diatom's animal-like cryptochrome (CPF1) carries all four tryptophans;
  - the green alga's carries a tyrosine at the fourth position, like the cryptochromes of animals' single-celled relatives.
- **The fungus gave no hit,** because a robin-only reference misses distant family members (several named photolyases and DASH proteins scored below the floor).
- **Score:** 2 of 4 predictions passed.

## Potential leads for future research
- **[Multi-reference finder]** Add a plant cryptochrome, a CPD photolyase and a fungal DASH as references, with measured sensitivity on the named members found here (the must-find list is now known).
- **[Manuscript 4]** Add the outgroup table (v0.2).
