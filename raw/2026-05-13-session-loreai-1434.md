# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Codex (OpenAI) vs Claude Code (Anthropic) subagent architectures for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Codex uses container-based isolation (each task = independent sandbox), Claude Code uses orchestrated subagents sharing local environment with parent coordination
- Claude Code supports worktree isolation as a middle ground — git-level isolation with parent-agent coordination
- Codex customization is flat (AGENTS.md + per-task prompts); Claude Code is layered (CLAUDE.md → SKILL.md → MCP servers → typed agents)

**Decisions Made:**
- Framing: These are **complementary models, not competing ones** — Codex for independent batch tasks, Claude Code for coordinated multi-step work
- Hybrid workflow recommended: Codex for bug fixes/docs/tests queue; Claude Code for refactoring/architecture/local-env tasks
- Practical Claude Code subagent limit: 2–4 parallel for best balance (5–8 max before context/cost issues)

**Lessons Learned:**
- Codex tasks share no mid-execution state — conflicts only discovered at merge time
- Claude Code's power comes from the extension stack (skills + hooks + agents + MCP), but requires investment in configuration
- Codex's security model (sandbox) is structurally safer than Claude Code's (permission-based trust); matters for team access control
- AGENTS.md (Codex) and CLAUDE.md (Claude Code) serve similar purposes and can share content for teams using both

**Action Items:**
- Article references several internal links (`/blog/claude-code-agent-teams`, `/blog/claude-code-subagents-examples`, etc.) — ensure these exist or are planned
- Pricing section notes rates change frequently — flag for periodic review
- Consider creating a wiki page: `codex-vs-claude-code.md` capturing this comparison for the knowledge base