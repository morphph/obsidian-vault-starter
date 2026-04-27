# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article between Claude Code and OpenAI Codex for potential wiki ingestion.

**Key Exchanges:**
- Article covers: execution model (local vs sandboxed cloud), multi-agent/parallel execution, pricing, IDE support, and when to choose each tool.

**Decisions Made:**
- No decisions captured — this appears to be a passive context review, not an active work session.

**Lessons Learned:**
- **Claude Code vs Codex core distinction:** Interactive collaboration (Claude Code, local, real-time) vs async delegation (Codex, sandboxed cloud, fire-and-forget).
- **Security posture difference:** Codex runs in isolated containers with no network access — stronger by default for regulated environments. Claude Code runs with full local permissions.
- **Multi-agent difference:** Claude Code sub-agents share session context and can coordinate (good for interdependent changes). Codex tasks are fully independent containers — parallel but uncoordinated (good for independent backlog items).
- **Pricing snapshot (as of article date):** Claude Code via Max plans ($20–$100/month) or API tokens. Codex via ChatGPT Pro ($200/month) / Team ($30/user/month) — no bundle discount.
- **Original Codex model (2021, deprecated 2023) ≠ current Codex agent (2025).** Same name, entirely different product.
- **Complementary use pattern:** Claude Code for active development sessions; Codex for async backlog task queue — not mutually exclusive.

**Action Items:**
- Consider ingesting this article as a raw source (`/ingest`) to create or update a `claude-code-vs-codex.md` wiki page covering the comparison, pricing, and architecture differences.