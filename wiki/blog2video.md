---
type: entity
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-session-unknown-0953.md
  - raw/2026-04-08-session-unknown-1017.md
  - raw/2026-04-08-session-unknown-1126.md
  - raw/2026-04-08-session-unknown-1139.md
  - raw/2026-04-08-session-unknown-1421.md
  - raw/2026-04-09-session-unknown-1915.md
tags: [wiki, project, pipeline, content]
---

# blog2video (AI精读)

## Summary
User's video production pipeline that transforms articles/tweets into narrated slide videos. Multi-stage pipeline: Source Fetch → Memo → Narration → Episode Splitter → Slide Planner → Slide HTML → Render. Outputs .mp4 videos with auto-generated cover photos for Chinese content platforms.

## Details
- **Pipeline stages:** Source fetch → memo extraction → narration.md (human review checkpoint) → video_1_script.md (auto-generated, no review needed) → episode splitting → slide planning → slide HTML → render (TTS + screenshots → video)
- **Review checkpoint:** `narration.md` is the human-editable source; `video_1_script.md` is a derived build artifact with `[SLIDE N]` markers and timecodes
- **Source fetching:** Uses [[source-fetch-fallback-chain]] — Playwright MCP → WebFetch → Puppeteer → Vision transcription → Abort. Playwright MCP with `--browser chrome` can fetch X/Twitter content without login via accessibility tree.
- **Diagram generation:** `scripts/lib/diagram-gen.ts` — D2 for architecture diagrams, Mermaid for process/flow. Prompt evaluates article type before choosing diagram type. Simple LR mermaid chains render as thin strips (~45px height) — avoid or use TD layout.
- **Delivery metadata:** Auto-generates `delivery_meta.md` with 2-3 版本 for both [[content-distribution-china|小红书 and 微信视频号]], with platform-specific title/description styles
- **Manifest naming:** Render script expects `manifest.json` (not `video_1_manifest.json`) — mismatch causes render failure
- **TTS:** Idempotent — if audio already exists, render retry skips TTS and proceeds from screenshots
- **Parallel execution:** Multiple episodes can run concurrently (e.g., 全景篇 render + Agent Loop narration generation)
- **Output:** `.mp4` and `cover_photo.png` excluded from git via `.gitignore` (large files stay local)
- **[[silent-fallback-antipattern]] lesson:** Pipeline once completed "successfully" with dramatically lower quality when Playwright MCP wasn't loaded — source content was only image captions instead of full article text. Fixed with preflight gate: ToolSearch must confirm `browser_navigate` available for X/Twitter URLs before proceeding.

## Connections
- Related: [[loreai]], [[silent-fallback-antipattern]], [[content-distribution-china]], [[claude-code]], [[compiler-analogy]]
- Pipeline follows [[compiler-analogy]]: source article = source code, LLM stages = compiler passes, rendered video = executable

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-08-session-unknown-0953.md | Initial creation — pipeline stages, review checkpoint, manifest naming |
| 2026-04-09 | raw/2026-04-08-session-unknown-1017.md | Added diagram generation logic (D2 vs Mermaid) |
| 2026-04-09 | raw/2026-04-08-session-unknown-1126.md | Added source fetch fallback chain |
| 2026-04-09 | raw/2026-04-08-session-unknown-1139.md | Added MCP config details (user-level) |
| 2026-04-09 | raw/2026-04-08-session-unknown-1421.md | Added silent fallback antipattern lesson |
| 2026-04-09 | raw/2026-04-09-session-unknown-1915.md | Added delivery metadata generation |
