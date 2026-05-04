# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Full feature comparison covering: execution model (local vs cloud), context systems (CLAUDE.md vs AGENTS.md), security trade-offs, pricing, multi-agent capabilities, IDE integration
- Claude Code = interactive local pair programmer; Codex = async cloud task delegator

**Decisions Made:**
- Framing: not "which is better" but "pair programmer vs background worker" — different tools for different workflow patterns
- Breakeven pricing ~$200/month (20 days × $10/day Claude Code ≈ ChatGPT Pro flat rate)
- Verdict: use both — Claude Code for interactive/complex tasks, Codex for well-defined async tickets

**Lessons Learned:**
- Claude Code's layered context system (CLAUDE.md + SKILL.md + memory) is its strongest competitive advantage — output quality improves over time
- Codex's isolation model (no network, ephemeral containers) provides security but limits verification to repo-contained tests only
- For tightly-coupled parallel work → Claude Code agent teams; for independent parallel tasks → Codex task queue
- Codex's AGENTS.md lacks persistent cross-session memory and layered skill system
- Code privacy difference is architecturally significant: Claude Code keeps source local, Codex uploads to OpenAI cloud

**Action Items:**
- Article ready for `drafts/` — consider running `/draft` to formalize
- Could ingest this as a wiki source comparing the two tools (useful reference for future builder-tool discussions)
- Pricing data may need updating — Claude Max plan ($100-200/mo) and Codex bundling with ChatGPT Pro ($200/mo) are time-sensitive claims