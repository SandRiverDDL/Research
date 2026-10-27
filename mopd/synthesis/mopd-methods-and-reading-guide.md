# MOPD 方法地图、阅读路线与同期对照

更新：2026-10-16。范围为当前36篇阅读笔记，包含方法、诊断证据、理论与系统报告。方法地图复用已有笔记；本轮新工作是36/36版本化原文HTML的定点表格/实验段检索，并对下列baseline证据逐项核对。不是36篇重新全文精读，也不是新的查新或方法生成。

## 先抓住共同骨架

【事实/综合】student先生成自己的轨迹；teacher在student已经生成的prefix上给监督；训练过程决定用哪个teacher、如何混合/缩放信号，再把它变成student参数更新。绝大多数后续工作改动这条链中的一到两个位置。多teacher还包括独立RL专家、多模态/文本teacher、同backbone多privileged views和critique experts，不能把它们当成同一种实验设置。

| 阅读时的问题 | 主要方法 | 实际改变什么 |
|---|---|---|
| 这条训练链怎样工作？ | MOPD；Video-MOPD；Qwen-Image-2.0-RL | 基础routed recipe及其应用；图像flow的监督对象不是token概率 |
| 各teacher究竟得到多大训练份额？ | Open-MOPD；DN-MOPD；D³-MOPD | 分别调token预算/反馈刷新、反馈尺度、prompt采样比例 |
| 当前状态该信谁？ | TrustMOPD；MOPD-Router；H-OPD；TGOPD；VG-OPD | reference位移、方向对齐、熵或外部验证决定监督选择/权重 |
| 学一个专长时怎样保住其他专长？ | UP；PMOPD；Road；SF；CaMOPD；UCMOPD | 分别干预实际更新、历史子空间、辅助teacher梯度、慢reference或训练信号选择；保护对象不相同 |
| 整合的目标本身是什么？ | Δ-MOPD；Latent-MOPD；SMOPD；AVSD | teacher增量、hidden states、多reward分布、跨view共识/残差信号 |
| teacher池从哪里来、怎样协作？ | TU-OPD；MAD-OPD；PromptSD；MT-SDPO | 互补teacher训练、debate、soft-prefix teacher、verified critiques |
| OPD优势和失败究竟由什么导致？ | Fusion Paradigms；Rethinking Capability Merging；Gradients→Capabilities；数据/支持集诊断 | 强baseline、指标、训练成本及机制解释，帮助审查方法论文 |

这些分组是阅读索引，存在交叉，不是彼此排斥的研究分类。

## 约两小时的首轮路线

【阅读建议，时间是建议预算】先读5篇的关键段，不通读36篇：

