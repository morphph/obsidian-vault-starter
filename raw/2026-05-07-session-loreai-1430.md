# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing a comparison article on OpenAI Codex vs ChatGPT for coding tasks (appears to be a draft/source for LoreAI blog).

**Key Exchanges:**
- Detailed product comparison between OpenAI Codex (async coding agent) and ChatGPT (sync conversational AI)
- Codex is a completely different product from the deprecated 2021-2023 Codex API that powered GitHub Copilot autocomplete

**Decisions Made:**
- Article positions Codex and ChatGPT as complementary, not competing tools
- Framework: "ChatGPT for thinking, Codex for doing"

**Lessons Learned:**
- Codex requires Pro ($200/mo), Team, or Enterprise — not available on Free or Plus tiers
- Codex's key differentiator: clones full repo, understands structure, runs actual test suite in sandbox, iterates until tests pass
- Codex works best for well-defined tasks you'd assign to a junior dev; poorly suited for tasks needing architectural judgment
- Optimal workflow: explore/plan in ChatGPT → execute in Codex → review diffs in ChatGPT
- Quality of Codex output depends directly on quality of task description — using ChatGPT to refine specs before Codex improves results
- As of mid-2026: Codex has a VS Code extension for assigning tasks from IDE
- OpenAI offers free Codex access for qualifying open-source projects

**Action Items:**
- Ingest this article into wiki — updates needed for: OpenAI/Codex wiki page, pricing info, product capabilities
- Cross-reference with existing wiki pages on AI coding tools (Claude Code, Copilot, etc.)
- Article contains internal links (`/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/blog/codex-complete-guide`) suggesting it's part of a content cluster for LoreAI