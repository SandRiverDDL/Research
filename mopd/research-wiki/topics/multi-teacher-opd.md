# Multi-Teacher On-Policy Distillation 文献地图

更新：2026-10-15。**36 篇原文定向阅读页：15 篇 seed + 21 篇补搜。**每页含方法、主要结果、假设、局限、开放问题和版本化来源；不代表每篇逐字全文精读。

入口：[跨论文综述与检索边界](../../synthesis/mopd-literature-review.md) · [领域gap综合](../../synthesis/mopd-gap-analysis.md) · [gap状态](../gap_map.md) · [自动索引](../index.md) · [原始 seed](../../synthesis/seed-sources.md)。

## 阅读口径

- 核心：多个可识别 teachers 对 student 自采样 states 提供直接蒸馏信号；RL hybrid、连续 flow states 在对应页面明确标注。
- 邻近：AVSD 的多 privileged views、MT-SDPO 的反馈→EMA target、PromptSD 的共享 backbone soft-prefix teachers，以及 MAD-OPD 的 deliberation teachers。它们有直接方法价值，但不等同独立领域 RL experts 整合。
- 对照/证据/理论：公平 fusion 比较、Agent retention、梯度/数值/词表诊断与 sequence-level aggregation theory。
- 表中数字仅是原文的指定设置。recovery/Norm、benchmark平均和cost口径不同，不能横向排序。各数字的表号、样本数和限制见对应论文页。
- 作者/年份均为2026；Venue默认 arXiv preprint，正式接收未核实。H-OPD 的 EMNLP2026仅为作者在arXiv comments中的声明。

## 文献表

### 基础 recipe、预算与调度

