# 本轮查新证据与覆盖边界

日期：2026-10-14。事实来自原论文，候选差异是待评审解释。搜索命中不等于全文核验；未发现不等于不存在。正式24篇文献见 [已有综述](../research-wiki/awesome-agentic-opd-review.md)。本轮补查的邻近工作留在此证据表，不自动混入此前仓库筛选统计。

| 工作 | 已核实的机制 | 阅读与来源 |
|---|---|---|
| OLIVE | student执行k轮，teacher接管M轮；student/observation tokens被mask，仅teacher动作CE。普通student-prefix→teacher续写已有直接agent方法。 | HTML摘要/引言、[§3.1–3.2](https://arxiv.org/html/2609.36246#S3.SS2) |
| SCOUT | teacher在student prefixes上生成完整continuations，以这些teacher continuations的outcome reward做周期RL；student保持OPD。不是直接优化student学习后的独立表现。 | HTML摘要/引言、[§3.2](https://arxiv.org/html/2609.38360#S3.SS2) |
| Prep-OPD | 先在初始student固定prefixes上RL训练teacher完成题目，再冻结teacher做bounded handoff和全混合轨迹OPD。 | [§3.1–3.3](https://arxiv.org/html/2610.04950#S3.SS3) |
| Relay-OPD | teacher top1为reflection token而student top5中没有reflection token时接管；生成有限段落后交回student。 | [§3.2](https://arxiv.org/html/2607.26057#S3) |
| AC-OPD | student anchors处teacher续写，以teacher uncertainty和teacher/student path discrepancy选择监督长度；数学/代码。 | HTML摘要/引言及[方法节](https://arxiv.org/html/2609.22254#Sx5) |
| R2-OPD | 对span的独立progress与teacher reward分别排序，冲突时屏蔽distillation reward。 | HTML摘要/引言；[原文](https://arxiv.org/html/2608.19408)；本轮未完整读方法 |
| Counterfactual Recoverability | 原摘要说明teacher continuation与rollback分支预算匹配比较，按recoverable/irreversible/ambiguous分配保留、回滚或普通监督。 | [原arXiv摘要](https://arxiv.org/abs/2608.04408)；HTML404，细节未核实，不能据此断言完整重合 |
| CROP | 用paraphrase校准counterfactual prompt sensitivity，选择task-relevant tokens。 | [原摘要](https://arxiv.org/abs/2608.13387) |
| BRTS | 多teacher rollouts按正确性优先、student alignment其次选轨迹；额外teacher-context loss。 | [原摘要](https://arxiv.org/abs/2605.09725) |
| CLOOPD | 固定已评分batch/advantage，重复student actor passes，按realization和token budget分配学习。 | [原摘要](https://arxiv.org/abs/2609.24141) |
| LENS-OPD | teacher hint→同一student的有/无hint分叉；用teacher likelihood验证未来；hinted student分布向hint-free student KL内化，加horizon/token控制。 | [§4.3–4.5](https://arxiv.org/html/2609.33409#S4)；内化分支含self-distillation，不作本项目候选机制，但查新仍需比较 |
| AGGREVATE | learner roll-in，探索action，再由expert rollout估cost-to-go；用cost-sensitive学习更新learner。 | [§2.2](https://arxiv.org/html/1406.5979#S2) |
| LOLS | learner roll-in、reference/learner混合rollout，学习相对reference及自身one-step deviations的改进。 | [§3、Table1](https://arxiv.org/html/1502.02206#S3)；算法细节仍需按候选进一步查 |
| Distilling Policy Distillation | 分析student-driven distillation目标/梯度与收敛，不能把长期KD loss-to-go本身宣称全新。 | [AISTATS2019官方摘要](https://proceedings.mlr.press/v89/czarnecki19a.html)；未读全文 |

## 检索记录（实际检索词的主题归并）

- landscape：agent on-policy distillation September October 2026；multi-turn distillation student recovery；OPD counterfactual；OPD continuation teacher student；agent distillation state equivalence；agent distillation cost-to-go。
- 方法邻近：teacher student handoff distillation；agent OPD subgoal；learner aware teacher student continuation reward；OPD memory sufficient；OPD environment equivalence。
- 定名复核：OLIVE、SCOUT、AC-OPD、R2-OPD、CLOOPD、AGGREVATE、LOLS的原论文。
- 来源覆盖：公开Web search，原arXiv HTML/abs、PMLR官方论文页、部分OpenReview检索命中。没有独立登录Google Scholar/Semantic Scholar API；不能声称数据库穷尽查新。社区清单/聚合站仅发现入口，结论引用原文。
- Overtaught, Underlearned (2610.16543)只出现搜索摘要，但原abs打开404，暂不作为肯定的新颖性否定证据。

## 候选机制相关的进一步检索

- 教师选择student options / waypoint：检索 `language agent knowledge distillation teacher subgoal student generated options 2024 2025 2026`、`on policy distillation teacher selects student candidate action options`、`hierarchical imitation learning teacher waypoint student reachability distillation`。
- 以student更新后收益选监督：检索 `knowledge distillation teacher demonstration selection student learning progress meta gradient`、`language model agent distillation post update student performance teaching`、`machine teaching demonstrations learner gain bilevel policy distillation`。
- 环境等价类：检索 `agent distillation action equivalence`、`policy distillation transition distribution`、`imitation learning equivalence classes actions`。主要检索到经典policy distillation/implicit imitation，未凭这些负面搜索结果宣布新颖。
- 分支程序：检索 `language agents distillation conditional plans`、`agent distillation branching policy`、`agent distillation program synthesis`。
- 证据瓶颈与反馈响应：检索 `agent distillation evidence bottleneck`、`memory distillation action sufficiency`、`agent teacher tool feedback distillation`。

| 补充近邻 | 已核实内容与差异检查点 | 原始来源/深度 |
|---|---|---|
| SCoRe | student轨迹首个错误由teacher修复，先SFT，再从verified prefix做短程RL。重新从错误前状态训练的笼统主张已覆盖。 | [ICML2026官方摘要](https://proceedings.mlr.press/v306/lyu26j.html)；arXiv2509.14257 |
| Sub-goal Distillation | teacher给oracle路径标subgoals，训练planner/executor，部署无teacher。仅从动作换成subgoal且去掉teacher，不能自称新颖。 | [PMLR官方摘要](https://proceedings.mlr.press/v274/hashemzadeh25a.html) |
| SmartAD | 多条正确teacher轨迹按student NLL选最易学者，action/final spans加权。 | [ACL2026 Findings官方摘要](https://aclanthology.org/2026.findings-acl.1349/) |
| MetaDistil | 通过蒸馏后student的反馈meta-learn teacher。post-update feedback本身已有经典KD工作，agent交互中的具体增量要独立论证。 | [ACL2022官方摘要](https://aclanthology.org/2022.acl-long.485/) |
| BranchOPD | 依据uncertainty/disagreement在共享student prefix重新采样多个student continuations，逐token teacher监督；含agent within-turn branching和protocol repair。 | [原摘要](https://arxiv.org/abs/2610.13481) |

补充原文摘要：
- [Skill-DisCo](https://arxiv.org/html/2606.26669)：从成功traces提取PFSM控制流子图并编译成可调用程序技能，部署策略/工具表示已有先例；本轮读摘要，方法未全读。
- [MAPD](https://arxiv.org/html/2607.24280)：offline多agent生成任务/计划/证据JSON，实际KD target是privileged student branch。属于self-distillation邻近，不纳入本项目候选，但结构化证据中间表示已有人研究。
- BranchOPD与SCoRe另核对了原HTML摘要；其方法章节分别为§4。

运行边界：生成阶段新增第三agent及唤醒旧文献agent均被runtime以 `agent thread limit reached` 拒绝；已保留两个模型各自的独立上下文，每个覆盖两个lens。不是四个fresh lens contexts。后续独立复核是否可启动需以实际工具结果记录。

- 工具反馈条件关系：实际搜索 `agent distillation observation contrastive`、`tool distillation counterfactual observations`、`policy distillation response relational`；尚未找到已核实的同一目标/同一设置直接覆盖。
- 编辑策略：实际搜索 `agent teacher edit on-policy distillation`、`student proposal correction distillation agent`、`distillation edit operator`；检索命中Online Speculative Decoding、编辑/纠错轨迹训练等近邻，不能仅以显式edit格式自称新颖。
- 已复用一个此前做论文核查、未参与本轮生成的文献agent准备复核；其已有文献上下文保留，因此不是全空白fresh线程。新的Astra reviewer spawn仍被线程数限制拒绝。

## 查新判定口径

本轮没有把“近邻多”当作淘汰依据。对16个原始候选逐项核对：独立teacher的实际监督对象、student state来源、更新公式是否可计算、最近方法已覆盖的部分与剩余delta。相近候选保留不同ID与原始模型来源；比较视角可以聚类，但不在质量评审前删除。只有具名原论文已含完整核心方案，才能按novelty判ABANDON。缺少实验、预算不明或只是没有分到首轮pilot，不写成实验失败或无新颖性。

资源估算只是假设：1.7B以下student、4B–8B teacher。多数生成器给的是工程人周与调用量，不能把它们误当GPU周或GPU小时。当前没有经过实测速率校准的GPU成本，故不以“可能复杂”触发客观预算淘汰。

关键新增近邻：[When EOS Tokens Disagree](https://arxiv.org/abs/2609.20511)，原摘要已核实：把功能相同EOS作为同一semantic stopping action处理。环境效应集合候选不能把“等价动作概率相加”本身宣称首创；剩余delta需是student状态上的执行验证等价关系及其完整agent学习收益。方法公式待进一步核。

后续原文核验：
- Semantic EOS的[§3.2 Fix 3](https://arxiv.org/html/2609.20511#S3.SS2)明确对teacher与student分别定义 `p(STOP|h)=Σ_e p(e|h)`，再把聚合概率代入原OPD更新。已读方法公式，不再只是摘要证据；环境动作候选A1/S1的求和操作本身明确已有先例。
- [Relational Knowledge Distillation，CVPR2019官方摘要](https://openaccess.thecvf.com/content_CVPR_2019/html/Park_Relational_Knowledge_Distillation_CVPR_2019_paper.html)：转移样本之间的关系，具体为距离/角度loss。A4/S4不能将“跨样本关系蒸馏”本身宣称新颖；可讨论的具体差异是合法环境反馈变化与动作偏好响应，在student真实访问状态上的配对监督。只读官方摘要，未核全文及后续全部变体。

独立于本轮生成的文献reviewer补核（保留其原文核查来源）：
- [ContrAgent: Symbolic Temporal Supervision of LLM Agents Using Contracts](https://arxiv.org/html/2609.18128)，§5.1–5.2：工具trace转checkable predicates，再转LTLf contracts/DFA，用于在线约束与离线轨迹评估。S3不能把temporal contracts用于agent监督本身宣称全新；其余差异是teacher条件契约作为偏好训练信号，最终更新student参数、部署不带契约监督器。本轮未据此判定完整方案已被覆盖。

候选公式核查（解释，不是实验）：S4给出的两个log-sigmoid项可分别归属h/o1与h/o2，数学上就是两个状态内的二分类交叉熵，并无跨状态耦合项；A4则有显式差分差异。S1、A5在有限候选集内归一化，只约束条件偏好，不能单凭该目标保证部署时把足够概率放在候选集合。原始候选公式保留，未静默修正。