1. **MOPD，约20分钟**：§3、Table 2、一个必要消融。弄清student轨迹、冻结teacher、domain routing和reverse-KL；统一后面论文的共同语言。[原文](https://arxiv.org/html/2606.30406v1#S3)
2. **Open-MOPD，约20分钟**：方法、capability imbalance诊断及主表。它也是多个后续论文反复复现的对照入口，阅读价值包括开放recipe与评测设置。[已有笔记](../research-wiki/papers/gao2026_openmopd_diagnosing_fixing.md)
3. **TrustMOPD，约20分钟**：§3、Table 1、response-level对照、Table 12成本。学习token级监督分配；注意MultiCap训练与overall recovery并非同题端到端组合率。[原文](https://arxiv.org/html/2609.23697v3#S3)
4. **UP-MOPD，约20分钟**：§2、Tables 1–2、gradient projection对照。看清“改原始梯度”与“改Adam后的实际更新”的区别，并核对重放成本。[原文](https://arxiv.org/html/2610.08398v1#S2)
5. **Consolidating RLVR / Fusion Paradigms，约15分钟**：同源experts、同数据条件和Tables 1–2。先建立Merge/MixRL/MOPD的公平对照与成本意识。[已有笔记](../research-wiki/papers/wu2026_consolidating_rlvr_capabilities.md)

首轮约95分钟，剩余时间用于核实一处最关心的baseline或消融。以上是覆盖代表机制的路线，不是论文质量排名。

## 第二轮只读与你的问题相邻的差异

| 当前关心什么 | 建议补读 | 与已读代表作相比，只需新增理解 |
|---|---|---|
| 监督选择/无标签routing | Router；TGOPD；VG-OPD | ExpertAlign如何定义；prompt admission与criterion许可分别验证什么；不要重读完整OPD推导 |
| 能力份额/尺度失衡 | DN-MOPD；D³-MOPD | 更新权重与采样权重的区别；Open统计token budget，DN统计feedback dispersion，不把两个设置的诊断拼成普适规律 |
| 更新互相干扰 | PMOPD；Road；SF-MOPD | 保护历史子空间/辅助teacher梯度/慢reference，各需要哪些额外状态和计算 |
| 你之前关心的互补与联合使用 | TU-OPD → Δ-MOPD → SMOPD；再按需MAD-OPD | 分清可解题union、teacher增量、同prompt多目标、teacher交互。TU的union成功不自动证明同题联合调用 |
| 多模态联合专长 | H-OPD；Video-MOPD；SF-MOPD | text teacher如何获取视觉信息，teacher pool与监督接口是否仍可比 |
| teacher制备/privileged information | PromptSD；AVSD；MT-SDPO | soft prefixes、多views与verified critique提供何种训练期信息，部署student是否可访问 |
| 数据预算或强baseline | One Training Example；Data-Free OPD；Rethinking Capability Merging | 少prompt是否真的少rollout；SFT/Soft-KD有没有独立调参；ID recovery与OOD retention分开看 |
| 诊断自己的实现 | Gradients→Capabilities；When Top-K Misses；Off-vs-On理论 | loss reduction、optimizer state、支持集与sequence objective；只读与你实现相关的诊断 |

## 每篇10分钟的差异阅读模板

只回答五个问题，再决定是否精读：

1. **改哪一步？** 用一句话和一条关键公式说清改动；找不到就先看Algorithm/overview。
2. **关键证据是什么？** 看一个主表加一个能区分作者解释与替代解释的消融；只看总分提升不够。
3. **比过谁？** 找最接近的同期完整方法，而非只看vanilla MOPD；确定是本地复现还是引用原作者数字。
4. **比较条件是什么？** teacher pool、student初始化、domain labels/privileged context、prompts、token/step预算、评测采样是否一致。
5. **新增成本与边界是什么？** 额外teacher forward、probe/debate、rollout、reference/hidden states或gradient replay；读绝对分数，核实recovery分母。

如果这五点与当前研究问题没有直接关系，留下已有wiki入口即可。重复的Introduction、benchmark定义和通用OPD推导不必每篇再读。若方法将成为你的baseline或承重novelty对照，再读实现与附录。

## 有没有对比同期MOPD？有，但网络不完整

【本轮原文核对】以下是明确列入实验主表/实验baseline段的对照，不只是related-work引用：

| 本文 | 实际对照 | 原文入口与比较边界 |
|---|---|---|
| MOPD-Router | Open-MOPD；Standard MOPD；Mean Aggregation | [Tables 1–2及§4.1 Baselines](https://arxiv.org/html/2609.30837v2#S4.T1)；无标签数据的routed baselines另获得模型生成domain labels；Entropy/Novelty是路由变体。 |
| PMOPD | Open-MOPD；MOPD；BB-MOPD | [§5.2明确称在本地模型/任务复现Open-MOPD](https://arxiv.org/html/2609.34605v1#S6.T3)；同总prompt数不自动等于相同总算力。 |
| UCMOPD | CaMOPD；vanilla MOPD；SelecTKD；ReOPOLD | [§4.1/Table 2，role-playing与medical设置。CaMOPD是直接多teacher对照，其余两项为相关distillation对照。](https://arxiv.org/html/2608.26735v2#S4.T2)； |
| UP-MOPD | Open-MOPD；GP-MOPD | [Table 2](https://arxiv.org/html/2610.08398v1#S3.T2)；星号为引用原作者结果，非星号为本论文复现/方法。医疗Table 1主要比M-OPD/GP，不把两张表混为同一baseline集合。 |
| Road MOPD | Open-MOPD；CaMOPD；vanilla MOPD；ExOPD | [Table 1及附录baseline实现](https://arxiv.org/html/2610.13521v1#S4.T1)；同一主表已有同期多teacher算法比较。ExOPD是相关OPD方法，不能全部算作独立MOPD算法。 |
| SF-MOPD | Open-MOPD；VAD-MOPD；MOPD；MeanTeacher；OPD-V | [视觉语言Table 1，作者称同数据/预算复现](https://arxiv.org/html/2610.02324v1#S2.T1)；更丰富对照集中在8B block，不把此结果当成纯文本三域排行。 |

【本地综合】这批已核对的实验中，**Open-MOPD是反复出现的对照，CaMOPD在general–specialist恢复方向也被复用**。可以沿这些对照关系读，建立可比设置；这不表示二者是全领域唯一最强baseline。

三处需要避免误读：

- **TrustMOPD Table 1**注明其MOPD baseline使用Open-MOPD实现。表中的实验行是label-routed MOPD、Uniform、Random、single teacher及Trust等；“使用代码”不能自动解释成比较了完整Open-MOPD改进。[Table 1](https://arxiv.org/html/2609.23697v3#S4.T1)
- **DN-MOPD Tables 1–2**包含Uniform pool、Dynamic router、Label-routed MOPD以及SFT/merging/single-teacher对照。它们不能直接改名为完整TrustMOPD或MOPD-Router的复现。[Table 1](https://arxiv.org/html/2609.35347v1#S3.T1)
- **IM-MOPD Table 1**主要比较普通初始化、SFT warm-up、Uniform Merge与iterative merging；这能检查初始化/注入时机，不构成它优于所有路由/投影MOPD变体的证据。[Table 1](https://arxiv.org/html/2609.34745v1#S4.T1)

因此，看见“SOTA”应改问“在什么teacher pool、哪些对照和什么预算下”。不能跨论文直接拿recovery百分比或Overall建立统一排行榜。引用了同期论文也不证明已经做了实测比较。

## 36篇的快速定位

下表方法描述来自既有原文阅读笔记，本轮未重写论文页。按主要贡献归组，方便只打开需要的分支。

### 基本recipe与系统落地

| 论文入口 | 一句话改动/证据 |
|---|---|
| [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](../research-wiki/papers/ma2026_mopd_multiteacher_onpolicy.md) | 独立训练领域 RL teachers，再在 student 自采样轨迹上做 domain-routed reverse-KL 蒸馏，实现能力整合。 |
| [Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding](../research-wiki/papers/qin2026_videomopd_multiteacher_onpolicy.md) | Video-MOPD 以视频、时序定位、STEM 独立 experts 做领域路由蒸馏，并离线筛选可靠高差距数据。 |
| [Qwen-Image-2.0-RL Technical Report](../research-wiki/papers/xu2026_qwenimage20rl_technical_report.md) | Qwen-Image-2.0-RL 以 student flow trajectories 的 velocity matching 整合 T2I 与 editing 专家。 |

### 各来源的训练份额与尺度

| 论文入口 | 一句话改动/证据 |
|---|---|
| [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](../research-wiki/papers/gao2026_openmopd_diagnosing_fixing.md) | Open-MOPD 以开放三域 recipe 诊断 token 预算失衡，并结合 token-share、gap-aware allocation 和 reward refresh 改善整合。 |
| [Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation](../research-wiki/papers/li2026_beyond_teacher_assignment.md) | DN-MOPD 保持领域路由，以 pooled/domain feedback dispersion 比值归一化各域蒸馏信号。 |
| [D³-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation](../research-wiki/papers/sun2026_d³mopd_dynamic_domain.md) | D³-MOPD 依据已有 reverse-KL 的相对量与下降速度，动态调整领域 prompt sampling。 |

### 监督选择、可靠性与探索

| 论文入口 | 一句话改动/证据 |
|---|---|
| [Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation](../research-wiki/papers/sun2026_distill_what_you.md) | TrustMOPD 用 teacher 相对共同 pre-RL reference 的位移校准无标签 token 级监督分配。 |
| [MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation](../research-wiki/papers/xu2026_mopdrouter_rethinking_teacher.md) | MOPD-Router 用 teacher 专长方向与其对 student 的纠正方向对齐度，分配无标签 token 级 OPD 信号。 |
| [H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation](../research-wiki/papers/yin2026_hopd_confidence_aware.md) | H-OPD 以逐 token 预测熵融合独立 VL/text teachers，替代静态样本路由。 |
| [Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation](../research-wiki/papers/liu2026_recovering_general_capabilities.md) | UCMOPD 用双温采样与 entropy-calibrated endorsement 筛选轨迹和 token，恢复一般能力并保留 specialization。 |
| [Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation](../research-wiki/papers/zhang2026_verify_before_you.md) | TGOPD 用 teacher 多次答案验证决定 prompt 是否接受 OPD，否则使用 GRPO fallback。 |
| [Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning](../research-wiki/papers/xu2026_who_teaches_which.md) | VG-OPD 按 criterion 验证 teacher 许可，在 student disagreement tokens 上加入稀疏蒸馏 advantage。 |
| [Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe](../research-wiki/papers/hou2026_uniopd_unifying_onpolicy.md) | Uni-OPD 同时改善 student 探索与 teacher outcome 排序的一致性，并验证多 teacher 文本/多模态整合。 |

### 能力保护、目标与参数整合

| 论文入口 | 一句话改动/证据 |
|---|---|
| [Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation](../research-wiki/papers/chen2026_counteractionaware_multiteacher_onpolicy.md) | CaMOPD 用交替更新、gap-based selection 与监督缩放，恢复 general capability 并保留 domain specialization。 |
| [PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation](../research-wiki/papers/liu2026_pmopd_task_ordering.md) | PMOPD 结合 task ordering/cycling 与累计更新子空间投影，保护已学习领域能力。 |
| [UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation](../research-wiki/papers/zhu2026_upmopd_update_projection.md) | UP-MOPD 直接投影 AdamW 实际候选 displacement，而非仅修正送入 optimizer 的梯度。 |
| [Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation](../research-wiki/papers/tian2026_beyond_domainrouted_supervision.md) | Road MOPD 在同一 student trajectory 上引入辅助 teachers，以 token agreement 和受约束梯度修正保护跨域能力。 |
| [Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation](../research-wiki/papers/yin2026_slowfast_multiteacher_onpolicy.md) | SF-MOPD 以慢速 EMA reference 修正 teacher 的 log-prob 方向，兼顾视觉领域学习与一般能力保留。 |
| [No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation](../research-wiki/papers/kim2026_pain_more_gain.md) | IM-MOPD 在 OPD 过程中用 validation recovery 选择未恢复领域，迭代注入对应 teacher task vectors。 |
| [Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts](../research-wiki/papers/sang2026_composing_what_each.md) | Δ-MOPD 将 teacher 相对各自 precursor 的 logit shift 重新锚定到冻结 student initialization，替代 endpoint target。 |
| [Latent-MOPD: Latent Multi-Teacher On-Policy Distillation](../research-wiki/papers/fang2026_latentmopd_latent_multiteacher.md) | Latent-MOPD 结合 routed token OPD 与 teacher hidden-state 对齐，以每 teacher crossfade schedule 协调监督。 |

### teacher构造、聚合与协作

| 论文入口 | 一句话改动/证据 |
|---|---|
| [Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold](../research-wiki/papers/lu2026_beyond_best_teacher.md) | RGRPO 逐轮训练互补 teachers，TU-OPD 以质量加权与 winner residual 压缩其可解题并集。 |
| [SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation](../research-wiki/papers/wang2026_smopd_multireward_reinforcement.md) | SMOPD 训练 reward-priority specialists，再以 arithmetic teacher mixture 的 forward-KL 和 GDPO anchor 整合。 |
| [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](../research-wiki/papers/wang2026_madopd_breaking_ceiling.md) | MAD-OPD 让多个独立 teachers 在 student states 上 debate，再以自报 confidence 加权 token 监督。 |
| [AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals](../research-wiki/papers/nguyen2026_avsd_adaptiveview_selfdistillation.md) | AVSD 将多个 privileged views 的 geometric consensus 与经一致性约束的 arithmetic residual 结合成自蒸馏目标。 |
| [One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context](../research-wiki/papers/ma2026_one_student_many.md) | PromptSD 在共享冻结 backbone 上学习 task-specific soft-prefix teachers，再将其通过 OPD 压缩到无 prefix student。 |
| [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs](../research-wiki/papers/he2026_learn_from_whoever.md) | MT-SDPO 缓存答案验证后的合格 teacher 集，将外部 critiques 与组内正确 self-anchor 合成 privileged EMA self-teacher。 |

### 机制诊断、数据与强对照

| 论文入口 | 一句话改动/证据 |
|---|---|
| [Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives](../research-wiki/papers/di2026_understanding_off_onpolicy.md) | sequence-level forward/reverse KL 分别对应 arithmetic/geometric teacher 聚合；reverse-KL aggregate 的 token conditionals 还依赖 continuation。 |
| [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](../research-wiki/papers/fu2026_rethinking_onpolicy_distillation.md) | 少量不同语义 queries 配合不断刷新的 student rollouts，可在固定预算下匹配部分全数据 MOPD。 |
| [Data-Free On-Policy Distillation: How Far Can We Go Without External Data?](../research-wiki/papers/li2026_datafree_onpolicy_distillation.md) | teacher 自生成少量固定问题可支持 MOPD 能力恢复，但空 prompt 的成功强依赖 student 行为。 |
| [Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models](../research-wiki/papers/li2026_every_coin_has.md) | OPD 可跨 prompt 域传递 teacher 偏好，固定 domain routing 并不能隔离 teacher 对其他能力的影响。 |
| [When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation](../research-wiki/papers/shen2026_when_topk_misses.md) | teacher top-K 可保留几乎全部概率质量，却遗漏纠正 student 工具调用决策所需的低概率坐标。 |
| [ACLArena: Agent Continual Learning in Multi-stage Post-training](../research-wiki/papers/wang2026_aclarena_agent_continual.md) | ACLArena 比较顺序训练后 MOPD、离线 replay 与 merging，显示 Agent 多能力恢复仍有明显取舍。 |
| [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](../research-wiki/papers/wu2026_consolidating_rlvr_capabilities.md) | 同源五域 experts/data 下，Merge、Mix RL 和 standard MOPD 呈现不同能力与成本取舍。 |
| [Rethinking Self-Distillation for Multi-Teacher Capability Merging](../research-wiki/papers/xie2026_rethinking_selfdistillation_multiteacher.md) | 独立调参和高质量 teacher 数据下，SFT/Soft-KD 可匹配部分 MOPD ID recovery，OOD retention 与运行成本仍有差异。 |
| [From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation](../research-wiki/papers/zhu2026_from_gradients_capabilities.md) | 损失平均、Adam momentum 与数值精度会改变 teacher 信号的表观几何；更接近完整词表梯度并不稳定提升能力。 |

## 新鲜核查与限制

36/36对应版本HTML成功访问；只提取包含候选方法名的表格和baseline段，随后人工核对上列6篇的明确同期对照、4篇的主表标签/脚注及比较边界。并非36篇所有实验/附录的穷尽审计；未列出的cross-comparison保持未核实，不判为不存在。

机械抽取已修正Math-OPD被误命中为H-OPD的边界问题；段落命中可能来自abstract/related work，不能据此创建实验比较关系。

证据：[原文表格/段落候选](../notes/mopd-baseline-audit.json)、[完整主表标签核对](../notes/mopd-baseline-table-checks.json)。没有运行实验、建立统一leaderboard、改36篇论文页或生成新idea。
