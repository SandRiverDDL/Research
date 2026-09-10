# Codex Research Process

## Why Not Copy OPD Directly

OPD 的流程适合高吞吐论文调研：大量 paper、L1 card、target queue、card validator、research map。

本项目的 source 数量少但单个 source 很重。DeepSeek-V4 或 MAI-Thinking-1 这种 source 不是普通 paper，而是 source bundle / system dossier。因此只复用 OPD 的原则：

- durable state in files;
- generated manifest / validation;
- bounded context;
- L1/L2 分层；
- synthesis 和 comparison 才做强判断。

不复用 OPD 的重 L1 card pipeline。这里 L1 只是 manifest index。

## Relation to Autoresearch / Agentic RL

从 `autoresearch` 和 `agentic-rl` 继承的规则：

- queue row / source listing 不是正式笔记；必须有 primary source 或从 primary source 做出的 bounded brief / section note。
- survey、blog、announcement 只能作为 recall / positioning signal，不能替代 TR、paper、repo、model card 或 evaluation source。
- 脚本只做 hygiene：manifest、status、validation、lookup、audit；importance、claim trust、transferability 仍由 Codex 和用户判断。
- 写完一轮 batch 或迁移后必须跑本地 validator，并说明验证结果。
- 旧 notes / legacy generated files 只能当历史材料，不当权威来源。

本项目必须保持独特的地方：

- 不写普通 L1 paper card。TR / open recipe / model release 是 source bundle，一个 source 可能包含 TR、model card、blog、repo、external eval。
- `README.md` 是 source-level verdict；`section-index.md` 是回原文地图；`notes/` 是核心机制压缩；`claims-and-gaps.md` 做可信度审计。
- Stage notes 默认 human-first：先写核心设计和创新点，再写机制流程、证据、缺口和 lookup-only。
- 不维护 heavy queue / target-card list / paper-card validator，除非 source 数量真的增长到需要。
- Source dossier 的目录保持扁平：`sources/<source-id>/notes/*.md`。source type 写在 metadata，不靠目录层级表达。

应该写入 skill 的只有跨项目稳定方法：

- evidence before conclusion；
- project-local rules outrank generic workflow；
- bounded input，不默认塞完整 PDF / survey；
- generated artifacts 不能成为无法维护的必需流程；
- validator 只管机械 hygiene，不承载研究判断。

不应该写入全局 skill 的内容：

- `foundation-model-systems` 的目录结构、note 文件名、lens 名称；
- model TR / recipe 的 stage checklist；
- DeepSeek / MAI / Kimi / GLM 等 source vocab；
- 当前 citation style、page anchor 约定、source dossier done criteria。

如果未来多个独立项目都需要同一套 TR dossier 流程，再考虑做一个本地 skill；当前只写在本项目文档。

## 固定规则 vs 判断规则

固定规则写入 `doc/`、模板和 validator：

- 每个重要 source dossier 至少有 `README.md`、`source-bundle.md`、`section-index.md`。
- `README.md` 是人和 AI 的默认入口，只放短结论、状态和阅读入口。
- `source-bundle.md` 记录 canonical URLs、本地 PDF、页数、freshness。
- `section-index.md` 记录 PDF section/page map、已读/未读状态、应该读哪里。
- 模型后续版本如果只有 blog / model card，不默认建成和主 TR 等价的独立 source；先判断它是 lineage 下的 release delta，还是值得独立精读的 major source。
- 横向总结、lens 和 comparison 必须按时间和设计新旧加权。若后续版本明确改变了训练流程、RL 组织、expert consolidation、eval target 或 serving/agent system，默认以后续版本为 current practice；旧 TR 只作为 lineage-reference / historical rationale，除非后续版本没有相关披露。
- `model-tr-stage-notes.md` 是本项目的 stage note guide；不要把这些 TR / recipe 规则写回全局 `research-codex-workflow` skill。
- Stage notes 的主体按训练流程、机制、ablation、缺口组织；关键 claim 必须能看出认知状态（事实 / 解释 / 猜测 / 开放问题），并保留 source anchors。不要把四种认知状态机械地当成默认一级标题。
- Lens/comparison 做强判断前，必须能回指 source dossier、section note 或 PDF 页码。
- 引用采用最小规则：单个 source dossier 默认引用主 TR PDF，只写句末页码如 `[29-30]`；非主 source 才写语义 label，如 `[model-card:2-4]`、`[announcement-thinking]`、`[blog-build-2026]`。
- 不使用旧式 `TR + p + page range` 前缀，也不把引用放在 bullet 开头。
- 精读 notes 默认放在 `notes/` 下，按训练阶段组织；不要把每个 technique 都拆成独立文件。
- 文件名用“阶段 + 机制”消歧，但不机械加前缀；例如 `pretraining-data-mixture.md`、`pretraining-engineering.md`，而不是宽泛的 `data-pretraining.md`。
- post-training 可以按子阶段拆成 `rl-training.md`、`sft-distillation.md`、`reward-verifier.md`、`tool-agent-training.md`、`consolidation.md`，但这些文件直接放在 `notes/` 根下；不要再建 post-training 子目录。

