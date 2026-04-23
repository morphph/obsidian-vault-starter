# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating AI newsletter candidates for Apr 23, filtering against recent issues to avoid duplication.

**Key Exchanges:**
- Reviewed Apr 21–22 newsletters to identify already-covered stories: ChatGPT Images 2.0, Claude Cowork live artifacts, Kimi K2.6 launch, LeCun critique, ml-intern
- Identified fresh stories for Apr 23 across launches, tools, and insights

**Decisions Made:**
- Skip: GPT-Image-2 angles (7+ items Apr 22), Kimi K2.6 (Apr 21+22, only cost angle is fresh), LeCun critique, ml-intern
- Include for Apr 23: Qwen3.6-27B, OpenAI Privacy Filter, Google TPU 8th gen (split training/inference), Gemini Enterprise Agent Platform, Claude Code /ultrareview, Cowork interactive charts, Claude MCP blog, Workspace Agents in ChatGPT, VS Code Copilot BYOM, Shopify CTO deep-dive, OpenAI $1.5B PE venture, Karpathy model-rendered UI signal
- Top-scored picks: /ultrareview (95), MCP blog (93), Cowork charts (92), OpenAI Privacy Filter (90), Google TPU (90), Karpathy model UI (90)

**Lessons Learned:**
- Prompt caching stat worth noting: 79% of Anthropic API orgs don't use it; best integrations hit 92–96% cache rates — new dashboard available
- Kimi K2.6 cost angle: 5x cheaper than Sonnet 4.5, 10x cheaper than Opus 4.7 for agentic workloads
- Anthropic reversed Claude Code pricing within hours of announcement — documented by Simon Willison
- Claude Code wins Webby Award — signals AI coding tools are now mainstream product category
- Google Cloud shipped 13 official agent skills compatible with Gemini CLI, Codex, and Claude Code

**Action Items:**
- None explicitly stated; newsletter output was being assembled for publication