# MOPD 领域图景与四个问题主题：多 teacher 相关性筛选

更新：2026-10-15。文献图景沿用已有36篇论文页的本地综合；本次按用户确认的范围，将原七项收敛为四个问题主题。**这里只完成“多 teacher 相关性”筛选，尚不能认定为四个已经成立的高价值 gap。** 本次未重新核查原文、搜索、查新或复现实验。

论文页是先前协作者编写的二手阅读材料。下文【作者报告】指论文页记录的作者结果；【既有笔记解释】指原笔记解读；【本地综合】与【待验证机制】分别指本地推理及尚待证明的解释。引用指向本地页，并标明其中已有的章节、公式或图表入口；不等于本轮重新核查过原文。作者、年份、venue与36篇逐篇表见[文献地图](../research-wiki/topics/multi-teacher-opd.md)：均为2026年材料，默认按arXiv预印本使用；H-OPD的正式接收仅有作者声明，未独立确认。

## 1. 文献共同勾勒出的领域图景

【本地综合】MOPD已经证明：在若干可比teacher、明确任务和可访问监督的条件下，多个专长可以进入一个student。问题已从“多个teacher能否蒸馏”推进到“哪些能力、通过什么信号、在什么条件与成本下能稳定整合”。[MOPD（Ma等）](../research-wiki/papers/ma2026_mopd_multiteacher_onpolicy.md)有30B和309B模型结果，[Video-MOPD（Qin等）](../research-wiki/papers/qin2026_videomopd_multiteacher_onpolicy.md)覆盖视频与时序定位，[Qwen-Image-2.0-RL（Xu等）](../research-wiki/papers/xu2026_qwenimage20rl_technical_report.md)将student-visited supervision扩展到flow velocity。它们证明了可行性，但不共同证明任意teacher pool、任意能力组合都可压缩；图像系统总提升还包含前置RL。

【本地综合】“多teacher”并非单一问题。独立domain RL experts、同prompt多reward specialists、共享backbone的soft-prefix teachers、多privileged views、提供critique的专家，以及能相互debate的teachers，拥有不同信息、训练成本和错误相关性。它们都能提供整合机制的证据，但不能把不同总体平均分当作同一问题的排行榜。尤其应区分**逐域能力恢复、同题多目标兼顾、一个轨迹内联合调用能力**。

【本地综合】共同出现的困难是：正确路由并不足以规定有效训练。领域token占比、log-ratio尺度、当前student与teacher差距、轨迹探索、目标支持集及optimizer变换都会影响最后学到什么。Open-MOPD中IF缺少gradient tokens，DN-MOPD中IF反而占据大部分初始梯度贡献；这是不同设置、统计对象和loss reduction下的结果，不能拼成一个普适方向的失衡。Gradients→Capabilities又显示，局部梯度差异可以被Adam共享动量显著改变。因此，预算不足、监督失真、参数干扰需要分别辨认。

【本地综合】聚合目标本身决定整合含义。SMOPD的arithmetic mixture、TrustMOPD的weighted reverse-KL、AVSD的共识与残差、Δ-MOPD的teacher-relative shifts、TU-OPD的winner residual，分别强调覆盖、可信选择、互补信息或后训练增量。Off-vs-On理论提醒：sequence-level geometric目标的token conditional包含continuation项，不等于逐位置简单几何平均。聚合已有充分的方法探索；仍需厘清不同互补结构与student可达状态下，目标保留了什么、遗漏了什么。

【本地综合】on-policy也不是无需条件的优胜机制。强SFT/Soft-KD可匹配部分ID recovery；有些online设置在OOD retention上更好。少量queries可接近全数据MOPD，却不意味着减少rollout计算，空prompt又明显变差。这些结果把问题转向：student访问哪些状态、teacher反馈提供何种增量，以及增量是否值得额外训练成本。它们既不否定MOPD，也不支持“更多on-policy交互必然更好”。

### 1.1 方法关系与实际覆盖

本表按文献中的干预位置整理，不预设gap分类。来源均为本地论文页；完整逐篇Problem/Method/Results及作者、venue见上述文献地图。

