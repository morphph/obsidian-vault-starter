---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-mattpocock-grill-with-docs-skill.md
  - raw/2026-05-17-aihero-grill-with-docs-changelog.md
  - raw/2026-05-17-repo-mattpocock-skills.md
  - raw/2026-05-17-aihero-5-agent-skills.md
tags: [wiki, skill, ddd, discovery, prompt-engineering]
---

# /grill-with-docs

## Summary
Matt Pocock's keystone Claude Code skill. Combines an interactive grilling session (relentless one-question-at-a-time interview) with DDD-style documentation generation (CONTEXT.md as ubiquitous-language glossary, ADRs for hard decisions). The entry point of his entire workflow and Phase 1 of [[idea-to-afk-agent-flow]].

## Details

### What it does
The skill interrogates you about a plan, walking down the design tree branch by branch. For each question:
1. Agent provides its recommended answer
2. User accepts or corrects (one Q at a time, sync)
3. If question is answerable from code, agent explores instead of asking
4. As terms resolve, CONTEXT.md updated inline
5. As major trade-offs surface, ADR offered if 3-gate test passes

### Two file artifacts

**CONTEXT.md** — bounded-context glossary
- Strict rule: glossary only, no implementation details, no specs, no scratch notes
- One per bounded context (single repo → single CONTEXT.md; system with multiple domains → root CONTEXT-MAP.md + per-domain CONTEXT.md)
- Created lazily on first term resolution

**ADRs** (`docs/adr/`) — architectural decision records
- Only created when ALL three conditions true:
  1. Hard to reverse
  2. Surprising without context (future reader will ask "why?")
  3. Result of real trade-off (genuine alternatives existed)
- Skip if any condition missing — prevents ADR pollution

### Why it's the keystone
Every subsequent skill in [[mattpocock-skills-library]] consumes CONTEXT.md:
- `/to-prd` uses domain vocabulary for user stories
- `/to-issues` uses it for issue titles
- `/tdd` uses it for test naming
- `/improve-codebase-architecture` uses it to spot unclear modules

Run grill-with-docs **before** any non-trivial change.

### Practical patterns

**One question at a time** — prevents the agent from dumping a wall of nested questions the user abandons. Enforces synchronous, decision-by-decision conversation.

**Recommended answer included** — reduces user friction. Most "questions" are actually proposals the user accepts; only the disagreements need real thought.

**Explore-first** — if the code can answer it, don't ask. Limits questions to ones requiring human judgment.

**Inline updates** — write to disk as decisions crystallize. Don't batch into a "final review" because half the terms will be forgotten.

### Concrete output value (Matt's example)
Before CONTEXT.md: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"

After CONTEXT.md: "There's a problem with the materialization cascade"

Pays off session after session: tokens saved, naming consistent, navigation easier, agents spend less time inferring jargon.

### Predecessor and evolution
Matt deprecated `/ubiquitous-language` (a documentation-only skill) and merged it into `/grill-with-docs`. Reason: the grilling session naturally surfaces what needs to be documented — separating them broke context.

Also added multi-bounded-context support (CONTEXT-MAP.md) to match real-system reality where one project has multiple domain models.

## Connections
- Container skill: [[mattpocock-skills-library]]
- Sibling: `/grill-me` (non-code variant)
- Output consumed by: [[to-prd]], [[to-issues]], [[tdd]], [[improve-codebase-architecture]] (all in mattpocock-skills-library)
- Related concepts: [[context-md-pattern]], [[sprint-contracts]], [[four-files-context-architecture]]
- Phase 1 of: [[idea-to-afk-agent-flow]]
- Owner: [[matt-pocock]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | SKILL.md + AI Hero changelog + AI Hero 5 skills + skills README (all Matt official) | Initial creation |
