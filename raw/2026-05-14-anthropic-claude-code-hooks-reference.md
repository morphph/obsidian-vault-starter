# Hooks Reference

> Reference for Claude Code hook events, configuration schema, JSON input/output formats, exit codes, async hooks, HTTP hooks, prompt hooks, and MCP tool hooks.

<Tip>
  For a quickstart guide with examples, see [Automate workflows with hooks](/en/hooks-guide).
</Tip>

Hooks are user-defined shell commands, HTTP endpoints, or LLM prompts that execute automatically at specific points in Claude Code's lifecycle. Use this reference to look up event schemas, configuration options, JSON input/output formats, and advanced features like async hooks, HTTP hooks, and MCP tool hooks. If you're setting up hooks for the first time, start with the [guide](/en/hooks-guide) instead.

## Hook lifecycle

Hooks fire at specific points during a Claude Code session. When an event fires and a matcher matches, Claude Code passes JSON context about the event to your hook handler. For command hooks, input arrives on stdin. For HTTP hooks, it arrives as the POST request body. Your handler can then inspect the input, take action, and optionally return a decision. Events fall into three cadences: once per session (`SessionStart`, `SessionEnd`), once per turn (`UserPromptSubmit`, `Stop`, `StopFailure`), and on every tool call inside the agentic loop (`PreToolUse`, `PostToolUse`):

<div style={{maxWidth: "500px", margin: "0 auto"}}>
  <Frame>
    <img src="https://mintcdn.com/claude-code/ZIW26Z9pnpsXLhbS/images/hooks-lifecycle.svg?fit=max&auto=format&n=ZIW26Z9pnpsXLhbS&q=85&s=ee23691324deb6501df09bfdae560b64" alt="Hook lifecycle diagram showing optional Setup feeding into SessionStart, then a per-turn loop containing UserPromptSubmit, UserPromptExpansion for slash commands, the nested agentic loop (PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure, PostToolBatch, SubagentStart/Stop, TaskCreated, TaskCompleted), and Stop or StopFailure, followed by TeammateIdle, PreCompact, PostCompact, and SessionEnd, with Elicitation and ElicitationResult nested inside MCP tool execution, PermissionDenied as a side branch from PermissionRequest for auto-mode denials, and WorktreeCreate, WorktreeRemove, Notification, ConfigChange, InstructionsLoaded, CwdChanged, and FileChanged as standalone async events" width="520" height="1228" data-path="images/hooks-lifecycle.svg" />
  </Frame>
</div>

