---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-worktrees.md
tags: [claude-code, official-docs, worktree, isolation, parallel, git, hooks]
---

# Source: Run parallel sessions with worktrees

## Summary
Official Anthropic doc on **worktree isolation** in [[claude-code]] — separate git checkouts for parallel sessions so edits never collide. Canonical spec of the `--worktree`/`-w` flag, `.worktreeinclude` for copying gitignored files (like `.env`), `isolation: worktree` for subagents, cleanup behavior, and `WorktreeCreate`/`WorktreeRemove` hooks for non-git VCS. **The file-isolation primitive that powers [[claude-code-agent-view|agent view]]'s auto-worktree behavior** for background sessions that edit files.

## CLI quickstart

```bash
claude --worktree feature-auth   # → .claude/worktrees/feature-auth/ on branch worktree-feature-auth
claude --worktree bugfix-123     # second isolated session
claude --worktree                # auto-generated name like "bright-running-fox"
claude --worktree "#1234"        # branches from PR #1234, → .claude/worktrees/pr-1234
```

Or in-session: ask Claude to "work in a worktree" → uses `EnterWorktree` tool.

> [!tip]
> Add `.claude/worktrees/` to `.gitignore` so worktree contents don't appear as untracked files in main checkout.

## Base branch selection

Default: branches from `origin/HEAD` (clean tree matching remote). If no remote or fetch fails: falls back to local `HEAD`.

```json
{
  "worktree": {
    "baseRef": "head"
  }
}
```

`baseRef: "head"` makes new worktrees carry unpushed commits + feature-branch state — **useful when isolating subagents that need to operate on in-progress work**. Accepts only `"fresh"` or `"head"`, not arbitrary git refs.

## `.worktreeinclude` — copy gitignored files

A worktree is a fresh checkout, so `.env` files aren't present. Add `.worktreeinclude` (uses `.gitignore` syntax) to copy them automatically:

```text
.env
.env.local
config/secrets.json
```

Only files that match a pattern **AND are gitignored** are copied — tracked files never duplicated. Applies to `--worktree` sessions, subagent worktrees, and desktop-app parallel sessions.

## Subagent worktree isolation

Two ways to give a [[source-claude-code-subagents-docs|subagent]] its own worktree:

1. Ad-hoc: ask Claude to "use worktrees for your agents"
2. Permanent on custom subagent: `isolation: worktree` in frontmatter

Each subagent gets a temporary worktree, **auto-removed when subagent finishes without changes**.

## Cleanup behavior on session exit

| State | What happens |
| :--- | :--- |
| No uncommitted changes, no untracked files, no new commits | Worktree + branch removed automatically (or prompt if session is named) |
| Any uncommitted/untracked/unpushed | Claude prompts to keep or remove. Remove = discard everything |
| Non-interactive runs (`--worktree` + `-p`) | NOT auto-cleaned — no exit prompt. Use `git worktree remove` |

Subagent worktrees orphaned by crashes are removed at startup once older than `cleanupPeriodDays`, provided clean state. **Worktrees created with `--worktree` are never removed by this sweep.**

## Non-git version control (SVN/Perforce/Mercurial)

Configure `WorktreeCreate` + `WorktreeRemove` hooks for custom creation/cleanup. Because the hook replaces default git behavior, **`.worktreeinclude` is NOT processed** when using `--worktree` with a custom VCS hook — copy local config files inside hook script instead.

Example SVN `WorktreeCreate`:

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

## Manual worktrees with `git worktree`

For full control over location + branch, use git directly — Claude Code starts in any directory. Useful when you want worktree outside the repo, or to check out specific existing branch:

```bash
git worktree add ../project-feature-a -b feature-a
cd ../project-feature-a && claude
```

Remember to initialize dev env in each worktree (dependencies, venv, etc.).

## Workspace trust gotcha

Before using `--worktree` in a directory for the first time, **accept workspace trust dialog by running `claude` once in that directory**. Otherwise `--worktree` exits with an error (even when combined with `-p`).

## Connection to other parallel primitives

- **Subagents** → file isolation: `isolation: worktree` frontmatter
- **[[claude-code-agent-view|Agent view]]** → automatically moves each dispatched session into its own worktree when it needs to edit files (under `.claude/worktrees/`)
- **[[source-claude-code-agent-teams-docs|Agent teams]]** → DO NOT auto-isolate teammates in worktrees. **You partition work manually** so teammates own different files.
- **Desktop app** → creates worktree for every new session automatically

## Connections
- Related: [[claude-code]], [[source-claude-code-agents-overview]], [[source-claude-code-subagents-docs]], [[claude-code-agent-view]], [[source-claude-code-agent-teams-docs]], [[forked-agent-pattern]], [[claude-code-sandboxing]], [[ralph-wiggum]]
- The file-isolation primitive [[ralph-wiggum|Ralph]] AFK loops should layer on top of — combined with [[claude-code-sandboxing|sandboxing]] this is the AFK safety stack
- Closes a gap in our existing [[claude-code-agent-view]] coverage which mentioned worktrees but didn't document the standalone flag

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-worktrees.md | Initial creation from official worktrees docs |
