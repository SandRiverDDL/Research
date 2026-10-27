---
title: "SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation"
authors: [Jie Sun, et al.]
org: other
year: 2026
venue: neurips-2026
arxiv_id: 2605.07711
url: https://arxiv.org/abs/2605.07711

confidence: 4
open_source: yes
verified: a

surveys:
  song-2026: "§4.3 cross-tokenizer OPD; Table 8"

addresses:
  - cross-tokenizer
  - special-token-mismatch

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：cross-tokenizer OPD 的 continuation-unit 对齐路线。

## 核心做法

SimCT 指出 cross-tokenizer OPD 的 exact shared-token matching 会在 tokenizer 分歧最大的位置静默丢掉 teacher signal；它把 supervision space 从共享单 token 扩展到 teacher/student 都能实现的短 multi-token continuation units，在不改变 OPD loss 形式的前提下恢复被丢弃的监督。

$$\mathcal{U}(h)=\{\text{short continuations realizable by both tokenizers}\}$$

实操含义：不强行 transport 概率或投影 representation，而是选择最细的 jointly tokenizable interface，让异构 tokenizer 的 teacher/student 仍可比较局部 continuation。

## 谱系位置

- 上游：DSKD / ULD — 这些方法处理 cross-tokenizer supervision loss；SimCT 从 OPD loss 内部扩大匹配单元。
- 同期：Revisiting OPD (2026) — special-token/tokenizer mismatch 是 sampled-token OPD 的 failure mode；SimCT 给出 cross-tokenizer 场景的具体修复。
- 下游：architecture-agnostic OPD — 支持 Qwen/Phi/Gemma 等异构 teacher-student pair。

## 优缺点

- ✅ [song-2026 §4.3]: 多 token continuation units 恢复 exact shared-token matching 丢掉的 teacher signal。
- ✅ [作者 ack Abstract]: 三组 heterogeneous teacher-student pair 上优于 shared-vocabulary OPD 和 cross-tokenizer baselines。
- ⚠️ [song-2026 §4.3]: 仍在离散 continuation interface 内工作，对更彻底的 latent/cross-modal mismatch 不能直接解决。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §4.3 Cross-Tokenizer OPD / Table 8 -->

<!-- venue verified 2026-10-04: https://neurips.cc/Downloads/2026 ; official entry: https://neurips.cc/virtual/2026/poster/153233 -->