The table below summarizes when each event fires. The [Hook events](#hook-events) section documents the full input schema and decision control options for each one.

| Event                 | When it fires                                                                                                                                          |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SessionStart`        | When a session begins or resumes                                                                                                                       |
| `Setup`               | When you start Claude Code with `--init-only`, or with `--init` or `--maintenance` in `-p` mode. For one-time preparation in CI or scripts             |
| `UserPromptSubmit`    | When you submit a prompt, before Claude processes it                                                                                                   |
| `UserPromptExpansion` | When a user-typed command expands into a prompt, before it reaches Claude. Can block the expansion                                                     |
| `PreToolUse`          | Before a tool call executes. Can block it                                                                                                              |
| `PermissionRequest`   | When a permission dialog appears                                                                                                                       |
| `PermissionDenied`    | When a tool call is denied by the auto mode classifier. Return `{retry: true}` to tell the model it may retry the denied tool call                     |
| `PostToolUse`         | After a tool call succeeds                                                                                                                             |
| `PostToolUseFailure`  | After a tool call fails                                                                                                                                |
| `PostToolBatch`       | After a full batch of parallel tool calls resolves, before the next model call                                                                         |
| `Notification`        | When Claude Code sends a notification                                                                                                                  |
| `SubagentStart`       | When a subagent is spawned                                                                                                                             |
| `SubagentStop`        | When a subagent finishes                                                                                                                               |
| `TaskCreated`         | When a task is being created via `TaskCreate`                                                                                                          |
| `TaskCompleted`       | When a task is being marked as completed                                                                                                               |
| `Stop`                | When Claude finishes responding                                                                                                                        |
| `StopFailure`         | When the turn ends due to an API error. Output and exit code are ignored                                                                               |
| `TeammateIdle`        | When an [agent team](/en/agent-teams) teammate is about to go idle                                                                                     |
| `InstructionsLoaded`  | When a CLAUDE.md or `.claude/rules/*.md` file is loaded into context. Fires at session start and when files are lazily loaded during a session         |
| `ConfigChange`        | When a configuration file changes during a session                                                                                                     |
| `CwdChanged`          | When the working directory changes, for example when Claude executes a `cd` command. Useful for reactive environment management with tools like direnv |
| `FileChanged`         | When a watched file changes on disk. The `matcher` field specifies which filenames to watch                                                            |
| `WorktreeCreate`      | When a worktree is being created via `--worktree` or `isolation: "worktree"`. Replaces default git behavior                                            |
| `WorktreeRemove`      | When a worktree is being removed, either at session exit or when a subagent finishes                                                                   |
| `PreCompact`          | Before context compaction                                                                                                                              |
| `PostCompact`         | After context compaction completes                                                                                                                     |
| `Elicitation`         | When an MCP server requests user input during a tool call                                                                                              |
| `ElicitationResult`   | After a user responds to an MCP elicitation, before the response is sent back to the server                                                            |
| `SessionEnd`          | When a session terminates                                                                                                                              |

### How a hook resolves

To see how these pieces fit together, consider this `PreToolUse` hook that blocks destructive shell commands. The `matcher` narrows to Bash tool calls and the `if` condition narrows further to Bash subcommands matching `rm *`, so `block-rm.sh` only spawns when both filters match:

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

The script reads the JSON input from stdin, extracts the command, and returns a `permissionDecision` of `"deny"` if it contains `rm -rf`:

```bash theme={null}
#!/bin/bash
# .claude/hooks/block-rm.sh
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked by hook"
    }
  }'
else
  exit 0  # allow the command
fi
```

Now suppose Claude Code decides to run `Bash "rm -rf /tmp/build"`. Here's what happens:

<Frame>
  <img src="https://mintcdn.com/claude-code/-tYw1BD_DEqfyyOZ/images/hook-resolution.svg?fit=max&auto=format&n=-tYw1BD_DEqfyyOZ&q=85&s=c73ebc1eeda2037570427d7af1e0a891" alt="Hook resolution flow: PreToolUse event fires, matcher checks for Bash match, if condition checks for Bash(rm *) match, hook handler runs, result returns to Claude Code" width="930" height="290" data-path="images/hook-resolution.svg" />
</Frame>

<Steps>
  <Step title="Event fires">
    The `PreToolUse` event fires. Claude Code sends the tool input as JSON on stdin to the hook:

    ```json theme={null}
    { "tool_name": "Bash", "tool_input": { "command": "rm -rf /tmp/build" }, ... }
    ```
  </Step>

  <Step title="Matcher checks">
    The matcher `"Bash"` matches the tool name, so this hook group activates. If you omit the matcher or use `"*"`, the group activates on every occurrence of the event.
  </Step>

  <Step title="If condition checks">
    The `if` condition `"Bash(rm *)"` matches because `rm -rf /tmp/build` is a subcommand matching `rm *`, so this handler spawns. If the command had been `npm test`, the `if` check would fail and `block-rm.sh` would never run, avoiding the process spawn overhead. The `if` field is optional; without it, every handler in the matched group runs.
  </Step>

  <Step title="Hook handler runs">
    The script inspects the full command and finds `rm -rf`, so it prints a decision to stdout:

    ```json theme={null}
    {
      "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Destructive command blocked by hook"
      }
    }
    ```

    If the command had been a safer `rm` variant like `rm file.txt`, the script would hit `exit 0` instead, which tells Claude Code to allow the tool call with no further action.
  </Step>

  <Step title="Claude Code acts on the result">
    Claude Code reads the JSON decision, blocks the tool call, and shows Claude the reason.
  </Step>
</Steps>

The [Configuration](#configuration) section below documents the full schema, and each [hook event](#hook-events) section documents what input your command receives and what output it can return.

## Configuration

Hooks are defined in JSON settings files. The configuration has three levels of nesting:

1. Choose a [hook event](#hook-events) to respond to, like `PreToolUse` or `Stop`
2. Add a [matcher group](#matcher-patterns) to filter when it fires, like "only for the Bash tool"
3. Define one or more [hook handlers](#hook-handler-fields) to run when matched

See [How a hook resolves](#how-a-hook-resolves) above for a complete walkthrough with an annotated example.

<Note>
  This page uses specific terms for each level: **hook event** for the lifecycle point, **matcher group** for the filter, and **hook handler** for the shell command, HTTP endpoint, MCP tool, prompt, or agent that runs. "Hook" on its own refers to the general feature.
</Note>

### Hook locations

Where you define a hook determines its scope:

| Location                                                   | Scope                         | Shareable                          |
| :--------------------------------------------------------- | :---------------------------- | :--------------------------------- |
| `~/.claude/settings.json`                                  | All your projects             | No, local to your machine          |
| `.claude/settings.json`                                    | Single project                | Yes, can be committed to the repo  |
| `.claude/settings.local.json`                              | Single project                | No, gitignored                     |
| Managed policy settings                                    | Organization-wide             | Yes, admin-controlled              |
| [Plugin](/en/plugins) `hooks/hooks.json`                   | When plugin is enabled        | Yes, bundled with the plugin       |
| [Skill](/en/skills) or [agent](/en/sub-agents) frontmatter | While the component is active | Yes, defined in the component file |

For details on settings file resolution, see [settings](/en/settings). Enterprise administrators can use `allowManagedHooksOnly` to block user, project, and plugin hooks. Hooks from plugins force-enabled in managed settings `enabledPlugins` are exempt, so administrators can distribute vetted hooks through an organization marketplace. See [Hook configuration](/en/settings#hook-configuration).

### Matcher patterns

The `matcher` field filters when hooks fire. How a matcher is evaluated depends on the characters it contains:

| Matcher value                       | Evaluated as                                          | Example                                                                                                            |
| :---------------------------------- | :---------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| `"*"`, `""`, or omitted             | Match all                                             | fires on every occurrence of the event                                                                             |
| Only letters, digits, `_`, and `\|` | Exact string, or `\|`-separated list of exact strings | `Bash` matches only the Bash tool; `Edit\|Write` matches either tool exactly                                       |
| Contains any other character        | JavaScript regular expression                         | `^Notebook` matches any tool starting with Notebook; `mcp__memory__.*` matches every tool from the `memory` server |

The `FileChanged` event does not follow these rules when building its watch list. See [FileChanged](#filechanged).

Each event type matches on a different field:

| Event                                                                                                                           | What the matcher filters                                     | Example matcher values                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`                                      | tool name                                                    | `Bash`, `Edit\|Write`, `mcp__.*`                                                                                                                   |
| `SessionStart`                                                                                                                  | how the session started                                      | `startup`, `resume`, `clear`, `compact`                                                                                                            |
| `Setup`                                                                                                                         | which CLI flag triggered setup                               | `init`, `maintenance`                                                                                                                              |
| `SessionEnd`                                                                                                                    | why the session ended                                        | `clear`, `resume`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other`                                                           |
| `Notification`                                                                                                                  | notification type                                            | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_complete`, `elicitation_response`                           |
| `SubagentStart`                                                                                                                 | agent type                                                   | `general-purpose`, `Explore`, `Plan`, or custom agent names                                                                                        |
| `PreCompact`, `PostCompact`                                                                                                     | what triggered compaction                                    | `manual`, `auto`                                                                                                                                   |
| `SubagentStop`                                                                                                                  | agent type                                                   | same values as `SubagentStart`                                                                                                                     |
| `ConfigChange`                                                                                                                  | configuration source                                         | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills`                                                                 |
| `CwdChanged`                                                                                                                    | no matcher support                                           | always fires on every directory change                                                                                                             |
| `FileChanged`                                                                                                                   | literal filenames to watch (see [FileChanged](#filechanged)) | `.envrc\|.env`                                                                                                                                     |
| `StopFailure`                                                                                                                   | error type                                                   | `rate_limit`, `authentication_failed`, `oauth_org_not_allowed`, `billing_error`, `invalid_request`, `server_error`, `max_output_tokens`, `unknown` |
| `InstructionsLoaded`                                                                                                            | load reason                                                  | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact`                                                                       |
| `UserPromptExpansion`                                                                                                           | command name                                                 | your skill or command names                                                                                                                        |
| `Elicitation`                                                                                                                   | MCP server name                                              | your configured MCP server names                                                                                                                   |
| `ElicitationResult`                                                                                                             | MCP server name                                              | same values as `Elicitation`                                                                                                                       |
| `UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove` | no matcher support                                           | always fires on every occurrence                                                                                                                   |

The matcher runs against a field from the [JSON input](#hook-input-and-output) that Claude Code sends to your hook on stdin. For tool events, that field is `tool_name`. Each [hook event](#hook-events) section lists the full set of matcher values and the input schema for that event.

This example runs a linting script only when Claude writes or edits a file:

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/lint-check.sh"
          }
        ]
      }
    ]
  }
}
```

`UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, and `CwdChanged` don't support matchers and always fire on every occurrence. If you add a `matcher` field to these events, it is silently ignored.

For tool events, you can filter more narrowly by setting the [`if` field](#common-fields) on individual hook handlers. `if` uses [permission rule syntax](/en/permissions) to match against the tool name and arguments together, so `"Bash(git *)"` runs when any subcommand of the Bash input matches `git *` and `"Edit(*.ts)"` runs only for TypeScript files.

#### Match MCP tools

[MCP](/en/mcp) server tools appear as regular tools in tool events (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`), so you can match them the same way you match any other tool name.

MCP tools follow the naming pattern `mcp__<server>__<tool>`, for example:

* `mcp__memory__create_entities`: Memory server's create entities tool
* `mcp__filesystem__read_file`: Filesystem server's read file tool
* `mcp__github__search_repositories`: GitHub server's search tool

To match every tool from a server, append `.*` to the server prefix. The `.*` is required: a matcher like `mcp__memory` contains only letters and underscores, so it is compared as an exact string and matches no tool.

* `mcp__memory__.*` matches all tools from the `memory` server
* `mcp__.*__write.*` matches any tool whose name starts with `write` from any server

This example logs all memory server operations and validates write operations from any MCP server:

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Memory operation initiated' >> ~/mcp-operations.log"
          }
        ]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/user/scripts/validate-mcp-write.py"
          }
        ]
      }
    ]
  }
}
```

### Hook handler fields

Each object in the inner `hooks` array is a hook handler: the shell command, HTTP endpoint, MCP tool, LLM prompt, or agent that runs when the matcher matches. There are five types:

* **[Command hooks](#command-hook-fields)** (`type: "command"`): run a shell command. Your script receives the event's [JSON input](#hook-input-and-output) on stdin and communicates results back through exit codes and stdout.
* **[HTTP hooks](#http-hook-fields)** (`type: "http"`): send the event's JSON input as an HTTP POST request to a URL. The endpoint communicates results back through the response body using the same [JSON output format](#json-output) as command hooks.
* **[MCP tool hooks](#mcp-tool-hook-fields)** (`type: "mcp_tool"`): call a tool on an already-connected [MCP server](/en/mcp). The tool's text output is treated like command-hook stdout.
* **[Prompt hooks](#prompt-and-agent-hook-fields)** (`type: "prompt"`): send a prompt to a Claude model for single-turn evaluation. The model returns a yes/no decision as JSON. See [Prompt-based hooks](#prompt-based-hooks).
* **[Agent hooks](#prompt-and-agent-hook-fields)** (`type: "agent"`): spawn a subagent that can use tools like Read, Grep, and Glob to verify conditions before returning a decision. Agent hooks are experimental and may change. See [Agent-based hooks](#agent-based-hooks).

#### Common fields

These fields apply to all hook types:

| Field           | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`          | yes      | `"command"`, `"http"`, `"mcp_tool"`, `"prompt"`, or `"agent"`                                                                                                                                                                                                                                                                                                                                                                                          |
| `if`            | no       | Permission rule syntax to filter when this hook runs, such as `"Bash(git *)"` or `"Edit(*.ts)"`. The hook only spawns if the tool call matches the pattern, or if a Bash command is too complex to parse. Only evaluated on tool events: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, and `PermissionDenied`. On other events, a hook with `if` set never runs. Uses the same syntax as [permission rules](/en/permissions) |
| `timeout`       | no       | Seconds before canceling. Defaults: 600 for command, 30 for prompt, 60 for agent                                                                                                                                                                                                                                                                                                                                                                       |
| `statusMessage` | no       | Custom spinner message displayed while the hook runs                                                                                                                                                                                                                                                                                                                                                                                                   |
| `once`          | no       | If `true`, runs once per session then is removed. Only honored for hooks declared in [skill frontmatter](#hooks-in-skills-and-agents); ignored in settings files and agent frontmatter                                                                                                                                                                                                                                                                 |

The `if` field holds exactly one permission rule. There is no `&&`, `||`, or list syntax for combining rules; to apply multiple conditions, define a separate hook handler for each. For Bash, the rule is matched against each subcommand of the tool input after leading `VAR=value` assignments are stripped, so `if: "Bash(git push *)"` matches both `FOO=bar git push` and `npm test && git push`. The hook runs if any subcommand matches, and always runs when the command is too complex to parse.

#### Command hook fields

In addition to the [common fields](#common-fields), command hooks accept these fields:

| Field         | Required | Description                                                                                                                                                                                                                                       |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `command`     | yes      | Shell command to execute. With `args`, the executable to spawn directly. See [Exec form and shell form](#exec-form-and-shell-form)                                                                                                                |
| `args`        | no       | Argument list. When present, `command` is resolved as an executable and spawned directly with `args` as the argument vector, with no shell involved. See [Exec form and shell form](#exec-form-and-shell-form)                                    |
| `async`       | no       | If `true`, runs in the background without blocking. See [Run hooks in the background](#run-hooks-in-the-background)                                                                                                                               |
| `asyncRewake` | no       | If `true`, runs in the background and wakes Claude on exit code 2. Implies `async`. The hook's stderr, or stdout if stderr is empty, is shown to Claude as a system reminder so it can react to a long-running background failure                 |
| `shell`       | no       | Shell to use for this hook. Accepts `"bash"` (default) or `"powershell"`. Setting `"powershell"` runs the command via PowerShell on Windows. Does not require `CLAUDE_CODE_USE_POWERSHELL_TOOL` since hooks spawn PowerShell directly. Ignored when `args` is set |

<a id="exec-form-and-shell-form" />

##### Exec form and shell form

A command hook runs as exec form when `args` is set, and shell form when `args` is omitted. Set `args` whenever the hook references a [path placeholder](#reference-scripts-by-path), since each element is passed as one argument with no quoting. Omit `args` when you need shell features like pipes or `&&`, or when neither concern applies.

**Exec form** runs when `args` is present. Claude Code resolves `command` as an executable on `PATH` and spawns it directly with `args` as the argument vector. There is no shell, so each `args` element is one argument exactly as written, and path placeholders like `${CLAUDE_PLUGIN_ROOT}` are substituted into `command` and into each `args` element as plain strings. Special characters such as apostrophes, `$`, and backticks pass through verbatim because there is no shell to interpret them. No shell tokenization happens on any platform.

**Shell form** runs when `args` is absent. The `command` string is passed to a shell: `sh -c` on macOS and Linux, Git Bash on Windows, or PowerShell when Git Bash isn't installed. Set the `shell` field to choose explicitly. The shell tokenizes the string, expands variables, and interprets pipes, `&&`, redirects, and globs.

<Note>
  On Windows, exec form requires `command` to resolve to a real executable such as a `.exe`. The `.cmd` and `.bat` shims that npm, npx, eslint, and other tools install in `node_modules/.bin` are not executables and cannot be spawned without a shell. To run them in exec form, invoke the underlying script with `node` directly, for example `"command": "node", "args": ["${CLAUDE_PLUGIN_ROOT}/node_modules/eslint/bin/eslint.js"]`. The `node` plus script-path pattern works on every platform because `node.exe` is a real binary. To run a `.cmd` or `.bat` shim by name, use shell form.
</Note>

This example runs a Node script bundled with a plugin. Exec form passes the resolved script path as one argument with no quoting:

```json theme={null}
{
  "type": "command",
  "command": "node",
  "args": ["${CLAUDE_PLUGIN_ROOT}/scripts/format.js", "--fix"]
}
```

The equivalent shell form needs quoting to handle paths with spaces or special characters:

```json theme={null}
{
  "type": "command",
  "command": "node \"${CLAUDE_PLUGIN_ROOT}\"/scripts/format.js --fix"
}
```

Both forms support the same [path placeholders](#reference-scripts-by-path), and both export them as the environment variables `CLAUDE_PROJECT_DIR`, `CLAUDE_PLUGIN_ROOT`, and `CLAUDE_PLUGIN_DATA` on the spawned process, so a script can read `process.env.CLAUDE_PLUGIN_ROOT` regardless of how it was launched. Plugin hooks additionally substitute `${user_config.*}` values; see [User configuration](/en/plugins-reference#user-configuration).

<Note>
  In exec form, `command` is the executable name or path only. If `command` is a bare name with no path separator and contains whitespace alongside `args`, Claude Code logs a warning because the spawn will fail: there is no executable named `node script.js`. Move the extra tokens into `args`. Absolute paths with spaces, such as `C:\Program Files\nodejs\node.exe`, are a single valid executable and do not trigger the warning.
</Note>

#### HTTP hook fields

In addition to the [common fields](#common-fields), HTTP hooks accept these fields:

| Field            | Required | Description                                                                                                                                                                                      |
| :--------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`            | yes      | URL to send the POST request to                                                                                                                                                                  |
| `headers`        | no       | Additional HTTP headers as key-value pairs. Values support environment variable interpolation using `$VAR_NAME` or `${VAR_NAME}` syntax. Only variables listed in `allowedEnvVars` are resolved  |
| `allowedEnvVars` | no       | List of environment variable names that may be interpolated into header values. References to unlisted variables are replaced with empty strings. Required for any env var interpolation to work |

Claude Code sends the hook's [JSON input](#hook-input-and-output) as the POST request body with `Content-Type: application/json`. The response body uses the same [JSON output format](#json-output) as command hooks.

Error handling differs from command hooks: non-2xx responses, connection failures, and timeouts all produce non-blocking errors that allow execution to continue. To block a tool call or deny a permission, return a 2xx response with a JSON body containing `decision: "block"` or a `hookSpecificOutput` with `permissionDecision: "deny"`.

This example sends `PreToolUse` events to a local validation service, authenticating with a token from the `MY_TOKEN` environment variable:

```json theme={null}
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "http",
            "url": "http://localhost:8080/hooks/pre-tool-use",
            "timeout": 30,
            "headers": {
              "Authorization": "Bearer $MY_TOKEN"
            },
            "allowedEnvVars": ["MY_TOKEN"]
          }
        ]
      }
    ]
  }
}
```

#### MCP tool hook fields

In addition to the [common fields](#common-fields), MCP tool hooks accept these fields:

| Field    | Required | Description                                                                                                                                          |
| :------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `server` | yes      | Name of a configured MCP server. The server must already be connected; the hook never triggers an OAuth or connection flow                           |
| `tool`   | yes      | Name of the tool to call on that server                                                                                                              |
| `input`  | no       | Arguments passed to the tool. String values support `${path}` substitution from the hook's [JSON input](#hook-input-and-output), such as `"${tool_input.file_path}"` |

The tool's text content is treated like command-hook stdout: if it parses as valid [JSON output](#json-output) it is processed as a decision, otherwise it is shown as plain text. If the named server is not connected, or the tool returns `isError: true`, the hook produces a non-blocking error and execution continues.

MCP tool hooks are available on every hook event once Claude Code has connected to your MCP servers. `SessionStart` and `Setup` typically fire before servers finish connecting, so hooks on those events should expect the "not connected" error on first run.

This example calls the `security_scan` tool on the `my_server` MCP server after each `Write` or `Edit`, passing the edited file's path:

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "my_server",
            "tool": "security_scan",
            "input": { "file_path": "${tool_input.file_path}" }
          }
        ]
      }
    ]
  }
}
```

#### Prompt and agent hook fields

In addition to the [common fields](#common-fields), prompt and agent hooks accept these fields:

| Field    | Required | Description                                                                                 |
| :------- | :------- | :------------------------------------------------------------------------------------------ |
| `prompt` | yes      | Prompt text to send to the model. Use `$ARGUMENTS` as a placeholder for the hook input JSON |
| `model`  | no       | Model to use for evaluation. Defaults to a fast model                                       |

All matching hooks run in parallel, and identical handlers are deduplicated automatically. Command hooks are deduplicated by command string and `args`, and HTTP hooks are deduplicated by URL. Handlers run in the current directory with Claude Code's environment. The `$CLAUDE_CODE_REMOTE` environment variable is set to `"true"` in remote web environments and not set in the local CLI.

### Reference scripts by path

Use these placeholders to reference hook scripts relative to the project or plugin root, regardless of the working directory when the hook runs:

* `${CLAUDE_PROJECT_DIR}`: the project root.
* `${CLAUDE_PLUGIN_ROOT}`: the plugin's installation directory, for scripts bundled with a [plugin](/en/plugins). Changes on each plugin update.
* `${CLAUDE_PLUGIN_DATA}`: the plugin's [persistent data directory](/en/plugins-reference#persistent-data-directory), for dependencies and state that should survive plugin updates.

Prefer [exec form](#exec-form-and-shell-form) for any hook that references a path placeholder. Exec form passes each `args` element as one argument with no shell tokenization, so paths with spaces or special characters need no quoting. In shell form, wrap each placeholder in double quotes.

<Tabs>
  <Tab title="Project scripts">
    This example uses `${CLAUDE_PROJECT_DIR}` to run a style checker from the project's `.claude/hooks/` directory after any `Write` or `Edit` tool call:

    ```json theme={null}
    {
      "hooks": {
        "PostToolUse": [
          {
            "matcher": "Write|Edit",
            "hooks": [
              {
                "type": "command",
                "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/check-style.sh",
                "args": []
              }
            ]
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="Plugin scripts">
    Define plugin hooks in `hooks/hooks.json` with an optional top-level `description` field. When a plugin is enabled, its hooks merge with your user and project hooks.

    This example runs a formatting script bundled with the plugin:

    ```json theme={null}
    {
      "description": "Automatic code formatting",
      "hooks": {
        "PostToolUse": [
          {
            "matcher": "Write|Edit",
            "hooks": [
              {
                "type": "command",
                "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh",
                "args": [],
                "timeout": 30
              }
            ]
          }
        ]
      }
    }
    ```

    See the [plugin components reference](/en/plugins-reference#hooks) for details on creating plugin hooks.
  </Tab>
</Tabs>

### Hooks in skills and agents

In addition to settings files and plugins, hooks can be defined directly in [skills](/en/skills) and [subagents](/en/sub-agents) using frontmatter. These hooks are scoped to the component's lifecycle and only run when that component is active.

All hook events are supported. For subagents, `Stop` hooks are automatically converted to `SubagentStop` since that is the event that fires when a subagent completes.

Hooks use the same configuration format as settings-based hooks but are scoped to the component's lifetime and cleaned up when it finishes.

This skill defines a `PreToolUse` hook that runs a security validation script before each `Bash` command:

```yaml theme={null}
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
---
```

Agents use the same format in their YAML frontmatter.

### The `/hooks` menu

Type `/hooks` in Claude Code to open a read-only browser for your configured hooks. The menu shows every hook event with a count of configured hooks, lets you drill into matchers, and shows the full details of each hook handler. Use it to verify configuration, check which settings file a hook came from, or inspect a hook's command, prompt, or URL.

The menu displays all five hook types: `command`, `prompt`, `agent`, `http`, and `mcp_tool`. Each hook is labeled with a `[type]` prefix and a source indicating where it was defined:

* `User`: from `~/.claude/settings.json`
* `Project`: from `.claude/settings.json`
* `Local`: from `.claude/settings.local.json`
* `Plugin`: from a plugin's `hooks/hooks.json`
* `Session`: registered in memory for the current session
* `Built-in`: registered internally by Claude Code

Selecting a hook opens a detail view showing its event, matcher, type, source file, and the full command, prompt, or URL. The menu is read-only: to add, modify, or remove hooks, edit the settings JSON directly or ask Claude to make the change.

### Disable or remove hooks

To remove a hook, delete its entry from the settings JSON file.

To temporarily disable all hooks without removing them, set `"disableAllHooks": true` in your settings file. There is no way to disable an individual hook while keeping it in the configuration.

The `disableAllHooks` setting respects the managed settings hierarchy. If an administrator has configured hooks through managed policy settings, `disableAllHooks` set in user, project, or local settings cannot disable those managed hooks. Only `disableAllHooks` set at the managed settings level can disable managed hooks.

Direct edits to hooks in settings files are normally picked up automatically by the file watcher.

## Hook input and output

Command hooks receive JSON data via stdin and communicate results through exit codes, stdout, and stderr. HTTP hooks receive the same JSON as the POST request body and communicate results through the HTTP response body. This section covers fields and behavior common to all events. Each event's section under [Hook events](#hook-events) includes its specific input schema and decision control options.

### Common input fields

Hook events receive these fields as JSON, in addition to event-specific fields documented in each [hook event](#hook-events) section. For command hooks, this JSON arrives via stdin. For HTTP hooks, it arrives as the POST request body.

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `session_id`      | Current session identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `transcript_path` | Path to conversation JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `cwd`             | Current working directory when the hook is invoked                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `permission_mode` | Current [permission mode](/en/permissions#permission-modes): `"default"`, `"plan"`, `"acceptEdits"`, `"auto"`, `"dontAsk"`, or `"bypassPermissions"`. Not all events receive this field: see each event's JSON example below to check                                                                                                                                                                                                                                                                                                                                                                       |
| `effort`          | Object with a `level` field holding the active [effort level](/en/model-config#adjust-effort-level) for the turn: `"low"`, `"medium"`, `"high"`, `"xhigh"`, or `"max"`. If the requested effort exceeds what the current model supports, this is the downgraded level the model actually used, not the level you requested. The object matches the [status line](/en/statusline#available-data) `effort` field. Present for events that fire within a tool-use context, such as `PreToolUse`, `PostToolUse`, `Stop`, and `SubagentStop`, when the current model supports the effort parameter. The level is also available to hook commands and the Bash tool as the `$CLAUDE_EFFORT` environment variable. |
| `hook_event_name` | Name of the event that fired                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

When running with `--agent` or inside a subagent, two additional fields are included:

| Field        | Description                                                                                                                                                                                                                                                                                                                                           |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`   | Unique identifier for the subagent. Present only when the hook fires inside a subagent call. Use this to distinguish subagent hook calls from main-thread calls.                                                                                                                                                                                      |
| `agent_type` | Agent name (for example, `"Explore"` or `"security-reviewer"`). Present when the session uses `--agent` or the hook fires inside a subagent. For subagents, the subagent's type takes precedence over the session's `--agent` value. For [custom subagents](/en/sub-agents), this is the `name` field from the agent's frontmatter, not the filename. |

Only [`SessionStart`](#sessionstart) hooks receive a `model` field. There is no `$CLAUDE_MODEL` environment variable. A hook process inherits the parent environment, so it can read `$ANTHROPIC_MODEL` if you set it in your shell, but that value does not change when you switch models with `/model` during a session.

For example, a `PreToolUse` hook for a Bash command receives this on stdin:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/home/user/.claude/projects/.../transcript.jsonl",
  "cwd": "/home/user/my-project",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test"
  }
}
```

The `tool_name` and `tool_input` fields are event-specific. Each [hook event](#hook-events) section documents the additional fields for that event.

### Exit code output

The exit code from your hook command tells Claude Code whether the action should proceed, be blocked, or be ignored.

**Exit 0** means success. Claude Code parses stdout for [JSON output fields](#json-output). JSON output is only processed on exit 0. For most events, stdout is written to the debug log but not shown in the transcript. The exceptions are `UserPromptSubmit`, `UserPromptExpansion`, and `SessionStart`, where stdout is added as context that Claude can see and act on.

**Exit 2** means a blocking error. Claude Code ignores stdout and any JSON in it. Instead, stderr text is fed back to Claude as an error message. The effect depends on the event: `PreToolUse` blocks the tool call, `UserPromptSubmit` rejects the prompt, and so on. See [exit code 2 behavior](#exit-code-2-behavior-per-event) for the full list.

**Any other exit code** is a non-blocking error for most hook events. The transcript shows a `<hook name> hook error` notice followed by the first line of stderr, so you can identify the cause without `--debug`. Execution continues and the full stderr is written to the debug log.

For example, a hook command script that blocks dangerous Bash commands:

```bash theme={null}
#!/bin/bash
# Reads JSON input from stdin, checks the command
command=$(jq -r '.tool_input.command' < /dev/stdin)

if [[ "$command" == rm* ]]; then
  echo "Blocked: rm commands are not allowed" >&2
  exit 2  # Blocking error: tool call is prevented
fi

exit 0  # Success: tool call proceeds
```

<Warning>
  For most hook events, only exit code 2 blocks the action. Claude Code treats exit code 1 as a non-blocking error and proceeds with the action, even though 1 is the conventional Unix failure code. If your hook is meant to enforce a policy, use `exit 2`. The exception is `WorktreeCreate`, where any non-zero exit code aborts worktree creation.
</Warning>

#### Exit code 2 behavior per event

Exit code 2 is the way a hook signals "stop, don't do this." The effect depends on the event, because some events represent actions that can be blocked (like a tool call that hasn't happened yet) and others represent things that already happened or can't be prevented.

| Hook event            | Can block? | What happens on exit 2                                                                                                               |
| :-------------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `PreToolUse`          | Yes        | Blocks the tool call                                                                                                                 |
| `PermissionRequest`   | Yes        | Denies the permission                                                                                                                |
| `UserPromptSubmit`    | Yes        | Blocks prompt processing and erases the prompt                                                                                       |
| `UserPromptExpansion` | Yes        | Blocks the expansion                                                                                                                 |
| `Stop`                | Yes        | Prevents Claude from stopping, continues the conversation                                                                            |
| `SubagentStop`        | Yes        | Prevents the subagent from stopping                                                                                                  |
| `TeammateIdle`        | Yes        | Prevents the teammate from going idle (teammate continues working)                                                                   |
| `TaskCreated`         | Yes        | Rolls back the task creation                                                                                                         |
| `TaskCompleted`       | Yes        | Prevents the task from being marked as completed                                                                                     |
| `ConfigChange`        | Yes        | Blocks the configuration change from taking effect (except `policy_settings`)                                                        |
| `StopFailure`         | No         | Output and exit code are ignored                                                                                                     |
| `PostToolUse`         | No         | Shows stderr to Claude (tool already ran)                                                                                            |
| `PostToolUseFailure`  | No         | Shows stderr to Claude (tool already failed)                                                                                         |
| `PostToolBatch`       | Yes        | Stops the agentic loop before the next model call                                                                                    |
| `PermissionDenied`    | No         | Exit code and stderr are ignored (denial already occurred). Use JSON `hookSpecificOutput.retry: true` to tell the model it may retry |
| `Notification`        | No         | Shows stderr to user only                                                                                                            |
| `SubagentStart`       | No         | Shows stderr to user only                                                                                                            |
| `SessionStart`        | No         | Shows stderr to user only                                                                                                            |
| `Setup`               | No         | Shows stderr to user only                                                                                                            |
| `SessionEnd`          | No         | Shows stderr to user only                                                                                                            |
| `CwdChanged`          | No         | Shows stderr to user only                                                                                                            |
| `FileChanged`         | No         | Shows stderr to user only                                                                                                            |
| `PreCompact`          | Yes        | Blocks compaction                                                                                                                    |
| `PostCompact`         | No         | Shows stderr to user only                                                                                                            |
| `Elicitation`         | Yes        | Denies the elicitation                                                                                                               |
| `ElicitationResult`   | Yes        | Blocks the response (action becomes decline)                                                                                         |
| `WorktreeCreate`      | Yes        | Any non-zero exit code causes worktree creation to fail                                                                              |
| `WorktreeRemove`      | No         | Failures are logged in debug mode only                                                                                               |
| `InstructionsLoaded`  | No         | Exit code is ignored                                                                                                                 |

### HTTP response handling

HTTP hooks use HTTP status codes and response bodies instead of exit codes and stdout:

* **2xx with an empty body**: success, equivalent to exit code 0 with no output
* **2xx with a plain text body**: success, the text is added as context
* **2xx with a JSON body**: success, parsed using the same [JSON output](#json-output) schema as command hooks
* **Non-2xx status**: non-blocking error, execution continues
* **Connection failure or timeout**: non-blocking error, execution continues

Unlike command hooks, HTTP hooks cannot signal a blocking error through status codes alone. To block a tool call or deny a permission, return a 2xx response with a JSON body containing the appropriate decision fields.

### JSON output

Exit codes let you allow or block, but JSON output gives you finer-grained control. Instead of exiting with code 2 to block, exit 0 and print a JSON object to stdout. Claude Code reads specific fields from that JSON to control behavior, including [decision control](#decision-control) for blocking, allowing, or escalating to the user.

<Note>
  You must choose one approach per hook, not both: either use exit codes alone for signaling, or exit 0 and print JSON for structured control. Claude Code only processes JSON on exit 0. If you exit 2, any JSON is ignored.
</Note>

Your hook's stdout must contain only the JSON object. If your shell profile prints text on startup, it can interfere with JSON parsing. See [JSON validation failed](/en/hooks-guide#json-validation-failed) in the troubleshooting guide.

Hook output injected into context (`additionalContext`, `systemMessage`, or plain stdout) is capped at 10,000 characters. Output that exceeds this limit is saved to a file and replaced with a preview and file path, the same way large tool results are handled.

The JSON object supports three kinds of fields:

* **Universal fields** like `continue` work across all events. These are listed in the table below.
* **Top-level `decision` and `reason`** are used by some events to block or provide feedback.
* **`hookSpecificOutput`** is a nested object for events that need richer control. It requires a `hookEventName` field set to the event name.

| Field            | Default | Description                                                                                                                |
| :--------------- | :------ | :------------------------------------------------------------------------------------------------------------------------- |
| `continue`       | `true`  | If `false`, Claude stops processing entirely after the hook runs. Takes precedence over any event-specific decision fields |
| `stopReason`     | none    | Message shown to the user when `continue` is `false`. Not shown to Claude                                                  |
| `suppressOutput` | `false` | If `true`, omits stdout from the debug log                                                                                 |
| `systemMessage`  | none    | Warning message shown to the user                                                                                          |

To stop Claude entirely regardless of event type:

```json theme={null}
{ "continue": false, "stopReason": "Build failed, fix errors before continuing" }
```

#### Add context for Claude

The `additionalContext` field passes a string from your hook into Claude's context window. Claude Code wraps the string in a system reminder and inserts it into the conversation at the point where the hook fired. Claude reads the reminder on the next model request, but it does not appear as a chat message in the interface.

Return `additionalContext` inside `hookSpecificOutput` alongside the event name:

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "This file is generated. Edit src/schema.ts and run `bun generate` instead."
  }
}
```

Where the reminder appears depends on the event:

* [SessionStart](#sessionstart), [Setup](#setup), and [SubagentStart](#subagentstart): at the start of the conversation, before the first prompt
* [UserPromptSubmit](#userpromptsubmit) and [UserPromptExpansion](#userpromptexpansion): alongside the submitted prompt
* [PreToolUse](#pretooluse), [PostToolUse](#posttooluse), [PostToolUseFailure](#posttoolusefailure), and [PostToolBatch](#posttoolbatch): next to the tool result

When several hooks return `additionalContext` for the same event, Claude receives all of the values. If a value exceeds 10,000 characters, Claude Code writes the full text to a file in the session directory and passes Claude the file path with a short preview instead.

Use `additionalContext` for information Claude should know about the current state of your environment or the operation that just ran:

* **Environment state**: the current branch, deployment target, or active feature flags
* **Conditional project rules**: which test command applies to the file just edited, which directories are read-only in this worktree
* **External data**: open issues assigned to you, recent CI results, content fetched from an internal service

For instructions that never change, prefer [CLAUDE.md](/en/memory). It loads without running a script and is the standard place for static project conventions.

Write the text as factual statements rather than imperative system instructions. Phrasing such as "The deployment target is production" or "This repo uses `bun test`" reads as project information. Text framed as out-of-band system commands can trigger Claude's prompt-injection defenses, which causes Claude to surface the text to you instead of treating it as context.

Once injected, the text is saved in the session transcript. For mid-session events like `PostToolUse` or `UserPromptSubmit`, resuming with `--continue` or `--resume` replays the saved text rather than re-running the hook for past turns, so values like timestamps or commit SHAs become stale on resume. `SessionStart` hooks run again on resume with `source` set to `"resume"`, so they can refresh their context.

#### Decision control

Not every event supports blocking or controlling behavior through JSON. The events that do each use a different set of fields to express that decision. Use this table as a quick reference before writing a hook:

| Events                                                                                                                              | Decision pattern               | Key fields                                                                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| UserPromptSubmit, UserPromptExpansion, PostToolUse, PostToolUseFailure, PostToolBatch, Stop, SubagentStop, ConfigChange, PreCompact | Top-level `decision`           | `decision: "block"`, `reason`                                                                                                                                       |
| TeammateIdle, TaskCreated, TaskCompleted                                                                                            | Exit code or `continue: false` | Exit code 2 blocks the action with stderr feedback. JSON `{"continue": false, "stopReason": "..."}` also stops the teammate entirely, matching `Stop` hook behavior |
| PreToolUse                                                                                                                          | `hookSpecificOutput`           | `permissionDecision` (allow/deny/ask/defer), `permissionDecisionReason`                                                                                             |
| PermissionRequest                                                                                                                   | `hookSpecificOutput`           | `decision.behavior` (allow/deny)                                                                                                                                    |
| PermissionDenied                                                                                                                    | `hookSpecificOutput`           | `retry: true` tells the model it may retry the denied tool call                                                                                                     |
| WorktreeCreate                                                                                                                      | path return                    | Command hook prints path on stdout; HTTP hook returns `hookSpecificOutput.worktreePath`. Hook failure or missing path fails creation                                |
| Elicitation                                                                                                                         | `hookSpecificOutput`           | `action` (accept/decline/cancel), `content` (form field values for accept)                                                                                          |
| ElicitationResult                                                                                                                   | `hookSpecificOutput`           | `action` (accept/decline/cancel), `content` (form field values override)                                                                                            |
| WorktreeRemove, Notification, SessionEnd, PostCompact, InstructionsLoaded, StopFailure, CwdChanged, FileChanged                     | None                           | No decision control. Used for side effects like logging or cleanup                                                                                                  |

Here are examples of each pattern in action:

<Tabs>
  <Tab title="Top-level decision">
    Used by `UserPromptSubmit`, `UserPromptExpansion`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Stop`, `SubagentStop`, `ConfigChange`, and `PreCompact`. The only value is `"block"`. To allow the action to proceed, omit `decision` from your JSON, or exit 0 without any JSON at all:

    ```json theme={null}
    {
      "decision": "block",
      "reason": "Test suite must pass before proceeding"
    }
    ```
  </Tab>

  <Tab title="PreToolUse">
    Uses `hookSpecificOutput` for richer control: allow, deny, or escalate to the user. You can also modify tool input before it runs or inject additional context for Claude. See [PreToolUse decision control](#pretooluse-decision-control) for the full set of options.

    ```json theme={null}
    {
      "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "Database writes are not allowed"
      }
    }
    ```
  </Tab>

  <Tab title="PermissionRequest">
    Uses `hookSpecificOutput` to allow or deny a permission request on behalf of the user. When allowing, you can also modify the tool's input or apply permission rules so the user isn't prompted again. See [PermissionRequest decision control](#permissionrequest-decision-control) for the full set of options.

    ```json theme={null}
    {
      "hookSpecificOutput": {
        "hookEventName": "PermissionRequest",
        "decision": {
          "behavior": "allow",
          "updatedInput": {
            "command": "npm run lint"
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

For extended examples including Bash command validation, prompt filtering, and auto-approval scripts, see [What you can automate](/en/hooks-guide#what-you-can-automate) in the guide and the [Bash command validator reference implementation](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py).

## Hook events

Each event corresponds to a point in Claude Code's lifecycle where hooks can run. The sections below are ordered to match the lifecycle: from session setup through the agentic loop to session end. Each section describes when the event fires, what matchers it supports, the JSON input it receives, and how to control behavior through output.

### SessionStart

Runs when Claude Code starts a new session or resumes an existing session. Useful for loading development context like existing issues or recent changes to your codebase, or setting up environment variables. For static context that does not require a script, use [CLAUDE.md](/en/memory) instead.

SessionStart runs on every session, so keep these hooks fast. Only `type: "command"` and `type: "mcp_tool"` hooks are supported.

The matcher value corresponds to how the session was initiated:

| Matcher   | When it fires                          |
| :-------- | :------------------------------------- |
| `startup` | New session                            |
| `resume`  | `--resume`, `--continue`, or `/resume` |
| `clear`   | `/clear`                               |
| `compact` | Auto or manual compaction              |

#### SessionStart input

In addition to the [common input fields](#common-input-fields), SessionStart hooks receive `source`, `model`, and optionally `agent_type`. The `source` field indicates how the session started: `"startup"` for new sessions, `"resume"` for resumed sessions, `"clear"` after `/clear`, or `"compact"` after compaction. The `model` field contains the model identifier. If you start Claude Code with `claude --agent <name>`, an `agent_type` field contains the agent name.

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "SessionStart",
  "source": "startup",
  "model": "claude-sonnet-4-6"
}
```

#### SessionStart decision control

Any text your hook script prints to stdout is added as context for Claude. In addition to the [JSON output fields](#json-output) available to all hooks, you can return these event-specific fields:

| Field               | Description                                                                                                                                                                                           |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additionalContext` | String added to Claude's context at the start of the conversation, before the first prompt. See [Add context for Claude](#add-context-for-claude) for how the text is delivered and what to put in it |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Current branch: feat/auth-refactor\nUncommitted changes: src/auth.ts, src/login.tsx\nActive issue: #4211 Migrate to OAuth2"
  }
}
```

Since plain stdout already reaches Claude for this event, a hook that only loads context can print to stdout directly without building JSON. Use the JSON form when you need to combine context with other fields such as `suppressOutput`.

#### Persist environment variables

SessionStart hooks have access to the `CLAUDE_ENV_FILE` environment variable, which provides a file path where you can persist environment variables for subsequent Bash commands.

To set individual environment variables, write `export` statements to `CLAUDE_ENV_FILE`. Use append (`>>`) to preserve variables set by other hooks:

```bash theme={null}
#!/bin/bash

if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
  echo 'export DEBUG_LOG=true' >> "$CLAUDE_ENV_FILE"
  echo 'export PATH="$PATH:./node_modules/.bin"' >> "$CLAUDE_ENV_FILE"
fi

exit 0
```

To capture all environment changes from setup commands, compare the exported variables before and after:

```bash theme={null}
#!/bin/bash

ENV_BEFORE=$(export -p | sort)

# Run your setup commands that modify the environment
source ~/.nvm/nvm.sh
nvm use 20

if [ -n "$CLAUDE_ENV_FILE" ]; then
  ENV_AFTER=$(export -p | sort)
  comm -13 <(echo "$ENV_BEFORE") <(echo "$ENV_AFTER") >> "$CLAUDE_ENV_FILE"
fi

exit 0
```

Any variables written to this file will be available in all subsequent Bash commands that Claude Code executes during the session.

<Note>
  `CLAUDE_ENV_FILE` is available for SessionStart, [Setup](#setup), [CwdChanged](#cwdchanged), and [FileChanged](#filechanged) hooks. Other hook types do not have access to this variable.
</Note>

### Setup

Fires only when you launch Claude Code with `--init-only`, or with `--init` or `--maintenance` in print mode (`-p`). It does not fire on normal startup. Use it for one-time dependency installation or scheduled cleanup that you trigger explicitly from CI or scripts, separate from normal session startup. For per-session initialization, use [SessionStart](#sessionstart) instead.

The matcher value corresponds to the CLI flag that triggered the hook:

| Matcher       | When it fires                              |
| :------------ | :----------------------------------------- |
| `init`        | `claude --init-only` or `claude -p --init` |
| `maintenance` | `claude -p --maintenance`                  |

`--init-only` runs Setup hooks and `SessionStart` hooks with the `startup` matcher, then exits without starting a conversation. `--init` and `--maintenance` fire Setup hooks only when combined with `-p` (print mode); in an interactive session those two flags do not currently fire Setup hooks.

Because Setup does not fire on every launch, a plugin that needs a dependency installed cannot rely on Setup alone. The practical pattern is to check for the dependency on first use and install on miss, for example a hook or skill that tests for `${CLAUDE_PLUGIN_DATA}/node_modules` and runs `npm install` if absent. See the [persistent data directory](/en/plugins-reference#persistent-data-directory) for where to store installed dependencies.

#### Setup input

In addition to the [common input fields](#common-input-fields), Setup hooks receive a `trigger` field set to either `"init"` or `"maintenance"`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "Setup",
  "trigger": "init"
}
```

#### Setup decision control

Setup hooks cannot block. On exit code 2, stderr is shown to the user; on any other non-zero exit code, stderr appears only when you launch with `--verbose`. In both cases execution continues. To pass information into Claude's context, return `additionalContext` in JSON output; plain stdout is written to the debug log only. In addition to the [JSON output fields](#json-output) available to all hooks, you can return these event-specific fields:

| Field               | Description                                                               |
| :------------------ | :------------------------------------------------------------------------ |
| `additionalContext` | String added to Claude's context. Multiple hooks' values are concatenated |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "Setup",
    "additionalContext": "Dependencies installed: node_modules, .venv"
  }
}
```

Setup hooks have access to `CLAUDE_ENV_FILE`. Variables written to that file persist into subsequent Bash commands for the session, just as in [SessionStart hooks](#persist-environment-variables). Only `type: "command"` and `type: "mcp_tool"` hooks are supported.

### InstructionsLoaded

Fires when a `CLAUDE.md` or `.claude/rules/*.md` file is loaded into context. This event fires at session start for eagerly-loaded files and again later when files are lazily loaded, for example when Claude accesses a subdirectory that contains a nested `CLAUDE.md` or when conditional rules with `paths:` frontmatter match. The hook does not support blocking or decision control. It runs asynchronously for observability purposes.

The matcher runs against `load_reason`. For example, use `"matcher": "session_start"` to fire only for files loaded at session start, or `"matcher": "path_glob_match|nested_traversal"` to fire only for lazy loads.

#### InstructionsLoaded input

In addition to the [common input fields](#common-input-fields), InstructionsLoaded hooks receive these fields:

| Field               | Description                                                                                                                                                                                                   |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `file_path`         | Absolute path to the instruction file that was loaded                                                                                                                                                         |
| `memory_type`       | Scope of the file: `"User"`, `"Project"`, `"Local"`, or `"Managed"`                                                                                                                                           |
| `load_reason`       | Why the file was loaded: `"session_start"`, `"nested_traversal"`, `"path_glob_match"`, `"include"`, or `"compact"`. The `"compact"` value fires when instruction files are re-loaded after a compaction event |
| `globs`             | Path glob patterns from the file's `paths:` frontmatter, if any. Present only for `path_glob_match` loads                                                                                                     |
| `trigger_file_path` | Path to the file whose access triggered this load, for lazy loads                                                                                                                                             |
| `parent_file_path`  | Path to the parent instruction file that included this one, for `include` loads                                                                                                                               |

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "InstructionsLoaded",
  "file_path": "/Users/my-project/CLAUDE.md",
  "memory_type": "Project",
  "load_reason": "session_start"
}
```

#### InstructionsLoaded decision control

InstructionsLoaded hooks have no decision control. They cannot block or modify instruction loading. Use this event for audit logging, compliance tracking, or observability.

### UserPromptSubmit

Runs when the user submits a prompt, before Claude processes it. This allows you to add additional context based on the prompt/conversation, validate prompts, or block certain types of prompts.

#### UserPromptSubmit input

In addition to the [common input fields](#common-input-fields), UserPromptSubmit hooks receive the `prompt` field containing the text the user submitted.

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Write a function to calculate the factorial of a number"
}
```

#### UserPromptSubmit decision control

`UserPromptSubmit` hooks can control whether a user prompt is processed and add context. All [JSON output fields](#json-output) are available.

There are two ways to add context to the conversation on exit code 0:

* **Plain text stdout**: any non-JSON text written to stdout is added as context
* **JSON with `additionalContext`**: use the JSON format below for more control. The `additionalContext` field is added as context

Plain stdout is shown as hook output in the transcript. The `additionalContext` field is added more discretely.

To block a prompt, return a JSON object with `decision` set to `"block"`:

| Field               | Description                                                                                                            |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------- |
| `decision`          | `"block"` prevents the prompt from being processed and erases it from context. Omit to allow the prompt to proceed     |
| `reason`            | Shown to the user when `decision` is `"block"`. Not added to context                                                   |
| `additionalContext` | String added to Claude's context alongside the submitted prompt. See [Add context for Claude](#add-context-for-claude) |
| `sessionTitle`      | Sets the session title. Use to name sessions automatically based on the prompt content                                 |

```json theme={null}
{
  "decision": "block",
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "My additional context here",
    "sessionTitle": "My session title"
  }
}
```

<Note>
  The JSON format isn't required for simple use cases. To add context, you can print plain text to stdout with exit code 0. Use JSON when you need to
  block prompts or want more structured control.
</Note>

### UserPromptExpansion

Runs when a user-typed slash command expands into a prompt before reaching Claude. Use this to block specific commands from direct invocation, inject context for a particular skill, or log which commands users invoke. For example, a hook matching `deploy` can block `/deploy` unless an approval file is present, or a hook matching a review skill can append the team's review checklist as `additionalContext`.

This event covers the path `PreToolUse` does not: a `PreToolUse` hook matching the `Skill` tool fires only when Claude calls the tool, but typing `/skillname` directly bypasses `PreToolUse`. `UserPromptExpansion` fires on that direct path.

Matches on `command_name`. Leave the matcher empty to fire on every prompt-type slash command.

#### UserPromptExpansion input

In addition to the [common input fields](#common-input-fields), UserPromptExpansion hooks receive `expansion_type`, `command_name`, `command_args`, `command_source`, and the original `prompt` string. The `expansion_type` field is `slash_command` for skill and custom commands, or `mcp_prompt` for MCP server prompts.

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../00893aaf.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "UserPromptExpansion",
  "expansion_type": "slash_command",
  "command_name": "example-skill",
  "command_args": "arg1 arg2",
  "command_source": "plugin",
  "prompt": "/example-skill arg1 arg2"
}
```

#### UserPromptExpansion decision control

`UserPromptExpansion` hooks can block the expansion or add context. All [JSON output fields](#json-output) are available.

| Field               | Description                                                                                                           |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `decision`          | `"block"` prevents the slash command from expanding. Omit to allow it to proceed                                      |
| `reason`            | Shown to the user when `decision` is `"block"`                                                                        |
| `additionalContext` | String added to Claude's context alongside the expanded prompt. See [Add context for Claude](#add-context-for-claude) |

```json theme={null}
{
  "decision": "block",
  "reason": "This slash command is not available",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptExpansion",
    "additionalContext": "Additional context for this expansion"
  }
}
```

### PreToolUse

Runs after Claude creates tool parameters and before processing the tool call. Matches on tool name: `Bash`, `Edit`, `Write`, `Read`, `Glob`, `Grep`, `Agent`, `WebFetch`, `WebSearch`, `AskUserQuestion`, `ExitPlanMode`, and any [MCP tool names](#match-mcp-tools).

Use [PreToolUse decision control](#pretooluse-decision-control) to allow, deny, ask, or defer the tool call.

#### PreToolUse input

In addition to the [common input fields](#common-input-fields), PreToolUse hooks receive `tool_name`, `tool_input`, and `tool_use_id`. The `tool_input` fields depend on the tool:

##### Bash

Executes shell commands.

| Field               | Type    | Example            | Description                                   |
| :------------------ | :------ | :----------------- | :-------------------------------------------- |
| `command`           | string  | `"npm test"`       | The shell command to execute                  |
| `description`       | string  | `"Run test suite"` | Optional description of what the command does |
| `timeout`           | number  | `120000`           | Optional timeout in milliseconds              |
| `run_in_background` | boolean | `false`            | Whether to run the command in background      |

##### Write

Creates or overwrites a file.

| Field       | Type   | Example               | Description                        |
| :---------- | :----- | :-------------------- | :--------------------------------- |
| `file_path` | string | `"/path/to/file.txt"` | Absolute path to the file to write |
| `content`   | string | `"file content"`      | Content to write to the file       |

##### Edit

Replaces a string in an existing file.

| Field         | Type    | Example               | Description                        |
| :------------ | :------ | :-------------------- | :--------------------------------- |
| `file_path`   | string  | `"/path/to/file.txt"` | Absolute path to the file to edit  |
| `old_string`  | string  | `"original text"`     | Text to find and replace           |
| `new_string`  | string  | `"replacement text"`  | Replacement text                   |
| `replace_all` | boolean | `false`               | Whether to replace all occurrences |

##### Read

Reads file contents.

| Field       | Type   | Example               | Description                                |
| :---------- | :----- | :-------------------- | :----------------------------------------- |
| `file_path` | string | `"/path/to/file.txt"` | Absolute path to the file to read          |
| `offset`    | number | `10`                  | Optional line number to start reading from |
| `limit`     | number | `50`                  | Optional number of lines to read           |

##### Glob

Finds files matching a glob pattern.

| Field     | Type   | Example          | Description                                                            |
| :-------- | :----- | :--------------- | :--------------------------------------------------------------------- |
| `pattern` | string | `"**/*.ts"`      | Glob pattern to match files against                                    |
| `path`    | string | `"/path/to/dir"` | Optional directory to search in. Defaults to current working directory |

##### Grep

Searches file contents with regular expressions.

| Field         | Type    | Example          | Description                                                                           |
| :------------ | :------ | :--------------- | :------------------------------------------------------------------------------------ |
| `pattern`     | string  | `"TODO.*fix"`    | Regular expression pattern to search for                                              |
| `path`        | string  | `"/path/to/dir"` | Optional file or directory to search in                                               |
| `glob`        | string  | `"*.ts"`         | Optional glob pattern to filter files                                                 |
| `output_mode` | string  | `"content"`      | `"content"`, `"files_with_matches"`, or `"count"`. Defaults to `"files_with_matches"` |
| `-i`          | boolean | `true`           | Case insensitive search                                                               |
| `multiline`   | boolean | `false`          | Enable multiline matching                                                             |

##### WebFetch

Fetches and processes web content.

| Field    | Type   | Example                       | Description                          |
| :------- | :----- | :---------------------------- | :----------------------------------- |
| `url`    | string | `"https://example.com/api"`   | URL to fetch content from            |
| `prompt` | string | `"Extract the API endpoints"` | Prompt to run on the fetched content |

##### WebSearch

Searches the web.

| Field             | Type   | Example                        | Description                                       |
| :---------------- | :----- | :----------------------------- | :------------------------------------------------ |
| `query`           | string | `"react hooks best practices"` | Search query                                      |
| `allowed_domains` | array  | `["docs.example.com"]`         | Optional: only include results from these domains |
| `blocked_domains` | array  | `["spam.example.com"]`         | Optional: exclude results from these domains      |

##### Agent

Spawns a [subagent](/en/sub-agents).

| Field           | Type   | Example                    | Description                                  |
| :-------------- | :----- | :------------------------- | :------------------------------------------- |
| `prompt`        | string | `"Find all API endpoints"` | The task for the agent to perform            |
| `description`   | string | `"Find API endpoints"`     | Short description of the task                |
| `subagent_type` | string | `"Explore"`                | Type of specialized agent to use             |
| `model`         | string | `"sonnet"`                 | Optional model alias to override the default |

##### AskUserQuestion

Asks the user one to four multiple-choice questions.

| Field       | Type   | Example                                                                                                            | Description                                                                                                                                                                                      |
| :---------- | :----- | :----------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `questions` | array  | `[{"question": "Which framework?", "header": "Framework", "options": [{"label": "React"}], "multiSelect": false}]` | Questions to present, each with a `question` string, short `header`, `options` array, and optional `multiSelect` flag                                                                            |
| `answers`   | object | `{"Which framework?": "React"}`                                                                                    | Optional. Maps question text to the selected option label. Multi-select answers join labels with commas. Claude does not set this field; supply it via `updatedInput` to answer programmatically |

##### ExitPlanMode

Presents a plan and asks the user to approve it before Claude leaves [plan mode](/en/permission-modes#analyze-before-you-edit-with-plan-mode). Claude writes the plan to a file on disk before calling the tool, so the literal `tool_input` from the model only carries `allowedPrompts`. Claude Code injects the plan content and file path before passing the input to hooks.

| Field            | Type   | Example                                     | Description                                                                                                                                             |
| :--------------- | :----- | :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `plan`           | string | `"## Refactor auth\n1. Extract..."`         | Plan content in Markdown. Injected from the plan file on disk                                                                                           |
| `planFilePath`   | string | `"/Users/.../plans/refactor-auth.md"`       | Path to the plan file. Injected                                                                                                                         |
| `allowedPrompts` | array  | `[{"tool": "Bash", "prompt": "run tests"}]` | Optional. Prompt-based permissions Claude is requesting to implement the plan, each with a `tool` name and a `prompt` describing the category of action |

In `PostToolUse`, `tool_response` is an object with `plan` and `filePath` fields holding the approved plan, plus internal status flags. Read `tool_response.plan` for the plan content rather than re-reading the file from disk.

#### PreToolUse decision control

`PreToolUse` hooks can control whether a tool call proceeds. Unlike other hooks that use a top-level `decision` field, PreToolUse returns its decision inside a `hookSpecificOutput` object. This gives it richer control:

| Field                       | Description                                                                                                                                                                                                                                                                                        |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `permissionDecision`        | One of `"allow"`, `"deny"`, `"ask"`, or `"defer"`. The decision to allow or deny the tool call, or ask the user to decide, or defer to another hook or the configured [permission rules](/en/permissions)                                                                                          |
| `permissionDecisionReason`  | Human-readable explanation for the decision, shown to the user when the decision is `"deny"` or `"ask"`                                                                                                                                                                                           |
| `permissionApplyRules`      | Object or array of objects for the tool. Populates permission rules automatically so you don't have to ask the user repeatedly. See [Permissions](/en/permissions) for the schema                                                                                                                   |
| `updatedInput`              | Object with any `tool_input` fields you want to override, for example `"command": "npm run lint --fix"`                                                                                                                                                                                           |
| `runAsynchronously`         | If `true`, runs the tool in the background without blocking the agentic loop. Useful for long-running operations like CI builds. Implies `permissionDecision: "allow"`. The tool executes and its stdout goes to Claude, but execution does not block. Claude Code does not wait for tool completion |
| `additionalContext`         | String added to Claude's context, shown alongside the tool result. Use for environment state Claude should know about                                                                                                                                                                              |

This example shows a hook that denies database writes and applies an auto-approval rule for read-only commands:

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Database writes are not allowed in this workspace",
    "permissionApplyRules": [
      {
        "pattern": "Bash(SELECT *)",
        "behavior": "allow"
      }
    ]
  }
}
```

If you want Claude to retry a deferred tool call, set `permissionDecision` to `"defer"` without providing a decision:

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "defer"
  }
}
```

