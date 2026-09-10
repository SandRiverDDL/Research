---
title: "Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation"
authors: [Guo Yu, et al.]
org: nju-alibaba
year: 2026
venue: arxiv
arxiv_id: 2606.13657
url: https://arxiv.org/abs/2606.13657

confidence: 3
verified: a

addresses:
  - no-new-capability
  - capacity-gap

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：dense supervision 的参数几何诊断。

## 核心做法

论文分析 OPD 训练后的参数变化，发现 dense teacher supervision 并不等于 dense parameter rewriting：OPD updates 小而 coordinate-sparse，跨层分布但 FFN 相对移动最大；同时数值上 full-rank、谱上集中。

$$\Delta\theta=\sum_t\nabla_\theta D(\pi_T(\cdot|s_t)\|\pi_\theta(\cdot|s_t))$$

实操含义：如果 OPD 的有效更新很稀疏，那么方法改进应关注哪些 states/parameters 被激活，而不是只增加 token 监督密度。

## 机制发现（可选）

- [作者 ack paper brief Abstract / §4]: OPD updates are small and coordinate-sparse，训练发现的 subnetwork 几乎能恢复 full-training performance。
- [作者 ack paper brief Abstract / §4.5]: OPD 中 SGD 不如 AdamW，说明 dense teacher supervision 仍保留有用 momentum / second-moment structure。
- [作者 ack paper brief Abstract / §5]: updates full-rank but spectrally concentrated，并偏离 source weights 的 principal singular subspaces。

## 谱系位置

- 上游：GKD / DistiLLM (2024) — 关注分布目标和训练稳定性。
- 同期：On the Geometry of OPD (2026) — 都把 OPD 放到参数空间解释，本篇更强调 dense signal 与 sparse update 的张力。
- 同期：Learning to Foresee (2026) — 都试图解释 OPD 的效率来源。

## 优缺点

- ✅ [作者 ack paper brief §3-5]: 给出 update sparsity、module structure、subnetwork sufficiency 和 spectral concentration 四类诊断。
- ⚠️ [作者 ack paper brief §6]: 几何发现仍主要是 post-hoc analysis，不能直接推出哪种 OPD objective 最优。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §3 / §4 / §5 / §6 -->
