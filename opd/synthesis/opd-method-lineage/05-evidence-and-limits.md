# 05. Evidence Used 与边界

> 本卷记录本报告依赖的证据、未读内容和后续需要升级为 L2 deep note 的位置。

## 证据来源

本报告默认使用以下本地证据：

- [`_meta/generated/research-map.md`](../../_meta/generated/research-map.md)：71 张核心卡的 decision index、axis counts、failure-mode counts、candidate tensions。
- [`_meta/generated/idea-context.md`](../../_meta/generated/idea-context.md)：high-signal tensions and compact paper context，用于避免拼接全部 L1 cards。
- [`_meta/generated/card-validation.md`](../../_meta/generated/card-validation.md)：当前 validation issues 为 0。
- L1 cards in [`notes/`](../../notes/)：每张卡带 source anchors，作为本报告的主证据。
- bounded paper briefs in [`_meta/briefs/papers/`](../../_meta/briefs/papers/)：仅在 L1 card 对机制判断不足时作为补充；本轮没有新增 full-PDF 精读。

## 关键 evidence anchors

开山线：

- [`notes/24_gkd.md`](../../notes/24_gkd.md)：OPD as imitation learning, student rollout, divergence-agnostic setup；anchors `pdf §3.1`, `song-2026 §2.3`。
- [`notes/24_minillm.md`](../../notes/24_minillm.md)：sequence-level reverse-KL / policy-gradient OPD；anchors `pdf §2.1-2.2`, `song-2026 §4.1`。
- [`notes/24_distillm.md`](../../notes/24_distillm.md)：skew-KL、KLD gradient explosion、replay buffer、SGO cost；anchors `pdf §2.2`, `§3.1`, `Fig 2`。

Objective / routing：

- [`notes/25_distillm-2.md`](../../notes/25_distillm-2.md)：source-level SKL/SRKL routing。
- [`notes/25_taid.md`](../../notes/25_taid.md)：target-level curriculum / interpolated teacher。
- [`notes/26_eopd.md`](../../notes/26_eopd.md)：teacher-entropy gated adaptive divergence。

Teacher reliability / flawed prefix：

- [`notes/26_revisiting-opd.md`](../../notes/26_revisiting-opd.md)：sampled-token OPD failure modes, support matching, special-token masking。
- [`notes/26_rethinking-opd-llm.md`](../../notes/26_rethinking-opd-llm.md)：thinking-pattern compatibility and new capability conditions。
- [`notes/26_rock-tokens.md`](../../notes/26_rock-tokens.md)：persistent high-loss low-utility tokens。
- [`notes/26_prune-opd.md`](../../notes/26_prune-opd.md)：top-k overlap drift detection and dynamic pruning。
- [`notes/26_trust-region-opd.md`](../../notes/26_trust-region-opd.md)：trust region and outlier handling。
- [`notes/26_kl-agreement-trap.md`](../../notes/26_kl-agreement-trap.md)：low-KL agreement can be a trap。

Granularity / credit：

- [`notes/26_tip.md`](../../notes/26_tip.md)：token entropy + divergence selection。
- [`notes/26_scope.md`](../../notes/26_scope.md)：trajectory correctness dual-path routing。
- [`notes/26_sod.md`](../../notes/26_sod.md)：step-wise OPD for tool-integrated reasoning。
- [`notes/26_near-future-guidance.md`](../../notes/26_near-future-guidance.md)：near-future trajectory consequence。
- [`notes/26_trajectory-refined-distillation.md`](../../notes/26_trajectory-refined-distillation.md)：trajectory-level refinement before distillation。
- [`notes/26_segment-level-opd.md`](../../notes/26_segment-level-opd.md)：agent segment local reward vs return alignment。

Privilege / multi-rollout：

