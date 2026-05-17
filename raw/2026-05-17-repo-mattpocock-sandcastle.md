# mattpocock/sandcastle

**Source:** https://github.com/mattpocock/sandcastle
**Author/Org:** Matt Pocock (mattpocock) / published under @ai-hero/sandcastle
**Stars:** 4,465 | **Forks:** 467 | **Language:** TypeScript | **Last updated:** 2026-05-17
**Fetch method:** GitHub Deep Scan (gh CLI)
**Fetched:** 2026-05-17

## What It Does

> "A TypeScript library for orchestrating AI coding agents in isolated sandboxes."

The framework Matt built for running AFK coding agents reliably. Three-step model:

1. You invoke agents with a single `sandcastle.run()`
2. Sandcastle handles sandboxing with a configurable branch strategy
3. Commits made on the branches get merged back

Provider-agnostic — ships with Docker, Podman, Vercel sandbox providers (Firecracker microVMs cloud-side). Custom providers via `createBindMountSandboxProvider` / `createIsolatedSandboxProvider`.

Three use cases stated: parallelizing multiple AFK agents, building review pipelines, orchestrating own agents.

## Install

```bash
npm install --save-dev @ai-hero/sandcastle
npx sandcastle init    # scaffolds .sandcastle/ with main.ts, prompt.md, env example
npx tsx .sandcastle/main.ts
```

## Core API

```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-7"),  // can pass effort: "high"
  sandbox: docker(),                     // or podman(), vercel(), noSandbox()
  promptFile: ".sandcastle/prompt.md",
});
```

Returns `{ iterations, commits, branch, stdout, completionSignal, logFilePath }`.

## Key Options (excerpt — full list very long)

- `agent: claudeCode(model, { effort })` — agent provider
- `sandbox: docker({ imageName, mounts, env, network })` — sandbox provider with mount/network config
- `cwd` — host repo (default `process.cwd()`)
- `branchStrategy: { type: "head" | "branch" | "merge-to-head" }` — how changes relate to branches
- `prompt` OR `promptFile` (mutually exclusive)
- `promptArgs: { ISSUE_NUMBER: "42" }` — `{{KEY}}` placeholder substitution
- `maxIterations: 5` — iteration cap (default 1)
- `hooks: { host: {...}, sandbox: {...} }` — lifecycle hooks (onWorktreeReady, onSandboxReady)
- `completionSignal: "<promise>COMPLETE</promise>"` — string agent emits to exit loop early
- `idleTimeoutSeconds: 600` — resets on each agent output event
- `output: Output.object({ tag, schema })` — structured output extraction (requires maxIterations=1)
- `logging: { type: "file" | "stdout", onAgentStreamEvent }` — file/stdout/custom forwarder

## Reusable Sandbox API

For multi-run scenarios (implement-then-review):

```typescript
await using sandbox = await createSandbox({
  branch: "agent/fix-42",
  sandbox: docker(),
  hooks: { sandbox: { onSandboxReady: [{ command: "npm install" }] } },
});

const impl = await sandbox.run({ agent: claudeCode("claude-opus-4-7"), promptFile: "implement.md", maxIterations: 5 });
const review = await sandbox.run({ agent: claudeCode("claude-sonnet-4-6"), prompt: "Review the changes and fix any issues." });
```

`await using` triggers `sandbox.close()` automatically. Sandbox stays alive between runs — installed deps persist. Worktree is preserved if uncommitted changes exist.

## Independent Worktree API

`createWorktree()` — git worktree as first-class concept, separate from sandbox. Useful pattern:
1. Run interactive session in worktree first (no sandbox)
2. Hand the same worktree to a sandboxed AFK agent

This is the **interactive→AFK escalation pattern** materialized as an API.

## File Tree Highlights

```
.factory/                  # "software-factory" pattern — implement + review agents + daemon
  implement-prompt.md
  implement-task.ts
  review-prompt.md
  run-daemon.sh
.sandcastle/               # default scaffolded by `sandcastle init`
  .env.example
  CODING_STANDARDS.md
  Dockerfile
  implement-prompt.md
  merge-prompt.md
  plan-prompt.md
  review-prompt.md
  run.ts
.claude/skills/pre-release/SKILL.md   # custom skill for releases
docs/adr/                  # 14+ ADRs documenting design decisions
docs/agents/{adding-a-backlog-manager,adding-an-agent-provider,domain,issue-tracker,triage}.md
```

Key inference: the **.factory/** directory IS the "software-factory" the user asked about. It's not a separate repo — it's a reference implementation pattern living inside sandcastle. Files like `run-daemon.sh` and the implement+review prompts form the autonomous overnight setup.

## ADRs Show Design Process

14+ ADRs in docs/adr/ — Matt eats his own dogfood. Examples:
- 0001-per-step-timeouts
- 0003-reuse-worktree-by-default
- 0008-inline-prompts-skip-processing
- 0010-structured-output
- 0011-resume-is-one-iteration
- 0012-agent-provider-owned-session-storage
- 0014-docker-uid-alignment-via-build-arg

The repo demonstrates the entire methodology from mattpocock/skills (CONTEXT.md + ADRs + skills).

## Repo Vitals

- **Stars: 4,465 | Forks: 467** — solid traction (~5% of skills repo)
- TypeScript primary; Docker for sandboxing
- Active: same-day commits as fetch (2026-05-17)
- Distributed as npm package `@ai-hero/sandcastle`

## Key Patterns

1. **`sandcastle.run()` as the AFK primitive** — single function call replaces complex orchestration
2. **Provider abstraction** — same code runs locally (Docker/Podman) or cloud (Vercel Firecracker)
3. **Worktree-first design** — `createWorktree()` separates git isolation from container isolation
4. **Completion signal pattern** — agent emits sentinel string to signal "done," replacing time-based polling
5. **Idle timeout reset on output** — prevents premature kill while still bounding stuck runs
6. **Lifecycle hooks split host/sandbox** — host hooks for git ops, sandbox hooks for `npm install`
7. **`.factory/` reference setup** — Matt's overnight pattern materialized as four prompts (plan + implement + review + merge) + a bash daemon
