# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Content signal triage for Claude Code SEO site — evaluating 20 signals (tweets, GitHub trending, releases) from May 4-5, 2026 for content actions.

**Key Exchanges:**
- 20 signals triaged with action routing (7 ignore, 6 refresh, 7 refresh_and_create)
- Each actionable signal mapped to specific target pages and subtopics

**Decisions Made:**
- **Ignore** ethically problematic content (signal 18: AIGC detection evasion) and niche/duplicate signals
- **New content gaps identified:**
  - `claude code project template CLAUDE.md` → FAQ (signal 4, viral "leaked" template thread)
  - `self-improving claude code skills eval loop` → blog (signal 5, 32→47/50 overnight)
  - `claude code with ollama local model` → blog (signal 6, Ollama v0.23.0 native support)
  - `claude code with deepseek cheaper alternative` → compare (signal 11, DeepClaude 17x cheaper)
  - `how to create claude code skills from documentation` → tutorial (signal 14, book-to-skill)
  - `claude code desktop app alternatives wrappers` → blog (signal 15, Sublodex)

**Lessons Learned:**
- CLAUDE.md is being perceived externally as "AI engineering infrastructure" — the project template pattern (rules + workflows + guardrails + skills) is a standalone content angle
- Self-improving skills via eval loops is emerging as a technique pattern (run N tests → score → rewrite prompt → retest)
- Cost reduction through backend-swapping (DeepClaude, Ollama local) is an active ecosystem trend — multiple signals converge on this
- Claude Code → Codex migration has a concrete file-mapping path: CLAUDE.md → AGENTS.md, settings.json → config.toml
- "Anti-slop" is becoming a framing for skills as quality-enforcement mechanisms (not just generation helpers)
- Notion MCP + CLAUDE.md for automated PM briefings validates non-coding use case angle

**Action Items:**
- Create 6 new content pieces identified above (FAQ, 3 blogs, 1 compare, 1 tutorial)
- Refresh existing pages: `blog/claude-code-mcp-setup` (add Lazyweb, TinyFish, Notion examples), `faq/claude-code-skills` (eval loops, book-to-skill, anti-slop pattern), `compare/claude-code-vs-codex` (migration path, DeepClaude), `blog/claude-code-memory` (CLAUDE.md portability across tools), `blog/claude-code-is-not-a-coding-tool` ($10k scraper story)
- Track Ollama + local model trend as potential disruption to pricing FAQ assumptions