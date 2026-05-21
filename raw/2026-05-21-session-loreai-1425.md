# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Review/ingest of a comparison article: Codex CLI vs Claude Code — positioning, architecture, and use-case guidance.

**Key Exchanges:**
- Detailed feature comparison between OpenAI's Codex CLI (cloud sandbox, async, stateless) and Anthropic's Claude Code (local execution, real-time, persistent memory)
- Decision frameworks for choosing between the two tools across 6 dimensions: execution model, context/memory, workflow (sync vs async), safety/sandboxing, pricing, IDE support

**Decisions Made:**
- Article verdict: Claude Code is the better daily driver for active developers; Codex CLI is better for task delegation at scale
- Recommended hybrid setup: Claude Code for interactive dev work, Codex CLI for batch/parallel operations
- Pricing models differ fundamentally: Codex = subscription-bundled (ChatGPT Pro/Team/Enterprise), Claude Code = pay-per-token API billing ($0.50–$5.00/session typical)

**Lessons Learned:**
- Codex CLI's sandbox model prevents local side effects but cannot access private resources (DBs, APIs, auth services) — tests requiring real infra must be mocked
- Claude Code's persistent context (CLAUDE.md, SKILL.md, auto-memory) compounds in value over weeks — Codex re-learns project structure every run
- Sync interaction (Claude Code) catches misunderstandings in seconds; async (Codex) discovers them only at review time — wasted compute
- Neither tool should have unreviewed access to production; code quality depends more on underlying model than tool wrapper
- Codex has free tiers for students and open-source maintainers; Claude Code has no free tier

**Action Items:**
- This article references several internal links (`/blog/claude-code-hooks-mastery`, `/blog/claude-code-memory`, `/blog/codex-for-students`, etc.) — if publishing on LoreAI, verify these resolve or convert to wiki references
- Content is suitable for ingest into wiki under AI tools/builder workflows category — could fan out to pages on [[Codex CLI]], [[Claude Code]], and a comparison page