# 33篇未确认主会录用论文：首次发布与公开投稿状态

核查日期：2026-10-16。对象是现有36篇中未命中2026主会accepted索引的33篇；3篇已确认主会Poster不计入本表。

## 可以回答什么

【事实】33/33已从arXiv submission history提取v1时间。**20/33在9–10月首次提交arXiv，26/33在8月以后首次提交**；最早2026-05-02，最晚2026-10-09。这里“首次发布日期”采用arXiv v1提交日期（UTC），不等于arXiv正式公告日，更不等于会议投稿日；不从arXiv ID月份反推日期。One Student, Many Teachers的ID为2607.18293，v1时间却为6月30日，统计按v1原始时间。

【事实】公开OpenReview元数据检索得到：**18篇ICLR 2027 Conference Submission、1篇ACL ARR 2026 October Submission、2篇ICLR 2027 Desk Rejected Submission、2篇workshop记录、10篇会议状态未核实。** 未发现本轮可确认的外审Reject记录，不等于证明历史上从未被拒。

【解释】这批论文中多数有下一轮投稿待结果的公开证据。不能拿“未被2026主会索引收录”作为投稿失败率，也不能把33篇归为同一种原因。

## 首次提交arXiv的月份

| 月份 | 篇数 |
|---|---:|
| 2026-05 | 2 |
| 2026-06 | 3 |
| 2026-07 | 2 |
| 2026-08 | 6 |
| 2026-09 | 13 |
| 2026-10 | 7 |

## 当前公开状态

| 类别 | 篇数 | 可以支持的结论 |
|---|---:|---|
| ICLR 2027 Conference Submission | 18 | 已有该轮投稿记录；尚未取得录用结果，不把Submission直接当作进入外审的证明 |
| ACL ARR 2026 October Submission | 1 | 已有ARR投稿记录；ARR是评审通道，不能直接称为ACL主会录用 |
| ICLR 2027 Desk Rejected Submission | 2 | Uni-OPD、Rethinking Self-Distillation for Multi-Teacher Capability Merging；确有desk rejection标记，原因未知，不能等同外审后的科学质量否定 |
| Workshop记录 | 2 | MOPD：ICML 2026 RLxF Workshop；ACLArena：CL4FMAgents @ NeurIPS 2026。本轮没有核对最终decision，不能升级为主会录用 |
| 会议状态未核实 | 10 | 其中Every Coin Has Two Sides的arXiv标注Under Review，但未确认会议；technical report也不一定以会议录用为目标 |

## 与会议时间线的关系