| 方法关系 | 代表文献与已有解决部分 | 关键条件或结果边界 |
|---|---|---|
| specialize后统一部署 | [MOPD](../research-wiki/papers/ma2026_mopd_multiteacher_onpolicy.md)、[Video-MOPD](../research-wiki/papers/qin2026_videomopd_multiteacher_onpolicy.md)、[Qwen-Image](../research-wiki/papers/xu2026_qwenimage20rl_technical_report.md)：student轨迹上按任务取监督 | 同源/兼容表示与任务路由；文本、视频、连续flow不能直接混算 |
| 分配训练量与信号尺度 | [Open-MOPD](../research-wiki/papers/gao2026_openmopd_diagnosing_fixing.md)、[DN-MOPD](../research-wiki/papers/li2026_beyond_teacher_assignment.md)、[D³-MOPD](../research-wiki/papers/sun2026_d³mopd_dynamic_domain.md)：token-share、dispersion、prompt sampling | 改变不同统计对象；Open 3B Total28.05→31.24；D³单checkpoint recovery .48→.73 |
| 依内部信号分配监督 | [TrustMOPD](../research-wiki/papers/sun2026_distill_what_you.md)、[MOPD-Router](../research-wiki/papers/xu2026_mopdrouter_rethinking_teacher.md)、[UCMOPD](../research-wiki/papers/liu2026_recovering_general_capabilities.md)：reference位移、方向对齐、entropy endorsement | 无标签token选择/轨迹筛选已有实证；proxy不等于正确性，也不等于少查询teacher |
| 依outcome验证监督 | [TGOPD](../research-wiki/papers/zhang2026_verify_before_you.md)、[VG-OPD](../research-wiki/papers/xu2026_who_teaches_which.md)、[Uni-OPD](../research-wiki/papers/hou2026_uniopd_unifying_onpolicy.md)：prompt gate、criterion许可、return排序修正 | 需要可靠verifier；验证对象不同；TGOPD中mask-only有时优于RL fallback |
| 利用异模态或交互信息 | [H-OPD](../research-wiki/papers/yin2026_hopd_confidence_aware.md)、[MT-SDPO](../research-wiki/papers/he2026_learn_from_whoever.md)、[MAD-OPD](../research-wiki/papers/wang2026_madopd_breaking_ceiling.md)：description、verified critiques、debate | 信息桥接已存在；自信或曾答对不认证当前prefix上的纠正；MT-SDPO不同模型收益不一致 |
| 保护已学能力 | [CaMOPD](../research-wiki/papers/chen2026_counteractionaware_multiteacher_onpolicy.md)、[PMOPD](../research-wiki/papers/liu2026_pmopd_task_ordering.md)、[Road](../research-wiki/papers/tian2026_beyond_domainrouted_supervision.md)、[UP](../research-wiki/papers/zhu2026_upmopd_update_projection.md)、[SF](../research-wiki/papers/yin2026_slowfast_multiteacher_onpolicy.md)、[ACLArena](../research-wiki/papers/wang2026_aclarena_agent_continual.md) | 保护对象分别为交替目标、历史更新子空间、辅助梯度、实际displacement、EMA偏好及阶段能力 |
| 改变迁移载体与训练路径 | [IM-MOPD](../research-wiki/papers/kim2026_pain_more_gain.md)、[Latent-MOPD](../research-wiki/papers/fang2026_latentmopd_latent_multiteacher.md)、[Δ-MOPD](../research-wiki/papers/sang2026_composing_what_each.md) | task vectors、hidden states、teacher-minus-precursor shifts已有收益；分别依赖兼容参数、表示/tokenizer、准确precursor |
| 兼顾共同与独有信号 | [AVSD](../research-wiki/papers/nguyen2026_avsd_adaptiveview_selfdistillation.md)、[SMOPD](../research-wiki/papers/wang2026_smopd_multireward_reinforcement.md) | 前者是同backbone privileged views；后者是reward specialists且带在线RL |
| 构造teacher pool | [TU-OPD](../research-wiki/papers/lu2026_beyond_best_teacher.md)、[PromptSD](../research-wiki/papers/ma2026_one_student_many.md) | 互补残余题训练与soft-prefix teachers已有方法；前者制备成本未等预算比较，后者不等同独立RL专家 |
| 改变问题数据 | [DF-OPD](../research-wiki/papers/li2026_datafree_onpolicy_distillation.md)、[One Training Example](../research-wiki/papers/fu2026_rethinking_onpolicy_distillation.md) | 固定训练预算下1000自生题或16-shot/domain可接近相应全数据结果；不代表免训练计算或普遍覆盖 |
| 重审比较优势 | [Rethinking Merging](../research-wiki/papers/xie2026_rethinking_selfdistillation_multiteacher.md)、[Fusion Paradigms](../research-wiki/papers/wu2026_consolidating_rlvr_capabilities.md) | 强SFT/Soft-KD与merge构成必要对照；ID/OOD、领域权重和计算口径可改变结论 |
| 解释信号与能力的联系 | [Gradients→Capabilities](../research-wiki/papers/zhu2026_from_gradients_capabilities.md)、[Every Coin](../research-wiki/papers/li2026_every_coin_has.md)、[Tool-call drift](../research-wiki/papers/shen2026_when_topk_misses.md)、[Off-vs-On theory](../research-wiki/papers/di2026_understanding_off_onpolicy.md) | 分别限制梯度几何、prompt域隔离、top-K mass保真和逐token聚合的解释；局部机制与理论不能无条件外推 |

