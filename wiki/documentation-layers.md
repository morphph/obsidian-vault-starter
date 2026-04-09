---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-claude-md-self-audit.md
tags: [wiki, practice, claude-code, governance]
---

# Documentation Layers

## Summary
A meta-convention in CLAUDE.md that maps change types to documentation locations, preventing Layer 1 bloat. Emerged from our own [[context-noise-governance|CLAUDE.md self-audit]]: without explicit governance, the natural tendency is to dump everything into CLAUDE.md because it's the most visible file. The table is Layer 1 content that prevents Layer 1 bloat — a self-regulating mechanism.

## Details

### The Pattern
Add a table to CLAUDE.md that answers: "I just made a change — where do I document it?"

| What changed | Update where |
|-------------|-------------|
| New convention (applies every session) | CLAUDE.md |
| Rule for specific file types/directories | `.claude/rules/{name}.md` with `paths:` glob |
| New slash command | `.claude/commands/{name}.md` + brief row in CLAUDE.md Commands table |
| New skill | `.claude/skills/{name}/SKILL.md` + brief row in CLAUDE.md Skills table |
| Skill/command behavior details | Inside the skill/command file, NOT CLAUDE.md |

### The Principle
**CLAUDE.md declares WHAT exists. Skills and commands define HOW they work.**

This maps directly to [[tw93]]'s context layering:
- **Layer 1 (CLAUDE.md)** = existence + brief description (always loaded)
- **Layer 2 (.claude/rules/)** = conditional rules (path-loaded)
- **Layer 3 (skills/commands)** = full implementation detail (on-demand)

### Why It's Needed
Without this, every new feature's documentation gravitates to CLAUDE.md:
- Developer adds a skill → documents the full workflow in CLAUDE.md (should be in SKILL.md)
- Developer adds a convention for .ts files → writes it in CLAUDE.md (should be in rules/)
- Developer adds a command → writes 30 lines of detail in CLAUDE.md (should be in commands/)

Each addition is small. Over months, CLAUDE.md bloats from 80 lines to 300+ — mostly content that's only relevant 5-10% of the time but loaded 100% of the time.

### Practical Examples From Our Audit

**Templates → rules/ (path-loaded):**
We had a 29-line Wiki Page Format template always-resident in CLAUDE.md. Moved to `.claude/rules/wiki-page-format.md` with `paths: ["wiki/**"]`. Now only loads when editing wiki files. CLAUDE.md keeps one pointer line.

**Ingest details → commands (on-demand):**
Source Fetching Tools (10 lines) and Source Types (7 lines) were in CLAUDE.md AND in `.claude/commands/ingest.md`. Pure duplication — removed from CLAUDE.md. The command file is the single source of truth, loaded only when /ingest runs.

**Infrastructure docs → removed (derivable):**
Pipeline B had 30 lines describing scripts/ and hooks/ file by file. Claude can just `ls scripts/` and read the files. Compressed to 3 lines of safety-critical info that ISN'T derivable from code (recursion guard, "no hooks in this repo").

### Self-Regulating Property
The table itself is ~10 lines in CLAUDE.md (Layer 1). Its purpose is to prevent other Layer 1 additions. Every time Claude or a human is about to add documentation, this table redirects them to the correct layer. The cost (10 always-resident lines) prevents much larger costs (50-100+ lines of misplaced content).

## Connections
- Related: [[context-noise-governance]], [[claude-code]]
- This is the governance mechanism that [[context-noise-governance]] recommends but doesn't specify how to implement

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-claude-md-self-audit.md | Initial creation from our own CLAUDE.md audit |
