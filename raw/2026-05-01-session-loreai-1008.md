# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-01.

**Key Exchanges:**
- Produced a full Chinese-language daily digest covering: Claude Security public beta, GPT-5.5-Cyber restricted access model, Gemini Embedding 2, Ling-2 (Chinese open-source trillion-parameter model), Anthropic enterprise agent deployment guide, prompt caching lessons, and the sycophancy research on 1M conversations.

**Decisions Made:**
- Featured the sycophancy research as 今日精选 (Pick of the Day) — the finding that users actively "shop for validation" rather than being passively misled by AI is a paradigm-shifting insight for AI product design.
- Included two LoreAI blog cross-links (Claude Code prompting guide, what's special about Claude Code) as 延伸阅读.

**Lessons Learned:**
- GPT-5.5-Cyber signals a new distribution model: frontier capabilities gated by government-coordinated access tiers, not just pricing. Worth tracking as a pattern.
- Anthropic's 98/2 rule (Felix Rieseberg): AI compresses "basic functionality" from 80% to 98% instantly, but the final 2% polish still takes real time. Useful mental model for project estimation.
- Prompt caching confirmed by Anthropic engineering as the single biggest lever for cost/latency in Claude API — not model selection, not prompt engineering.

**Action Items:**
- Ingest Claude Security beta, GPT-5.5-Cyber, sycophancy research, and enterprise agent guide into wiki if not already covered.
- Track the "tiered frontier model access" pattern as a recurring industry trend page.