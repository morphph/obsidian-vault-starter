# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/drafting a comparative analysis article on Codex CLI vs Claude Code for the LoreAI blog.

**Key Exchanges:**
- The content covers a detailed comparison across: sandbox/security model, context systems, extensibility, model quality, pricing, and git workflow integration.

**Decisions Made:**
- Article framing: Codex CLI = "safety-first, open-source" vs Claude Code = "capability-first platform"
- Verdict structure: neither is universally better; use case determines choice
- FAQ section included to handle common confusions (e.g., Codex CLI ≠ original Codex model)

**Lessons Learned:**
- Codex CLI's network-disabled sandbox is a **hard technical constraint** in full-auto mode, not just policy — cannot fetch docs, install packages, or push to remotes
- Claude Code's context system (CLAUDE.md + SKILL.md + hooks + auto-memory) is **multi-layered and persistent** vs Codex CLI's single `AGENTS.md` per session
- Codex CLI has free tier programs: open-source maintainer access + $100 student credits
- Claude Code available via Anthropic API, Max subscription, AWS Bedrock, or GCP Vertex AI
- Both tools can coexist in the same repo (AGENTS.md + CLAUDE.md)

**Action Items:**
- Article references internal blog links (`/blog/claude-code-memory`, `/blog/claude-code-hooks-*`, `/blog/codex-complete-guide`, `/faq/is-codex-cli-safe-to-use`) — verify these slugs exist before publishing
- Consider ingesting this as a raw source into the wiki under a `codex-cli-vs-claude-code.md` page