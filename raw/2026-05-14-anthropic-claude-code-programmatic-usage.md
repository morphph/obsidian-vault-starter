# Claude Code Official Docs — Run Claude Code programmatically

Captured 2026-05-14 from https://code.claude.com/docs/en/headless.md

> Use the Agent SDK to run Claude Code programmatically from the CLI, Python, or TypeScript.

> [!note]
> Starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit, separate from interactive usage limits.

The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code. Available as CLI for scripts/CI/CD, or Python and TypeScript packages.

To run non-interactive mode, pass `-p` with prompt:
```bash
claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"
```

For Python/TypeScript SDK with structured outputs, tool approval callbacks, native message objects → see full Agent SDK docs.

## Basic usage

`-p` (or `--print`) for non-interactive. All CLI options work with `-p`:
* `--continue` for continuing conversations
* `--allowedTools` for auto-approving tools
* `--output-format` for structured output

```bash
claude -p "What does the auth module do?"
```

### Start faster with bare mode

`--bare` reduces startup time by skipping auto-discovery of hooks, skills, plugins, MCP servers, auto memory, CLAUDE.md. Without it, `claude -p` loads same context an interactive session would.

Bare mode useful for CI and scripts where you need same result on every machine. A hook in teammate's `~/.claude` or MCP server in project's `.mcp.json` won't run in bare mode.

```bash
claude --bare -p "Summarize this file" --allowedTools "Read"
```

In bare mode Claude has access to Bash, file read, file edit tools. Pass context via flags:

| To load | Use |
| --- | --- |
| System prompt additions | `--append-system-prompt`, `--append-system-prompt-file` |
| Settings | `--settings <file-or-json>` |
| MCP servers | `--mcp-config <file-or-json>` |
| Custom agents | `--agents <json>` |
| A plugin | `--plugin-dir <path>`, `--plugin-url <url>` |

Bare mode skips OAuth and keychain reads. Anthropic auth must come from `ANTHROPIC_API_KEY` or `apiKeyHelper`. Bedrock, Vertex, Foundry use usual provider credentials.

> [!note]
> `--bare` is recommended mode for scripted/SDK calls, will become default for `-p` in future release.

## Examples

### Pipe data through Claude

```bash
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

With `--output-format json`, payload includes `total_cost_usd` and per-model cost breakdown.

> [!note]
> Piped stdin capped at 10MB (Claude Code v2.1.128+). For larger inputs, write to file and reference path.

### Add Claude to a build script

```json
{
  "scripts": {
    "lint:claude": "git diff main | claude -p \"you are a typo linter. for each typo in this diff, report filename:line on one line and the issue on the next. return nothing else.\""
  }
}
```

### Get structured output

`--output-format`:
* `text` (default): plain text
* `json`: structured with result, session ID, metadata
* `stream-json`: newline-delimited JSON for real-time streaming

```bash
claude -p "Summarize this project" --output-format json
```

JSON Schema:
```bash
claude -p "Extract the main function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}'
```

Result in `structured_output` field.

### Stream responses

```bash
claude -p "Explain recursion" --output-format stream-json --verbose --include-partial-messages
```

Filter for text deltas with jq:
```bash
claude -p "Write a poem" --output-format stream-json --verbose --include-partial-messages | \
  jq -rj 'select(.type == "stream_event" and .event.delta.type? == "text_delta") | .event.delta.text'
```

API retry events: `system/api_retry` with attempt, max_retries, retry_delay_ms, error_status, error.

`system/init` event reports session metadata including model, tools, MCP servers, loaded plugins. First event in stream unless `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` is set.

### Auto-approve tools

```bash
claude -p "Run the test suite and fix any failures" \
  --allowedTools "Bash,Read,Edit"
```

Permission modes:
* `dontAsk` — denies anything not in `permissions.allow` rules or read-only command set (locked-down CI)
* `acceptEdits` — lets Claude write files without prompting, auto-approves common filesystem commands

```bash
claude -p "Apply the lint fixes" --permission-mode acceptEdits
```

Other shell commands and network requests still need `--allowedTools` entry or `permissions.allow` rule, otherwise run aborts.

### Create a commit

```bash
claude -p "Look at my staged changes and create an appropriate commit" \
  --allowedTools "Bash(git diff *),Bash(git log *),Bash(git status *),Bash(git commit *)"
```

`--allowedTools` uses permission rule syntax. Trailing ` *` enables prefix matching.

> [!note]
> User-invoked skills like `/commit` and built-in commands only available in interactive mode. In `-p` mode, describe task instead.

### Customize the system prompt

```bash
gh pr diff "$1" | claude -p \
  --append-system-prompt "You are a security engineer. Review for vulnerabilities." \
  --output-format json
```

`--system-prompt` to fully replace default.

### Continue conversations

```bash
# First request
claude -p "Review this codebase for performance issues"

# Continue most recent
claude -p "Now focus on the database queries" --continue
claude -p "Generate a summary of all issues found" --continue

# Capture session ID
session_id=$(claude -p "Start a review" --output-format json | jq -r '.session_id')
claude -p "Continue that review" --resume "$session_id"
```

## Next steps

* Agent SDK quickstart: Python or TypeScript
* CLI reference: all flags
* GitHub Actions
* GitLab CI/CD
