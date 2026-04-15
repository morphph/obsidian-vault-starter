---
type: concept
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
tags: [wiki, security, agentic, tool]
---

# Claude Code Sandboxing

## Summary
[[Anthropic]]'s native sandboxing for [[claude-code|Claude Code]] — OS-level filesystem and network isolation using Seatbelt (macOS) and bubblewrap (Linux). Reduces permission prompts by 84% while maintaining security. The critical safety foundation for running autonomous [[ralph-wiggum|Ralph]] loops AFK. Open-sourced as `@anthropic-ai/sandbox-runtime`.

## Details
- **Core principle**: Effective sandboxing requires **both** filesystem and network isolation. Either alone is insufficient.
- **Filesystem isolation**: 
  - Default: read/write to current working directory only
  - Read access to full system (except denied dirs)
  - Configurable via `sandbox.filesystem.allowWrite`, `denyWrite`, `denyRead`, `allowRead`
  - OS-level enforcement applies to all child processes (kubectl, terraform, npm, etc.)
- **Network isolation**:
  - Unix domain socket → proxy server outside sandbox
  - Only approved domains accessible
  - New domain requests trigger permission prompts
  - `allowManagedDomainsOnly` blocks non-allowed domains automatically
- **Two sandbox modes**:
  - **Auto-allow**: sandboxed commands auto-approved, non-sandboxable fall back to permission flow. Best for autonomous/AFK coding.
  - **Regular permissions**: all commands go through standard permission flow. More control, more interruptions.
- **Setup**:
  - macOS: works out of the box
  - Linux/WSL2: `sudo apt-get install bubblewrap socat`
  - Enable: `/sandbox` command
- **Security benefits**:
  - Protection against prompt injection (can't modify `~/.bashrc`, can't exfiltrate data)
  - Reduced attack surface from malicious dependencies, compromised scripts
  - All boundary violations blocked at OS level with immediate notifications
- **Security limitations**:
  - Domain-level filtering only (no traffic inspection)
  - Broad domains like `github.com` could enable exfiltration
  - Domain fronting possible
  - `allowUnixSockets` can expose Docker socket
  - `enableWeakerNestedSandbox` considerably weakens security
- **Escape hatch**: `dangerouslyDisableSandbox` parameter (goes through normal permissions). Disable with `"allowUnsandboxedCommands": false`.
- **Open source**: `npx @anthropic-ai/sandbox-runtime <command>` — can sandbox any program, not just Claude Code
- **Docker sandboxes** (`docker sandbox run claude`): Maximum isolation for AFK Ralph. Mounts only the project directory. Auto-injects Git config. Persistent state across runs. Requires Docker Desktop 4.50+.
- **Relationship to Ralph**: With `--dangerously-skip-permissions` or `--permission-mode acceptEdits`, the sandbox becomes the **only security boundary**. Essential for overnight/AFK loops.

## Connections
- Related: [[claude-code]], [[ralph-wiggum]], [[permission-system]], [[anthropic]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-anthropic-claude-code-sandboxing.md | Initial creation — engineering blog + official docs |