### 1.2 共识、表面分歧与尚未分清的层次

- **已有共识（本地覆盖内）**：多teacher整合可行；domain label不保证最佳监督；同一student会受到跨域影响；初始化、目标、数据和optimizer均可能影响结果。共识不等于每种干预在每个设置都必要。
- **条件性分歧**：预算修正有时很有效、某些averaging差别又很小；MOPD有时优于Mix-RL、merge或离线训练有时可比；保留共识与保留teacher特有分布都有成功实例。应先检查设置与目标差异，不能据此选出普适结论。
- **失败模式**是可观察行为，如IF弱化、错误teacher仍受模仿、over-calling、恢复一个域时另一个域回落。**瓶颈**需要解释限制机制：特定top-K目标遗漏决策坐标有干预证据，“所有退化都源于梯度冲突”则没有。
- **research gap**是重要目标仍未充分解决的部分，可以来自机制未明、适用条件受限或目标不完整；不要求先有“修复后仍失败”的数值。**evidence gap**是判断所缺的证据：没有某项benchmark、计时或大规模消融，不自动证明现有方法失败。

## 2. 经多 teacher 相关性筛选的四个问题主题

这里将“MOPD 特有”限定为：**问题的关键部分来自多个 teacher 的选择、交互或整合。** 这些问题可能与离线多教师蒸馏、模型合并共享，不能说只有 MOPD 才存在。一般的监督效用、曝光不足、支持集遗漏、optimizer 变换、遗忘、接口迁移或 online/offline 差异，不单独列为核心 gap。

以下四项不作优先级排序，也不构成选题、方法必要性或 novelty 声明。①②尤其需要进一步限定条件；③④的多 teacher 属性更直接。为保留旧图谱语义，四个收窄后的主题使用 G15–G18；原 G8–G14 的处理见文末。

<a id="g15"></a>

### ① G15 — 多 teacher 的学习收益如何兼容，而不是彼此挤占或抵消？

**问题范围。** 合并原2、3，仅保留跨 teacher 相互作用：不同 teacher 的监督尺度、训练比例与整合顺序，如何影响各自能力在同一 student 中的获得与保留。关注相对支配、训练预算竞争，以及吸收 teacher B 时是否损害从 teacher A 获得的能力；联合整合与顺序整合可能呈现不同取舍。

**已有覆盖。** 【作者报告，据本地笔记】Open-MOPD、DN-MOPD 与 D³-MOPD 分别处理不同领域监督的 token 份额、信号尺度和采样比例；PMOPD、Road、UP-MOPD 等处理整合顺序与能力干扰。DN 的归一化和 UP 的实际更新投影已直接覆盖部分问题，不能把“平衡多个 teacher”或“保护已有能力”当作空白。

