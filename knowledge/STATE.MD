# STATE.md

**Role:** the contract for `state.json`, the system's technical memory.
**Edited by:** the human only. `state.json` itself is written by the agent alone.

---

## 0. What it is for

`state.json` does four things and nothing else:

1. Avoid processing the same offer twice
2. Rotate letter openings (`VOICE.md §3`)
3. Audit whether scoring drifts (`RUBRIC.md §4`)
4. Remember pending offers without repeating them every day

**It is not the human's information channel.** That is the daily summary. The human should never need to open this file.

---

## 1. Structure

```
state.json
├── meta                → last run, run counter
├── dedup_index         → permanent list of identity keys
├── offers              → full records
├── opening_rotation    → last opening used
└── calibration         → scoring disagreements, per dimension
```

**Identity key:** `organisation|title`, lower-case, no accents, no punctuation.

---

## 2. Offer record

```json
"example org|knowledge manager": {
  "status": "escalated",
  "title": "Knowledge Manager",
  "organisation": "Example Org",
  "received": "2026-09-14",
  "source": "portal_alert",
  "score": { "D1": 8, "D2": 9, "D3": 6, "D4": 5, "D5": 5, "D6": 7, "final": 7.37 },
  "gaps": ["years in a technical writing role"],
  "escalation_questions": ["Work mode not stated. Hybrid or on-site?"],
  "reported": true
}
```

**A record is never deleted.** It is closed or archived.

---

## 3. How state survives between runs

Each scheduled run starts from a fresh clone of `main` and writes to its own branch. A GitHub Actions workflow merges that branch into `main` **only if the single changed file is `state.json` and the JSON is valid.**

> **Why this is safe:** the condition "only `state.json`" means the automatic merge can never change the rules, the hook or the reviewer. Those still need human review.

> *Documented case (19–20/08/2026): three runs wrote their state correctly, each on its own branch. None reached `main`, so every run believed it was the first and reprocessed the whole inbox.*