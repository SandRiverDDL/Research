---
title: "Cornerstones or Stumbling Blocks? Deciphering the Rock Tokens in On-Policy Distillation"
authors: [Yuxuan Jiang, et al.]
org: umbc-case-asu-vu
year: 2026
venue: arxiv
arxiv_id: 2605.09253
url: https://arxiv.org/abs/2605.09253

confidence: 4
open_source: yes
verified: a

surveys:
  song-2026: "References; OPD method coverage audit"

addresses:
  - low-utility-token-supervision
  - coarse-credit-assignment
  - sgo-generation-cost

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: score-threshold
  extra: none
---

> **一句话**：OPD 高损失 token 的低效监督诊断。

## 核心做法

论文把 OPD 中持续高 loss、训练后仍不收敛的 token 定义为 Rock Tokens：它们标记 student-teacher mismatch，但 causal knockout 显示其中大量 token 对实际 reasoning 功能贡献很低。作者用 context-consistent high-loss 检测找到这些 token，再用 window-aware token reweighting / freeze 跳过低贡献区域。

$$\mathrm{RockScore}(v)=\sum_{(x,t):y_t=v}\mathbf{1}[\ell_t\ \text{persistently high}]$$

实操含义：OPD 不是所有 token 都值得等权监督；高 KL / 高梯度范数可能只是优化阻塞点，而不一定是能力瓶颈。

## 机制发现（可选）

- [作者 ack Abstract / §2]: Rock Tokens 在 OPD apparent saturation 后仍保持高 loss，最多可占生成 token 的 18%，同时贡献大量梯度范数但自身不被 teacher signal 修正。
- [作者 ack §3]: Pillar Tokens 很少，且与 Rock Tokens 高度正交；高频率、高 loss 或高 entropy 不能直接等价为“重要 token”。
- [作者 ack §4]: window-aware reweighting/freezing 可以在保持 reasoning performance trajectory 的同时减少无效 token 更新。
- [作者 ack Appendix A]: 实验主要在 math reasoning 和一个 30B-to-4B 设定上，binary gradient-freeze mask 也偏粗糙。

## 谱系位置

- 上游：Revisiting OPD (2026) — Revisiting 诊断 sampled-token imbalance / special-token mismatch；本文进一步问高 loss token 是否真的有功能贡献。
- 同期：Prune-OPD (2026) — Prune-OPD 在 trajectory prefix drift 后截断 suffix；本文在 token/window 层面跳过低贡献监督。
- 同期：EffOPD (2026) — EffOPD 从参数更新方向找冗余；本文从 token loss 动态找冗余。

## 优缺点

- ✅ [作者 ack Abstract / §2-4]: 把“高 loss token = 学习重点”的直觉拆开，提出低贡献高损耗 token 这一类 OPD 特有 failure mode。
- ✅ [作者 ack §4]: 给出可操作的 selective distillation 路线，而不是只做可视化诊断。
- ⚠️ [作者 ack Appendix A]: 结论主要来自 math reasoning 和特定 teacher-student pair，能否迁移到 code / tool / structured-output OPD 需要复查。

## headline number

无一致 Table/Fig anchor 的 speedup 数字不放入 headline number；18% token 占比仅作为机制证据保留。

<!-- pdf: arXiv HTML v2 Abstract / §2 Rock Tokens / §3 Pillar Tokens / §4 Genuine Contribution / Appendix A -->
<!-- song-2026: References / survey-reference-audit -->