**仍需限定的部分。** 【开放问题】在什么 teacher 组合、训练比例与整合顺序下，现有归一化、调度或投影已足够？何时仍存在跨 teacher 的相对支配、抵消或能力损害？【本地解释】Open 与 DN 在不同设置下呈现不同失衡方向，Gradients→Capabilities 显示局部梯度差异会受 optimizer 改变；这些证据要求限定设置，不能拼成普适的“梯度冲突”结论。泛泛的“梯度如何变成能力”“如何避免遗忘”不再是本条研究问题。

**判断边界。** 简单预算修正、固定权重、已有投影或更相关训练数据可能已足够。保护代理与长期行为不一致，本身也是通用持续学习问题；只有落实到 A/B teacher 的整合关系时才属于本条。现有结果支持部分跨 teacher 相互作用值得研究，但尚未证明已有处理后仍存在独立且高价值的方法瓶颈。

证据入口：[Open §3.2/Fig.3/§4](../research-wiki/papers/gao2026_openmopd_diagnosing_fixing.md)；[DN Algorithm1/Tables C.10、D.3/App.E.2](../research-wiki/papers/li2026_beyond_teacher_assignment.md)；[D³ §3/App.I](../research-wiki/papers/sun2026_d³mopd_dynamic_domain.md)；[Gradients→Capabilities §3–5/Figs.2、5](../research-wiki/papers/zhu2026_from_gradients_capabilities.md)；[PMOPD §4/Table4](../research-wiki/papers/liu2026_pmopd_task_ordering.md)；[Road §3.3/Table3](../research-wiki/papers/tian2026_beyond_domainrouted_supervision.md)；[UP §2.3/§3.1 Table1](../research-wiki/papers/zhu2026_upmopd_update_projection.md)。

<a id="g16"></a>

### ② G16 — 不同训练来源的专长能否兼容地整合？

**问题范围。** 收窄原4。多个 teacher 的能力增量与各自继承偏好一起进入目标时，哪些训练背景差异会妨碍这些专长在同一 student 中组合？核心是多个来源如何共同构成兼容目标；单独的跨 tokenizer、跨接口迁移或缺 precursor 不再列为本项目核心 gap。

**已有覆盖。** 【作者报告，据本地笔记】Δ-MOPD 通过 teacher-relative shifts 分离后训练增量与继承偏好，已有多 teacher 结果及 phased-order 对照，直接研究了本条的一部分。基础 MOPD 的异源 teacher 替换结果、Every Coin 的跨 prompt 域影响提供相关观察；IM-MOPD 的 task-vector 注入提供另一种整合路径。不能把异源整合笼统写成未被研究。

**仍需限定的部分。** 【开放问题】当不同来源带来的偏好并不一致时，哪些差异会妨碍各自专长组成兼容的联合目标，哪些已可由相对 shift 或现有整合方法处理？Δ 的准确 precursor 与可比较 token 坐标限定其适用范围，但**缺 precursor 本身仍不是多 teacher 特有问题**，不能据此直接宣布一个新 gap。

**判断边界。** 有准确 precursor 时 Δ 已是直接解决方案；参数兼容时 IM 或普通 merge 可能足够。更强异源 teacher 下的训练不稳定，也可能涉及学习率、尺度或初始化，不能全部归因于继承偏好冲突。多来源偏好不一致何时成为现有方法未充分处理的组合障碍，仍需条件化证据；本次不认定任意异源 pool 都存在独立瓶颈。

证据入口：[Δ §2–3 Eq.2–6/Tables2–3/§9](../research-wiki/papers/sang2026_composing_what_each.md)；[MOPD §4.4.2](../research-wiki/papers/ma2026_mopd_multiteacher_onpolicy.md)；[Every Coin §4/App.C.4](../research-wiki/papers/li2026_every_coin_has.md)；[IM §3.2/Table2](../research-wiki/papers/kim2026_pain_more_gain.md)。

<a id="g17"></a>

### ③ G17 — teacher 之间的互补，怎样变成同一个 student 可使用的互补能力？

