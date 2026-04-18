---
type: concept
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, agentic, skills, design-pattern]
---

# Skill as Method Call

## Summary
A skill file is not a prompt — it's a **parameterized procedure**. Like a method in software, the same skill produces radically different capabilities depending on the arguments passed in. Coined by [[garry-tan|Garry Tan]] as one of the five definitions in [[thin-harness-fat-skills]]. Reframes prompt engineering as software design, with markdown as the language and human judgment as the runtime.

## Details
- **Definition**: A skill file teaches the model **how** to do something (the process). The user supplies **what** (the inputs/parameters). The skill is reusable across wildly different domains because it encodes a *procedure of judgment*, not a fixed task.
- **Anti-pattern**: Treating skills as one-shot prompts tied to a single use case
- **Correct pattern**: Identify the abstract procedure, parameterize its inputs, invoke it with different arguments

### Garry's `/investigate` example
Same 7-step skill, same markdown file:
- Parameters: `TARGET`, `QUESTION`, `DATASET`
- Steps: scope → build timeline → diarize each doc → synthesize → argue both sides → cite sources

| Invocation | TARGET | DATASET | What it becomes |
|---|---|---|---|
| 1 | Safety scientist | 2.1M discovery emails | Medical research analyst (whistleblower question) |
| 2 | Shell company | FEC filings | Forensic investigator (campaign-finance trace) |

> "Same skill. Same seven steps. Same markdown file. The skill describes a process of judgment. The invocation supplies the world."

### Why markdown beats source code for this
- **Source code** encodes deterministic transforms; rigid by design
- **Markdown** encodes process, judgment, and context — in the language the model already thinks in
- "Markdown is, in fact, a more perfect encapsulation of capability than rigid source code."

### Implications for skill design
- **Look for re-use surface**: If you wrote the same prompt twice with different specifics, it's a skill begging to be parameterized
- **Name the verbs**: `/investigate`, `/match`, `/enrich`, `/improve` — abstract procedures, not domain tasks
- **Document the parameters explicitly** at the top of the skill file
- **Test with diverse invocations**: a good skill produces useful output across very different inputs (the medical-vs-FEC test)

### How this relates to existing patterns
- Builds on [[harness-design]]'s "fat skills" arm of the dichotomy
- Compatible with [[claude-code]] slash commands (each is essentially a method)
- Aligns with [[boris-cherny]]'s practice of committing slash commands to git as team-shared APIs

### Concrete examples in our own wiki/setup
- `/ingest <url|file|scan>` — three parameter modes, same procedure
- `/draft <wiki-page|raw-file|topic>` — three input types, one procedure
- `/visualize <topic|path|blank>` — same diagram-building procedure, different inputs
- All five LLM Wiki commands already follow the pattern intuitively

## Connections
- Related: [[thin-harness-fat-skills]], [[harness-design]], [[claude-code]], [[garry-tan]], [[ralph-wiggum]], [[llm-judgment-vs-scripts]], [[boris-cherny]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Initial creation — definition + investigate example + design implications |
