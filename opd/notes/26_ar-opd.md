---
title: "Beyond Absolute Imitation: Anchored Residual Guidance for Privileged On-Policy Distillation"
authors: [Wenhao Zhang]
org: scut
year: 2026
venue: arxiv
arxiv_id: 2606.10385
url: https://arxiv.org/abs/2606.10385
zotero_key:

confidence: 4
open_source: yes
verified: a

addresses:
  - privileged-context-gap
  - flawed-prefix-trap

decisions:
  rollout: student
  loss: forward-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: privileged-info
---

> **一句话**：privileged OPD 的 anchor/residual 解耦路线。

## 核心做法

Privileged OPD 的痛点：full-view teacher 见到 oracle answer 后，会把概率质量推到学生当前 prefix 不可达的 hindsight token 上 → 学生模仿这些 "答案条件化" token 形成 shortcut。AR-OPD 的处方是不直接模仿 full teacher，而是用 partial-oracle teacher（去掉答案）作为 **causally reachable anchor**，再把 full-view 的 log-prob 增量作为 **λ-scaled residual** 加上去，把"foresight"转成可控更新而非绝对模仿目标。

## 谱系位置

vs. SDFT / OPSD：这两者都把 privileged teacher 当作 monolithic imitation target（SDFT 用 EMA 稳定，OPSD 用 JSD + clipping），AR-OPD 第一次明确把 privileged 信号 **解耦**为 reachable anchor 与 future-directed residual 两个可独立调控的组件，并定量诊断 hindsight leakage / 长程 reliability 退化。

## Method

Loss = forward-KL( q_anchor + λ·(log q_full − log q_partial) ‖ π_θ )，其中 anchor 把 reference trace 截断到前 ρ=0.5 比例（去掉答案）。每个 student state 需要两次 teacher forward。Base = Qwen2.5-7B-Instruct，单一模型族；4 个领域：NuminaMath→MATH500/AMC23、Magicoder-Evol→HumanEval/MBPP、SciKnowEval Chem L-3、MedMCQA→MedQA/MedCQA；max_completion=1024 tok，λ ∈ {0.4, 0.6, 0.8, 1.0, 1.2} 扫描。

## 优缺点

- ✅ [作者 ack §4.2]: 把 full-view privilege 拆成 reachable anchor 与 future-directed residual，可诊断并缓解 shortcut leakage。
- ⚠️ [作者 ack Appendix B]: 每个 student state 需要 partial/full 两次 teacher forward，训练成本高于普通 privileged OPD。

## headline number

- Full OPD 68.0 → AR-OPD 70.3 average; shortcut leakage -21.7%; long rollout segment +7.2（§6.2 Table 1）

## Evidence

- TL;DR 数字 +2.3 / 21.7% / 7.2 来自 Abstract & §1 contributions ❸ & §6.2 Table 1
- "full-view pass@4 从 90.18% → 9.09%（128→768-1024 tok）" 来自 §4.2
- MATH500 +3.6 / AMC23 +2.5 vs Full OPD 来自 §6.2 Table 1
- 项目页 https://vanhowe.github.io/AR-OPD/ 含训练/评测 code（Appendix B）

<!-- pdf: §4 Failure Analysis / §6.2 Experiments / Appendix B -->
