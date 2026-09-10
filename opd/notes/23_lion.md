---
title: "Lion: Adversarial Distillation of Proprietary Large Language Models"
authors: [Yuxin Jiang, et al.]
org: hkust
year: 2023
venue: emnlp-2023
arxiv_id: 2305.12870
url: https://arxiv.org/abs/2305.12870

confidence: 3
open_source: partial
verified: s

surveys:
  song-2026: "Table 1 black-box signal; Table 2 black-box/API-constrained; §5.2 verbal feedback and curriculum"

addresses:
  - api-only-teacher

decisions:
  rollout: teacher
  loss: forward-kl
  signal: verbal
  iteration: iterative
  filter: curriculum
  extra: verbal-feedback
---

> **一句话**：早期把 API-only teacher 反馈做成闭环课程的黑盒蒸馏代表。

## 核心做法

针对 proprietary LLM 只能通过 API 访问的问题，Lion 让同一个 ChatGPT 扮演 teacher、referee 和 generator：先用 teacher response imitation 训练 student，再用 referee 找出 student 落后的 hard instructions，最后让 generator 围绕这些 weakness 生成新指令。

$$d_i=\mathrm{score}_{\mathcal{R}}(\mathcal{T}(x_i))-\mathrm{score}_{\mathcal{R}}(\mathcal{S}(x_i)),\quad d_i\ge\tau\Rightarrow x_i\in X_{\mathrm{hard}}$$

实操上，Train Pool 每轮替换为新生成指令，Cache Pool 持续累积用于 hard-mining；这把单向 API distillation 改成 student-aware curriculum。

## 谱系位置

- 上游：Alpaca / Vicuna (2023) — 都是 teacher 一次性生成 instruction data，缺少 student-aware feedback loop
- 同期：black-box KD / instruction tuning — Lion 的区别是用同一个 API teacher 生成、评判并扩展 hard instructions
- 下游：GAD (Ye 2025) — 同属 black-box / API-constrained distillation，但把 verbal referee 换成 adversarial discriminator reward
- 下游：OVD (Xiong 2026) — 延续 API-only verbal/score supervision，用环境或 teacher scores 做 trajectory matching

## 优缺点

- ✅ [作者 ack §Abstract / §3.1-3.3]: 无需 teacher logits、hidden states 或梯度，只靠 API 输出和自然语言评分即可形成 imitation-discrimination-generation 闭环
- ✅ [song-2026 §5.2]: verbal feedback curriculum 能针对 student weakness 生成更难指令，逐步缩小 teacher-student gap
- ⚠️ [song-2026 §5.2]: 监督信号来自自然语言 critique / score，换取 API compatibility 的同时牺牲 white-box distributional fidelity
- ⚠️ [作者 ack §3.3]: hard instruction 依赖 referee score gap 和阈值，质量受 teacher-as-judge 的一致性影响

## headline number

- Lion-13B 在 Vicuna-Instructions 上达到 ChatGPT 平均表现的 98.38%（§Table 1）

<!-- pdf: §Abstract / §3.1 Initialization / §3.2 Imitation Stage / §3.3 Discrimination Stage / §5.1 Table 1 -->
<!-- song-2026: Table 1 / Table 2 / §5.2 Black-Box and API-Constrained Distillation -->
