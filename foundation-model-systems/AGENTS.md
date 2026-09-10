# Foundation Model Systems Research Workspace

> 本文件收窄 `~/Research/AGENTS.md`。当前目录用于研究 foundation model system：模型发布报告、开源模型项目、训练 recipe、architecture、data pipeline、post-training / RL、eval、safety 和 infra。

## 角色

你是研究协作者。目标不是堆模型报告摘要，而是帮助用户形成判断：

- frontier / industrial model system 的思想和方法是什么；
- 哪些公开 claim 可信，哪些只是 reporting rhetoric；
- 哪些训练、数据、eval、infra insight 能迁移到用户可操作的后训练和未来基模工作；
- 哪些知识值得内化成 intuition / taste，哪些只需要随查随用。

## 当前入口

进入项目时先读：

1. `doc/memory/STATE.md` — 当前状态和下一步。
2. `doc/codex-research-process.md` — 本项目流程。
3. `doc/model-tr-stage-notes.md` — model TR / open recipe 的 stage note guide。
4. `_meta/generated/status.md` — 如果存在，优先读脚本生成状态。

只有在新建或重写对应 artifact 时才读：

- `doc/templates/source-dossier.md`
- `doc/templates/section-index.md`
- `doc/templates/section-note.md`
- `doc/templates/lens-note.md`
- `doc/templates/comparison.md`

需要解释根规则时再读：

- `/Users/chy/Research/doc/model-systems-research.md`
- `/Users/chy/Research/doc/autoresearch-common.md`

## 目录约定

- `sources/<source-id>/`: 按单个模型、TR bundle 或开源项目组织的 source dossier；不要再按 `model-tr` / `recipe` / `open-projects` 加一层目录。
- `lenses/`: 按研究问题抽取横向 insight；不重复 source dossier。
- `comparison/`: 跨模型判断、transferability、claim audit、下一步阅读决策。
- `papers/`: PDF 镜像或临时下载。
- `_meta/generated/`: 脚本生成 manifest / validation / status；不要手改。

## Source Dossier 优先

本项目不以 L1 paper card 为核心。原因：

- 候选 source 数量少、辨识度高；
- 重要 source 往往是 TR + model card + blog + repo + external eval 的 bundle；
- 研究价值在 source dossier、lens 和 comparison，而不是单篇卡片。

L1 只保留为 manifest/index 级信息：source 名、类型、日期、URL、coverage、priority、dossier 状态。

模型后续版本如果只有 blog / model card，不默认当作和主 TR 等价的独立 source。优先作为同一 model lineage 下的 release delta；只有当 architecture、training recipe、eval target 明显变化、信息量足够写高价值 notes、或后续会单独 comparison 时，才升级成独立 dossier，并在 metadata 标明 `lineage`、`role: release-delta`、`base_source`。

横向总结和“当前先进实践”判断必须按时间和信息设计加权：后续版本如果明确改变了训练流程、RL 组织、expert consolidation、eval target 或 serving/agent system，以后续版本的设计为准；旧 TR 只能作为 lineage / rationale / historical baseline。不要因为旧版本有完整 TR 就把它误当成当前 SOTA 做法。

## Family Bundle（针对 closed-weights / 多 release blog-only 家族）

默认每个模型 / TR bundle 一个 dossier（如 `sources/deepseek-v4/`、`sources/qwen3/`）。但当一个家族满足以下条件时，合一个 family 目录、用 `release-deltas/<id>.md` 单文件跟踪 release：

- 该家族**没有 TR**，主要公开材料是 blog + system card + product 文档；
- 同一 lineage 下有多个 release，但每个 release 单独信息量不足以撑 ≥2 个 stage notes；
- release 之间共享一套 disclosure 风格和材料源（统一在 `source-bundle.md` 的 citation labels 里管理）。

例：`sources/anthropic-claude/`、`sources/openai-frontier/`、`sources/google-gemini/`、`sources/meta-frontier/`。每个 release-delta 必须写 `定位 / 公开材料范围 / Agent data（或对应 lens）视角信号 / 不能推出的事 / 升级 trigger / Caveats`。升级独立 dossier 的条件由 release-delta 自己写，AGENTS.md 不重复。

开源 / 单 release 的 architecture-level 换代（例：Qwen3.5）即使没 TR 也可以独立 dossier；family bundle 只针对 closed-weights 多 release 的样本。不要把 family bundle 当成偷懒模式，写第一档（TR-anchored）source 时仍然每模型一目录。

## Closed-weights 三类证据纪律

closed-weights source 引用必须明确区分三类证据，不要混用：

- **evaluation 证据**：system card / safety report / 第三方 eval。说明 capability 与 risk，不能反推 training data 规模、mixture、合成 pipeline。
- **product framing 证据**：engineering / product blog、API docs、产品演示。说明产品形态与 inference-time scaffolding，不能反推训练 trajectory 或 data 来源。
- **training recipe 证据**：paper / TR / 训练 post-mortem。frontier closed 阵营通常**没有**这一档；缺位时如实写"未公开"，不要从前两类推断。

任何一条 closed-weights claim 引用时必须能追到上述三类之一的具体 anchor。

## Section Index 优先

TR-like source 必须有 `section-index.md`。它是后续回读 PDF 的导航层，不是 summary。

- 做 stage notes 前先建 index。
- 写 lens/comparison 前先读 index，判断是否需要回读 PDF 页段。
- 第一版 notes 只能代表已读 section，不代表全文事实全集。
- 需要强结论时，回到 index 指向的 PDF 页码、table、figure 或 appendix。

## Stage Notes 优先

大厂 TR 默认值得精读，但不要把每个 technique 都拆成独立文件。先按 stage 写到 `notes/`：

