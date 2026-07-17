# research/codex/ — Codex 常青报告(两份长期维护)

Codex 官方一直在更新,所以这里维护**两份常青报告**,以后有新变化**直接在这两份上改**,不再新开调研文件夹。

这两份是**读者指南**形状(guide 模板 v1):头部契约 → 心智模型 + 决策表 → Claude Code 映射/职责边界 → 每主题处方收尾 → 端到端工作流 → 分阶段计划 → 可复制模板 → 检查清单 → 官方索引 + 常青更新记录。研究元话术(核验状态、GA/弃用追踪、辨伪、「推断·未实测」)不在指南正文,统一住 `facts.md`。

| 文件 | 定位 | 读者 |
|---|---|---|
| [`codex-overview.md`](codex-overview.md) | **上手 Codex:从 Claude Code 迁过来,一天摸清全貌** —— 心智模型 + 需求→入口决策表 + 能力映射/职责边界 + 装/配置基础 + 权限三件套 + 功能一览(每功能处方) + 端到端工作流 + 七天上手计划 + 可复制模板 + 检查清单 | 想快速摸清 Codex 全貌 |
| [`codex-advanced.md`](codex-advanced.md) | **压榨 Codex:把它变成能无人值守跑几十小时的 agent 平台** —— 流水线心智 + subagents 深配 + 无人值守 + Cloud/Remote/Worktree + codex exec 任务持久层 + SDK/App Server/Agents SDK/GitHub Action + 长时任务四文件法 + `/goal` 方法论 + Rules/Hooks + 审批分级 + Phase 1-5 + 无人值守模板 + ASCII 架构图 + 上线检查表 | 已了解,想榨干 |
| [`facts.md`](facts.md) | **核验事实台账**(非成品):逐条 ✅/⚠️/❌、确切 TOML 默认值、GA/弃用追踪、第三方辨伪、「推断·未实测」——两份指南的事实底座 | 维护者 / 核验时查 |
| [`ingest-candidates.md`](ingest-candidates.md) | 值得 `/ingest` 的官方源(已对 `raw/` 去重) | — |

## 维护规则
- **正文只呈现最新状态**,不写"X 已过时/我们更新了"这类元话术;核验状态/GA 追踪/辨伪只住 `facts.md`。
- 官方一变:先在 `facts.md` 核验并记状态,再把已核验结论改进指南正文(要命的 gotcha 以 callout 形式)。
- 每份文末有 **`## 更新记录`** 表格(日期 | 变更 | 官方来源)——正文改完,更新记录补一行。
- 事实漂移极快(默认模型/文档域名/功能改名两周内可全变),更新前重核 [`learn.chatgpt.com/docs/changelog`](https://learn.chatgpt.com/docs/changelog) 与 `/models`。
- 这两份是 Tier-4 常青报告(非 vault);要发布 → 从进阶篇角度走 `/draft`;`drafts/openai-codex-getting-started` 是独立的上手篇发布稿(与本目录报告一同话题,注意同步纠偏)。

> 本目录 2026-07-17 由旧 `research/openai-codex`(getting-started 调研)+ `research/codex-advanced-guide`(进阶调研)合并而成,两个旧文件夹已删除(git 保留历史)。
