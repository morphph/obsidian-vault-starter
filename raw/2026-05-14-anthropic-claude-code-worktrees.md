# Claude Code Official Docs — Run parallel sessions with worktrees

Captured 2026-05-14 from https://code.claude.com/docs/en/worktrees.md

> Isolate parallel Claude Code sessions in separate git worktrees so changes don't collide. Covers the `--worktree` flag, subagent isolation, `.worktreeinclude`, cleanup, and non-git VCS hooks.

A git worktree is a separate working directory with its own files and branch, sharing the same repository history and remote as your main checkout. Running each Claude Code session in its own worktree means edits in one session never touch files in another.

This page covers worktree isolation in the CLI. Everything below assumes a git repository. For other version control systems, see [Non-git version control](#non-git-version-control). The desktop app creates a worktree for every new session automatically.

Worktrees are one of several ways to run Claude in parallel. They isolate file edits, while subagents and agent teams coordinate the work itself.

## Start Claude in a worktree

Pass `--worktree` or `-w` to create an isolated worktree and start Claude in it. By default, the worktree is created under `.claude/worktrees/<value>/` at your repository root, on a new branch named `worktree-<value>`:

```bash
claude --worktree feature-auth
```

Run again with different name for second isolated session:

```bash
claude --worktree bugfix-123
```

Omit the name → Claude generates one such as `bright-running-fox`:

```bash
claude --worktree
```

Ask Claude to "work in a worktree" during a session, and it will create one with the `EnterWorktree` tool.

Before using `--worktree` in a directory for the first time, accept the workspace trust dialog by running `claude` once in that directory.

> [!tip]
> Add `.claude/worktrees/` to your `.gitignore` so worktree contents don't appear as untracked files in your main checkout.

### Choose the base branch

Worktrees branch from your repository's default branch, `origin/HEAD`, so they start from a clean tree matching the remote. If no remote is configured or the fetch fails, the worktree falls back to your current local `HEAD`.

To always branch from local `HEAD` instead, set `worktree.baseRef` to `"head"` in settings:

```json
{
  "worktree": {
    "baseRef": "head"
  }
}
```

Setting `baseRef` to `"head"` makes new worktrees carry your unpushed commits and feature-branch state. Useful when isolating subagents that need to operate on in-progress work. The setting accepts only `"fresh"` or `"head"`.

To branch from a specific pull request:

```bash
claude --worktree "#1234"
```

Claude Code fetches `pull/<number>/head` from `origin` and creates the worktree at `.claude/worktrees/pr-<number>`.

For full control over worktree creation, configure a `WorktreeCreate` hook.

## Copy gitignored files into worktrees

A worktree is a fresh checkout, so untracked files like `.env` from your main repository are not present. To copy them automatically, add a `.worktreeinclude` file to your project root.

The file uses `.gitignore` syntax. Only files that match a pattern AND are also gitignored are copied.

```text
.env
.env.local
config/secrets.json
```

This applies to worktrees created with `--worktree`, subagent worktrees, and parallel sessions in the desktop app.

## Isolate subagents with worktrees

Ask Claude to "use worktrees for your agents", or set it permanently on a custom subagent by adding `isolation: worktree` to the frontmatter. Each subagent gets a temporary worktree that is removed automatically when the subagent finishes without changes.

## Clean up worktrees

When you exit a worktree session, cleanup depends on whether you made changes:

* **No uncommitted changes, no untracked files, no new commits**: worktree and branch removed automatically. If session has a name, Claude prompts instead.
* **Uncommitted changes, untracked files, or new commits exist**: Claude prompts you to keep or remove. Removing deletes worktree directory and branch, discarding any uncommitted changes.
* **Non-interactive runs**: worktrees created with `--worktree` alongside `-p` are not cleaned up automatically. Remove with `git worktree remove`.

Subagent worktrees orphaned by a crash are removed at startup once they're older than your `cleanupPeriodDays` setting, provided no uncommitted changes / untracked files / unpushed commits. Worktrees created with `--worktree` are never removed by this sweep.

## Manage worktrees manually

For full control over worktree location and branch configuration, create worktrees with Git directly:

```bash
git worktree add ../project-feature-a -b feature-a
git worktree add ../project-bugfix bugfix-123
cd ../project-feature-a && claude
git worktree list
git worktree remove ../project-feature-a
```

Remember to initialize your development environment in each new worktree.

## Non-git version control

For SVN, Perforce, Mercurial, configure `WorktreeCreate` and `WorktreeRemove` hooks to provide custom creation and cleanup logic. Because the hook replaces the default git behavior, `.worktreeinclude` is not processed when you use `--worktree`. Copy any local configuration files inside your hook script instead.

Example SVN `WorktreeCreate` hook:

```json
{
  "hooks": {
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'NAME=$(jq -r .name); DIR=\"$HOME/.claude/worktrees/$NAME\"; svn checkout https://svn.example.com/repo/trunk \"$DIR\" >&2 && echo \"$DIR\"'"
          }
        ]
      }
    ]
  }
}
```

## See also

* Subagents: delegate work to isolated agents within a session
* Agent teams: coordinate multiple Claude sessions automatically
* Manage sessions: name, resume, and switch between conversations
* Desktop parallel sessions: worktree-backed sessions in the desktop app
