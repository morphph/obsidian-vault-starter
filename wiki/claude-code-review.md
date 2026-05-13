---
type: concept
created: 2026-05-13
last-updated: 2026-05-13
sources:
  - raw/2026-05-13-claude-code-goal-and-code-review.md
tags: [claude-code, pr-review, multi-agent, github, verification, managed-service]
---

# Code Review — Multi-agent PR review as a managed service

## Summary
[[anthropic]] managed GitHub PR review service that dispatches a **fleet of specialized agents** in parallel on each PR, with a **verification step** to filter false positives. Findings post as inline diff comments + summary, ranked by severity. Research preview for **Team / Enterprise** subscriptions. Average 20 min / review, $15–25 / review. The architectural twin of [[multi-agent-architecture]] applied to code review, with the same agent-fleet pattern Anthropic runs internally.

## Details

### Trigger modes (configured per repo)
- **Once after PR creation** — on PR open or ready-for-review.
- **After every push** — runs on every push, auto-resolves threads when issues are fixed. Most expensive mode.
- **Manual** — only on explicit comment trigger.
- `@claude review` — starts a review **and subscribes** the PR to push-triggered reviews going forward.
- `@claude review once` — single review, no subscription. Use for long-running PRs to avoid per-push cost.
- Manual triggers work on draft PRs (explicit intent overrides draft status).

### Severity model
| Marker | Severity | Meaning |
|--------|----------|---------|
| 🔴 | Important | Bug that should be fixed before merging |
| 🟡 | Nit | Minor issue, worth fixing but not blocking |
| 🟣 | Pre-existing | Bug in the codebase but not introduced by this PR |

Each finding has a **collapsible extended reasoning** section: why Claude flagged it and how it verified.

### Check-run integration
- A **Claude Code Review** check appears alongside CI checks.
- **Always neutral conclusion** — never blocks branch-protected merges by default.
- **Details** link shows severity table of every finding.
- Findings also render as **annotations in the Files changed tab**.
- Machine-readable severity JSON in check-run output — parse with `gh api ... --jq` to gate merges if you want. `normal` key = Important count.

### Reported quality (Anthropic internal testing)
- Large PRs (>1000 LOC): 84% receive findings, avg 7.5 issues.
- Small PRs (<50 LOC): 31% receive findings, avg 0.5 issues.
- **False positive rate: <1%** of findings marked incorrect by engineers.
- Has caught critical bugs humans missed (one-line auth failure; pre-existing type mismatch corrupting an encryption key cache).

### Feedback loop
- 👍/👎 pre-attached to every finding — one-click rating.
- Reactions collected post-merge, used to tune the reviewer. Reactions do NOT trigger re-review.
- **Replying inline does NOT prompt Claude** — fix code and push; push-mode auto-resolves threads.
- For a fresh review without pushing: `@claude review once` as top-level PR comment.

### Customization — two files, two roles

#### `CLAUDE.md` (project-wide, hierarchical)
- Code Review reads it as **project context**.
- Newly-introduced violations flagged as **nit-level** findings.
- Bidirectional: PR making a `CLAUDE.md` claim outdated → Claude flags docs need updating too.

#### `REVIEW.md` (review-only, highest priority)
- Pasted **verbatim** into every agent's system prompt — `@` imports NOT expanded.
- High-impact knobs:
  - **Severity recalibration** — redefine "Important" for the repo (docs-only / prototype / backend service all have different bars).
  - **Nit volume cap** — e.g., "report at most 5 nits, mention the rest as a count in summary."
  - **Skip rules** — paths, branches, finding categories where Claude posts nothing (generated code, lockfiles, vendored deps, lint/spellcheck already in CI).
  - **Repo-specific checks** — e.g., "new API routes must have an integration test." Lands more reliably than the same rule buried in a long `CLAUDE.md`.
  - **Verification bar** — "behavior claims need a `file:line` citation, not naming-based inference."
  - **Re-review convergence** — "after first review, suppress new nits, post Important findings only" — stops a one-line fix reaching round 7 on style alone.
  - **Summary shape** — request a one-line tally up top (`2 factual, 4 style`).
- Keep it focused: length dilutes priority. Project context → `CLAUDE.md`. Review behavior → `REVIEW.md`.

## Setup (admin, once)
1. claude.ai/admin-settings/claude-code → Code Review section.
2. Install **Claude GitHub App** (perms: contents r+w, issues r+w, PRs r+w).
3. Select repositories.
4. Pick Review Behavior per repo.

## Cost & availability
- **Team / Enterprise only**. Research preview. Not available with Zero Data Retention.
- **$15–25 per review** avg, scales with PR size/complexity. Separate from plan included usage.
- Billed on Anthropic bill regardless of Bedrock/Vertex routing for other features.
- Monthly **spend cap** at claude.ai/admin-settings/usage. Skipped reviews post comment when hit.
- Analytics: claude.ai/analytics/code-review (PRs reviewed, weekly cost, feedback resolutions, per-repo).

## Local alternative
The plugin marketplace ships a **`code-review` plugin** for running on-demand reviews locally before pushing. Useful for individual devs without Team/Enterprise.

## How it works (architecture)
- Multiple agents run **in parallel on Anthropic infrastructure**, each scanning for a different issue class.
- A **verification agent** checks candidates against actual code behavior to filter false positives.
- Results deduplicated, severity-ranked, posted inline + summary.
- Average completion: ~20 min. Failed runs end with a neutral conclusion; never blocks merge automatically.

## Comparison with /ultrareview
`/ultrareview` is the user-triggered local Claude Code multi-agent review (no GitHub integration, runs from CLI). Code Review is the **managed-service** version: same pattern, but always-on, GitHub-integrated, per-PR, with admin spend controls and analytics. `/ultrareview` is per-developer; Code Review is per-org.

## Anti-patterns
- Treating Code Review as a substitute for human review — it's a **first pass**, not a gatekeeper. Findings don't block merge by design.
- Not writing a `REVIEW.md` for noisy repos — the default calibration is "production backend"; docs/prototypes/SDKs need recalibration or you'll drown in nits.
- Using "After every push" on high-churn PRs without a nit cap — cost multiplies fast.
- Skipping the GitHub App permissions audit — write access to contents/issues/PRs is broad; review what your org grants.

## Connections
- Related: [[claude-code]], [[multi-agent-architecture]], [[verification-loops]], [[anthropic]], [[claude-managed-agents]]
- Same fleet-of-agents-plus-verifier pattern as [[multi-agent-architecture]] and [[managed-agents-multiagent]].
- Architectural sibling of [[claude-code-goal]]: both add a model-evaluator step to close a human-in-the-loop gap. `/goal` does it at turn boundary; Code Review at PR boundary.
- `REVIEW.md` as configuration is a [[resolvers]]-style routing primitive — highest-priority instruction injection.
- The 👍/👎 + re-tuning loop is a production form of [[trigger-evals]] — production data feeds back into the reviewer.

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-13 | raw/2026-05-13-claude-code-goal-and-code-review.md | Initial creation from official Code Review docs at code.claude.com/docs/en/code-review + claude.com/blog/code-review |
