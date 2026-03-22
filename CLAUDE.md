# Vault Context

## Owner
This vault belongs to vfan — a full-time builder based in Singapore.
Growth marketer at a B2B LLM API company by day, independent AI content builder by night.
Works comfortably in both English and Chinese. Prefers concise, action-oriented communication.

## Projects (detailed context in /projects/)
- [[LoreAI]] — Bilingual AI developer content platform (loreai.dev)
- [[blog2video]] — English tech blogs → Chinese narrated videos for Xiaohongshu/WeChat, brand "AI精读"

## Vault Structure
- `inbox.md` — **Primary capture point.** Append-only file for building logs and learning notes. Written by `/build-log` (Claude Code) and OpenClaw Telegram bot.
- `/projects/` — Project context files. Each has an AUTO-SYNCED section (from repo) and a HUMAN section (strategic thinking). Human section is never overwritten by agent.
- `/references/` — Tool notes, strategy research, people notes, external resources. Agent-assisted content is allowed here but must be tagged with `source: agent`.
- `/building-journal/` — Polished, ready-to-publish content (口播稿, scripts, articles). Use `status: ready/published` in frontmatter.
- `/agent-output/` — Agent-generated reports, analyses, suggestions. Staging area for human review. Nothing here is part of the "real" vault.
- `/loreai/` — LoreAI pipeline architecture docs and canvas visualizations.
- `/archive/` — Archived folders and commands from the previous vault design.

## Capture System
Two capture paths feed into `inbox.md`:
1. **`/build-log`** — Global Claude Code command. Works from any project. Captures building learnings mid-session or auto-summarizes at session end.
2. **OpenClaw Telegram bot** — Summarizes articles/videos in Chinese. Saves to inbox.md when user says "保存".

## Human-Machine Separation Rules
1. The HUMAN sections of `/projects/` files are **human-only**. Agent reads but NEVER writes here.
2. `/agent-output/` is where all agent-generated content goes. Reports, ideas analysis, connection maps — all written here.
3. `/references/` allows agent-assisted content but tag it with `source: agent` in frontmatter.
4. `inbox.md` is shared — both human and agent can append, but NEVER delete or modify existing entries.
5. When I say "write this down" or "save this" without specifying where, ask me where it should go.

## Linking Conventions
- Always link project names: [[LoreAI]], [[blog2video]]
- Link people: [[Person Name]]
- Link MY concepts and theories, NOT generic terms:
  - ✅ [[AEO as distribution strategy]], [[bilingual content arbitrage]], [[owning subscribers vs renting SEO traffic]]
  - ❌ [[AI]], [[marketing]], [[content]], [[Python]]
- Unresolved links are fine — they'll become notes later
- Don't link generic tech terms. Only link things that might appear across multiple notes.

## Repo Locations (for /sync-project)
- loreai: ~/Desktop/Project/loreai-v2
- blog2video: ~/Desktop/Project/blog2video

## My Preferences
- I don't enjoy journaling. I enjoy building. Build logs, not diaries.
- Chinese-English mixing is normal. Don't standardize.
- I care about cross-project patterns more than single-project details.
- When suggesting ideas, make them actionable — tools to build, experiments to run.
- Keep output concise. I can always ask for more detail.
