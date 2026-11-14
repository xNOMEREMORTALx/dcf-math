# DCF L3477: The worm's pump fixed, the nerve "battery balance" across six animals, and a blind test across all other animals in Swiss-Prot
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 14 November 2026

**Leads:** [Pump loop], [Battery balance], [Full worm proteome] (replaced, see §3). Development only. **No predictions graded.**

---

## 1. [Pump loop] (development)
- **The change:** the calcium-pump loop is widened from A-[IV]-P-E-G-L to **[AS]-[IV]-P-E-G-L**. The worm PMCA (mca-1) reads S-I-P-E-G-L.
- **Effect across six species:** mca-1 is now a calcium pump, and nothing else changed (no new mismatch).
- **Files:** `rounds/dcf_pump_L3477.py` and the v6 tool `rounds/dcf_neurochem4_L3477.py` (v5 + this loop).

## 2. [Battery balance]: dischargers (channels) vs chargers (metal pumps), descriptive
`rounds/L3477_battery.txt`, from v6 calls:

| species | Na | Ca | K | HCN | K2P | Na/K pumps | Ca pumps | Cu pumps | channels : pumps |
|---|---|---|---|---|---|---|---|---|---|
| zebrafish (complete) | 7 | 18 | 55 | 7 | 11 | 9 | 12 | 2 | 98 : 23 = **4.3** |
| chicken (complete) | 9 | 9 | 34 | 4 | 13 | 2 | 7 | 2 | 69 : 11 = **6.3** |
| fruit fly (complete) | 1 | 3 | 9 | 1 | 7 | 2 | 3 | 1 | 21 : 6 = **3.5** |
| mouse (files 1–3) | 9 | 10 | 38 | 4 | 14 | 6 | 9 | 2 | 4.4 |
| human (files 1–4) | 2 | 6 | 16 | 1 | 8 | 1 | 5 | 0 | 5.5 |
| worm (reviewed only) | **0** | 0 | 3 | 0 | 5 | 0 | 1 | 0 | 8 : 1 |

**Reading:**
- **The chargers are few and conserved.** Every complete animal set has 1–2 copper pumps, a handful of calcium pumps and a few Na⁺/K⁺ pumps.
- **The dischargers multiplied in vertebrates.** Vertebrates carry **4–6 channel genes per metal pump**, against 3.5 in the fly. Most of the extra is **potassium** channels: 34–55 in vertebrates against 9 in the fly.
- **One reading** is that richer nervous systems diversified the *release* side (many K⁺ channel types, each with its own timing) while keeping the *storage* side (pumps) nearly fixed. That shapes how fast, and in how many rhythms, the battery can discharge.
  - This is descriptive. Gene counts depend on genome duplication (the fish have extra copies), and the human and mouse sets are partial.

## 3. [Full worm proteome] replaced by a broader test
- **What I tried:** a full-worm test needs an independent truth for unreviewed proteins, i.e. InterPro IDs.
- **Why it isn't possible right now:** the InterPro service rate-limited my lookups, and one UniProt lookup returned an unrelated cached page. I could not verify the IDs reliably, so I did not freeze a test on them.
- **The broader test instead:** **every reviewed animal protein in Swiss-Prot, except the six species already used.**
  - That covers rat, cow, pig, frog, snails, squid, leech, jellyfish, other nematodes and more, all graded against UniProt's own curated families.
  - **Pre-registration:** `PREREGISTERED_L3477_metazoa.txt`, 14 predictions (M1–M14), including **two sharp controls:**
    - **M13:** no sodium-channel calls on any **nematode** entry;
    - **M14:** **no sodium↔calcium swaps** among all true sodium and calcium channels.
- **Disclosed:** many entries are close relatives (orthologs) of proteins already seen, such as rat and cow.

## Action for Gary: one file
https://rest.uniprot.org/uniprotkb/stream?format=tsv&fields=accession,organism_name,lineage,gene_primary,protein_families,sequence&query=(taxonomy_id:33208)+AND+(reviewed:true)+NOT+(organism_id:9606)+NOT+(organism_id:10090)+NOT+(organism_id:7955)+NOT+(organism_id:9031)+NOT+(organism_id:7227)+NOT+(organism_id:6239)&compressed=true

- **Size:** this one is larger, probably 20–40 MB compressed.
- **How to save:** keep it compressed. If the browser shows text instead of downloading, save the page as a file, as you did last time.

## Record
No predictions graded. **379 of 530 passed, plus 3 split.** M1–M14 are waiting.

## Summary
- **The worm's calcium pump is now read correctly,** with no side effects in any other species.
- **Across six animals, the nerve battery's chargers (metal pumps) are few and conserved,** while its dischargers (channels, especially potassium) multiplied in vertebrates to 4–6 per pump.
- **A test on all other animals in Swiss-Prot is frozen,** graded by UniProt, with controls for nematode sodium channels and sodium/calcium swaps.

## Potential leads for future research
- **[Metazoa]** Grade M1–M14.
- **[Per-phylum battery]** From the same file: channels per pump by phylum (sponges and placozoans have no nervous system; cnidarians have the first nerve nets).
- **[Earliest channels]** Sponges and comb jellies would show which metal gates existed before nerves evolved. This links to Gary's question about evolution and the origin of the nervous system.
- **[InterPro truth]** Retry the InterPro lookups later for a full-proteome worm test.
