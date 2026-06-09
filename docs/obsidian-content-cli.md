# obsidian-content CLI — contract

Agent-native CLI exposing this repo (the human-curated **Tier-1 source layer**) to
the **Hermes** orchestration agent. Hermes never reads this repo's internals; it
calls these verbs and consumes stable JSON.

- **Entry point:** `bin/obsidian-content <verb> [flags]` (thin shim → `scripts/obsidian_content.py`)
- **Stack:** Python 3.11+, **stdlib only**, no dependencies, no install step.
- **Path-portable:** resolves the repo from the script's own location, so it works
  from any working directory. Override the interpreter with `OBSIDIAN_CONTENT_PYTHON`.

## What this CLI does and does NOT do

| Does | Does NOT |
|------|----------|
| Read the local append-only event log | Write the central Hermes SQLite ledger |
| Read curated source markdown from `raw/` | Modify anything in `raw/` (immutable) |
| Append `ingest` / `routed` events locally | `git push`, publish, or deploy |
| Emit stable machine-readable JSON | Call gbrain or run LLM workflows |

## JSON envelope

Every verb prints exactly one JSON object to **stdout**:

```json
{
  "contract_version": "1.0",
  "ok": true,
  "verb": "list-ingests",
  "artifacts": { "...": "verb-specific payload" },
  "warnings": ["non-fatal notes"],
  "errors": ["fatal reasons when ok=false"]
}
```

`contract_version` is bumped on breaking changes to this envelope or verb behavior.
Records inside the event log carry their own `schema_version` (currently `1`).

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | Success (`ok: true`) |
| `1` | Handled failure (`ok: false`, reasons in `errors[]`) — valid JSON still printed |
| `2` | Usage error (bad/missing flags, unknown verb) — argparse message on **stderr**, no JSON |

Hermes should: parse stdout as JSON when exit ∈ {0,1}; treat exit `2` as a caller bug.

## Verbs

### `list-ingests` — discover ingests
```
bin/obsidian-content list-ingests [--status new|routed|all] [--since YYYY-MM-DD] [--limit N] [--newest]
```
- `--status` defaults to **`new`** (unrouted) — the discovery case.
- `--since` filters by event timestamp (ISO date/datetime, inclusive lower bound).
- `--limit N` caps results; add `--newest` to take the newest N (default: oldest N).
- `artifacts`: `{ status_filter, count, total_matched, ingests: [ <state row>, ... ] }`

A state row:
```json
{
  "event_id": "a3513de0247c",
  "ts": "2026-05-22T00:00:00+00:00",
  "source_path": "raw/2026-05-22-repo-anthropics-skills.md",
  "title": "anthropics/skills (Official Anthropic Skills Repo)",
  "fetch_method": "GitHub Deep Scan (gh CLI)",
  "tier": 1,
  "pages_created": ["anthropics-skills-repo.md", "..."],
  "pages_updated": ["index.md", "..."],
  "routed": false, "routed_ts": null, "routed_by": null, "task_ref": null
}
```

### `export-source` — get clean source markdown
```
bin/obsidian-content export-source --id <event_id> [--out PATH] [--dry-run]
```
- Default: returns the curated markdown inline in `artifacts.content` (+ `bytes`).
- `--out PATH`: writes a copy to PATH (relative paths resolve to repo root) and
  returns `artifacts.written_to` instead of inline content.
- `--dry-run` with `--out`: reports `would_write_to`, writes nothing.
- `ok:false` (exit 1) if the `event_id` is unknown or the source file is missing.

This is the handoff point for downstream Blog2Video / LoreAI consumers.

### `mark-routed` — mark an ingest as routed (idempotent)
```
bin/obsidian-content mark-routed --id <event_id> [--by hermes] [--task-ref REF] [--dry-run]
```
- Appends a `routed` event. **Idempotent**: a second call is a no-op
  (`changed:false`, warning emitted, still `ok:true`).
- `--dry-run`: reports what would happen, writes nothing.
- `ok:false` if the `event_id` is unknown.

### `record-ingest` — append a Tier-1 ingest event (the `/ingest` integration point)
```
bin/obsidian-content record-ingest --source raw/<file>.md [--title ...] [--fetch-method ...] \
    [--pages-created "a.md, b.md"] [--pages-updated "c.md"] [--tier 1] [--ts ISO] [--dry-run]
```
- Called by the `/ingest` skill (step 7) after a successful ingest.
- **Idempotent**: `event_id = sha1(source_path)[:12]`, so re-recording the same
  source is a no-op (`recorded:false`).
- Warns (but still records) if the source file does not yet exist.

### `backfill-from-log` — one-time historical seed
```
bin/obsidian-content backfill-from-log [--dry-run]
```
- Parses `wiki/log.md` ingest entries and seeds events for any not already present.
- Idempotent (re-run adds 0). **Skips sources whose file no longer exists**
  (renamed/removed per log corrections) and reports them under `skipped_missing`.

## Idempotency model

The event log (`events/ingest-events.jsonl`) is **append-only** and folded into
state on read:
- `ingest` records create/refresh a row; `routed` records flip `routed: true`.
- Folding is deterministic — replaying the same records yields the same state.
- Re-running `record-ingest`, `mark-routed`, or `backfill-from-log` never
  corrupts or duplicates state.

## How Hermes should call this CLI

A minimal poll → route → ack loop:

```bash
CLI="bin/obsidian-content"          # or an absolute path on the Obsidian host

# 1. Discover new Tier-1 ingests
$CLI list-ingests --status new --since 2026-06-01

# 2. For each event_id, pull the clean source for downstream task creation
$CLI export-source --id <event_id> --out /tmp/<event_id>.md

#    ...Hermes creates downstream tasks in its OWN ledger (not here)...

# 3. Acknowledge so it drops out of the 'new' queue
$CLI mark-routed --id <event_id> --by hermes --task-ref <hermes-task-id>
```

Guidelines:
- Always branch on exit code first, then parse stdout JSON.
- Treat `event_id` as the durable key across all three verbs.
- `mark-routed` is safe to retry (idempotent), so Hermes can ack at-least-once.

## Smoke check

```bash
bin/obsidian-content --version
bin/obsidian-content backfill-from-log --dry-run        # parses log, writes nothing
bin/obsidian-content list-ingests --status new --limit 1 --newest
# grab an id from the above, then:
bin/obsidian-content export-source --id <id> | head
bin/obsidian-content mark-routed --id <id> --dry-run
```
