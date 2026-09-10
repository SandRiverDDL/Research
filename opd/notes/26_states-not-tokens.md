---
title: "Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation"
authors: [Dong Nie]
org: independent
year: 2026
venue: arxiv
arxiv_id: 2605.22731
url: https://arxiv.org/abs/2605.22731

confidence: 4
verified: a

addresses:
  - exposure-bias
  - no-new-capability

decisions:
  rollout: student
  loss: reward
  signal: outcome
  iteration: iterative
  filter: none
  extra: none
---

> **一句话**：state distribution 视角的统一框架。

## 核心做法

论文把 post-training 统一为 state-conditioned supervision：state 是 prompt 加已生成 prefix，SFT、RL、OPD 的关键差异之一是 state source 和 signal source。它把 OPD 定义成 teacher-guided on-policy learning，而不是单纯 token matching。

$$s_t=(x,y_{<t}),\qquad d_\theta(s)=\Pr_{\pi_\theta}(x,y_{<t})$$

实操含义：OPD 的关键不只是 teacher token，而是 student 在训练中实际访问哪些 prefixes。

## 机制发现（可选）

- [作者 ack paper brief §2.1-2.2]: autoregressive state 被定义为 prompt + prefix，state source 与 signal source 是两条正交轴。
- [作者 ack paper brief §2.3-2.5]: SFT 是 off-policy state fitting，RL 是 on-policy local improvement，OPD 是 teacher-guided on-policy learning。
- [作者 ack paper brief §3]: 统一框架把 post-training 写成 state-conditioned supervision，而不是只比较 loss 名称。

## 谱系位置

- 上游：GKD (2024) — 从 imitation learning 引入 student-generated trajectories。
- 同期：On the Geometry of OPD (2026) — 本篇看 state distribution，Geometry 看 parameter update subspace。
- 下游：synthesis report — 适合作为 OPD 方法谱系的理论背景，而非单一方法 baseline。

## 优缺点

- ✅ [作者 ack paper brief §2-3]: 把“on-policy 为什么有用”从 token matching 改写为 state coverage / state provenance 问题。
- ⚠️ [作者 ack paper brief §3]: 框架偏解释性，不直接给出 teacher reliability 或 filtering 的可执行算法。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief §2 / §3 -->
