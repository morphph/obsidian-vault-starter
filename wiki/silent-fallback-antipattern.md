---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-session-unknown-1421.md
  - raw/2026-04-08-session-unknown-1126.md
tags: [wiki, pattern, pipeline, quality]
---

# Silent Fallback Antipattern

## Summary
Design antipattern where a fallback chain silently degrades quality without warning. The pipeline completes "successfully" but produces dramatically inferior output. The remedy is **preflight gates** — hard-stop checks for required capabilities before execution begins. Prefer failing loudly over succeeding quietly with bad results.

## Details
- **The incident:** [[blog2video]] pipeline rendered a video from a Twitter/X article. Playwright MCP was configured in `~/.claude/.mcp.json` but not loaded in the current session (MCP servers only initialize at startup). Without Playwright, the fetch-source fallback chain silently degraded to vision transcription of images — producing a video based on image captions instead of the full article text. No error, no warning.
- **Why it's dangerous:** The pipeline completed end-to-end. Without manual review of the output quality, the degradation would go unnoticed. Silent fallbacks create a false sense of reliability.
- **The fix — preflight gate pattern:** Before proceeding with a critical dependency, check that it's available:
  - For Twitter/X URLs: `ToolSearch` must confirm `browser_navigate` is available
  - If not → immediate stop with restart instructions
  - No silent fallback to inferior alternatives
- **The principle:** "Silent fallback chains are dangerous. Always prefer hard stops over silent degradation for critical dependencies."
- **Generalization:** Any pipeline step that has a fallback chain should ask: "If we fall back, is the quality difference acceptable or catastrophic?" If catastrophic, make it a hard stop, not a fallback.
- **MCP specifics:** MCP servers only load at session startup. `/clear` won't reload them. Must exit and restart Claude Code for new MCP config to take effect.
- **Preflight check pattern:** `ToolSearch` for required MCP tools before proceeding — reusable for any pipeline step that depends on a specific MCP server.

## Connections
- Related: [[blog2video]], [[verification-loops]], [[harness-design]], [[claude-code]]
- Preflight gates are input guardrails (the first level of [[verification-loops]]) — checking preconditions before any work begins
- Parallels [[permission-system]]'s fail-closed defaults: "unknown = deny" is safer than "unknown = try anyway"

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-08-session-unknown-1421.md | Initial creation — the incident + preflight gate fix |
| 2026-04-09 | raw/2026-04-08-session-unknown-1126.md | Added MCP session startup details |
