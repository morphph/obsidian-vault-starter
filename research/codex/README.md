# research/codex/ — Codex 常青报告(两份长期维护)

Codex 官方一直在更新,所以这里维护**两份常青报告**,以后有新变化**直接在这两份上改**,不再新开调研文件夹。

| 文件 | 定位 | 读者 |
|---|---|---|
| [`codex-overview.md`](codex-overview.md) | **一文了解 Codex** —— 是什么 + 四 surface + 装/配置基础 + 模型 + **功能一览**(subagents/MCP/hooks/skills/scheduled/cloud/remote,简介+最小例) | 想快速摸清 Codex 全貌 |
| [`codex-advanced.md`](codex-advanced.md) | **Codex 进阶实战:当自主 agent 平台压榨** —— 并行深配 + 无人值守 + 后台/远程 + 长时任务 + **逐字 TOML 金料** + `/goal` 方法论 + prompting | 已了解,想榨干 |
| [`ingest-candidates.md`](ingest-candidates.md) | 值得 `/ingest` 的官方源(已对 `raw/` 去重) | — |

## 维护规则
- **正文只呈现最新状态**,不写"X 已过时/我们更新了"这类元话术。
- 每份文末有 **`## 更新记录`** 表格(日期 | 变更 | 官方来源)——官方一变,就在正文改 + 更新记录补一行。
- 事实漂移极快(默认模型/文档域名/功能改名两周内可全变),更新前重核 [`learn.chatgpt.com/docs/changelog`](https://learn.chatgpt.com/docs/changelog) 与 `/models`。
- 这两份是 Tier-4 常青报告(非 vault);要发布 → 从进阶篇角度走 `/draft`;`drafts/openai-codex-getting-started` 是独立的上手篇发布稿(与本目录报告一同话题,注意同步纠偏)。

> 本目录 2026-07-17 由旧 `research/openai-codex`(getting-started 调研)+ `research/codex-advanced-guide`(进阶调研)合并而成,两个旧文件夹已删除(git 保留历史)。
