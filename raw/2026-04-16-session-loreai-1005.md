# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI news digest reviewed — 2026-04-16, covering launches, tools, research, and insights.

**Key Exchanges:**
- No interactive Q&A — digest was presented as a structured feed of scored items.

**Decisions Made:**
- None recorded — this was a read-only review session.

**Lessons Learned:**
- **Claude Code cost structure**: One developer's dashboard found 56% of spend = thinking tokens, only 21% = actual coding output. Critical signal for managing agentic coding costs.
- **Gemini Flash TTS Audio Tags**: Inline text directives for controlling vocal style/pace are more complex than they appear — Simon Willison flagged the prompt engineering required is non-trivial.
- **Mollick's 3-phase AI capability pattern**: Overhyped claims → quiet wins → breakthrough. Phase 1 poisons credibility for phases 2–3. Useful frame for evaluating new capability claims.
- **API credential trust gap**: Gas Town issue surfaces a growing risk — AI tools sitting between users and LLM APIs may misuse credits. Worth auditing any tools with API key access.

**Action Items:**
- Watch for Claude Opus 4.7 official announcement (reported imminent by The Information).
- Track EU AI Act + GDPR final amendments — decision expected within ~2 weeks of 2026-04-16. High stakes for training data rights and open-source AI.
- Evaluate Nucleus-Image (17B params / 2B active at inference) as a cost-efficient alternative to dense diffusion models.
- Explore Humwork MCP server as a "human-in-the-loop" fallback for agent workflows hitting capability limits.
- Review OpenAI Agents SDK sandbox environments (Vercel/Modal) for safer long-running agent deployments.