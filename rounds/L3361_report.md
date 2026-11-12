# DCF L3361: a eukaryote cut (0.0035) frozen and tested next on 7 fresh protists from UniProt, including *Naegleria*, an aerobe that carries anaerobic enzymes
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 12 November 2026

**Lead:** [Eukaryote scale]. **Pre-registration:** `PREREGISTERED_L3361_eukscale.txt` (`f0282f90…ffe4`), pushed before download.

All seven proteome IDs were checked in UniProt (organism, strain, protein count, reference status) before freezing.

---

## 1. The test
- **Cut:** 0.0035, between the lowest anaerobic parasite (*Trichomonas*, 0.0040) and the highest aerobe (*Tetrahymena*, 0.0029).
- **Species:** none was used before.

| group | organism (UniProt proteome, proteins) |
|---|---|
| anaerobes | *Spironucleus salmonicida* (UP000018208, 8,076); *Blastocystis hominis* (UP000008312, 5,820); *Cryptosporidium parvum* Iowa II (UP000006726, 3,805) |
| aerobes | *Leishmania major* (UP000000542, 8,039); *Trypanosoma brucei* (UP000008524, 8,588); *Chlamydomonas reinhardtii* (UP000006906, 18,840) |
| special case | ***Naegleria gruberi*** (UP000006671, 15,631): aerobic, but its genome encodes iron hydrogenase and PFOR |

| id | prediction |
|---|---|
| ES1 | the 0.0035 cut classifies ≥ 5 of the 6 correctly |
| ES2 | every anaerobe reads above every aerobe |
| ES3 | ***Naegleria* reads ≥ 0.0035**: the label comes from its enzymes, not its lifestyle |

**ES3 puts the repeated lesson from the low-oxygen failures into practice:** label genomes by their enzymes.

## Action for Gary: 7 downloads (UniProt)
Open each link; each downloads a compressed FASTA (`stream.gz`). Rename or zip them together as **`protists2.zip`**; each file says inside which organism it is.

1. Spironucleus: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000018208
2. Blastocystis: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000008312
3. Cryptosporidium: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000006726
4. Leishmania: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000000542
5. Trypanosoma: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000008524
6. Chlamydomonas: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000006906
7. Naegleria: https://rest.uniprot.org/uniprotkb/stream?format=fasta&compressed=true&query=proteome:UP000006671

## Record
No predictions graded. **314 of 448 passed, plus 3 split.**

## Summary
- **A eukaryote-specific cut is frozen** and will be tested on seven protists never used before.
- **One of them is a deliberate twist.** The oxygen-breathing amoeba *Naegleria* carries anaerobic enzymes, so the prediction is that it reads like an anaerobe. That would show the ladder follows enzymes, not lifestyle.

## Potential leads for future research
- **[Eukaryote scale]** Grade ES1–ES3 when the files arrive.
- **[Metagenome tier]**, **[Ladder-P]**, **[Venue]**: carried.
