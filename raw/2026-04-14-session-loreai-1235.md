# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Content intelligence pipeline processing Twitter/HN signals about Claude Code and MCP developments to determine wiki/blog refresh actions.

**Key Exchanges:**
- 12 signals processed (indices 21–32), each evaluated for target pages and action type (refresh / refresh_and_create / ignore)
- Two signals ignored: Power Apps MCP (too niche/enterprise) and Zen skills package (pre-release, no artifact)

**Decisions Made:**
- **Anthropic MCP Registry** (signal 25): Confirmed as a real structural product feature — third-party servers can be published and auto-discovered by agents. Flagged for `refresh_and_create` with suggested keyword `anthropic mcp registry claude code`.
- **claude-mem security incident** (signal 30): Unauthenticated API endpoints, API keys exposed in plaintext, launched `$CMEM` token. Flagged for new blog: "how to evaluate third-party Claude Code extensions for security."
- **FileCity everything-claude-code** (signal 32): 47 agents + 181 skills reference harness — identified as a "production-grade Claude Code harness" content angle not currently covered.
- **StartSession hooks** (signal 27): Anthropic team officially confirmed as the intended mechanism for script automation in the Claude Code desktop app, which also abstracts worktree complexity.
- **MCP as cross-team distribution layer** (signals 21, 26): Recurring pattern — Sales/Marketing/CS/Engineering all consuming same Markdown strategy docs via MCP. Reinforces the "Claude Code is not a coding tool" narrative.

**Lessons Learned:**
- GTM/non-technical MCP adoption is a confirmed recurring pattern (at least 2 independent signals in this batch).
- Gemma 4 is newly viable as a local/free Claude Code alternative via Ollama — free-alternatives content predates this model and needs updating.
- Security vetting of third-party Claude Code extensions is an unaddressed content gap surfaced by a real incident.

**Action Items:**
- Create FAQ: `anthropic-mcp-registry-claude-code`
- Create blog: `claude-code-extension-security-risks` (anchor on claude-mem incident)
- Create blog: `claude-code-agent-harness-production-setup` (anchor on FileCity)
- Refresh hooks guides with StartSession desktop app confirmation
- Refresh free-alternatives blog with Ollama + Gemma 4
- Refresh MCP setup guide with Registry, Seedance (design-to-video), Arcade (GTM) examples
- Monitor Claudraband HN thread for more details before acting