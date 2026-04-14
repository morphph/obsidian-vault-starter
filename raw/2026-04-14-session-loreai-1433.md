# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing article content comparing Codex CLI vs Claude Code for potential wiki ingestion.

**Key Exchanges:**
- Article covers: task model (async vs interactive), safety/sandboxing, project context/memory, workflow integration, pricing, model capabilities, and decision framework for choosing between the two tools.

**Decisions Made:**
- No decisions made — this appears to be a flush/compact trigger on a session where article content was being reviewed or drafted, not an active working session.

**Lessons Learned:**
- Codex CLI: container-isolated sandbox, async PR-based delegation, flat $200/mo (ChatGPT Pro), uses o3/o4-mini, no persistent memory across tasks, better for well-scoped parallelizable work
- Claude Code: local shell access + permission layers, interactive pair-programming model, pay-per-token, uses Claude family, persistent context via CLAUDE.md, better for ambiguous/iterative/complex work
- Key differentiator: Codex = safer by default (architectural sandboxing); Claude Code = more capable but requires conscious permission config
- Context gap: Claude Code improves over time via CLAUDE.md; Codex infers from code only
- Complementary tools — many devs use both: Codex for task queue, Claude Code for deep work

**Action Items:**
- Consider ingesting this article as a raw source → wiki page on `codex-cli-vs-claude-code.md` covering the comparison framework, pricing notes, and safety tradeoffs