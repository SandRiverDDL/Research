# Agentic RL L1 Card Template

> L1 是 research index，不是全文总结。每段强结论必须有 source anchor。

## L1 压缩契约

- 目标长度：700-1000 中文字；超过 1200 字通常应拆到 L2 note 或 `comparison/`。
- 每节只写后续检索、comparison、idea 判断会复用的信息。
- 不写收录判定、长背景、完整实验复述、无信息量 evidence 列表。
- `相对方法` 是 method contrast，不是正式 comparison；完整横向判断写到 `comparison/`。
- 普通 L1 不需要覆盖所有实验；只保留关键机制、关键风险和关键对照。

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
paper_type: <core-rl-method | environment-recipe | infra-interface | benchmark-env | survey | data-overlap>
lifecycle_role: <survey-seed | canonical-anchor | strong-baseline | frontier-candidate | background | low-confidence-novelty-risk>
boundary_risk: <none | data | recipe | framework | reasoning | infra>

failure_modes: [<from doc/taxonomy/failure-modes.md>]
design_knobs: [<from doc/taxonomy/design-knobs.md>]

rl_env: <web | gui | tool | code | embodied | game | simulated | mixed>
rl_interaction: <online | offline-rollout | replay | self-play | environment-generated>
rl_reward: <outcome | process | verifier | human | tool-success | dense | sparse>
rl_credit: <trajectory | step | token | tool-call | state | segment>
---
```

Source-only metadata 放在文件尾部，不放开头 YAML：

```markdown
<!-- meta:
authors: [<first author>, et al.]
url: <url>
arxiv_id: <id if any>
pdf: papers/<file>.pdf
brief: _meta/briefs/papers/<file>.md
survey: <seed / forward recall source>
rl_optimizer: <policy-gradient | actor-critic | grpo-like | dpo-like | q-learning | search | other>
rl_data_reuse: <none | replay | rejection-sampling | off-policy | curriculum>
rl_warm_start: <none | standard | data-centric | required | unclear>
-->
```

## 一句话定位

在 Agentic RL 谱系里的位置，≤30 字中文。

## 难题 / Failure Modes

> 开头 YAML 的 `failure_modes` 必须从 `doc/taxonomy/failure-modes.md` 选择；正文解释本文如何定义和处理这些 failure，不要只贴标签。
> 2-3 行即可；每格一句短句。只写本文真正处理的 failure，不凑表。

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` |  |  |  |

## 方法机制

3-5 句话说明训练闭环如何运行：rollout 如何产生、reward/advantage 如何计算、policy 如何更新、额外模块如何参与。不展开完整公式，除非公式就是核心方法。证据锚点直接写在句尾，例如 `[PDF §3.1]`、`[Table 2]`、`[Appendix D]`。

## 相对方法

3-4 行即可。只写“这篇论文为什么要和谁比”，不是完整 comparison。

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO / PPO / GiGPO / ... |  |  |  |

## 设计决策 / Design Knobs

> 开头 YAML 的 `design_knobs` 必须从 `doc/taxonomy/design-knobs.md` 选择；正文解释本文在 agentic RL training loop 里改了哪些设计选择。
> 2-4 行即可。这里不是写 paper-specific 风险，而是写方法属于哪些设计 knob。

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` |  | trajectory / token / step / state / segment |

## 方法优缺点 / 适用边界

- 优势：1-2 条。
- 不足 / 风险：1-2 条。

<!-- meta:
authors:
url:
arxiv_id:
pdf:
brief:
survey:
rl_optimizer:
rl_data_reuse:
rl_warm_start:
-->

## 模板原则

- 开头 YAML 控制在 8-12 行；只放人会看、Obsidian 会筛选的字段。
- `rl_axes` 不再使用 nested mapping；新卡使用 `rl_env` / `rl_interaction` / `rl_reward` / `rl_credit` 等 flat fields，避免 Obsidian 显示 JSON object。
- `failure_modes` 和 `design_knobs` 放 YAML 做机器聚类；body 表格只解释这些标签在本文里的含义。
- `Design Knobs` 是 RL training design space 的决策位点，不是 paper-specific 风险清单。
- `Evidence` 不单独成节；有用证据锚点写进正文，PDF/brief/source metadata 放尾部 HTML 注释。
- `收录判定` 属于 queue / triage，不放给人读的 card body。
