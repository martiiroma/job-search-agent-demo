# Example 2 — Discarded

## The offer *(fictional)*

> **Learning Experience Designer** · Contoso Learning · Barcelona
>
> Design e-learning courses for corporate clients and deliver authoring-tool training. Schedule: Monday to Thursday 9:00–14:00 and 15:00–18:30, Friday 8:00–15:00.

## Hard filters

| Filter | Result |
|---|---|
| E9 Deadline | Open ✓ |
| E1 Language | ✓ |
| **E8 Schedule** | **✗ Split shift, Monday to Thursday** |

**Result:** discarded by **E8**. The rubric is never opened.

## What is recorded

```json
"contoso learning|learning experience designer": {
  "status": "discarded",
  "reason": "E8 — split shift Monday to Thursday",
  "reported": true
}
```

**The discard still appears in the daily summary**, with its reason in one line. A wrong discard is invisible unless it is reported, so every discard is.