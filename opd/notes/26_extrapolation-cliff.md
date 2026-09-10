---
title: "The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs"
authors: [Xin Li, et al.]
org: ntu
year: 2026
venue: arxiv
arxiv_id: 2605.08737
url: https://arxiv.org/abs/2605.08737

confidence: 4
verified: a

surveys:
  song-2026: "References; OPD method coverage audit"

addresses:
  - structured-output-cliff
  - reward-hacking
  - large-policy-divergence

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：OPD 奖励外推的结构化输出边界。

## 核心做法

论文研究 λ>1 reward extrapolation 在 near-deterministic structured output 上的安全边界：外推能让 student in-domain 超过 teacher，但超过闭式阈值 λ* 后，训练会从 format-preserving 变成 format-collapsing。阈值由 teacher modal probability、warm-start mass 和 importance-sampling clip strength 决定。

$$\lambda^\star=\lambda^\star(p,b,c)$$

实操含义：对 JSON / function-call / listwise ranking 这类输出，OPD 外推不能只看任务分数；必须单独守住 parse validity / contract adherence。

## 机制发现（可选）

- [作者 ack Abstract / §4]: 单位置 Bernoulli reduction 给出 base-relative clip-safety threshold，λ 超过阈值时 fixed point 离开 clip-safe region。
- [作者 ack §5.1]: Amazon Fashion 的 fine-grid cliff interval、budget-extension test 和 small-clip cross-prediction 都落在预注册预测窗口内。
- [作者 ack Abstract / §5]: parsed outputs 上的 ranking quality 对 λ 基本平坦，性能变化主要来自 parse validity / format adherence。
- [作者 ack Appendix F / G]: scope checks 覆盖 JSONSchemaBench、MBPP、BFCL、GSM8K 等，但 sharp cliff 依赖 near-deterministic outer scaffold 和 dominant binding class。

## 谱系位置

- 上游：G-OPD / ExOPD (2026) — 继承 λ>1 reward extrapolation 的收益命题，但指出其结构化输出安全边界。
- 同期：OPD+ (2026) — OPD+ 修正 advantage 设计；本文给出外推系数在 structured-output 上的 deployment rule。
- 同期：ASPO / entropy-aware objectives — 作者报告同机制修复仍保留 cliff，说明问题不是单个实现细节。

## 优缺点

- ✅ [作者 ack §4 / §5]: 将“外推过头会坏格式”变成可测量的闭式阈值和预注册验证，而不是经验调参。
- ✅ [作者 ack Abstract / §5]: 区分了 rank quality 与 parse validity，避免把格式崩塌误读为语义排序能力下降。
- ⚠️ [作者 ack Appendix F]: sharp cliff 主要适用于 near-deterministic structured outputs；开放式 reasoning 是否有同样清晰阈值不能直接外推。

## headline number

- Qwen3 1.7B reaches in-domain parity with an 8B-SFT baseline at one-fifth parameters when operating below λ*（§Fig 1 / §5）

<!-- pdf: arXiv HTML v1 Abstract / §3.2 / §4 / §5 / Appendix F / Appendix G -->
<!-- song-2026: References / survey-reference-audit -->
