---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, connection, pattern]
---

# Connection: Assumptions Expire × Tool Evolution

## Summary
[[tw93]]'s tool evolution case studies from Claude Code's internal development provide concrete evidence for [[assumptions-expire]]. Scaffolding designed for weak models becomes counterproductive when models improve — and this applies to tools, not just harness architecture.

## The Evidence

### AskUserQuestion: Three Iterations
| Version | Approach | Problem |
|---------|----------|---------|
| v1 | Added `question` parameter to existing tools (Bash) | Model usually ignored it, kept running |
| v2 | Required specific markdown format in output | Model often "forgot" the format — fragile |
| v3 | Independent `AskUserQuestion` tool | Explicit call = pause, no ambiguity, reliable |

**Lesson:** When you need the model to stop and ask, give it a **dedicated tool**. Flags and format conventions get skipped. The tool's existence IS the constraint.

### TodoWrite: From Crutch to Shackle
- **Early:** TodoWrite tool + periodic reminders every 5 turns to keep Claude on task
- **After model improvement:** The tool became a constraint — Claude interpreted Todo as rigid instructions it must follow exactly, losing ability to adapt plans flexibly
- **Tw93's observation:** "当初加这个工具是因为模型不够强，模型变强之后它反而变成了枷锁" (The limitations added because the model was weak became shackles when it got strong)

### Search: RAG → Grep → Progressive Disclosure
- **v1:** RAG vector database — fast but needed indexing, fragile, and "Claude didn't like using it"
- **v2:** Grep tool for self-directed search — much better
- **Emergent benefit:** Claude reads Skill files → Skill references other files → model recursively reads on demand → "progressive disclosure" pattern emerged naturally

## The Pattern
[[assumptions-expire]] predicted this at the architecture level: as models improve, strip away scaffolding. Tw93's examples show this happens at the **tool level** too — and the failure mode isn't that old tools stop working, but that they **actively constrain** the now-smarter model.

**Implication for builders:** Periodically audit your tools. Ask: "Was this tool designed because the model couldn't do X? Can it now?" If yes, the tool might be making things worse.

## Connections
- Related: [[assumptions-expire]], [[harness-design]], [[claude-code]], [[tw93]]
- Rhymes with [[llm-judgment-vs-scripts]]: the boundary between what the model should handle vs what tools should enforce shifts as models improve

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-tw93-claude-code-architecture-governance.md | Initial creation — AskUserQuestion, TodoWrite, Search evolution stories |
