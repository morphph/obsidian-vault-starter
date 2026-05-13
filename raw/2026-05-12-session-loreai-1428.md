# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article draft comparing Codex CLI (OpenAI) vs Claude Code (Anthropic) as AI coding agents.

**Key Exchanges:**
- Detailed architectural comparison: Codex CLI uses cloud-sandboxed async execution (like delegating to a junior dev), Claude Code uses local-first interactive execution (like pair programming)
- Context system comparison: Codex CLI relies on single `AGENTS.md` file; Claude Code has multi-layered system (CLAUDE.md → SKILL.md → rules → hooks → memory)
- Extensibility: Claude Code extends via MCP servers, hooks, agent teams; Codex CLI extends via VS Code extension and ChatGPT ecosystem

**Decisions Made:**
- Article frames the tools as complementary, not competing — optimized for different workflows
- Verdict: Claude Code provides more capability for individual complex projects; Codex CLI provides safer/more scalable delegation for well-defined batch tasks
- Many developers will use both: Claude Code for interactive daily work, Codex CLI for overnight issue backlog processing

**Lessons Learned:**
- The key workflow question: "Do you know exactly what you want before you start, or do you figure it out as you go?" — this determines which tool fits
- Codex CLI's sandbox is safer by architecture (hard isolation); Claude Code is safe by permission (soft controls)
- Codex CLI clones repo fresh each task — no persistent codebase understanding across tasks; Claude Code maintains session context
- Pricing: Codex via ChatGPT plans ($20-$200/mo fixed); Claude Code via API usage-based or Max plan ($100/mo)
- Model: Codex uses codex-1 (RL fine-tuned for SWE); Claude Code offers Opus/Sonnet/Haiku tier selection

**Action Items:**
- Article references several internal links (`/blog/whats-so-special-about-the-claude-code`, `/blog/claude-code-hooks-mastery`, `/blog/claude-code-agent-teams`, etc.) — ensure these exist or are planned
- Codex CLI pricing/model details may need updating as OpenAI evolves offerings — flag for periodic review
- Consider ingesting this article into wiki as source material for `codex-cli.md` and updating `claude-code.md` wiki pages with comparison points