**问题范围。** 保留原5。明确区分两种目标：覆盖更多可解样本，以及在同一任务中联合使用不同专长。前者成功不能自动证明后者成功；核心是分散于多个 teacher 的能力如何进入同一部署 student。

**已有覆盖。** 【作者报告，据本地笔记】Trust 的 MultiCap 与生成位置分配对照已研究生成过程中能力需求的变化；TU-OPD 已构造互补 teachers 并压缩可解题 union。H-OPD 的 VL/text 专长组合、SMOPD 的同 prompt 多 reward 整合、AVSD 的共识与特有 residual、MAD-OPD 的 teacher 交互监督也各有覆盖。因此，“利用互补性”本身不是空白。

**仍需限定的部分。** 【开放问题】具体哪种互补结构仍不能被已有方法充分整合？需要说明互补发生在样本之间、同题不同阶段还是不同约束之间，以及目标要求的是覆盖并集还是联合使用。只有定位具体结构及既有方法的适用边界，才能进一步判断是否存在方法 gap；缺一个组合 benchmark 不足以完成这一判断。

**判断边界。** Trust、H-OPD、SMOPD 已有部分联合使用证据，不能声称现有方法只会分域选择。TU-OPD 的 student 超过 best teacher 也不自动证明跨域同题组合。【待验证假设】局部聚合丢失独有有效模式、关键联合状态访问不足、student 容量不足，是不同解释，本地材料未统一区分。③的多 teacher 属性明确，但普遍组合失败及新方法必要性均未成立。

证据入口：[Trust Table1/App.C.4.1/App.F](../research-wiki/papers/sun2026_distill_what_you.md)；[TU-OPD §3/Tables1、3](../research-wiki/papers/lu2026_beyond_best_teacher.md)；[H-OPD §3/Table1/App.C Table8](../research-wiki/papers/yin2026_hopd_confidence_aware.md)；[SMOPD §2.2–3/Tables1–2](../research-wiki/papers/wang2026_smopd_multireward_reinforcement.md)；[AVSD §2 Eq.2–3](../research-wiki/papers/nguyen2026_avsd_adaptiveview_selfdistillation.md)；[MAD-OPD §4/Table1](../research-wiki/papers/wang2026_madopd_breaking_ceiling.md)。

<a id="g18"></a>

### ④ G18 — 什么样的新增 teacher 值得加入，新增能力能否抵偿整合成本？

**问题范围。** 保留原7，删除泛化的成本统计诉求。核心是新增 teacher 提供多少非冗余、可迁移且能被 student 吸收的能力，以及增加 teacher 相比强化已有 teacher 是否更有价值。它涉及 pool 的构成与扩展，不能简化为补一张成本表。

**已有覆盖。** 【作者报告，据本地笔记】TU-OPD 通过残余可解区域构造互补 teachers 并压缩其 union，已经把 pool 构成作为方法的一部分；PromptSD 探索共享 backbone 的 soft-prefix teachers，改变 teacher 制备方式。现有路由、调度与 offload 等机制也会影响整合代价，不能预设 teacher 数量增加必然导致成本等比例上升。

**仍需限定的部分。** 【开放问题】新增 teacher 的独有能力在多大程度上可被 student 吸收，何时只是增加重复监督或引入整合冲突？在给定资源下，这种增量何时比强化已有 teacher 更有价值？TU-OPD 的互补构造提供直接起点，但本地笔记记录的等总预算比较边界，尚不足以确定最优 pool 构成或扩展规律。

**判断边界。** 已有 teacher 的复用与从零制备 pool 是不同决策。成本在此用于判断新增能力是否划算；单纯缺计时、成本表或大 pool 实验只属于证据不足，不能自动升级为方法 gap。④的多 teacher 属性明确，但哪些新增 teacher 值得加入、是否需要新方法，仍待具体任务与 student 条件下的证据。