### PermissionRequest

Runs when Claude Code is about to display a [permission dialog](/en/permissions) to the user. Use this to grant or deny tool calls programmatically based on context, prevent interrupting the user with prompts, or apply permission rules automatically. Matches on `tool_name`.

#### PermissionRequest input

In addition to the [common input fields](#common-input-fields), PermissionRequest hooks receive `tool_name`, `tool_input`, `permission_decision_status`, and `permission_rules`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "permission_mode": "default",
  "hook_event_name": "PermissionRequest",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm publish"
  },
  "permission_decision_status": "undecided",
  "permission_rules": [
    {
      "pattern": "Edit(*.md)",
      "behavior": "allow"
    }
  ]
}
```

#### PermissionRequest decision control

PermissionRequest hooks return a decision inside `hookSpecificOutput`. Unlike PreToolUse, this hook's decision is binary: allow or deny. You cannot ask the user or defer.

| Field                  | Description                                                                                                                                                                       |
| :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `decision.behavior`    | Either `"allow"` or `"deny"`. Omit to let Claude Code show the permission dialog to the user                                                                                       |
| `decision.rules`       | Optional [permission rule](/en/permissions) object or array to apply automatically, so the user is not prompted again on matching calls                                            |
| `updatedInput`         | Object with any `tool_input` fields you want to override. The tool receives the updated input when you allow it                                                                    |
| `additionalContext`    | String added to Claude's context when you allow a tool call. Use for environment state or context Claude should know about                                                        |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow",
      "rules": {
        "pattern": "Bash(npm publish)",
        "behavior": "allow"
      },
      "updatedInput": {
        "command": "npm publish --dry-run"
      }
    },
    "additionalContext": "Publishing to npm registry..."
  }
}
```

