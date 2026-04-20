# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/draft comparing Claude Code vs OpenAI Codex as AI coding tools, likely for LoreAI publication.

**Key Exchanges:**
- No interactive Q&A — session contains a single article text block for summarization

**Decisions Made:**
- None recorded in this session

**Lessons Learned:**
- **Claude Code vs Codex mental model:** Claude Code = local + interactive (pair programming); Codex = cloud + async (task delegation)
- **Key differentiators:**
  - *Context fidelity:* Claude Code sees local state (uncommitted changes, env vars, Docker); Codex needs everything committed + setup script
  - *Feedback loop:* Claude Code is real-time and steerable mid-task; Codex is submit-and-wait
  - *Parallelism:* Codex wins — native parallel cloud tasks; Claude Code needs multiple terminals
  - *Security:* Claude Code = code stays local; Codex = cloned to OpenAI servers
  - *Config system:* Claude Code has CLAUDE.md + skills + hooks + MCP (programmable stack); Codex only has AGENTS.md (no hooks/skills equivalent)
- **Pricing:** Claude Code (Pro $20/Max $100-$200 or API per-token); Codex (bundled in ChatGPT Pro $200, Team $30/user)
- **Codex free tiers:** open-source maintainers and students
- **Model stack:** Claude Code = Claude Opus/Sonnet; Codex = o3-based specialized model

**Action Items:**
- Article references internal links (`/blog/claude-code-agent-teams`, `/compare/claude-code-vs-cursor`, `/blog/codex-for-open-source`, etc.) — verify these slugs exist before publishing
- Consider ingesting this as a raw source if it's being published to LoreAI, then wiki page on `claude-code-vs-codex.md`