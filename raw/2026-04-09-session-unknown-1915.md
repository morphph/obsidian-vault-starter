# Session Capture: unknown

**Date:** 2026-04-09
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---



**Context:** Blog2video pipeline — rendering two Claude Code explainer videos (akshay-pachaar-tweet, troyhua-tweet) and preparing delivery metadata for 微信视频号 and 小红书.

**Key Exchanges:**
- User improved troyhua-tweet hook by adding authority credentials (CMU PhD + Agentic Memory + 135K views/850 bookmarks) and restructured to "价值先行 → 权威背书"
- Detailed research on 微信视频号 meta best practices: title (前16字决定生死), description (长视频仅100字限制), hashtag strategy (1大+2中+1-2小), algorithm (社交推荐权重>50%, 完播率是核心指标)
- Key distinction: 视频号 vs 小红书 need **different style** titles and descriptions — 视频号 is social-driven, 小红书 is search-driven

**Decisions Made:**
- Every video render now auto-generates `delivery_meta.md` with 2-3 版本 for both 小红书 and 视频号
- 视频号封面图不需要额外优化 — 信息流自动播放，前3秒才是真正的"封面"
- Two platforms should get different meta styles (钩子+关键词前置 vs SEO关键词覆盖)

**Lessons Learned:**
- 视频号长视频描述限制仅 **100字**（含标签和@），必须极度精炼
- 视频号核心杠杆是朋友圈/社群转发，不是SEO
- 话题标签：同一话题发3条以上，系统才稳定识别活跃度
- 完播率超35%获额外流量加权

**Action Items:**
- rclone 尚未配置 `gdrive:` remote，需要用户手动 `rclone config` 后才能上传 Google Drive
- `delivery_meta.md` 自动生成逻辑已记入 memory，后续 pipeline 需遵守