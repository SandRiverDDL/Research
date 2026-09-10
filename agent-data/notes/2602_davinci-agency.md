---
title: "daVinci-Agency: Unlocking Long-Horizon Agency Data-Efficiently"
year: 2026
venue: arxiv
paper_type: real-world-trajectory-mining
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [long-horizon-drift, coverage-gap, real-log-privacy-bias]
data_knobs: [real-log-mining, trajectory-source, success-filtering, difficulty-curriculum]

agent_domain: code
data_object: trajectory
data_source: real-world-log
selection_signal: success
adaptivity: static
failure_use: discard
training_consumer: sft
---

## 一句话

PR 演化链作为长程监督。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-drift` | 合成长轨迹每步独立，容易丢真实依赖。 | 从 semantically linked PR chains 构造跨阶段监督。 | 依赖高质量 repo 历史，迁移成本高。 |
| `coverage-gap` | 单 issue / 单 feature 数据覆盖不了项目演化。 | 链接最多 5 个 PR，保留 evolving states。 | 只覆盖可挖掘的 GitHub 开发模式。 |

## 核心做法

daVinci-Agency 的核心不是“合成长任务”，而是把真实项目演化建模成 chain-of-PRs。每个 PR chain 是语义相关 PR 的有序序列，后续 PR 迭代、修复或扩展前序 PR，因此轨迹天然包含长期一致性和阶段目标。[arXiv HTML §3.2] 论文从 9 个 GitHub repositories 挖链，并构造平均 85k tokens、116 tool calls 的长轨迹。[Brief] 结果上，GLM-4.6 只用 239 samples 微调，在 Toolathlon 上报告 47% relative gain；论文还包含 Qwen3-30B-A3B 的 fine-tuning 结果。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `real-log-mining` | 挖真实 PR 演化链。 | synthetic issue / single PR demo。 |
| `trajectory-source` | real-world repository history。 | teacher rollout 或 benchmark replay。 |
| `success-filtering` | evolving ground truth state 对齐和 rejection sampling。 | LLM judge 估计成功。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| SWE-Smith / isolated SWE data | 单步或单 issue 缺少跨阶段依赖。 | PR chain 保留演化逻辑。 | 数据少，repo selection bias 明显。 |

## 谱系位置

- 上游：SWE-bench / GitHub PR mining。
- 同期：Open-SWE-Traces、SWE-Master、DeNovoSWE。
- 下游：内部任务历史 / PR 历史的 long-horizon agent SFT。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 这是 supervised long-horizon trajectory data。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：对你当前 M2 长程任务和 M4 failure-switching 很关键，尤其提醒“真实历史 > 纯合成长轨迹”。
- 不足 / 风险：样本极少且依赖 repo 选择；需要做 regression guardrail，避免只提升 code-agent 长程场景。

<!-- meta:
authors: [Mohan Jiang, et al.]
url: https://arxiv.org/abs/2602.02619
arxiv_id: 2602.02619
pdf:
brief: _meta/briefs/papers/2602.02619_davinci-agency.md
survey: user known-item
agentic_rl_overlap: false
agentic_rl_queue: none
-->
