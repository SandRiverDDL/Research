---
title: "OPD+: Rethinking the Advantage Design for On-Policy Distillation"
authors: [Hanyang Zhao, et al.]
org: columbia-amazon-meta
year: 2026
venue: arxiv
arxiv_id: 2606.01039
url: https://arxiv.org/abs/2606.01039

confidence: 3
verified: a

addresses:
  - stop-gradient-bias
  - policy-gradient-variance

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：OPD advantage 停梯度设计的理论修正路线。

## 核心做法

现有 OPD 常把 divergence reward 里的 student likelihood 停梯度，主要是为了训练稳定；OPD+ 指出对一般 f-divergence，这会让 reward objective 和对应 gradient 的估计有偏。论文给出基于 f-divergence 的通用 on-policy distillation 优化框架，并提出不把关键 student-likelihood 项错误停梯度的 corrected OPD+。

$$\nabla_\theta \mathbb{E}_{y\sim\pi_\theta}[R_f(y,\theta)] \neq \mathbb{E}_{y\sim\pi_\theta}[\mathrm{sg}(R_f)\nabla_\theta\log\pi_\theta(y)]$$

实操含义：如果 OPD loss 被写成 RL-style advantage，必须明确哪些 student-dependent reward 项允许反传，否则“稳定 trick”可能改变优化目标。

## 机制发现（可选）

- [作者 ack Abstract / §1]: divergence reward 依赖 student likelihood，通用 stop-gradient 会导致 reward objective 与 gradient 有偏。
- [作者 ack §1]: OPD+ 支持多种 f-divergence，而不是把 KL baseline 当作唯一可用目标。
- [作者 ack Abstract]: 在数学 reasoning 和 tool-use benchmarks 上优于 KL baseline。

## 谱系位置

- 上游：MiniLLM / sampled-token OPD / Tinker OPD — 共享 RL-style objective 与 advantage 估计问题。
- 同期：Revisiting OPD (2026) — Revisiting 关注 sampled-token estimator 的 bias-variance 与 support mismatch；OPD+ 关注 stop-gradient advantage design 的目标偏差。
- 同期：Rethinking OPD (2026) — Rethinking 给出 teacher/student 成败条件；OPD+ 给出 loss/gradient 层面的理论修正。

## 优缺点

- ✅ [作者 ack Abstract]: 把 OPD 的 stop-gradient 稳定 trick 提升为可证明的 objective-bias 问题。
- ✅ [作者 ack §1]: f-divergence 框架使 KL 以外的 divergence choice 可以被统一讨论。
- ⚠️ [作者 ack Abstract]: 当前公开信息只说明优于 KL baseline，具体收益仍需回表格/实验设置核查后才能作为强证据。

## headline number

无 Table/Fig anchor 的摘要级提升不放入 headline number。

<!-- pdf: arXiv HTML v1 Abstract / §1 -->
