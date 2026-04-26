# Session Capture: loreai

**Date:** 2026-04-26
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the April 26, 2026 LoreAI newsletter draft covering major AI launches, funding, and research.

**Key Exchanges:**
- No interactive Q&A — session produced a full newsletter draft output.

**Decisions Made:**
- Newsletter structured into sections: Launch / Tool / Insight / Research / Technique / Build / Model Literacy / Quick Links / Pick of the Day
- Pick of the Day: Mollick's AI reproducibility / peer review angle (chosen for conceptual weight over pure hype)

**Lessons Learned:**
- DeepSeek-V4 positions million-token context as an agentic architecture decision, not a vanity metric — worth tracking separately from advertised vs. effective context length
- Google's $40B Anthropic deal + 5GW compute commitment is the largest AI investment on record; reshapes the Google/Amazon/Anthropic triangle
- Claude Code v2.1.117+ behavioral fix: stopped over-calling Grep/Glob, switched to native file ops — 4 months of complaints resolved
- Claude Code desktop now has a file browser (CMD+Shift+F)
- GPT-5.5 Pro API priced at $30/1M output tokens — most expensive frontier API tier ever
- Codex + GPT-5.5 one-shotting full apps is now a widespread developer report, not an isolated demo
- Meta signed a multi-billion Amazon Graviton deal for agentic inference — validates hybrid cloud even for vertically integrated players
- Kimi Code = drop-in Claude Code replacement from Moonshot AI (100 tok/s, 262K context, 2 env vars to switch)
- China moving to require prior approval for US investment in Chinese AI firms

**Action Items:**
- Consider updating wiki pages: `deepseek.md`, `anthropic.md`, `openai.md`, `claude-code.md` with today's developments
- New wiki page candidate: `effective-context-length.md` (advertised vs. effective context, lost-in-the-middle problem)
- Log today's newsletter publish in `wiki/log.md`