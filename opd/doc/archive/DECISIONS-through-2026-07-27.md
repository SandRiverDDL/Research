# OPD 决策记录（历史快照）

> 归档于 2026-07-27。仅供历史审计，不是现行规则源。

## 2026-07-27 — L1 schema 与脚本解耦

决策：新 L1 只保留 `title`、`authors`、`year`、`venue`、`paper_id`、`source`；正文不使用 Markdown 标题，研究内容以可选软标签表达。Registry 直接扫描 cards，只保留 `lookup/status/validate`，不解析正文或 taxonomy。

原因：旧流程把 YAML taxonomy、正文标题、自动 maps 和队列状态耦合在一起，修改卡片结构会触发脚本、validator 和生成物连锁变化。

影响：71 张旧卡不迁移，通过 `arxiv_id` / `url` adapter 永久兼容。Manifest、target queue、triage、pack、audit、sync、自动 research-map / idea-context 和 brief builders 退出核心流程；历史产物保留。此决策覆盖下文关于强制 `addresses`、自动 generated files 和 brief-builder 主流程的旧决策。

## 2026-07-27 — 顶会 landscape 与经典谱系并行

决策：OPD 文献库不再只以“是否足够经典”决定是否值得抽卡。近期顶会录用的 in-scope OPD 论文应作为独立 landscape 覆盖，用于学习可发表的问题选择、贡献粒度、实验包装和 idea pattern。

原因：用户当前目标是形成可投顶会的 OPD 工作，而不是只复现经典级贡献。顶会录用本身不是科学可信度证明，但它对 publication taste 有观察价值。

影响：核心谱系卡仍保持高证据门槛；venue landscape 卡可以降低“经典 anchor”门槛，但必须保留原论文证据，并将科学可信度与录用观察价值分开标注。本决策覆盖 2026-06-15 trust-gated triage 中“普通录用论文默认不写卡”的过强口径。

## 2026-07-27 — Cards 是 ideation 上游索引，不替代原文证据

决策：大范围 cards 作为 ResearchStudio-Idea 的长期 recall / routing memory；针对具体方向仍做 freshness retrieval。Failure mode 可来自单篇证据，bottleneck 必须由多篇近邻工作的残余限制重建；关键 bottleneck、novelty 和 idea claim 必须回到原文 source anchors。

原因：固定 40–45 篇临时检索可能漏掉经典祖先、较早分支和已积累的领域证据；但只读卡片又会继承摘要压缩和判断偏差。

影响：采用 `broad cards → shortlist → original-source evidence upgrade → bottleneck → pattern → collision/audit` 的证据流。召回数量不固定，以 coverage 和 saturation 为停止条件。

## 2026-06-12 — L1 卡是研究索引

决策：L1 card 只保留核心方法、原理、创新点、决策点、解决的 failure mode、谱系位置和 source anchors，不写成完整论文总结。

原因：当前目标是降低人阅读和比较负担，而不是为每篇论文生成长篇读后感。

影响：实验细节、复现信息、主观 verdict、idea 判断进入 L2 note、comparison 或 synthesis 文档。

## 2026-06-12 — L1 使用 bounded briefs（已被 2026-07-27 流程简化覆盖）

历史决策：L1 写卡使用脚本生成的 paper/survey brief，不默认读取完整 PDF 或完整 survey。

原因：完整来源直接进上下文会导致 token 成本高、运行慢、重复 prefill，并且更难控制 source anchor。

当前影响：bounded reading 原则仍保留，但项目不再维护强制 brief-builder；既有 `_meta/briefs/` 仅作历史证据缓存。

## 2026-06-12 — 普通写卡不默认使用 subagent

决策：普通 paper card 写作留在主会话完成。

原因：subagent 会重复加载项目规则、模板、brief 和上下文，通常增加 token 和 wall time。

影响：subagent 只用于小型、独立、可丢弃的任务，例如固定词表分类、字段检查、短 synthesis 独立批评。

## 2026-06-12 — failure-mode taxonomy 只维护一份（机器校验部分已覆盖）

历史决策：`doc/taxonomy/failure-modes.md` 是 `addresses` tag 的唯一来源。

原因：人读列表和 validator 列表分开维护会很快漂移。

当前影响：该文件只供人和 synthesis 参考；新卡不要求 `addresses`，validator 不读取 taxonomy。

## 2026-06-12 — generated files 不手动维护（已被 2026-07-27 流程简化覆盖）

历史决策：manifest、target queue、validation report 和 briefs 都是脚本生成物。

原因：手工 checklist 容易忘、容易过期。

当前影响：这些文件作为历史快照保留，不再自动维护，也不作为当前状态源。