### PermissionDenied

Runs after a tool call is denied by the auto mode classifier. The hook runs asynchronously and does not block execution. Use it to decide whether the model should retry the tool call, or to log denials for audit purposes.

The matcher runs against `tool_name`. [Exit codes](#exit-code-output) are ignored for this event. Return JSON with the [hookSpecificOutput](#permissiondenied-decision-control) fields below.

#### PermissionDenied input

In addition to the [common input fields](#common-input-fields), PermissionDenied hooks receive `tool_name`, `tool_input`, and `denial_reason`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "permission_mode": "auto",
  "hook_event_name": "PermissionDenied",
  "tool_name": "Bash",
  "tool_input": {
    "command": "rm -rf /"
  },
  "denial_reason": "Destructive shell command"
}
```

#### PermissionDenied decision control

Exit code and stderr are ignored for this event. Return JSON to tell the model whether it may retry the denied tool call:

| Field   | Description                                                   |
| :------ | :------------------------------------------------------------ |
| `retry` | If `true`, tells the model it may retry the denied tool call. |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionDenied",
    "retry": true
  }
}
```

### PostToolUse

Runs after a tool call succeeds. Matches on tool name. Use this to verify tool output, inject context for Claude, validate file changes, or run side-effect operations like linting or security scanning.

#### PostToolUse input

In addition to the [common input fields](#common-input-fields), PostToolUse hooks receive `tool_name`, `tool_input`, `tool_response`, and `tool_use_id`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "permission_mode": "default",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/Users/my-project/index.js",
    "content": "console.log('Hello world')"
  },
  "tool_response": "Successfully wrote to file /Users/my-project/index.js"
}
```

#### PostToolUse decision control

`PostToolUse` hooks can block further execution and add context. Like `UserPromptSubmit`, there are two ways to add context:

* **Plain text stdout**: any text written to stdout on exit 0 is added as context
* **JSON with `additionalContext`**: use the JSON format for more control

| Field               | Description                                                                                                            |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------- |
| `decision`          | `"block"` stops the agentic loop and returns to the user. Omit to continue                                              |
| `reason`            | Shown to the user when `decision` is `"block"`                                                                         |
| `additionalContext` | String added to Claude's context alongside the tool result. See [Add context for Claude](#add-context-for-claude)     |

```json theme={null}
{
  "decision": "block",
  "reason": "Linting failed, please fix errors",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "File syntax is valid"
  }
}
```

### PostToolUseFailure

Runs after a tool call fails. Matches on tool name. Use this to retry failed operations, provide guidance to Claude on how to recover, or trigger alerting mechanisms.

#### PostToolUseFailure input

In addition to the [common input fields](#common-input-fields), PostToolUseFailure hooks receive `tool_name`, `tool_input`, `tool_response`, and `tool_use_id`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "permission_mode": "default",
  "hook_event_name": "PostToolUseFailure",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm install"
  },
  "tool_response": "npm ERR! code EACCES\nnpm ERR! syscall mkdir"
}
```

