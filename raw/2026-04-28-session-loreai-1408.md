# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex for agentic coding.

**Key Exchanges:**
- Comprehensive feature comparison between Claude Code (local, interactive, terminal-first) and OpenAI Codex (cloud, async, sandboxed)
- Detailed breakdown of execution models: real-time pair programming vs task delegation

**Decisions Made:**
- Article positions both tools as complementary, not competing — "which execution model matches how you work?"
- Claude Code recommended for: complex refactoring, debugging, infra/DevOps, exploratory dev, external service tasks
- Codex recommended for: batch tasks, well-scoped changes, security-sensitive environments, async workflows, student/OSS use
- Pricing framing: Claude Code cheaper for light use (Pro $20/mo), Codex better cost certainty for heavy parallel use (Pro $200/mo flat)

**Lessons Learned:**
- Context systems differ fundamentally: Claude Code has persistent cross-session memory + hierarchical CLAUDE.md; Codex starts fresh each task with AGENTS.md, no memory unless encoded in repo files
- Codex sandbox = no internet access by design (security advantage but limits API/service tasks)
- Claude Code's extension stack (hooks, MCP, skills, agent teams) enables deep workflow customization; Codex's ecosystem focuses on integration (VS Code, ChatGPT, GitHub PRs)
- Key Codex limitation: no mid-task steering — wrong approaches only discovered at completion

**Action Items:**
- Article references several internal links (`/blog/codex-for-students`, `/blog/claude-code-hooks-mastery`, `/compare/claude-code-vs-cursor`, etc.) — ensure these destination pages exist
- Article ends with subscribe CTA for LoreAI — confirms this is publication-ready content for loreai.dev