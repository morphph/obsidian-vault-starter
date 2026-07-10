# Outline: 从 Opus 到 Fable —— 一个中文 builder 的 Fable 5 迁移清单
> 基于角度: report §7 角度1（推荐）· 目标渠道/形式: 中文博客长文（GEO 优化）

## prior_coverage（强制字段——对「已表达角度清单」逐条声明关系）
- **无旧发布角度——首次覆盖该话题**。drafts/ 里没有任何 Fable 5 成稿；wiki/ 无 Fable 页。
- 唯一相关内部存量：`raw/2026-07-08-fable-finding-your-unknowns.md`（Thariq 一手源，**是 source 不是已表达角度**）
  → 本文可**复用**其素材（四象限、金句），但角度不同：Thariq 讲「厘清 unknowns 的心法」，本文讲
  「Opus→Fable 的**具体迁移动作清单**」。**新证据推进，非重合**。
- 相邻 vault 页 [[claude-opus-4-7]] / [[xhigh-effort-level]] / [[task-budgets]] / [[adaptive-thinking]]
  → 讲的是 Opus 4.7 的三件套；本文是**这套框架在 Fable 5 上的升级/变化**，**不同模型、明确推进**。

## take 占位（Gate 1 由作者填,3–5 句: thesis / 不同意主流叙事哪点 / 对 AI builder 的含义）
> ⏳ 待作者 take —— 本 outline 的每个主张段都要能挂到 take 上，writer 无 take 不开工。
> 候选 thesis 方向（供作者取舍，非定稿）：主流 X 帖把 Fable 当「更强的 Opus」来教 prompt，
> 但真正的迁移成本不在 prompt 措辞，而在 **harness 契约（超时/异步/进度 UI）+ 兜底逻辑（refusal）+
> skill 瘦身（prune prescriptive）**——这三处不改，换了 Fable 反而更差。

## 结构（逐节: 论点 + 挂哪些 report 论断/出处 + 预估篇幅占比）
1. **一句话价值 + 谁该读** — 论点: Fable 5 = 最难长时程任务的顶层模型，$10/$50，用法和前代反着来 —
   证据: [外部: introducing-fable-5 URL] [外部: prompting-guide URL] — ~8%
   （GEO: 前置定义句「Claude Fable 5 是……」+ 角色化入口「独立 builder / 内容创作者 / 团队 lead」）
2. **心智切换：从「给步骤」到「给目标+给理由」** — 论点: 前代的 prescriptive skill 现在是枷锁，需 prune —
   证据: [外部: prompting-guide] [内部/Tier-1: assumptions-expire] — 含「给理由」模板 — ~18%
3. **effort 是新主拨盘** — 论点: 默认 high / first-shot 才 xhigh / 日常降级仍胜前代 —
   证据: [外部: prompting-guide] [内部/Tier-1: xhigh-effort-level] [内部/Tier-1: adaptive-thinking] — ~14%
   （GEO: 加对比表 low/medium/high/xhigh + 具体数字）
4. **harness 契约变了：长 = 数分钟到数小时** — 论点: 迁移前先改超时/异步查进度/别显示 token 倒计时 —
   证据: [外部: prompting-guide] [内部/Tier-1: context-anxiety] [内部/Tier-1: task-budgets] — ~16%
5. **拒答会咬你：安全分类器 + Opus 4.8 兜底** — 论点: refusal 走 HTTP 200、善意任务也误触、redeploy 后误拒升高 →
   兜底非可选 — 证据: [外部: introducing-fable-5] [外部: redeploying-fable-5] — 含伪代码 — ~16%
6. **让它自主：memory / subagent / verifier / send_to_user** — 论点: 并行 subagent + fresh-context verifier +
   memory 文件 + 自主 system reminder — 证据: [外部: prompting-guide] [内部/Tier-1: verification-loops] — ~14%
7. **成本与路由：别全流量上 Fable** — 论点: 80–90% 留 Sonnet/Opus，只升级最难长时程 —
   证据: [外部: digitalapplied（标⚠️社区共识）] [外部: simonwillison 的 $110/天实测] — ~10%
8. **收尾：一张迁移前/后对照 checklist** — 把全文压成一张可扫描表（GEO: 结构化自包含）— ~4%

> GEO 落地提醒（给 /draft）：第 1/3/5 节标了「加定义句/对比表/伪代码」，第 2/5/7 节标了「加官方链接 +
> 具体数字（$10/$50、<5%、128k、80–90%）」——正文必须真的填上，否则 GEO 规则失效。
