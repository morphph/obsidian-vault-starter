# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working with a draft/source article comparing OpenAI Codex vs ChatGPT for the LoreAI blog.

**Key Exchanges:**
- Detailed comparison of Codex (autonomous coding agent with sandbox execution, repo access, PR delivery) vs ChatGPT (conversational, no repo access, copy-paste workflow)
- Codex is async/task-oriented; ChatGPT is sync/conversational — different interaction models suit different phases of work

**Decisions Made:**
- Codex requires Pro ($200/mo), Team, or Enterprise — not available on Free or Plus tiers
- Best practice: use ChatGPT for thinking/design phase, Codex for execution phase, ChatGPT again for code review — mirrors senior/junior engineer delegation pattern
- Hybrid workflow is the recommended default for serious engineering use

**Lessons Learned:**
- Codex's key differentiator: full repository context (reads project structure, imports, conventions, config files automatically) — eliminates the context-providing overhead of ChatGPT for large codebases
- Codex works best for well-scoped, batch-delegatable tasks (refactoring, test generation, dependency upgrades); ChatGPT better for exploratory debugging and learning
- OpenAI has student ($100 credits) and open-source maintainer programs for Codex access
- Codex runs in-browser (no install) with optional VS Code extension for IDE integration

**Action Items:**
- Article references several internal links (`/blog/codex-vscode`, `/blog/codex-complete-guide`, `/blog/codex-for-students`, `/blog/codex-for-open-source`) — ensure these exist or are queued for creation
- Pricing info dated "early 2026" — will need periodic freshness checks
- Consider ingesting this as a raw source and fanning out to wiki pages: `openai-codex.md`, `chatgpt.md`, updates to any existing AI tools comparison pages