# events/

Machine-readable event log for the autonomous content system. This directory is
the **stable contract surface** between this repo (the human-curated Tier-1 source
layer) and the Hermes orchestration agent.

## ingest-events.jsonl

Append-only [JSON Lines](https://jsonlines.org/). One JSON object per line. Never
rewritten in place — state is computed by *folding* the records (so replays and
duplicate appends are idempotent).

### Record types

**`ingest`** — emitted by `/ingest` after a source is successfully added to the wiki:

```json
{"type":"ingest","schema_version":1,"event_id":"a1b2c3d4e5f6","ts":"2026-06-09T10:00:00+00:00","source_path":"raw/2026-05-22-repo-anthropics-skills.md","title":"anthropics/skills","fetch_method":"GitHub Deep Scan","tier":1,"pages_created":["anthropics-skills-repo.md"],"pages_updated":["index.md"]}
```

**`routed`** — emitted by `mark-routed` once Hermes has created downstream tasks:

```json
{"type":"routed","schema_version":1,"event_id":"a1b2c3d4e5f6","ts":"2026-06-09T11:00:00+00:00","routed_by":"hermes","task_ref":"hermes-task-123"}
```

### Key properties

- **`event_id`** = first 12 hex chars of `sha1(source_path)`. Stable and
  deterministic, so re-recording the same source is a no-op.
- **Append-only** — safe for concurrent appends; no read-modify-write races.
- **Folded state** — `list-ingests` replays records: an `ingest` row becomes
  `routed: true` once a matching `routed` record exists. Folding twice yields the
  same result.

Do not hand-edit this file. Use the `obsidian-content` CLI (see
`docs/obsidian-content-cli.md`).