证据入口：[TU-OPD §3/Table3/Limitations（含成本与覆盖边界）](../research-wiki/papers/lu2026_beyond_best_teacher.md)；[PromptSD App.C Table8/§7](../research-wiki/papers/ma2026_one_student_many.md)。成本口径及可行实现参照[综述成本表](mopd-literature-review.md#成本证据)，不作为独立核心 gap。

## 3. 四个主题的关系与判断边界

【本地解释】①关注多个 teacher 在学习过程中的相互作用；②关注不同训练来源带来的专长与偏好能否组成兼容目标；③关注整合后实际需要使用的互补结构；④关注 pool 构成与新增 teacher 的边际价值。它们可以相互影响，但不要求一次方法工作同时回答全部问题。

**四项仅通过多 teacher 相关性筛选，尚未通过高价值 gap、方法必要性或 novelty 判断。** ①②仍需进一步限定条件；③④多 teacher 属性更直接，也不能因此自动视为优先选题。用户确认的是范围修订，尚未确认具体研究方向或 lenses。

- 通用 OPD、持续学习与接口迁移证据仍可用于解释领域图景或作为对照；出现在 MOPD 论文里，不会自动使问题变成多 teacher 特有。
- 区分作者报告、本地解释与待验证假设。不能从剩余分数差、缺评测或某个假设受限直接推出需要新方法；已有有效替代方案必须纳入判断。
- 不将 recovery 当准确率；single-checkpoint 与逐 benchmark 峰值、Avg@K 与 pass@K、ID 与 OOD 须分别理解。指标与成本分母见[本地综述](mopd-literature-review.md)。
- 36篇不是穷尽覆盖。未建正式页的系统报告和垂直方法仍只是覆盖入口；本次不据此宣称无人研究，也不开展查新、idea 生成、方案细化或实验规划。

## 4. 原七项处理与来源记录

下表保留原 ID 和锚点，仅用于历史追溯；原七项不再是当前核心 gap 清单。

| 原条目 / 历史 ID | 本次处理 | 原因与当前去向 |
|---|---|---|
| <a id="g8"></a>1 / G8：监督是否真正有用 | 剔除原条目 | teacher 答对原题能否纠正 student prefix，单 teacher 同样面对。选择与聚合多个 teacher 是更具体的问题，不能靠引用 Router 将原问题改称 MOPD 特有。 |
| <a id="g9"></a>2 / G9：信号如何转成能力 | 收窄，与3合并 | 只保留跨 teacher 的预算竞争、相对支配或抵消，进入① G15。曝光不足、支持集缺失、optimizer 变换本身不属核心 gap。 |
| <a id="g10"></a>3 / G10：能力保护跨分布、跨阶段成立 | 收窄，与2合并 | 只保留吸收 B 是否损害从 A 获得的能力，以及联合/顺序整合的差异，进入① G15。通用遗忘与保护代理失真剔除。 |
| <a id="g11"></a>4 / G11：异源 teacher 迁移专长 | 收窄 | 只保留多来源专长与继承偏好的兼容组合，进入② G16。单独的 tokenizer、接口或 precursor 缺失不属核心 gap。 |
| <a id="g12"></a>5 / G12：互补能力联合使用 | 保留并明确边界 | 进入③ G17；区分可解样本覆盖与同一任务中的联合使用，需定位尚未充分整合的具体互补结构。 |
| <a id="g13"></a>6 / G13：on-policy 附加收益的条件 | 剔除原条目 | online/offline、状态覆盖与 OOD 收益的原表述属于通用 OPD，未指出多 teacher 引入的独立部分。 |
| <a id="g14"></a>7 / G14：扩大 teacher pool 是否划算 | 保留，删除泛化成本统计诉求 | 进入④ G18；只聚焦新增 teacher 的非冗余、可迁移能力及整合价值。缺成本表只是证据不足。 |

文献图景沿用先前对36篇本地论文页的综合。本次按用户确认的筛选标准修改范围与入口，没有重新逐篇阅读或核查原文。G1–G14 及其旧 graph 边保留历史语义；G15–G18 是当前四个问题主题，ID 前缀沿用 wiki 约定，不代表已确认的 gap。通过 ARIS helper 记录的当前关系只表示已有工作覆盖相关主题的一部分，不表示剩余问题成立或已被解决。

本次结构与链接验证见[项目状态](../doc/memory/STATE.md)与[wiki 检查记录](../research-wiki/LINT_REPORT.md)。本地检查通过不代表原文核查、novelty 验证或实验复现。
