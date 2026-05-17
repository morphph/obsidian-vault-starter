# Session Capture: loreai

**Date:** 2026-05-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-17 with 22 items across 6 sections + quick links.

**Key Exchanges:**
- Produced full newsletter JSON with headline hook, model literacy explainer (MoE/Active Parameters), and pick of the day (CTF competitions broken by AI)

**Decisions Made:**
- Pick of the day: CTF story (id 38851) chosen for its "canary in the coal mine" thesis — first competitive skill domain to fall to AI brute-force iteration
- Model literacy topic: MoE and Active Parameters, tied to the 30B-A3B Olympiad gold story
- Hero placements: MoE model (LAUNCH), GPT-5.5 Codex regression + CTF death (INSIGHT), PrimeIntellect autonomous research (RESEARCH)

**Lessons Learned:**
- GPT-5.5 has had a documented ~48hr capability regression in Codex — "silent degradation" is now a known production pattern worth tracking
- MoE architecture has crossed from theoretical to competition-winning: 30B total / 3B active = Olympiad gold
- Test-time compute scaling (second scaling law) still shows no plateau across hacking, math, science
- Anthropic's Mythos found 11x more security vulnerabilities (250 vs 22) than prior frontier models — explains phased release strategy
- Steering vectors are becoming practical again thanks to DeepSeek-V4-Flash architecture

**Action Items:**
- Ingest key stories into wiki: MoE milestone, GPT-5.5 regression pattern, CTF domain collapse, PrimeIntellect autonomous research, Anthropic Mythos security results
- Track: Cerebras $60B IPO (public AI chip comparator), River AI $5B pre-product valuation (talent premium thesis), Gemini Pro pricing rumor ($12/1M output)
- Track new tools: Multica (open-source agent orchestration), Zerostack v1.0 (Rust Unix-philosophy agent), HomeClaw (MCP + Apple Home)