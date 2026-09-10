---
title: "ACC: Compiling Agent Trajectories for Long-Context Training"
year: 2026
venue: arxiv
paper_type: search-to-sft-distillation
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [coverage-gap, trajectory-distribution-mismatch]
data_knobs: [search-to-sft-distillation, trajectory-to-sft, observation-action-alignment]

agent_domain: mixed
data_object: trajectory
data_source: environment-generated
selection_signal: coverage
adaptivity: static
failure_use: ignore
training_consumer: sft
---

## 一句话

把 agent 轨迹编译成长上下文监督。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | 标准 agent SFT mask tool responses，只训练 tool selection，远距离 observation 证据没有监督。 | 把 search / SWE / SQL 轨迹中的工具返回和环境观察编译成长上下文 QA。 | 是否提升真实工具执行策略，需要和原 agent SFT 联合评估。 |
| `trajectory-distribution-mismatch` | agent 轨迹中的证据分散在多轮，和普通长文档合成不同。 | 用真实 agent rollout 作为长上下文训练源。 | 训练为 direct answer 可能弱化后续工具调用行为。 |

## 核心做法

ACC 的关键不是生成新 trajectory，而是把已有 agent 轨迹重新实例化为 long-context QA：输入包含原问题、tool responses 和多轮 environment observations，目标是直接回答原任务，从而监督模型整合远距离证据。[Brief] 论文明确指出标准 agent SFT mask tool responses，导致散落证据没有被训练到。[arXiv abstract] 对你的 30B A3B MoE 很贴：作者直接训练 Qwen3-30B-A3B，MRCR 68.3（+18.1）、GraphWalks 77.5（+7.6），并声称保持 GPQA、MMLU-Pro、AIME、IFEval。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `search-to-sft-distillation` | 把工具轨迹中的 observation 编译为 QA supervision。 | 只对 assistant action / final answer 做 SFT。 |
| `observation-action-alignment` | 强化 question 与远距离 evidence 的显式依赖。 | 让模型在 masked tool response 轨迹里隐式学。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 标准 agent SFT | mask tool responses，监督盲区在 observation 证据整合。 | 编译轨迹为 long-context QA。 | 可能更像训练“读轨迹回答”，不是完整 agent action policy。 |

## 谱系位置

- 上游：agent trajectory SFT、long-context SFT。
- 同期：Open-SWE-Traces、S1-DeepResearch、DataMind。
- 下游：benchmark bad case 中“stdout/文件/多轮证据已出现但最终没整合”的数据增强。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 这是 SFT 数据重构，不是 RL algorithm。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：直接命中长程 observation grounding，而且模型规模与用户的 A3B MoE 接近。
- 不足 / 风险：摘要级证据还不足以判断数据构造细节、负样本处理和是否会损害 tool-use policy。

<!-- meta:
authors: [Qisheng Su, et al.]
url: https://arxiv.org/abs/2605.21850
arxiv_id: 2605.21850
pdf:
brief: _meta/briefs/papers/2605.21850_acc-agent-context-compilation.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
