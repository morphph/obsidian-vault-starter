---
status: draft
take: waived            # 作者显式豁免 take（WF3 TAKE_OPTIONAL, 2026-07-09）；下文 thesis 为编辑立场工作论点，非作者亲笔
lang: zh
sources:
  - raw/2026-07-08-fable-finding-your-unknowns.md
external-refs:          # 载重主张所依赖的官方源尚未 ingest —— 见文末「溯源与待办」
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - https://www.anthropic.com/news/claude-fable-5-mythos-5
  - https://www.anthropic.com/news/redeploying-fable-5
  - https://simonwillison.net/2026/Jun/9/claude-fable-5/
  - https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026
  - https://x.com/trq212/status/2073100352921215386
research: research/best-practices-for-claude-fable-5/
platform: blog
created: 2026-07-09
last-updated: 2026-07-09
tags: [draft]
---

# Claude Fable 5 最佳实践：从 Opus 到 Fable 的迁移清单

X 上现在到处是「Fable 5 的 10 条 prompt 技巧」。它们大多把 Fable 当成「更强的 Opus」来教你——换个措辞、堆几个 few-shot、把 prompt 写得更狠。

但如果你真的把线上流量切过去，你会发现第一个咬你的不是 prompt 措辞，而是别的东西：请求跑了六分钟客户端超时断了、一个善意的安全脚本任务被拒了却返回 HTTP 200、你精心写的旧 skill 反而让产出变差。

**这篇不是又一份「怎么 prompt Fable」清单。这是一份「你原来这么用 Opus，换 Fable 该改哪几处」的迁移清单——每条都挂官方出处。**

## 谁该读这篇 · 一句话价值

**定义先行**:Claude Fable 5(`claude-fable-5`,2026-06-09 GA)是 Anthropic 面向**最难的长时程任务**的旗舰模型——1M context、单次最多 128k output token、$10/M input 与 $50/M output 定价、只有 adaptive thinking、raw chain-of-thought 永不返回([官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5))。

它的最佳实践和前代**反着来**:前代模型你要**给步骤、给清单**;Fable 你要**给目标、给理由**,让它自己想怎么做([官方 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5))。

**这篇文章的工作论点(编辑立场):** 主流科普帖把迁移成本算在「prompt 怎么写」上,算错了。真正的迁移成本在三处基础设施——**① harness 契约(超时 / 异步查进度 / 进度 UI)、② 兜底逻辑(refusal → Opus 4.8)、③ skill 瘦身(prune 掉旧的 prescriptive 指令)**。这三处不改,你换了 Fable 只会更差、更贵、更容易在生产里翻车。

**角色化入口——对号入座:**
- **独立 builder**:你最该先做的是 §1(prune 旧 skill)和 §2(把 effort 当主拨盘)。这两处零成本,立刻见效。
- **内容创作者 / 用 agent 跑长任务的人**:重点看 §3(harness 契约)和 §5(memory + send_to_user),它们决定你的长跑任务会不会中途死掉。
- **团队 lead / 做集成的人**:§4(refusal 兜底)和 §6(成本路由)是你上线前的两道闸——省不得。

---

## 1. 心智切换:从「给步骤」到「给目标 + 给理由」

前代模型能力弱,你得手把手:精确规定每一步、枚举每种边界、写满 prescriptive 的 skill 文件。**这套习惯在 Fable 上是枷锁。**

Fable 被造来**吸收模糊、自己补「怎么做」**。官方 prompting guide 的第一条就是:给目标不给清单,过度规定反而拉低产出([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5))。所以迁移第一步不是写新 prompt,而是**审计并删减旧的 skill**:那些为弱模型写的「必须先做 A 再做 B、遇到 C 要怎样」的详细步骤,现在多半是负资产。

> 这正是「假设会过期」的又一实证——你为上一代模型写下的约束,会在下一代模型上变成枷锁。每次模型升级,旧 skill 都值得重审一遍。

**给理由,而不只是给指令。** Fable 在有上下文时判断更准。用这个模板:

> "I'm working on [大任务] for [谁]. They need [产出使能什么]. With that in mind: [具体请求]."

（「我在为 [谁] 做 [大任务],他们需要 [产出能带来什么]。基于这个背景:[请求]」）

