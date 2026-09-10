---
title: "Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents"
year: 2026
venue: arxiv
paper_type: real-world-trajectory-mining
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [coverage-gap, real-log-privacy-bias, long-horizon-drift]
data_knobs: [real-log-mining, teacher-rollout, trajectory-to-sft]

agent_domain: code
data_object: trajectory
data_source: real-world-log
selection_signal: coverage
adaptivity: static
failure_use: ignore
training_consumer: sft
---

## 一句话

真实 PR 来源的 SWE 轨迹数据。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | SWE agent 缺少大规模、多语言、长程轨迹。 | 从 20,000 real-world PRs 构造 207,489 trajectories。 | PR 分布和 benchmark 分布是否一致需要核查。 |
| `real-log-privacy-bias` | 真实代码数据涉及许可和来源约束。 | 过滤 permissive licenses，来自 SWE-rebench-V2。 | 开源许可过滤可能改变任务分布。 |

## 核心做法

Open-SWE-Traces 是典型 real-world trajectory mining seed：从 real-world PRs 出发，经 OpenHands 和 SWE-agent harnesses 生成 207,489 条跨 9 种语言的 agentic trajectories。[Brief] 它采用 hybrid-reasoning synthesis：Minimax-M2.5 生成带 thinking 的轨迹，Qwen3.5-122B 提供 non-thinking traces。[Brief] 作者验证在 Qwen3-30B-A3B 系列上 fine-tune，报告 SWE-bench Verified 61.7%、Multilingual 57.1%、Pro 36.8%。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `real-log-mining` | 真实 PR 作为 trajectory seed。 | 纯 synthetic issue / patch。 |
| `teacher-rollout` | 双模式 teacher 生成 thinking / non-thinking traces。 | 单一 teacher 蒸馏。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 合成 SWE 轨迹 | 可能偏离真实 repo edit 分布。 | 从真实 PRs 构造长程轨迹。 | teacher synthesis 仍可能引入风格 artifact。 |

## 谱系位置

- 上游：real-world PR mining、SWE-agent/OpenHands。
- 同期：SWE-Master、DeNovoSWE、SWE-Lego。
- 下游：内部 PR / 工单 / IDE 历史挖掘的数据方案。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 主要是 SFT trajectory dataset，不是 RL algorithm。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：和用户 30B A3B MoE 直接相关，且提供 real-world log mining 思路。
- 不足 / 风险：摘要未说明失败轨迹、negative samples 或 step-level mask；需要读 PDF 看 filtering。

<!-- meta:
authors: [Wasi Uddin Ahmad, et al.]
url: https://arxiv.org/abs/2606.16038
arxiv_id: 2606.16038
pdf:
brief: _meta/briefs/papers/2606.16038_open-swe-traces.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