#### PostToolUseFailure decision control

`PostToolUseFailure` hooks can block further execution and add context:

| Field               | Description                                                                                                           |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `decision`          | `"block"` stops the agentic loop. Omit to continue                                                                     |
| `reason`            | Shown to the user when `decision` is `"block"`                                                                        |
| `additionalContext` | String added to Claude's context alongside the failed tool result. Use to guide Claude toward recovery steps           |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUseFailure",
    "additionalContext": "npm cache clear --force might resolve this issue"
  }
}
```

### PostToolBatch

Runs after a batch of parallel tool calls completes, before the next model call. Matches on tool name. Use this to validate that related tool calls succeeded together, or to prevent the model from proceeding until certain conditions are met.

#### PostToolBatch input

In addition to the [common input fields](#common-input-fields), PostToolBatch hooks receive a `batch` field containing an array of tool call results. Each entry has `tool_name`, `tool_input`, `success`, and `response`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "permission_mode": "default",
  "hook_event_name": "PostToolBatch",
  "batch": [
    {
      "tool_name": "Write",
      "tool_input": { "file_path": "/Users/my-project/file1.txt", "content": "..." },
      "success": true,
      "response": "Successfully wrote to file..."
    },
    {
      "tool_name": "Bash",
      "tool_input": { "command": "npm test" },
      "success": false,
      "response": "Test failed..."
    }
  ]
}
```

