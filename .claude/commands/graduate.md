---
name: graduate
description: Scan recent build logs for ideas worth promoting to standalone notes. Interactive — you approve each one before it's created.
---

# Graduate — Promote Ideas from Build Logs

Scan recent daily build logs, find ideas worth developing, help decide which to promote into standalone notes in ideas/.

## Steps

1. Read all daily build logs from the past 14 days.

2. Find candidates:
   - All entries tagged with #idea
   - Entries that sound like ideas even without the tag (questions, "what if", tool concepts, strategic observations)
   - Entries tagged #learning that could develop into insights

3. Present candidates one by one:
   ```
   📝 Candidate 1/N: [brief title]
   Source: daily/2026-03-04.md
   Original: "[the exact text from the build log]"
   Connected to: [[Project1]], [[Project2]]
   
   → Graduate to ideas/? [yes / skip / merge with existing]
   ```

4. Wait for response before next candidate.

5. For "yes":
   - Create file in `ideas/` with descriptive name (e.g., `auto-topic-selection-pipeline.md`)
   - Frontmatter: `graduated-from`, `date`, `status: seed`
   - Content: core idea, context from build log, [[links]] to related notes, 2-3 next steps
   - Show draft before writing, wait for approval

6. For "merge":
   - Ask which note to merge with
   - Append insight to that note

7. Final summary:
   ```
   ✅ Graduated: 3 ideas → ideas/
   ⏭️ Skipped: 2
   🔗 Merged: 1 → ideas/existing-note.md
   ```

## Important
- This command writes to ideas/ — the one exception to human-only rule, because I review and approve each one interactively.
- Keep graduated notes short. Seeds, not essays.
- Always show draft and ask for confirmation before writing.
