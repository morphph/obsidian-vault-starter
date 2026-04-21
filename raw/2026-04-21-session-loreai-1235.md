# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Automated daily ingest run surfaced 11 Claude Code signals (GitHub trending + Twitter) with recommended wiki/blog actions for 2026-04-21.

**Key Exchanges:**
- Signal batch covered signals #21–31, all in the Claude Code domain
- Actions split between `refresh` (update existing pages) and `refresh_and_create` / `create` (new blog needed)

**Decisions Made:**
- **New blogs to create** (gaps confirmed):
  - `blog/claude-code-workflow-templates-starter-kit` — reusable workflow templates (Blink-h/agent-startup-kit)
  - `blog/claude-code-security-vulnerability-scanning` — pen testing MCP + hooks backdoor attack surface (CarbeneAI/Talon + s0ld13rr/claude-code-backdoor)
  - `blog/claude-code-macos-session-companion` — Notch-Pilot / session visibility on macOS
  - `blog/claude-code-unity-editor-game-development` — UniClaude with 60+ MCP tools for Unity
  - `blog/claude-code-design-prototyping` — HTML decks/prototypes via skills + Chrome DevTools MCP (bluzir/claude-code-design)

- **Pages to refresh** (add sections):
  - Hooks mastery blog: add reliability/stability tradeoffs + hooks-as-backdoor security warning
  - Non-technical use cases blog: add language learning (english-immersion) + OSINT/threat-intel (huntkit)
  - MCP setup blog: add Talon (pen testing), huntkit (OSINT), claude-code-design
  - `faq/claude-code-skills`: add english-immersion and design workflow as non-coding skill examples

**Lessons Learned:**
- Hooks in `settings.json` are a real attack surface — public PoC (`claude-code-backdoor`) demonstrates backdooring via shared/cloned project configs. Any hooks content must include a trust warning.
- Hooks reliability is questioned by practitioners for production use; agent platforms recommended instead for high-stakes automation.
- Claude Code is expanding into non-dev verticals: game dev (Unity), security/OSINT, language learning, UI design — all via MCP + skills pattern.

**Action Items:**
- Create 5 new blog drafts listed above
- Refresh hooks mastery, MCP setup, non-technical use cases, and skills FAQ pages with new examples and security section
- Tag `s0ld13rr/claude-code-backdoor` as high-urgency — add to security scanning page ASAP