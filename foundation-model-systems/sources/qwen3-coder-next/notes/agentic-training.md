# Qwen3-Coder-Next Agentic Training

```yaml
---
source_id: qwen3-coder-next
section_type: rl-training
stage: post-training
substage: agentic-coding-training
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Qwen3-Coder-Next 的核心训练信号来自 verifiable coding tasks paired with executable environments，目标是让模型从真实环境反馈学习 agentic coding。[1-3]
- 它强调 agentic training 不只是 post-training：mid-training 就加入 natural code、synthetic coding、多轮 agentic coding、instruction-following 和 FIM completion。[3-6]
- 大规模 agentic training 的 infra 问题被显式写入报告：Slurm 多 `srun` RPC 导致 startup bottleneck，Ray actor registration/GCS 在 3K+ GPU scale 下成为问题。[13]
- 小 active footprint 是 recipe 目标：80B total 但 3B active，要靠训练数据和环境反馈弥补 active params 小的问题。[1]

## Why It Matters

它是 MiMo 之外另一个非常适合读的 coding-agent recipe。MiMo 更强调 MOPD/agentic RL，Qwen 更强调 executable task synthesis、mid-training 和 domain experts。两者组合能帮你理解 2026 coding model 怎么从 static code pretraining 走向 environment-grounded training。

## Gaps / Open Questions

- Synthesis pipeline 细节和过滤阈值还不够完整。
- Executable environments 的质量、leakage、test robustness 需要进一步审计。
- RL objective 和 reward normalization 细节第一版未完全提取。

## Evidence Anchors

- **2026-10-19 数据来源补核（事实）**：§2.1 点名 SWE-smith、SWE-Flow、SWE-rebench、Multi-SWE-RL 作为带 executable repositories/tests 的 seed datasets，并进一步合成新 issues；另一路从真实 GitHub PR 构造 buggy/fixed states、Docker 与 verifier。点名 seeds 不等于最终扩展 corpus 全部公开。[2-3]
- 原文入口：https://arxiv.org/html/2603.00729#S2.SS1

- 1-3: task synthesis and environment-grounded training。
- 3-6: mid-training data。
- 13: Slurm/Ray infra bottlenecks。
