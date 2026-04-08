---
type: concept
created: 2026-04-08
last-updated: 2026-04-08
sources:
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
tags: [wiki, architecture, agentic, memory]
---

# Dreaming

## Summary
Layer 6 of [[claude-code|Claude Code]]'s [[context-management|7-layer memory architecture]]. Cross-session memory consolidation running as a background process — analogous to biological sleep consolidation. Reviews past session transcripts, improves the memory directory, merges near-duplicates, prunes stale facts, resolves contradictions.

## Details

### The Concept
While [[session-memory]] captures within a session, dreaming synthesizes **across sessions**. It's modeled after how biological memory consolidation happens during sleep: experiences from the day are reviewed, organized, and integrated into long-term storage.

### Gate Sequence (Cheapest Check First)
The dream system uses cascading gates — most turns exit early at the cheapest check:
1. Feature flag check (GrowthBook `tengu_onyx_plover`)
2. 10-minute throttle since last scan
3. Time since last consolidation (must exceed threshold)
4. Session count since last consolidation (must have enough new material)
5. Lock acquisition (PID-based mutex)

### Lock Mechanism
The lock file at `<memoryDir>/.consolidate-lock` serves double duty:
- **Body:** Process PID
- **mtime:** `lastConsolidatedAt` timestamp (the lock IS the timestamp)
- **Acquire:** Write PID → mtime = now. Verify PID on re-read (race protection)
- **Success:** mtime stays at now
- **Failure:** `rollbackConsolidationLock(priorMtime)` rewinds mtime via `utimes()`
- **Stale:** mtime > 60 min AND PID not running → reclaim
- **Crash recovery:** Dead PID → next process reclaims

### Four-Phase Consolidation

**Phase 1 — Orient:**
- `ls` the memory directory, read MEMORY.md, skim existing files to avoid duplicates

**Phase 2 — Gather Recent Signal:**
- Review daily logs if present
- Check for drifted memories (facts contradicting current codebase)
- Grep transcripts narrowly — "Don't exhaustively read transcripts. Look only for things you already suspect matter."

**Phase 3 — Consolidate:**
- Write or update memory files
- Merge into existing files rather than creating near-duplicates
- Convert relative dates to absolute
- Delete contradicted facts at the source

**Phase 4 — Prune and Index:**
- Keep MEMORY.md under 200 lines / 25KB
- Remove stale/wrong/superseded pointers
- Shorten verbose index entries
- Resolve contradictions between files

### Tool Constraints
Strict restrictions on the dream agent:
- **Bash:** Read-only only (ls, find, grep, cat, stat, wc, head, tail)
- **Edit/Write:** Only to memory directory paths
- No MCP tools, no Agent tool, no destructive operations

### UI
Dreams appear as background tasks in the footer pill. Users can kill a dream — lock mtime is rolled back so next session retries.

## Connections
- Related: [[context-management]], [[claude-code]], [[session-memory]], [[forked-agent-pattern]]
- Dreaming is to Claude Code what [[time-gated-compilation]] is to our wiki — both defer synthesis to a quieter moment
- Our `compile.py` is structurally similar: orient (read index) → gather (read raw files) → consolidate (create/update pages) → prune (update index)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Initial creation |
