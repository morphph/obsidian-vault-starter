---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-deep-links.md
tags: [claude-code, official-docs, deep-links, url-scheme, runbook, integration]
---

# Source: Launch sessions from links (deep links)

## Summary
Official Anthropic doc on **`claude-cli://` deep links** in [[claude-code]] — a custom URL scheme that opens Claude Code in a new terminal window with a pre-filled prompt + working directory. Embed in runbooks, alerts, dashboards, README, CI failure notifications. Click → terminal opens → prompt populated (**not sent until Enter**). Requires v2.1.91+. **The "one-click-into-Claude" primitive** — closes a UX gap for ops teams who page on-call into a session.

## Anatomy of a deep link

Every link starts with `claude-cli://open` — the **only path the handler accepts**.

Parameters:

| Parameter | Description |
| :--- | :--- |
| `q` | URL-encoded prompt text to pre-fill. `%0A` for newlines. **Max 5,000 chars.** |
| `cwd` | Absolute path for working directory. Network/UNC paths rejected. |
| `repo` | GitHub `owner/name` slug → resolves to local clone Claude Code has seen before |

If both `cwd` + `repo` passed: **`cwd` takes precedence**, `repo` ignored.

Example:
```text
claude-cli://open?repo=acme/payments&q=Investigate%20the%20failed%20deploy.%0ACheck%20recent%20commits.
```

## `repo` lookup mechanism (smart but local-only)

- Each `claude` invocation in a git repo records that directory's path against the repo's `owner/name` slug
- Deep link with `repo=...` opens **most recently used** matching path
- Multiple clones/worktrees tracked separately
- Lookup ONLY finds paths where Claude Code has run at least once
- If no match → opens in home directory

Launched session shows which path it picked + when that clone last fetched — so you can tell if looking at stale code.

## What launches when you click

1. Browser/app hands URL to OS
2. OS recognizes `claude-cli://` prefix, starts Claude Code
3. New terminal window opens with Claude Code running in chosen directory, prompt in input box
4. **Banner above input shows external link launched + which directory** (for prompts >1,000 chars: "scroll and review")
5. You read prompt, edit if wanted, press Enter to send

Deep link **never executes anything on its own** — only chooses directory and fills prompt box. Permission rules, CLAUDE.md, trust prompts apply the same as any other session.

## Embed in a runbook

```markdown
## High 5xx rate on web-gateway

1. Acknowledge the page in PagerDuty.
2. [Open Claude Code in the gateway repo](claude-cli://open?repo=acme/web-gateway&q=5xx%20rate%20is%20elevated...%20Check%20recent%20deploys%2C%20error%20logs%2C%20open%20incidents.)
3. Post initial findings in #incident.
```

> [!warning]
> **GitHub-rendered Markdown does NOT allow `claude-cli://`** — strips the scheme in READMEs, issues, PRs, wikis. Link text shows but no clickable link. Workaround: put deep link in code block so readers can paste into address bar.

## Open from shell scripts

```bash
# macOS
open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"

# Linux
xdg-open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"

# Windows PowerShell
Start-Process "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"

# Windows cmd.exe (empty title arg needed before URL)
start "" "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"
```

## OS handler registration (auto, user-level only)

Claude Code registers the handler **first time you start an interactive session** on macOS/Linux/Windows — no separate install command.

| Platform | Handler location |
| :--- | :--- |
| macOS | `~/Applications/Claude Code URL Handler.app` |
| Linux | `claude-code-url-handler.desktop` under `$XDG_DATA_HOME/applications` |
| Windows | `HKEY_CURRENT_USER\Software\Classes\claude-cli` |

Terminal emulator detection:
- **macOS**: remembers from most recent interactive session — iTerm2, Ghostty, kitty, Alacritty, WezTerm, Terminal.app
- **Linux**: `$TERMINAL` → `x-terminal-emulator` → common emulators
- **Windows**: Windows Terminal → PowerShell → cmd.exe

To prevent registration entirely: `disableDeepLinkRegistration: "disable"` in `settings.json`. Enforce via managed settings.

## VS Code variant

VS Code extension registers `vscode://anthropic.claude-code/open` handler — opens Claude Code editor tab rather than terminal window.

## Concrete use patterns

- Incident runbook step that opens affected service's repo with diagnostic prompt
- Monitoring alert / dashboard linking to investigation prompt
- README/wiki page that opens project with onboarding prompt
- CI failure notification that pre-fills failing job's name

## Connection to our wiki — runbook-style ingest URLs

We could embed `claude-cli://` links in our own wiki pages — e.g., on `digest-anthropic-*.md` pages, link to "open Claude Code in this vault with /ingest-anthropic-daily preloaded." Worth exploring as part of the synthesis page.

## Connections
- Related: [[claude-code]], [[source-claude-code-programmatic-usage-docs]], [[source-claude-code-channels-docs]], [[agent-skills-standard]]
- Pairs with [[source-claude-code-programmatic-usage-docs]] and [[source-claude-code-channels-docs]] as the **three external entry points to a session**: deep link (UI click), `-p` (CLI invocation), channels (event push)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-deep-links.md | Initial creation — new primitive, no prior wiki coverage |
