# Vault Context

## Owner
This vault belongs to vfan — a full-time builder based in Singapore.
Growth marketer at a B2B LLM API company by day, independent AI content builder by night.
Works comfortably in both English and Chinese. Prefers concise, action-oriented communication.

## Projects (detailed context in /projects/)
- [[LoreAI]] — Bilingual AI developer content platform (loreai.dev)
- [[blog2video]] — English tech blogs → Chinese narrated videos for Xiaohongshu/WeChat, brand "AI精读"

## Vault Structure
- `/daily/` — Daily build logs. Human-written only. Contains both build notes and ideas (tagged #idea).
- `/projects/` — Project context files. Each has an AUTO-SYNCED section (from repo) and a HUMAN section (strategic thinking). Human section is never overwritten by agent.
- `/ideas/` — Ideas that "graduated" from daily build logs via /graduate command. Each is a standalone note worth developing.
- `/references/` — Tool notes, strategy research, people notes, external resources. Agent-assisted content is allowed here but must be tagged with `source: agent`.
- `/agent-output/` — Agent-generated reports, analyses, suggestions. Staging area for human review. Nothing here is part of the "real" vault.
- `COMMANDS.md` — Command cheatsheet with usage scenarios.

## Human-Machine Separation Rules
1. `/daily/`, `/ideas/`, and the HUMAN sections of `/projects/` files are **human-only**. Agent reads but NEVER writes here (exception: /log and /graduate which are interactive and human-approved).
2. `/agent-output/` is where all agent-generated content goes. Reports, ideas analysis, connection maps — all written here.
3. `/references/` allows agent-assisted content but tag it with `source: agent` in frontmatter.
4. When I say "write this down" or "save this" without specifying where, ask me where it should go.

## Linking Conventions
- Always link project names: [[LoreAI]], [[blog2video]]
- Link people: [[Person Name]]
- Link MY concepts and theories, NOT generic terms:
  - ✅ [[AEO as distribution strategy]], [[bilingual content arbitrage]], [[owning subscribers vs renting SEO traffic]]
  - ❌ [[AI]], [[marketing]], [[content]], [[Python]]
- Unresolved links are fine — they'll become notes later
- Don't link generic tech terms. Only link things that might appear across multiple notes.

## Daily Build Log Format
Each daily note in /daily/ uses this loose structure:
```
# YYYY-MM-DD

## Build Log
- what I worked on (with [[project links]])
- what surprised me
- what's stuck (#blocker)
- #idea tagged thoughts
- #learning tagged discoveries

## Tomorrow
- what I plan to work on next
```

## Session Management Rules
- When user runs /ideas, /emerge, or /connect: check if the current session already has significant conversation history. If so, suggest starting a fresh session for better output quality.
- When writing to daily/ via /log: after writing, automatically scan the new content and suggest [[wiki links]] for mentioned projects, people, and concepts. Show suggestions before applying.

## Repo Locations (for /sync-project)
- loreai: ~/Desktop/Project/loreai-v2
- blog2video: ~/Desktop/Project/blog2video

## My Preferences
- I don't enjoy journaling. I enjoy building. Build logs, not diaries.
- Chinese-English mixing is normal. Don't standardize.
- I care about cross-project patterns more than single-project details.
- When suggesting ideas, make them actionable — tools to build, experiments to run.
- Keep output concise. I can always ask for more detail.
