---
title: "DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch"
year: 2026
venue: arxiv
paper_type: synthetic-verifiable-data
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [coverage-gap, long-horizon-drift, difficulty-mismatch]
data_knobs: [environment-synthesis, difficulty-curriculum, failure-repair]

agent_domain: code
data_object: environment
data_source: synthetic
selection_signal: difficulty
adaptivity: curriculum
failure_use: repair
training_consumer: sft
---

## 一句话

whole-repo generation 的可验证长程数据。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | 现有 SWE 数据多是局部 bug fixing，缺 whole-repository generation。 | 构造 4,818 个从文档生成完整 repo 的实例。 | 规模相比 trace dataset 小，泛化范围需验证。 |
| `difficulty-mismatch` | 长程任务既要质量也要多样性。 | difficulty-aware trajectory filtering。 | 难度指标如何定义需读全文。 |

## 核心做法

DeNovoSWE 把 SWE agent training 从 patch-level 推到 whole-repository generation：每个实例要求从 documentation 生成完整 repo，数据通过 sandboxed agentic workflow 自动构造，无需人工标注。[Brief] 其机制口号是 divide-and-conquer + critic-repair，并加入 difficulty-aware trajectory filtering 平衡质量和多样性。[arXiv abstract] 作者报告 fine-tune Qwen3-30B-A3B 后 BeyondSWE-Doc2Repo 从 5.8% 提升到 47.2%。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `environment-synthesis` | 用 sandboxed workflow 构造 whole-repo 任务。 | 从已有 issue/PR 中抽局部任务。 |
| `failure-repair` | critic-repair philosophy。 | 成功轨迹过滤或人工修正。 |
| `difficulty-curriculum` | difficulty-aware filtering。 | 无差别混合长程样本。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| SWE bug-fix 数据 | 偏局部 patch，不训练架构级长程构建。 | 从文档到完整 repo 的 synthetic/verifiable data。 | 可能偏向 repo generation benchmark，不一定提升普通 SWE-bench。 |

## 谱系位置

- 上游：SWE-bench / Doc2Repo / synthetic SWE。
- 同期：Open-SWE-Traces、SWE-Master、SWE-Lego。
- 下游：长程任务分解、spec ledger、critic-repair 数据。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 重点是可验证数据构造和 filtering，不是 RL update。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：直接连接 M2 长程任务分解和 difficulty-aware 数据选择。
- 不足 / 风险：需要核查 generated repos 的 verifier 强度和是否存在 benchmark overfit。

<!-- meta:
authors: [Jiale Zhao, et al.]
url: https://arxiv.org/abs/2606.10728
arxiv_id: 2606.10728
pdf:
brief: _meta/briefs/papers/2606.10728_denovoswe.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
