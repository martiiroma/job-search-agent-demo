# SOURCES.md

**Role:** where offers come from and how they are read.
**Edited by:** the human only.

---

## 0. One entry channel

Everything the system processes arrives in **one dedicated inbox**: portal alerts, offers the human forwards, public calls.

| | Allowed |
|---|---|
| **Discover** new offers by searching the web | ⛔ No |
| **Resolve** an offer that already arrived, by finding its full text elsewhere | ✅ Yes |

A resolution search always starts from a title and an organisation that are already in a received email. That keeps it auditable.

---

## 1. Source types

| Type | How it is recognised | Behaviour |
|---|---|---|
| A | Full text is in the email | Process directly. No fetch |
| B | Link to an open public source | Fetch directly |
| C | Link to a blocked portal | **No direct fetch and no workarounds.** Run the resolution cascade (§3) |
| D | Forwarded by the human | Process directly, high priority |
| E | Reply from the human (`[REPLY]` subject) | A decision on an escalated offer. **Processed first** |

---

## 2. Minimum extraction

An offer can only be scored with all four of: **title · organisation · duties · requirements.** If one is missing, the offer stays **pending**. A missing field is never filled in.

---

## 3. Resolution cascade

1. Search the organisation's own careers page.
2. Then its applicant tracking system.
3. Then other open job boards.

**A result only counts as the same offer if all four match:** same organisation · equivalent title · compatible location · coherent date. If any check fails, **escalate. Never assume.**

Every resolved offer records where it came from and where its text was actually read.

## 4. Cheap filters first

Before any resolution, the hard filters that can be decided from the alert alone (deadline, location, internship, required language in the title) are applied. An offer that fails one is discarded, not left pending.

> *Documented case (21/08/2026): twelve offers were left pending after the cascade failed. Five of them were in Germany, Poland, Ireland and Austria: obvious location discards that never needed resolving. Effort went into impossible offers, and they cluttered the pending list.*
>
> **Correct order:** metadata → cheap filters → *(only if it survives)* resolution → minimum extraction → scoring.