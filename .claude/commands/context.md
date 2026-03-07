---
name: context
description: Load project context. Default (fast): CLAUDE.md + all project files (~5K tokens). Say "full" for recent build logs + ideas too.
---

# Context Load — Tiered

Load context about vfan's projects and current state. Two levels:

## Determine load level

- If $ARGUMENTS contains "full" → Level 2
- Otherwise → Level 1

---

## Level 1: Fast Load (default)

1. Read `CLAUDE.md` (vault root).
2. Read ALL files in `projects/` directory.
3. Provide a concise summary:

```
## Context Loaded (fast mode)

**Projects:**
- [project]: [one-line status from context file]
- ...

**Unfilled sections:** [list any projects that still have [Write: ...] placeholders]

💡 For recent build logs and ideas, say "load full context" or run `/context full`.

What are we working on?
```

---

## Level 2: Full Load

1. Everything from Level 1, plus:
2. Read the most recent 7 daily build logs from `daily/` (sorted by date, newest first).
3. Read the most recent 5 files from `ideas/` (if any exist).
4. Read the most recent report from `agent-output/` (if any exist).

5. Provide a richer summary:

```
## Context Loaded (full mode)

**Projects:**
- [project]: [one-line status]
- ...

**This week's focus:** [based on recent build logs, what am I spending time on?]
**Open blockers:** [any #blocker tags found in recent logs]
**Active ideas:** [any #idea tags not yet graduated]
**Cross-project note:** [anything interesting — overlaps, gaps, contradictions]

What are we working on?
```

## Important
- Be concise in summaries. I can ask for details.
- Don't read agent-output/ in Level 1 — that's staging area.
- If project context files have empty [Write: ...] sections, flag them — those need filling.
