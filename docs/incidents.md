# Incident catalogue

Almost every real problem in this system was found by running it, not by designing it. None of these appeared in any documentation.

Each incident keeps its root cause and the change it caused. The same convention lives inside the rules: every correction is recorded as a dated case in the rule it changed, so its origin can be traced.

## Build incidents

| # | Incident | Root cause | Fix |
|---|---|---|---|
| 1 | Accents corrupted in Google Docs | Double UTF-8 encoding, **intermittent** | Drive taken out of the critical path |
| 2 | A 2.3 MB PDF could not be uploaded to Drive | The upload tool embeds the file as base64 inside the call | Canva used as the document store |
| 3 | Downloading the exported PDF was blocked | The run's network policy | Domain allowed |
| 4 | A paragraph appeared with a list bullet | Text replacement inherits the target's formatting | Separate formatting step and a mandatory visual check |
| 5 | Partial bold in job descriptions | Same mechanism as #4 | Rule widened: *checking the text is not enough, check how it looks* |
| 6 | Hooks not loaded | The folder was named `claude/`, without the dot. **No error appeared** | `.claude/` and a documented regression test |
| 7 | An email was really sent during a test | The send tool exists in the connector; only the hook stood in the way | Documented explicitly |
| 8 | Editing a master design was not blocked | Transactional path: the design ID is not in the edit call | Block the opening of the transaction instead |
| 9 | A `[GUARD]` message was flagged as an injection | The denial contained an instruction | Denial messages are declarative only |
| 10 | `state.json` was always empty | Each run's branch never reached `main` | Merge workflow and inbox labels |
| 11 | `state.json` overwritten with an empty template | A manual upload from outside the system | `state.json` is owned by the agent alone |
| 12 | An offer ID was read as a phone number | The phone pattern accepted nine bare digits | Require a +34 prefix or separators |
| 13 | Four viable offers rejected by the reviewer | Impossible checks combined with presumption of rejection | `NOT VERIFIABLE` ≠ `FAILURE` |
| 14 | A false "repeated opening" | The rotation was updated before the review | Update only after approval |
| 15 | The daily public-jobs fetch kept failing | Scheduled GitHub Actions runs are best effort | Three layers of tolerance |
| 16 | Three bullets and a change-log entry were reported as added but never written | A text replacement found no match **and said nothing**; found a month later | Replacements fail loudly, and every ID is checked after editing |

## Found in operation

| # | Incident | Root cause | Status |
|---|---|---|---|
| 17 | The guard blocked deleting single elements in a working copy of a design | Rule 5 matches "delete" and "page" anywhere in the call, and every edit call carries `page_index` | **Open.** Workaround: those elements are deleted by hand |

## Lessons that repeated

1. **A structural barrier beats a persuasive rule.** If an action can be made impossible, do that instead of asking for it not to happen.
2. **A silent failure is worse than a loud one.** #1, #6 and #16 all hid themselves: an intermittent bug, a hook that silently did not exist, a replacement that reported nothing.
3. **Test instead of assuming.** None of these were in any documentation.
4. **Separate "it failed" from "I cannot check it".** #13 was the costliest design mistake in the project.