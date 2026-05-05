# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-05.

**Key Exchanges:**
- Produced a structured newsletter JSON covering 22 items across LAUNCH, TOOL, RESEARCH, TECHNIQUE, INSIGHT, and BUILD sections

**Decisions Made:**
- Pick of the Day: DeepSeek V4 Pro (item 33303) — thesis that open-source cost curve is compressing faster than closed labs can monetize
- Model Literacy topic: MoE and Inference Cost Economics — explaining why parameter count is no longer a useful proxy for capability
- Hero items: DeepSeek V4 Pro, Unity AI open beta, Anthropic Claude as creative partner, Sierra $150M ARR

**Lessons Learned:**
- DeepSeek V4 Pro claims to outperform Opus 4.7 and GPT 5.5 at 10x lower inference cost — open-source crossing the frontier threshold
- Anthropic SDK v0.98.0 shipped full enterprise auth stack (Workload Identity Federation + OAuth + auth profiles + Managed Agents APIs) in both Python and TypeScript simultaneously
- Blueprint-Bench 2 shows humans still significantly outperform all frontier models on complex tasks — grounds superhuman capability hype
- Sierra's $150M ARR in <2 years ($15B+ valuation) is the fastest validation that enterprise agent deployment is a real revenue category
- DeepSeek V4's self-testing improves code pass rates but creates dangerous overconfidence on incorrect solutions — important failure mode for autonomous coding evaluation
- Context engineering (prompts, rules, memory) identified as the primary differentiator in agent quality, not model selection

**Action Items:**
- Ingest DeepSeek V4 Pro into wiki (model capabilities, MoE architecture, cost comparison vs closed models)
- Update Anthropic wiki page with SDK v0.98.0 enterprise auth features and Claude creative positioning
- Track Sierra as a signal for agent economy validation
- Note Unity's MCP Server integration as expansion of MCP ecosystem beyond coding tools