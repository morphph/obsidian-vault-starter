# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/draft comparing Claude Code vs OpenAI Codex as AI coding tools (likely for LoreAI blog).

**Key Exchanges:**
- Comprehensive feature comparison covering: execution model (local vs cloud), workflow (sync vs async), context systems, multi-agent scaling, security, and pricing

**Decisions Made:**
- Positioning framework: Claude Code = interactive/complex/local; Codex = async/scoped/isolated
- "Many teams will use both" — not zero-sum framing
- Verdict: Claude Code for senior devs valuing control/depth; Codex for teams valuing throughput/safety

**Lessons Learned:**
- Claude Code's differentiation centers on 3 axes: real-time interactivity, deep context (CLAUDE.md + SKILL.md + hooks stack), and multi-agent parallelism within a single task
- Codex's differentiation centers on: fire-and-forget async, sandbox isolation (no secrets access), multi-device/cloud-native, bundled with ChatGPT Pro
- Codex parallelism is at the task level (many independent tasks); Claude Code parallelism is at the sub-agent level (one task split across agents)
- Pricing as of 2026: Claude Max $100-200/mo or API billing; Codex via ChatGPT Pro $200/mo, Plus $20/mo, free for OSS maintainers, $100 credits for students

**Action Items:**
- This content should be ingested into wiki as a source — covers Claude Code capabilities, Codex competitive landscape, and pricing data points (all within wiki domain focus)
- Potential wiki pages to create/update: Claude Code features, Codex (OpenAI), AI coding tools comparison, pricing landscape