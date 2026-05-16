# Claude Code Official Docs — Launch sessions from links

Captured 2026-05-14 from https://code.claude.com/docs/en/deep-links.md

> Open a Claude Code terminal session from a URL. Embed `claude-cli://` links in runbooks, alerts, and dashboards so a click opens Claude Code in the right repo with the right prompt.

A deep link is a `claude-cli://` URL that opens Claude Code in a new terminal window. The URL can carry a working directory and a prompt to pre-fill.

This lets you share a one-click starting point for a task. The prompt is populated but not sent until you press Enter.

Where to use:
* Incident runbook step that opens affected service's repo with diagnostic prompt
* Monitoring alert / dashboard that links to investigation prompt
* README or wiki page that opens project with onboarding prompt
* CI failure notification with failing job's name

> [!note]
> Deep links require Claude Code v2.1.91 or later.

## How it works

`claude-cli://` is custom URL scheme that Claude Code registers with OS. When you click:
1. Browser/app hands URL to OS
2. OS recognizes `claude-cli://` prefix, starts Claude Code
3. New terminal window opens with Claude Code running in directory link specified, prompt text in input box
4. You read prompt, edit if wanted, press Enter

Link itself can be hosted anywhere, but session always opens locally on machine where you clicked.

> [!note]
> Platform displaying link must allow custom URL schemes. GitHub-rendered Markdown allows `http`/`https` but strips schemes like `claude-cli://` in READMEs, issues, PRs, wikis.

### What a launched session shows

Deep link never executes anything on its own. Link only chooses directory and fills prompt box. If you click link from untrusted page, prompt is still inert until you read it and press Enter.

When session opens, banner above input shows external link launched it and which directory it selected. For prompts over 1,000 characters, banner tells you to scroll and review. Permission rules, `CLAUDE.md`, trust prompts apply same as any other session.

## Build a link

Every deep link starts with `claude-cli://open`, only path handler accepts:

```text
claude-cli://open
```

Parameters:

| Parameter | Description |
| --- | --- |
| `q` | Text to pre-fill in prompt box. URL-encode the value. Use `%0A` for line breaks. Max 5,000 chars. |
| `cwd` | Absolute path for working directory. Network and UNC paths rejected. |
| `repo` | A GitHub `owner/name` slug. Claude Code resolves to local clone it has seen before. If no matching clone, opens in home directory. |

`cwd` and `repo` are two ways to set working directory. If you pass both, `cwd` takes precedence.

```text
claude-cli://open?repo=acme/payments&q=Investigate%20the%20failed%20deploy%20of%20payments-api.%0ACheck%20recent%20commits%20to%20main%20and%20the%20last%20successful%20build.
```

Decoded prompt:
```text
Investigate the failed deploy of payments-api.
Check recent commits to main and the last successful build.
```

### Choose between `cwd` and `repo`

Use `cwd` when everyone clicking link has project at same absolute path (devcontainer, VM image).

Use `repo` when link is shared and each person clones to different location. Resolution:
* Each time you run `claude` in a Git repo, that directory's path is recorded against the repo's `owner/name` slug
* `repo` opens whichever matching path you used most recently
* Multiple clones/worktrees tracked separately
* Lookup only finds paths where Claude Code has run at least once

Launched session shows which path it picked and when that clone last fetched from remote.

## Examples

### Embed a link in a runbook

```markdown
## High 5xx rate on web-gateway

1. Acknowledge the page in PagerDuty.
2. [Open Claude Code in the gateway repo](claude-cli://open?repo=acme/web-gateway&q=5xx%20rate%20is%20elevated%20on%20web-gateway.%20Check%20recent%20deploys%2C%20error%20logs%20from%20the%20last%2030%20minutes%2C%20and%20open%20incidents%20in%20Linear.)
3. Post initial findings in #incident.
```

### Open a link from the shell

macOS:
```bash
open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"
```

Linux:
```bash
xdg-open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"
```

Windows PowerShell:
```powershell
Start-Process "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"
```

Windows cmd.exe:
```cmd
start "" "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"
```

## Registration and supported platforms

Claude Code registers the `claude-cli://` handler with OS first time you start interactive session.

| Platform | Handler location |
| --- | --- |
| macOS | `~/Applications/Claude Code URL Handler.app` |
| Linux | `claude-code-url-handler.desktop` under `$XDG_DATA_HOME/applications` |
| Windows | `HKEY_CURRENT_USER\Software\Classes\claude-cli` |

Terminal emulator detection:
* **macOS**: remembers terminal from most recent interactive session (iTerm2, Ghostty, kitty, Alacritty, WezTerm, Terminal.app)
* **Linux**: honors `$TERMINAL`, then `x-terminal-emulator`, then common emulators
* **Windows**: Windows Terminal → PowerShell → cmd.exe

To prevent registration: set `disableDeepLinkRegistration: "disable"` in `settings.json`. Enforce via managed settings.

## Open a VS Code tab instead of a terminal

VS Code extension registers `vscode://anthropic.claude-code/open` handler.

## Troubleshooting

* **Clicking does nothing**: handler not registered. Start interactive `claude` session once.
* **Link renders as plain text**: GitHub strips `claude-cli://`. Put in code block.
* **Opens in home dir instead of repo**: `repo` only resolves to clones Claude Code has seen. Run `claude` inside clone once.
* **Wrong terminal**: macOS — start `claude` in preferred terminal once. Linux — set `$TERMINAL`. Windows — order is fixed.

## Learn more

* Skills: store long runbook prompt as `/skill` so `q` parameter only names it
* Non-interactive mode: run Claude from script
