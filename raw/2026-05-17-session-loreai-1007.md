# Session Capture: loreai

**Date:** 2026-05-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User produced/reviewed the 2026-05-17 AI daily newsletter digest (appears to be a completed draft ready for publication).

**Key Exchanges:**
- Newsletter covers: OpenAI's 48-hour GPT-5.5 Codex regression, a 30B MoE model (3B active params) winning Olympiad gold, CTF scene dying due to frontier AI

**Decisions Made:**
- Pick of the Day: CTF death as preview of all competitive skill domains (not just a security story)
- Model Literacy section explains MoE/active parameters — framing "parameter count on the label is increasingly misleading"

**Lessons Learned:**
- OpenAI acknowledged production model instability publicly — frontier models aren't static artifacts, they can silently degrade
- MoE efficiency thesis validated: 3B active parameters matching frontier reasoning at fraction of inference cost
- CTF is first competitive domain to fully break under AI capability pressure — pattern will repeat wherever "practice makes perfect" meets "AI iterates faster than you practice"
- Anthropic's Mythos: 11x multiplier on security vulns (250 vs 22) explains why it's unreleased — capability gap drives caution
- Gemini Pro rumored at GPT-5.5 coding level at $12/1M output (50%+ cheaper than OpenAI)
- Talent premium in AI has decoupled from output (River AI: $5B valuation, no product)
- Second scaling law undefeated: more thinking tokens → better results, no plateau observed yet

**Action Items:**
- Ingest CTF death essay (kabir.au/blog/the-ctf-scene-is-dead) — cross-domain implications for competitive skill domains
- Track Anthropic Mythos — 250 vulns benchmark is significant capability signal
- Track Cerebras $60B IPO as public AI chip comparator
- Note Claude API grey markets (Chinese resellers at 10% list price) — distribution/pricing intelligence