#### PostToolBatch decision control

PostToolBatch hooks can block execution:

| Field               | Description                                                                                                  |
| :------------------ | :----------------------------------------------------------------------------------------------------------- |
| `decision`          | `"block"` stops the agentic loop before the next model call. Omit to continue                                 |
| `reason`            | Shown to the user when `decision` is `"block"`                                                               |
| `additionalContext` | String added to Claude's context. Useful for describing overall batch status                                 |

```json theme={null}
{
  "decision": "block",
  "reason": "Test suite must pass before proceeding",
  "hookSpecificOutput": {
    "hookEventName": "PostToolBatch",
    "additionalContext": "4 tests passed, 2 tests failed"
  }
}
```

### Stop

Runs when Claude finishes responding. Use this to trigger deployment, log conversation summaries, or validate the final state of your codebase. For error cases, use [StopFailure](#stopfailure) instead.

#### Stop input

In addition to the [common input fields](#common-input-fields), Stop hooks receive a `response_summary` field:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "permission_mode": "default",
  "hook_event_name": "Stop",
  "response_summary": "Added user authentication to the application..."
}
```

#### Stop decision control

Stop hooks can prevent Claude from stopping by returning exit code 2 or a blocking decision. This keeps the conversation going:

| Field    | Description                                                                    |
| :------- | :----------------------------------------------------------------------------- |
| `decision` | `"block"` prevents Claude from stopping and continues the conversation. Omit to allow Stop |
| `reason` | Message shown to the user and Claude when `decision` is `"block"`              |

```json theme={null}
{
  "decision": "block",
  "reason": "Tests are failing, please run the test suite"
}
```

### StopFailure

Runs when a turn ends due to an API error or other failure condition. Unlike [Stop](#stop), this event represents a failure state. The hook runs asynchronously and output is ignored. Use it for error logging or alerting.

Matches on `error_type`: `rate_limit`, `authentication_failed`, `oauth_org_not_allowed`, `billing_error`, `invalid_request`, `server_error`, `max_output_tokens`, or `unknown`.

#### StopFailure input

In addition to the [common input fields](#common-input-fields), StopFailure hooks receive `error_type` and `error_message`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "StopFailure",
  "error_type": "rate_limit",
  "error_message": "Rate limit exceeded. Please try again later."
}
```

#### StopFailure decision control

StopFailure hooks have no decision control. Exit code and output are ignored. Use this event for logging only.

### SubagentStart

Runs when a subagent is spawned. Use this to inject context into the subagent's initial state, log subagent launches, or apply organizational policies.

#### SubagentStart input

In addition to the [common input fields](#common-input-fields), SubagentStart hooks receive `agent_id`, `agent_type`, and `prompt`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "SubagentStart",
  "agent_id": "subagent-12345",
  "agent_type": "Explore",
  "prompt": "Find all API endpoints in the codebase"
}
```

#### SubagentStart decision control

SubagentStart hooks can add context. Plain stdout is treated as context:

| Field               | Description                                                                                                           |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `additionalContext` | String added to the subagent's context before it starts working. Useful for passing requirements or constraints       |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Use the Explore agent to thoroughly investigate the codebase..."
  }
}
```

### SubagentStop

Runs when a subagent finishes. Use this for logging, cleanup, or to prevent the subagent from returning control to the parent session.

Matches on `agent_type`. The value is the subagent type, like `"Explore"` or a custom agent name.

#### SubagentStop input

In addition to the [common input fields](#common-input-fields), SubagentStop hooks receive `agent_id`, `agent_type`, and `response_summary`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "SubagentStop",
  "agent_id": "subagent-12345",
  "agent_type": "Explore",
  "response_summary": "Found 12 API endpoints..."
}
```

#### SubagentStop decision control

SubagentStop hooks can prevent the subagent from stopping:

| Field    | Description                                                                                               |
| :------- | :-------------------------------------------------------------------------------------------------------- |
| `decision` | `"block"` prevents the subagent from stopping and continues its work. Omit to let it finish              |
| `reason` | Message shown to Claude when `decision` is `"block"`                                                      |

```json theme={null}
{
  "decision": "block",
  "reason": "Testing found critical issues. Please continue investigation"
}
```

### TaskCreated

Runs when a task is being created via the `TaskCreate` tool. Use this to validate task parameters or prevent certain tasks from being created.

#### TaskCreated input

In addition to the [common input fields](#common-input-fields), TaskCreated hooks receive `task_input` with the fields from the TaskCreate tool call:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "TaskCreated",
  "task_input": {
    "name": "Deploy to production",
    "description": "Deploy the latest build"
  }
}
```

#### TaskCreated decision control

TaskCreated hooks can prevent task creation:

| Field    | Description                                                                                  |
| :------- | :------------------------------------------------------------------------------------------- |
| `decision` | `"block"` rolls back the task creation. Omit to allow it                                      |
| `reason` | Message shown to the user when `decision` is `"block"`                                        |

```json theme={null}
{
  "decision": "block",
  "reason": "Task names must follow the format: [TEAM]-[TYPE]-[NUMBER]"
}
```

### TaskCompleted

Runs when a task is being marked as completed. Use this to verify task requirements before allowing completion.

#### TaskCompleted input

In addition to the [common input fields](#common-input-fields), TaskCompleted hooks receive `task_id` and `task_input`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "TaskCompleted",
  "task_id": "task-12345",
  "task_input": {
    "name": "Deploy to production",
    "description": "Deploy the latest build"
  }
}
```

#### TaskCompleted decision control

TaskCompleted hooks can prevent task completion:

| Field    | Description                                                                                 |
| :------- | :------------------------------------------------------------------------------------------- |
| `decision` | `"block"` prevents the task from being marked completed. Omit to allow it                    |
| `reason` | Message shown to the user when `decision` is `"block"`                                       |

```json theme={null}
{
  "decision": "block",
  "reason": "All tests must pass before marking tasks complete"
}
```

### TeammateIdle

Runs when an [agent team](/en/agent-teams) teammate is about to go idle. Use this to prevent teammates from becoming idle, extend their work, or trigger handoffs to other team members.

#### TeammateIdle input

In addition to the [common input fields](#common-input-fields), TeammateIdle hooks receive `teammate_id` and `teammate_role`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "TeammateIdle",
  "teammate_id": "teammate-12345",
  "teammate_role": "code_reviewer"
}
```

#### TeammateIdle decision control

TeammateIdle hooks can prevent a teammate from going idle:

| Field    | Description                                                                                     |
| :------- | :---------------------------------------------------------------------------------------------- |
| `decision` | `"block"` (via exit code 2 or JSON) prevents the teammate from going idle. Omit to let it idle |
| `reason` | Message shown to Claude when blocking. Exit code 2 uses stderr, JSON uses this field            |

### ConfigChange

Runs when a configuration file changes during a session. Use this to validate configuration changes, reload application state, or prevent certain configuration modifications.

Matches on `config_source`: `user_settings`, `project_settings`, `local_settings`, `policy_settings`, or `skills`.

#### ConfigChange input

In addition to the [common input fields](#common-input-fields), ConfigChange hooks receive `config_source` and `config_path`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "ConfigChange",
  "config_source": "project_settings",
  "config_path": "/Users/my-project/.claude/settings.json"
}
```

#### ConfigChange decision control

ConfigChange hooks can prevent configuration changes (except for policy settings):

| Field    | Description                                                                                    |
| :------- | :--------------------------------------------------------------------------------------------- |
| `decision` | `"block"` prevents the configuration change from taking effect. Omit to allow it               |
| `reason` | Message shown to the user when `decision` is `"block"`                                         |

```json theme={null}
{
  "decision": "block",
  "reason": "Configuration changes are not allowed in production"
}
```

### CwdChanged

Runs when the working directory changes, for example when Claude executes a `cd` command. Use this to manage environment setup based on the new directory, or to prevent changing to certain directories.

#### CwdChanged input

In addition to the [common input fields](#common-input-fields), CwdChanged hooks receive a new `cwd` field (in addition to the one in common fields). The top-level `cwd` is the new directory; you can infer the old directory from the previous event.

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project/subdir",
  "hook_event_name": "CwdChanged"
}
```

#### CwdChanged decision control

CwdChanged hooks have no matchers and always fire. The hooks have access to `CLAUDE_ENV_FILE` to persist environment variables. See [Persist environment variables](#persist-environment-variables) for how to use it.

<Note>
  CwdChanged is a good place to integrate with tools like direnv. A hook can read a `.envrc` file from the new directory, execute it, and write the resulting environment variables to `CLAUDE_ENV_FILE`.
</Note>

### FileChanged

Runs when a watched file changes on disk. Use this to reload application state, run tests, or trigger other reactive behavior based on file changes.

#### FileChanged input

In addition to the [common input fields](#common-input-fields), FileChanged hooks receive `file_path`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "FileChanged",
  "file_path": "/Users/my-project/.env"
}
```

#### FileChanged matcher

FileChanged does not follow the standard matcher rules. The `matcher` field holds a literal filename or pipe-separated list of filenames to watch, not a regex or exact string match:

```json theme={null}
{
  "hooks": {
    "FileChanged": [
      {
        "matcher": ".env|.envrc|package.json",
        "hooks": [
          {
            "type": "command",
            "command": "./reload-config.sh"
          }
        ]
      }
    ]
  }
}
```

#### FileChanged decision control

FileChanged hooks have access to `CLAUDE_ENV_FILE` and can add context via `additionalContext`. Exit code 2 shows stderr to the user.

### WorktreeCreate

Runs when a worktree is being created via `--worktree` or `isolation: "worktree"`. Use this to customize the worktree creation process or to enforce organization-specific worktree setup.

#### WorktreeCreate input

In addition to the [common input fields](#common-input-fields), WorktreeCreate hooks receive `worktree_name` and `source_worktree`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "WorktreeCreate",
  "worktree_name": "feature-branch",
  "source_worktree": "/Users/my-project/.git"
}
```

#### WorktreeCreate decision control

WorktreeCreate hooks replace the default git worktree creation behavior. The hook must print the path to the created worktree on stdout (exit code 0), or fail with any non-zero exit code to abort creation:

**Command hook:**

```bash theme={null}
#!/bin/bash
# Create a worktree and return its path
git worktree add --detach /tmp/worktree-name
echo "/tmp/worktree-name"
exit 0
```

**HTTP hook:**

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "WorktreeCreate",
    "worktreePath": "/tmp/worktree-name"
  }
}
```

If the hook fails or returns no path, worktree creation fails.

### WorktreeRemove

Runs when a worktree is being removed, either at session exit or when a subagent finishes. The hook runs asynchronously and failures are logged in debug mode only.

#### WorktreeRemove input

In addition to the [common input fields](#common-input-fields), WorktreeRemove hooks receive `worktree_path`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "WorktreeRemove",
  "worktree_path": "/tmp/worktree-name"
}
```

