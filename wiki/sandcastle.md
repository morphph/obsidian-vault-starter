---
type: entity
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-repo-mattpocock-sandcastle.md
tags: [wiki, framework, afk, sandbox, orchestration]
---

# Sandcastle

## Summary
TypeScript framework by [[matt-pocock]] for orchestrating AFK coding agents in isolated sandboxes — 4,465 stars, distributed as `@ai-hero/sandcastle`. Provider-agnostic (Docker / Podman / Vercel Firecracker). The Phase 5 primitive of [[idea-to-afk-agent-flow]]. Productizes the Ralph pattern as a typed JS API.

## Details

### Core API
```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
});
```

Returns `{ iterations, commits, branch, stdout, completionSignal, logFilePath }`.

### Install
```bash
npm install --save-dev @ai-hero/sandcastle
npx sandcastle init     # scaffolds .sandcastle/ with main.ts, prompt.md, .env.example
npx tsx .sandcastle/main.ts
```

### Provider Abstraction
| Provider | Type | Use case |
|----------|------|----------|
| `docker()` | Bind-mount | Local dev, most common |
| `podman()` | Bind-mount | Rootless alternative, CI |
| `vercel()` | Isolated (Firecracker microVM) | Cloud parallelism, many agents |
| `noSandbox()` | None | Trusted local interactive only |

Same code switches provider without modification — dev locally, scale to cloud.

### Key Options (selection)
- `agent: claudeCode(model, { effort: "high" })`
- `sandbox: docker({ imageName, mounts, env, network })`
- `branchStrategy: { type: "head" | "branch" | "merge-to-head" }`
- `prompt` OR `promptFile` (mutually exclusive)
- `promptArgs: { ISSUE_NUMBER: "42" }` — `{{KEY}}` substitution
- `maxIterations: 5`
- `hooks: { host: {...}, sandbox: {...} }` — lifecycle hooks split by location
- `completionSignal: "<promise>COMPLETE</promise>"` — agent emits to exit loop early
- `idleTimeoutSeconds: 600` — resets on each output event
- `output: Output.object({ tag, schema })` — structured output extraction

### Reusable Sandbox Pattern
For multi-run (implement-then-review) on same branch:
```typescript
await using sandbox = await createSandbox({ branch, sandbox: docker() });
const impl = await sandbox.run({ agent: claudeCode("claude-opus-4-7"), promptFile: "implement.md", maxIterations: 5 });
const review = await sandbox.run({ agent: claudeCode("claude-sonnet-4-6"), prompt: "Review and fix." });
```
`await using` auto-cleans. Container persists between runs — deps install once.

### `createWorktree()` — Interactive→AFK Bridge
Materializes the **interactive→AFK escalation pattern** as an API:
```typescript
await using wt = await createWorktree({ branchStrategy: { type: "branch", branch: "agent/fix-42" } });

// Step 1: human-driven interactive session (no sandbox)
await wt.interactive({ agent: claudeCode("claude-opus-4-7"), prompt: "Explore the bug." });

// Step 2: same worktree, now run AFK sandboxed
await wt.run({ agent: claudeCode("claude-opus-4-7"), sandbox: docker(), prompt: "Fix it.", maxIterations: 3 });
```

This API is the concrete implementation of Phase 4 → Phase 5 in [[idea-to-afk-agent-flow]].

### The `.factory/` Pattern (Software-Factory)
Inside the Sandcastle repo, `.factory/` directory contains the reference overnight-pipeline setup:
- `implement-prompt.md`
- `review-prompt.md`
- `merge-prompt.md`
- `plan-prompt.md`
- `run-daemon.sh`
- `implement-task.ts`

This is what "software-factory" refers to — not a separate repo, but a 5-file pattern inside Sandcastle.

### Design Maturity Signal
14+ ADRs under `docs/adr/`:
- `0001-per-step-timeouts`
- `0003-reuse-worktree-by-default`
- `0008-inline-prompts-skip-processing`
- `0010-structured-output`
- `0011-resume-is-one-iteration`
- `0012-agent-provider-owned-session-storage`
- `0014-docker-uid-alignment-via-build-arg`

Matt dogfoods his own [[grill-with-docs]] methodology — the repo itself demonstrates the workflow.

### Key Patterns Worth Stealing
1. **Single-function AFK primitive** — `sandcastle.run()` collapses orchestration
2. **Completion-signal pattern** — agent emits sentinel string; better than time polling
3. **Idle-timeout reset on output** — bounds stuck runs without killing slow ones
4. **Lifecycle hooks split host/sandbox** — host for git ops, sandbox for `npm install`
5. **Worktree-first design** — git isolation independent of container isolation

## Connections
- Owner: [[matt-pocock]]
- Built atop: [[claude-code]], [[claude-code-sandboxing]]
- Productizes: [[ralph-wiggum]] pattern
- Phase 5 of: [[idea-to-afk-agent-flow]]
- Sibling: [[mattpocock-skills-library]] (Matt's other major project)
- Related: [[forked-agent-pattern]], [[claude-code-monitor-tool]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | GitHub Deep Scan of sandcastle repo | Initial creation |
