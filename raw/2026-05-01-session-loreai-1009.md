# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Assembling and formatting the daily AI newsletter for May 1, 2026.

**Key Exchanges:**
- Source material was provided covering: Anthropic SDK v0.92.0, Karpathy's Sequoia talk, Zig's AI ban, Meta employee tracking, sycophancy research, PyTorch Lightning malware, and more
- Newsletter was drafted with lead stories on Claude Security public beta, GPT-5.5-Cyber restricted rollout, and Anthropic's enterprise agent playbook

**Decisions Made:**
- Lead stories chosen: Claude Security (codebase scanning), GPT-5.5-Cyber (government-gated release), Anthropic enterprise agent playbook — prioritizing actionable builder news over commentary
- Pick of the Day: Anthropic's 1M conversation sycophancy analysis — chosen for its framework-shifting insight (product problem, not just alignment problem)
- Model Literacy topic: Prompt caching mechanics — chosen for direct builder relevance

**Lessons Learned:**
- Karpathy's reframe: stop asking "how does AI make X faster?" → ask "what couldn't exist before?" — useful product roadmap lens
- Zig's AI contribution ban reasoning: code review is for growing contributors, not just code quality — transferable framework for any org's review process
- Mollick's Microsoft-OpenAI natural experiment: identical model access → wildly different products — model access alone isn't a moat
- Sycophancy inversion: users actively shop for validation; fix may be UI/conversation design, not just RLHF
- Prompt caching was Claude Code team's single biggest lever for cost + latency

**Action Items:**
- Ingest newsletter sources into wiki (Anthropic SDK update, Claude Security beta, enterprise agent playbook, sycophancy research)
- Track GPT-5.5-Cyber as precedent for government-gated frontier model releases
- Monitor PyTorch Lightning supply chain attack developments
- Update [[anthropic]] wiki page with SDK v0.92.0 Managed Agents API changes