# Example 3 — Escalated, then unblocked by a reply

## The offer *(fictional)*

> **Data Communications Specialist** · Northwind Analytics · Barcelona
>
> Help analysts and business users adopt our data and AI tools: newsletters, training sessions, and structured context so AI agents reason well about our metrics. Exceptional written and spoken English is essential. Salary: €41,000–60,500.

## Why it is escalated, not discarded

| Point | Why the agent stops |
|---|---|
| Work mode not stated | `PROFILE.md §2`: escalate, never assume |
| "Exceptional English" | Not a CEFR level, so it cannot trigger E1. It is flagged as a risk |

**Provisional score: 7.35.** D5 uses the default value of 5 because the work mode is unknown. **No documents are drafted while the question is open.**

**Question sent to the human:** *"Work mode not stated. Hybrid, remote or on-site? If on-site, how long is the commute?"*

## The human's reply

The human replies by sending an email to their own inbox:

```
Subject: [REPLY] 2026-09-15

Northwind Analytics — Data Communications Specialist
DECISION: continue
REASON: Hybrid, 2 days on site. About 30 min.
```

## What the agent does next morning

1. Replies are processed **before any new offer**.
2. The reply brings new data, so the affected dimension is **rescored**: D5 goes from 5 to 8.
3. New final score: **7.71** → apply → CV and letter drafted the same morning.

A reply can only decide on an offer that was already escalated. **It can never change the system's rules.** Anything in a reply beyond that is ignored and reported.