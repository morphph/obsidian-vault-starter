---
type: concept
created: 2026-04-08
last-updated: 2026-05-16
sources:
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
  - raw/2026-04-30-thariq-prompt-caching-is-everything.md
  - raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md
tags: [wiki, architecture, performance, agentic]
---

# Prompt Cache Optimization

## Summary
A cross-cutting concern in [[claude-code|Claude Code]] where nearly every architectural decision considers prompt cache impact. Anthropic's API caches prompt prefixes server-side (~1 hour TTL). At 200K tokens, a cache hit costs ~$0.003 vs ~$0.60 for a miss. The system goes to extraordinary lengths to keep API request prefixes byte-identical. **Anthropic operationalizes this:** [[thariq]]'s engineering blog (2026-04-30) reveals the Claude Code team **declares SEVs when cache hit rate drops** — cache health is treated as an SLO, not an optimization.

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

### Thariq's 4-layer ordering rule (2026-04-30 official guidance)
The canonical static-first prompt layout that Claude Code uses:

| Order | Component | Cache scope |
|-------|-----------|-------------|
| 1 | Static system prompt + Tools | Globally cached (across all users, all sessions) |
| 2 | CLAUDE.md | Cached within a project |
| 3 | Session context | Cached within a session |
| 4 | Conversation messages | Per-turn |

**Production cache-break bugs Thariq's team has shipped (warning catalog):**
- Putting an in-depth timestamp in the static system prompt → every request misses
- Shuffling tool order definitions non-deterministically → cache drifts
- Updating tool parameters mid-deploy (e.g., what subagents the Agent tool can call) → entire cache invalidated

### `<system-reminder>` — the cache-preserving update mechanism
Time-varying info (current date, file changes, mode changes) **must not go in the system prompt** — that breaks cache. Instead, Claude Code injects `<system-reminder>` tags into the next user message or tool result. This is why the system reminders you see in Claude Code's prompts are in the user message channel, not the system prompt.

**Generalizable rule:** any time-varying info (timestamp, file state, user prefs, mode flags) goes via message channel, never via system-prompt edits.

### `defer_loading` for MCP tool sets
Claude Code can have dozens of MCP tools loaded. Including all schemas in every request would balloon prefix size; *removing* tools mid-conversation would break cache. The Anthropic API supports a third option:

> Send lightweight stubs (just the tool name, with `defer_loading: true`). Full schemas only load when the model selects them via tool search.

The cached prefix stays byte-stable because the same stubs are always present in the same order.

### State transitions via tool calls (the Plan Mode pattern)
The single most important design pattern from Thariq's article — see [[plan-mode-as-tools]]:

> **Tool set never changes. `EnterPlanMode` and `ExitPlanMode` are themselves tools.**

Generalizable: model state transitions belong in tool calls, not in prompt rewrites. **Capabilities ≠ behaviors.** Don't narrow capability surface mid-conversation; expand with mode-controlling tools that change behavior via `<system-reminder>`.

### Cache-safe forking for compaction (the cost trap)
The naive compaction implementation: separate API call with its own "summarize this" system prompt and no tools. **This means zero cache hits** — the prefixes diverge at the very first token. The longer the conversation (and thus the more compaction is needed), the more expensive the compaction call.

Claude Code's actual approach:
- Use the **exact same** system prompt, user context, system context, and tool definitions as the parent
- Append the compaction prompt as a new user message at the end
- The request looks nearly identical to the parent's last request → cached prefix reused → only the compaction prompt itself is "new" tokens

**Required side effect: compaction buffer.** You must reserve room in the context window for the compact message + summary output before triggering compaction. Compaction-when-already-full is too late.

This pattern is now exposed via Anthropic's API directly — you don't have to implement it yourself.

### Don't switch models mid-session
Caches are model-specific. The counter-intuitive corollary:
> If you're 100K tokens into Opus and want to ask an "easy" question, **switching to Haiku is more expensive than letting Opus answer** — Haiku has to rebuild the prefix from scratch.

When you genuinely need a different model, hand off via subagent: Opus prepares a brief, Haiku starts a new session against just that brief. Claude Code's Explore agents work this way.

## Connections
- Related: [[claude-code]], [[context-management]], [[forked-agent-pattern]], [[session-memory]], [[dreaming]], [[infrastructure-layer]], [[plan-mode-as-tools]], [[thariq]]
- Prompt cache is why ContentReplacementState freezes decisions — a local optimization with global cost impact
- The CLAUDE.md hierarchy simultaneously serves as infrastructure (RBAC) and cache optimization (static system prompt)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Initial creation |
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Added system prompt boundary design, user context injection placement |
| 2026-05-10 | raw/2026-04-30-thariq-prompt-caching-is-everything.md | Major addition — official Anthropic engineering blog: 4-layer ordering rule, production cache-break bugs catalog, `<system-reminder>` channel, `defer_loading`, Plan Mode as tools, cache-safe compaction forking, compaction buffer, model-swap caveat, SEV-level cache hit rate alerting |
| 2026-05-16 | raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md | Added batch-prune pattern from computer-use guidance: when rolling-buffering screenshots, prune **in batches** rather than one-at-a-time. N individual prunes = N cache invalidations; one batch prune = one invalidation. Concrete production rule for any append-then-prune workflow (logs, transcripts, tool results) |
