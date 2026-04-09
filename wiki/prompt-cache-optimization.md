---
type: concept
created: 2026-04-08
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
tags: [wiki, architecture, performance, agentic]
---

# Prompt Cache Optimization

## Summary
A cross-cutting concern in [[claude-code|Claude Code]] where nearly every architectural decision considers prompt cache impact. Anthropic's API caches prompt prefixes server-side (~1 hour TTL). At 200K tokens, a cache hit costs ~$0.003 vs ~$0.60 for a miss. The system goes to extraordinary lengths to keep API request prefixes byte-identical.

## Details

### Why It Matters
- Cache hit: pay only for new tokens
- Cache miss: re-tokenize entire prompt from scratch
- At 200K tokens: **200x cost difference** ($0.003 vs $0.60)
- Every design decision in [[context-management]] factors this in

### Six Cache-Preserving Patterns

1. **CacheSafeParams** — Every [[forked-agent-pattern|forked agent]] inherits parent's exact system prompt, tools, and message prefix → cache hit
2. **renderedSystemPrompt** — Forks thread the parent's already-rendered system prompt bytes, avoiding re-rendering divergence (e.g., GrowthBook flag values changing between renders)
3. **ContentReplacementState cloning** — Tool result persistence decisions are frozen. Same results get same previews on every API call → stable prefix
4. **Cached microcompact** — Uses `cache_edits` API to delete tool results from server-side cache without changing local prefix → no cache break
5. **Fork message construction** — All fork children get byte-identical prefixes. Only the final directive differs → maximum sharing across concurrent forks
6. **Post-compact cache break notification** — `notifyCompaction()` resets cache baseline so the expected post-compact miss isn't flagged as anomaly

### Cache Break Detection
- `promptCacheBreakDetection.ts` actively monitors for unexpected cache misses
- Known-good cache breaks (compaction, microcompact) pre-registered to avoid false positives
- Unexpected breaks flagged for investigation

### System Prompt Boundary Design (Rohit)
- `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` marker splits prompt into two zones
- **Above boundary:** identical across all users, all sessions → global cache hit. ~80% of the prompt. 577+ lines never re-tokenized.
- **Below boundary:** memoized (once per session) or volatile (every turn). Volatile sections minimized.
- **User context injection:** CLAUDE.md contents, git status, current date injected as **first user message** in `<system-reminder>` tags — NOT in system prompt. Context changes every turn; putting it in system prompt would break cache.
- "No agent tutorial or framework discusses designing the prompt for cache efficiency. At scale, this determines whether your agent costs $0.02 per session or $0.20."

### Implications for Builders
- Any system running multiple LLM calls should consider prompt prefix stability
- The [[forked-agent-pattern]] shows how to share cache across concurrent operations
- `cache_edits` API enables server-side modifications without client-side prefix changes — powerful for systems that need to clean up context without losing cache
- Design system prompts with static/dynamic boundary from day one

## Connections
- Related: [[claude-code]], [[context-management]], [[forked-agent-pattern]], [[session-memory]], [[dreaming]], [[infrastructure-layer]]
- Prompt cache is why ContentReplacementState freezes decisions — a local optimization with global cost impact
- The CLAUDE.md hierarchy simultaneously serves as infrastructure (RBAC) and cache optimization (static system prompt)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Initial creation |
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Added system prompt boundary design, user context injection placement |