- `notes/architecture.md`
- `notes/pretraining-data-mixture.md`
- `notes/pretraining-engineering.md`
- `notes/rl-training.md`
- `notes/sft-distillation.md`
- `notes/reward-verifier.md`
- `notes/tool-agent-training.md`
- `notes/consolidation.md`
- `notes/eval.md`
- `notes/infra.md` / `notes/safety.md` only when needed
- `notes/claims-and-gaps.md`

拆分原则：

- 文件名要能提示阶段和机制；必要时用 `pretraining-`、`infra-` 等前缀消歧，但不要给 `rl-training.md` 这类已清楚的机制名再加阶段前缀。
- 低于约 180 行的 stage note 通常不拆。
- 超过约 220 行、或包含 3 个以上独立训练流程时，按子阶段拆。
- 单个 technique 只有在它是核心贡献、公式/系统细节足够多、或会跨多个 TR 反复比较时才独立成文件。
- 采用 progressive splitting：先 stage note，再在父 note 内写 method blocks；只有机制独立、信息量足够、复用/比较价值高或父 note 膨胀时，才拆成独立 method note。
- Lookup facts、表格数字、具体 benchmark entries 不单独建文件。

## 研究层级

```text
source intake       整理 source bundle / 目录 / coverage
stage notes         按训练阶段忠实抽取事实、anchor、未披露项
lens synthesis      抽象可复用 insight 和 transferability
comparison judgment 跨模型判断和下一步阅读决策
```

Extra high 模型优先用于 `lenses/` 和 `comparison/`，不要浪费在机械 extraction 上。

写 lens / comparison / 总结时区分两种价值：

- `current-practice`: 当前最新 release / 后续版本采用的设计，优先进入“现在先进模型怎么做”的总结。
- `lineage-reference`: 旧 TR 或较早 release 中披露更完整、可解释后续设计来源的材料；可以写 notes 和追溯，但不能覆盖后续版本的明确改动。

## Pilot Sources

第一轮只做两个 pilot，测试流程是否真的有用：

- `sources/deepseek-v4/`
- `sources/mai-thinking-1/`

不要一开始扩到 Kimi / GLM / Qwen / OLMo / MiniMax。等 pilot comparison 证明结构有效后再加。

## 写作规则

- 笔记中文为主，术语保留英文。
- 每条强结论标注：事实 / 解释 / 猜测 / 开放问题。
- 但不要把 `事实 / 解释 / 猜测 / 开放问题` 机械地当成 stage note 的默认一级结构；stage note 主体按训练流程、机制、实验/ablation、缺口来组织，认知状态只在 bullet 前缀或局部小节里标注。
- Stage note 默认用 human-first 结构：`Core Design / Innovation`、`Why It Matters`、`Mechanism Sketch`、`Details / Evidence`、`Gaps / Open Questions`、`Lookup-only`、`Evidence Anchors`。
- 主线优先记录核心设计、创新点、关键取舍、训练流程、证据和未披露项；精确比例、超参、benchmark entries、cluster/kernels 名称等放 `Lookup-only`，不要污染主线。
- `eval.md` 重点写 eval 方法、设计思路、setting、可比性和 claim support；不要转写 leaderboard 表。数值只在 headline positioning、claim-critical ablation、异常结果或影响 comparison 时进入主线，否则放 `Lookup-only`。
- `## 问题` 不能只写一个大问题；stage note 至少写 scope 和它覆盖的 2-5 个子问题，避免一个文件只能服务一种查询。
- 写 model TR / open recipe 的 stage note 时，使用 `doc/model-tr-stage-notes.md` 的 checklist 作为阅读提醒；checklist 不是硬模板，不要为无信息量项目加空标题。
- 每个可复用 insight 必须有 source anchor。
- 不懂的 infra 不硬解释，标 `depth: surface` / `need_expert_review: true`。
- Lens note 只 cross-link，不重写 source dossier。没有至少 3 个 source 或明确横向问题时，不急着生成 lens。
- Lens、comparison 和跨模型 summary 都是独立交付物；只有用户明确要求时才生成。补 source dossier、stage notes 或 release delta 不自动授权这些综合产物。
- 用户确认的优先级和模型清单必须按原话记录；assistant 提议、旧候选列表和 workflow 中的可选步骤不得自动并入已确认 scope。

## State Sync

- `doc/memory/STATE.md` 是 compact / 新 task 后的 hot memory，目标控制在约 4 KB；只保留 current goal、confirmed contract、当前进度、next action、blocker、必要路径和 decision 引用。
- 用户确认或纠正 scope、优先级、对象清单、交付物、排除项或授权边界后，必须立即增量更新 `STATE.md`，再继续执行。
- 批量搜索、连续读 PDF 等高 context 操作之前，以及每个实质里程碑完成后，检查并替换 `STATE.md` 中的旧进度；长任务最终回复前完成最后一次同步。
- 无实质变化的普通问答不更新。不要把聊天原文、完整 source catalog、搜索日志或 tool output 写入 `STATE.md`。
- compact 后先读本文件和 `STATE.md`；仅当 `STATE.md` 引用相关历史理由时再读 `DECISIONS.md`。

## 长任务通知

当本项目里的长时间任务结束时，用系统语音通知用户。优先用 macOS `say` 命令做简短中文通知，例如：

```bash
say "Foundation model systems 任务完成"
```

如果当前环境没有可用语音命令，在最终回复里明确说明未能语音通知。

## 本地命令

用户不需要记命令；Codex 内部维护时使用：

```bash
scripts/model_systems.py status
scripts/model_systems.py sync
scripts/model_systems.py validate
```
