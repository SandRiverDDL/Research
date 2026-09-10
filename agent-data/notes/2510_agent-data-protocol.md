---
title: "Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents"
year: 2025
venue: arxiv
paper_type: data-centric-posttraining
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [format-only-imitation, coverage-gap, action-grammar-fragility]
data_knobs: [action-schema, tool-call-grammar, coverage-balancing]

agent_domain: mixed
data_object: trajectory
data_source: mixed
selection_signal: coverage
adaptivity: static
failure_use: ignore
training_consumer: sft
---

## 一句话

统一异构 agent SFT 数据格式。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | agent 数据分散在 tool、browser、coding、SWE 等异构格式里，难以统一训练。 | 用 ADP 作为 interlingua，统一 13 个 agent training datasets。 | 格式统一不等于质量统一；过滤和 mixture 仍需另做。 |
| `action-grammar-fragility` | 每个框架有自己的 tool/action/interface 表达。 | 设计可解析、可训练的轻量表示。 | 是否会牺牲某些 domain-specific signal 需要看细节。 |

## 核心做法

ADP 的贡献是数据协议，不是单个生成算法。它把 API/tool use、browsing、coding、software engineering 和 general workflows 映射到统一表示，再转成多个 agent framework 的训练格式。[Brief] 作者称统一 13 个现有 agent 数据集后做 SFT，平均较 base model 提升约 20%，并在 coding、browsing、tool use、research benchmarks 上达到 SOTA 或 near-SOTA。[arXiv abstract]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `action-schema` | 用统一协议表达任务、工具、轨迹和框架接口。 | 每个数据集单独写转换脚本。 |
| `coverage-balancing` | 通过整合多 domain 数据提高 agent SFT 覆盖。 | 单 domain tuning。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 单数据集 agent SFT | 数据格式碎片化，难扩到多任务。 | 建协议层统一训练入口。 | 协议层可能隐藏质量差异和 failure 标签。 |

## 谱系位置

- 上游：ToolBench / WebLINX / SWE / browsing datasets。
- 同期：ACC、Open-SWE-Traces、SWE-Master。
- 下游：本项目可借鉴其 schema，设计内部 agent SFT 数据格式。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- ADP 是 SFT 数据协议；RL 不是核心贡献。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：直接解决“数据格式/接口碎片化”，适合作为你内部多类 SFT 数据统一 schema 的 seed。
- 不足 / 风险：协议和规模不自动保证 benchmark slice gain，需要再配合 failure-driven filtering / mixture。

<!-- meta:
authors: [Yueqi Song, et al.]
url: https://arxiv.org/abs/2510.24702
arxiv_id: 2510.24702
pdf:
brief: _meta/briefs/papers/2510.24702_agent-data-protocol.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
