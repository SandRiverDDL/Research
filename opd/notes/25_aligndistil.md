---
title: "AlignDistil: Token-Level Language Model Alignment via Adaptive Policy Distillation"
authors: [Songming Zhang, et al.]
org: bjtu-tencent
year: 2025
venue: acl-2025
arxiv_id: 2503.02832
url: https://arxiv.org/abs/2503.02832

confidence: 4
verified: s

surveys:
  song-2026: "§4.3 RL-augmented objectives; Table 5; experimental table"

addresses:
  - coarse-credit-assignment

decisions:
  rollout: mixed
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: rm
---

> **一句话**：preference 路径的 OPD 先行作。

## 核心做法

把 RLHF/DPO 的 sequence-level preference 目标改写成 token-level distillation：DPO 隐式 reward 给出 teacher distribution，再用正常 DPO 与 reverse DPO 构造 contrastive reward，并按 token 自适应外推 teacher logits。

$$\pi^*(y|x)\propto\pi_{\mathrm{ref}}(y|x)\exp(r(y,x)/\beta)$$

实操含义是把稀疏 response-level feedback 变成每个 token 的分布监督，避免好 token 被整句惩罚或坏 token 被整句奖励。

## 谱系位置

- 上游：DPO (2024) — AlignDistil 使用 DPO implicit reward 推出 token-level teacher distribution
- 上游：RTO (2024) — 同样关心 token-level reward，AlignDistil 改为直接蒸馏分布而非只做 scalar reward 优化
- 下游：G-OPD (2026) — survey 将其列在同一 RL-augmented objective 谱系，进一步把 OPD 写成 dense KL-RL / reward extrapolation
- 下游：REOPOLD (2026) — 同表中沿 log-ratio token reward 继续推进

## 优缺点

- ✅ [作者 ack §1]：把 sequence-level RLHF objective 等价化为 token-level distillation，直接解决 response-level reward 的粗粒度 credit assignment
- ✅ [song-2026 §4.3]：DPO-style 方法适合 preference pair 比 full teacher logits 更容易构造的场景
- ⚠️ [song-2026 §4.3]：它仍在 KL-constrained policy optimization 谱系内，信号层级取决于可获得的偏好/teacher 信息

## headline number

- AlpacaEval 2.0 LC WR 16.51 → 19.45（§6.1 Table 2）

<!-- pdf: §1 Introduction / §4 Method / §6.1 Analysis / §7 Related Work -->
<!-- song-2026: §4.3 RL-Augmented Objectives / Table 5 -->