#### WorktreeRemove decision control

WorktreeRemove hooks have no decision control. Use them for cleanup.

### PreCompact

Runs before context compaction. Use this to audit context before compaction, or to prevent compaction in certain situations.

Matches on `trigger`: `manual` or `auto`.

#### PreCompact input

In addition to the [common input fields](#common-input-fields), PreCompact hooks receive `trigger`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "PreCompact",
  "trigger": "auto"
}
```

#### PreCompact decision control

PreCompact hooks can block compaction:

| Field    | Description                                                          |
| :------- | :------------------------------------------------------------------- |
| `decision` | `"block"` prevents context compaction. Omit to allow it              |
| `reason` | Message shown to the user when `decision` is `"block"`               |

```json theme={null}
{
  "decision": "block",
  "reason": "Cannot compact context during active session"
}
```

### PostCompact

Runs after context compaction completes. Use this to verify the compacted context or trigger side effects.

Matches on `trigger`: `manual` or `auto`.

#### PostCompact input

In addition to the [common input fields](#common-input-fields), PostCompact hooks receive `trigger`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "PostCompact",
  "trigger": "manual"
}
```

#### PostCompact decision control

PostCompact hooks have no decision control.

### Notification

Runs when Claude Code sends a notification. Use this to log notifications, integrate with external notification systems, or filter which notifications are displayed.

