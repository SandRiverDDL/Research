# Model TR Stage Notes Guide

本 guide 只适用于 `foundation-model-systems`。它是项目内约束，不是全局 Codex skill；不要把这些规则写回 `research-codex-workflow`。

## Why This Exists

普通 paper card 适合高吞吐抽卡；model technical report / open recipe 更像 system dossier。Stage note 的目标是复原一个模型系统在某个阶段“具体怎么做、为什么这么做、哪里没披露、哪些 insight 可迁移”，不是把 claim 按事实/解释/猜测分桶。

## Default Note Shape

Source dossier 的完成标准保持简单：

- `README.md` 能给 source-level verdict。
- `section-index.md` 能回原文定位。
- `notes/` 能压缩核心机制。
- `claims-and-gaps.md` 能审计可信度。

不要把完成标准扩展成复杂 checklist；下面的 stage checklist 只服务写 note。

Stage notes 可以忠实记录旧版本和历史设计，但 lens / comparison / 总结必须额外判断 recency。一个完整旧 TR 的细节多，不代表它仍是当前先进实践；如果后续版本披露了新的 RL 流程、OPD/consolidation、eval target、architecture 或 serving 约束，应在总结中标为 current-practice，并把旧 TR 标为 lineage-reference。

Stage note 默认使用 human-first 轻模板，先帮人抓住核心设计，再保留足够证据给 Codex 后续做 comparison：

- `Core Design / Innovation`: 3-6 条最高价值结论，优先写这个 source 的核心设计、创新点、关键取舍和训练系统思想；每条要能回到 source anchor。
- `Why It Matters`: 说明这部分为什么值得学，区分哪些能培养 intuition / taste，哪些只是随查随用。
- `Mechanism Sketch`: 用短流程复原“具体怎么做”，例如 data mix search、SFT/RL flow、context extension、infra control loop。
- `Details / Evidence`: 只展开方法必要细节、关键 ablation、具体控制项和证据；不要把表格数字、benchmark entries 或实现枚举全文搬进来。
- `Gaps / Open Questions`: 只放未披露项、需回读页段、比较时必须补证据的问题。
- `Lookup-only`: 把精确比例、超参、benchmark 数字、cluster/kernels 名称等放这里，避免污染主线。
- `Evidence Anchors`: 页码或非 TR source label 的简短说明。

`Scope / Coverage` 可以放在 YAML 或正文开头一句里；不要为了模板加空标题。`Transfer Hooks` 只有在有具体可迁移机制时才写，且应落到 mechanism、failure mode、eval gate 或 data decision。

Eval stage note 的主线不是分数汇总，而是评估方法、设计思路和可信度：它如何定义能力、如何控制 scaffold / tools / context / sampling / judge 等变量、如何支撑训练或 release claim。具体 benchmark 数字默认放 `Lookup-only`；只有 headline positioning、claim-critical ablation、异常结果或直接影响比较判断的数字才进入主线。

`事实 / 解释 / 猜测 / 开放问题` 是 claim 的认知状态标签，可以放在 bullet 前缀或局部 caveat 里；不要把它们机械地当成一级标题。

## Checklist Rules

下面的 checklist 是阅读提醒，不是硬模板。写 note 时只保留该 source 真的有信息量的部分；不要为了填满 checklist 加空标题。

如果一个 stage note 低于约 180 行，通常不拆。超过约 220 行、或包含 3 个以上独立训练流程时，优先按子阶段拆，而不是按每个 trick 拆。

## Progressive Splitting Rules

Stage note 采用 progressive splitting：先粗后细，先按阶段/机制承载信息，再在信息量、重要性和复用价值足够时拆成更细 note。

默认路径：

```text
pretraining.md / posttraining.md / eval.md / architecture.md
-> pretraining-data-mixture.md / rl-training.md / sft-distillation.md / opd.md
-> critic-based-ppo.md / anti-hacking.md / scale-ladder.md / indexshare.md
```

不要只因为一个术语出现就拆文件。拆分单位不是名词，而是值得后续复用和比较的机制。

拆成独立 method note 前，优先在父 stage note 里写 `Method Blocks`：

```text
## Method Blocks

### <method name>

- 官方披露：
- 合理解释：
- 未披露 / 不能下结论：
```

只有满足以下条件时，才把 method block 拆成独立 note：

- 独立机制：它有自己的 problem、mechanism、tradeoff、evidence 和 gaps，不只是父阶段的一个小实现细节。
- 信息量足够：source 披露了流程、设计理由、ablation、公式或系统细节；否则独立文件会变成猜测壳。
- 复用价值高：后续会和其他 source 反复比较，或会进入 lens / comparison。
- 父文件膨胀：父 stage note 超过约 220 行，或包含 3 个以上独立训练/系统流程。
- 查询频率高：用户或后续任务经常单独查询这个机制。

如果披露不足但概念重要，保留在父 note 的 method block 中，并明确区分 `官方披露`、`合理解释`、`未披露 / 不能下结论`。

## File Naming Rules

文件名的目标是让人一眼知道“阶段 + 机制”，但不要机械加前缀。

- 当方法名本身已经说明阶段时，不加多余前缀：`rl-training.md`、`sft-distillation.md`、`consolidation.md`。
- 当方法名容易跨阶段歧义时，加阶段前缀：`pretraining-data-mixture.md`、`pretraining-engineering.md`、`infra-cluster-goodput.md`。
- 不给 `rl-training.md` 这类已清楚的机制名再加阶段前缀；post-training 子阶段直接放在 `notes/` 根下，例如 `rl-training.md`、`sft-distillation.md`、`consolidation.md`。
- 单个 source note 数量不多时优先保持浅层目录；只有一个 note 超过约 220 行或包含 3 个以上独立流程时才考虑拆文件，不靠目录分层解决。
- `data-pretraining.md` 太宽，容易把 data mixture、continued pretraining、long-context extension 和 infra 混在一起；新 note 优先拆成 `pretraining-data-mixture.md` 和 `pretraining-engineering.md` 这样的机制文件。

