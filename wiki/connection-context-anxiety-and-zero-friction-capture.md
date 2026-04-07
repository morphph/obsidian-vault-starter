---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, connection, insight]
---

# Connection: Context Anxiety and Zero-Friction Capture

## The Connection

[[context-anxiety]] is not just an LLM failure mode — it's also a **human knowledge worker failure mode**. When you're deep in a long coding session and feel context slipping away, you skip documenting, skip reflecting, and rush to finish. This is the same behavioral pattern as an LLM "wrapping up prematurely" as context fills.

## Key Insight

[[zero-friction-capture]] is the remedy for human context anxiety — just as Claude Code's [[context-management]] (4-layer compression) is the remedy for LLM context anxiety. Both are **harness-level solutions**: you don't change the "model" (whether LLM or human), you change the scaffolding around it.

The old /build-log failed because it required the human to act precisely when they're most context-anxious — mid-session, under cognitive load. Hook-based capture removes that demand entirely.

## Where Else This Applies

Any system with a human in the loop should ask: **when will the user be "context anxious"?** Then design zero-friction mechanisms for those moments:
- LoreAI newsletter editing: auto-save drafts, don't require explicit "save" actions
- blog2video script review: pre-fill review checklist from prior session context
- Any multi-step workflow: capture state automatically at each transition, don't rely on the user to document

## Related Concepts
- [[context-anxiety]] — The LLM failure mode
- [[zero-friction-capture]] — The harness solution
- [[context-management]] — Claude Code's 4-layer compression (the LLM-side remedy)
- [[harness-design]] — Both solutions are harness-level, not model-level

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | Discussion: context-anxiety × zero-friction-capture | Initial creation — first connection article in wiki |
