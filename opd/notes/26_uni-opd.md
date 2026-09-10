---
title: "Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe"
authors: [Wenjin Hou, et al.]
org: other
year: 2026
venue: arxiv
arxiv_id: 2605.03677
url: https://arxiv.org/abs/2605.03677

confidence: 4
verified: a

surveys:
  song-2026: "§7.1 curriculum and difficulty adaptation; Table 9"

addresses:
  - capacity-gap
  - order-inconsistent-token-signal
  - flawed-prefix-trap

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: data-balancing
  extra: none
---

> **一句话**：student/teacher 双视角的统一 OPD recipe。

## 核心做法

Uni-OPD 把 OPD 失败拆成两个正交瓶颈：student 侧没有探索到 informative states，teacher 侧 token-level supervision 与 outcome ordering 不一致。对应地，它用 difficulty-aware + correctness-aware data balancing 促进 informative rollout，再用 outcome-guided margin calibration 恢复正确/错误轨迹之间的 order consistency。

$$\text{reliable OPD}=\text{informative states}+\text{outcome-consistent token guidance}$$

实操含义：既要问“学生采到了值得学的状态吗”，也要问“teacher token 分数是否真的按最终答案质量排序”。

## 谱系位置

- 上游：PACED (2026) — PACED 用 pass rate 选 competence boundary；Uni-OPD 扩展为 difficulty + correctness 双准则。
- 同期：SCOPE / SOD (2026) — 也处理 teacher signal reliability，但 Uni-OPD 把 student exploration 与 teacher calibration 分解成两个视角。
- 下游：LLM/MLLM multi-teacher OPD — Uni-OPD 声称覆盖 5 domains / 16 benchmarks，可作为 recipe 层 baseline。

## 优缺点

- ✅ [song-2026 §7.1]: 双视角把 curriculum 和 supervision reliability 解耦，说明两类问题可以独立处理。
- ✅ [作者 ack Abstract]: 覆盖 LLM/MLLM、single/multi-teacher、strong-to-weak、cross-modal 等设置。
- ⚠️ [song-2026 §7.1]: recipe 组件较多，作为机制归因时需要区分 data balancing 与 margin calibration 各自贡献。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §7.1 Curriculum and Difficulty Adaptation / Table 9 -->
