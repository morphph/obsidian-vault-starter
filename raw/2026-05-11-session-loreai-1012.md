# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User compiled/reviewed the daily AI newsletter for May 11, 2026, covering frontier model regressions, DeepSeek funding, and builder tools.

**Key Exchanges:**
- Newsletter content assembled covering: model regression patterns (Opus 4.7, Gemini 3.1, Sonnet 4.6 all regressing), DeepSeek's $7.35B raise, MCP token overhead problem, GPT-Realtime-2 enterprise demo

**Decisions Made:**
- Lead story angle: "frontier model regression isn't a fluke — it's structural" (RLHF over-optimization, training data pollution, alignment trade-offs)
- Pick of the Day: the monotonic improvement assumption is breaking down; actionable advice is pin versions + build own evals

**Lessons Learned:**
- Three structural causes of model regression: (1) RLHF over-optimization losing capability on untrained tasks, (2) AI-generated training data contamination, (3) alignment trading raw capability for safety
- MCP token overhead is real: 5-server setup burns ~55K tokens before any work starts (Playwright 13.7K, Chrome DevTools 18K)
- GBrain MCP thin client (v0.31.1) consolidates multiple MCP servers into single endpoint — signals MCP moving from dev tool to infrastructure
- DeepSeek hiring product talent from ByteDance, positioning as global frontier lab
- Shopify's AI agent "River" forces public-channel-only usage to create social learning of prompting

**Action Items:**
- Ingest newsletter content into wiki (model regression patterns, DeepSeek funding, MCP ecosystem developments)
- Update wiki pages: [[deepseek]], [[mcp-ecosystem]], [[model-evaluation]] with new data points
- Track Google I/O outcomes (referenced as inflection point for Gemini's identity)