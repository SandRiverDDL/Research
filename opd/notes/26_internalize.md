---
title: "Internalize the Temperature: On-Policy Self-Distillation as Policy Reheater for Reinforcement Learning"
authors: [Xuewei Yang, et al.]
org: tsinghua
year: 2026
venue: arxiv
arxiv_id: 2606.00755
url: https://arxiv.org/abs/2606.00755

confidence: 3
open_source: partial
verified: a

surveys:
  song-2026: "§5.3 self-distillation / behavioral PI context"

addresses:
  - entropy-collapse
  - mode-collapse-fwdkl

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: iterative
  filter: score-threshold
  extra: none
---

> **一句话**：policy reheating 型自蒸馏。

## 核心做法

RLVR 后期 policy entropy collapse 后，临时升采样温度只改变 rollout policy，不改变模型参数；本文用当前模型 logits 的高温 softmax 构造 stop-gradient self-teacher，把探索分布内化进权重。

$$p_T(v)\propto q_\theta(v)^{1/T}$$

训练时在 on-policy rollouts 上做 KL self-distillation，熵从低阈值恢复到目标阈值后停止，再回到原 RL 流程继续优化。

## 谱系位置

- 上游：GKD / OPSD (2024-2026) — 继承 on-policy distillation 的 student rollout + dense logit supervision
- 上游：DAPO / RLVR pipeline — 方法作为 entropy collapse 后的 inter-stage intervention 插入
- 同期：OPCD / OEL (2026) — 都是把额外上下文或行为信号内化到参数，Internalize 只内化温度分布形状
- 下游：cascaded OPSD-RL schedules — 作者将多轮 reheating + RL 作为未来方向

## 优缺点

- ✅ [作者 ack §3.2]：温度变换保留 token ranking，只改变分布锐度，降低语义偏序被破坏的风险
- ✅ [作者 ack §5]：把 entropy restoration 与 RL objective 解耦，可作为模块化 inter-stage 操作
- ⚠️ [作者 ack §Limitations]：实验只覆盖 Qwen3-4B/8B，entropy trigger 和 recovery target 是经验阈值，不是原则化优化

## headline number

- Avg@8 29.40 → 31.46 on Qwen3-4B and 34.27 → 36.60 on Qwen3-8B（§4.2 Table 1）

<!-- pdf: §3.2 Temperature-Scaled OPSD / §4.2 Main Results / §Limitations -->
<!-- song-2026: §5.3 Self-Distillation -->
