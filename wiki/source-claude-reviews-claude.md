---
type: source-summary
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
tags: [wiki, source, architecture-analysis]
---

# Source: Claude Reviews Claude — 架构总览

## Summary
Comprehensive Chinese-language architectural analysis of [[claude-code|Claude Code]] (Anthropic's official CLI). 17 chapters, 8,600+ lines of technical deep-dive. Treats Claude Code as a codebase to reverse-engineer, documenting its six foundational pillars and key engineering patterns.

## Key Takeaways
- Claude Code architecture rests on 6 pillars: System Prompt, Tool System, [[query-loop|Query Loop]], [[context-management|Context Management]], [[multi-agent-architecture|Multi-Agent Coordination]], [[permission-system|Security & Permissions]]
- Core design principle: "LLM as reasoning center; Harness provides perception, action, memory, and constraints" — validates the [[harness-design]] pattern
- 42+ integrated tools, 12-step query loop state machine, 4-layer context compression, 7-layer security
- Notable patterns: "35-line Store" (React 19 replaces Redux), "Fork Ink" (custom terminal renderer), "Leaf Module Pattern" (anti-circular-dependency)
- Security: fail-closed defaults for safety, fail-open for config/external services
- Context window = "scarcest resource" — all architecture decisions optimize for this

## Entities Extracted
- [[claude-code]] (new), [[Anthropic]] (updated)

## Concepts Extracted
- [[query-loop]] (new), [[context-management]] (new), [[permission-system]] (new)
- [[harness-design]] (updated), [[multi-agent-architecture]] (updated), [[context-anxiety]] (updated)

## Source File
`raw/2026-04-06-claude-reviews-claude-overview.md`