## 2026-06-12 — dogfood workflow 文档归档

决策：`doc/codex-autoresearch-workflow.md` 不再作为当前入口，已归档到 `doc/archive/codex-dogfood-2026-06-12/`。

原因：其中混合了 schema 设计、dogfood finding、open questions 和 handoff，和 `STATE.md` / `DECISIONS.md` / `OPEN-QUESTIONS.md` 职责重叠。

影响：当前入口只保留 `doc/codex-research-process.md`；长期决策沉淀到本文件，未决问题放 `OPEN-QUESTIONS.md`。

## 2026-06-15 — 检索轮采用 fast recall audit

决策：OPD 不做 60-90 分钟的系统综述式检索轮。默认只做 10-15 分钟 fast recall audit，除非用户明确要写 related work 定稿或做系统综述。

原因：当前已有 60+ candidate 和 10+ rewrite/rerun 队列，瓶颈是 card rewrite 与 comparison，不是继续扩大候选池。长检索轮会显著拖慢研究节奏，并把大量低价值顶会/预印本带进队列。

影响：综述 cutoff 前默认相信 song-2026 已覆盖大部分重要 OPD 方法，只做 known-item recovery、S/A anchor 的轻量 citation/cross-ref 检查；cutoff 后只做 arXiv/OpenReview/官方 accepted list 的精确增量检索。连续一轮没有新增 S/A 或 direct novelty-risk，就停止检索，回到写卡和 comparison。

## 2026-06-15 — method paper 采用 trust-gated triage

决策：顶会接收不自动等于可信或值得写卡。方法类论文若没有开源代码、没有社区影响力、也不直接威胁 novelty，默认降为 C 或最多 B，不写 L1 card。

原因：当前顶会质量良莠不齐，低引用、不开源、无复现的 method paper 对研究判断的可信度很低；把这类论文纳入深读会浪费时间，并污染方法谱系。

影响：

- direct competitor / 同问题同机制同 evaluation setup：即使不开源也要进 novelty-risk 候选，必要时写 L1，但在结论中标低可信。
- method paper：不开源且无影响力信号时，不作为可靠方法证据；只在 manifest/off-scope 中留审计痕迹。
- benchmark / eval paper：不要求 method code，但必须有数据、protocol、eval script、leaderboard 或足够清晰的可复现定义。
- theory / taxonomy / position paper：不要求代码，但只有在改变 failure-mode taxonomy、evaluation definition 或核心机制解释时才升为 A。

## 2026-06-15 — 总结报告不是 L1 card 拼接

决策：comparison / synthesis report 负责跨论文结构、证据可信度、矛盾和研究机会，不重复每张 L1 card 的单篇摘要。

原因：L1 card 已经覆盖单篇的核心方法、原理、创新点、决策点、解决的问题和谱系位置；报告如果只重排这些字段，无法降低认知负担，也无法服务 idea 生成。

影响：报告默认包含总论、方法谱系、决策轴对照、failure-mode 到方法族映射、证据可信度、关键 tension、开放问题 / idea hooks 和 `Evidence used`。强结论必须能回到 card、brief、report appendix、L2 note 或原文 source anchor。

## 2026-06-15 — survey reference audit 必须透明暴露全集

决策：survey coverage audit 不能只输出正则命中的 OPD-ish 标题，也不能把“进了队列但未写卡”算成完全覆盖。脚本必须同时输出全量 arXiv references、标题 OPD-ish subset、已写卡/已排除、已进队列未写卡、完全漏进 pipeline 这几类。

原因：综述 references 总 token 很小，模型直接扫标题列表的成本低；如果把语义判断藏在正则里，会漏掉不含 OPD 字样但实际相关的 self-distillation / on-policy learning / DAgger / privileged distillation 工作。

影响：`survey-audit` 的正则只承担结构化抽取和高精度标记，不承担最终相关性判断；每轮覆盖检查后都应看 `_meta/generated/survey-reference-audit.md` 和 `_meta/generated/survey-reference-semantic-skim.md`。

## 2026-06-15 — maybe 队列必须分用途

决策：`maybe` 不再只是“暂缓”池，至少要区分 `novelty-risk`、`report-background`、`application-branch`、`low-evidence-direct`、`ignore-unless-needed`。

原因：一个 40+ 篇的暂缓池会把复杂度转嫁给人。用户真正需要知道的是：哪些可能威胁 idea novelty，哪些只是报告背景，哪些只有做特定应用分支时才需要读。

影响：`candidate-triage.md` 需要给 maybe 论文写用途桶和升级条件；后续自然语言 `找新的论文抽卡` 只默认抽 `select` 或被用户/报告需求触发升级的 `novelty-risk`。