- [`notes/26_opsd.md`](../../notes/26_opsd.md)：ground-truth-conditioned same-model teacher。
- [`notes/26_hdpo.md`](../../notes/26_hdpo.md)：privileged self-distillation for GRPO cliff prompts。
- [`notes/26_pbsd.md`](../../notes/26_pbsd.md)：Bayesian turn-level credit from privilege。
- [`notes/26_many-faces-opd.md`](../../notes/26_many-faces-opd.md)：PI internalization boundary。
- [`notes/26_multi-rollout-peer.md`](../../notes/26_multi-rollout-peer.md)：peer success/failure context。
- [`notes/26_ssopd.md`](../../notes/26_ssopd.md)：correct-wrong group process supervision。

Signal interface：

- [`notes/26_oprd.md`](../../notes/26_oprd.md)：representation-level OPD and output-space variance claim。
- [`notes/26_ropd.md`](../../notes/26_ropd.md)：rubric-based black-box OPD。
- [`notes/25_bopd.md`](../../notes/25_bopd.md)：dynamic discriminator black-box OPD。
- [`notes/26_simct.md`](../../notes/26_simct.md)：cross-tokenizer continuation units。

Geometry / extrapolation：

- [`notes/26_states-not-tokens.md`](../../notes/26_states-not-tokens.md)：state distribution view。
- [`notes/26_geometry-opd.md`](../../notes/26_geometry-opd.md)：parameter geometry / subspace locking。
- [`notes/26_dense-supervision-sparse-updates.md`](../../notes/26_dense-supervision-sparse-updates.md)：dense supervision, sparse updates。
- [`notes/26_effopd.md`](../../notes/26_effopd.md)：validation-gated parameter extrapolation。
- [`notes/26_g-opd-reward-extrapolation.md`](../../notes/26_g-opd-reward-extrapolation.md)：generalized OPD and reward extrapolation。
- [`notes/26_extrapolation-cliff.md`](../../notes/26_extrapolation-cliff.md)：structured-output extrapolation cliff。

## 本轮没有做什么

没有重新读完整 survey 或完整 PDF。原因是当前报告目标是 source-backed synthesis，不是 L2 deep review；L1 cards 已经承担单篇入口，bounded briefs 承担必要补证据。

没有对 68 篇候选全部抽卡。当前 triage 为 `select=0`，多数是 novelty-risk / application-branch / low-evidence-direct 候选。只有在具体 idea 触及对应 failure mode 时才升级读取。

没有更新 citation、acceptance status、GitHub stars 或最新引用数。这些是时间敏感信息；正式投稿相关判断前需要单独检索。

## 当前报告的缺陷

1. 机制线覆盖较完整，但很多 2026 论文仍是 arXiv / OpenReview 候选，可信度低于 GKD/MiniLLM/DistiLLM/TAID/OPSD 等 anchor。
2. “teacher reliability” 目前是跨论文解释，不是一个已有统一理论。报告把它作为 synthesis 主线，但这仍然需要实验验证。
3. Geometry / parameter-subspace 分支主要来自 post-hoc analysis，尚未和 trust controller 或 granularity routing 完整闭环。
4. Black-box/API teacher 分支复现链条弱，尤其依赖 LLM judge 或闭源 teacher 时，只能作为 novelty-risk 和应用方向，不宜作为强方法证据。
5. 报告没有逐篇列出所有 71 张 cards；这是有意取舍。需要查单篇细节时回到 L1 card。

## 什么时候需要 L2 deep note

当你准备把某个 hook 写成正式 idea 或 paper proposal 时，至少对 direct competitors 做 L2 deep note。建议：

- Trust controller：Revisiting OPD、TrOPD、Prune-OPD、KAT、Near-Future。
- Distillability predictor：Rethinking OPD、TAID、Capacity Gap Rethinking、PACED、Geometry OPD。
- Multi-granularity routing：TIP、SCOPE、SOD、Segment-Level、TRD。
- Privilege benchmark：OPSD、HDPO、PBSD、Many Faces。
- Representation-assisted trust：OPRD、SimCT、TrOPD。
- Reward extrapolation：G-OPD、Extrapolation Cliff、OPD+。

L2 deep note 必须记录：完整方法公式、实验设置、main tables、ablation、limitations、代码/复现状态、与拟议 idea 的 direct overlap。
