# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article between Claude Code and Codex CLI for potential wiki ingestion.

**Key Exchanges:**
- The conversation context is a full article comparing Claude Code vs Codex CLI across six dimensions: execution model, developer experience, programmability, safety/trust, pricing, and IDE integration.

**Decisions Made:**
- No explicit decisions captured — this appears to be a read/review pass of source material, not an active working session.

**Lessons Learned:**
- **Claude Code vs Codex CLI decision rules (condensed):**
  - Local services / integration tests / real-time steering → Claude Code
  - Hard sandboxing / audit trails / async batch tasks → Codex CLI
  - Deep customization (CLAUDE.md, skills, hooks, MCP) → Claude Code only
  - Already on ChatGPT Pro/Team → Codex is essentially free marginal cost
  - Codex safety = isolation by construction; Claude Code safety = approval-based
  - Codex pricing: subscription-capped; Claude Code: usage-based (API or Max plan $100–$200/mo)
- The two tools are framed as **complementary**: Claude Code = AI pair programmer; Codex CLI = async task runner

**Action Items:**
- If this article is intended for the wiki, consider running `/ingest` on it as a source to create or update a `claude-code-vs-codex.md` wiki page under the "Builder tools and workflows" domain.