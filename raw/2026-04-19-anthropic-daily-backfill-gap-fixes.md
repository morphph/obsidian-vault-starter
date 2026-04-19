# Anthropic + Claude Daily-Fetch Backfill — Gap Fixes (2026-04-19)

Continuation run filling three gaps identified in the initial 2026-04-18 backfill.

## Fix 1 — claude.com/blog pagination (Playwright)

**Finding:** Blog has sparse Jan-Feb 2026 content. Full 2026-01-01..2026-04-18 list contains only **16 posts** (not 50+ as feared). The blog's Webflow pagination uses `?<token>_page=N` query params; content between posts skips from **2026-03-12 → 2025-12-09** (nothing in Jan-Feb 2026).

**Missing from initial backfill (1 post):**
- 2026-03-12 — "Claude now creates interactive charts, diagrams and visualizations" — /blog/claude-builds-visuals

All other 15 posts already captured in initial run.

## Fix 2 — platform.claude.com/docs/en/claude-code (Playwright)

**Finding:** Canonical URL moved. `platform.claude.com/docs/en/claude-code` now redirects to **`code.claude.com/docs`**. The new page is a rich overview with install configurator, "What you can do" accordion (8 sections), surface comparison table.

**Key snapshot takeaways (2026-04-19):**
- Claude Code positioned as "agentic coding tool — terminal, IDE, desktop app, browser"
- 6 install surfaces: Terminal, VS Code, JetBrains, Desktop app, Web, + mentioned Cursor
- Package managers: Homebrew (`claude-code` stable vs `claude-code@latest`), WinGet
- Native Windows requires Git for Windows
- Features called out: Automate tedious tasks, Build features/fix bugs, Commits/PRs, MCP, CLAUDE.md + auto memory + Skills + Hooks, Agent teams + Agent SDK, Pipe/script CLI, **Routines** (Anthropic-managed cron), Desktop scheduled tasks, `/loop`, Remote Control, Dispatch, `/teleport`, `/desktop`, Slack `@Claude`
- Web: claude.ai/code

**Implication for source list:** Replace `platform.claude.com/docs/en/claude-code` with `code.claude.com/docs` as the canonical Claude Code docs URL. Requires Playwright (JS-rendered SPA).

## Fix 3 — Claude Code dated releases (gh CLI)

**Finding:** atom feed only returns latest 10 entries. Used `gh api repos/anthropics/claude-code/releases?per_page=100` instead. All 88 in-window releases dated.

**Full dated release list (v2.0.76 → v2.1.114), 2026-01-01 → 2026-04-18:**

| Version | Date (UTC) |
|---|---|
| v2.1.114 | 2026-04-18 |
| v2.1.113 | 2026-04-17 |
| v2.1.112 | 2026-04-16 |
| v2.1.111 | 2026-04-16 |
| v2.1.110 | 2026-04-15 |
| v2.1.109 | 2026-04-15 |
| v2.1.108 | 2026-04-14 |
| v2.1.107 | 2026-04-14 |
| v2.1.105 | 2026-04-13 |
| v2.1.104 | 2026-04-13 |
| v2.1.101 | 2026-04-10 |
| v2.1.100 | 2026-04-10 |
| v2.1.98  | 2026-04-09 |
| v2.1.97  | 2026-04-08 |
| v2.1.96  | 2026-04-08 |
| v2.1.94  | 2026-04-07 |
| v2.1.92  | 2026-04-04 |
| v2.1.91  | 2026-04-02 |
| v2.1.90  | 2026-04-01 |
| v2.1.89  | 2026-04-01 |
| v2.1.87  | 2026-03-29 |
| v2.1.86  | 2026-03-27 |
| v2.1.85  | 2026-03-26 |
| v2.1.84  | 2026-03-26 |
| v2.1.83  | 2026-03-25 |
| v2.1.81  | 2026-03-20 |
| v2.1.80  | 2026-03-19 |
| v2.1.79  | 2026-03-18 |
| v2.1.78  | 2026-03-17 |
| v2.1.77  | 2026-03-17 |
| v2.1.76  | 2026-03-14 |
| v2.1.75  | 2026-03-13 |
| v2.1.74  | 2026-03-12 |
| v2.1.73  | 2026-03-11 |
| v2.1.72  | 2026-03-10 |
| v2.1.71  | 2026-03-07 |
| v2.1.70  | 2026-03-06 |
| v2.1.69  | 2026-03-05 |
| v2.1.68  | 2026-03-04 |
| v2.1.66  | 2026-03-04 |
| v2.1.63  | 2026-02-28 |
| v2.1.62  | 2026-02-27 |
| v2.1.61  | 2026-02-26 |
| v2.1.59  | 2026-02-26 |
| v2.1.58  | 2026-02-25 |
| v2.1.56  | 2026-02-25 |
| v2.1.55  | 2026-02-25 |
| v2.1.53  | 2026-02-25 |
| v2.1.52  | 2026-02-24 |
| v2.1.51  | 2026-02-24 |
| v2.1.50  | 2026-02-20 |
| v2.1.49  | 2026-02-19 |
| v2.1.47  | 2026-02-18 |
| v2.1.45  | 2026-02-17 |
| v2.1.44  | 2026-02-16 |
| v2.1.42  | 2026-02-13 |
| v2.1.41  | 2026-02-13 |
| v2.1.39  | 2026-02-10 |
| v2.1.38  | 2026-02-10 |
| v2.1.37  | 2026-02-07 |
| v2.1.36  | 2026-02-07 |
| v2.1.34  | 2026-02-06 |
| v2.1.33  | 2026-02-06 |
| v2.1.32  | 2026-02-05 |
| v2.1.31  | 2026-02-04 |
| v2.1.30  | 2026-02-03 |
| v2.1.29  | 2026-01-31 |
| v2.1.27  | 2026-01-30 |
| v2.1.25  | 2026-01-29 |
| v2.1.23  | 2026-01-29 |
| v2.1.22  | 2026-01-28 |
| v2.1.21  | 2026-01-28 |
| v2.1.20  | 2026-01-27 |
| v2.1.19  | 2026-01-23 |
| v2.1.17  | 2026-01-22 |
| v2.1.16  | 2026-01-22 |
| v2.1.15  | 2026-01-21 |
| v2.1.14  | 2026-01-20 |
| v2.1.12  | 2026-01-17 |
| v2.1.11  | 2026-01-17 |
| v2.1.9   | 2026-01-16 |
| v2.1.7   | 2026-01-14 |
| v2.1.6   | 2026-01-13 |
| v2.1.5   | 2026-01-12 |
| v2.1.4   | 2026-01-11 |
| v2.1.3   | 2026-01-09 |
| v2.1.2   | 2026-01-09 |
| v2.1.1   | 2026-01-07 |
| v2.0.76  | 2026-01-07 |

**88 releases in window.** Versions with gaps in numbering are expected (internal/canary builds).

## Summary
All three gaps resolved. Backfill for Option B is now **legitimately complete**:
- Websites: all covered
- RSS + gh-api dated releases: complete
- X handles: still intentionally skipped (Option B scope)
