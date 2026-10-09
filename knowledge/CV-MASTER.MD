# CV-MASTER.md

**Role:** single source of truth about the candidate. Every claim in a CV or letter must trace back to this file.
**Candidate:** Alex Demo *(fictional)*
**Edited by:** the human only. The agent never writes here.

---

## 0. Rules of use

1. **The agent selects and orders. It never rewrites, rephrases or summarises.** A bullet is used word for word.
2. **No figure is recalculated, added up, rounded or derived.** If an offer asks for a number that is not in §5, the right answer is to leave it out.
3. **No new bullets.** If nothing fits a requirement, it is flagged as a gap and escalated to the human.
4. **Every bullet declares its scope:** `CV` (fits the CV layout) or `LETTER` (cover letters only).
5. **Tense follows the period.** Only a role that ends in *Present* can be described in the present tense.

---

## 1. Fixed blocks

- **Name:** Alex Demo
- **Location:** Barcelona
- **Languages:** Catalan (native) · Spanish (native) · English (B2, Cambridge First)
- **Education:** BA in Journalism · MA in Video Editing

---

## 2. Roles — canonical titles and dates

| ID | Title | Organisation | Period |
|---|---|---|---|
| `PRJ` | AI job-search agent | Personal project | Aug 2026 – Present |
| `NWM` | Post-production coordinator | Northwind Media | Jan 2020 – Mar 2026 |
| `TRN` | Generative AI trainer | Contoso Consulting | Apr 2025 – Sep 2025 |

> Titles are immutable. A letter may describe the *work* in the offer's vocabulary, never rename the *role*.

---

## 3. Competency taxonomy (closed list)

The rubric can only score against these codes. The agent cannot create new ones.

| Code | Competency |
|---|---|
| `KNOW` | Knowledge management: knowledge bases, structured documentation, standards others apply |
| `AGENT` | AI system design: context and rules for agents, roles, safety limits |
| `QA` | Verification and quality control: validation protocols, test batteries, calibration |
| `TRAIN` | Training and teaching |
| `PROJ` | Project, budget and deadline management |
| `TEAM` | Team leadership and coordination |
| `AV` | Audiovisual production and editing |

---

## 4. Bullet pool

Format: `[ID] (characters) (competencies) — scope`

### `PRJ` — AI job-search agent

- **[PRJ-01]** (104c) (`KNOW`, `AGENT`) — CV
  > Designed a knowledge base of 8 Markdown documents that separates what the agent knows from what it does.
- **[PRJ-02]** (106c) (`KNOW`, `QA`) — CV
  > Broke the CV down into verified claims: the agent can only select and combine them, never invent new ones.
- **[PRJ-03]** (119c) (`QA`, `AGENT`) — CV
  > Validated the security barriers with a 6-test battery that tries to break through them, rather than trusting the agent.

### `NWM` — Northwind Media

- **[NWM-01]** (77c) (`PROJ`) — CV
  > Delivered 100% of projects on time and with no budget deviation over 6 years.
- **[NWM-02]** (105c) (`KNOW`, `TEAM`) — CV
  > Created the team's standard operating procedures: shorter waits and more autonomy for the technical team.
- **[NWM-C1]** (105c) (`KNOW`, `QA`) — LETTER
  > I standardised the validation and delivery protocols with the client, reducing review cycles per project.

### `TRN` — Contoso Consulting

- **[TRN-01]** (113c) (`TRAIN`) — CV
  > Designed and delivered a custom 12-hour generative AI programme, taking the learner from zero to independent use.

---

## 5. Verified metrics register

**No figure may come from anywhere else.**

| Figure | What it measures | Must not be derived into |
|---|---|---|
| 8 documents | Markdown files of the agent's knowledge base | A count of "rules" or "features" |
| 6 tests | Security regression battery | A number of incidents or total tests run |
| 100% on time | Delivery rate at Northwind Media over 6 years | A claim about the whole career |
| 12 hours | Training programme length | ⚠️ **One-to-one consultancy, one learner.** Never "trained the team" |

### Real scope — what can and cannot be claimed

**Can be claimed:** designing the knowledge base, the rules and the test protocol.
**Cannot be claimed:** writing the hook code (it was written with an AI coding assistant), Git beyond a basic level, years in a job titled *technical writer*.

> *Documented case: the English CV said "trained staff" (plural). The training had one learner. The plural came from a translation, not from this file: two language versions of one document had drifted apart. That is why there is one master, not one per language.*