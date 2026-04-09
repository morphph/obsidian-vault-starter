---
type: source-summary
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-claude-code-official-docs-best-practices.md
tags: [wiki, source, reference, claude-code]
---

# Source: Claude Code Official Docs — Feature Reference

## Summary
Cross-reference document compiling official Anthropic documentation URLs for every [[claude-code|Claude Code]] feature mentioned in [[boris-cherny|Boris Cherny]]'s best practices threads. Confirms and details feature specifications. Key correction: 26 hook event types (not 20 as previously cited).

## Key Contributions

### Corrections to Wiki
- Hook event types: 26 confirmed (SessionStart, InstructionsLoaded, UserPromptSubmit, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, Notification, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure, TeammateIdle, CwdChanged, FileChanged, PreCompact, PostCompact, ConfigChange, Elicitation, ElicitationResult, WorktreeCreate, WorktreeRemove, SessionEnd)
- 4 hook handler types: command, http, prompt, agent
- Skills replace Commands (old `.claude/commands/` still works; new `.claude/skills/` adds directory support, frontmatter, auto-discovery, path-scoping)
- 6 permission modes: default, acceptEdits, plan, auto, dontAsk, bypassPermissions

### Feature Catalog Not Previously Detailed
- `/teleport` — one-way cloud → terminal session transfer
- `/remote-control` — control local CLI from phone/web, auto-reconnects
- `/loop` — recurring task execution (default 10min, max 50 tasks, 7-day expiry)
- `/schedule` — cloud scheduled tasks on Anthropic infrastructure (hourly to weekly)
- `/branch` — fork conversation at current point
- `/btw` — side query without polluting main conversation
- `/batch` — parallel changes across worktrees (5-30 units)
- `/voice` — push-to-talk dictation, 20 languages, coding vocabulary
- `--bare` — 10x faster startup, skips hooks/LSP/MCP/skills
- `--add-dir` — multi-repo access
- `--agent` — custom agent from `.claude/agents/`
- Cowork Dispatch — Desktop app spawns Code sessions from mobile/Slack
- Chrome extension — live debugging, design verification, session recording (GIF)
- Output styles: Default, Explanatory, Learning + custom markdown files

### MCP Specifics
- 3 transports: HTTP (recommended), SSE (deprecated), stdio (local)
- 3 scopes: local, project (.mcp.json), user (~/.claude.json)
- OAuth 2.0 support, env var expansion
- `MAX_MCP_OUTPUT_TOKENS` default warning at 10K

## Connections
- Related: [[claude-code]], [[boris-cherny]], [[context-noise-governance]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-claude-code-official-docs-best-practices.md | Initial creation — official docs cross-reference |
