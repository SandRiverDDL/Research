---
title: "Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation"
authors: [Yuchen Cai, et al.]
org: ustc-tencent-nus
year: 2026
venue: neurips-2026
arxiv_id: 2605.11739
url: https://arxiv.org/abs/2605.11739

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "§6 Training Efficiency; Table 9"

addresses:
  - parameter-update-redundancy
  - sgo-generation-cost

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: iterative
  filter: score-threshold
  extra: none
---

> **一句话**：OPD 参数更新冗余的加速路线。

## 核心做法

论文从参数动力学解释 OPD 为什么比 RL 更高效：OPD 早期就锁定接近最终模型的 update trajectory，并把更新集中在 reasoning 更关键的中间层/主子空间。EffOPD 利用这个“foresight”，在指数 checkpoint 处沿当前 update direction 做 adaptive extrapolation，并用小验证集接受或拒绝候选参数。

$$\theta'=\theta_t+\alpha(\theta_t-\theta_{t_0})$$

实操含义：当 OPD 的方向已经稳定，继续小步 dense training 可能是在补 magnitude；可以用验证门控的参数外推减少冗余更新。

## 机制发现（可选）

- [作者 ack Abstract / §2]: OPD 在 module-allocation level 避免低边际收益模块的冗余更新，中间层 MLP 对 reasoning gain 更关键。
- [作者 ack §3]: OPD update matrix 更低秩，主子空间早期就与最终更新子空间高度对齐。
- [作者 ack §4.1]: EffOPD 在 exponential checkpoints 生成 extrapolated candidate，用 50 examples validation 接受；若候选失败则退回 vanilla OPD。

## 谱系位置

- 上游：GKD / MiniLLM / industrial OPD recipes — 继承 student rollout + dense teacher supervision 训练框架。
- 同期：Prune-OPD (2026) — Prune-OPD 省 generation/scoring suffix；EffOPD 省参数优化步数。
- 同期：Rock Tokens (2026) — 两者都识别 OPD 冗余，Rock Tokens 是 token/window 层面，EffOPD 是 parameter-subspace 层面。

## 优缺点

- ✅ [作者 ack §2-3]: 把 OPD efficiency 从“dense reward 更稳定”的宏观说法推进到模块分配和低秩方向锁定。
- ✅ [作者 ack §4]: 加速器是 plug-and-play，不引入额外 trainable modules。
- ⚠️ [作者 ack §4.1 / Appendix C]: 外推接受依赖小验证集，若 validation 不代表最终目标，可能把稳定方向误判为可外推方向。

## headline number

- Average training acceleration about 3x while maintaining comparable final performance（§Fig 6 / §Fig 7）

<!-- pdf: arXiv HTML v3 Abstract / §2 Functional Redundancy Avoidance / §3 Early Low-Rank Lock-in / §4.1-4.2 / Appendix C -->
<!-- song-2026: §6 Training Efficiency / Table 9 -->

<!-- venue verified 2026-10-04: https://neurips.cc/Downloads/2026 ; official entry: https://neurips.cc/virtual/2026/poster/154435 -->
