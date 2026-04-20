# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an AI industry newsletter digest dated April 20, 2026 for knowledge worth capturing in the wiki.

**Key Exchanges:**
- Newsletter covers major releases: Claude Managed Agents public beta, Gemini 3.1 Flash TTS, Opus 4.7 workflow guide, Claude Mythos (cybersecurity model), OpenAI GPT Rosalind (life sciences)
- Model literacy concept introduced: **Model Cascading / Fast-Slow Routing** — pair cheap executor (Haiku) with smart advisor (Opus); escalate only on high-complexity steps; cuts token cost 60-80% on long agentic runs

**Decisions Made:**
- (No user decisions recorded — this is a passive newsletter review session)

**Lessons Learned:**
- **Advisor pattern insight**: Bottleneck in AI coding is not model intelligence but *when* to deploy it. Most steps in a 200-step agentic run are mechanical — Opus is only needed at ~5 ambiguous decision points
- **Harness is the product**: Mollick's observation on Gemini Pro 3.1 — model quality is necessary but not sufficient; the UX/harness wrapper determines user experience
- **Opus 4.7 adaptive thinking was patched Day 1** — launch-day evaluation underestimated the model; re-test if you dismissed it early
- **Managed Agents + Advisor Pattern arriving same week** is a deliberate stack — multi-model orchestration is now a first-class platform primitive

**Action Items:**
- Ingest this newsletter digest into wiki (covers: Claude Managed Agents, Opus 4.7, model cascading concept, Claude Mythos, GPT Rosalind, Anthropic governance/policy moves)
- Consider creating/updating wiki pages: `anthropic.md`, `claude-opus.md`, `model-cascading.md` (new concept), `openai.md`
- Note Claude Code Hackathon deadline is approaching — $100K prizes, $500 API credits