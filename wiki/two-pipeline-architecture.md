---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, system-design, architecture]
---

# Two-Pipeline Architecture

## Summary
The wiki's full architecture has two input pipelines feeding one knowledge base. Pipeline A captures external knowledge (articles, repos, tweets) via manual or automated entry points. Pipeline B captures internal knowledge (your own Claude Code coding sessions) via hooks. Both converge at `raw/`, compiled by the same LLM compiler into `wiki/`.

## Details

### Pipeline A: External Knowledge
Two entry points, same pipeline:
- **Desktop (manual)**: You find something interesting → `/ingest <url>`. Supports articles, GitHub repos (deep scan), tweets (Playwright MCP), any URL.
- **Telegram bot (auto)**: Claude Code Channels-configured bot receives forwarded articles → auto-saves to `raw/`. Also RSS feeds.
- Both produce immutable markdown files in `raw/`

### Pipeline B: Internal Knowledge
- Claude Code hooks (SessionEnd + PreCompact) fire when you code in LoreAI or blog2video
- Hook spawns background flush.py → [[agent-sdk-vs-claude-code|Agent SDK]] extracts decisions, lessons, patterns
- Writes to `raw/` (same destination as Pipeline A)
- Uses [[zero-friction-capture]] — you do nothing, knowledge flows automatically
- Recursion prevention via `CLAUDE_INVOKED_BY` env var

### Convergence Point
Both pipelines dump into `raw/`. Then:
- **Manual**: `/ingest scan` compiles immediately
- **Auto**: [[time-gated-compilation]] at 6 PM compiles everything accumulated that day
- Same LLM Compiler ([[compiler-analogy]]), same `wiki/` output, same `index.md` retrieval

### Why Two Pipelines Matter
External knowledge (what others build) + internal knowledge (what you learn by building) → cross-project patterns become discoverable. `/query "what pipeline patterns have I seen AND used?"` can now search both sources.

## Connections
- Related: [[compiler-analogy]], [[zero-friction-capture]], [[time-gated-compilation]], [[agent-sdk-vs-claude-code]], [[index-over-rag]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | Architecture discussion | Initial creation — synthesized from Karpathy + claude-memory-compiler patterns |
