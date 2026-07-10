# Outline: 给目标不给步骤 —— Thariq 的「四象限 unknowns」怎么用在 Fable 5 上
> 基于角度: report §7 角度3（作者 2026-07-10 回炉选定，替换此前机器选的角度1）· 目标渠道/形式: 中文精读长文（GEO 优化）+ EN 镜像；与 WF1 白板视频（同源 Thariq 文）联动互链

## prior_coverage（强制字段——对「已表达角度清单」逐条声明关系）
- **无旧发布角度——首次覆盖该话题**。drafts/ 此前的 fable-5 稿是角度1（迁移清单）的**未发布**草稿，
  已作废归档（`research/best-practices-for-claude-fable-5/drafts-angle1-archive/`），非已表达角度。
- `raw/2026-07-08-fable-finding-your-unknowns.md`（Thariq 一手源，已在库）→ 本文的**主源**：
  借它的四象限框架 + 金句，但角度是「每格未知 × 一个 Fable prompting 动作」的落地对接，
  Thariq 原文讲心法、本文讲操作——**新证据推进，非重合**。
- **与 WF1 白板视频同源联动**（同一篇 Thariq 文）：视频 = 精读讲解（图为脊柱），本文 = 落地操作
  （动作为脊柱）——跨形态复用，角度不同，发布后互链。
- 相邻 vault 页 [[claude-opus-4-7]] / [[xhigh-effort-level]] / [[adaptive-thinking]] → 前代框架，本文只在
  「给目标+理由」动作处引一句对照，不展开。

## take（Gate 1 —— 作者 2026-07-10 选定角度3，take 由会话代录作者决策；Gate 2 审稿首问仍是「愿不愿署名」）
> X 上的 Fable 教程都在教「怎么把 prompt 写得更好」，但 Fable 是第一个瓶颈不在 prompt 措辞、
> 而在「你能不能澄清自己未知」的模型——功夫在 prompt 之外。Thariq 的四象限是目前唯一把这个
> 瓶颈拆到可操作的框架，而它正好能和官方「给目标不给步骤」原则对接：每一格未知，对应一个
> 具体的 Fable 动作。只给目标不挖未知，你给的目标本身就可能是错的。对 builder 的含义：
> 升级到 Fable 之前先升级你的提问方式——最贵的 bug 藏在你从来没写下来的那句话里。

## 结构（逐节: 论点 + 挂哪些 report 论断/出处 + 预估篇幅占比）
> 写法纪律（对标 loop-engineering-guide 的成稿感，2026-07-09 差异对比结论烘焙于此）：
> ① 开场用叙事锚，不用清单腔；② 早给一段「地图」再逐节展开；③ 同源引注首提留链、
> 后文裸述，文末「参考来源」聚合；④ 全角标点、粗体只留判断句、无「工作论点/三句话收尾」
> 等脚手架标签；⑤ 正文自然织入 /zh/blog、/zh/glossary 内链。

1. **叙事锚开场** — Thariq 帖 3.35M views、2 万 bookmarks 的现象级传播 + 他那句「Fable 是第一个
   让我觉得，工作质量被『我澄清未知的能力』卡住的模型」——瓶颈为什么换了位置 —
   证据: [内部/Tier-1: raw fable-finding-your-unknowns] — ~10%
2. **地图段：官方原则缺了半句** — 官方 guide 说「给目标不给步骤」，但没告诉你：目标错了怎么办。
   答案 = 先挖未知再定目标；引出地图≠疆域 + 四象限总览（一段话 + 一张结构预告，全文挂此地图）—
   证据: [外部: prompting-guide] [内部/Tier-1: raw] — ~12%（GEO: 前置定义句「四象限 unknowns 是……」+
   角色化入口一行：写代码的 / 用 agent 跑长任务的 / 带团队的分别重点看哪节）
3. **四象限逐格 × Fable 动作**（主体）— 每格 = 一句定义 + 你怎么识别自己在这格 + 一个当场可抄的
   Fable 动作：已知的已知→「大任务+受众+产出价值+请求」目标模板；已知的未知→让 Fable 反向访谈你
   （一次一问、先问改变架构的）；未知的已知→原型逼隐性标准出水 + 参照物直接指向源代码；
   未知的未知→盲区扫描（blindspot pass 原话模板）—
   证据: [内部/Tier-1: raw]（四象限+全部动作原文）[外部: prompting-guide]（give goals/context 原则）— ~40%
4. **串成流程：实现前中后** — 五个便宜探测→实现笔记（Deviations 记账）→推介+测验（考满分才 merge）；
   一句点破：这是把四象限动作按时间轴排开，不是新增负担 —
   证据: [内部/Tier-1: raw] — ~15%
5. **经济学收束** — cheap now < expensive later；Simon Willison 实测「一天 $110 干完几天的活」的
   数字压轴：模型越贵，挖未知的杠杆越大 —
   证据: [外部: simonwillison.net Initial impressions] [内部/Tier-1: raw] — ~10%
6. **行动清单 + 向前踢** — 五条从今天开始的动作（下个项目第一句话就让 Claude 找 unknowns…）；
   收尾互链：这套「先挖未知再设计循环」正是 [loop-engineering](/zh/blog/loop-engineering-guide) 的
   前置功课；预告同源白板视频版 —
   证据: 全文回收 — ~8%（收尾禁标签化，仿标杆结语）
7. **参考来源**（文末聚合段）— Thariq X Article / 官方 prompting guide / 官方 intro / Simon Willison。

## GEO 块（成稿 frontmatter 必带；publish 链 _extract_article 现只透传 title/desc，其余先随稿带着）
- description（手写摘要，非首段截断）: zh =「Claude Fable 5 的瓶颈不在 prompt 措辞，在你能不能澄清
  自己的未知。本文把 Thariq（Anthropic Claude Code 团队）的四象限 unknowns 框架拆成四个当场可抄的
  Fable 动作：目标模板、反向访谈、原型+参照源码、盲区扫描，附实现前中后完整流程。」en 镜像同义。
- keywords: claude fable 5, unknowns, 四象限, finding your unknowns, thariq, give goals not steps,
  blindspot pass, agentic coding, prompting, implementation notes
- category: techniques · related_blog: loop-engineering-guide · related_glossary: claude-code, claude

## 溯源注记
- 载重主张主源 = raw Thariq（**已在库**，比角度1 的溯源缺口轻得多）；官方 guide / intro / Simon 的
  论断维持 external-refs 标注（三篇官方源 ingest 与否，Gate 2 时作者再拍）。
- report.md 本身不可被成稿引用（纪律照旧）。