## RL Checklist

适用于 reasoning RL、agentic RL、preference/safety RL、specialist climb。

- 起点 policy: 从 base、mid-trained、SFT checkpoint 还是 specialist checkpoint 开始。
- Objective: PPO / GRPO / DPO-like / custom objective，以及 token-level or response-level 更新。
- Reward: task reward、verifier、process reward、language/style reward、length penalty、safety reward。
- Sampling: rollout group size、temperature/top-p、pass-rate filtering、rejection sampling、environment interaction。
- Stability controls: entropy control、ratio clipping、KL、gradient / loss spike 处理、collapse recovery。
- Curriculum: length、difficulty、domain、tool-use 或 environment curriculum。
- Specialists: 不同 domain climb 如何分工，是否共享数据、reward、eval gate。
- Reset / transfer: self-distillation、checkpoint migration、rollback、warm start。
- Gaps: prompt distribution、reward implementation、environment mix、gating criteria 是否公开。

## SFT / Distillation Checklist

适用于 instruction tuning、trace distillation、self-distillation、teacher-student packing。

- 起点 checkpoint 和目标行为。
- Teacher / trace 来源：human、model-generated、specialist、multi-checkpoint、third-party or self-generated。
- Filtering: correctness、style、safety、degenerate CoT、reward hacking、length。
- Mixture: sample weight vs token weight、domain balance、public/internal data。
- Training schedule: epochs、sequence length、batch、LR、dropout、MoE balance；只记录对结论有用的数字。
- Role: final alignment、capability packing、policy initialization、collapse recovery、format conversion。
- Failure modes: over-constraining policy、forgetting long context、safety/reasoning tradeoff。
- Gaps: exact data composition、teacher selection、filtering thresholds、ablation 是否公开。

## OPD / Policy Distillation Checklist

适用于 online policy distillation、logit distillation、multi-teacher distillation、trajectory-level distillation。

- Teacher / student 关系：同源、跨代、multi-teacher、specialist-to-generalist。
- Student-generated or teacher-generated trajectories。
- Supervision target: full-vocab logits、selected token logits、trace text、rewarded trajectories。
- Online loop: 是否边生成边蒸馏，是否随 student policy 更新。
- Filtering / weighting: trajectory score、teacher confidence、domain balance、difficulty。
- Infra dependency: logit storage、serving throughput、rollout generation、teacher ensemble cost。
- Role vs SFT/RL: 是聚合 teachers、提升 policy smoothness、压缩能力，还是做 final alignment。
- Gaps: teacher routing、logit temperature、loss weights、compute budget 是否披露。

## Data / Pretraining Checklist

适用于 pretraining、mid-training、continued pretraining、data mixture search。

- Source families: web、code、math、books、PDF、synthetic、proprietary、licensed。
- Cleaning: quality filtering、dedup、decontamination、PII/safety filtering、language normalization。
- Mixture search: local/global search、scale ladder、NLL frontier、rank non-invariance、repeat caps。
- Curriculum / stages: pretraining、mid-training、long-context extension、domain continuation。
- Governance: data cutoff、provenance、copyright/license、open-vs-closed disclosure。
- What to internalize: selection philosophy、scaling transfer assumptions、eval-linked data decisions。
- Lookup-only: exact percentages、cutoff tables、benchmark decontam lists，除非影响判断。
- Gaps: private data proportion、filter model、dedup thresholds、contamination audit 是否公开。

## Eval Checklist

适用于 benchmark、human eval、internal eval、safety eval、training gate。

- Eval design philosophy: 这套 eval 想证明什么能力或 failure mode，而不是只看最终分数。
- Eval role: leaderboard reporting、training gate、ablation selector、safety release gate、regression guard。
- Suite composition: public benchmarks、internal eval、human eval、agentic eval、safety eval 如何组合。
- Benchmark scope: reasoning、coding、agentic、tool-use、instruction following、safety。
- Eval setting: sampling、context length、tools、scaffold、judge model、multi-run / pass@k / timeout 处理。
- Public vs internal: 哪些可复现，哪些只能作为 claim。
- Contamination / leakage: 数据 cutoff、decontam、benchmark freshness、judge leakage。
- Human eval: task distribution、rater design、pairwise setup、style bias。
- Comparability: 是否同 prompt、same scaffold、same tool access、same context length。
- Claim support: 哪些核心 claim 被 eval 设计支撑，哪些只是 reporting rhetoric。
- Numbers policy: headline positioning、claim-critical ablation、异常/反直觉结果可以进入主线；普通 leaderboard tables 和 exact benchmark entries 放 `Lookup-only`。
- Gaps: missing baselines、missing variance、unreleased eval sets、unclear judge model。

## Transfer Hooks

Stage note 的迁移线索应该分成三类：

- `worth-internalizing`: 能培养直觉/taste 的机制，例如 pass-rate filtering、mixture search、final RL 防遗忘。
- `try-at-small-scale`: 可以用小模型或小数据做 ablation 的 recipe fragment。
- `lookup-only`: 需要时回查的数字、表格、benchmark entries、具体超参。
- `lineage-reference`: 较早版本披露完整、可解释设计来源，但不应直接代表当前先进实践的内容。
- `current-practice`: 后续版本或最新 release 明确采用、当前总结应优先考虑的设计。

不要把“对实习/未来基模方向的启发”写成空泛反思；必须落到机制、failure mode、eval gate 或数据决策。
