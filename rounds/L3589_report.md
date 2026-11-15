# DCF L3589: The sea anemone's potassium channels are diverse (2 of 2), so the comb jelly's Shaker expansion is its own; phone 6.14 adds local alignment
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Leads:** [Other expansions], [Phone]. **Pre-registration:** `PREREGISTERED_L3589_anemone.txt`.

---

## Sea anemone (*Nematostella*) channels by nearest mouse channel (local aligner)
| subfamily | anemone | comb jelly (L3585) |
|---|---|---|
| Kv1 Shaker | 17 | **104** |
| Kv4 Shal | 9 | 9 |
| Kv3 Shaw | 8 | 3 |
| KCNH eag/erg/elk | 8 | 2 |
| Kv2 Shab | 2 | 1 |
| other (Kv6/9, Kv7) | 2 | 3 |
| K2P (leak) | 17 of 18 confirmed | 19 of 19 |
| **largest share** | **37%** | **85%** |

- **A1 (≥ 4 of Kv1, Kv2, Kv3, Kv4, KCNH present): 5 present, PASS.**
- **A2 (no subfamily > 60%): 37%, PASS.**

**Reading:**
- **The sea anemone's nerve net uses the full range of potassium-channel families,** as vertebrates do.
- **The comb jelly's piling-up of one subfamily (85% Shaker) is specific to its lineage.** That fits the idea that comb jellies built their nervous system along a separate path.

## Phone bundle 6.14
- **Menu 35 now asks "global or local."**
  - **Local** (Smith–Waterman) is for proteins of different lengths. It reports a score normalised by the self-scores.
- **A new self-test row:** a shared core scores the same inside a long and a short protein.
- **Self-test 267/267.**
- **Install:** copy all **ten** `.py` files into one folder and open `dcf_phone_6.14.py` (numpy needed for menu 35).

## Record
**+2 passed. 427 of 583 passed, plus 3 split.** Audit 99 of 117. Manuscript 2 is at **v0.13**.

## Summary
- **The sea anemone spreads its potassium channels across five families** (largest share 37%). The comb jelly packs 85% of its channels into one, Shaker. This contrast is now confirmed blind.
- **The phone can align proteins of any length** with the new local option.

## Potential leads for future research
- **[Outside reader]** Manuscript 2 v0.13 (five figures, 99/117 audited).
- **[Placozoan and sponge K sets]** Name them the same way to see the potassium repertoire before nerves.
- **[Manuscript 2 Figure 6]** Subfamily bars: comb jelly vs anemone vs mouse.
