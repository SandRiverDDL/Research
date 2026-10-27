# MOPD 已收集论文的公开录用状态

更新：2026-10-16。范围：现有36篇论文；使用五场会议官方索引快照复核，替代此前网页检索的初步统计。

## 结论

**已确认3篇主会Poster：AVSD（NeurIPS 2026）、H-OPD（EMNLP 2026）、CaMOPD（EMNLP 2026）。其余33篇尚未确认录用。**

- AVSD：NeurIPS官方JSON的Conference记录，decision为Accept (poster)，OpenReview ID `fRtcETLCZ2`；完整标题匹配且9位本地作者一致。[官方记录](https://openreview.net/forum?id=fRtcETLCZ2)
- H-OPD：EMNLP官方日程`572-MAIN`、Poster，完整标题匹配；确认主会，补足此前仅有arXiv作者标注的证据。
- CaMOPD：EMNLP官方日程`6445-MAIN`、Poster，完整标题匹配；上一轮漏查此日程数据，此次新增确认。

EMNLP一手来源：[官方日程CSV](https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/export?format=csv&gid=943432490)。`MAIN`与`FIND`分别保存，不能混算。

## 33篇未确认主会录用论文的后续状态复核

2026-10-16新增核查：18篇ICLR 2027 Submission、1篇ARR 2026 October Submission、2篇ICLR 2027 Desk Rejected Submission、2篇workshop记录、10篇会议状态未核实。20/33首次提交arXiv在9–10月；不能把未命中2026主会索引当作被拒。逐篇日期、来源和边界见[发布日期与投稿状态报告](mopd-release-and-submission-status.md)。这不改变前述3篇主会Poster的索引结果。

## 索引与身份匹配

[下载与覆盖说明](../notes/conference-index-2026/README.md)：ICLR 5,575、ICML 6,563、NeurIPS 6,070、ACL 4,459、EMNLP 5,611，共28,278条去重记录；包含明确标注的特殊track/Findings，不包含workshop合集。

已保存10份官方原始metadata和来源哈希。索引生成、去重、36篇输入覆盖及来源哈希检查PASS；没有修改共享索引脚本、旧缓存或36篇论文页。

完整标题先规范化匹配；可用的官方arXiv标识符单独匹配；标题近似和作者交集只用于候选召回，不能直接宣布录用。结果见[匹配数据](../notes/conference-index-2026/mopd-matches.json)。本轮没有确认额外的改名录用。

代表性误匹配已核对：TrustMOPD与SimCT共享7位作者，但分别解决多teacher可靠性分配和cross-tokenizer监督；IM-MOPD与Mixture-Trained Merging共享4位作者，但训练机制不同。Video-MOPD与MosaicAudio标题相近，任务分别是视频理解和video-to-audio生成，也不能直接当作同一论文。

限制：EMNLP日程没有作者/摘要；部分官方JSON记录缺摘要。每篇保留最多3个近似/作者候选，未对33篇逐一穷尽所有改名版本或作者发表历史。4个定向OpenReview notes API请求返回403；候选判断采用官方索引摘要，EffOPD条目另外复用两天前的官方摘要缓存。未知不等于未录用/被拒。

## 逐篇状态

| 论文 | arXiv | 索引复核结果 | 一手入口 |
|---|---|---|---|
| Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation | 2605.27115 | EMNLP 2026 主会 Poster | [6445-MAIN](https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/export?format=csv&gid=943432490) |
| Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives | 2609.38666 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.38666) |
| Latent-MOPD: Latent Multi-Teacher On-Policy Distillation | 2610.02381 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.02381) |
| Rethinking On-Policy Distillation of Large Language Models II: One Training Example | 2609.04172 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.04172) |
| Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation | 2608.19098 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2608.19098) |
| Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs | 2609.02548 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.02548) |
| Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe | 2605.03677 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2605.03677) |
| No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation | 2609.34745 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.34745) |
| Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation | 2609.35347 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.35347) |
| Data-Free On-Policy Distillation: How Far Can We Go Without External Data? | 2609.14193 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.14193) |
| Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models | 2608.16647 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2608.16647) |
| PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation | 2609.34605 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.34605) |
| Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation | 2608.26735 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2608.26735) |
| Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold | 2607.27770 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2607.27770) |
| MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training | 2606.30406 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2606.30406) |
| One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context | 2607.18293 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2607.18293) |
| AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals | 2605.20643 | NEURIPS 2026 主会 Poster | [fRtcETLCZ2](https://openreview.net/forum?id=fRtcETLCZ2) |
| Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding | 2609.09300 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.09300) |
| Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts | 2610.10460 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.10460) |
| When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation | 2607.07050 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2607.07050) |
| Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation | 2609.23697 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.23697) |
| D³-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation | 2608.24987 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2608.24987) |
| Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation | 2610.13521 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.13521) |
| ACLArena: Agent Continual Learning in Multi-stage Post-training | 2609.23989 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.23989) |
| MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate | 2605.01347 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2605.01347) |
| SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation | 2608.03092 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2608.03092) |
| Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms | 2608.27409 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2608.27409) |
| Rethinking Self-Distillation for Multi-Teacher Capability Merging | 2610.04272 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.04272) |
| MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation | 2609.30837 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.30837) |
| Qwen-Image-2.0-RL Technical Report | 2606.27608 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2606.27608) |
| Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning | 2609.15404 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.15404) |
| H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation | 2607.02592 | EMNLP 2026 主会 Poster | [572-MAIN](https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/export?format=csv&gid=943432490) |
| Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation | 2610.02324 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.02324) |
| Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation | 2609.02998 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2609.02998) |
| From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation | 2610.02179 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.02179) |
| UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation | 2610.08398 | 尚未确认录用；改名可能性未完全排除 | [arXiv](https://arxiv.org/abs/2610.08398) |
