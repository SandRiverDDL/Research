---
title: "Rubric-based On-policy Distillation"
authors: [Junfeng Fang, et al.]
org: other
year: 2026
venue: arxiv
arxiv_id: 2605.07396
url: https://arxiv.org/abs/2605.07396

confidence: 4
open_source: yes
verified: a

surveys:
  song-2026: "§5.2 black-box and API-constrained distillation; Table 7"

addresses:
  - api-only-teacher
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: reward
  signal: verbal
  iteration: one-shot
  filter: none
  extra: verbal-feedback
---

> **一句话**：用 structured rubric 替代 teacher logits 的 black-box OPD。

## 核心做法

ROPD 认为 OPD 对 teacher logits 的依赖限制了 black-box/API teacher 使用；它从 teacher-student contrasts 归纳 prompt-specific rubrics，再用这些 rubrics 给 student rollouts 打 semantic score，作为 on-policy optimization 的 reward。

$$x,y_\theta,y_T\rightarrow \mathrm{rubric}(x)\rightarrow r_{\mathrm{rubric}}(x,y_\theta)$$

实操含义：把 white-box token logits 换成可解释的 structured semantic rubric，使 proprietary teacher 只能出文本时也能做 on-policy distillation。

## 谱系位置

- 上游：GAD / Lion — 同属 black-box teacher distillation，但 ROPD 用 semantic rubrics 而不是 discriminator 或 adversarial game。
- 同期：OmniOPD / black-box OPD — 都试图绕过 logit access；ROPD 的接口最语义化。
- 下游：API teacher OPD — 可作为 proprietary/open teacher 混用时的简单 baseline。

## 优缺点

- ✅ [作者 ack Abstract]: structured rubrics 可作为 teacher logits 的 scalable alternative，只需 teacher-generated responses。
- ✅ [song-2026 §5.2]: rubric-based semantic scoring 是 black-box/API-constrained distillation 的重要路线。
- ⚠️ [作者 ack Abstract]: semantic score 是 sequence-level/rubric-level signal，token-level credit assignment 不如 white-box logit OPD 直接。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §5.2 Black-Box and API-Constrained Distillation / Table 7 -->
