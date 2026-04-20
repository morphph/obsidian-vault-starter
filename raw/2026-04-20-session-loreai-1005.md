# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a daily AI newsletter digest for 2026-04-20 covering Anthropic platform launches, Google TTS, and agentic architecture patterns.

**Key Exchanges:**
- No Q&A exchanges — single-turn newsletter generation task.

**Decisions Made:**
- Led with Anthropic's managed agent platform play as the week's dominant story arc.
- Framed the advisor strategy as the "Pick of the Day" because it pairs architecturally with Managed Agents — not just a cost tip but a complementary stack.

**Lessons Learned:**
- **Managed Agents + Advisor Pattern = intentional stack**: Anthropic shipped both in the same week — multi-model orchestration as a platform primitive alongside the cost-routing pattern that makes it economically viable. These are designed together.
- **Opus 4.7 adaptive thinking was patched on Day 1**: Launch-day tests showing weak reasoning were outdated within 24 hours. Benchmark comparisons from April 16 are stale.
- **Gemini's problem is the harness, not the model**: Mollick's framing — Gemini Pro 3.1 is competitive at the model layer but the product wrapper (no auditable CoT, clunky UX) limits it. Useful mental model for evaluating AI products going forward.
- **Model cascading terminology**: Fast-slow routing / advisor pattern is the formal name for what power users were doing ad hoc. Core builder skill as agentic runs scale.

**Action Items:**
- Consider ingesting Managed Agents platform docs into wiki (`platform.claude.com/docs/en/managed-agents/overview`)
- Consider creating or updating wiki pages: `claude-managed-agents.md`, `advisor-pattern.md`, `opus-4-7.md`
- Claude Code Hackathon deadline approaching — applications closing soon