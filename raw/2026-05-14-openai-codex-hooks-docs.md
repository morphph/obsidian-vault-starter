# OpenAI Codex Hooks (Documentation)

**Source:** https://developers.openai.com/codex/hooks
**Publisher:** OpenAI Developers (official docs)
**GA date:** 2026-05-14 (per Codex changelog)
**Fetch date:** 2026-05-20
**Fetch method:** WebFetch

---

## Overview

Codex's hooks framework injects custom scripts into the agentic lifecycle. Capabilities include custom logging, prompt security scanning, automatic memory creation, validation checks, and context-aware prompting.

## Configuration locations (precedence)

- `~/.codex/hooks.json` (user level)
- `~/.codex/config.toml` (user level)
- `<repo>/.codex/hooks.json` (project level)
- `<repo>/.codex/config.toml` (project level)
- Plugin-bundled hooks (opt-in via `[features].plugin_hooks = true`)
- Enterprise `requirements.toml` (managed, enforced)

Per docs: "Higher-precedence config layers don't replace lower-precedence hooks." Multiple matching sources all execute.

## Six lifecycle events

1. **SessionStart** — session init. Matcher filters: `startup | resume | clear`.
2. **PreToolUse** — before Bash, `apply_patch`, file edits, MCP tools.
3. **PermissionRequest** — when approval is required for privileged operation.
4. **PostToolUse** — after tool execution completes.
5. **UserPromptSubmit** — before user input is processed.
6. **Stop** — when a conversation turn ends.

## Hook structure (JSON)

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "regex_pattern_or_*",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/script.py",
            "statusMessage": "optional",
            "timeout": 600
          }
        ]
      }
    ]
  }
}
```

## Matcher rules

- **PreToolUse / PostToolUse / PermissionRequest** match tool names: `Bash`, `apply_patch`, MCP tool names like `mcp__filesystem__.*`
- **SessionStart** matches start source: `startup | resume | clear`
- **UserPromptSubmit / Stop** ignore matchers (use `"*"`, `""`, or omit)

## stdin / stdout contract

stdin JSON contains shared fields:
- `session_id`, `transcript_path`, `cwd`, `hook_event_name`, `model`, `turn_id`, `permission_mode`
- Turn-specific events also get `tool_name`, `tool_input`, `tool_response`

Exit codes:
- **Exit 0** = success, Codex continues
- **Exit 2** = blocking decision; reason written to stderr (fed back to agent as feedback)

JSON stdout:

```json
{
  "continue": true,
  "stopReason": "optional reason",
  "systemMessage": "warning text",
  "suppressOutput": false
}
```

## Event-specific outputs

### PreToolUse
- Deny: `"permissionDecision": "deny"`
- Allow with rewrite: `"permissionDecision": "allow"` + `"updatedInput"`
- Add context: `"additionalContext"`

### PermissionRequest
- `"behavior": "allow"` → skip approval
- `"behavior": "deny"` with optional message
- Decline → normal flow proceeds

### PostToolUse
- Cannot undo side effects but can `"decision": "block"`, replace output, add dev context

### Stop
- Can force continuation via `"decision": "block"` to trigger auto-continuation with new prompt

## Permissions and trust model

Non-managed hooks (user / project / plugin) require trust review via `/hooks` command before execution. Project-local hooks load only when `.codex/` is trusted.

Managed hooks from `requirements.toml` or MDM are trusted by policy and cannot be disabled. Enforce enterprise-wide:

```toml
[features]
hooks = true

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
```

## Constraints

- Default timeout 600s; customize per hook
- `async: true` parsed but unsupported (skipped)
- Only `type: "command"` runs today; `prompt` and `agent` types reserved
- Multiple matching command hooks launch concurrently — one cannot block another
- Project-local hooks load only when `.codex/` is trusted

---

## Direct comparison with Claude Code Hooks (researcher note)

| Dimension | Codex (2026-05-14 GA) | Claude Code |
|---|---|---|
| Lifecycle events | 6: SessionStart / PreToolUse / PermissionRequest / PostToolUse / UserPromptSubmit / Stop | Similar set: PreToolUse / PostToolUse / Stop / SessionEnd / PreCompact / UserPromptSubmit |
| Block mechanism | exit 2 → stderr fed back | exit 2 → stderr fed back |
| Config | `hooks.json` or `[hooks]` in `config.toml`, user / project / plugin / enterprise layers | `settings.json`, user / project / plugin layers |
| Managed/enforced | Yes (enterprise `requirements.toml`) | Yes (admin policy) |
| Permission decisions via hook | Yes (PreToolUse + PermissionRequest can allow/deny with JSON) | Yes (deny/allow via JSON) |

**Conclusion:** Codex Hooks at 2026-05-14 GA is at functional parity with Claude Code hooks. The "Anthropic stack thicker" claim made in earlier writing is outdated post-2026-05-14.
