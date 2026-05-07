# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Building the daily AI newsletter digest for 2026-05-07 — a major news day anchored by the Anthropic-SpaceX compute deal and Claude Managed Agents launch.

**Key Exchanges:**
- Generated full newsletter JSON with 23 items across INSIGHT, LAUNCH, TOOL, RESEARCH, BUILD sections plus quick links
- Pick of the day: DeepMind × EVE Online alignment testbed — thesis that adversarial MMOs are the only environments complex enough to test agent safety at scale
- Model literacy concept: "Asynchronous Agent Reasoning (Dreaming)" — agents reasoning between sessions without user prompts

**Decisions Made:**
- Hero stories: SpaceX-Anthropic compute deal (INSIGHT), Claude Managed Agents with dreaming (LAUNCH), OpenAI open-source MRC networking protocol (TOOL), DeepMind × EVE Online (RESEARCH)
- Framed SpaceX deal as "bypassing traditional cloud" — new compute partnership model outside AWS/Azure/GCP
- Framed MRC as "TCP/IP of GPU clusters" — five competitors agreeing networking isn't a moat
- DeepSeek $50B valuation positioned as validation of open-source frontier model business model

**Lessons Learned:**
- Usage limits doubling immediately after SpaceX deal (34095) shows Anthropic translating infra deals into user value fast — worth tracking as a pattern
- ServiceNow research (34029): training agents for first-try correctness beats training for self-repair — practical insight for code-gen pipeline design
- Sierra hitting $150M ARR selling services not APIs confirms the "AI labs → services companies" pivot thesis

**Action Items:**
- Wiki pages to create/update: SpaceX-Anthropic compute deal, Claude Managed Agents (dreaming/outcomes/multiagent), MRC protocol, DeepMind EVE Online alignment
- Track SubQ claims (50x faster, 20x cheaper, 12M context) — flagged as "big if" pending independent validation
- Next.js 16.2.5 security patch — actionable for any projects using Next.js in production
- Anthropic Python SDK v0.100.0 — milestone release with full managed agents support