---
title: "Teacher-Guided Policy Optimization for On-Policy Reasoning Distillation under Large Policy Divergence"
authors: [Xinyu Liu, et al.]
org: neu
year: 2026
venue: arxiv
arxiv_id: 2605.13230
url: https://arxiv.org/abs/2605.13230

confidence: 3
verified: a

surveys:
  song-2026: "§4.3 RL-augmented objectives; Table 5"

addresses:
  - large-policy-divergence
  - policy-gradient-variance

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：directional teacher guidance 代表作。

## 核心做法

大 teacher 与小 student 分布差距很大时，RKL/log-ratio 更像事后判分，不能告诉 student 下一步该往哪走；TGPO 在 student rollout 每一步引入 teacher 预测作为 differentiable guidance，并把它嵌入 GRPO 更新。

$$J_{\mathrm{TGPO}}=J_{\mathrm{GRPO}}+w_t J_{\mathrm{Guidance}}$$

实操上，guidance 权重线性衰减：早期靠 teacher 给方向，后期退回纯 RL，避免 teacher 约束长期压制 exploration。

## 谱系位置

- 上游：MiniLLM / RKL-OPD — TGPO 批评 RKL 在 rejection regime 中缺少 directional guidance
- 上游：KDRL / OP Distill — 同样结合 KD 与 RL，TGPO 更强调把 teacher signal 放进 policy gradient 内部
- 同期：REOPOLD (2026) — REOPOLD 把 log-ratio 当 token reward 并 clipping，TGPO 改成 dense directional guidance
- 下游：dGRPO / CoDistill-GRPO — survey 将其放在 RL-augmented objectives 的 dense guidance 分支

## 优缺点

- ✅ [作者 ack §3.2]：annealed guidance 在 early training 提供 teacher 方向，后期让 GRPO 主导
- ✅ [song-2026 §4.3]：把 teacher guidance 嵌入 policy gradient，减少 additive KD+RL 里手调平衡项的问题
- ⚠️ [作者 ack §5.3]：guidance scheduling 本身仍是关键超参，过强或过久会限制 RL 探索

## headline number

- ID avg 41.7 → 45.6 vs KDRL, OOD avg 56.8（§5.1 Table 1）
- RKL baseline length explosion beyond 8000 tokens（§5.2 Figure 4）

<!-- pdf: §2 RKL Limitations / §3 TGPO / §5 Results / Appendix A -->
<!-- song-2026: §4.3 RL-Augmented Objectives / Table 5 -->
