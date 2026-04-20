# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the 2026-04-20 AI精读 newsletter digest JSON — a daily roundup of Anthropic + AI industry news.

**Key Exchanges:**
- Session produced a structured newsletter JSON with 25 items across 6 sections (LAUNCH, TOOL, TECHNIQUE, RESEARCH, INSIGHT, BUILD)

**Decisions Made:**
- Pick of the day: item 25445, the Advisor Strategy pattern — framed as the first credible architecture for economically viable long agentic runs, not just a cost hack
- Model literacy concept: Model Cascading (Fast-Slow Routing) — paired with Managed Agents as first-class multi-model orchestration primitive

**Lessons Learned:**
- Opus 4.7 adaptive thinking was patched post-launch to activate more aggressively — worth flagging to readers who bounced on day one
- Gemini Pro 3.1 illustrates a growing gap: strong model, weak harness (no auditable CoT, manual canvas, minimal tool integration)
- The advisor pattern (cheap executor + smart advisor on hard steps) is the practical implementation of model cascading that power users were doing ad hoc

**Action Items:**
- Key wiki pages worth updating: `anthropic.md` (Managed Agents beta, Mythos/Glasswing preview, LTBT board addition), `claude-code.md` (Routines, desktop rebuild, v2.1.113), `google-gemini.md` (Flash TTS multi-speaker 70+ languages), `agentic-patterns.md` (advisor strategy)
- Qwen3.6-35B-A3B (Apache 2.0, 3B active params MoE) worth logging as open-source model milestone