# Gap Map

2026-10-15 重建。依据现有24篇论文；以下是库内证据支持的开放问题，不是全领域查新结论，也不是已选定的idea。原16个pending ideas不作为证据。

## 当前摘要

五个方法层面的gap，编号保留历史兼容性，顺序不代表排名：

- **G1｜错误恢复与交互成本。** 低成本prefix replay／短rollout与真实student错误状态覆盖之间，仍缺少可靠的兼顾方式；最终要改善自主恢复能力。
- **G2｜纠错与自主探索。** disagreement、confidence、teacher preference不能直接判定何时该纠错、何时该保留有效探索；选择性监督已有方法，剩余问题是让选择服务实际任务收益。
- **G5｜跨轮任务信用。** token／turn匹配、深度加权及OPD＋RL已有覆盖；开放问题是无专用solver时，如何把延迟任务后果变成有效的teacher监督，而非只更像teacher。
- **G6｜新程序知识迁移。** teacher会做不等于student能通过OPD学会；不同有效操作路径可能造成负迁移。需要区分已有规划模式强化与新技能获取。
- **G7｜多专家能力整合。** 路由、debate和顺序蒸馏已有覆盖；仍需在有限student容量与训练预算下，兼顾新增能力、旧能力保留和跨域组合。

**G3**拆为监督接口前提与G7，不再混作一个方法gap；**G4**改作全体gap共同的成本／评测约束。G1/G2有多篇直接方法证据；G6/G7有受控机制证据但真实环境外推有限；G5更偏研究假设。均不预设逐状态probe、环境分叉或额外judge是解法。

完整论据、已有覆盖、降级条件及24篇对应关系见下文；压缩query pack不能替代正文。

## 范围与判断口径

- **对象固定：** 19篇方法／技术报告、1篇框架、4篇基础背景，名单见[wiki索引](index.md)及[原调研](awesome-agentic-opd-review.md)。CAST是solver-teacher边界工作；Cross-Domain Hybrid OPD间接相关。4篇背景仅有摘要级阅读，不承担多轮机制结论。
- **证据层级：** 【事实】指作者方法或报告的观察；【解释】是本次跨论文判断；【开放问题】尚待验证。实验未复现；“库内未建立证据”不推出“无人做过”。
- **本次核查：** 阅读24页已有方法与边界记录，并回查TCOD、ReOPD、SAGE、ATOD、FutureBridge、TurnOPD、CAST、MemOPD、Top-K Drift、Planning Physics的原HTML相关章节。其余沿用wiki阅读记录。新增的Planning Physics §5.3知识错配证据直接引原文；不把整批论文标成全文精读。
- **方法论文口径：** gap必须说明训练中缺什么、现有方法覆盖到哪里、什么结果会让它不再成立。诊断帮助检验方法；单独做审计、换阈值或补公平排行，不自动构成新方法贡献。

## G1

### 在可承受交互成本下，学会从student自己的错误中恢复

**定位：状态分布与训练闭环。多篇直接方法支持问题存在；覆盖—成本边界尚未确定。**

