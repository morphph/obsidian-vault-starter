# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language AI news newsletter draft for April 20, 2026, covering Anthropic and adjacent AI industry releases.

**Key Exchanges:**
- No back-and-forth — session produced a single newsletter draft covering ~15+ AI news items from that date.

**Decisions Made:**
- Newsletter structured into sections: 发布动态 / 开发者工具 / 技术实战 / 研究前沿 / 行业洞察 / 快讯, with a 今日精选 editorial pick at the end.
- Advisor Strategy chosen as the lead editorial pick — framed as architectural significance, not just cost optimization.

**Lessons Learned:**
- **Advisor Strategy** (Fast-Slow Routing): Use cheap model for most steps, escalate to expensive model only at decision bottlenecks. Claims 70-80% cost reduction with minimal quality loss. Becomes viable at scale when combined with Managed Agents platform routing.
- **Claude Managed Agents public beta**: Fully managed sandbox + tools + SSE streaming — removes infra barrier for small teams deploying autonomous agents.
- **Gemini product gap**: Ethan Mollick flagged Gemini Pro 3.1 as a strong model trapped in weak product (no auditable chain-of-thought, poor tool integration). Signal: model capability ≠ moat, product UX is.
- **Opus 4.7 Adaptive Thinking**: Triggered more frequently after day-1 criticism. Token cost up, quality improved.
- **Claude Mythos**: Anthropic's first vertical-specialized model (cybersecurity/defensive). Signals move beyond general-purpose toward domain-specific.
- **Qwen3.6-35B-A3B**: 35B params, 3B activated, Apache 2.0, consumer GPU viable — notable efficiency benchmark for open-source.

**Action Items:**
- Consider ingesting Advisor Strategy blog post (`https://www.claude.com/blog/the-advisor-strategy`) as a raw source — architectural pattern worth a dedicated wiki page.
- Consider ingesting Managed Agents docs (`https://platform.claude.com/docs/en/managed-agents/overview`) for wiki page on Claude infra.