# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI news digest curation for May 20, 2026 — dominated by Google I/O and Anthropic enterprise moves.

**Key Exchanges:**
- Curated 25 scored items from multiple source tiers (Twitter, blogs, RSS, HuggingFace, HN)
- Pool spans Google I/O announcements, Anthropic partnerships/talent, OpenAI updates, and open-source research

**Decisions Made:**
- Top story: **Karpathy joins Anthropic** (score 98) — former Tesla AI lead, OpenAI founding team. Biggest talent move of the year.
- Google I/O 2026 cluster: **Gemini 3.5 Flash** (frontier agents/coding model), **Gemini Omni** (any-input-to-video generation), **Project Genie** (Street View → interactive 3D environments), **Gemini for Science** toolkit, **Chrome DevTools for AI agents**
- Anthropic enterprise cluster: **KPMG** (276K employees) + **PwC** deployments = two Big Four firms locked down. **Claude Managed Agents** adds self-hosted sandboxes and MCP tunnels (top enterprise blocker removed). **Stainless acquisition** = vertical integration of SDK/MCP surface.
- **Claude Code blog**: "Unreasonable effectiveness of HTML" as agent output format — practical technique
- **Cloudflare validates Mythos**: independent real-world security audit confirms 11x vulnerability discovery claims
- OpenAI: adopts **Google's SynthID watermark** (cross-company provenance cooperation); launches **Guaranteed Capacity** (compute as commodity market with forward contracts)
- **Mistral acquires Emmi AI**: European AI consolidation, same vertical integration playbook as Anthropic/Stainless

**Lessons Learned:**
- Simon Willison's Gemini 3.5 Flash pricing analysis: 3x predecessor but still cheaper than GPT-5.5 / Opus 4.7 — important context against I/O hype
- Enterprise AI adoption pattern: Big Four consulting firms are the beachhead for mass deployment (276K+ seats at once)
- AI compute becoming a commodity market — OpenAI's guaranteed capacity mirrors energy/cloud forward contracts
- Formal verification (TLA+) becoming more relevant as AI-generated code scales, not less

**Action Items:**
- Ingest Karpathy joining Anthropic → update [[anthropic]] wiki page (talent/team section)
- Ingest Google I/O 2026 cluster → create or update [[gemini]] wiki page with 3.5 Flash, Omni, Genie
- Update [[anthropic]] with KPMG/PwC enterprise deployments and Managed Agents updates
- Update [[claude-code]] with HTML effectiveness technique and v2.1.145 release notes
- Track Cloudflare Mythos validation → update [[mythos]] if page exists
- Note Mistral/Emmi acquisition → relevant to AI industry competitive landscape