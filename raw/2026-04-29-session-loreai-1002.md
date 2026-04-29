# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the daily Anthropic/AI digest — scoring and selecting ~24 candidate stories for the newsletter.

**Key Exchanges:**
- Reviewed recent newsletter coverage to avoid duplication, then analyzed and scored candidates across categories (LAUNCH, TOOL, INSIGHT, RESEARCH, TECHNIQUE, BUILD)

**Decisions Made:**
- Top-scored stories: Claude Blender MCP connector (95), Claude Code onboarding blog post (92), Mistral Workflows (91), GPT-5.4 solving Erdős problem (90), OpenAI models on Amazon Bedrock (90)
- Included two VibeVoice entries (Simon Willison review + GitHub repo) — signals strong interest in open-source STT with speaker diarization
- Covered the OpenAI $8 ChatGPT tier → 122M subscriber projection as a business model inflection point
- Noted Claude Code's rapid release cadence: 50+ stability fixes across 4 CLI releases (v2.1.121–v2.1.122)

**Lessons Learned:**
- OpenAI's multi-cloud pivot (landing on Bedrock after dissolving Microsoft exclusivity) is a major enterprise procurement shift worth tracking over time
- Creative tooling MCP connectors (Blender, FigJam) signal expansion of agentic AI beyond code into design/3D workflows
- IP ownership of AI-generated code is becoming a live legal question (trending HN discussion on Claude Code specifically)

**Action Items:**
- Track OpenAI-on-Bedrock enterprise adoption as a recurring theme
- Monitor VibeVoice adoption as potential Whisper replacement in production voice pipelines
- Watch how OpenAI's $8 tier cannibalization of $20 Pro affects broader API pricing strategy