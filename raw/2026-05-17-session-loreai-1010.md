# Session Capture: loreai

**Date:** 2026-05-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Producing the daily AI newsletter edition for Saturday, May 17, 2026.

**Key Exchanges:**
- Source material was provided covering: inference-time compute scaling (Mollick), Codex multi-machine orchestration, HomeClaw MCP for Apple Home, free coding agent stack (Open Code + Qwen 3.6 Plus), DeepSeek-V4-Flash steering vectors, Anthropic agent masterclass, Multica managed agent platform, Zerostack v1.0, personal AI agent architecture, MoE model literacy explainer, and CTF scene death analysis.
- Final newsletter structured around 3 lead stories + quick hits + model literacy + pick of the day.

**Decisions Made:**
- Lead story #1: 30B-A3B MoE model winning Olympiad gold (efficiency > brute force framing)
- Lead story #2: OpenAI's 48-hour GPT-5.5 Codex regression (rare transparency angle)
- Lead story #3: CTF competitions dying under AI pressure (cultural/existential framing)
- Model Literacy section explains MoE architecture and why "active parameters" matter more than total parameter count
- Pick of the Day: CTF death as preview of all competitive skill domains breaking under AI capability pressure

**Lessons Learned:**
- MoE active parameter count (3B active out of 30B total) is the new metric to watch — headline parameter counts are increasingly misleading
- Steering vectors (activation-space behavior modification without fine-tuning) are now practical on DeepSeek-V4-Flash architecture
- Multi-machine agent orchestration (Codex daisy-chaining computers) signals shift from "coding agent" to "control plane"
- Anthropic's Mythos found 250 security vulnerabilities where prior models found 22 (11x multiplier) — explains why it's unreleased

**Action Items:**
- Potential wiki pages: MoE architecture, steering vectors, Codex multi-machine, Multica, Zerostack, CTF-AI impact
- Track Cerebras ($60B IPO) as new public AI chip comparator
- Track Claude API grey markets (10% of list price via Chinese resellers) — distribution/pricing signal
- Track River AI (ex-xAI cofounder, $1B raise at $5B, no product yet)