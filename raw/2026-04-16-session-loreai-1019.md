# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Produced a Chinese-language newsletter issue (2026-04-16) covering AI developer tools, model releases, and research highlights.

**Key Exchanges:**
- Newsletter covers: Claude Code Routines (Research Preview), OpenAI Agents SDK sandbox/memory updates, Gemini 3.1 Flash TTS with Audio Tags, Humwork MCP Server (YC, human-in-the-loop for stuck agents), Gemini Robotics-ER 1.6 spatial reasoning, VAKRA benchmark (IBM), Notion's AI rebuild story, Baidu ERNIE-Image open-source.

**Decisions Made:**
- Lead angle: "AI coding tools cross a threshold from chat → autonomous infrastructure" — Claude Code Routines as the anchor story
- Event-driven Agent Architecture chosen as the 模型小课堂 concept (cron / webhook / API trigger paradigm)
- 今日精选 editorial conclusion: competition is shifting from best model → best orchestration layer

**Lessons Learned:**
- Claude Code Routines and OpenAI Agents SDK dropped same day — framing them as competing philosophies ("configure-and-run" vs "give you all the parts") works well editorially
- VAKRA finding worth highlighting: most Agent failures are edge-case tool-call handling, not model capability

**Action Items:**
- Consider ingesting Claude Code Routines as a wiki page (new product capability worth tracking)
- May want a wiki update on OpenAI Agents SDK feature state (sandbox, memory, open-source harness)