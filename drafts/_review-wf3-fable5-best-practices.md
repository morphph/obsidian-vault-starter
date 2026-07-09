# WF3 Gate 1 · 待你的 take —— Best Practices for Claude Fable 5

> 状态：**卡在 Gate 1（take 闸）**。writer 无 take 不开工。
> 你只需给 **3–5 句亲笔 take**：thesis / 不同意主流叙事哪点 / 对 AI builder 的含义。
> 给法：直接在本文件「👉 你的 take」处写下来（写完告诉我一声），或在 Telegram 回我口述。
>
> 角度：report §7 角度1 · 目标形式：中文博客长文（GEO 优化）· 调研成本 28 turns / $3.10
> 原始调研产物在 VPS：`research/best-practices-for-claude-fable-5/`（outline.md / report.md / research-plan.md）——research/ 是 Tier-4 scratch，不进同步 vault，所以本 review note 是它的可读镜像。

---

## 👉 你的 take（在这里写，3–5 句）

（待填）

---

## prior_coverage（与已表达角度的关系）
- **首次覆盖**：drafts/ 无 Fable 5 成稿，wiki/ 无 Fable 页。
- 唯一相关内部存量：`raw/2026-07-08-fable-finding-your-unknowns.md`（Thariq 一手源，**是 source 不是已发角度**）。可复用其素材（四象限、金句），但角度不同：Thariq 讲「厘清 unknowns 的心法」，本文讲「Opus→Fable 的**具体迁移动作清单**」——新证据推进，非重合。
- 相邻 vault 页 [[claude-opus-4-7]] / [[xhigh-effort-level]] / [[task-budgets]] / [[adaptive-thinking]] 讲的是 Opus 4.7 三件套；本文是**这套框架在 Fable 5 上的升级/变化**——不同模型，明确推进。

## 候选 thesis（供你取舍，非定稿）
主流 X 帖把 Fable 当「更强的 Opus」来教 prompt，但真正的迁移成本不在 prompt 措辞，而在 **harness 契约（超时/异步/进度 UI）+ 兜底逻辑（refusal）+ skill 瘦身（prune prescriptive）**——这三处不改，换了 Fable 反而更差。

## 结构（8 节 · 论点 + 挂哪些证据 + 预估篇幅）
1. **一句话价值 + 谁该读**（~8%）— Fable 5 = 最难长时程任务的顶层模型，$10/$50，用法和前代反着来。GEO：前置定义句 +「独立 builder / 内容创作者 / 团队 lead」角色化入口。
2. **心智切换：从「给步骤」到「给目标+给理由」**（~18%）— 前代 prescriptive skill 现在是枷锁，需 prune。含「给理由」模板。
3. **effort 是新主拨盘**（~14%）— 默认 high / first-shot 才 xhigh / 日常降级仍胜前代。GEO：low/medium/high/xhigh 对比表 + 具体数字。
4. **harness 契约变了：长 = 数分钟到数小时**（~16%）— 迁移前先改超时 / 异步查进度 / 别显示 token 倒计时。
5. **拒答会咬你：安全分类器 + Opus 4.8 兜底**（~16%）— refusal 走 HTTP 200、善意任务也误触、redeploy 后误拒升高 → 兜底非可选。含伪代码。
6. **让它自主：memory / subagent / verifier / send_to_user**（~14%）— 并行 subagent + fresh-context verifier + memory 文件 + 自主 system reminder。
7. **成本与路由：别全流量上 Fable**（~10%）— 80–90% 留 Sonnet/Opus，只升级最难长时程。挂 simonwillison $110/天实测。
8. **收尾：迁移前/后对照 checklist**（~4%）— 全文压成一张可扫描表。

> GEO 落地提醒（交给 /draft 时执行）：第 1/3/5 节要真的填上「定义句 / 对比表 / 伪代码」；第 2/5/7 节要真的填「官方链接 + 具体数字（$10/$50、<5%、128k、80–90%）」，否则 GEO 规则失效。
