# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI digest compiled for 2026-05-15, covering Anthropic news, model releases, and ecosystem tools.

**Key Exchanges:**
- Newsletter JSON generated with 24 items across 6 sections (Insight, Launch, Research, Technique, Tool, Build) + 7 quick links
- Pick of the day: Gemini 3.2 Flash's cost-performance implications (distillation + sparse MoE collapsing the quality-cost frontier)

**Decisions Made:**
- Hero selections: Anthropic $200M Gates Foundation (Insight), Claude for Small Business (Launch), Gemini 3.2 Flash rumors (Research), Claude Code large codebase guide (Technique)
- Model literacy topic: Knowledge Distillation & Sparse Mixture-of-Experts — tied to Flash rumors

**Lessons Learned:**
- Anthropic is systematically expanding Claude's addressable market: legal → small business → API credits for all paid tiers
- The open/closed model gap is closing (GLM 5.1 leading Artificial Analysis index)
- MCP crossed enterprise threshold with official AWS server launch
- Claude Code v2.1.142 introduced five agent flags (`--add-dir`, `--settings`, `--mcp-config`, `--model`) making multi-repo workflows first-class

**Action Items:**
- Wiki pages to create/update: [[anthropic]] (Gates $200M, US-China paper, Claude for Small Business, API credits, Mythos 250 vulns), [[gemini]] (3.2 Flash rumors), [[claude-code]] (v2.1.142, large codebase guide, 50% limit increase), [[mcp]] (AWS official server), [[open-source-models]] (GLM 5.1)
- Track June 15 date for programmatic API credits launch
- Track July 13 date for Claude Code 50% limit increase expiry
- Gemini 3.2 Flash claims unconfirmed — flag for verification at Google I/O