| Paper（作者，年份） | Venue | Method | Key Result（限定设置） | 项目关系 | 来源 |
|---|---|---|---|---|---|
| [MOPD](../papers/ma2026_mopd_multiteacher_onpolicy.md)（Ma et al., 2026） | arXiv | Domain-routed reverse-KL | 30B recovery .9373 vs Mix-RL .8818 | 核心 | seed / [原文](https://arxiv.org/html/2606.30406v1) |
| [Open-MOPD](../papers/gao2026_openmopd_diagnosing_fixing.md)（Gao et al., 2026） | arXiv | Token-share/gap/refresh | 3B Total28.05→31.24 | 核心 | seed / [原文](https://arxiv.org/html/2608.19098v1) |
| [DN-MOPD](../papers/li2026_beyond_teacher_assignment.md)（Li et al., 2026） | arXiv | Feedback dispersion normalization | 9B/4B/2B +1.17/+2.24/+2.36pp | 核心 | seed / [原文](https://arxiv.org/html/2609.35347v1) |
| [D³-MOPD](../papers/sun2026_d³mopd_dynamic_domain.md)（Sun et al., 2026） | arXiv | KL-progress prompt scheduling | 35B single-checkpoint recovery .48→.73 | 核心 | 补搜 / [原文](https://arxiv.org/html/2608.24987v2) |
| [Uni-OPD](../papers/hou2026_uniopd_unifying_onpolicy.md)（Hou et al., 2026） | arXiv | Exploration/outcome-consistent recipe | 多teacher4B math47.0→48.5 | 核心 | 补搜 / [原文](https://arxiv.org/html/2605.03677v2) |
| [SMOPD](../papers/wang2026_smopd_multireward_reinforcement.md)（Wang et al., 2026） | arXiv | Reward specialists+arithmetic FKL+RL | 1.5B format8.8%→97.5% | 核心 | 补搜 / [原文](https://arxiv.org/html/2608.03092v2) |

### 监督可靠性、选择与定位

| Paper（作者，年份） | Venue | Method | Key Result（限定设置） | 项目关系 | 来源 |
|---|---|---|---|---|---|
| [TrustMOPD](../papers/sun2026_distill_what_you.md)（Sun et al., 2026） | arXiv | Reference displacement calibration | 3B MultiCap recovery98.0% | 核心 | seed / [原文](https://arxiv.org/html/2609.23697v3) |
| [MOPD-Router](../papers/xu2026_mopdrouter_rethinking_teacher.md)（Xu et al., 2026） | arXiv | Specialization/teaching alignment | 4B unlabeled Overall47.88→53.76 | 核心 | 补搜 / [原文](https://arxiv.org/html/2609.30837v2) |
| [UCMOPD](../papers/liu2026_recovering_general_capabilities.md)（Liu et al., 2026） | arXiv | Dual-temperature+entropy filtering | 4B general53.31→54.43 | 核心 | 补搜 / [原文](https://arxiv.org/html/2608.26735v2) |
| [TGOPD](../papers/zhang2026_verify_before_you.md)（Zhang et al., 2026） | arXiv | Verified prompt gate+GRPO fallback | 4B avg53.40→54.54 | 核心 | 补搜 / [原文](https://arxiv.org/html/2609.02998v2) |
| [VG-OPD](../papers/xu2026_who_teaches_which.md)（Xu et al., 2026） | arXiv | Criterion license+token masks+RL | 8B GPQA-D44.1→47.3 | 核心 | 补搜 / [原文](https://arxiv.org/html/2609.15404v2) |
| [Video-MOPD](../papers/qin2026_videomopd_multiteacher_onpolicy.md)（Qin et al., 2026） | arXiv | Offline reliable-data selection+routing | 8B video Avg63.68→69.12 | 核心 | 补搜 / [原文](https://arxiv.org/html/2609.09300v1) |
| [MT-SDPO](../papers/he2026_learn_from_whoever.md)（He et al., 2026） | arXiv | Verified critiques→privileged EMA | 8B Macro62.47→67.11 | 邻近 | seed / [原文](https://arxiv.org/html/2609.02548v1) |

### 能力保留、更新、初始化与目标

| Paper（作者，年份） | Venue | Method | Key Result（限定设置） | 项目关系 | 来源 |
|---|---|---|---|---|---|
| [CaMOPD](../papers/chen2026_counteractionaware_multiteacher_onpolicy.md)（Chen et al., 2026） | arXiv | Alternating recovery/preservation | 4B general43.78→49.07 | 核心 | seed / [原文](https://arxiv.org/html/2605.27115v2) |
| [PMOPD](../papers/liu2026_pmopd_task_ordering.md)（Liu et al., 2026） | arXiv | Task order/cycles+subspace projection | 7B avg64.43→66.97 | 核心 | seed / [原文](https://arxiv.org/html/2609.34605v1) |
| [Road MOPD](../papers/tian2026_beyond_domainrouted_supervision.md)（Tian et al., 2026） | arXiv | Auxiliary teacher guarding | 4B三域49.76→52.89 | 核心 | seed / [原文](https://arxiv.org/html/2610.13521v1) |
| [UP-MOPD](../papers/zhu2026_upmopd_update_projection.md)（Zhu et al., 2026） | arXiv | Project actual AdamW displacement | 3B avg30.85→32.67；step1.42× | 核心 | seed / [原文](https://arxiv.org/html/2610.08398v1) |
| [IM-MOPD](../papers/kim2026_pain_more_gain.md)（Kim et al., 2026） | arXiv | Validation-triggered task vectors | 4B recovery53.8%→86.9% | 核心 | seed / [原文](https://arxiv.org/html/2609.34745v1) |
| [Latent-MOPD](../papers/fang2026_latentmopd_latent_multiteacher.md)（Fang et al., 2026） | arXiv | Hidden-state alignment+crossfade | 1.5B Norm .90→1.05 | 核心 | seed / [原文](https://arxiv.org/html/2610.02381v1) |
| [SF-MOPD](../papers/yin2026_slowfast_multiteacher_onpolicy.md)（Yin et al., 2026） | arXiv | EMA slow-fast log-prob correction | VL8B all avg65.5→67.7 | 核心 | seed / [原文](https://arxiv.org/html/2610.02324v1) |
| [Δ-MOPD](../papers/sang2026_composing_what_each.md)（Sang et al., 2026） | arXiv | Teacher-minus-precursor logit shifts | 三teacher Math29.39→33.50 | 核心 | seed / [原文](https://arxiv.org/html/2610.10460v1) |

### 问题数据与 teacher 构造

| Paper（作者，年份） | Venue | Method | Key Result（限定设置） | 项目关系 | 来源 |
|---|---|---|---|---|---|
| [DF-OPD](../papers/li2026_datafree_onpolicy_distillation.md)（Li et al., 2026） | arXiv | Teacher-generated question pools | 3B1000 questions recovery98.5% | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2609.14193v4) |
| [One Training Example](../papers/fu2026_rethinking_onpolicy_distillation.md)（Fu et al., 2026） | arXiv | Few queries+fresh student rollouts | 16-shot/domain52.9 vs full52.8 | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2609.04172v1) |
| [Teacher-Union OPD](../papers/lu2026_beyond_best_teacher.md)（Lu et al., 2026） | arXiv | Residual RL experts+union compression | 1.7B best teacher16.37→student16.70 | 核心 | 补搜 / [原文](https://arxiv.org/html/2607.27770v1) |
| [PromptSD](../papers/ma2026_one_student_many.md)（Ma et al., 2026） | arXiv | Learned soft-prefix teachers | 1.7B multi-task target Avg56.2 | 邻近 | 补搜 / [原文](https://arxiv.org/html/2607.18293v1) |

### 多视角、异构模态与协商

| Paper（作者，年份） | Venue | Method | Key Result（限定设置） | 项目关系 | 来源 |
|---|---|---|---|---|---|
| [AVSD](../papers/nguyen2026_avsd_adaptiveview_selfdistillation.md)（Nguyen et al., 2026） | arXiv | Privileged-view consensus/residual | 4B五任务OPSD58.2→59.9 | 邻近 | seed / [原文](https://arxiv.org/html/2605.20643v1) |
| [H-OPD](../papers/yin2026_hopd_confidence_aware.md)（Yin et al., 2026） | 作者报EMNLP2026 | VL/text entropy token mixing | VL2B11任务Avg51.1→53.5 | 核心 | 补搜 / [原文](https://arxiv.org/html/2607.02592v3) |
| [MAD-OPD](../papers/wang2026_madopd_breaking_ceiling.md)（Wang et al., 2026） | arXiv | Debate+confidence-weighted OPD | 4B agent/code Avg25.69/48.12 | 邻近 | 补搜 / [原文](https://arxiv.org/html/2605.01347v1) |
| [Qwen-Image-2.0-RL](../papers/xu2026_qwenimage20rl_technical_report.md)（Xu et al., 2026） | arXiv | Student-trajectory velocity matching | 系统Qwen-Image-Bench55.23→57.84 | 系统 | 补搜 / [原文](https://arxiv.org/html/2606.27608v1) |

### 公平对照、诊断与理论

| Paper（作者，年份） | Venue | Method | Key Result（限定设置） | 项目关系 | 来源 |
|---|---|---|---|---|---|
| [Rethinking Merging](../papers/xie2026_rethinking_selfdistillation_multiteacher.md)（Xie et al., 2026） | arXiv | Tuned SFT/Soft-KD/online comparisons | 8B MIA recovery SFT98.2%/MOPD97.9% | 证据/对照 | seed / [原文](https://arxiv.org/html/2610.04272v1) |
| [Fusion paradigms](../papers/wu2026_consolidating_rlvr_capabilities.md)（Wu et al., 2026） | arXiv | Merge/MixRL/MOPD shared experts | 4B avg63.70/62.26/63.31 | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2608.27409v2) |
| [Gradients→Capabilities](../papers/zhu2026_from_gradients_capabilities.md)（Zhu et al., 2026） | arXiv | Weighting/precision/optimizer audits | Gradient cosine .68→Adam update .96 | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2610.02179v1) |
| [Every Coin](../papers/li2026_every_coin_has.md)（Li et al., 2026） | arXiv | Teacher origin/domain swap diagnostics | 影响跨越训练prompt域 | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2608.16647v2) |
| [Tool-call drift](../papers/shen2026_when_topk_misses.md)（Shen et al., 2026） | arXiv | Top-K decision-support audit | Over-call14.20%→3.73%；recall也降 | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2607.07050v6) |
| [ACLArena](../papers/wang2026_aclarena_agent_continual.md)（Wang et al., 2026） | arXiv | Continual Agent fusion comparisons | AIME26 10.21→21.25，部分域回落 | 证据/对照 | 补搜 / [原文](https://arxiv.org/html/2609.23989v1) |
| [Off-vs-On theory](../papers/di2026_understanding_off_onpolicy.md)（Di et al., 2026） | arXiv | Sequence-level aggregation theory | Tabular regret；无LLM主表 | 理论 | 补搜 / [原文](https://arxiv.org/html/2609.38666v1) |

## 当前证据能支持什么

【综合解释】领域路由、监督权重、目标构造、数据采样与 optimizer 更新属于不同设计轴。多个方法可以同时有效，但现有不同规模、teacher来源、recovery分母和预算的结果不能支持一个统一排行榜。

【范围修订】当前为四个问题主题 G15–G18：多 teacher 学习收益的兼容、多来源专长的兼容组合、互补能力在单一 student 中的使用，以及新增 teacher 的边际价值。原1/6剔除，原2/3收窄合并，原4收窄，原5/7保留并限定边界。**仅通过多 teacher 相关性筛选，尚未认定为高价值 gap**；①②尤其需要限定条件，③④的多 teacher 属性更直接。没有选题排序或 novelty 声明。见[完整报告](../../synthesis/mopd-gap-analysis.md)与[当前问题主题](../gap_map.md)。G1–G14及旧关系仅保留历史语义。

## 来源与覆盖限制

文献图景来自先前对36篇本地论文页及综述的综合；本次只修订问题范围，没有重新逐篇阅读、检索、Zotero访问或原文核查。以下为先前建库过程的来源记录。

先前建库实际使用项目seed、web发现、版本化arXiv HTML/abs；Open-MOPD对摘要措辞的歧义额外核对同版PDF。arXiv API helper已调用但超时，改用官方网页元数据。随后通过WSL2镜像网络补查Windows Zotero本地API：当前user library的40条非attachment records与36篇wiki匹配为0；未检查其他groups或annotations。桌面API可用，当前会话未暴露Zotero MCP。Obsidian未使用，未下载PDF。扩展目录仅用于发现候选，正式页事实均回到原文。未读系统报告、更多垂直Agent/跨模态方法列在综述的待核查部分；不能将36篇当作穷尽收录。
