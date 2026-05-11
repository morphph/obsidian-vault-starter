# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily intelligence sweep (`/ingest-anthropic-daily`) processing 20 signals from Twitter and GitHub for the Claude Code content wiki.

**Key Exchanges:**
- Evaluated 20 signals; 5 ignored (crypto spam, duplicates, niche IoT, OpenCode misattribution, niche novelty), 7 refresh-only, 4 refresh-and-create, 2 create-only

**Decisions Made:**
- **Create content for:**
  - Karpathy's CLAUDE.md playbook (41%→11% error reduction) → blog: "karpathy claude.md best practices"
  - 73% token waste breakdown (CLAUDE.md 14%, history 13%, hooks 11%) → blog: "where do claude code tokens go"
  - Overnight autonomous coding risks (20k lines, no commits/tests) → blog: "claude code autonomous overnight coding"
  - 5-agent plugin orchestration pattern (brainstorm→plan→implement→review→validate) → tutorial: "claude code multi-agent plugin workflow"
  - HTML as Claude Code output medium (HN traction) → tutorial: "claude code generate html output"
  - Claude Certified Architect — Anthropic's first technical certification → FAQ: "claude certified architect certification"

- **Refresh existing pages for:**
  - AgentMemory (12-hook, 95.2% recall, 92% token reduction) → memory blog + hooks mastery
  - Ruflo 100-agent swarm → subagents blog + MCP setup
  - 115-command/67-MCP digital marketing plugin → plugin FAQ + MCP setup
  - DeepSeekCode (Claude Code fork) → vs-alternatives compare page
  - skill-set curated community collection → skills FAQ
  - claude-goal persistent /goal command → skills FAQ + CLI FAQ
  - huashu-md-html conversion skill → skills FAQ (non-technical use case)
  - "12 Claude Code Concepts" viral thread → topic hub + key FAQs

**Lessons Learned:**
- Community is building at scale on top of Claude Code's plugin/skill/hook system — ecosystem maturity signals are accelerating (100-agent swarms, 115-command plugins, curated skill packs)
- Token waste and cost optimization is an emerging high-intent topic cluster — multiple independent signals point to practitioner demand for efficiency guidance
- Non-technical use cases (HTML output, document conversion, digital marketing) keep surfacing as a distinct content gap

**Action Items:**
- 6 new pages to create (4 blogs, 1 tutorial, 1 FAQ) — prioritize Karpathy CLAUDE.md and token waste posts for search volume
- 8 existing pages to refresh with new community evidence
- None of the content has been written yet — this was triage/routing only