# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comparative article on Claude Code vs OpenAI Codex for the wiki knowledge base.

**Key Exchanges:**
- Article source: LoreAI blog post comparing Claude Code and Codex across six dimensions: execution model, context/config, workflow, safety, pricing, and extensibility.

**Decisions Made:**
- N/A (no interactive decisions in this context — content appears to be a source document for ingestion)

**Lessons Learned:**
- **Claude Code strengths:** Real-time interactive execution, local environment access, deep extensibility (Skills/Hooks/MCP/Agent Teams), layered context system (CLAUDE.md + SKILL.md), cross-session memory, multi-IDE support
- **Codex strengths:** Async batch execution, sandboxed safety (no network, no local side effects), bundled with ChatGPT Pro/Team/Enterprise, lower setup friction, good for well-scoped parallel tasks
- **Key architectural contrast:** Claude Code = synchronous pair-programmer with programmable extension stack; Codex = async task executor with cloud sandboxing
- **Codex limitation:** Wrong early assumptions propagate silently; no mid-task steering possible
- **Pricing note (as of article date):** Codex bundled with ChatGPT Pro ($200/mo), Team ($30/user/mo); Claude Code bundled with Claude Pro/Team with usage caps, also available via per-token API
- **Extensibility gap:** Claude Code has Hooks, Skills, MCP servers, Agent Teams; Codex only has AGENTS.md + VS Code extension (no hooks/skills equivalent at launch)
- **Verdict:** Tools complement, not compete — use Claude Code for complex interactive work, Codex for batching clear-cut tasks

**Action Items:**
- Consider ingesting this article into `wiki/claude-code-vs-codex.md` and updating `wiki/index.md` accordingly