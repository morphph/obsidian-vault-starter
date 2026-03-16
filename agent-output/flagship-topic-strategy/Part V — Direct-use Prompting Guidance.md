# Part V — Direct-use prompting guidance for Claude Code

This section exists so the strategy can be translated into high-success execution prompts.

## 1. Recommended prompt pattern

When assigning work to Claude Code, provide:

- the overall implementation spec,

- one task pack only,

- any repo-specific constraints or commands,

- and a request to summarize its plan before making changes if the task is non-trivial.


## 2. Recommended execution framing

Use phrasing like:

- implement only this task pack,

- do not proceed to the next task pack automatically,

- validate before claiming success,

- if blocked, stop and summarize blocker precisely,

- preserve legacy newsletter behavior unless this task explicitly changes it.


## 3. Recommended working mode

Ask Claude Code to:

- inspect relevant files first,

- explain intended modifications briefly,

- then implement,

- then validate,

- then summarize files changed, validations run, and any residual risks.


## 4. Anti-patterns to avoid

Do not ask Claude Code to:

- redesign the entire platform in one pass,

- refactor unrelated systems opportunistically,

- fix broad aesthetic/UI issues while doing infrastructure work,

- rewrite all prompts without necessity,

- expand to many topics before the pilot topic is stable.


## 5. What to ask Claude Code to report back

After each task pack, ask for:

- files changed

- key behavior changed

- validations performed

- open risks

- whether the next task pack is now unblocked


---
