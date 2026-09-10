---
title: "TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models"
authors: [Makoto Shing, et al.]
org: sakana-ai
year: 2025
venue: iclr-2025
arxiv_id: 2501.16937
url: https://arxiv.org/abs/2501.16937

confidence: 3
open_source: yes
verified: s

surveys:
  song-2026: "§5.1 white-box logit supervision; Table 6"

addresses:
  - capacity-gap
  - mode-collapse-fwdkl

decisions:
  rollout: offline
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: curriculum
  extra: none
---

> **一句话**：target-level curriculum 的代表作。

## 核心做法

在 logit 空间把 detached student distribution 和 teacher distribution 插值成中间 teacher，让目标从接近 student 逐步移动到完整 teacher，以缓解 capacity gap、mode averaging 与 mode collapse。

$$p_t(y_s|y^{<s})=\mathrm{softmax}((1-t)\mathrm{logit}_{q'_\theta}(y_s|y^{<s})+t\mathrm{logit}_{p}(y_s|y^{<s}))$$

训练损失是 KL($p_t\|q_\theta$)，只对 student 分布反传；$t$ 由 loss 相对变化率自适应更新，学习顺时更快揭示 teacher 信号。

## 谱系位置

- 上游：GKD (2024) — 同样用 teacher logits 做 token 级监督，但 GKD 通过 rollout mixture 处理 exposure bias
- 同期：PromptKD (2024) — PromptKD pre-hoc 调整 teacher，TAID post-hoc 调整 target distribution
- 下游：Veto (2026) — survey 将其与 TAID 同列为 student-friendly target reformulation
- 下游：PACED / AdaSwitch (2026) — survey 把 TAID 放进 prompt、token、target、teacher 四种 curriculum granularity 谱系

## 优缺点

- ✅ [作者 ack §3.1]：用 detached student logits 构造中间目标，让 teacher signal 难度随 student 能力平滑上升
- ✅ [song-2026 §5.1]：TAID 回答的是“每个阶段揭示多少 teacher knowledge”，区别于 PACED 的“选哪些问题”
- ⚠️ [song-2026 §5.1]：target-level curriculum 与 prompt/token/teacher-level curriculum 相互独立，现有系统尚未同时整合四者

## headline number

- MT-Bench 2.24 → 4.05 for Phi-3-mini→TinyLlama instruction tuning（§6.1 Table 1）

<!-- pdf: §3.1 Temporally interpolated distribution / §3.2 Adaptive scheduling / §6.1 Results -->
<!-- song-2026: §5.1 White-Box Logit Supervision / Table 6 -->
