---
title: "Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes"
authors: [Yuqian Fu, et al.]
org: casia
year: 2026
venue: arxiv
arxiv_id: 2603.25562
url: https://arxiv.org/abs/2603.25562

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "§6.1 token and sample weighting; Table 9; References"

addresses:
  - sampled-token-imbalance
  - flawed-prefix-trap
  - special-token-mismatch

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：sampled-token OPD 的机制诊断与修复基线。

## 核心做法

论文先把 token-level OPD 的 bias-variance tradeoff 说清楚：相对 sequence-level reverse-KL，token-level estimator 有 bias，但能切断 future-reward coupling、降低长序列方差；随后指出当前 sampled-token 实现把监督退化成单 token log-ratio，长 rollout 中容易失真。修复方案是 teacher top-K local support matching：只在 teacher 支持集内做截断 reverse-KL，并配合 top-p rollout sampling 与 special-token masking。

$$\mathcal{L}_{\mathrm{local}}=\sum_{v\in\mathrm{TopK}(p_T)}\bar p_T(v)\log\frac{\bar p_T(v)}{\bar p_\theta(v)}$$

实操含义：保留 token-level OPD 的低方差优势，但不再让单个 sampled token 或 special-token 边界决定整步更新方向。

## 机制发现（可选）

- [作者 ack §2 / Appendix D]: token-level OPD 相对 sequence-level reverse-KL 有 bias，但 worst-case variance 更紧；future-reward coupling 越强，梯度方差越大、训练越不稳。
- [作者 ack §2.2 Fig.2]: sampled-token signal 高度不平衡，多数 token 得到负 reward，少数局部正 token 容易主导更新。
- [作者 ack §2.2 Fig.3 / Appendix H]: student prefix 漂到 teacher 低支持区域后，teacher 对重复、自我重置等无意义 continuation 仍可能局部对齐，导致 flawed-prefix trap。
- [作者 ack §2.2]: tokenizer 或 special-token mismatch 会把同一 raw text 切成不同 token，sampled-token log-prob 比较被实现细节扭曲。

## 谱系位置

- 上游：MiniLLM / sampled-token OPD (2024-2025) — 继承 token-level reverse-KL / log-ratio 路线，但系统诊断其长程脆弱性。
- 同期：TIP (2026) — TIP 做 token importance selection；Revisiting OPD 关注 sampled-token estimator 本身的 support mismatch。
- 同期：Trust Region OPD (2026) — 同样怀疑 teacher 在大分布差距下不可靠；Revisiting OPD 选择 local teacher support set 截断。
- 下游：后续 sampled-token / top-k OPD 方法 — 应把 top-K support、top-p rollout 和 special-token masking 当作 baseline hygiene，而非可选 trick。

## 优缺点

- ✅ [作者 ack §2-3]: 同时给出理论 tradeoff、empirical failure modes 和实现级修复，信息量高于单纯方法改进。
- ✅ [song-2026 §6.1]: 综述将其列为 sampled-token OPD 脆弱性的系统 failure-mode analysis，并记录 19.8% gain。
- ⚠️ [作者 ack Appendix A]: support-set KL 是 truncated objective，teacher matching 仍只是 task success 的 proxy，不能替代 outcome-level verification。

## headline number

无 Table/Fig anchor 的 abstract 级数字不放入 headline number；19.8% gain 仅在上方作为 survey/abstract 证据记录。

<!-- pdf: arXiv HTML v2 Abstract / §2 / §3 / §4 / Appendix A-D / Appendix H -->
<!-- song-2026: §6.1 Token and Sample Weighting / Table 9 / References -->
