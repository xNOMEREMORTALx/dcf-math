# DCF L3813: the cryptochrome reader is 25× faster and identical on all 63 blind hits (phone 6.18)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Phone app:** `phone/dcf_phone_6.18.py`.
- **Reader module:** `phone/dcf_cryreader.py`, also in dcf-genefinder, unreleased, for v1.2.0.
- **Bundle:** `phone/dcf_phone_bundle_6.18.zip`.

---

## What changed
**1. A faster traceback.**
- The traceback alignment that reads the TrpA–D chain was a loop over every cell.
- Now each row is computed at once. Horizontal gaps are resolved exactly by a running maximum: H[j] = max over k ≤ j of (V[k] − 8·(j − k)), where V is the best of zero, the diagonal and the gap from above.
- The scores and tie rules are unchanged.

**2. The scan's tie rule.**
- One Pacific oyster protein (A0A8W8J9Y2) scores exactly 1,364 against both robin CRY4 and fly 6-4.
- The scan breaks ties with max((score, name)); the reader now does the same.
- Both references are cryptochrome-family, so no call changes.

## Checks
| check | result |
|---|---|
| random proteins plus the six references (124), old against new traceback | **identical** |
| speed per protein (computer) | 0.25 s → **0.010 s** |
| all blind hits of L3785, L3797 and L3805, re-read by the reader | **63 of 63 identical** (score, tetrad, family) |
| phone self-test, 12 files | **270/270** |

## Summary
- **Menu 37 now reads a protein's cryptochrome family and electron chain in about a hundredth of a second on a computer.** Reading whole proteomes on the phone is now practical.
- **It reproduces the computer scan exactly on every blind hit so far** (63 of 63).

## Potential leads for future research
- **[L3809]** Waiting for the SF18/SF17 downloads. The frozen scan still uses the old loop traceback, by design, so the slow step there stays.
- **[Phone proteome mode]** Let menu 37 read a whole proteome TSV and print only the hits. It is fast enough now.
- **[Releases]** dcf-math v1.2.0 and dcf-genefinder v1.2.0 when Gary is ready.
