# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article on Codex Subagents vs Custom Agents for the LoreAI blog.

**Key Exchanges:**
- Generated a full comparison piece (`use-subagents-and-custom-agents-in-codex`) covering architecture differences, use cases, and selection criteria for the two multi-agent approaches in Codex

**Decisions Made:**
- **Selection heuristic:** "One-time task decomposition → Subagents; Recurring standardized task → Custom Agents" — this is the core framing of the article
- **Positioning:** Subagents = zero-config, parallel, ephemeral; Custom Agents = configurable identity, reusable, team-shareable
- **Hybrid recommendation:** Mature teams use both — Custom Agents define roles, Subagents parallelize within those roles

**Lessons Learned:**
- Subagents inherit the parent Agent's context and tools; Custom Agents have independent system prompts, tool bindings, and configs
- Custom Agents built via Agent SDK, can bind MCP tools, enforce output format — higher setup cost but better auditability
- For individual devs / small teams, Subagents' zero-config is usually the better starting point; Custom Agents pay off at team scale (standardization)
- Codex Subagents run in cloud sandboxes vs Claude Code Agent Teams which run locally — important architectural distinction worth noting in future content

**Action Items:**
- Ensure the draft is saved to `drafts/` and any related wiki pages are cross-referenced
- Verify internal links (`codex-complete-guide`, `agent-sdk`, `agentic-coding`, etc.) all resolve to existing published content