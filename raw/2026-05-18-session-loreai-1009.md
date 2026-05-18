# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-18, covering enterprise AI spending shifts, open model releases, and developer tooling trends.

**Key Exchanges:**
- Anthropic overtook OpenAI in enterprise spending for the first time, per Ramp corporate card transaction data — signal that enterprise AI adoption has shifted from ChatGPT seats to API-driven developer workflows
- Yann LeCun publicly committed to a 12–18 month timeline for hierarchical world models at Meta FAIR
- Massive open-weight model release month: Gemma 4, DeepSeek V4, Kimi K2.6, MiMo 2.5, GLM-5.1 all dropped simultaneously
- ArXiv instituted one-year bans for fully AI-generated paper submissions — first major enforcement mechanism

**Decisions Made:**
- Pick of the Day: Ramp enterprise spend data chosen as top story, framed as "corporate AI crossing from experiment to infrastructure" — the AWS playbook analogy (making yourself indispensable to the build process)
- Model Literacy topic: Model routing — dispatching tasks to specialized models based on capability/cost rather than single frontier model

**Lessons Learned:**
- Local LLM inference on Apple Silicon is actually more expensive per token than cloud APIs when factoring hardware amortization, electricity, and idle time — "local is free" narrative debunked
- AI consumer products need pre-built skills and guided workflows, not open-ended chat (Mollick insight)
- AI accelerates execution but can't compress human coordination bottlenecks (process speed contrarian take)
- Terminal coding agent UX is becoming model-agnostic and commoditized (DeepSeek-TUI with 30K+ stars)

**Action Items:**
- Track LeCun's world model timeline — check back late 2027 for delivery
- Monitor Anthropic vs OpenAI enterprise spend trend in future Ramp reports
- Watch for KempeLab's next move after departing Meta FAIR reasoning team
- New tools to track: claude-code-setup plugin, Bindu (agent payments infra), narrator-ai-cli-skill
- Singapore FM's NanoClaw project — notable signal for AI literacy as leadership requirement