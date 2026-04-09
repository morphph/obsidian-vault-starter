---
type: synthesis
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-bcherny-claude-code-best-practices.md
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
tags: [wiki, connection, practice, context]
---

# 用"办公桌"理解Claude Code Best Practices

## Summary
[[boris-cherny|Boris Cherny]]的Claude Code最佳实践，结合[[tw93]]的context分层理论，可以用一个非技术比喻完整理解：**Claude的注意力就是一张办公桌——关键不是桌子多大，而是桌上放了什么。** Boris的每条建议本质上都在回答同一个问题：怎么管理这张桌子。

## 一个关键认知

大多数人觉得Claude Code的限制是"装不下"——200K token不够用。

[[tw93]]纠正了这个误解：

> **Context问题不是容量问题，是噪音问题。**

200K token其实很大。真正的问题是：有用的信息被无关的东西淹没了。Claude不是装不下，而是**在一堆噪音里找不到重点**，然后开始变笨。

理解了这个，后面所有建议都有了逻辑。

## 办公桌比喻

想象Claude是一个很聪明的同事，坐在一张桌子前。桌面空间有限——摆在桌上的东西就是它此刻能看到、能想到的全部。

Tw93把"什么东西该放在哪"分了五层：

| 层 | 比喻 | 特点 |
|---|------|------|
| **CLAUDE.md** | 贴在显示器上的便签 | 永远在眼前，每一秒都在看 |
| **Rules** | 抽屉里按主题分类的手册 | 做特定任务时自动拉出来 |
| **Skills / Commands** | 标准操作流程卡 | 你说"做这个"时才摆上桌 |
| **Subagents** | 派任务给隔壁同事 | 结果带回来，过程不占你的桌 |
| **Hooks** | 办公室自动化系统 | 桌上完全看不到，但活默默干了 |

原则很简单：**偶尔用的东西就不要每次都放在桌上。**

## Boris的Best Practices = 桌面管理术

### "投资CLAUDE.md，每次纠正后都更新"

CLAUDE.md是贴在显示器上的便签——**每次对话、每一轮交互，它都在。** Tw93量化过：它占2-5K token，而且是固定开销，无法避免。

这意味着：
- 写得好 → 每一轮对话都有正确的指引，Claude始终在正确的轨道上
- 写得烂 → 每一轮都在注入噪音，Claude每一秒都在被错误信息干扰
- 写得太长 → 重要规则被淹没在文字海洋里

所以Boris说"ruthlessly edit"——像打磨slogan一样打磨CLAUDE.md。因为它的影响是乘法效应：好坏都会被放大到每一轮交互中。

### "用slash commands做每天重复的事"

每天做几十次的操作（commit、push、开PR），做成slash command存在`.claude/commands/`里。

桌面逻辑：这些流程卡平时不在桌上，你说"/commit-push-pr"的时候才拿出来用。**用完就收起来，不占常驻空间。** 如果你把这些指令全写在CLAUDE.md里，就是把偶尔用的手册永远贴在显示器上——浪费最宝贵的"永远可见"位置。

### "用subagents保持main context focus"

Boris说"想让Claude投入更多算力时，就加一句'use subagents'"。

桌面逻辑：大任务（搜索整个codebase、分析大量文件）会把桌面堆满。把这些任务**派给隔壁桌的同事**，它在自己的桌上工作，只把结论带回来。你的桌面保持整洁，注意力集中在主线任务上。

关键区别：subagent不是"更多帮手"，而是**注意力隔离**。

### "用hooks做自动格式化"

Boris的PostToolUse hook会在Claude每次改完代码后自动格式化。

桌面逻辑：hooks是办公室自动化——灯到时间自动关、邮件自动归档。**完全不占桌面空间，Claude甚至不知道它在运行。** 相反，如果你让Claude自己去想"代码格式对不对"，那就是让它在桌上额外摆一摊文件来处理一个完全可以自动化的事。

原则：**能让机器自动做的事，就别让Claude花注意力想。** 省出来的注意力给真正需要判断的工作。

### "给Claude一种验证自己工作的方式"（Chrome Extension）

Boris说这是他最重要的建议。Chrome extension让Claude截屏看自己写的网页——等于给了它一面镜子。

桌面逻辑：这面镜子不在桌上，是一个**外部验证工具**。没有镜子，Claude只能凭自己的记忆判断"我写得对不对"——但它看不到真实效果。有了镜子，它能迭代："截图看看→不对→改→再看→好了"。

Boris的原话："Once you do that, Claude will iterate until the result is great."——关键词是iterate。没有验证手段，Claude没有迭代的依据。

### "跑5个并行session"

Boris同时跑5+个Claude，每个做不同的事。

桌面逻辑：**一张桌子做一件事。** 如果你把5个任务塞进同一个session，就是在一张桌上摊开5个项目的文件——互相干扰，全都做不好。5张桌子各做各的，每张桌子都保持整洁和专注。

### "Plan mode先规划，然后一次执行"

Boris的流程：先在Plan mode里反复讨论方案，确认OK后切到auto-accept让Claude一口气执行。

桌面逻辑：**桌子还干净的时候把方向想清楚。** 对话越长，桌上堆的东西越多，Claude的判断力就越差。如果你上来就让Claude边做边想，到了中段桌面已经很杂乱了——这时候发现方向错了，回头代价很高。

Plan mode的价值：在注意力最清醒的时候做最重要的决策。

## 一个检验自己的方法

下次使用Claude Code的时候，可以问自己：

1. **我的CLAUDE.md上次是什么时候更新的？** → 如果超过一周没动，可能已经过时了
2. **有没有什么东西我总是重复告诉Claude？** → 那就该进CLAUDE.md或slash command
3. **我是不是在同一个session里做太多事了？** → 开新session，保持桌面整洁
4. **Claude犯的错，是因为它能力不够，还是因为它没看到正确的信息？** → 大多数时候是后者

## Connections
- Related: [[boris-cherny]], [[tw93]], [[claude-code]], [[context-noise-governance]], [[context-management]]
- Boris的tips是实践层面的"怎么做"；Tw93的分层是认知层面的"为什么这样做有效"
- 两者结合，从"照着做"升级到"理解了所以这样做"

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-bcherny-claude-code-best-practices.md, raw/2026-04-09-tw93-claude-code-architecture-governance.md | Initial creation — cross-cutting synthesis |