有了「为什么」,当你的指令和现场情况冲突时,Fable 知道该往哪个方向 veer(偏转),而不是机械照做一条已经不合适的指令。Thariq(Claude Code @ Anthropic,Fable 的一手 driver)把这件事讲得最透:指令太具体,Claude 会在该转向时仍死守你的话;太模糊,它会拿行业默认做法填空,而那未必合你的场景([Thariq, "Finding Your Unknowns"](https://x.com/trq212/status/2073100352921215386))。给理由,就是给它一把判断「什么时候该偏转」的尺子。

**动作清单:**
- [ ] 打开你现有的 skill / system prompt,删掉为弱模型写的分步规定,只留目标和约束。
- [ ] 把关键请求改写成「大任务 + 受众 + 产出价值 + 请求」四段式。
- [ ] 加一句抑制过度发挥的话:"do the simplest thing that works well,别超需求地重构、加抽象、处理不可能发生的情况"——高 effort 下的 Fable 容易过度设计,一句话就能收住。

---

## 2. effort 是新的主拨盘

前代你调 thinking budget;Fable 把它简化成一个拨盘:**effort**,四档 `low / medium / high / xhigh`,默认 `high`([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5))。

同时要知道:Fable **只有 adaptive thinking 这一种模式**,不支持关闭 thinking、没有 extended-thinking 预算,而且 **raw chain-of-thought 永不返回**——你只能拿到 `summarized` 或(默认)`omitted` 的 thinking block([官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5))。所以「调 thinking」这件事,现在就等于「调 effort」。

| effort 档 | 什么时候用 | 代价 / 注意 |
|-----------|-----------|------------|
| `low` / `medium` | 日常任务、批量处理、成本敏感场景 | 官方说法:即便降档,日常质量仍胜前代的 xhigh。先降档,不够再往上 |
| `high`(默认) | 绝大多数正经任务的起点 | 单次请求在 high 下可跑**数分钟**——先把客户端超时改好(见 §3) |
| `xhigh` | **first-shot 一次做对**比速度更重要的关键任务 | 最慢最贵;别默认开。留给「重跑代价高、必须一次对」的场景 |

**迁移动作:** 不要无脑把所有请求拉到最高档。默认停在 `high`;只有当「一次做对」的价值明显压过延迟和成本时,才升 `xhigh`;日常和批量任务大胆降到 `medium/low`。这条继承自 Opus 4.7 的 effort 框架,但在 Fable 上 effort 成了**首要**拨盘——权重比以前更高。

---

## 3. harness 契约变了:「长」= 数分钟到数小时

这是最容易被科普帖漏掉、却最容易在生产里咬你的一处。

Fable 的「长时程」是字面意义的长:**单次请求在 high effort 下可跑数分钟,自主运行可延续数小时甚至数天**([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5))。你为 Opus 写的客户端——30 秒超时、同步等返回、前端转个圈——会直接崩。

**迁移前必须先改 harness,这是前置项,不是优化项:**

1. **拉长客户端超时。** 按「分钟到小时」重设,而不是秒。同步阻塞等一个可能跑几分钟的请求是自杀。
2. **改成异步查进度。** 别阻塞等返回;发起任务后轮询 / streaming 查状态。
3. **别显示「剩余 token / context 倒计时」。** 这是反直觉但关键的一条:如果 UI 把「你还剩多少 context」暴露给模型,Fable 会因此**提前收尾**,或主动建议你「我们该开个新会话了」——本可继续的长任务被你自己的进度条掐断了。

> 这一条呼应我们追踪已久的 context-anxiety 现象:模型看到「快没空间了」的信号,会像人赶 deadline 一样仓促结尾。**解法是别把倒计时喂给它。**

Simon Willison 的独立实测印证了这个量级:他称 Fable「a beast——slow, expensive」,一天烧掉 **$110**,但一次干完了「several days' worth of work」(好几天的活),还实测了 human-in-the-loop 的暂停 / 续跑([Simon Willison, "Initial impressions"](https://simonwillison.net/2026/Jun/9/claude-fable-5/))。慢和贵是特性不是 bug——但你的 harness 得先扛得住「慢」。

---

## 4. 拒答会咬你:安全分类器 + Opus 4.8 兜底

如果这篇你只改一处,改这处。

Fable 对三个领域跑安全分类器:**进攻性网络安全、生物 / 生命科学、reasoning-extraction(试图套取 summarized thinking 的行为)**([官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5))。触发时的行为有三个坑,每个都能让没准备的集成翻车:

1. **拒答走 HTTP 200,不是 error。** 返回体里是成功的 `stop_reason: "refusal"`,并指明哪个分类器触发了。你按「非 200 才是失败」写的错误处理会**静默漏掉**它。
2. **善意任务也会误触(false positive)。** 一个正当的安全审计脚本、一段生物信息学分析,都可能被拒。官方明确承认这类 false positive 存在。
3. **redeploy 之后误拒率更高了。** Fable 曾在 **2026-06-12 下架**(美国出口管制 + Amazon 报告的一个绕过安全措施的越狱),**2026-07-01 完整重部署**;改进后的分类器在 >99% 情况下拦住了那个越狱技术——**代价是更多 false positive**([redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5))。也就是说,误拒不是会随时间消失的临时现象,而是这次安全修复的**已知代价**。

好消息:官方把兜底路径铺好了。**保护措施平均只在 <5% 的会话触发;拒答(在出 output 前发生)不计费;fallback 时退还 prompt-cache 的切换成本**;官方直接建议**服务端或客户端 fallback 到 Opus 4.8**([官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5))。

**所以兜底不是可选项。** 最小实现:

```python
# 伪代码:refusal 兜底到 Opus 4.8
resp = call_model("claude-fable-5", request)

# 坑:refusal 是成功的 HTTP 200,不是 error —— 必须显式检查 stop_reason
if resp.stop_reason == "refusal":
    log.warn(f"Fable refused via classifier: {resp.refusal_classifier}")
    # 官方推荐:直接兜底到 Opus 4.8;拒答未出 output,不计费
    resp = call_model("claude-opus-4-8", request)

return resp
```

**别踩的额外一坑:别让 Fable 复述 / 逐字输出它的推理过程**——这会触发 reasoning_extraction 分类器、推高拒答率。需要看它想什么,读 `summarized` thinking block 就够了,别在 prompt 里要求它把 chain-of-thought 打出来([官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5))。

---

## 5. 让它自主:memory / subagent / verifier / send_to_user

Fable 的卖点是**自主长跑**——更强地派发并维持并行 subagent、更长时程地目标导向运行([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5))。要把这个能力真正用起来,配四件事:

**① 建 memory 系统(Markdown)。** 一课一文件、文件顶部一行摘要、把「纠正过的做法」和「确认有效的做法」都记下来。让 Fable 在开始新任务前先复盘旧会话的 memory 来 bootstrap——它自己的经验就成了下一次的起点。

**② 放开用并行 subagent,优先 async。** 用非阻塞编排让多个 subagent 并跑;long-lived subagent 靠 cache read 省成本。

**③ 用 fresh-context verifier,而不是自我批判。** 官方推荐:让一个**全新上下文**的 verifier subagent 来检查产出,而不是让原模型自评。这一条印证了我们一直说的:模型自评有 self-evaluation bias,换一个没被原任务上下文污染的 verifier 更靠谱。

**④ 建 `send_to_user` tool + 配套 system reminder。** 长 async agent 需要一个专门的 tool 把逐字交付 / 进度**送达用户而不结束 turn**(tool input 永不被 summarize,内容不会丢)。两个配套纪律:
- 必须在 system prompt 里明确指示它用这个 tool,否则模型很少主动调。
- 给自主管线加一句 system reminder:**「你在自主运行,用户没盯着」**——防它停在问权限、或以「I'll now run X」这类承诺结尾却不真的调工具。

**再配一条 grounding 纪律:** 要求 Fable 把每一条进度 claim 都对照实际的 tool 结果核验。这几乎能消除长跑中最烦人的「假状态报告」——它声称做了某事,其实没有([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5))。

**checkpoint 只在三种情况暂停:** 破坏性 / 不可逆动作、真实的 scope 变更、只能人来提供的输入。别枚举每一种可能情况——Fable 的指令遵循够强,一句简洁的边界规则比一张详尽清单更有效。

---

## 6. 成本与路由:别把全流量切上 Fable

$10/$50 的定价让「什么都上 Fable」在经济上说不通。社区已形成的路由共识(⚠️ 非官方,来自 [DigitalApplied](https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026) 的家族对比框架):**把 80–90% 的流量留在更便宜的 Sonnet 5 / Opus 4.8,只把最难的长时程任务升级到 Fable。**

一个好用的心智模型是家族分层:**Sonnet 5 管执行、Opus 4.8 管判断、Fable 5 管最难的长时程升级**(⚠️ 社区综合措辞,多源一致但非官方原话)。

**反直觉但重要的一条——往高打,别往低打。** 想真正评估 Fable 值不值,把你**最难的、还没解决的问题**丢给它,让它自己 scope、问你澄清问题;只拿简单任务测,你只会低估它。Thariq 说 Fable 是第一个「产出被我澄清 unknowns 的能力卡住」的模型([Thariq, "Finding Your Unknowns"](https://x.com/trq212/status/2073100352921215386))——意思是瓶颈已经从「模型能力」移到了「你把问题讲清楚的能力」。用简单任务测,你根本碰不到这个瓶颈,也就看不到它的上限。

> ⚠️ **定价核对提醒:** 只有 Fable 的 **$10/$50** 是官方确认的。二手源对 Sonnet 5 报价互相矛盾($2/$10 vs $3/$15),做家族成本对比时,Sonnet/Opus 的价一律当「待核」。

---

## 迁移前 / 后对照 checklist

<!-- CTA: [placeholder for closing call-to-action] -->

把全文压成一张可扫描表——这就是你的迁移动作清单:

| 维度 | 你原来对 Opus 这么做 | 换 Fable 该改成 |
|------|---------------------|----------------|
| **skill / prompt** | 写详细分步、枚举边界 | prune 掉 prescriptive 步骤,给目标 + 给理由 |
| **effort** | 调 thinking budget | 默认 `high`,关键任务 `xhigh`,日常降 `medium/low` |
| **客户端超时** | 秒级 | 分钟到小时级 |
| **进度查询** | 同步阻塞等返回 | 异步 / streaming 轮询 |
| **进度 UI** | 显示 token 倒计时 | **别显示**倒计时(否则它提前收尾) |
| **错误处理** | 只看非 200 | 显式检查 `stop_reason: "refusal"`(它走 200) |
| **兜底** | 无 / 重试 | refusal → **Opus 4.8 fallback**(必备) |
| **推理输出** | 随便让它 think out loud | 别要求复述 CoT(触发 reasoning_extraction 拒答) |
| **verifier** | 让模型自评 | fresh-context verifier subagent |
| **memory** | 无 | Markdown memory,一课一文件,复盘 bootstrap |
| **路由** | 单模型 | 80–90% 留 Sonnet/Opus,只升级最难长时程 |

**三句话收尾:** 换 Fable,别先急着改 prompt 措辞。先改三处基础设施——**harness 扛得住长跑、集成接得住 refusal、旧 skill 瘦得下来**。这三处改到位,Fable 才会像官方说的那样,一次干完你好几天的活;改不到位,它只会更贵、更容易在生产里翻车。

---

## 溯源与待办(给定稿前)

> ⚠️ **载重主张的 raw/ 溯源缺口(WF3 headless 自检):** 本文绝大多数载重主张(effort 拨盘、refusal 行为、harness 契约、路由经济学)依赖的是**尚未 ingest 进 `raw/` 的官方源**——它们目前只在 `external-refs` 里。按项目规则「载重主张须由 raw/ 源背书」,**定稿前强烈建议先 `/ingest` 以下官方源**:
> - `prompting-claude-fable-5`(§6 几乎每条最佳实践的原始出处)
> - `introducing-claude-fable-5-and-claude-mythos-5`(§1 事实骨架:定价 / refusal / adaptive-thinking)
> - `redeploying-fable-5`(下架 → 重部署 + 误拒率代价)
>
> 唯一已在 `raw/` 的源是 Thariq 的 "Finding Your Unknowns",本文只把它当**色彩 / 概念背书**,未让它承担核心事实。
>
> 另:知识截止 2026-01,Fable 5 于 2026-06 发布——**§1 全部事实依赖外部一手源**,ingest 时请逐条核验官方 URL。
