# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Review of 31 content signals (Twitter/HN) about Claude Code ecosystem developments for wiki/blog refresh decisions.

**Key Exchanges:**
- Signals were pre-classified with `action` labels (refresh / refresh_and_create / ignore) and mapped to target wiki pages and subtopics
- Three signals flagged as `ignore`: Spanish opinion tweet on skills framing, Perplexity Personal Computer comparison — no new factual content

**Decisions Made:**
- **PACER incident (signal 21):** Add financial/access safety warning to hooks guides — risk of unattended hooks triggering spend against credentialed third-party APIs
- **Garry Tan architectural limit (signal 28):** Document confirmed Claude Code limitation — bash system calls cannot be intercepted or post-run hooked; both hooks guides need this boundary documented
- **Uptime gap (signal 23):** Claude API has ~2 nines uptime vs Codex ~4 nines — add to vs-codex compare page and pricing FAQ
- **Anthropic 13 free courses (signal 31):** Includes "Claude Code in Action," "Intro to Agent Skills," two MCP courses — update install FAQ + skills FAQ with links; create roundup blog post

**Lessons Learned:**
- HeyGen shipped production video via Claude Code + HyperFrames (`npx skills add heygen-com/hyperframes`) — concrete non-coding use case with installable skill
- CodeBurn (GitHub: AgentSeal/codeburn) = open-source per-task token usage analyzer for Claude Code, surfaced on HN — reference in pricing/cost content
- Replica API wraps Claude Code + Codex as sandboxed embeddable agent with hooks, skills, SSE streaming — relevant to subagents/agent SDK subtopics
- GRAFT MCP server published with explicit cross-IDE install instructions including Claude Code

**Action Items:**
- Refresh: `claude-code-hooks-*` (PACER warning + Garry Tan bash limitation), `claude-code-vs-codex` (uptime), `claude-code-pricing` (uptime + CodeBurn), `claude-code-mcp-setup` (GRAFT), `claude-code-memory` (3-layer/permission framing from signal 26)
- Create new content: Claude Code video generation skill tutorial (HyperFrames), token usage tracking blog (CodeBurn), Anthropic free courses roundup blog