---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-session-unknown-1915.md
tags: [wiki, content-distribution, china, social-platforms]
---

# Content Distribution: China Platforms

## Summary
Platform-specific distribution strategies for 微信视频号 and 小红书. Key insight: the two platforms need **different styles** — 视频号 is social-recommendation-driven (朋友圈/社群转发), 小红书 is search-driven (SEO关键词覆盖). Same content, different metadata optimization.

## Details

### 微信视频号
- **Algorithm:** 社交推荐权重 >50% (friend shares dominate discovery), 完播率 is core metric (>35% gets extra traffic weighting)
- **Title:** 前16字决定生死 — must hook in first 16 characters. Style: 钩子 + 关键词前置
- **Description:** 长视频仅 **100字限制**（含标签和@）— must be extremely concise
- **Hashtags:** 1大 + 2中 + 1-2小 topics. 同一话题发3条以上，系统才稳定识别活跃度
- **Cover image:** 不需要额外优化 — 信息流自动播放，前3秒才是真正的"封面"
- **Core leverage:** 朋友圈/社群转发，不是 SEO

### 小红书
- **Algorithm:** Search-driven discovery
- **Title style:** SEO关键词覆盖 — optimize for search terms
- **Description:** Longer, keyword-rich descriptions allowed
- **Different from 视频号:** Focus on discoverability through search, not social sharing

### Delivery Metadata Generation
- [[blog2video]] auto-generates `delivery_meta.md` with 2-3 versions for each platform
- Different title/description styles per platform in same file
- Ensures content is optimized for each platform's discovery mechanism

## Connections
- Related: [[blog2video]], [[loreai]], [[keyword-grouping-engine]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-session-unknown-1915.md | Initial creation — 视频号 + 小红书 strategy research |
