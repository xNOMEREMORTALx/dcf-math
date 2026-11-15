# DCF L3605: Sponges and a placozoan, blind. EAG-type K channels and no fast sodium channel, as predicted, but no confident Shab (2 of 3). Without nerves, the battery has many chargers and almost no dischargers
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Data:** `27.gz` (26 MB), 111,584 UniProt proteins from 835 organisms.
- **Mostly sponges:** *Geodia* 60,924; *Ephydatia* 30,399; *Oopsacas* 16,366.
- **Plus:** 134 from a placozoan (*Placozoa* sp. H4).
- **No** *Amphimedon* or *Trichoplax* entries, as specified.

**Procedure:** hashes matched; the frozen `rounds/dcf_nonneural_L3597.py` → `rounds/L3605_grade_output.txt`.

---

## Results (PREREGISTERED_L3597_nonneural)
| # | prediction | result |
|---|---|---|
| B1 | a Kv2 (Shab) channel named (local score > 300) | **FAIL**: the only Shab-like hit scores 125 (*Ephydatia*, below the threshold) |
| B2 | a KCNH (EAG-type) channel named | **PASS**: *Oopsacas* A0AAV7K069 → Kcnh6 (score 427) |
| B3 | no DEKA sodium channel | **PASS**: 0 |

**2 of 3 pass.**

## Reading (follow-up after grading; `rounds/L3605_followup.txt`)
| | count across 111,584 sponge proteins |
|---|---|
| voltage-gated K calls | **2** |
| K2P leak calls | 4 (two named confidently: Kcnk16-like, Kcnk10-like) |
| calcium channel | 1 |
| **metal pumps** | **36** (Na⁺/K⁺ 8, Ca²⁺ 21, Cu 7) |
| iron hydroxylases | 4 |

- **Sponges carry very few channels:** two voltage-gated K channels in three large proteomes. One is EAG-type, as predicted. A Shab-like protein is present but too divergent or fragmentary to name confidently, so B1 fails.
- **The nerve battery without nerves:**
  - **chargers:** 36 metal pumps;
  - **dischargers:** about 7 channels;
  - **ratio:** about 0.2 channels per pump, against 3.5–13 in animals with nerves (L3477, L3549).
- **What that means:** animals without nerves keep the energy-storage side (pumps) but have almost none of the fast-release side. **The arrival of nerves coincides with a large expansion of channels, not of pumps.**

## Record
**+2 passed, 1 failed. 432 of 590 passed, plus 3 split.**

## Summary
- **In more than 100,000 sponge proteins, the predictions held for EAG-type potassium channels and for the absence of a fast sodium channel.** The predicted Shab-type channel was not confidently found, so that prediction failed.
- **Sponges have dozens of metal pumps but only a handful of channels:** about 0.2 channels per pump, against 3.5–13 in animals with nerves. The battery's chargers came first; the dischargers multiplied with nerves.

## Potential leads for future research
- **[Battery ratio as a test]** Pre-register "channels per pump < 1 in every animal without nerves, > 2 in every animal with nerves." It can be checked on lineages not yet used, e.g. a mesozoan, or a choanoflagellate other than *Monosiga*.
- **[Figure 7]** Channels per pump across all lineages, from sponge to mouse.