交给 Codex / skill 判断，不写成硬性必填：

- 是否需要全读某份 TR。
- 哪些 section 需要 deep read，哪些只需要 skim。
- 某个 claim 是否需要回读 appendix/table/figure。
- 某个 source 是否已经够写 lens，还是需要补 section note。
- 新 source 应该先进 source dossier，还是只登记为 comparison candidate。

原则：固定规则保证可追溯；判断规则保留研究弹性。

## Source Dossier Done Criteria

简单标准：看 `README.md` 能知道结论，看 `notes/` 能复原核心机制，看 `section-index.md` 能回原文核查。

一个 source dossier 完成到可读状态只要求四件事：

- `README.md` = source-level verdict：核心 takeaway、最重要的 3-5 个机制、最大证据缺口、推荐阅读顺序。
- `section-index.md` = 回原文地图：architecture / data / post-training / eval / infra 分别该回哪些页。
- `notes/` = 核心机制压缩：只写影响判断和 comparison 的关键 stage，不追求覆盖全文。
- `claims-and-gaps.md` = 可信度审计：哪些可信，哪些 underdisclosed，哪些只是 lookup-only。

不要把完成标准扩展成多层打分体系；复杂 checklist 只作为写 notes 时的提醒。

## Model Lineage and Release Deltas

很多模型后续更新只有 blog、model card 或 repo changelog，没有新的 technical report。此时不要机械地把每个小版本都当作完全独立的 source dossier。

默认区分三层：

```text
model family / lineage
major TR version
blog-only release delta
```

处理规则：

- 有完整 TR 的版本作为 lineage 的主 anchor；`section-index.md` 和大多数 stage notes 以主 TR 为准。
- 后续只有 blog / model card 的小更新，优先作为同一 lineage 下的 release delta 记录，例如 `notes/release-glm-5.2.md`，只写相对主 TR 或上一版本的增量。
- 只有当 blog-only 版本满足以下条件时，才升级成独立 source dossier：architecture / training recipe / eval target 明显变化；公开信息足够写出 2-3 个高价值 stage notes；后续会被单独 comparison；或用户明确要求精读这个版本。
- 独立建 dossier 的 blog-only 版本必须在 metadata 中标明 lineage 关系，例如 `lineage: glm-5`、`role: release-delta`、`base_source: glm-5-tr`；notes 只写增量，不把旧 TR 的内容默认为新版本事实。
- 小 release delta 不需要完整 `section-index.md`；但如果它升级成独立 source dossier，仍需有 `source-bundle.md` 和 `section-index.md`。没有 PDF 页码时，section index 使用语义 source label。

判断口径：小 blog 更新放进 parent source 的 release note；大 blog 更新可以单独建 dossier，但必须保留 lineage/base-source 标记，并明确哪些是新披露、哪些只是继承或推测。

### Synthesis Priority

当一个 lineage 同时有旧 full TR 和新 release delta 时，写总结时不要机械平均：

- `current-practice` 优先：当前最新 release 或明确后续改动优先代表“现在先进模型怎么做”。
- `lineage-reference` 保留：旧 full TR 可用于解释设计来源、术语、infra 约束和历史 baseline。
- `disclosure-weight` 辅助：如果新 release 只给 blog/model card，必须标注证据较弱；但证据较弱不等于可以用旧 TR 覆盖它的明确改动。
- `anchor-vs-latest` 分离：anchor 是最完整可读的资料，不一定是最新实践；latest 是当前模型行为/设计的优先候选，不一定披露完整。

例：如果 GLM-5 披露多阶段 RL，而 GLM-5.2 明确披露“分别训练 experts 后通过 OPD / parallel OPD 合并”，总结 GLM 当前后训练时以后者为 current practice，GLM-5 多阶段 RL 作为 lineage-reference。MiniMax-M2 series 可保留为 agentic data / Forge / self-evolution 的完整训练系统资料，但 MiniMax 当前模型总结应优先检查 M3 / MSA / M3 model card 是否改变 architecture、context、multimodal 或 serving 设计。

## Citation Style

本项目不维护全局 source 编号系统。默认 source 是当前 dossier 的主 technical report PDF，因此 stage notes 里的大多数事实只需要句末页码：

```markdown
- V4 支持三种 reasoning modes：Non-think、Think High、Think Max。[29]
```

只有引用非主 TR source 时才写来源 label。Label 用可读语义名，不用 `BLOG1` / `BLOG2`：

```markdown
- Model card 披露了 license、weights distribution 和 intended use。[model-card:2-4]
- 发布说明强调 model positioning，但没有补充训练细节。[announcement-thinking]
- Build 2026 blog 只作为产品背景，不作为训练事实来源。[blog-build-2026]
```

Lens / comparison 如果一个段落只讨论一个模型，继续用页码；同一段同时比较多个模型时才加模型前缀，例如 `[DS:29-30]`、`[MAI:31-33]`。

