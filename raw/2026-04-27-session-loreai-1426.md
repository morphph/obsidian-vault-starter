# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article — Claude Code vs Codex CLI — likely for ingestion into the wiki or publication on LoreAI.

**Key Exchanges:**
- No back-and-forth; this was a single content review request against a long-form article comparing the two tools across 8 dimensions: context system, extensibility, security, pricing, IDE integration, use cases, and verdict.

**Decisions Made:**
- None recorded — this appears to be a passive review/flush request, not a task session.

**Lessons Learned:**
- **Codex CLI uses codex-1**, built on OpenAI's o3 reasoning model family; optimized for code generation and sandboxed async task delegation.
- **Claude Code wins** on: context (CLAUDE.md / SKILL.md / auto-memory), extensibility (hooks, MCP, sub-agents), IDE integration breadth, interactive/judgment-heavy tasks.
- **Codex CLI wins** on: default container isolation, predictable flat pricing for heavy team use, zero-setup team adoption.
- **Pricing**: Codex CLI = $200/month (ChatGPT Pro); Claude Code = usage-based API (~$50–100/month for moderate solo use).
- **AGENTS.md** is Codex CLI's equivalent of CLAUDE.md — less mature ecosystem.
- Recommended hybrid: Claude Code for interactive dev, Codex CLI for batch async delegation.
- Article dated to mid-2026 — reflects current state as of this session.

**Action Items:**
- Consider ingesting this article as a raw source (`/ingest`) and creating or updating a `codex-cli.md` wiki page with comparisons to Claude Code.
- May warrant updating the existing `claude-code.md` wiki page (if it exists) with Codex CLI contrast points.