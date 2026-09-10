---
title: "SPIN: Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models"
authors: [Zixiang Chen, et al.]
org: ucla
year: 2024
venue: icml-2024
arxiv_id: 2401.01335
url: https://arxiv.org/abs/2401.01335

confidence: 3
open_source: yes
verified: s

surveys:
  song-2026: "§5.3 Self-distillation boundary; §9 game-theoretic self-play"

addresses:
  - teacher-staleness

decisions:
  rollout: student
  loss: preference
  signal: preference
  iteration: iterative
  filter: none
  extra: none
---

> **一句话**：OPD 邻近的自博弈对齐代表作。

## 核心做法

把上一轮模型采样的回复当 rejected，把 SFT 数据回复当 chosen，用 DPO 形式的 logistic loss 反复训练新 checkpoint；固定点是模型分布对齐到人类示范数据分布。

$$\ell\!\left(\lambda\log\frac{p_\theta(y|x)}{p_{\theta_t}(y|x)}-\lambda\log\frac{p_\theta(y'|x)}{p_{\theta_t}(y'|x)}\right)$$

实操上，每轮先由旧模型生成负例，再训练新模型区分旧模型输出与 SFT reference；它不需要额外偏好数据、reward model 或更强 teacher。

## 谱系位置

- 上游：DPO (2023) — SPIN 复用 preference loss 形式，但自动构造 chosen/rejected
- 同期：ReST (2023) — 同样减少人工反馈依赖，但 ReST 需要 binary feedback 或 reward model
- 下游：IRIS (2026) — survey 称其用 interpolative Renyi divergence 统一若干 self-play 变体

## 优缺点

- ✅ [作者 ack §4.1]：chosen/rejected 由 SFT 数据与上一轮自采样自动构造，不依赖额外人类或 GPT-4 偏好数据
- ✅ [song-2026 §9]：Nash-equilibrium 目标提供了不同于 OPD 分布对齐的稳定化视角
- ⚠️ [song-2026 §5.3]：survey 明确把 SPIN 排除在 OPD self-distillation scope 外，核心是 successive checkpoints 的 adversarial competition
- ⚠️ [作者 ack §7]：固定 target data distribution 会给性能上限，作者将动态 target distribution 列为未来方向

<!-- pdf: §1 Introduction / §4 Method / §7 Conclusion and Discussion -->
<!-- song-2026: §5.3 Self-distillation / §9 Conclusion -->
