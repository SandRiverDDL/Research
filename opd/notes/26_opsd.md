---
title: "Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models"
authors: [Siyan Zhao, et al.]
org: meta-ucla
year: 2026
venue: icml-2026
arxiv_id: 2601.18734
url: https://arxiv.org/abs/2601.18734

confidence: 2
open_source: yes
verified: r

surveys:
  song-2026: "§3 key methods; §5.3 privileged information; Table 2"

addresses:
  - privileged-context-gap
  - compounding-error

decisions:
  rollout: student
  loss: jsd
  signal: logit
  iteration: iterative
  filter: none
  extra: privileged-info
---

> **一句话**：GT-conditioned self-distillation 基线。

## 核心做法

同一模型分成两个 context：teacher 看问题和 ground-truth solution，student 只看问题；student 自己 rollout，teacher 在同一 prefix 上给 full-vocabulary next-token distribution，梯度只回传 student logits。

$$\mathcal{L}=\mathbb{E}_{(x,y^\star)}\mathbb{E}_{\hat y\sim p_S}\left[\frac1{|\hat y|}\sum_n D(p_T(\cdot|x,y^\star,\hat y_{<n})\|p_S(\cdot|x,\hat y_{<n}))\right]$$

核心假设是 rationalization gap：对同一个模型，看到参考解后“解释为什么”比从零生成更容易，因此可作为自己的 privileged teacher。

## 谱系位置

- 上游：GKD / MiniLLM (2024) — 继承 student rollout 上做 dense distribution matching
- 同期：RLVR / GRPO — OPSD 用 dense token supervision 替代稀疏 binary reward
- 下游：HDPO (2026) — 在 GRPO cliff prompt 上接入 GT-conditioned self-distillation
- 下游：GATES / π-Distill / OEL (2026) — survey 将 OPSD 作为 privileged self-distillation 家族的基线

## 优缺点

- ✅ [作者 ack §3.2]：不需要外部 teacher 或 reward model，teacher/student 共享参数，只靠 conditioning context 产生监督差异
- ✅ [song-2026 §5.3]：GT-conditioned PI 是 self-distillation 中最清晰的信号来源之一
- ⚠️ [song-2026 §5.3]：当问题超过模型 comprehension threshold 时，即使看到 ground truth，teacher 也可能无法给出有意义 supervision

## headline number

- Qwen3-1.7B Avg@12 37.7 → 43.4 vs GRPO（§4 Table 2）
- generation cap 1024 tokens vs GRPO 16k in token-efficiency comparison（§4 Figure 3）

<!-- pdf: §3.1 Learning from Verifiable Reasoning Dataset / §3.2 OPSD / §4 Results -->
<!-- song-2026: §3 Key Methods / §5.3 Privileged Information -->
