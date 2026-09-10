---
title: "ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation"
authors: [Anonymous]
org: other
year: 2026
venue: acl-arr-2026-may
arxiv_id: openreview-kv6QSpUJbc
url: https://openreview.net/forum?id=kv6QSpUJbc

confidence: 4
verified: a

addresses:
  - cross-rollout-credit
  - flawed-prefix-trap

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: trajectory-level
  extra: none
---

> **一句话**：negative trajectory weighting 路线。

## 核心做法

ReNIO 反转了“正确 rollout 更值得学”的默认直觉：incorrect student-generated outputs 可能暴露更大的 student-teacher deviations。方法由 prefix-computable student-teacher log-ratio、fixed-threshold key-token selection、geometric-mean sample weight 和 weighted distillation objective 组成。

$$w(y^-)=g\!\left(\frac{\pi_\theta(y^-)}{\pi_T(y^-)}\right),\qquad \mathcal{L}=\mathbb{E}_{y^-}[w(y^-)D_T(y^-)]$$

实操含义：过滤不应只保留正确轨迹；错误轨迹如果能定位差距，反而可能是高价值监督。

## 机制发现（可选）

- [作者 ack paper brief §3]: ReNIO 明确包含 log-ratio signal、key-token selection、geometric-mean aggregation 和 weighted objective 四个组件。
- [作者 ack paper brief §3.1-3.2]: student-generated output 在 student-visited prefixes 上接受 teacher token-level supervision，log-ratio 可前缀计算。
- [作者 ack paper brief §3.3-3.5]: fixed-threshold key tokens 被聚合成 sample-level normalized weight。

## 谱系位置

- 上游：MOPD (2026) — 利用同 prompt 多 rollout 的成功/失败对比。
- 同期：BRTS (2026) — BRTS 在 teacher rollouts 中选可靠正例，ReNIO 在 student 错误轨迹中挖纠错信号。
- 同期：Trajectory-Refined Distillation (2026) — 都减少“只看正确最终答案”的粗粒度监督。

## 优缺点

- ✅ [作者 ack paper brief §3]: 把 negative trajectory 从“过滤掉的失败样本”改写成可加权的监督资源。
- ⚠️ [作者 ack paper brief §4]: 负轨迹重权的噪声控制依赖 threshold 和 aggregation 设计，需要看 ablation。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached OpenReview PDF brief §3 / §4 -->
