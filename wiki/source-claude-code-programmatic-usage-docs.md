---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-programmatic-usage.md
tags: [claude-code, official-docs, headless, agent-sdk, ci-cd, scripting]
---

# Source: Run Claude Code programmatically (headless mode)

## Summary
Official Anthropic doc on **non-interactive Claude Code via `claude -p`** — same harness, agent loop, context management, but driven by CLI flags instead of TUI. Available as CLI for scripts/CI/CD, or as [Python](https://code.claude.com/docs/en/agent-sdk/python)/[TypeScript](https://code.claude.com/docs/en/agent-sdk/typescript) Agent SDK packages. **Starting June 15, 2026: subscription plans get a separate monthly Agent SDK credit** (not from interactive usage limits).

## `claude -p` basics

```bash
claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"
```

All [CLI options](/en/cli-reference) work with `-p`:
- `--continue` for continuing conversations
- `--allowedTools` for auto-approving tools
- `--output-format` for structured output

## `--bare` mode — the CI default

```bash
claude --bare -p "Summarize this file" --allowedTools "Read"
```

Skips auto-discovery of: hooks, skills, plugins, MCP servers, auto memory, CLAUDE.md.

**Without `--bare`, `-p` loads the same context an interactive session would.** A hook in a teammate's `~/.claude` or an MCP server in `.mcp.json` will run. With `--bare`, only flags you pass explicitly take effect.

> [!note]
> `--bare` is the recommended mode for scripted/SDK calls, **will become the default for `-p` in a future release**.

Bare mode skips OAuth and keychain reads. Anthropic auth must come from `ANTHROPIC_API_KEY` or `apiKeyHelper` in `--settings`.

Pass context explicitly:

| Load | Use |
| :--- | :--- |
| System prompt additions | `--append-system-prompt`, `--append-system-prompt-file` |
| Settings | `--settings <file-or-json>` |
| MCP servers | `--mcp-config <file-or-json>` |
| Custom agents | `--agents <json>` |
| A plugin | `--plugin-dir <path>`, `--plugin-url <url>` |

## Pipe data through Claude (Unix-style)

```bash
cat build-error.txt | claude -p 'explain root cause' > output.txt
```

> [!note]
> Piped stdin capped at 10MB as of v2.1.128. For larger inputs, write to file and reference path in prompt.

With `--output-format json`, payload includes `total_cost_usd` + per-model cost breakdown — scripted callers can track spend per invocation without consulting usage dashboard.

## Structured output

| Format | What it gives you |
| :--- | :--- |
| `text` (default) | Plain text |
| `json` | result + session_id + metadata |
| `stream-json` | Newline-delimited JSON for streaming |

Schema-constrained:
```bash
claude -p "Extract function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}'
```

Result in `structured_output` field.

## Streaming events

```bash
claude -p "Explain recursion" --output-format stream-json --verbose --include-partial-messages
```

Each line is a JSON object. Filter text deltas with jq:
```bash
| jq -rj 'select(.type == "stream_event" and .event.delta.type? == "text_delta") | .event.delta.text'
```

Notable system events:
- `system/init` — session metadata (model, tools, MCP, plugins). First event unless `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` set
- `system/plugin_install` — emitted during marketplace plugin install (started/installed/failed/completed)
- `system/api_retry` — emitted before retry (attempt, max_retries, retry_delay_ms, error_status, error category)

Plugin error reporting in `system/init`: `plugins` (loaded successfully) + `plugin_errors` (load failures, dependency mismatches). Use `plugin_errors` to fail CI when a required plugin didn't load.

## Auto-approve tools

```bash
claude -p "Run the test suite and fix any failures" \
  --allowedTools "Bash,Read,Edit"
```

Or a permission mode for the whole session:
- `dontAsk` — denies anything not in `permissions.allow` rules or read-only command set. **For locked-down CI.**
- `acceptEdits` — auto-approves writes + common filesystem commands (mkdir, touch, mv, cp). Other shell + network still need explicit allow.

## Continue conversations across script invocations

```bash
session_id=$(claude -p "Start a review" --output-format json | jq -r '.session_id')
claude -p "Continue that review" --resume "$session_id"
```

`--continue` for most recent. `--resume <id>` for specific.

## Limitations

> [!note]
> **User-invokable skills** (like `/commit`) and **built-in commands** are only available in interactive mode. In `-p` mode, describe the task you want to accomplish instead.

## Connection to our pipelines

`claude -p --bare` is the right primitive for our Pipeline B's `flush.py`/`compile.py` if they ever need to invoke Claude programmatically (they don't currently — they're shell-only, but if they grow to use LLM judgment this is the entry point).

## Connections
- Related: [[claude-code]], [[claude-managed-agents]], [[source-claude-code-routines-docs]], [[source-claude-code-deep-links-docs]], [[two-pipeline-architecture]], [[agent-sdk-vs-claude-code]], [[source-claude-code-hooks-docs]]
- Refines [[agent-sdk-vs-claude-code]] — the docs now explicitly say `claude -p` IS the Agent SDK's CLI surface
- Pairs with [[source-claude-code-deep-links-docs]] (UI launch from URL) and [[source-claude-code-channels-docs|channels]] (events into session) — three entry points to a Claude Code session

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-programmatic-usage.md | Initial creation from official `headless.md` |