## Workflow

### 1. Source Intake

For each source dossier:

- fill `README.md` status;
- fill `source-bundle.md` with canonical URLs and local PDF paths when available;
- fill `section-index.md` with TOC/page ranges, reading map, and if-you-need routing;
- identify which stage notes are needed;
- record source freshness and confidence.
- for blog-only updates, decide whether they are release deltas under an existing lineage or independent source dossiers; record `lineage`, `role`, and `base_source` when independent.

### 1.5. Section Index

For TR-like sources, always create `section-index.md` before deep notes. It is not a summary; it is an AI-readable navigation layer.

Use it to answer:

- Which PDF pages contain architecture / data / post-training / eval / infra?
- Which pages have already been read into notes?
- Which pages should be read before lens/comparison?
- Which appendix/table/figure contains lookup-only details?

Do not treat first-pass notes as the complete fact set. When a lens or comparison needs a strong claim, return to the indexed PDF pages.

### 2. Stage Notes

TR 精读默认按 stage note 写，不按单个 trick 过度拆分：

```text
sources/<source-id>/
  notes/
    architecture.md
    pretraining-data-mixture.md
    pretraining-engineering.md
    rl-training.md
    sft-distillation.md
    reward-verifier.md
    tool-agent-training.md
    consolidation.md
    eval.md
    infra.md
    safety.md
    claims-and-gaps.md
```

Only create files that are actually needed. A technique stays inside its parent stage note unless it is a core contribution, has enough algorithm/formula/system detail to stand alone, or will be repeatedly compared across sources.

Use the following rough split rule:

- under 180 lines: usually keep in one stage note;
- over 220 lines: consider splitting, but this is a warning, not a hard failure;
- 3+ independent sub-flows in one file: split by substage, not by every trick;
- lookup-only facts and table numbers stay in stage notes or evidence anchors.

Stage note 推荐结构：

- `Core Design / Innovation`：先写 3-6 条最高价值结论，聚焦核心设计、创新点、关键取舍和训练系统思想；每条需要能追到 anchor。
- `Why It Matters`：说明为什么值得学，区分能培养 intuition / taste 的内容和随查随用内容。
- `Mechanism Sketch`：用短流程复原“具体怎么做”，例如 data mix search、SFT/RL flow、context extension、infra control loop。
- `Details / Evidence`：只展开方法必要细节、关键 ablation、具体控制项和证据；不要把表格数字、benchmark entries 或实现枚举全文搬进来。
- `Gaps / Open Questions`：只放未披露项、需要回读页段、或比较时必须补证据的问题。
- `Lookup-only`：放精确比例、超参、benchmark 数字、cluster/kernels 名称等随查随用信息。
- `Evidence Anchors`：页码或非 TR source label 的简短说明。

`Scope / Coverage` 可以放在 YAML 或正文开头一句里，不强制作为一级标题。`Transfer Hooks` 只有在有具体可迁移机制时才写，不写空泛启发。

Eval note 例外强调：`eval.md` 的主线应分析评估方法、suite 设计、setting、可比性和 claim support，不做分数表转写。具体数值默认 `Lookup-only`；只有 headline positioning、claim-critical ablation、异常结果或直接影响 comparison 的数字进入主线。

SFT / RL / OPD / data / eval 的阶段 checklist 维护在 `doc/model-tr-stage-notes.md`。它们是阅读提醒，不是必填标题；如果某个 source 没有公开相关信息，不要为了 checklist 填空。

### 3. Lens Synthesis

Lens generation is deferred until there are at least 3 sources or a concrete comparison question. Use lenses for cross-source technical structure, not for source-level extraction:

- `lenses/pretraining/data-mixture/`
- `lenses/pretraining/engineering/`
- `lenses/rl-training/`
- `lenses/sft-distillation/`
- `lenses/reward-verifier/`
- `lenses/tool-agent-training/`
- `lenses/consolidation/`
- `lenses/eval/`
- `lenses/infra/`

Lens notes should link back to source stage notes and anchors. They should answer cross-source mechanism/taxonomy/evidence-strength questions, not repeat full source summaries.

### 4. Comparison

Comparison files are final research artifacts. They should answer:

- what differs across sources;
- which claim is reliable vs speculative;
- what transfers to small/mid-scale post-training;
- what matters for future base-model work;
- which source to read next.

## Pilot Plan

First pilot:

1. Build source dossiers for DeepSeek-V4 and MAI-Thinking-1.
2. Write only high-value stage notes:
   - DeepSeek-V4: architecture, post-training consolidation/reward/tool-agent, eval, claims-and-gaps.
   - MAI-Thinking-1: pretraining-data-mixture, pretraining-engineering, RL training, SFT distillation, consolidation, eval, claims-and-gaps.
3. Keep notes in stage-note layout under `notes/`.
4. Write one comparison:
   - `comparison/deepseek-v4-vs-mai-thinking-1-pilot.md`

Only after the pilot should the project add Kimi, GLM, Qwen, OLMo, or MiniMax.
