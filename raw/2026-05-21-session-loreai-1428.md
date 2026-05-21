# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/review of a comprehensive comparison article: Codex CLI vs Claude Code for AI-assisted coding.

**Key Exchanges:**
- Detailed architectural comparison: Codex CLI = sandbox-first (isolation), Claude Code = local-first (permission-based)
- Codex CLI uses `AGENTS.md` (flat); Claude Code uses `CLAUDE.md` + `SKILL.md` (two-tier programmable instruction system)
- Codex CLI = async task delegation model; Claude Code = real-time conversational/pair-programming model
- Claude Code leads in multi-agent orchestration (agent teams, MCP, extension stack); Codex CLI doesn't yet offer multi-agent in CLI form

**Decisions Made:**
- Verdict: Claude Code is the stronger choice for most active daily developers due to interactivity, local env access, skill system, and multi-agent capabilities
- Codex CLI recommended when: sandbox isolation is a hard requirement, async delegation preferred, or already in OpenAI ecosystem
- Both tools can be used together — Claude Code for interactive work, Codex CLI for well-defined async batch tasks

**Lessons Learned:**
- Sandbox isolation (Codex) means no `npm install`, no external APIs, no private registries unless networking explicitly enabled — maximum safety but workflow impedance mismatch
- Permission-based safety (Claude Code) requires active configuration but enables workflows sandboxing fundamentally can't support (hooks, local build tools, authenticated sessions)
- Pricing decision rule: already on ChatGPT Plus → Codex CLI is free to try; starting fresh with heavy use → Claude Max $100/mo better cost predictability than per-token
- The interactivity gap has real consequences: ambiguity → Claude Code asks you; Codex CLI guesses and you review after

**Action Items:**
- Article references several internal blog posts (skills guide, hooks guide, security scanning, MCP server creation, agent teams) — ensure wiki pages exist for these concepts
- Consider creating wiki page: `codex-cli-vs-claude-code.md` summarizing this comparison
- Track Codex CLI multi-agent roadmap — noted as likely coming but not available yet (as of article date)