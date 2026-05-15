# Dispatch Tracker

> Last updated: 2026-05-14 13:32 UTC
> Total dispatches: 2

## #2 — https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
**URL:** https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
**Created:** 2026-05-14T13:22

| Pipeline | Status | Started | Completed |
|----------|--------|---------|-----------|
| Obsidian /ingest | ✅ completed | 2026-05-14T13:22 | 2026-05-14T13:25 |
| Blog2Video | 📝 awaiting_review | 2026-05-14T13:22 | - |

**Obsidian summary:** 更贵」。文章给出实测数据推翻这点:

- **Opus 4.7**: 推荐默认用 `high`，理由是它 **token 用量只有 `max` 的 ~50%，但成功率接近 max**。`max` 留给真正复杂的一次性任务。哪怕 `low`，质量也在 Opus 4.6 high～max 之间。
- **4.6 系列**: `medium` 是 sweet spot — top accuracy 但 token 只有 `high` 的一半。
- **最反直觉的**: `low` 模式比**完全不开 thinking 更省 token**。因为不思考 → 出错 → 重试 → 总 token 反而更高

**Blog2Video summary:** 叙述稿已生成：`./blog2video-output/best-practices-computer-browser-use/narration.md`

**摘要**
- 标题：**Claude 点击不准？多半是你截图开太大了**
- 字数：约 **2314 中文字符** （~3328 非空字符）
- 预计时长：**~11.6 分钟**（按 200 字/分钟）
- 段落数：**7 段** — Hook + 三个反直觉深度展开（分辨率/思考预算/上下文管理）+ 安全 + 演示回放 + 一句话总结
- Tradeoff 已保留：滚动缓冲必须批量裁剪（不能每步删一张）、演示回放 strict 模

---

## #1 — https://x.com/chrishayduk/status/2053807198870880743?s=46
**URL:** https://x.com/chrishayduk/status/2053807198870880743?s=46
**Created:** 2026-05-14T12:54

| Pipeline | Status | Started | Completed |
|----------|--------|---------|-----------|
| Obsidian /ingest | ✅ completed | 2026-05-14T12:54 | 2026-05-14T12:56 |
| Blog2Video | 📝 awaiting_review | 2026-05-14T13:28 | - |

**Obsidian summary:** -----|------|------|
| **PLAN.md** | 战略层 | 高层计划，朝目标走的方向。可以人工 seed 初始想法。 |
| **EXPERIMENTS.md** | 经验库 ⭐最重要 | 干净、curated 的实验列表：每条 = 标题 + 简要描述 + 结果。让 agent 和你都能回顾"试过什么 / 为什么成或败"。 |
| **EXPERIMENT_NOTES.md** | 草稿本 | 按时间排序的实时思考流。**用来审计 agent 的推理过程**，发现走偏时及时介入。 |

这套结构和我们 wiki 里几个已有的 pattern 形成有趣对照：
- 和 [

**Blog2Video summary:** The existing `chrishayduk-tweet/` output is **untracked** — running URL mode would overwrite an uncommitted finished narration. Before I do anything destructive, which mode do you want?

1. **Iterate** — treat existing `narration.md` as prior version, improve it (optionally with your feedback). Keep

---
