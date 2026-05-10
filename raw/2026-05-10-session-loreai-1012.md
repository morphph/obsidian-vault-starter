# Session Capture: loreai

**Date:** 2026-05-10
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-10.

**Key Exchanges:**
- Newsletter covers: Baidu Ernie-5.1 launch, Anthropic alignment research ("teaching Claude why"), Google health coach preview, xAI Grok Voice, Antirez's ds4 local inference engine, Altman crowdsourcing next model priorities
- Pick of the Day: Anthropic's research on teaching Claude to understand reasoning behind rules (not just pattern-match)

**Decisions Made:**
- Framed Anthropic alignment research as more significant than Baidu's benchmark claims — reasoning: alignment-as-reasoning is a structural advance; benchmark scores are incremental
- Positioned Baidu's Saturday launch timing as the real story (3rd major Chinese lab drop in 2 weeks), not the unverified benchmark claims
- Included token consumption analysis (73% loss in Claude Code) as actionable technique content

**Lessons Learned:**
- Altman's crowdsource thread reveals market wants reliability/tool-use/sustained reasoning over raw intelligence — signal for product positioning
- Factory AI's 16-day multi-agent system: validation contracts written *before* implementation prevent drift — key architecture pattern
- WebRTC is wrong transport for server-to-client AI audio streaming (latency, session management, scaling issues)
- Weight quantization at 2-bit makes frontier models runnable on 128GB Macs — practical threshold crossed
- Anthropic growing 10x/year while competitors cut 10%+ staff — winner-take-most dynamic emerging

**Action Items:**
- Ingest Anthropic "teaching Claude why" research paper into wiki when full paper is available
- Track GitHub deprecation of Grok Code Fast 1 from Copilot (deadline: May 15)
- Monitor Ernie-5.1 independent evals when they land
- Consider wiki page for continuous diffusion language models if the research gains traction