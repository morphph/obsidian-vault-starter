# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/published article comparing OpenAI Codex vs ChatGPT for developers — likely a LoreAI blog piece.

**Key Exchanges:**
- Detailed pricing breakdown: Free ($0) → Plus ($20) → Pro ($200) → Team ($25-30/seat) → Enterprise (custom). Codex requires Pro minimum ($200) or Team plan.
- Codex runs on **codex-1**, fine-tuned from o3 specifically for software engineering (RL from coding tasks, self-verification via tests).
- OpenAI offers a Codex student program with $100 free credits.
- Old Codex API (2021, deprecated 2023) ≠ current Codex agent (2025) — same name, entirely different products.

**Decisions Made:**
- Verdict positions them as complementary, not competitors: ChatGPT for understanding/planning, Codex for execution.
- "If you can only pick one" recommendation: ChatGPT Plus at $20/month for broadest coverage.

**Lessons Learned:**
- Codex's value gap widens for multi-step, multi-file tasks with test verification — comparable to ChatGPT for isolated questions.
- Codex is a poor fit for: repos without tests, non-GitHub repos, exploratory/undefined work.
- ChatGPT's model flexibility (GPT-4o, o3, o4-mini) is an advantage for mixed coding + non-coding workflows.
- Cost-per-task consideration: simple Codex tasks take seconds, complex ones run several minutes — bundled on Pro but worth monitoring on Team/Enterprise.

**Action Items:**
- This content references internal links (`/blog/codex-complete-guide`, `/faq/codex-download`, `/blog/codex-for-students`, `/subscribe`) — ensure those destination pages exist or are planned.
- Consider ingesting this into wiki as an OpenAI pricing/product page if not already captured.