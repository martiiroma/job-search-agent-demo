# PROFILE.md

**Role:** hard filter before scoring. An offer that fails a filter is discarded **before** the rubric is opened.
**Edited by:** the human only.

---

## 0. Rules of use

1. **Order matters.** Hard filters first (§1). Only offers that pass them are scored.
2. **No silent discards.** Every discard is recorded with its reason.
3. **In doubt, escalate. Never discard.** A wrong discard is invisible and irreversible; an unnecessary escalation costs thirty seconds.
4. **A preference is not a filter.** Preferences adjust the score; they never discard anything on their own.

---

## 1. Hard filters

| Code | Discard when… | Escalate instead when… |
|---|---|---|
| **E9** | The application deadline has passed. *Checked first: it is the cheapest.* | — |
| **E1** | A language the candidate does not have is **required** | English is required at C1 or above |
| **E2** | The **declared** salary is below the minimum | The salary is not declared. *An estimate never triggers a discard.* |
| **E3** | The role is fully on-site and over 55 min away by public transport | The work mode is not stated |
| **E4** | Freelance is the only contract type | — |
| **E5** | Relocation outside the metro area is required | — |
| **E6** | **No part** of the required degree is held | A related degree or master's covers part of it |
| **E7** | It is an internship or entry-level role | — |
| **E8** | Split shifts, night shifts or regular weekends | — |
| **E10** | Regular start before 06:00, or before 07:00 with a long commute | — |

> *Documented case (26/08/2026): the best-scoring offer the system had seen (8.07/10) started at 05:00. No other dimension can make up for a start time the candidate cannot keep. The rule was written with that case attached, not just the number.*

---

## 2. Escalation zone

The agent stops and asks a concrete question when:

- A requirement is ambiguous (is a language "required" or "valued"?)
- The work mode or location is unclear
- The offer looks like a near-duplicate of one already processed
- The offer was published more than a week ago

An escalation is not a failure. It hands back a decision that belongs to the human.