- [ICLR 2027官方Reviewer Guide](https://iclr.cc/Conferences/2027/ReviewerGuidelines)：首轮评审计划11月5日释出，作者讨论11月5–18日，reviewer最终推荐截止11月25日。截至本次核查10月16日尚未到计划释出时间；没有取得公开评分，不据此对18篇投稿作录用预测。评分公开后可以作为录用前景证据，但不替代最终decision。
- [ICML 2026官方CFP](https://icml.cc/Conferences/2026/CallForPapers)：全文截止2026-01-28。
- [NeurIPS 2026官方CFP](https://neurips.cc/Conferences/2026/CallForPapers)：摘要截止05-04、全文截止05-06、通知09-24。
- [EMNLP 2026官方CFP](https://2026.emnlp.org/calls/main_conference_papers/)：最晚ARR cycle截止05-25、commitment截止08-02、通知08-20。

【事实】31/33的arXiv v1时间晚于5月25日；2篇5月首发的是MAD-OPD（5月2日）和Uni-OPD（5月5日）。

【判断边界】这些时间说明公开发布集中在本年度主要投稿窗口之后，**不能证明论文没有提前匿名投稿，也不能证明它们被拒后才公开**。本项目已有反例：H-OPD在7月提交arXiv却被EMNLP 2026主会收录。是否投过/被拒，须追到具体投稿与decision。ICLR 2027投稿记录也不排除更早的其他会议投稿史。

## 逐篇日期与状态

日期来自arXiv v1（UTC）。状态来自公开OpenReview search API的`venue`/`venueid`；匿名记录按规范化完整标题匹配，不推断作者身份。API原始命中与source URL已保存，只持久化本项目相关条目。

| 首次arXiv日期 | 论文 | 当前公开状态 | 来源 |
|---|---|---|---|
| 2026-05-02 | MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2605.01347)；[OpenReview](https://openreview.net/forum?id=vTPKOmuzFp) |
| 2026-05-05 | Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe | ICLR 2027：Desk Rejected Submission；原因未核实 | [arXiv](https://arxiv.org/abs/2605.03677)；[OpenReview](https://openreview.net/forum?id=ck9F16zS9F) |
| 2026-06-25 | Qwen-Image-2.0-RL Technical Report | 会议投稿/结果未核实；technical report | [arXiv](https://arxiv.org/abs/2606.27608) |
| 2026-06-29 | MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training | 有workshop记录：ICML 2026 RLxF Workshop；本轮未独立核对decision | [arXiv](https://arxiv.org/abs/2606.30406)；[OpenReview](https://openreview.net/forum?id=Ir65sQ5tV6) |
| 2026-06-30 | One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context | ACL ARR 2026 October：Submission | [arXiv](https://arxiv.org/abs/2607.18293)；[OpenReview](https://openreview.net/forum?id=bRuZJRVJx3) |
| 2026-07-08 | When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2607.07050)；[OpenReview](https://openreview.net/forum?id=OgxhRCb2g3) |
| 2026-07-30 | Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2607.27770) |
| 2026-08-04 | SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2608.03092) |
| 2026-08-17 | Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models | 会议投稿/结果未核实；作者arXiv标注Under Review | [arXiv](https://arxiv.org/abs/2608.16647) |
| 2026-08-19 | Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2608.19098)；[OpenReview](https://openreview.net/forum?id=acOWuxDgZs) |
| 2026-08-25 | D³-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2608.24987) |
| 2026-08-27 | Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2608.27409)；[OpenReview](https://openreview.net/forum?id=AoBpLhdXID) |
| 2026-08-27 | Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2608.26735)；[OpenReview](https://openreview.net/forum?id=dQbHXq138L) |
| 2026-09-02 | Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2609.02548) |
| 2026-09-02 | Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.02998)；[OpenReview](https://openreview.net/forum?id=9uQm8TP4zN) |
| 2026-09-03 | Rethinking On-Policy Distillation of Large Language Models II: One Training Example | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2609.04172) |
| 2026-09-08 | Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding | 会议投稿/结果未核实；technical report | [arXiv](https://arxiv.org/abs/2609.09300) |
| 2026-09-12 | Data-Free On-Policy Distillation: How Far Can We Go Without External Data? | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.14193)；[OpenReview](https://openreview.net/forum?id=OyPHHYZnia) |
| 2026-09-14 | Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.15404)；[OpenReview](https://openreview.net/forum?id=dP8uHxOdEG) |
| 2026-09-20 | Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.23697)；[OpenReview](https://openreview.net/forum?id=7OM4vVAkEd) |
| 2026-09-21 | ACLArena: Agent Continual Learning in Multi-stage Post-training | 有workshop记录：CL4FMAgents @ NeurIPS 2026；本轮未独立核对decision | [arXiv](https://arxiv.org/abs/2609.23989)；[OpenReview](https://openreview.net/forum?id=PHAPWKhHml) |
| 2026-09-25 | MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.30837)；[OpenReview](https://openreview.net/forum?id=7Ajj2iy7yC) |
| 2026-09-28 | Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.35347)；[OpenReview](https://openreview.net/forum?id=IJKUVDoKy1) |
| 2026-09-28 | No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.34745)；[OpenReview](https://openreview.net/forum?id=VNjcy5xYcF) |
| 2026-09-28 | PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.34605)；[OpenReview](https://openreview.net/forum?id=Th9EmakZ47) |
| 2026-09-29 | Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2609.38666)；[OpenReview](https://openreview.net/forum?id=QzAdsHLXcH) |
| 2026-10-01 | From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2610.02179)；[OpenReview](https://openreview.net/forum?id=kqCLUujaMh) |
| 2026-10-01 | Latent-MOPD: Latent Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2610.02381)；[OpenReview](https://openreview.net/forum?id=YGDYGf6pa2) |
| 2026-10-01 | Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2610.02324) |
| 2026-10-03 | Rethinking Self-Distillation for Multi-Teacher Capability Merging | ICLR 2027：Desk Rejected Submission；原因未核实 | [arXiv](https://arxiv.org/abs/2610.04272)；[OpenReview](https://openreview.net/forum?id=YzYnYsf1PF) |
| 2026-10-06 | UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2610.08398)；[OpenReview](https://openreview.net/forum?id=LZxfSX1Oqu) |
| 2026-10-07 | Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts | 会议投稿/结果未核实 | [arXiv](https://arxiv.org/abs/2610.10460) |
| 2026-10-09 | Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation | ICLR 2027：公开列为Submission，尚无录用结果 | [arXiv](https://arxiv.org/abs/2610.13521)；[OpenReview](https://openreview.net/forum?id=q5NpkqNLNY) |

## 证据与验证

- [arXiv v1提取记录](../notes/conference-index-2026/arxiv-first-release.json)：33篇、版本时间和Comments。
- [公开投稿检索记录](../notes/conference-index-2026/submission-status-search.json)：MOPD及少量专名检索，再对未命中论文逐项做完整标题短语检索；21次查询均成功返回。未命中不是未投稿证明，改名或非公开投稿仍可能漏检。
- [合并结果](../notes/conference-index-2026/release-and-submission-summary.json)：每篇日期、状态与原始forum/source链接。
- 官方forum网页部分触发浏览器验证或不可读；状态来自可访问的官方公开search API，不声称读到了decision全文。Workshop的venue元数据仅按记录报告，不额外猜测录用。
- 验证：33个唯一arXiv ID、33个v1时间、月份总数33、状态总数33（18+1+2+2+10），全部PASS。未修改36篇论文页。