Matches on `notification_type`: `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`, `elicitation_complete`, `elicitation_response`, and others.

#### Notification input

In addition to the [common input fields](#common-input-fields), Notification hooks receive `notification_type` and `notification_message`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "Notification",
  "notification_type": "permission_prompt",
  "notification_message": "Claude wants to run: Bash(npm test)"
}
```

#### Notification decision control

Notification hooks have no decision control. Use them for logging or external integrations.

### Elicitation

Runs when an MCP server requests user input during a tool call. Use this to provide answers programmatically without user interaction, or to deny elicitation requests.

Matches on the MCP server name.

#### Elicitation input

In addition to the [common input fields](#common-input-fields), Elicitation hooks receive `server_name`, `request_id`, and `form`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "Elicitation",
  "server_name": "github",
  "request_id": "req-12345",
  "form": {
    "fields": [
      {
        "name": "token",
        "label": "GitHub Token",
        "type": "text"
      }
    ]
  }
}
```

#### Elicitation decision control

Elicitation hooks can accept or decline the elicitation, or provide form field values programmatically:

| Field          | Description                                                                                                |
| :------------- | :--------------------------------------------------------------------------------------------------------- |
| `action`       | One of `"accept"` (provide form values), `"decline"` (refuse the request), or `"cancel"` (cancel the tool call) |
| `content`      | Object mapping field names to values when `action` is `"accept"`, for example `{"token": "ghp_xxxx"}`     |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "Elicitation",
    "action": "accept",
    "content": {
      "token": "ghp_xxxx"
    }
  }
}
```

### ElicitationResult

Runs after a user responds to an MCP elicitation, before the response is sent back to the server. Use this to validate user input, modify field values, or prevent sending responses.

Matches on the MCP server name.

#### ElicitationResult input

In addition to the [common input fields](#common-input-fields), ElicitationResult hooks receive `server_name`, `request_id`, `form`, and `result`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "ElicitationResult",
  "server_name": "github",
  "request_id": "req-12345",
  "form": { "fields": [...] },
  "result": {
    "action": "accept",
    "content": {
      "token": "ghp_xxxx"
    }
  }
}
```

#### ElicitationResult decision control

ElicitationResult hooks can modify the response before it reaches the server:

| Field     | Description                                                                                                        |
| :-------- | :----------------------------------------------------------------------------------------------------------------- |
| `action`  | One of `"accept"`, `"decline"`, or `"cancel"`. Omit to use the user's original response                           |
| `content` | Object mapping field names to values when `action` is `"accept"`. Omit to use the user's original values           |

```json theme={null}
{
  "hookSpecificOutput": {
    "hookEventName": "ElicitationResult",
    "action": "accept",
    "content": {
      "token": "ghp_yyyy"
    }
  }
}
```

### SessionEnd

Runs when a session terminates. Use this for logging, cleanup, saving conversation history, or triggering post-session workflows.

Matches on `end_reason`: `clear`, `resume`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, or `other`.

#### SessionEnd input

In addition to the [common input fields](#common-input-fields), SessionEnd hooks receive `end_reason`:

```json theme={null}
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../transcript.jsonl",
  "cwd": "/Users/my-project",
  "hook_event_name": "SessionEnd",
  "end_reason": "clear"
}
```

#### SessionEnd decision control

SessionEnd hooks have no decision control. Use them for logging and cleanup.

## Advanced hook features

### Async hooks

Command hooks can run in the background without blocking Claude Code's agentic loop. Set `async: true` to launch a hook and continue immediately, or `asyncRewake: true` to launch a hook and wake Claude on exit code 2.

```json theme={null}
{
  "type": "command",
  "command": "/path/to/hook.sh",
  "args": [],
  "async": true
}
```

### Prompt-based hooks

Hooks can delegate decisions to a Claude model by setting `type: "prompt"`. The model reads the hook input and returns a yes/no decision:

```json theme={null}
{
  "type": "prompt",
  "prompt": "Should this tool call be allowed? Tool: $ARGUMENTS",
  "timeout": 30
}
```

### Agent-based hooks

Hooks can spawn subagents that use tools to verify conditions. Agent hooks are experimental:

```json theme={null}
{
  "type": "agent",
  "prompt": "Verify that tests pass",
  "timeout": 60
}
```