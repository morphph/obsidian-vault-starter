# Session Capture: loreai

**Date:** 2026-05-03
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest (2026-05-03) covering DeepSeek V4 launch, SWE-bench data efficiency research, and coding agent ecosystem developments.

**Key Exchanges:**
- Produced a 21-item structured newsletter JSON with sections: LAUNCH, RESEARCH, TOOL, TECHNIQUE, INSIGHT, BUILD, QUICK_LINKS
- Pick of the day: tiny LLM solving SWE-bench with only 250 training examples — thesis that data curation matters more than scale

**Decisions Made:**
- **Hero items chosen:** DeepSeek V4 Flash (speed/cost), DeepSeek V4 Pro (benchmarks vs Opus 4.7 Medium), 250-example SWE-bench result, Code with Claude conference
- **Model literacy concept:** "Scaling Laws vs. Data Efficiency" — linking the tiny-LLM result and DeepSeek V4 Flash's speed-first approach as twin challenges to bigger-is-better orthodoxy
- **Angle framing:** DeepSeek V4 positioned as open-source frontier closing gap on closed models; Codex /hatch framed as coding agents expanding into creative workflows

**Lessons Learned:**
- DeepSeek V4 Pro now surpasses Anthropic's Opus 4.7 Medium on independent benchmarks — open/closed gap continuing to shrink
- Agent-driven compute demand is the variable that invalidated the "AI bubble" thesis (Ethan Mollick / Atlantic piece)
- Architecture pattern emerging: agent harness outside sandbox, agent inside — trust boundary matters as teams ship more coding agents

**Action Items:**
- Track Code with Claude developer conference (next week) for potential wiki updates on Anthropic developer ecosystem
- Monitor DeepSeek V4 adoption and real-world performance reports for wiki page updates
- The 250-example SWE-bench paper deserves a dedicated wiki page if not already captured — challenges core assumptions about model scale requirements