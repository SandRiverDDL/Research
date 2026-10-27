本轮复用此前的文献核查上下文，未参与候选生成；不是全空白审阅线程。已逐项阅读16项及证据文件，并补查原始来源。**没有发现足以支持 ABANDON 的完整方案精确覆盖。**以下是早期查新判断，未做实验，也未修改候选。

表中 **P＝PROCEED，C＝PROCEED WITH CAUTION**。所有公式原则上可计算；主要例外是 S7 的 `violation` 尚缺明确评分定义。判定针对现有方案，不代表效果成立。

| ID | 判定 | 最近工作与可核验的剩余 delta | 关键技术风险 | 最小决定性对照：同数据、同总成本 |
|---|---|---|---|---|
| **A1** | **P** | [semantic STOP](https://arxiv.org/abs/2609.20511)已有等价动作概率求和；新增的是**在student状态执行候选、据环境效应建立等价类**。不能claim求和原理首创。 | 即时效应相同不保证未来等价；少量teacher样本估计类分布很噪。 | 完全相同候选与执行结果，比较逐行动CE与集合质量目标；计入所有分叉。 |
| **A2** | **P** | [Skill-DisCo](https://arxiv.org/html/2606.26669)已有可执行条件控制流，但从成功trace离线编译外部技能；这里将**student状态上的teacher条件控制器训练进student生成策略**。 | DSL解释器可能贡献主要能力；未发生分支的teacher标签未必正确。 | 同一控制器全部分支展开后的action CE，与AST CE比较；部署计算量相同。 |
| **A3** | **P** | [MemOPD](https://arxiv.org/html/2608.07068v1)恢复评分接口；[MAPD](https://arxiv.org/html/2607.24280)已有结构化证据中间表示。剩余delta是**独立teacher证据指针实际约束行动上下文**。 | teacher-forced指针造成部署落差；下一步充分证据未必维持长期状态。 | 同一证据/行动标签：full-history、等长摘要、硬证据瓶颈；分别测oracle与预测指针。 |
| **A4** | **P** | [CROP](https://arxiv.org/abs/2608.13387)用counterfactual sensitivity选择token；关系蒸馏已有先例。这里直接转移**合法工具反馈干预引起的teacher行动log-odds变化**。 | 两状态KL已包含关系标签；关系项可能只是重新加权，长行动尺度不稳。 | 同一 \(h,h′\)、候选及teacher logprob，比较独立KL与差分关系项。 |
| **A5** | **C** | [AGGREVATE](https://arxiv.org/html/1406.5979#S2)、[LOLS](https://arxiv.org/html/1502.02206#S3)已有learner roll-in及候选rollout改进。剩余为独立teacher排序**student实执行短option**；与普通轨迹偏好学习的差异偏薄。 | 候选内softmax不约束候选外行为；短option偏好不一定改善最终任务。 | 同一options及排序：逐轨迹CE、偏好目标、token teacher监督；匹配分叉与训练量。 |
| **A6** | **P** | [MetaDistil](https://aclanthology.org/2022.acl-long.485/)已用更新后student反馈优化teacher；[SmartAD](https://aclanthology.org/2026.findings-acl.1349/)按student NLL选演示。这里**teacher固定，按独立自主迁移收益选择演示**，区别明确。 | 影子更新收益高方差，赢家偏差与选择集过拟合；正式样本效率可能抵不过选择成本。 | 同一K份演示，比较随机、NLL、当前成功率、更新后收益选择；必须含同总成本“全部演示”。 |
| **A7** | **C** | [Sub-goal Distillation](https://proceedings.mlr.press/v274/hashemzadeh25a.html)已覆盖teacher subgoal→planner/executor→无teacher部署。剩余只在**student实际实现路径上的在线goal-conditioned监督**，须证明贡献超过数据分布改变。 | waypoint可达性、预测与执行误差相乘；不能把层级结构本身claim新颖。 | 相同waypoint/行动标签，oracle-path训练与student-path训练；oracle/预测waypoint分别报告。 |
| **A8** | **C** | [SCoRe](https://proceedings.mlr.press/v306/lyu26j.html)已有teacher修复student错误；[DCR](https://arxiv.org/abs/2407.02397)已有学习refinement。剩余是**部署保留结构化edit policy**，单凭edit格式不足。 | edit太局部不能换策略，太自由则退化为完整重写；两遍推理混淆效果。 | 固定draft，同一修复标签转final-action或edit；比较等推理预算两遍重写，测误改率。 |
| **S1** | **P** | 与A1属**暂定同家族**，不是删除或合并结论；[semantic STOP](https://arxiv.org/abs/2609.20511)不覆盖执行验证的环境等价类。 | **候选内归一化对候选集合总概率质量不敏感**，训练可能只改变候选间排序而不提高自主生成。 | 同候选逐行动目标；除成功率，必须测候选集合的未归一化概率质量。 |
| **S2** | **C** | [MAPD](https://arxiv.org/html/2607.24280)已有plan/evidence JSON，[MemOPD](https://arxiv.org/html/2608.07068v1)已有memory机制。现方案主要是**常规OPD加结构化状态辅助CE**，算法delta偏薄。 | ledger部署不使用，正确预测不保证actor使用；辅助任务也可能抢容量。 | 相同actor数据、训练tokens：普通摘要辅助与ledger辅助；测实际状态错误及成功率。 |
| **S3** | **C** | 新发现[ContrAgent](https://arxiv.org/html/2609.18128)已有工具trace、可检查时序契约、DFA监督。其主要是在线gate/离线评估；剩余为**teacher条件契约产生偏好对并训练teacher-free策略**，尚未被精确覆盖。 | teacher偏好被误当必要条件；满足契约未必完成任务；偏好对稀缺。 | 同轨迹、同契约标签：普通成功偏好、契约偏好、continuation CE；评测时移除契约。 |
| **S4** | **C** | 与A4属**暂定同家族**；[CROP](https://arxiv.org/abs/2608.13387)非直接覆盖。但现公式可分解为**两个独立状态的pairwise分类loss**，没有显式跨状态关系约束，关系claim偏薄。 | 可能仅训练局部二选一；提高判别不保证生成正确action。 | 同反馈对与行动标签，直接比较独立CE、逐状态pairwise与所提目标，测完整生成。 |
| **S5** | **C** | 与A8属**暂定同家族**；[SCoRe](https://proceedings.mlr.press/v306/lyu26j.html)、[DCR](https://arxiv.org/abs/2407.02397)覆盖纠错训练大框架，剩余是显式patch执行策略。 | 与A8相同；开放edit表示还容易变成普通重写监督。 | 固定draft、同修复信息、同部署tokens：patch、全量重写、普通self-review。 |
| **S6** | **C** | [MetaDistil](https://aclanthology.org/2022.acl-long.485/)已直接以蒸馏后student反馈训练teacher；[SCOUT](https://arxiv.org/html/2609.38360#S3.SS2)/[Prep-OPD](https://arxiv.org/html/2610.04950#S3.SS3)已适配teacher。剩余是agent自主泛化收益及离散continuation优化；不能claim首次“teacher为学习收益优化”。 | 高方差outer reward；teacher可适配probe或单一student checkpoint。 | 同候选、影子更新、probe：固定teacher、teacher自身reward适配、learning-gain适配；外测任务完全隔离。 |
| **S7** | **P** | [PAIRED](https://arxiv.org/abs/2012.02096)已有对抗环境设计，[BranchOPD](https://arxiv.org/abs/2610.13481)已有student分叉；这里是**独立teacher依据当前意图选择合法反馈反例，并监督新student状态**。未见精确覆盖。 | `violation`评分尚未具体化；可能集中训练不自然异常，牺牲正常任务。 | 同一合法分支池、调用数及teacher标签：随机选择与teacher选择；外测自然异常和正常任务。 |
| **S8** | **C** | [LENS](https://arxiv.org/html/2609.33409#S4)已有hint与hint-free内化，[OLIVE](https://arxiv.org/html/2609.36246#S3.SS2)已有teacher continuation。独立teacher最终target符合scope；剩余是**teach-back使teacher标签改变且更可学**，仅替换self teacher不足。 | teacher可能本来就能直接给相同标签；额外交互只是更贵标注。 | 相同teacher tokens：直接标签、hint-conditioned标签、teach-back后标签；部署均无hint。 |

首轮优先最多三个家族：

1. **环境效应集合：A1/S1。**监督对象与token模仿的差异最清楚，且能用完全相同的数据隔离目标贡献。先核实确实存在大量安全可合并行动；S1的候选外概率问题必须显式测量。求和运算不构成原创性。
2. **反馈响应关系：A4/S4。**直接针对agent忽略工具反馈，合法分叉使因果假设较易检验。以A4的跨状态差分主张接受检验；S4保留原样作为同家族候选，其当前公式是否带来额外关系监督应由对照回答。
3. **更新后教学收益：A6/S6，优先A6。**这是高上限选项：若实际学习收益能稳定预测演示价值，会改变teacher监督的选择依据。A6先隔离固定teacher选择效果；S6额外训练teacher的贡献和成本另行验证，不能借MetaDistil已有原理包装首创。

其余均保留为**未经验证的储备候选**，不入首轮不是科学否定。查新只清除了目前已核实的精确重合风险；不等于数据库穷尽，也不替代后续pilot与外部审阅。
