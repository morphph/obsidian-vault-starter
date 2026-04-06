---
name: sync-project
description: Auto-extract latest info from code repos into vault project context files. Updates auto-synced section only, never touches human-written sections. Usage: /sync-project [project-name] or /sync-project all
---

# Sync Project Context from Repo

Update the "Auto-synced from repo" section of project context files using the latest information from code repositories.

## Arguments
- `$ARGUMENTS` can be a specific project name (e.g., "loreai") or "all" to sync everything.

## Repo locations (from CLAUDE.md)
- loreai: ~/Desktop/Project/loreai-v2
- blog2video: ~/Desktop/Project/blog2video

## For each project to sync:

1. Check if the repo directory exists. If not, skip with a warning.

2. From the repo, read:
   - README.md (first 200 lines max)
   - Any PRD, ROADMAP, or CHANGELOG file if it exists
   - `git log --oneline -10` (last 10 commits)
   - Package.json or pyproject.toml (just the name/description/version)

3. Synthesize into a concise update. Extract:
   - **Architecture:** High-level technical architecture (one paragraph max)
   - **Tech stack:** Key technologies and frameworks
   - **Recent activity:** Summary of last 10 commits in plain language
   - **Current version/status:** If discernible

4. Find the corresponding project context file in `projects/`.

5. Replace ONLY the content between `## Auto-synced from repo` and `## Human context`.
   **CRITICAL: Never modify anything in or after the "## Human context" section.**

6. Update the `last-updated` field in frontmatter to today's date.

7. Report results:
   ```
   ✅ loreai — synced (last commit: "update AEO module")
   ✅ blog2video — synced (last commit: "fix narration pacing")
   ```

## Important
- READ from repo, WRITE to vault. One direction only.
- Only the auto-synced section is machine-written.
- If a project context file doesn't exist yet, create one using the template structure but leave the Human context section with [Write: ...] placeholders.
