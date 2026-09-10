---
title: "Reinforcement Learning from Rich Feedback with Distributional DAgger"
authors: [Rishabh Agrawal, et al.]
org: other
year: 2026
venue: arxiv
arxiv_id: 2606.05152
url: https://arxiv.org/abs/2606.05152

confidence: 3
verified: a

addresses:
  - exposure-bias
  - policy-gradient-variance

decisions:
  rollout: student
  loss: forward-kl
  signal: outcome
  iteration: iterative
  filter: none
  extra: none
---

> **一句话**：DAgger 理论的 rich-feedback 延伸。

## 核心做法

论文从 Distributional DAgger 角度审视 rich feedback RL：它区分 distill teacher 的 divergence measure 和优化它的 gradient estimator，并证明常见 f-divergence self-distillation 目标即使 teacher 更强，也不保证 monotonic policy improvement。

$$\max_\theta \mathbb{E}_{s\sim d_\theta}\mathbb{E}_{a\sim\pi^*(\cdot|s)}\log\pi_\theta(a|s)$$

实操含义：OPD/自蒸馏目标不只要看 dense signal，还要看它是否保留 imitation learning 的单调改进条件。

## 机制发现（可选）

- [作者 ack paper brief §3.1]: general f-divergence self-distillation objectives 在 contextual bandits 中也不保证 monotonic policy improvement。
- [作者 ack paper brief §3.2]: local tokenwise gradients 可能忽略早期决策对未来 teacher-student disagreement 的影响。
- [作者 ack paper brief §4]: forward cross-entropy 被用来连接 teacher-weighted likelihood of success 的下界。

## 谱系位置

- 上游：GKD (2024) — 从 DAgger 视角定义 OPD。
- 同期：OPD+ (2026) — 都从目标函数层面审视 OPD 的理论偏差。
- 同期：Post-Training is About States (2026) — 都把 learner-induced states 作为核心对象。

## 优缺点

- ✅ [作者 ack paper brief §3]: 给 OPD/OPSD 常用 divergence choice 提供“单调改进不保证”的理论反例。
- ⚠️ [作者 ack paper brief §1-3]: 它是 rich-feedback / DAgger 理论工作，不应被当作纯 OPD method baseline。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv PDF brief §3 / §4 -->
