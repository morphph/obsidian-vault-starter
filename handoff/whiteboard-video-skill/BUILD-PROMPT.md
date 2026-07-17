# Fable 5 Prompt — 造一个「话题 → 白板讲解视频」skill

> 运行建议：模型 `claude-fable-5`，effort = `high`（复杂的多组件工程任务；别用 low/medium）。工作目录 = 仓库根 `obsidian-vault-starter/`。给读写 + 跑命令权限。这活儿大、跑得久——单次可能跑很多分钟，正常。先出方案、对齐关键决策，再动手建。

---

你要造一个 Claude Code skill。先说清楚它是干什么、给谁用、为什么——你才知道什么叫「造对了」。

**背景 / 意图（这决定了什么是好 skill）**
主人是一个 solo AI-content builder（新加坡，增长营销 + 独立 AI 内容，中英双语，项目 blog2video / AI精读）。他想**批量生产**一类短视频,形式是被验证过的:*「You Can Learn X in N Minutes」*——在一块手绘白板上,把一整个系统从最简单的积木讲起,技术/非技术的人都看得懂。示例话题:*「12 分钟学会 Claude Code 和 Agentic Coding」*。

他手上有一个参考视频(Sean's AI Stories),已经被拆成两半:**说了什么**(transcript)+ **长什么样**(逆向出来的 visual-style-prompt)。这个 skill 的使命,就是拿这两半当**风格靶子**,给任意话题生成同一个模子里的全新视频。

这条链路的价值 = **主人丢一个话题,就能可靠地得到一支 Sean 风格的白板讲解视频(脚本 + 字幕 + 音频 + 成片),中间只在关键处等他拍板一次**。你造的 skill 好不好,就看它能不能稳定产出这个,且不逼主人在昂贵的渲染前盲赌。

**从哪里读起(入口,不是全集——自己把参考和仓库资源摸透)**
- `references/sean-whiteboard-explainer/note.md`——**先读这个**,它讲清楚风格靶子怎么用
- `references/sean-whiteboard-explainer/visual-style-prompt.md`——要复现的**视觉 DNA**(布局 / 配色带 hex / 手绘图示 / 运镜 / 节奏)。成片应该看起来像是从这份 prompt 产出来的
- `references/sean-whiteboard-explainer/transcript.md`——要模仿的**旁白口吻和结构**(一个贯穿的例子、比喻优先于术语、~150 wpm、「let me walk you through this」的口气)。注意:模仿的是**口吻**,不是内容——内容来自话题的调研
- `references/sean-whiteboard-explainer/captions.srt`——字幕格式参考
- `HANDOFF.md`(本文件同级)——完整背景、已定决策、留给你的决策
- 仓库里可复用的东西:`.claude/skills/excalidraw-diagram/`(生成 `.excalidraw` JSON,用来做白板)、`remotion-best-practices` skill(Remotion = React 视频,用来渲染)、`.claude/skills/research/`(已有的话题调研工作流)、`CLAUDE.md`(仓库规约:CLAUDE.md 声明 WHAT,skill 定义 HOW;新工具要按「Documentation Layers」表登记)

别把这份清单当结论。真去读、真去把 excalidraw / remotion 两个 skill 跑通看它们能给你什么,形成你自己的判断。

**复用优先——这条链路大半已经存在,先摸清再决定造什么(别重造轮子)**
主人另外两个项目合起来几乎就是这个 skill。你要有这三个仓库的读权限:
- **content-ops**(`/Users/yufanp/Desktop/Project/content-ops`)——**编排的形状已经有了**。WF3 = `话题 → 深调研 → 作者复审闸 → 产出发布`;WF1 = `URL → 精读 → 白板 → 闸 → 渲染 → 打包`,全程写中央 ledger。**这个 skill 本质就是「把输出格式钉成 Sean 白板模板的 WF3」**。读 `.claude/commands/WF3.md`、`WF1.md` 当编排蓝本——话题前门、复审闸、ledger 纪律都已解决,别从零发明。
- **blog2video**(`/Users/yufanp/Desktop/Project/blog2video`)——**渲染层已经有了,而且它不是单个渲染器,是一个按格式分的视频模板库**(`.claude/skills/`:`faceless-explainer`、`website-to-video`、`product-launch-video`、`slideshow`、`talking-head-recut`…),底下是共享的 **HyperFrames 动画引擎 + Remotion 渲染 + 接好的 TTS**。离你最近的是 **`faceless-explainer`**(话题 → 纯发明式视觉的讲解视频)。Sean 的手绘「N 分钟学会 X」白板,基本就是**这个家族里的一个新模板**(更长、单块 Excalidraw 画布、白板视觉系统)。复用它的引擎 + TTS,**别在 vault 里另起一套 Remotion+TTS**。
- **「让主人挑模板」这件事 blog2video 已经解决**:它靠 `/hyperframes` + 每个模板自述里的路由规则在格式间转派。所以你是**往这个路由里加一个模板**,不是从头造一个菜单。两种入口都要照顾:① 「12 分钟讲 X」这类把格式写进话题的,直接路由到白板模板;② 先跑 WF3 式调研、到渲染时再从菜单挑模板(白板 / faceless-explainer / slideshow…)。
- **一个大决策,先提议别默认**:既然渲染和编排都在别的 repo,这**到底还是不是一个 vault skill**?还是真正形态是「**在 blog2video 里加一个白板模板 + 在 content-ops 里做 WF3 式话题前门**」,vault 只留 Sean 参照 + Excalidraw 白板作画?把三个 repo 都读一遍再提议每块落在哪、怎么跨库够到。vault 这边仍然拥有:参照(`references/sean-whiteboard-explainer/`)、调研 stash(`research/`)、Excalidraw 白板作画。

(详见 HANDOFF.md 的「This is WF3 with the format pinned」一节。)

**这个 skill 要实现的链路(目标,不是给你逐步脚本)**
一个命令、一个话题,跑这条流水线:

1. **调研** — 对话题做深入调研:事实、结构、以及那些让它「可教」的最简积木。
2. **脚本** — 用 Sean 的口吻和结构写旁白,走「N 分钟学会 X」的形式;顺带产出 transcript + 字幕。
3. **白板** — 一块 Excalidraw 画布(手绘感、参考里的配色系统),旁白就沿着这块板走。
4. **【复审闸门】** — 把旁白 + 白板一起给主人看。**在他批准前,不跑任何昂贵的东西。** 这是硬性设计,不是可选项。
5. **音频** — 旁白 TTS。
6. **渲染** — 成片:白板的 pan/zoom 跟着音频走,字幕压进画面。

产出:transcript · 字幕 · 音频 · 成片。

**必须尊重的不变量(违反了就是白造)**
- **复审闸门是硬的**:skill 必须在「旁白 + 白板」做完后停下、等主人批准,才继续音频和渲染。音频/渲染慢又费钱,主人要在花钱前先看。
- **风格保真**:成片要像 `visual-style-prompt.md` 描述的那样——单块连续 Excalidraw 画布、手绘感、那套配色(红橙标题 / 橙色虚线分组 / 粉珊瑚中心节点 / 绿色输入输出 / 灰色数据库筒 / 黑箭头)、缩放平移、渐进揭示。别退化成 PPT 或光鲜的企业风。
- **范围**:复现白板 + 旁白 + 字幕。**不做**摄像头人像 / 数字人 talking-head——那是以后另说的决定。
- **仓库规约**:CLAUDE.md 的分层原则(CLAUDE.md 声明 WHAT、skill 定义 HOW)、NEVER 清单;这个 skill 是新工具,按文档分层登记,别把实现细节塞进 CLAUDE.md。
- 主人偏好:最小摩擦、skill-first。

如果某个做法值得做但会碰到上面某条,明说这个张力,别偷偷绕过。

**留给你拍板的决策(先提议,别默默替他定)**
- **落点(最大的一个)**——这是一个 vault skill,还是「blog2video 里的白板模板 + content-ops 里的 WF3 式话题前门」?给方案,别默认在 vault 里从零建。
- **TTS**——blog2video 已接好 TTS(见上面复用块);优先复用,只有理由充分才提替代方案(说明 API key / 成本)。
- **渲染器**——blog2video 已经在 HyperFrames 底下跑 Remotion;复用那套引擎做 Excalidraw 导出的定时 pan/zoom,别在 vault 里重搭一套。确认接缝,别重建。
- **调研怎么跑**——复用 content-ops WF3 的调研 / vault 的 `/research` / skill 内轻调研,三选一并说清是否吃 vault 的 research stash。
- **粒度与模板注册**——一个 skill 还是编排几个脚本;以及白板模板怎么注册进 blog2video 的 `/hyperframes` 路由,让两种入口都能选到它。

**任务**
1. 把参考和两个可复用 skill(excalidraw / remotion)摸透,把上面这条链路在脑子里跑通。
2. **先出一份简短方案**:链路怎么落地、上面四个决策你怎么选(带理由)、skill folder 长什么样、哪里可能卡住。把关键决策摆出来让主人对齐——这一步别跳过,主人想在你动手大建之前拍一次板(和 skill 本身的复审闸门是同一个哲学)。
3. 对齐后,按你方案里定的**落点**把它建出来(vault skill / blog2video 模板 / content-ops WF3 前门,或三者组合;名字你可提更好的):承载工作流的 SKILL.md,`references/` / 脚本 / 模板按需分层。把这个 handoff 里的 `references/sean-whiteboard-explainer/` 作为自带的风格靶子带进去。
4. 端到端自测一遍(哪怕用一个小话题),证明链路到复审闸门为止真能跑通;闸门之后的音频/渲染至少要能在批准后跑起来。

**工作方式(自己拿捏,别按我的步骤走)**
读真实文件、真把 excalidraw/remotion 跑一下,别猜 API。有足够信息就动手,别把已定的事反复重推、别罗列你不打算深入的选项;要在几个方案里选就直接给推荐,别写穷举综述(这条不适用于你的思考过程,只针对给主人看的输出)。你每一个设计决定都要能指向你**真读过 / 真跑过**的某个文件或 skill 作为依据;没核实的标「未核实」,别当事实报。别过度工程——这个任务不需要的功能、抽象、防御性错误处理都别加;一个直白能跑的实现胜过一个华丽的框架。可以放手用 sub-agent 并行摸索(excalidraw 能力 / remotion 能力 / TTS 选型可以并行调研)。

**边界(明确不要做的事)**
- **别跳过复审闸门**——不管是 skill 的设计里,还是你自己动手建之前那次方案对齐。
- 别做 talking-head / 数字人。
- 别把实现细节写进 `CLAUDE.md`;那里只登记「有这么个 skill」,细节进 SKILL.md。
- 别改 `raw/` / `wiki/`,别碰无关的 vault 文件。
- 别为了显得完整而堆功能;先把主线(话题→脚本→白板→闸门→音频→渲染)跑通,花哨的留到主人要。

**交付物 / 形状**
- 一个能用的 skill(`.claude/skills/whiteboard-video/` 或你提议的更好名字):SKILL.md + 需要的脚本/模板 + 自带的风格靶子 references。
- 一份简短的「怎么用」说明:主人给一个话题,命令怎么敲,闸门在哪、他要在闸门看什么、批准后会得到什么文件。
- 按仓库规约在该登记的地方登记这个 skill(CLAUDE.md 的命令/技能表 + README hub,如适用)。

**沟通风格(你最终给主人的东西怎么写)**
结论先行:第一句说清「skill 建好了 / 我建议的方案是什么 / 现在卡在哪」——就是主人如果说「给我个 TLDR」他想听的那句。之后才是支撑细节。要好读,不要为了短压成箭头链、缩写、生造标签——主人没看过你中间的推理,每个文件名 / 术语 / 决策都用一句人话说清是什么。宁可清楚,不要简短。
