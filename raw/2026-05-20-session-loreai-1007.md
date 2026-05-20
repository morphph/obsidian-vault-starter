# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the 2026-05-20 AI daily newsletter covering Karpathy joining Anthropic and Google I/O announcements.

**Key Exchanges:**
- Produced a full newsletter issue with 6 sections: 发布动态, 开发者工具, 研究前沿, 行业洞察, 技术实战, 模型小课堂

**Decisions Made:**
- Led with Karpathy → Anthropic and Google I/O as the two headline stories (biggest talent move + biggest product drop of the day)
- Featured DeepMind cellular aging discovery as 今日精选 (AI for Science graduating from benchmarks to real discoveries)
- Grouped Anthropic acquisitions (Stainless) + enterprise wins (KPMG 276K, PwC) as a pattern: vertical integration + locking down Big 4

**Lessons Learned:**
- Gemini 3.5 Flash pricing is 3x previous gen (Simon Willison analysis) — "cheapest option" positioning eroding
- AI companies converging on "model vendor → platform company" playbook (Anthropic acquiring Stainless, Mistral acquiring Emmi AI)
- Claude Managed Agents self-hosted sandbox = the "can use → dare to use" threshold for compliance-bound enterprises
- HTML as Claude Code output format outperforms plain text/Markdown (Anthropic blog finding)
- Multi-Token Prediction (MTP) explained as concept — key for evaluating local model speed claims

**Action Items:**
- Wiki pages to create/update: [[karpathy]], [[anthropic]] (Karpathy hire, Stainless acquisition, KPMG/PwC deployments), [[google-gemini]] (3.5 Flash, Omni, I/O 2026), [[claude-managed-agents]] (self-hosted sandbox), [[openai]] (Guaranteed Capacity, SynthID adoption), [[mistral]] (Emmi AI acquisition), [[mythos]] (Cloudflare independent validation)
- Track Gemini 3.5 Flash pricing trend — 3x increase signals market-wide price normalization
- Monitor what role Karpathy takes at Anthropic (research vs product vs new direction)