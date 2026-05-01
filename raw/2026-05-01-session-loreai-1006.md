# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI newsletter compiled for 2026-05-01 covering major industry announcements, techniques, and insights.

**Key Exchanges:**
- Claude Security enters public beta — full vulnerability scanner with auto-patching inside Claude Code (Enterprise tier)
- OpenAI's GPT-5.5-Cyber: first government-gated frontier model release, restricted to critical infrastructure defenders before GA — establishes dual-use technology precedent
- Ling-2: trillion-parameter open-source model from China claiming better token efficiency than Western efficient architectures
- Gemini Embedding 2 GA: first natively multimodal embedding model (text, images, video in single space)
- Anthropic published enterprise agent playbook covering orchestration, guardrails, and production patterns
- Anthropic analyzed 1M conversations on sycophancy — finding is that users actively seek validation, not just that models are too agreeable; implies fix is in product/UI design, not just model tuning
- Anthropic TypeScript SDK v0.92.0 ships improved Managed Agents APIs

**Decisions Made:**
- (none by user — this was newsletter output)

**Lessons Learned:**
- **Prompt caching is the #1 lever** for cost and latency in multi-turn agent systems (from Claude Code team's engineering lessons)
- **98/2 rule** (Felix Rieseberg): AI collapses 80/20 to 98/2 — getting to "basically works" is instant, last 2% polish still takes real time. Project estimation shape changes, not just speed
- **Karpathy's reframe**: Stop asking "how does AI make X faster?" — ask "what couldn't exist before?" New app categories, not faster old ones
- **Mollick's natural experiment**: Microsoft and OpenAI have identical model access but built divergent products — model capability is necessary but insufficient; product design and distribution are the real moat
- **Shai-Hulud malware in PyTorch Lightning** — supply chain attacks targeting ML infrastructure are escalating
- **Zig's AI contribution ban reasoning**: code review is about growing contributors, not just code quality; AI submissions short-circuit the mentorship loop

**Action Items:**
- Ingest Claude Security public beta into wiki (new Anthropic product)
- Ingest GPT-5.5-Cyber and government-gated model precedent
- Update wiki on Ling-2 / China open-source frontier race
- Ingest Anthropic enterprise agent playbook and prompt caching lessons
- Ingest sycophancy research (1M conversations study) — significant for AI alignment understanding
- Note SDK update: Anthropic TypeScript SDK v0.92.0 with Managed Agents API changes