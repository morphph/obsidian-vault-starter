---
type: concept
created: 2026-04-08
last-updated: 2026-04-08
sources:
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
tags: [wiki, architecture, agentic, memory]
---

# Session Memory

## Summary
Layer 3 of [[claude-code|Claude Code]]'s [[context-management|7-layer memory architecture]]. Instead of waiting until context is full and desperately summarizing, **continuously maintain structured notes** about the conversation. When compaction is needed, the summary already exists — no API call required. This is the "free compaction" trick that makes the system dramatically cheaper.

## Details

### How It Works
- A **[[forked-agent-pattern|forked subagent]]** periodically extracts structured notes into a markdown file at `~/.claude/projects/<slug>/.claude/session-memory/<sessionId>.md`
- The subagent only has access to FileEdit on the memory file (all other tools denied)
- Shares the parent's prompt cache for cost efficiency
- Runs sequentially (via `sequential()` wrapper) to prevent overlapping extractions

### Template Structure
The session memory file has 10 sections:
1. Session Title (5-10 word descriptive)
2. Current State (what's actively being worked on)
3. Task Specification (what the user asked to build)
4. Files and Functions (important files and relevance)
5. Workflow (bash commands and interpretation)
6. Errors & Corrections
7. Codebase and System Documentation
8. Learnings (what worked, what didn't)
9. Key Results (specific outputs)
10. Worklog (step-by-step attempts)

### Trigger Logic
Fires when **both** conditions are met:
- Token growth since last extraction ≥ threshold
- AND (tool calls since last ≥ threshold OR no tool calls in last turn)

The "no tool calls" clause captures **natural conversation breaks** — the model has finished a work sequence and is responding with text.

### The Payoff: Free Compaction
When autocompact triggers, it first tries session memory compaction:
- Check if session memory has actual content (not just the empty template)
- Use the session memory markdown **as the compaction summary** — no summarizer API call
- Keep recent messages (10K-40K tokens, 5+ text block messages)
- Result: compaction at near-zero cost vs a full API call

### Configuration
```
minTokens: 10,000       # Minimum tokens to preserve
minTextBlockMessages: 5  # Minimum messages with text blocks
maxTokens: 40,000       # Hard cap on preserved tokens
```

## Connections
- Related: [[context-management]], [[claude-code]], [[dreaming]], [[forked-agent-pattern]], [[context-anxiety]], [[prompt-cache-optimization]]
- Session memory captures within-session notes; [[dreaming]] consolidates across sessions
- Our Pipeline B's flush.py does a similar extraction at session end, but externally via Agent SDK rather than internally

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Initial creation |
