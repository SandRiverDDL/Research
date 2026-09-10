# Agent Post-Training Data L1 Card Template

> L1 是 research index，不是全文总结。每段强结论必须有 source anchor。

## L1 压缩契约

- 目标长度：700-1000 中文字；超过 1200 字通常应拆到 L2 note 或 `comparison/`。
- 每节只写后续检索、comparison、idea 判断会复用的信息。
- 不写收录判定、长背景、完整实验复述、无信息量 evidence 列表。
- `相对方法` 是 method contrast，不是正式 comparison；完整横向判断写到 `comparison/`。

## Citation Anchor Policy

- 每张 L1 通常 3-6 个锚点足够。
- 必须锚定：关键数字、核心机制出处、作者承认的 limitation、关键 ablation。
- 不需要锚定：一句话定位、项目判断、常识性概括。
- 锚点优先放在段末或关键 claim 后，不要每格机械引用。
- PDF/brief 路径只保留 HTML 注释，不写成 `Evidence` 节。

```yaml
---
title: <FULL_TITLE>
year: <YYYY>
venue: <venue | arxiv>
paper_type: <trajectory-curation | synthetic-verifiable-data | real-world-trajectory-mining | search-to-sft-distillation | verifier-filtering | metacognitive-scaffolding | data-centric-posttraining | data-flywheel-method | survey | benchmark-eval | background | rl-overlap>
lifecycle_role: <survey-seed | canonical-anchor | strong-baseline | frontier-candidate | background | low-confidence-novelty-risk>
boundary_risk: <none | rl | eval | recipe | infra | alignment>

failure_modes: [<from doc/taxonomy/failure-modes.md>]
data_knobs: [<from doc/taxonomy/design-knobs.md>]

agent_domain: <code | gui | web | browser | tool | search | game | mixed | general>
data_object: <prompt | task | demo | trajectory | tool-call | observation | benchmark-task | replay-buffer | environment>
data_source: <human | teacher | self-generated | environment-generated | replay | synthetic | web | real-world-log>
selection_signal: <success | verifier | difficulty | novelty | uncertainty | cost | format-validity | coverage | reward>
adaptivity: <static | iterative | curriculum | student-feedback | environment-feedback | online>
failure_use: <discard | mask | repair | contrast | mine | replay | ignore>
training_consumer: <sft | pre-rl | rl | eval-only | background>
---
```

## 一句话

在 Agent Post-Training Data 谱系里的位置，≤30 字中文。

## 难题 / Failure Modes

> 开头 YAML 的 `failure_modes` 必须从 `doc/taxonomy/failure-modes.md` 选择；正文解释本文如何定义和处理这些 failure。
> 2-3 行即可。只写本文真正处理的 failure，不凑表。

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `failure-signal-waste` |  |  |  |

## 核心做法

3-5 句话说明它改变了什么数据对象、数据从哪里来、用什么信号筛选/加权/修复、数据服务哪个训练阶段。证据锚点直接写在句尾，例如 `[PDF §3.1]`、`[Table 2]`、`[Appendix D]`。

## Data Mechanism / Design Knobs

> 开头 YAML 的 `data_knobs` 必须从 `doc/taxonomy/design-knobs.md` 选择；正文解释本文在 agent data pipeline 里改了哪些设计选择。
> 2-4 行即可。这里不是写 paper-specific 风险，而是写方法属于哪些可迁移设计位点。

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `step-level-masking` |  | trajectory-level discard / repair |

## 相对方法

3-4 行即可。只写“这篇论文为什么要和谁比”，不是完整 comparison。

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
|  |  |  |  |

## 谱系位置

- 上游：
- 同期：
- 下游：

## 和 Agentic RL 的关系

- agentic_rl_overlap:
- 如果有 RL 部分：它是 data pipeline 的消费者，还是 RL algorithm 的贡献？
- 需要登记到 `agentic-rl` queue 吗？

## 优缺点

- 优势：1-2 条。
- 不足 / 风险：1-2 条。

Source-only metadata 放在文件尾部，不放开头 YAML：

```markdown
<!-- meta:
authors: [<first author>, et al.]
url: <url>
arxiv_id: <id if any>
pdf: papers/<file>.pdf
brief: _meta/briefs/papers/<file>.md
survey: <seed / forward recall source>
agentic_rl_overlap: <true | false>
agentic_rl_queue: <none | comparison/queue.md row | path>
-->
```
