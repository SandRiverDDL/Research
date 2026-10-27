# Research Wiki Query Pack

_Auto-generated. Do not edit._

## Open Gaps
# Gap Map

更新：2026-10-15。当前仅有四个经多 teacher 相关性筛选的问题主题，**尚未认定为高价值 gap**。多 teacher 相关性指关键问题来自多个 teacher 的选择、交互或整合，不代表 MOPD 独有。本次依据本地笔记修订，未重新核查原文或查新。[完整报告](../synthesis/mopd-gap-analysis.md)。

## G15 — ① 多 teacher 学习收益的兼容

合并并收窄原2/3：只讨论跨 teacher 的预算竞争、相对支配/抵消，以及吸收 B 对 A 能力的影响与联合/顺序整合差异。归一化和投影已有覆盖，需限定何时足够、何时仍有相互作用。[证据与边界](../synthesis/mopd-gap-analysis.md#g15)

## G16 — ② 多来源专长的兼容组合

收窄原4：多个 teacher 的能力增量与继承偏好如何组成兼容目标。Δ-MOPD 已覆盖一部分；缺 precursor、跨 tokenizer 或接口迁移本身不属核心 gap。[证据与边界](../synthesis/mopd-gap-analysis.md#g16)

## G17 — ③ 互补能力在单一 student 中的使用

保留原5：区分可解样本覆盖与同题联合使用。Trust、TU-OPD 已研究互补性；仍需定位现有方法未充分整合的具体互补结构。[证据与边界](../synthesis/mopd-gap-analysis.md#g17)

## G18 — ④ 新增 teacher 的边际价值

保留原7：新增 teacher 的非冗余、可迁移能力能否抵偿整合成本，是否优于强化已有 teacher。泛化的成本统计诉求剔除。[证据与边界](../synthesis/mopd-gap-analysis.md#g18)

## 当前判断的使用边界

①②仍需进一步限定条件；③④多 teacher 属性更直接。四项不构成优先级、选题、方法必要性或 novelty 声明，也可能与离线多教师蒸馏、模型合并共享。已有方法的成功与适用条件须先说明，缺评测不等于方法失败。用户确认的是范围修订，尚未选定研究方向或 lenses；不能自动进入 idea 生成、方案细化、实验规划或查新。36篇本地笔记不是穷尽覆盖，引用记录也不是本次重新核查过的原文证据。这里的 G 前缀只沿用 wiki ID 约定，不将问题主题升级为已成立的 gap。完整证据与限制以报告为准。

## 历史 ID（均不属于当前四个主题）

旧 ID 与 graph 边保留原语义，只用于追溯；不得作为当前主题或本次查新结论。原七项的处理理由见[报告修订表](../synthesis/mopd-gap-analysis.md#4-原七项处理与来源记录)。

## Key Papers (36 total)
- [paper:chen2026_counteractionaware_multiteacher_onpolicy] Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation: CaMOPD 用交替更新、gap-based selection 与监督缩放，恢复 general capability 并保留 domain specialization。
- [paper:di2026_understanding_off_onpolicy] Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives: sequence-level forward/reverse KL 分别对应 arithmetic/geometric teacher 聚合；reverse-KL aggregate 的 token conditionals 还依赖 continuation。
- [paper:fang2026_latentmopd_latent_multiteacher] Latent-MOPD: Latent Multi-Teacher On-Policy Distillation: Latent-MOPD 结合 routed token OPD 与 teacher hidden-state 对齐，以每 teacher crossfade schedule 协调监督。
- [paper:fu2026_rethinking_onpolicy_distillation] Rethinking On-Policy Distillation of Large Language Models II: One Training Example: 少量不同语义 queries 配合不断刷新的 student rollouts，可在固定预算下匹配部分全数据 MOPD。
- [paper:gao2026_openmopd_diagnosing_fixing] Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation: Open-MOPD 以开放三域 recipe 诊断 token 预算失衡，并结合 token-share、gap-aware allocation 和 reward refresh 改善整合。
- [paper:he2026_learn_from_whoever] Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs: MT-SDPO 缓存答案验证后的合格 teacher 集，将外部 critiques 与组内正确 self-anchor 合成 privileged EMA self-teacher。
- [paper:hou2026_uniopd_unifying_onpolicy] Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe: Uni-OPD 同时改善 student 探索与 teacher outcome 排序的一致性，并验证多 teacher 文本/多模态整合。
- [paper:kim2026_pain_more_gain] No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation: IM-MOPD 在 OPD 过程中用 validation recovery 选择未恢复领域，迭代注入对应 teacher task vectors。
- [paper:li2026_beyond_teacher_
## Recent Relationships (182 total)
  idea:g15-repair-aware-endpoint --inspired_by--> paper:liu2026_pmopd_task_ordering
  idea:g15-repair-aware-endpoint --addresses_gap--> gap:G15
  idea:g15-teacher-commutator-steering --inspired_by--> paper:liu2026_pmopd_task_ordering
  idea:g15-teacher-commutator-steering --inspired_by--> paper:zhu2026_upmopd_update_projection
  idea:g15-teacher-commutator-steering --addresses_gap--> gap:G15
  idea:g15-channel-split-rejoin --inspired_by--> paper:zhu2026_upmopd_update_projection
  idea:g15-channel-split-rejoin --inspired_by--> paper:liu2026_pmopd_task_ordering
  idea:g15-channel-split-rejoin --addresses_gap--> gap:G15
  idea:g15-cross-learning-metric --inspired_by--> paper:li2026_beyond_teacher_assignment
  idea:g15-cross-learning-metric --inspired_by--> paper:zhu2026_from_gradients_capabilities
  idea:g15-cross-learning-metric --addresses_gap--> gap:G15
  idea:g15-target-tangent-plastici
