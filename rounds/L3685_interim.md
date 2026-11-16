# DCF L3685 (interim): Parasite or flatworm? A four-flatworm test is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Lead:** [Free-living flatworm]. **No predictions graded.**

**The question:** the blood fluke *Schistosoma mansoni* has no NAV-family channel and no strong NR1 in UniProt (L3681). Is that a **parasite** trait or a **flatworm** trait?

**Data available:** UniProt has no planarian (*Schmidtea*) proteome. It does have the free-living *Macrostomum lignano* and many parasites.

**Frozen:**
- **Pre-registration:** `PREREGISTERED_L3685_flatworms.txt`.
- **Script:** `rounds/dcf_flatworm_L3685.py`. It uses the floored NR1 caller and adds a **NAV-family** count (a four-domain channel nearest a mouse Scn, score ≥ 1,000).
- **Check on the seen *S. mansoni* (not a test):** NR1 0, Na 0, NAV-family 0, kit absent. This reproduces L3681.

| # | organism | lifestyle | prediction |
|---|---|---|---|
| F1 | *Macrostomum lignano* | free-living | kit present |
| F2 | *Macrostomum lignano* | free-living | ≥ 1 NAV-family channel |
| F3 | *Fasciola hepatica* | liver fluke | kit absent |
| F4 | *Echinococcus multilocularis* | tapeworm | kit absent |
| F5 | *Schistosoma japonicum* | blood fluke | kit absent |
| F6 | the three parasites together | | 0 NAV-family channels |

**Files needed:** UniProt proteomes UP000095280, UP000230066, UP000017246 and UP000311919. The links were sent in chat.

## Record
No predictions graded. **482 of 654 passed, plus 3 split.**

## Summary
- **A test of whether flatworm parasites lost the fast-signalling kit (the sodium spike channel and NR1) is frozen,** with a free-living flatworm as the comparison.

## Potential leads for future research
- **[Flatworms]** Grade F1–F6 when the files arrive.
- **[Urchin NR1]** RefSeq protein for *S. purpuratus*.
