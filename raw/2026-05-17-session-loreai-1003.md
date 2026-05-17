# Session Capture: loreai

**Date:** 2026-05-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generating the daily AI newsletter digest (2026-05-17 edition) with curated items from HN/sources.

**Key Exchanges:**
- Produced a 22-item newsletter JSON covering launches, insights, research, tools, techniques, and build stories
- Pick of the day: AI breaking open CTF competitions — first concrete proof AI collapses skill gradients in competitive domains

**Decisions Made:**
- Model literacy concept: Mixture of Experts (Active vs Total Parameters) — tied to the 30B-A3B Olympiad gold story
- Hero items: 30B MoE reasoning model, GPT-5.5 silent regression fix, Gemini Pro pricing rumors, PrimeIntellect autonomous AI research
- Framing: GPT-5.5 reliability as "production infrastructure problem," CTF collapse as "warning shot for all puzzle-solving domains"

**Lessons Learned:**
- GPT-5.5 had a ~48hr silent capability regression in Codex that went undetected until users noticed — frontier model monitoring is still immature
- Anthropic's Mythos found 250 security vulns vs 22 from prior models (11x) — explains cautious release strategy
- No plateau observed yet in test-time compute scaling across multiple domains (math, hacking, science, crosswords)
- Chinese grey market selling Claude API at 10% of list price via promo credit pools — documented by Oxford researchers

**Action Items:**
- Potential wiki updates: Cerebras IPO ($60B), Gemini Pro pricing ($12/1M output), PrimeIntellect autonomous research, Anthropic Mythos capabilities
- Track: MoE architecture trend (efficiency thesis strengthening), CTF/competitive-domain AI disruption pattern
- Note for wiki: Anthropic dropped 2-hour masterclass on building Claude agents (memory, hooks, hallucination mitigation)