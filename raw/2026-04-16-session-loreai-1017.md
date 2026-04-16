# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a newsletter draft covering AI developer tooling launches from 2026-04-16.

**Key Exchanges:**
- Draft produced covering: Claude Code Desktop redesign, Claude Code Routines launch, OpenAI Agents SDK sandbox update, Gemini 3.1 Flash TTS, Gemini Robotics-ER 1.6, Humwork (YC-backed MCP server that pays humans when agents fail), VAKRA benchmark (IBM Research), Notion's 5-rebuild journey, $0 open-source AI stack.

**Decisions Made:**
- Framing thesis: The AI race has shifted from "better models" to "better orchestration" — Claude Code Routines and OpenAI Agents SDK both bet on event-driven autonomous agent infrastructure.
- Pick of the Day: Claude Code Routines, framed as the moment AI coding tools cross from chat assistants to autonomous infrastructure.

**Lessons Learned:**
- VAKRA benchmark finding worth tracking: agents fail more on tool selection and parameter formatting than on reasoning itself — important signal for agent evaluation design.
- Event-driven agent architecture (cron, webhook, API trigger) is the new paradigm; understanding this shift from "chatbot you talk to" → "service that reacts" is key for production agents.
- Humwork's wedge: "agents need help too" — MCP server routes stuck agents to verified human experts in 30s. Interesting model for human-in-the-loop at the agent layer.

**Action Items:**
- Consider ingesting Claude Code Routines launch details into wiki (Claude Code page or new routines page).
- VAKRA benchmark and Humwork both worth tracking as new entries.