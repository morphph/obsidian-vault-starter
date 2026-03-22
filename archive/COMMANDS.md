# 命令速查表

> 在 Claude Code 里输入 `/` 可以看到所有可用命令。
> 以下是每个命令的说明和推荐使用场景。

---

## 日常命令（每天用）

### /log
**做什么：** 快速记录今天的 build log。问你三个问题（做了什么、有什么发现、明天计划），写入 daily 笔记，自动识别项目名加 [[链接]]，自动标记 #idea / #blocker / #learning。
**什么时候用：** 每天结束工作时，花 5 分钟运行一次。
**写入位置：** `daily/YYYY-MM-DD.md`

---

## 上下文命令（每个 session 开始时用）

### /context
**做什么：** 加载你的项目全景。默认加载 CLAUDE.md + 所有项目上下文文件（快速模式，约 5K tokens）。如果需要更多上下文，说 "load full context" 会额外加载最近 7 天 build log 和 ideas。
**什么时候用：** 开始任何需要跨项目理解的工作 session 时。
**写入位置：** 不写入文件，只加载到 session 上下文中。

### /sync-project
**做什么：** 从你的代码仓库（GitHub repo）自动提取最新的技术信息——README、最近 git log——更新项目上下文文件的"Auto-synced"部分。不会碰你手写的"Human context"部分。
**什么时候用：** 项目有重大更新后，或者每周跑一次保持同步。
**用法：** `/sync-project hot2content` 或 `/sync-project all`
**写入位置：** 更新 `projects/` 下的对应文件（仅 auto-synced 部分）

---

## 思维工具（每周或需要灵感时用）

### /ideas
**做什么：** 全面扫描 vault（30 天 build log + 所有项目 + ideas + references），生成跨项目想法报告。包括：要构建的工具、值得发展的想法、未命名的模式、Top 5 行动建议。
**什么时候用：** 每周一次，或者感觉需要新方向时。
**⚠️ 重量级命令：** 建议在干净的新 session 里运行（命令会自动提醒你）。
**写入位置：** `agent-output/ideas-report-YYYY-MM-DD.md`

### /emerge
**做什么：** 扫描 60 天的 vault 内容，发现你反复围绕但从未明确命名的模式、理论和方向。帮你把潜意识里的想法变成清晰的概念。
**什么时候用：** 每月一次，或者在做战略规划前。
**⚠️ 重量级命令：** 建议在干净的新 session 里运行。
**写入位置：** `agent-output/emerge-YYYY-MM-DD.md`

### /connect
**做什么：** 输入两个概念、项目或领域，在 vault 的链接图谱中找到它们之间隐藏的连接和桥梁。
**什么时候用：** 当你想探索两个看似不相关的领域之间的关系时。
**用法：** `/connect blog2video AEO` 或 `/connect Xiaohongshu email-subscribers`
**写入位置：** `agent-output/connect-X-Y-YYYY-MM-DD.md`

### /graduate
**做什么：** 扫描最近 14 天的 build log，找出标记了 #idea 或者看起来像好想法的内容，逐个问你是否要"毕业"成独立笔记。
**什么时候用：** 每周一次，配合 /ideas 一起跑。
**写入位置：** 确认后写入 `ideas/` 目录

---

## 使用节奏建议

| 频率 | 命令 | 耗时 |
|------|------|------|
| 每天 | `/log` | 5 分钟 |
| 每个 session 开始 | `/context` | 30 秒 |
| 每周 | `/ideas` → `/graduate` | 20 分钟 |
| 每周或按需 | `/sync-project all` | 2 分钟 |
| 每月 | `/emerge` | 15 分钟 |
| 需要灵感时 | `/connect X Y` | 5 分钟 |
