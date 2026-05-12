# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Running `/ingest-anthropic-daily` sweep for 2026-05-12, selecting and scoring ~22 items across blog, Twitter, GitHub, HuggingFace, HN, and RSS sources.

**Key Exchanges:**
- Reviewed recent newsletter coverage before selecting to avoid duplication
- Curated 22 items spanning LAUNCH, INSIGHT, TECHNIQUE, RESEARCH, TOOL, and BUILD categories

**Decisions Made:**
- Top-scored items (93-95): Claude Code agent view launch (blog + tweet + release), Claude Platform on AWS — these are the headline Anthropic stories for the day
- OpenAI counter-moves scored high (91-92): Deployment Company (enterprise services pivot) and Daybreak (cybersecurity), positioned as competitive context
- Karpathy's "HTML as output" tip (89) linked back to swyx's "HTML is the new markdown" thesis from prior week — continuity tracked
- Gemini Flash 3.2 confirmation (82) flagged as cost-performance threat if it replaces GPT 5.5 low in high-volume inference

**Lessons Learned:**
- Claude Code v2.1.139's `/goal` command + agent view = multi-agent orchestrator pattern — bigger than either feature alone
- Claude Platform on AWS breaks the Bedrock-only constraint; SDK v0.101.0 shipped same day with native AWS client (coordinated launch)
- Criminal hackers using AI to find vulnerabilities crossed from theoretical to confirmed (NYT report) — validates both Daybreak and Mythos timing
- "Agentic search is 80% of context engineering" (Leonie workshop) — useful framing for the field

**Action Items:**
- Ingest these items into wiki pages (anthropic/claude-code, openai, web-agents, cybersecurity-ai, context-engineering)
- Update wiki/index.md with any new pages created
- Log the digest operation to wiki/log.md