【事实】TCOD通过F2B逐渐加深student rollout，B2F则先执行成功teacher前缀再移交student；两者仍有真实环境交互。ReOPD重放teacher histories，只自采样当前action且不执行它，作者明确承认轨迹池覆盖限制。两类方法改变的状态分布不同。[TCOD §4.2](https://arxiv.org/html/2604.24005v3#S4.SS2)、[ReOPD §§4、6](https://arxiv.org/html/2607.04763v3#S4)。

【已有覆盖】Guided-OPD、DASH-OPD已经研究混合执行和接管调度；TurnOPD已经自适应分配rollout深度。因此“从短到长”“teacher适时接管”“少跑一些无效turn”均不是尚无人覆盖的问题。见[Guided-OPD](papers/li2026_onpolicy_distillation_curriculum.md)、[DASH-OPD](papers/xia2026_dashopd_discrepancyaware_switching.md)、[TurnOPD](papers/zhou2026_turnopd_making_onpolicy.md)。

【解释】teacher-prefix训练可以提供可靠示范，却不会自然生成student错误action造成的新observation；截断或接管也会改变哪些恢复过程得到练习。这不证明这些方法缺乏恢复能力，但现有成功率不能单独回答它们如何学会恢复。

【开放问题】能否在有限在线交互与teacher预算下，持续获得并有效学习足够多的student-induced recovery经验，且训练后无需teacher接管？问题允许在线、复用或混合训练，不预设可重置环境。

**成立／降级条件：** 改进需要同时体现在自主完成任务和错误后恢复上，计入数据采集成本。若简单的现有replay＋online混合或课程基线已消除差距，就应缩小该gap；仅提升teacher-assisted rollout成绩不足以支持它。

## G2

### 让teacher纠错与student有效探索兼容

**定位：监督是否应当施加。方法证据多，但选择、加权与退火已很拥挤。**

【事实】SOD衰减高divergence step；ATOD保留高disagreement或高uncertainty turn，并逐步从OPD转向GRPO。它们的设置不同，不能仅凭权重方向判为矛盾。[SOD方法记录](papers/zhong2026_sod_stepwise_onpolicy.md)、[ATOD §§4.2–4.3](https://arxiv.org/html/2606.27814v6#S4.SS3)。

【事实】SAGE已根据环境失败反馈、teacher判断与预测置信度选择监督强度；FutureBridge已用student后续轨迹筛选teacher介入，但筛选指标是teacher-preferred token ratio。[SAGE §§3.3–3.5](https://arxiv.org/html/2606.19659v1#S3.SS3)、[FutureBridge §§3.2–3.3](https://arxiv.org/html/2608.01953v2#S3.SS2)。DGPO也已对错误预测施加teacher guidance，保留成功student行为，见[DGPO](papers/kotoge2025_can_compact_language.md)。

【解释】同一高分歧现象可能来自student错误、有效替代策略，或teacher对当前history不适用。上述代理能够有用，但其定义本身不保证区分这三种情况。teacher置信度高也不自动意味着纠正对任务有益。

【开放问题】如何使训练在纠正真实错误的同时保留有任务价值的student探索，并让这种选择在student逐渐变强后仍有效？目标是学到更好的自主策略；不要求对每个状态先做额外实验才能给监督。

**成立／降级条件：** 应同时体现错误减少与有效替代策略保留；仅KL下降、teacher偏好提高或supervision命中率提高不够。强对照包括选择性OPD、OPD退火＋RL以及错误条件teacher guidance。若只是换一个confidence／disagreement阈值，则属于已有路线的小改。

## G5

### 从局部模仿，走向能分配跨轮任务信用的蒸馏监督

**定位：监督目标与credit assignment。存在明确先例，当前属于需要进一步证实的研究缺口。**

【事实】TurnOPD已对turn进行归一化和深度加权；FutureBridge已考虑介入后的student行为。CAST则直接利用solver的cost-to-go构造turn级信号，并在特定假设下建立与OPD的联系。因此“首次turn-level监督”“首次考虑future”“首次value指导蒸馏”都不成立。[TurnOPD方法](https://arxiv.org/html/2607.05804v2#S5)、[FutureBridge §3](https://arxiv.org/html/2608.01953v2#S3)、[CAST §2.2及Appendix C.5](https://arxiv.org/html/2607.25308v1#S2.SS2)。

【解释】分配turn权重不等于辨认哪些先前决策造成了最终成功或失败；teacher偏好也不等同于任务价值。CAST提供了正面先例，但依赖可查询的专用solver。这一差距尚不能被描述成“token KL已被证明无法学习长程能力”。

【开放问题】在没有专用solver的文本工具环境里，如何把延迟任务后果转成有效、可规模化的teacher监督，使关键决策获得合理信用，同时允许不同的有效行动序列？需要说明teacher提供的知识如何帮助分配信用，才能与一般RL credit assignment区分。

**成立／降级条件：** 需要在同等reward和交互预算下，优于已有OPD＋RL、turn reweighting等强基线，且收益落在延迟后果或长程组合任务上。仅更换KL方向、加terminal reward，或为每个action生成大量未来分支，都不足以独立证明此gap已被解决。

## G6

### 跨越程序知识差异，而不只强化student已有的规划模式

**定位：单teacher下的知识可迁移性。受控失败证据具体，但外推范围有限。**

【事实】Planning Physics将planning pattern与procedural knowledge分开。在§5.3的合成crafting实验中，teacher与student掌握完成同一目标的不同有效recipe；高成功率teacher的OPD仍可能降低student原有表现，未顺利建立新知识。该结果来自人为控制的任务与知识差异，不能直接概括所有真实agent。[§5.3、Table 4、Figs.11–14](https://arxiv.org/html/2607.24720v1#S5.SS3)。

【已有覆盖】该论文已经识别知识错配；TCOD、Guided-OPD和ReOPD已改变student接触teacher知识的前缀或课程。因此“teacher更强却不好蒸馏”“加一个课程／teacher示范”不能单独作为新贡献。

【解释】G2问的是当前监督是否值得跟随；这里即使teacher指导正确，student也可能缺少实现它所需的程序知识。提高teacher可靠性或改善评分接口，并不能自动补齐这种能力缺口。

【开放问题】如何让OPD真正获取student原先不会的工具使用程序或技能组合，同时保留已经掌握的有效程序？关键区分是新知识获取、已有能力激活，以及对teacher表面路径的拟合。

**成立／降级条件：** 除受控知识错配外，应有真实文本工具任务中的迁移证据，并与teacher示范SFT＋普通OPD等基线比较。若差距完全由student缺乏基本可执行能力、任务条件不一致或简单cold start不足造成，该gap需缩小。更强student若已拥有目标知识，也可能使它失去主要价值。

## G7

### 在有限student容量下整合多个专家，而不牺牲已有能力

**定位：多个知识来源的联合学习。与G6的单teacher可学性不同。**

【事实】KAT-Coder-V2／V2.5和Mach-Mind-4-Flash已有领域路由专家蒸馏；MAD-OPD已有多teacher debate。技术报告的完整模型成绩支持这些配方可用，但不能隔离OPD或某种路由机制的独立效果。见[KAT-V2](papers/li2026_katcoderv2_technical_report.md)、[KAT-V2.5](papers/huang2026_katcoderv25_technical_report.md)、[Mach-Mind](papers/team2026_machmind4flash_technical_report.md)、[MAD-OPD](papers/wang2026_madopd_breaking_ceiling.md)。

【事实】Planning Physics在共享／兼容模式下观察到跨域迁移，在冲突模式下观察到顺序蒸馏遗忘；这是受控模板环境中的证据。[§§6.2–6.3、Tables 6–7](https://arxiv.org/html/2607.24720v1#S6.SS3)。Cross-Domain Hybrid OPD有能力恢复也有退化项，且其OPD作用于通用responses，不能当成逐步纠正搜索轨迹的证据，见[该论文记录](papers/chen2026_crossdomain_hybrid_opd.md)。

【解释】选对teacher与把其能力稳定并入同一个student是两件事；平均分提高可能掩盖少数领域退化。多teacher带来新知识，也引入共享参数上的冲突。

【开放问题】如何在固定student容量和可核算的训练预算下，使不同专家的互补知识可组合、冲突行为可区分，同时保留旧领域能力？需要处理知识整合本身，而不只增加teacher数量或推理时继续调用专家。

**成立／降级条件：** 应同时看新增域、旧域和跨域组合；对比单强teacher、简单多域混合／路由及顺序蒸馏，并计入专家成本。先排除G3的评分接口错误。若平衡数据混合或普通抗遗忘方法已解决问题，不能将通用continual learning效果包装成Agentic OPD独有贡献。

## G3

### 历史综合项：拆成监督接口前提与G7

旧G3同时包含“真实状态／决策信息是否保真”和“多teacher是否干扰”。本轮保留编号及已有关系，以免旧paper链接失去语义；多专家整合的当前问题见G7。

【事实】MemOPD已重建真实invocation的位置、mask与causal visibility，并实现共享前缀packing；Top-K Drift已分析关键决策token的support遗漏，并比较support restoration／teacher–student support union等处理。[MemOPD §§3.3–3.4](https://arxiv.org/html/2608.07068v1#S3.SS3)、[Top-K Drift §§3.1–3.3](https://arxiv.org/html/2607.07050v6#S3.SS1)。

【解释】本轮把这两项作为基线正确性的前提：teacher必须对实际执行时的context评分，压缩后的监督也要保留决策相关信息。不能把修复已知错误再登记成独立新gap。若研究低带宽、异构tokenizer或黑盒teacher接口，需要额外原文证据和查新；现有wiki不足以据此认定成熟选题。

## G4

### 全体gap共同的成本与评测约束

旧G4“统一总成本后收益是否稳定”保留为评价要求，不作为本轮独立方法方向。

【事实】ReOPD复用teacher轨迹可减少在线环境执行；TurnOPD调整rollout预算；FutureBridge增加候选介入验证；MAD-OPD引入多个teacher及debate。EasyOPD提供共同实现边界，但不会自动统一这些训练regime。见[ReOPD](papers/liao2026_multiturn_onpolicy_distillation.md)、[TurnOPD](papers/zhou2026_turnopd_making_onpolicy.md)、[FutureBridge](papers/chen2026_look_ahead_before.md)、[MAD-OPD](papers/wang2026_madopd_breaking_ceiling.md)、[EasyOPD](papers/sun2026_easyopd_easytouse_onpolicy.md)。

后续方法至少需要以下判断口径：

- **成本：** 分列student训练／生成、teacher生成／评分、环境交互、额外验证；既有teacher训练与轨迹池可按复用场景摊销，但须说明是否计入。额外流程若随每个状态或候选分支增长，需证明相应收益值得该开销。
- **训练和部署：** 主要终点是无teacher辅助的student任务表现；恢复能力、知识获取或旧域保留按对应gap选择，不用一个总平均数替代。
- **公平性：** baseline共享可比的初始化、teacher能力、数据、环境和预算；不同预算报告效果—成本曲线。checkpoint波动不能当独立训练seed方差。
- **长期价值：** 更强模型下仍成立的理由应具体落在环境分布、未知技能或有限容量上。仅小模型格式失败、固定阈值收益或特定backend错误，需要降低优先级。

## 24篇论文如何参与本次重建

以下列出证据角色；“相关”不等于该论文已经解决对应gap。方法细节和原文入口保留在各paper页，新增核查见上文直接引用。

| 论文 | 当前证据角色与边界 |
| --- | --- |
| [TCOD](papers/wang2026_tcod_exploring_temporal.md) | G1：深度课程与teacher warm start；不能把稳定KL等同自主恢复。 |
| [ReOPD](papers/liao2026_multiturn_onpolicy_distillation.md) | G1：低交互成本与固定prefix覆盖的边界。 |
| [Guided-OPD](papers/li2026_onpolicy_distillation_curriculum.md) | G1：混合执行课程已覆盖；不是空白。 |
| [DASH-OPD](papers/xia2026_dashopd_discrepancyaware_switching.md) | G1：自适应接管／归还已覆盖。 |
| [TurnOPD](papers/zhou2026_turnopd_making_onpolicy.md) | G1/G5：深度预算、turn加权已覆盖；G4成本对照。 |
| [SOD](papers/zhong2026_sod_stepwise_onpolicy.md) | G2：高分歧降权及与RL联合训练。 |
| [ATOD](papers/tan2026_atod_annealed_turnaware.md) | G2：保留高分歧／高不确定turn、OPD→RL退火。 |
| [SAGE-OPD](papers/zhou2026_sageopd_selective_agentguided.md) | G2：环境反馈＋teacher判断；已处理有效替代行为被过度约束的问题。 |
| [FutureBridge](papers/chen2026_look_ahead_before.md) | G2/G5：未来验证已覆盖，筛选目标仍是teacher-relative proxy。 |
| [DGPO](papers/kotoge2025_can_compact_language.md) | G2：错误条件teacher guidance；只适用于已读文本RAG设置。 |
| [CAST](papers/wang2026_cast_game_solvers.md) | G5：solver提供turn价值的已有先例；不等于一般LM teacher。 |
| [Planning Physics](papers/men2026_physics_multiturn_longhorizon.md) | G6/G7：程序知识错配与多teacher冲突；机制证据来自受控合成环境。 |
| [KAT-Coder-V2](papers/li2026_katcoderv2_technical_report.md) | G7：路由专家整合；完整模型分数不是OPD独立消融。 |
| [KAT-Coder-V2.5](papers/huang2026_katcoderv25_technical_report.md) | G2/G7：漂移后缀处理与领域专家整合，配方贡献未完全分离。 |
| [Mach-Mind-4-Flash](papers/team2026_machmind4flash_technical_report.md) | G7：多专家与composition ablation；不能概括必然正迁移。 |
| [MAD-OPD](papers/wang2026_madopd_breaking_ceiling.md) | G7：debate已有覆盖；增加teacher数量及轮数有成本。 |
| [Cross-Domain Hybrid OPD](papers/chen2026_crossdomain_hybrid_opd.md) | G7间接证据：通用能力保持，不是搜索轨迹逐turn OPD。 |
| [MemOPD](papers/liu2026_memopd_onpolicy_distillation.md) | G3：真实invocation对齐是监督有效性的前提。 |
| [Top-K Drift](papers/shen2026_when_topk_misses.md) | G3：保留概率质量不保证保留决策监督。 |
| [EasyOPD](papers/sun2026_easyopd_easytouse_onpolicy.md) | G4实现基础；共享backend不构成公平性证明。 |
| [GKD](papers/agarwal2023_onpolicy_distillation_language.md) | 背景：student自采样及divergence选择已有基础。 |
| [MiniLLM](papers/gu2023_minillm_onpolicy_distillation.md) | 背景：reverse-KL OPD已有基础。 |
| [SKD](papers/xu2024_speculative_knowledge_distillation.md) | 背景：token级交错采样，不直接证明多轮恢复。 |
| [Survey](papers/song2026_survey_onpolicy_distillation.md) | 分类导航；摘要级阅读不提供新的机制证据。 |

## 旧gap迁移与证据缺口

| 旧项 | 本轮处理 |
| --- | --- |
| G1：rollout深度与监督可靠性 | 保留ID，收窄为错误恢复覆盖与交互成本；可靠性选择归G2。 |
| G2：高disagreement的意义 | 保留ID，改为纠错和有效探索的训练问题；跨轮信用另列G5。 |
| G3：评分接口＋多teacher干扰 | 保留历史入口；接口作为前提，多专家整合另列G7。 |
| G4：统一成本与协议 | 保留为所有方法的评价约束。 |
| 原先未单列的知识迁移 | 根据Planning Physics §5.3新列G6，明确合成环境边界。 |

【证据缺口】G5尚缺少统一条件下“局部模仿不足”的直接比较；G6/G7缺少对真实工具环境的充分外推；G1/G2缺少共同预算下的恢复／探索分解。三者都不能靠补一句“需要更多实验”变成已验证创新点。

【后续边界】本次完成gap重建与关系登记。没有选择具体方法，没有把旧idea升级为推荐，没有启动新一轮idea生成、全领域查新或实验。
