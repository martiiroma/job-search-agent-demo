# RUBRIC.md

**Role:** how an offer that passed the hard filters is scored.
**Edited by:** the human only.

---

## 0. Guiding principle — read before scoring anything

**This document is a working rule for the agent, not a way to please the human.**

1. **A day with no offers is a valid result.** No lowering the bar to fill the daily summary.
2. **No dimension is raised to compensate for another.** The weights already balance them.
3. **Gaps are always declared**, even when they push the score below the threshold.
4. **Score only what the offer says.** Missing data gets the default value of §2, never a guess.

> **Quality criterion:** the system is measured by how often the human agrees with its scores, not by how many applications it produces.

---

## 1. Dimensions and weights

| # | Dimension | Weight |
|---|---|---|
| D1 | Skills fit — against the closed taxonomy in `CV-MASTER.md §3` | 30% |
| D2 | Role framing — does it move the candidate where they want to go? | 25% |
| D3 | Sector | 15% |
| D4 | Pay | 12% |
| D5 | Work mode and location | 12% |
| D6 | Schedule flexibility | 6% |

**Final score = Σ (dimension score × weight)**, each dimension on a 0–10 scale.

Every dimension score needs a written reason. A score without its *why* cannot be audited.

---

## 2. Missing data — default values

| Missing | Default | Also |
|---|---|---|
| Salary | D4 = 5 | Never estimated from the market |
| Work mode | D5 = 5 | Escalate |
| Schedule | D6 = 5 | — |

---

## 3. Action thresholds

| Final score | Action |
|---|---|
| ≥ 8.0 | **Priority.** Draft CV and letter, highlight in the summary |
| 7.0 – 7.9 | **Apply.** Draft CV and letter |
| 5.5 – 6.9 | **Report only.** The human decides |
| < 5.5 | **Discard**, with reason and scores recorded |

---

## 4. Calibration

Before the system was allowed to draft documents, it ran in **evaluation mode**: it scored real offers and the human scored them too. Every disagreement is recorded per dimension in `STATE.md`.

**At 3 disagreements in one dimension**, the agent flags it in the summary. It never changes the rubric itself.