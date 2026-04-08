---
type: concept
created: 2026-04-08
last-updated: 2026-04-08
sources:
  - raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
tags: [wiki, architecture, pattern, agentic]
---

# Forked Agent Pattern

## Summary
The foundation for all background operations in [[claude-code|Claude Code]]. A forked agent gets an **isolated context** with cloned mutable state (preventing cross-contamination) but **shares the prompt cache prefix** with the parent (preventing cost explosion). This balance — isolation with sharing — is the key architectural insight.

## Details

### How It Works
```
CacheSafeParams = {
  systemPrompt       // Must be byte-identical to parent
  userContext         // Shared context
  systemContext       // Shared context
  toolUseContext      // Contains tools, model, options
  forkContextMessages // Parent's conversation (cache prefix)
}
```

### What's Cloned (Isolated)
- `readFileState` — LRU cache (prevents cross-contamination)
- `abortController` — Child linked to parent (parent abort kills child)
- `denialTracking` — Fresh state
- `ContentReplacementState` — Cloned (preserves cache-stable decisions)

### What's Shared (For Cost)
- System prompt (byte-identical)
- Message prefix (parent's conversation)
- Tool definitions
→ API sees identical prefix → cache hit

### Fork Message Construction
All fork children produce byte-identical API request prefixes:
1. Full parent assistant message (all tool_use blocks, thinking, text)
2. Single user message with identical placeholder results for every tool_use
3. Only the per-child directive text block differs

This maximizes [[prompt-cache-optimization|prompt cache]] sharing across concurrent forks.

### Anti-Recursion
Fork children keep the Agent tool in their pool (for cache-identical definitions) but detect `<fork_boilerplate_tag>` in conversation history to reject recursive fork attempts.

### Where It's Used
Nearly every background system in Claude Code:
- [[session-memory]] extraction
- Auto memory extraction
- [[dreaming]] consolidation
- Full compaction summarization
- Agent summaries (30-second progress snapshots using Haiku)

### Inter-Agent Communication (SendMessage)
- **In-process:** `queuePendingMessage()` → drained at next tool round
- **Process-based:** `writeToMailbox()` → file-based mailbox
- **Cross-session:** `postInterClaudeMessage()` via bridge/UDS
- Structured lifecycle messages: `shutdown_request`/`shutdown_response`, `plan_approval_response`

## Connections
- Related: [[claude-code]], [[context-management]], [[session-memory]], [[dreaming]], [[prompt-cache-optimization]], [[multi-agent-architecture]]
- This is the internal version of what [[agent-sdk-vs-claude-code]] describes externally — spawning subordinate LLM tasks

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-08 | raw/2026-04-08-troyhua-claude-code-7-layers-memory.md | Initial creation |
