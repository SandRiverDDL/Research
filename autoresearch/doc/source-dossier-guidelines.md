# Source Dossier 编写指南

> 本文定义 Autoresearch 项目中开源系统 / 复杂研究系统 dossier 的默认研究深度、证据纪律与验收标准。目录契约的决策理由见 `doc/memory/DECISIONS.md`。

## 1. 目标与边界

Source dossier 用于保存一个系统级对象的完整理解，适合同时涉及：

- 论文中的方法设计；
- README 中的安装、调用与作者定位；
- skill / workflow contract；
- 少量关键源码实现；
- evaluation、维护状态与个人采用判断。

Dossier 不是正式 L1 card：

- L1 是 research index，回答“它是什么、为何重要、证据入口在哪里”。
- Dossier 是 source-level understanding，回答“系统实际怎么工作、证据强弱如何、哪些部分值得采用”。
- Nested dossier 不进入正式 card count，不套 L1 frontmatter，也不写入 queue。

## 2. 目录契约

```text
notes/<system-slug>/
  overview.md       # 唯一入口
  <mechanism>.md    # 仅在 overview 无法清楚承载时拆分
  <evaluation>.md
```

硬规则：

- `overview.md` 是唯一入口，不另建同名 root-level L1。
- 不增加 `notes/dossiers/` 中间层。
- 默认保持 2–4 个文件；只有出现可独立维护的问题域时才继续拆分。
- 子文档必须返回 `overview.md`，overview 必须链接全部子文档。

## 3. 语言硬要求

**IMPORTANT — MUST：dossier 的标题、解释、综合判断和主要正文必须以中文为主。**

允许保留英文的内容仅包括：

- 技术术语、模型名、skill 名、字段名和文件名；
- 原始引文；
- code、command、schema；
- 中文翻译会降低准确性的短语。

不得因为主要来源、README 或源码是英文，就把笔记主体写成英文。完成前应快速检查标题、段落与结论是否仍以中文承担叙事。

## 4. 默认阅读深度：逐级升级，不做全仓审计

### Level 1：Paper + README（默认必读）

用于确认：

- 系统定位、研究问题与宣称贡献；
- 作者描述的总体流程；
- 安装、调用、模型/API/GPU 依赖；
- 官方 evaluation、limitations 与维护入口。

如果任务只是项目介绍、使用方式或论文方法概览，读到这里通常足够。

### Level 2：主入口 skill / workflow contract（系统 dossier 默认必读）

只读能够控制主流程的入口，例如：

- `SKILL.md` / workflow definition；
- 主 orchestrator / state machine；
- evaluation protocol。

用于确认 README 所说的阶段是否真的进入运行 contract、哪些步骤是 LLM judgment、哪些是 deterministic gate、哪里会中止或恢复。

### Level 3：Targeted source inspection（按问题触发）

只有出现以下情况才读对应源码：

- 用户明确追问“代码实际执行到哪里”；
- paper、README 与 skill 描述矛盾；
- 某个 hard gate、retry、resume、validator 或安全边界是关键判断；
- 需要区分作者规划、prompt 约定与真实实现；
- 一个结论会直接影响采用、成本或风险判断。

每个问题只检查最小 decisive file / function。不要为了“完整”遍历整个仓库，也不要逐项复述全部 skills。

## 5. 证据层级与标注

正文使用以下标签，避免把不同证据混写：

- **事实**：可追到论文页码、固定 commit 文件或官方运行文档。
- **作者自报**：README、技术报告或项目方展示的 score / run / community outcome。
- **第三方证据**：独立复现、benchmark、audit 或正式 venue outcome。
- **解释**：对事实关系的机制性解读。
- **判断**：本项目的采用、可信度或 SOTA 边界结论。
- **开放问题**：现有材料无法回答的证据缺口。

“Code-confirmed”只表示实现路径存在，不表示科学结论正确。GitHub stars、release 频率和大厂/名实验室归属只属于 operational credibility signal。

## 6. Source anchors：少而关键

每个 dossier 默认保留 **8–15 个独立 source anchors**，而不是逐句堆链接。

优先级：

1. 官方论文 PDF，关键结论带章节或页码；
2. 固定 commit；
3. README / setup；
4. 主 pipeline skill / orchestrator；
5. 2–4 个决定性机制文件；
6. evaluation protocol / limitations；
7. 必要的第三方证据。

同一文件在多个相邻段落支撑同一判断时可复用章节级引用，无需每句话重复链接。固定 commit 用于稳定源码判断；快速变化的 stars/releases 必须标日期。

## 7. 最小首版原则

首版目标是“机制可理解、关键判断可追溯”，不是穷尽仓库：

- overview 先回答定位、边界、使用方式、成本、总体流程与采用结论；
- 子文档只承载 overview 会明显过长的机制或评价问题；
- 不建立无法自动维护的 source map、skill inventory 或 raw search dump；
- 不为未来可能的问题预先拆文件；
- 用户继续追问某个机制时，再增量深化对应文档。

推荐停止条件：已经能够回答系统是什么、实际执行链是什么、证据有什么局限、个人应如何采用；继续阅读只会增加实现细节而不会改变判断。

## 8. Operational snapshot

维护状态只保存最小快照：

- 审计日期；
- 固定 commit；
- stars / release / recent activity 的简短信号；
- 是否有持续维护和社区采用。

不保存大段 commit log，不把 snapshot 写成长期不变事实，也不由此推出 scientific SOTA。

## 9. 验收清单

完成前只做与风险相称的验证：

- [ ] 中文为主体，英文只承担术语、引文、代码与原始名称。
- [ ] `overview.md` 能到达全部子文档，子文档能返回 overview。
- [ ] 本地 PDF 链接可解析，关键论文判断带章节或页码。
- [ ] 关键源码判断固定到 commit；抽查 decisive paths 存在。
- [ ] 作者自报 score 未写成独立评价或正式 SOTA 结论。
- [ ] 事实、解释、判断和开放问题没有混写。
- [ ] 未新增 root-level L1、comparison、queue、taxonomy 或 validator 规则，除非任务明确要求。
- [ ] 运行项目 validator，确认 nested dossier 被忽略、正式 card count 不变。

通常不需要逐个验证几十个重复 GitHub 链接，也不需要渲染整篇 PDF。首页加一个关键证据页、一次链接检查和一次 validator 已足够。

## 10. 常见过度行为

- 为写 dossier 全面审计所有源码与 skills。
- 把 README 每个功能逐项复述成目录。
- 为每个事实重复添加同一源码链接。
- 用 stars、作者 affiliation 或 LLM-judge score 替代科学证据。
- overview 与 evaluation/adoption 重复同一结论。
- 在首版就创建 comparison、模板、source map 或新的必需流程。
- 因来源是英文而把 dossier 主体写成英文。

