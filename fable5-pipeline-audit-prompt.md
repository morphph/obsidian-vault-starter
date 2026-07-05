# Fable 5 Prompt — Research→Draft 链路审计 + 优化 plan

> 运行建议：effort = `high`（复杂推理/综合任务，别用 low/medium）。工作目录 = 仓库根 `obsidian-vault-starter/`。允许它读文件、跑只读命令；不给写权限也可以，它的产出就是 plan 本身。

---

你在审计一个基于 Obsidian 的内容生产链路。先说清楚这条链路是干什么的，你才知道什么叫「优化」。

**背景 / 意图（这决定了什么是好 plan）**
这是一个 solo AI-content builder 的内容生产主干。它把一个「想写的话题」变成一篇可发布的文章，中间分两段：

- `/research <topic>` → 在 `research/<slug>/` 里产出调研工作区（research-plan + 单份 report + ingest-candidates + meta.json）。report 有固定形状：§1-2 事实、§3-5 分渠道 Top-N、§6 洞察、§7 排序后的「内容角度」+ 时间线。
- `/draft research/<slug>/` → 从 report 的 §7 某个角度切入，写出 `drafts/<name>.md`，人再润色发布。

这条链路的价值 = **用最少的人工摩擦，把一个话题可靠地变成有事实支撑、且按 GEO/AEO 规则写、能被 AI 答案引擎引用的文章**。你的工作是找出这条链路在哪里漏掉质量、漏掉可靠性、或者制造了不必要的摩擦，然后给出一个排好优先级的改进 plan。这个 plan 是给主人自己迭代这套工作流用的，所以要落地、要能直接动手，不要泛泛而谈。

**从哪里读起（入口，不是全集——自己去把链路走通）**
- `CLAUDE.md`（根）——schema，四层模型 + `research/` 非 vault 工作区 + `audience-profile.md` taste anchor
- `research/README.md`——非 vault 工作区的规格 + Tier 边界 + 排除警告
- `audience-profile.md`（根）——读者画像 + Voice + GEO/AEO 写作规则
- `.claude/commands/research.md`、`.claude/commands/draft.md`——`/research`、`/draft` 的完整工作流（真正的逻辑在这两个文件里；没有独立的 `.claude/skills/research|draft/` 目录）
- `.claude/commands/ingest.md`——research→draft 之间那道人工筛选闸门（ingest-candidates → `raw/`）
- `research/loop-engineering/`——唯一一次真实 research 跑出来的工作区（4 个产物齐全），拿它对照 command 里的模板
- `research/_reference/`——目标形状的参考 fixture（注意哪些文件其实还不存在）
- `drafts/`——已有文章，用来验证 research→draft 那道缝到底跑没跑通过
- `research-to-obsidian-handoff.md`（根）——safety invariants / hard-constraints 的出处

别把上面这份清单当成结论。真的去读这些文件，把整条链路从 `/research` 一路走到 `drafts/` 里的成品，形成你自己的判断。

**读的时候要带对镜头（这些词看懂了才读得对，但都要在文件里核对，别信我这几行）**
四层模型 `raw→wiki→drafts→learn`；research report 本身是 **Tier-4 衍生物**（存档级，禁止回流选题/vault，否则「选题引用自己的调研 → 塌缩」）；**事实轴 vs 增长轴** 两个综合镜头；「按渠道采集、按轴综合」；`推断·未实测`（测不到的互动数据必须这么标，禁止编造）；graceful degradation（`bird`/`last30days`/`summarize` 本机没有，缺了要记 warning 继续，不能让整跑失败）；**§7 角度即骨架**（draft 没有中间 outline 产物）；**务实 sourcing 规则**（`sources:` 只放已 ingest 的 `raw/`，其余进 `external-refs:`，load-bearing claim 必须能追到 Tier-1）；GEO 规则（引用 +40%、数字 +37%、前置结论、可扫描、定义句）。

**plan 必须尊重的不变量（违反了就是废 plan）**
- `CLAUDE.md` 的 NEVER 清单（不动 `raw/`、`wiki/` 扁平结构、每条 claim 可溯源、research 产物永不自动进 vault 等）
- 「`CLAUDE.md` 声明 WHAT，skills/commands 定义 HOW」的分层原则
- Tier 阶梯与四层边界
- 主人偏好的工作方式：最小摩擦、skill-first（先技能后 CLI）、`research-to-obsidian-handoff.md` 里的 hard constraints

如果一个改进值得做但会碰到某条不变量，明说这个张力，别偷偷绕过。

**任务**
1. 把 research→draft 这条链路端到端走通、看透细节。
2. 基于你看到的，提一个排好优先级的优化改进 plan。

特别值得盯的地方（不是限定范围，是提示往哪看得深一点）：research→draft 那道缝（§7 角度怎么变成文章、audience-profile 怎么两头喂、务实 sourcing 和 load-bearing flag 到底有没有跑过）；哪里有沉默的人工判断在兜底（去重、dup 检测、GEO 占位符有没有真被填、sha256 手算）；`report.md`/`draft` 的形状只活在 command 模板里、没有 rule/fixture 兜底带来的风险。

**工作方式（自己拿捏，别按我的步骤走）**
读真实文件，别猜。有足够信息就动手判断——不要把已经确定的事实反复重推，不要罗列你并不打算深入的选项；要在几个方案里选就直接给推荐，别写一份穷举综述。你的每一条 gap 和每一条建议都要能指向你**真读过**的某个文件 + 章节作为证据；没核实的就标「未核实」，别当成事实报。

**边界（明确不要做的事）**
- 只读 + 提议。**不要**改或建任何链路/vault 文件，不要跑 `/research` 或 `/draft`，不要动手实施任何改动——这一轮的交付物就是你的评估和 plan。
- 不要为了凑数造问题。链路本来就设计得挺克制，如果某块其实没毛病，就说它没毛病。
- 需要落一个文件时，最多新建一个 plan 的 md，不要编辑任何已存在的文件。

**交付物 / plan 的形状**
开头先给结论：最高杠杆的前 3 个改动，一句话一个，让主人扫一眼就知道最该动什么。然后是完整的排序 plan，每一条：
- 问题（带 文件 + 章节 证据）
- 具体改什么
- 为什么有用（挂回这条链路的价值：质量 / 可靠性 / 摩擦）
- 工作量 + 风险
- 是 quick win 还是结构性改动

按优先级或主题分组。最后给一句：如果只能先做一件事，做哪件，为什么。

**沟通风格（最终这份 plan 的写法）**
结论先行：第一句说清「链路现在最大的问题是什么 / 我最建议先做什么」。之后才是支撑细节。要好读，不要为了短就压成箭头链、缩写、生造的标签——主人没看过你中间的推理过程，每个文件名/章节/术语都给它一句人话说清是什么。宁可清楚，不要简短。
