# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a detailed comparison article on OpenAI Codex vs ChatGPT for the wiki knowledge base.

**Key Exchanges:**
- Detailed breakdown of OpenAI Codex (May 2025 launch) as an async autonomous coding agent vs ChatGPT as a sync conversational tool
- Codex runs on **codex-1**, fine-tuned from o3 via RL on real coding tasks — exclusive to the Codex agent, not available in ChatGPT chat
- Codex operates in a **network-disabled sandbox** (no internet during execution) — strong isolation but all deps must be pre-installed
- Codex reads **AGENTS.md** (OpenAI's equivalent of project instruction files) for per-repo conventions
- Old Codex API (2021–2023, powered early Copilot) was deprecated March 2023 — current Codex is an entirely different product

**Decisions Made:**
- Article positions Codex for clear-spec tasks with test coverage; ChatGPT for exploration, learning, debugging, non-coding
- Recommended workflow: ChatGPT for design → Codex for implementation → ChatGPT for review

**Lessons Learned:**
- Codex's async model shifts developer role from writer to reviewer — latency tradeoff (minutes vs real-time)
- "Correct in isolation" ≠ "correct for your project" — Codex's repo awareness is its key differentiator over ChatGPT for coding
- Codex is best when codebase has existing test infrastructure it can run to verify its own work
- Free tier for verified open-source maintainers; $100 credits for eligible students

**Action Items:**
- Ingest into wiki: update or create pages for [[openai-codex]], [[codex-1-model]], and cross-reference with existing OpenAI/model pages
- Pricing data (Plus $20, Pro $200, Team $25-30) should be captured with a date stamp (May 2025 launch era) since it will likely change