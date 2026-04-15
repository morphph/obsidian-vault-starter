# Claude Code Sandboxing — Anthropic Official

**Source:** https://www.anthropic.com/engineering/claude-code-sandboxing + https://code.claude.com/docs/en/sandboxing
**Author:** Anthropic
**Fetch method:** WebFetch
**Date fetched:** 2026-04-15

---

## Overview

Claude Code features native sandboxing to provide a more secure environment for agent execution while reducing the need for constant permission prompts. Instead of asking permission for each bash command, sandboxing creates defined boundaries where Claude Code can work more freely with reduced risk.

## Why Sandboxing Matters

Traditional permission-based security leads to:
- **Approval fatigue**: Repeatedly clicking "approve" causes users to pay less attention
- **Reduced productivity**: Constant interruptions slow workflows
- **Limited autonomy**: Agent can't work efficiently when waiting for approvals

Internal result: **sandboxing safely reduces permission prompts by 84%**.

## Core Architecture

### Filesystem Isolation
- Default: read/write to current working directory and subdirectories
- Read access to entire computer (except denied directories)
- Cannot modify files outside working directory without explicit permission
- Configurable via `sandbox.filesystem.allowWrite`
- OS-level enforcement: Seatbelt (macOS), bubblewrap (Linux/WSL2)

### Network Isolation
- Domain restrictions: only approved domains accessible
- Unix domain socket → proxy server outside sandbox enforces rules
- New domain requests trigger permission prompts
- `allowManagedDomainsOnly` blocks non-allowed domains automatically

**Critical principle**: "Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys; without filesystem isolation, a compromised agent could backdoor system resources."

## Sandbox Modes

**Auto-allow mode**: Sandboxed commands auto-approved. Non-sandboxable commands fall back to regular permission flow. Best for autonomous/AFK operation.

**Regular permissions mode**: All commands go through standard permission flow even when sandboxed. More control, more approvals.

## Setup

### Prerequisites
- macOS: works out of the box (Seatbelt)
- Linux/WSL2: `sudo apt-get install bubblewrap socat`
- WSL1: not supported

### Enable
```
/sandbox
```

### Configuration (settings.json)
```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": ["~/.kube", "/tmp/build"],
      "denyWrite": ["~/.ssh"],
      "denyRead": ["~/"],
      "allowRead": ["."]
    }
  }
}
```

## Security Benefits

### Protection Against Prompt Injection
Even if attacker manipulates Claude's behavior:
- Cannot modify `~/.bashrc`, `/bin/` etc.
- Cannot exfiltrate data to attacker-controlled servers
- Cannot download malicious scripts from unauthorized domains
- All access attempts blocked at OS level with immediate notifications

### Reduced Attack Surface
Limits damage from: malicious dependencies, compromised scripts, social engineering, prompt injection.

## Escape Hatch
When commands fail due to sandbox restrictions, Claude can retry with `dangerouslyDisableSandbox` parameter (goes through normal permission flow). Disable with `"allowUnsandboxedCommands": false`.

## Security Limitations
- Network filtering operates at domain level, does not inspect traffic
- Broad domains like `github.com` could enable data exfiltration
- Domain fronting may bypass filtering
- `allowUnixSockets` can grant access to powerful services (e.g., Docker socket)
- Overly broad filesystem write permissions enable privilege escalation
- Linux `enableWeakerNestedSandbox` considerably weakens security

## Open Source

The sandbox runtime is available as open source:
```bash
npx @anthropic-ai/sandbox-runtime <command-to-sandbox>
```

Can sandbox any program, not just Claude Code. E.g., sandbox an MCP server.

## Relationship to Permissions
- **Permissions**: control which tools Claude can use (evaluated before tool runs)
- **Sandboxing**: OS-level enforcement restricting what Bash commands can access
- Both are complementary security layers that work together
- Filesystem restrictions from both systems are merged

## Best Practices
1. Start restrictive, expand as needed
2. Monitor sandbox violation attempts
3. Use environment-specific configs
4. Combine with permissions for defense-in-depth
5. Test configurations before relying on them

## Relevance to Ralph Wiggum / AFK Coding
Sandboxing is the security foundation for running autonomous coding loops. With `--dangerously-skip-permissions` or `--permission-mode acceptEdits`, the sandbox becomes the **only security boundary**. Essential for overnight/AFK Ralph loops. Docker sandboxes (`docker sandbox run claude`) provide the most isolation — mount only the project directory.
