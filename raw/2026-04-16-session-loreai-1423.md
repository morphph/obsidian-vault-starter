# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article between Codex CLI and Claude Code for potential wiki ingestion.

**Key Exchanges:**
- Article covers: security model, context/project understanding, extensibility, model quality, pricing, developer experience, and when to choose each tool.

**Decisions Made:**
- N/A (no user decisions recorded — this appears to be a pre-compact flush of article content)

**Lessons Learned:**
- **Security**: Codex CLI offers network-disabled sandbox by default (zero config); Claude Code uses hooks + permission system (more power, requires setup)
- **Context**: Codex CLI uses single `codex.md`/`AGENTS.md` file; Claude Code uses hierarchical `CLAUDE.md` (root + subdirs + user-level) + `SKILL.md` files + persistent memory across sessions
- **Extensibility**: Codex CLI is minimal/closed; Claude Code supports 5 mechanisms — SKILL.md, Hooks, MCP servers, Agent teams, Custom slash commands
- **Models**: Codex CLI → OpenAI (o3, o4-mini); Claude Code → Anthropic (Opus, Sonnet)
- **Pricing**: Both usage-based API billing; Claude Code also offers Claude Max subscription for heavy users
- **DX**: Codex CLI = low friction, quick start; Claude Code = steeper setup, compounding returns for team/complex projects
- **Verdict**: Codex CLI for solo/security-first/focused tasks; Claude Code for teams/large codebases/extensibility needs

**Action Items:**
- Consider ingesting this article as a raw source → wiki page comparing `codex-cli` vs `claude-code` as builder tools