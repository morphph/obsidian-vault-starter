# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curated the 2026-05-18 daily AI newsletter digest (20 items across INSIGHT, RESEARCH, TOOL, TECHNIQUE, BUILD sections).

**Key Exchanges:**
- Generated full newsletter JSON with headline hook: "Anthropic Overtakes OpenAI in Enterprise While LeCun Gives World Models 18 Months"
- Pick of the day: Ramp corporate card data showing Anthropic overtaking OpenAI in enterprise spend — framed as the shift from experimentation budgets to production infrastructure line items
- Model literacy concept: **Model Routing** — dispatching tasks to specialized models by capability and cost as the default multi-agent architecture

**Decisions Made:**
- Hero stories: Anthropic enterprise spend (INSIGHT), Anthropic engineer crowdsourcing Claude gaps (INSIGHT), LeCun's 12–18 month world model timeline (RESEARCH), Singapore FM building AI agent on Raspberry Pi (BUILD)
- Chose model routing as the educational concept, tied to the agent swarms quick link

**Lessons Learned:**
- Local LLM inference on Apple Silicon is more expensive per token than cloud APIs when hardware amortization + electricity are factored in — "local is free" narrative collapses under real math
- Mollick insight: AI consumer products need pre-built skills/guided workflows, not open-ended chat — structured UX beats blank text boxes
- The coding agent form factor (terminal-based) is commoditizing fast (DeepSeek-TUI at 30K+ stars)
- ArXiv's 1-year ban for fully AI-generated papers = first real enforcement mechanism against academic AI slop

**Action Items:**
- Wiki candidates: [[anthropic]] update with enterprise spend overtake milestone; [[world-models]] page for LeCun timeline; [[model-routing]] as emerging architecture pattern; [[claude-code-setup]] as new Anthropic tooling
- Track open-weight model flood (Gemma 4, DeepSeek V4, Kimi K2.6, MiMo 2.5, GLM-5.1) — Nathan Lambert calls it most eventful month for open-weight releases ever