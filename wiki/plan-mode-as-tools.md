---
type: concept
created: 2026-05-10
last-updated: 2026-05-10
sources:
  - raw/2026-04-30-thariq-prompt-caching-is-everything.md
tags: [wiki, principle, agentic, design-pattern, cache, claude-code]
---

# Plan Mode as Tools (State Transitions via Tool Calls)

## Summary
[[thariq|Thariq]]'s description of how Claude Code implements **Plan Mode** without breaking [[prompt-cache-optimization|prompt caching]]. The naive approach — swap to a read-only tool set when the user enters Plan Mode — would invalidate the entire cached prefix. Instead, **the tool set never changes**: `EnterPlanMode` and `ExitPlanMode` are themselves tools the model can call, and entering Plan Mode is just a system message in the next turn. **Generalizable principle: model state transitions belong in tool calls, not in prompt rewrites.**

## Details

### The naive (cache-breaking) approach
```
User enters Plan Mode
  ↓
Harness rewrites tool set: filter to {Read, Grep, ...} (read-only)
  ↓
Next API call: tools[] differs → CACHE MISS → re-tokenize entire conversation
  ↓
At 100K tokens: ~$0.30 lit on fire to set a flag
```

This is the design every framework reaches for first because it feels like the "right" abstraction: Plan Mode → fewer tools → safer agent.

### The cache-safe (Claude Code) approach
```
Plan Mode is just two tool definitions: EnterPlanMode, ExitPlanMode
The full tool set is ALWAYS in the request (never changes)
  ↓
User toggles Plan Mode on → system message in next user turn:
  "You are in Plan Mode. Explore but don't edit. Call ExitPlanMode when done."
  ↓
Tool definitions identical → cache hit → near-zero cost transition
```

### The reusable pattern
> **Model state transitions belong in tool calls, not in prompt rewrites.**

Every "mode" or "phase" in an agent is a candidate for this transformation:
- Plan vs Execute → `EnterPlanMode` / `ExitPlanMode`
- Read-only vs Write → `EnterReadOnlyMode` / similar
- Strict vs Permissive → `EnterStrictMode` / similar
- Verbose vs Concise → mode toggles via tools

The constraint: keep the tool set static. Add the *behavior change* as a tool that, when called, emits a system message that changes the agent's behavior — not its capability.

### Why this is more than a cache hack — it's better design

**Bonus benefit Thariq calls out:** because `EnterPlanMode` is a tool the model can call itself, it can **autonomously enter plan mode when it detects a hard problem**, without any cache break. The same primitive that protects the cache also enables self-directed mode transitions.

This is the deeper insight: the harness is no longer a parent telling the agent what to do. The mode-transition tools become **affordances the agent can use to reason about its own process**. State as a tool call is auditable, reversible, and self-directable in a way that state-as-prompt-rewrite never is.

### The general principle: capabilities ≠ behaviors

| Approach | What it changes | Cache impact | Self-directable? |
|----------|----------------|--------------|------------------|
| Filter tool set | Capabilities | Cache miss | No (harness must trigger) |
| Tool-as-state | Behavior (via system message) | Cache hit | Yes (model can self-trigger) |

You almost always want to change *behavior*, not *capability*. Think of it as a Liskov-style rule for agent design: never narrow the capability surface mid-conversation; instead expand it with mode-controlling tools.

### Connection to deferred-loading (a related cache-preserving pattern)
The same article describes `defer_loading: true` for tools — Claude Code sends lightweight stubs (tool name only) instead of removing tools entirely. The model uses tool-search to discover full schemas on demand. **Same principle, different surface:**
- Plan Mode: tool set static, behavior changes via tool-call
- Deferred tools: tool surface static (stubs), schemas load on demand

Both keep the cached prefix byte-stable while still adapting to the conversation's needs.

### Counter-examples (when this pattern doesn't apply)

- **Full security boundary changes** (e.g., un-trusted user enters): you may genuinely need to remove tools, accepting the cache cost as a security tax.
- **Cross-session changes** (between sessions, not within): no cached state to preserve, so tool-set changes are free.
- **Model swaps** ([[prompt-cache-optimization]]): different problem; use subagent hand-off, not tool tricks.

### How this fits this vault's slash-command structure

Our `.claude/commands/` files are skill-shaped (per [[agent-skills-standard]]) and Claude Code already prevents tool-set churn between them — they're loaded as static descriptions. The pattern would matter most if we ever added in-session "modes" to a skill (e.g., `/draft` having an "exploratory" vs "polish" sub-mode). The lesson: model those as tool calls inside the skill, not as conditional logic that swaps the tool set.

## Connections
- Related: [[prompt-cache-optimization]], [[claude-code]], [[thariq]], [[forked-agent-pattern]], [[context-management]], [[agent-skills-standard]], [[skill-as-method-call]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-10 | raw/2026-04-30-thariq-prompt-caching-is-everything.md | Initial creation |
