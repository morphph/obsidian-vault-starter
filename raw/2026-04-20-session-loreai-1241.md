# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Automated daily signal sweep (signals 64–80) routing GitHub trending + Twitter content about Claude Code tools into the wiki content pipeline.

**Key Exchanges:**
- No user-LLM dialogue — this is pipeline output (routing decisions, not a conversation).

**Decisions Made:**
- **AGENTS.md** emerging as a cross-agent instruction standard (competing with / complementing CLAUDE.md); a comparison page flagged as content gap (`suggested_content_type: compare`)
- **Memory-forge-rs** (Tauri/Rust, offline visual memory editor) flagged as new angle not covered by existing memory blog → new FAQ on session memory management
- **Notch-Pilot** (macOS notch companion, intercepts permission prompts, shows parallel sessions) → new blog on macOS companion tools category
- **claude-code-backdoor repo** confirms concrete security risk: malicious hooks in `settings.json` can backdoor Claude Code → hooks guide needs security section
- **Claude Code internal architecture** (ralph-loop: `while True: context → model → tool → result`) reverse-engineered and trending → new architecture explainer blog flagged
- **claudeclaw-os** (Telegram relay for Claude Code CLI on phone) → refresh remote sessions blogs as third-party alternative to official remote feature
- Korean legal skill (signal 68) and TikTok hook tweet (signal 64/80) → ignored as too niche/incidental

**Lessons Learned:**
- hooks/settings.json is an active attack surface — security framing needed in hooks documentation
- A new category of **macOS ambient companion tools** is forming (ClaudeWatch menu bar, Notch-Pilot notch app) — worth a dedicated blog
- AGENTS.md is gaining multi-agent adoption (Codex, Gemini CLI, Cursor) — not Claude-specific, signals a cross-tool standard forming
- Community skills are expanding into non-coding domains (language learning, motion graphics, legal docs) — validates "not a coding tool" framing

**Action Items:**
- Create: `compare/agents-md-vs-claude-md.md`
- Create: `faq/claude-code-session-memory-management.md`
- Create: `blog/claude-code-macos-companion-tools.md`
- Create: `blog/claude-code-agent-loop-architecture.md`
- Refresh: hooks guide — add security considerations section (settings.json backdoor vector)
- Refresh: `blog/claude-code-memory.md` — add third-party memory orchestration (Orb, Memory-forge-rs)
- Refresh: `faq/claude-code-plugin-json-manifest.md` — add Xcode/SwiftUI plugin as real-world example
- Refresh: `faq/claude-code-skills.md` — add evolutionary naming, web-design spec-first, Seedance as concrete examples