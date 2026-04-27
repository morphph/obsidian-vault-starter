# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a detailed comparison article between Codex CLI and Claude Code as coding agent tools.

**Key Exchanges:**
- Article covers: context/instruction systems, task parallelism, feedback loop speed, safety models, pricing, IDE integration, model capabilities, and decision frameworks
- Verdict: the two tools are **complementary**, not interchangeable — Codex CLI for parallel throughput on well-scoped tasks, Claude Code for interactive depth and complex/exploratory work

**Decisions Made:**
- No decisions made this session — this appears to be source material review only, with no edits or ingest commands issued

**Lessons Learned:**
- Codex CLI strengths: async parallel execution, sandboxed safety by default, GitHub-native PR workflow, bundled with ChatGPT Pro/Enterprise pricing
- Claude Code strengths: real-time interactive steering, MCP ecosystem for external tool integration, programmable hooks/skills/sub-agents, local environment access
- Key differentiators by dimension:
  - **Feedback loop**: Codex = minutes (async); Claude Code = seconds (real-time)
  - **Safety**: Codex = sandbox isolation by default; Claude Code = configurable allowlists in real env
  - **Parallelism**: Codex = cloud-native multi-task; Claude Code = sub-agents within session
  - **Pricing**: Codex = bundled with ChatGPT plans; Claude Code = usage API or Max subscription
- Recommended hybrid: queue well-scoped backlog to Codex CLI, handle complex/exploratory tasks with Claude Code
- Old OpenAI Codex model (2021, GPT-3 descendant) ≠ Codex CLI (2025, RL-trained codex-1 model)

**Action Items:**
- If this content is meant to be ingested into the wiki, run `/ingest` on the source file to create a `codex-cli-vs-claude-code.md` wiki page