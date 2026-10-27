# 可迁入 Agentic OPD 的 stepwise 操作 pattern

> 用户已纠正：领域／目标谱系不构成所需交付。**先读§0的OPD接口迁移筛选**；§1–12保留为来源池，不作为用户认可的方法方案。所有迁移均未验证收益或最终新颖性。

> 2026-10-19；机制调研。面向通用、white-box、文本多轮 Agentic OPD。这里的 step 指一次 agent response／工具交互决策；推理论文的文本 step 与环境 turn 不自动等价。
> 【事实】描述原方法；【迁移解释】描述可借鉴的结构，不是已验证的新方法。未做训练、代码复现或完整新颖性检索。优先复用已有 student rollout、teacher 前向和环境反馈，明确额外生成及阻塞依赖。

## 0. 用户纠正后：以OPD训练接口筛机制

### 0.1 迁移必须落到实际改动

基线：student自主多轮rollout，teacher对已生成tokens做批量前向，蒸馏信号通常含 `d_tj=log p_T(y_tj|prefix)−log p_S(y_tj|prefix)`；有task reward时再与RL组合。只列原论文目标、给step乘任意scalar、或改训练对象但不说明如何接回这个闭环，都不能算完成迁移。

以下是**迁移草案**，不是原论文已验证的OPD实现。按“可明确接入／需新信号／只宜作对照”分层；不是用户已选idea。

| 来源机制 | OPD里具体改什么 | 复用信号、增量成本 | 能回答的缺口与边界 |
|---|---|---|---|
| **WEPO的结构化候选对比 → action候选分布蒸馏** | 从student已有tool call出发，用schema/可选对象构造少量合法但含义不同的action；teacher/student各自对相同候选强制评分，把候选内softmax分布做KL，作为原OPD辅助项 | 已有history、tool schema和teacher；不新增自回归候选生成/环境执行，但每个候选都增加teacher及student评分，batch不代表免费 | 直接比较工具选择/关键参数，减少纯措辞监督。候选集内分布是序列分数代理，不是真实语义动作边缘分布；工具参数须可枚举，teacher偏好也不保证正确。[WEPO §3](https://arxiv.org/html/2412.10742#S3.SS2) |
| **clean-view distillation → teacher评分上下文去污染** | student照常读完整history并生成reasoning/action；teacher评分action时保留公开任务/历史动作/工具反馈，去掉student内部reasoning。训练的action token不变，teacher条件输入变 | 复用一次rollout；若替换action监督的teacher pass，不需teacher生成；若保留原全文OPD又加clean view，则增加一次前向 | 避免teacher被student错误thought牵引。去掉thought也可能令teacher缺少计算支撑，条件策略变了，必须验证。来源SecOPD为同初始化自蒸馏/generic邻近方法，此处只借clean/attacked条件分离，改为独立外部teacher是迁移解释。[SecOPD §4](https://arxiv.org/html/2608.21500v1#S4) |
| **NoisyAgent/PAFT的异常状态训练 → 恢复状态上的OPD** | 把原本会采的一部分episodes放到带失败/截断/接口扰动的环境；student在受扰状态自主续跑，teacher对这些真实prefix评分。监督改为当前状态可执行的恢复动作；已有RL时clean/noisy各自算RL advantage | 不要求同一状态成对分叉；增加扰动构造、重试和可能更长的轨迹。不能从clean轨迹篡改observation后照抄后续action冒充on-policy | 直接补student错误/异常prefix的监督覆盖，而非只降低这些位置权重。须保持环境一致、任务可解与teacher恢复能力；fatal state需停止目标。[NoisyAgent §3](https://arxiv.org/html/2605.27209v1#S3)、[PAFT §6.1](https://arxiv.org/html/2607.01084v1#S6.SS1) |
| **iStar隐式step reward → OPD＋局部task credit** | 原student成功/失败轨迹pairs训练implicit PRM；由其对每turn给step reward，用于RL通道的局部advantage；原teacher token蒸馏保留 | 不新增逐状态环境分支/step标签，但需已有outcome对比、额外PRM训练和前向。单条轨迹不能凭空提供偏好 | 让同一失败轨迹中的turn不必共享一个终局RL系数；不能把signed step advantage直接当负KL权重。优先级取决于是否接受额外learner成本。[iStar §3.1](https://arxiv.org/html/2509.19199#S3.SS1) |
| **DeLoop日志自监督 → 局部anti-loop偏好辅助OPD** | 在已有student日志中挖重复action与后续恢复action，形成局部DPO辅助项：`L=L_OPD+alpha L_local-pref`，原rollout机制不变 | pair mining可复用日志；增加chosen/rejected及reference评分，无需teacher生成。仅保留恢复action在旧状态可执行、所需信息当时已可见的样本 | 提供原teacher逐token评分未显式表达的“避免循环”训练约束。原DeLoop将后来action搬回旧history是弱监督；状态/证据改变时不能直接搬，故是条件性迁移，不是通用免费插件。[DeLoop §4](https://arxiv.org/html/2610.19376#S4) |
| **EntroPO的熵/约束分离 → 改OPD局部目标形状** | 固定prefix下用`KL(p_S||p_T)−lambda H(p_S)`替代纯KL；等价于对teacher分布做温度软化并改变整体尺度 | 若已有完整分布，主要为概率算术，无额外rollout；仅sampled log-prob时须说明entropy estimator | 防策略过早集中；不是动作级多样性的保证。这是成熟温度/熵基线，单独迁移不足以声称方法创新。[EntroPO §3](https://arxiv.org/html/2509.12434#S3.SS2) |
| **RETA分通道标准化＋R²质量守恒 → OPD/RL尺度解耦** | OPD与task-RL通道分别控制尺度再混合；step gate前后固定蒸馏系数质量，避免同时改变位置分配与总强度 | 复用既有advantage/outcome，主要为算术；不增生成 | 是判断step reweight收益来源的必要对照，不直接解决teacher正确性或时间信用，不包装为独立创新。[RETA §4](https://arxiv.org/html/2606.15441v1#S4.SS2)、[R²-OPD §4](https://arxiv.org/html/2609.35517#S4) |

### 0.2 action候选蒸馏的最小定义

对同一个decision prefix `h`及候选集合`C={a1,...,aK}`，定义已规范化action字符串的序列分数 `s_M(ai|h)=sum_j log p_M(ai_j|h,ai_<j)`，以及 `q_M(i|h,C)=softmax_i(s_M/temperature)`。辅助目标为 `KL(q_T||q_S)`。所有候选都已给定，teacher/student用teacher forcing评分；不需要teacher自己decode候选。

这是**有限候选集的序列偏好蒸馏**，不是ActionOPD原始语义等价类概率；候选覆盖、不同长度与参数表示偏差仍要处理。WEPO原方法是有标注正负动作的DPO；把二元硬偏好换成teacher软分布是本次迁移解释，不能写成WEPO已有结论或已查新贡献。

### 0.3 暂不算直接可搬的方法

- HPL/SDPO的完整局部偏好构造、CSO的成功suffix验证：缺少局部labels时要额外MC/teacher/PRM/环境分支，不能靠“按turn求均值”就说搬了原方法。
- CoBRA的双路线counterfactual：核心证据依赖强制分支；没有该证据时不能用entropy替代工具收益。
- ARLAS/RETA完整attacker训练、MCMA完整memory-copilot训练：会新增一套训练闭环；其目标类别或优点不是对当前OPD的直接修改。
- DEPO/WebThinker成本偏好：若仅把少steps当优质teacher监督，没有处理正确性与student状态覆盖，就未完成向OPD的迁移。

本次纠正核查：candidate KL的概率定义及熵温度等价只做CPU数学检查；没有训练结果、完整查新或独立方法评审。§1–12继续作为来源记录，不能把论文数量当可迁移机制数量。

### 0.4 用户指定三个最近邻后的迁移清单

用户本次限定teacher-guided/interactive imitation、process supervision/credit assignment、agentic preference optimization。下面只给接入OPD闭环的操作。来源事实与迁移解释分开；没有新的训练/查新结论。

| 近邻／来源 | 来源原机制【事实】 | 接入OPD的具体位置【迁移解释】 | 成本／前提 |
|---|---|---|---|
| Teacher-guided：**SafeDAgger**，Jiakai Zhang & Kyunghyun Cho, 2016，[§3.1–3.2](https://arxiv.org/html/1605.06450#S3.SS1) | 学safety policy，从learner特征预测是否偏离expert，不先查询expert；选择需要标注的状态 | 用历史OPD日志训练轻量query head，在昂贵teacher前向前筛turn；只搬查询选择，不默认搬teacher接管 | 增加head训练/前向并需刷新；预测的是deviation，不保证teacher可靠或该步有task价值。原场景为自动驾驶，仅作经典机制邻居，不纳入文本agent正式paper集 |
| Teacher-guided：**SCoRe**，Yuanjie Lyu et al., 2025/ICML2026，[§4.2–4.3](https://arxiv.org/html/2509.14257#S4.SS2) | student先跑完整轨迹；失败后teacher定位并纠正最早错误，student再续跑，可重复纠正；收集修复轨迹SFT，后续从已验证prefix做短程RL | 对失败episodes低频收集局部正向纠正目标，作为原OPD的辅助SFT/forward-KL数据；另可从该prefix专练弱点 | teacher judge、纠正生成和suffix续跑均有成本，不是只做一次forward；stateful环境必须可还原真实状态。原动作是code，不把文本prefix重放当环境重置 |
| Process credit：**GiGPO/HGPO**，[GiGPO §4.2–4.3](https://arxiv.org/html/2505.10978v3#S4.SS2)、[HGPO §4](https://arxiv.org/html/2602.22817#S4) | 已有rollouts按重复state/历史归组，用return-to-go构局部relative advantage | 在OPD＋RL中保留teacher token信号，将task通道改为episode advantage＋局部state-group advantage，广播到该turn tokens | 不新增局部分支或critic；需已有grouped trajectories、可靠outcome和可比状态。不能给纯OPD无reward设置凭空加出task credit；负advantage不直接乘KL |
| Process credit：**iStar**，[§3.1](https://arxiv.org/html/2509.19199#S3.SS1) | 用现有outcome trajectory pairs训练implicit PRM，再产生action-level step rewards | 保留原OPD，使用learned step reward计算RL通道局部advantage；可用于难找到重复state时 | 没有额外step标签/局部分支，但增加PRM训练与评分；学到的相关credit不保证因果贡献 |
| Preference：**WEPO**，[§3.1–3.2](https://arxiv.org/html/2412.10742#S3.SS2) | 同网页/意图，用DOM结构构造混淆element负例，做局部DPO | 借结构化候选构造：对同history的候选tool actions强制评分，蒸馏teacher候选内soft偏好；具体定义见§0.2 | 无需teacher decode或实际执行负例，但增加teacher/student候选前向；原WEPO有人工正确动作，soft-teacher替代是迁移草案，不能称原文已验证 |
| Preference：**ToolPreference/TP-LLaMA**，[§4.2](https://arxiv.org/html/2406.07115#S4.SS2) | 从已有成功/失败搜索树提取同父节点的sibling action pairs，局部DPO | 若已有搜索树，可在原OPD外加局部pair loss，训练actor在相同prefix区分两动作 | 挖pair不需新rollout，但树生成成本已发生；普通线性日志没有siblings，不能假设免费获得；paired loss需额外评分 |
| Preference：**DeLoop**，[§4](https://arxiv.org/html/2610.19376#S4) | 单rollout循环动作与后来打破循环动作组成局部DPO pair | 原OPD＋anti-loop偏好辅助；即使最终失败，仍可从局部恢复获得训练信号 | 无新teacher生成/局部分支；后来动作必须能在旧状态执行且不依赖未来信息，否则不接受该pair |
| Preference：**HPL/SDPO-social**，[HPL §3.3–3.5](https://arxiv.org/html/2510.03253#S3.SS3)、[SDPO §3.2–3.3](https://arxiv.org/html/2501.01821#S3.SS2) | 以语义action-group/等轮数交互片段构偏好，HPL另有长度与reward-gap课程 | 仅在已有片段质量标签时，将辅助偏好目标从整轨迹缩到局部行为组；保留其history条件 | 原造数需MC后缀或judge/完整session。只有turn边界或KL大小不足以恢复原方法的局部质量标签 |

【迁移优先级判断】若当前骨架为ATOD/SOD式OPD＋RL、已有多轨迹outcome，先看GiGPO/HGPO的局部参照；若目标是action-level，先看WEPO的结构候选＋soft teacher评分；若瓶颈是teacher前向预算，先看SafeDAgger式预查询head。SCoRe可提供真正纠正目标，但原pipeline更贵；iStar增加learner模型成本。以上均为机制筛选，不是用户已选idea或新颖性认证。

【与现有OPD的重叠】监督选择、prefix课程和局部teacher纠正已有SAGE-OPD、TCOD、SOPD等邻近覆盖；不能仅迁移“筛turn／短horizon／teacher修正”就声称新贡献。没有state重现、outcome pairs或局部正负标签时，必须按实际缺口降级，不能用disagreement冒充这些信号。

## 1. Agentic OPD 是否常做 stepwise reweight？

【事实】这是已有方法的一条明显路线，但没有做全领域计量，不能说多数方法都如此。SOD 按 turn 内 sampled-token log-prob gap 调整蒸馏强度；ATOD 的 T-DUR 联合 disagreement 与 student uncertainty；TurnOPD 调整 turn 的 loss budget。三者都不是新的语义 action 分布。[SOD §4.2](https://arxiv.org/html/2605.07725v3#S4.SS2)、[ATOD §4.3](https://arxiv.org/html/2606.27814v6#S4.SS3)、[TurnOPD §5.2](https://arxiv.org/html/2607.05804v2#S5.SS2)

【关键区别】SOD 对上升的 mismatch 衰减监督；ATOD 保留高 disagreement 或高 student uncertainty 的 turn。相同统计量在不同假设下能产生相反操作：不能把 disagreement 本身当 teacher 可靠性、动作价值或可学习性的通用标尺。

【解释】stepwise 至少能改变六个对象：监督粒度、参照组、正负目标、训练位置分布、目标上下文、损失预算。只写 `sum_t w_t loss_t` 会把这些机制压扁。

## 2. Pattern 对照表

成本以“已有常规 OPD rollout 和 teacher 评分”为参照。没有新增 rollout 不等于没有新增模型前向；group 方法还要求本来已有足够轨迹和重复状态。

| ID | 可搬的操作 | 代表原方法 | 需要已有的信号／数据 | 增量成本与迁移前提 |
|---|---|---|---|---|
| P1 | 按 turn／segment 分配固定监督预算 | TurnOPD | turn 边界、已有 token loss | reducer／聚合很轻；完整 TurnOPD 的深度 probe 另算 |
| P2 | 按任务结果校准 teacher 更新方向，保留总监督强度 | R²-OPD | 原 OPD advantage、终局 verifier outcome | 有现成 outcome 时主要为算术；原实验是数学 reasoning |
| P3 | 对既有轨迹中的可比状态做局部相对比较 | GiGPO、HGPO | 多轨迹、重复状态／历史、return-to-go | 事后归组，无新增分支／critic；singleton 不产生对比 |
| P4 | 在 turn 边界估计 TD／GAE | Turn-PPO | transition、reward、训练好的 value critic | 不新增环境分支，但新增 critic 前向和训练 |
| P5 | 将子目标选择与段内执行分别分配 credit | HiPER | 原生 plan／switch 边界、高低层 value | 原方法双层 critic、额外规划输出；不适合无改动套 flat agent |
| P6 | 同 prefix 的局部动作偏好／hard-negative mining | Agentic-DPO | 专家状态和动作、student 局部负例 | 单步生成和双侧打分；不执行负例、不生成 suffix |
| P7 | 首错局部化；坏 prefix 作 context，只学修复 | Step-DPO、Agent-R | 首错位置、同 prefix 的修正／可执行修复轨迹 | 原构造分别需完整 suffix 采样或 MCTS，适合离线摊销 |
| P8 | 按工具观察的边际预测收益筛选调用 | Toolformer | 调用与返回值、固定真实 suffix | 打分是多条件前向；构造候选和执行工具另算 |
| P9 | 改采样／重放位置，而不只在算完后乘权重 | PER、ReOPD | pool／buffer、priority、policy version | buffer 调度轻；旧状态分布、staleness 与校正不可省略 |
| P10 | 将已有 action 的优势转成非负回归权重 | AWR | 轨迹 return、value baseline | 不新增局部分支，但需 value 拟合；不是直接复制负 advantage |

## 3. 原机制、迁移与边界

### P1：监督预算的单位——token → turn

【事实】TurnOPD 将 token-mass 权重 `q_t=n_t/sum(n)` 与 turn-uniform 权重 `1/T` 随训练进度插值；这是 loss allocation。其 adaptive horizon controller 是另一个组件，需要周期性 full-depth probes。[§5.1–5.2](https://arxiv.org/html/2607.05804v2#S5.SS2)

【迁移解释】原 rollout 不变，先把每轮 token loss 求均值，再决定轮间预算，可防长 reasoning 自动压过短工具决策。这改变训练单位，没有得到动作语义等价，也没有识别因果贡献。【边界】只搬 reducer 的开销很小；深轮样本少时，强行均衡会放大噪声。不能把完整方法称为零新增采样。

### P2：校准方向，区分再分配与整体降权

【事实】R²-OPD 用 outcome 符号与原 OPD advantage 的一致性构造 sigmoid gate，再归一化，使每条 response 的 `sum |advantage|` 保持原值。它不翻转原 advantage 的符号。[§4，Eq.13–16](https://arxiv.org/html/2609.35517#S4)

【迁移解释】可以借“既有任务结果校准 teacher 信号，同时固定监督预算”的结构，避免将整体减弱 OPD 误判为更好的 step 选择。【边界】原验证是数学任务，迁到工具 turn 尚未验证；终点成功不能证明每步正确，失败也不能把所有动作判错。若原流程没有 verifier，新增判分需计费。

### P3：从现有 rollout 提取可比组

【事实】GiGPO 将同任务、重复 environment state 的已采样动作归组，按已实现的 return-to-go 计算局部 relative advantage，叠加 episode advantage；无额外 rollout。HGPO 进一步按最近历史状态构造嵌套组，以缓解仅看当前状态的混淆。[GiGPO §4.2–4.3](https://arxiv.org/html/2505.10978v3#S4.SS2)、[HGPO §4](https://arxiv.org/html/2602.22817#S4)

【迁移解释】可借局部参照组，校准某 turn 的统计，而不在每个状态再采 teacher/student 候选。【边界】需已有 grouped trajectories 与状态重复；同 observation 不等于同 belief。实际未来回报仍受后续策略影响，不是动作的隔离因果贡献；严格历史匹配会令组很小。

### P4：用前后状态的 value 差提供时间信用

【事实】Turn-PPO 将整次 response 当 action；critic 在 turn 边界估值，使用 `delta_t=r_t+gamma V_{t+1}-V_t` 及 turn GAE，整段 response 共享 turn advantage。[§2.3–2.4](https://arxiv.org/html/2512.17008#S2.SS3)

【迁移解释】可借 turn 级 credit 的单位，以及从原轨迹事后估计进展的方法。【边界】必须新增或已有 critic；teacher token likelihood 不是状态 value。Signed advantage 属于 policy-gradient 更新，若转成蒸馏权重，非负映射和混合方式是另一个方法选择，不能声称原文已验证。

### P5：按子目标段分别记账

【事实】HiPER 显式生成 subgoal 与 SWITCH/KEEP，段内做 low-level GAE，segment 边界 bootstrap 到 high-level value，宏观层按段持续时间折扣计算 credit。[§4.1、4.3，Eq.6–10](https://arxiv.org/html/2602.16165v1#S4.SS3)

【迁移解释】有原生子目标时，可区分“选错计划”与“正确计划执行失败”，改变监督的聚合边界。【边界】原方法含两类 critic 并改变输出接口；对 flat agent 事后随意切段，不继承其理论或实验证据。额外 planning tokens 也占吞吐。

### P6：同 prefix 下训练动作差异

【事实】Agentic-DPO 在专家状态采四个单步 student actions，过滤无效／专家等价动作，选择概率最高的不同动作作 rejected；对 action tokens 做局部 DPO并保留 SFT anchor。负例按 refresh round 更新，不执行到环境，也不生成后缀。[§3.2–3.3、Algorithm 1](https://arxiv.org/html/2607.10601v1#S3.SS2)

【迁移解释】可借同历史的局部偏好与困难负例，而非对整条失败轨迹每个 token 同罚。【边界】仍需单步采样和成对打分；专家状态不等于 student occupancy，非专家动作也可能正确。从两条同任务但不同状态的日志抽动作，不能自动组成有效局部偏好。

### P7：保留错误经历，局部化学习目标

【事实】Step-DPO 找第一错误文本 step，只比较该正确 prefix 下的正负 step；原正例构造依赖完整 continuation 的正确性筛选。Agent-R 用 MCTS／actor critique 构造失败 prefix＋revision＋好分支，只对修复输出训练。[Step-DPO §3](https://arxiv.org/html/2406.18629v1#S3)、[Agent-R §3.1–3.2，Eq.6](https://arxiv.org/html/2501.11425v3#S3.SS1)

【迁移解释】错误 prefix 可以作为恢复训练的输入，而不作为正向模仿目标；失败 suffix 也不必全受惩罚。【边界】原数据构造成本高，分别需要首错定位／多次完整 suffix 或 MCTS。已有修复日志时可摊销；首错本身不能由终局失败唯一定位。Agent-R 属自训练，这里只借数据操作。

### P8：观察是否带来边际信息

【事实】Toolformer 比较固定 suffix 在“call＋result”“无 call”“call 无 result”下的预测 loss；以后两种对照中的较小 loss 减去带结果 loss，筛选有用调用，然后 LM finetune。[§2，Filtering API Calls](https://arxiv.org/html/2302.04761#S2)

【迁移解释】可借固定已有后缀、多视图前向对照的操作，不必再生成新未来；把 observation 的信息收益与动作序列的 teacher likelihood 分开。【边界】候选生成和工具执行仍有原始成本；预测文本更容易不等于任务更接近成功。隐藏观察后评分原 suffix 是文本反事实，不是可执行的环境反事实。

### P9：采样前省计算，处理分布变化

【事实】PER 按 TD-error priority 重放 transition，并用 importance weights 调整优先采样偏差。ReOPD 从 teacher prefix pool 按深度衰减采位置，student 只生成当前 action；当前动作不执行到环境。[PER §3.2–3.4](https://arxiv.org/html/1511.05952#S3.SS2)、[ReOPD §4](https://arxiv.org/html/2607.04763v3#S4)

【迁移解释】若已有便宜 priority，可在昂贵 teacher 前向前选择训练位置；算完所有 teacher logits 再 mask，通常只改变梯度，不省掉已支付的评分。【边界】PER 的 TD-error 不是 teacher mismatch；旧 rollout 需要处理 policy staleness。ReOPD 的 prefix 来自 teacher pool，仅 action 内 on-policy，不是完整 student 状态分布。采样与 loss weighting 不应无意重复应用。

### P10：优势加权回归，而不是任意符号乘 KL

【事实】AWR 对已有 state-action 用 `exp((return−V)/beta)` 作为非负回归权重，并截断过大权重；value 和 policy 都用 buffer 数据拟合。[§3、3.3](https://arxiv.org/html/1910.00177#S3)

【迁移解释】可借“结果感知的 action quality → 非负训练权重”，与 teacher fidelity 分开表达。【边界】需要可用 value baseline，权重会放大估值误差；AWR 优化 action likelihood，直接给 OPD loss 套同式不是原算法或已验证等价搬运。

## 4. 条件性 pattern 与反例

- **已有反馈回填上一段**：FACA 利用 instrumented user simulator 同一次调用产生的 private reaction strategy，事后给前一 U2U segment 分配局部反馈。可借反馈对齐结构，但普通工具返回没有该隐藏标签；额外加 LLM extractor 不是免费。[FACA §3](https://arxiv.org/html/2608.17499#S3)
- **局部偏好未必比整轨迹好**：ETO 的 step-wise 变体通过在专家 prefix 上续跑到终点给当前动作贴标签；需要新环境交互，WebShop 对照也未超过 trajectory DPO。不能把“整轨迹 reward → 每步标签”当正确的自动分解。[ETO §4.4、附录 C](https://arxiv.org/html/2403.02502#A3)
- **分支式 lookahead 不符合本轮默认成本要求**：ProAct 的 MC-Critic 要从中间状态执行额外 continuations；random policy 只降低生成成本，不消除环境分支。[§3.3.1](https://arxiv.org/html/2602.05327#S3.SS3)
- **transition extraction 不等于细粒度 credit 已实现**：Agent Lightning 提供解耦训练和 transition 接口，但所核论文实现给 action 同一个 episode return；不能据此引用为已实现的 step-specific credit redistribution。[§3.3.2](https://arxiv.org/html/2508.03680#S3.SS3.SSS2)

## 5. 如何筛出适合当前 OPD 的 pattern

【解释／优先级，非用户已选方法】

1. **原 OPD 日志就能支持**：P1 reducer；有终局结果时 P2 校准。成本低、适合必要对照，但本身已有直接 OPD 先例。
2. **日志满足条件时值得借鉴**：P3 历史可比组；有修复日志时 P7；有 call/result/suffix 时 P8。其关键是比较对象与监督单位，而非多一个熵或 divergence 因子。
3. **接受新增 learner 成本时**：P4 critic／GAE、P10 value-based regression。新增前向可与 rollout 解耦，但仍占 GPU 和训练时间。
4. **明确改状态分布或采样时**：P6 局部负例、P9 replay；单独记专家状态覆盖、staleness 和额外生成预算。
5. **接口已有层级时才优先**：P5；不为搬一个 pattern 先新增一套 planner。

三类边界必须分清：

- teacher 可靠性、student 动作价值、student 可学习性是三个信号，不能因都能写成 scalar 就互换。
- 负 policy advantage 直接乘正 KL，会奖励增大 KL；迁移的是粒度／统计／信号，loss 的符号与目标必须重新定义。
- 数学 step、交互 turn、subgoal segment、语义 action 是不同单位；改变边界不自动获得语义等价或因果信用。

## 6. 来源与核查范围

原始来源为 arXiv HTML 及本 wiki 已有 OPD 页；未下载 PDF、未导入 Zotero。SOD、ATOD、TurnOPD、R²-OPD、PER、AWR、ReOPD 已核具体方法段；DPO/tool 与 RL 子任务分别只读核查原文方法，结果由主线程综合。未把摘要登记视为全文精读。

主要外部条目的作者与首次 arXiv 年份已由原 abstract 页 metadata 核对：

| 简称 | 作者／首次年份 | 原论文标题 | arXiv |
|---|---|---|---|
| GiGPO | Lang Feng et al., 2025 | Group-in-Group Policy Optimization for LLM Agent Training | 2505.10978 |
| HGPO | Shuo He et al., 2026 | Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks | 2602.22817 |
| Turn-PPO | Junbo Li et al., 2025 | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs | 2512.17008 |
| HiPER | Jiangweizhi Peng et al., 2026 | HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents | 2602.16165 |
| Agentic-DPO | Yixiong Chen & Alan Yuille, 2026 | Agentic-DPO: From Imitation to Agentic Policy Optimization on Expert Trajectories | 2607.10601 |
| Step-DPO | Xin Lai et al., 2024 | Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs | 2406.18629 |
| Agent-R | Siyu Yuan et al., 2025 | Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training | 2501.11425 |
| Toolformer | Timo Schick et al., 2023 | Toolformer: Language Models Can Teach Themselves to Use Tools | 2302.04761 |
| PER | Tom Schaul et al., 2015 | Prioritized Experience Replay | 1511.05952 |
| AWR | Xue Bin Peng et al., 2019 | Advantage-Weighted Regression: Simple and Scalable Off-Policy Reinforcement Learning | 1910.00177 |

本轮以所链 arXiv 版本为出处，不将 preprint 状态推断为正式录用。PER 方法段读2016年v4；AWR方法段读v3，首次日期以上述原abstract页为准。

检索缺口：未核实适用于文本多轮 agent、无额外采样的 action-type advantage normalization 原方法，也未核实专门针对 rejected tool span 的 unlikelihood 原方法；不以 HGPO 或局部 DPO 冒充这两类证据。本报告是代表性机制检索，不是全领域穷尽或最终 novelty check。

结构与链接检查只核本次新增报告、wiki log 和状态条目；原 paper／idea 页、graph、自动 index／query pack 不变。本轮没有新增 paper／idea 节点，因此未重建实体派生索引。

## 7. 扩展：按什么目标找训练方法

【本次综合，不是领域统一taxonomy】用户指出上轮方法覆盖过窄，尤其Agentic DPO遗漏较多。第一轮把低rollout开销放在筛选前端，漏掉了安全、噪声、探索、记忆及多目标偏好的重要家族。下面先按目标发现方法，再按成本筛迁移；不再因方法昂贵而省略其存在。

| 目标轴 | 具体要改善什么 | 已核代表 | 与其他轴的边界 |
|---|---|---|---|
| 任务性能／长程信用 | 当前任务成功；关键动作和组合行为可学 | DMPO、SDPO、HPL、CSO、iStar | 降KL或减少steps不是成功的替代指标 |
| 训练数据／探索效率 | 相同交互预算获得更多有效监督 | ToolPreference、ARPO、PAPRIKA | 样本效率不自动等于GPU小时更少 |
| 训练系统吞吐 | rollout调度、尾部等待、环境与learner利用率 | WAR、ProRL（本轮仅候选） | 属系统训练，不冒充新的preference loss |
| 部署／交互效率 | inference tokens、工具调用、循环、费用 | DEPO、DeLoop、K-DPO、CoBRA、SMART、WebThinker | 优化调用次数的训练本身仍可能昂贵 |
| 安全 | 恶意意图、注入、越权、授权确认 | SecAlign/Meta-SecAlign、AgentAlign、ARLAS、RETA、tool-check RL | 拒绝全部请求是捷径，要同时测正常任务效用 |
| 鲁棒性／恢复 | 工具噪声、失败、截断、接口变化、不可解时停止 | NoisyAgent、PAFT、ToolRL-DR、RoTTuning | 异常处理与攻击防御不可互代 |
| 泛化／组合性 | 新任务、新函数组合、新schema、分布变化 | Magnet、WEPO、PAPRIKA、MCMA | 更高in-domain成功率不证明OOD泛化 |
| 探索／主动信息获取 | 问什么、查什么、何时澄清或不问 | PAPRIKA、information-gain clarifier | 生成更多thought不等于获取了新证据 |
| 记忆／长程一致性 | 什么该记、如何抽象、如何复用失败经验 | MCMA | 优化memory policy不等于直接优化actor动作 |
| 个性化／用户目标对齐 | 同一显式任务下，匹配用户隐含偏好 | PUMA；DiaTool-DPO为待补读候选 | 个性化参数训练与多轮澄清不是同一方法 |
| 解多样性／test-time scaling | 保留多种可行策略，支持多样本后验证 | EntroPO | 与单次pass¹和部署成本可能冲突 |
| 协作／通信效率 | 多agent之间的信息分工与通信 | Optima（本轮仅邻近候选） | 原项目是单agent多轮，不能直接当同设定证据 |

## 8. 性能与泛化取向的偏好家族

本节8篇核查原HTML方法及数据构造。年份按原论文metadata；引用所链版本，不默认作完整全文精读或正式会议录核验。

| 方法／作者／年份与原文 | 原训练操作【事实】 | 可搬的结构与成本边界【解释】 |
|---|---|---|
| **DMPO** — Wentao Shi et al., 2024；Direct Multi-Turn Preference Optimization for Language Agents；[§4.2–4.3](https://arxiv.org/html/2406.14868#S4.SS2) | 在多轮trajectory DPO中加入时序／长度相关action log-ratio系数；以专家winning及SFT agent losing轨迹构造离线数据。 | 可借多轮目标与长度处理；loss不需新critic或逐步分支。其动态环境论证是近似，且被SDPO质疑，不背书为严格occupancy解法。 |
| **SDPO-social** — Aobo Kong et al., 2025；SDPO: Segment-Level Direct Preference Optimization for Social Agents；[§3.2–3.3](https://arxiv.org/html/2501.01821#S3.SS2) | judge定位错误轮，从此前history重采5个完整session，选有效正片段及等轮数负片段做DPO。 | 可借等长度、局部多轮对比；原造数有完整suffix及judge成本。这里SDPO指social segment方法，不是同名self-distillation。 |
| **HPL** — Heyang Gao et al., 2025；Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents；[§3.3–3.5](https://arxiv.org/html/2510.03253#S3.SS3) | 同时构建trajectory、step和语义action-group偏好；按组长度与reward gap做双维课程；组质量通过MC suffix估计。 | 可借组合行为的监督单位及训练顺序。数据构造需环境后缀采样，one-shot exploration后离线优化；短训练片段不等于便宜造数。 |
| **WEPO** — Jiarun Liu et al., 2024；WEPO: Web Element Preference Optimization for LLM-based Web Navigation；[§3.1–3.2](https://arxiv.org/html/2412.10742#S3.SS2) | HTML-only，使用正确element/action及DOM邻近混淆element，规则生成负操作做局部DPO。 | 可借结构化候选集合制造hard negative，无需为每个负例自回归生成。但依赖人工正例、DOM/ranker；未标注替代动作不一定错。 |
| **Magnet** — Fan Yin et al., 2025；Magnet: Multi-turn Tool-use Data Synthesis and Distillation via Graph Translation；[§3.4–3.5](https://arxiv.org/html/2503.07826#S3.SS5) | 从函数依赖图经Insert/Merge/Split构造组合与缺信息任务；用正确／错误hint生成多轮偏好，优化mDPO＋MLE。 | 可借主动控制错误类型及工具依赖的任务分布。原实例有10条student轨迹、teacher生成和judge，离线可摊销，成本不低。 |
| **WebThinker** — Xiaoxi Li et al., 2025；WebThinker: Empowering Large Reasoning Models with Deep Research Capability；[§3.5](https://arxiv.org/html/2504.21776#S3.SS5) | 对完整search/navigation/report轨迹做迭代DPO；先按正确性/质量排序，两者都正确再比工具次数，次数相同且长度差够大再偏好短轨迹。 | 可借成功优先的字典序pair规则，将成本放入偏好构造。需多条完整环境rollout；没有给局部动作隔离信用，也未证明训练吞吐提升。 |
| **EntroPO** — Jiahao Yu et al., 2025；Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization；[§3.2–3.3、D.4](https://arxiv.org/html/2509.12434#S3.SS2) | 熵正则改变多轮DPO中policy/reference log-prob系数，保留代码正确解多样性；离线teacher/student轨迹按test case配对。 | 可借可行策略支持集的目标；不是teacher熵权重。loss本身不加rollout，原采样和test-time多轨迹验证另计；确定性代码环境假设不能无条件搬。 |
| **CSO** — Mukai Li et al., 2026；Verified Critical Step Optimization for LLM Agents；[§3.2–3.3](https://arxiv.org/html/2602.03412#S3.SS2) | teacher为失败轨迹各状态提出alternative，PRM先筛点，再替换动作、由student续跑；确实转成功的动作构局部DPO。 | 可借student可完成的局部修正验证。逐状态expert生成、PRM和分支suffix均有成本；只适合有预算的离线/迭代数据机制，不能称廉价插件。 |

## 9. 效率家族：先区分优化阶段与完整造数

| 方法／作者／年份与原文 | 原机制【事实】 | 效率口径与成本边界 |
|---|---|---|
| **DEPO** — Sirui Chen et al., 2025；Dual-Efficiency Preference Optimization；[§3.2–3.4](https://arxiv.org/html/2511.15392#S3.SS4) | KTO desirable分支加入平均每步token数、总step数的效率bonus；undesirable不加。 | 优化部署token/step。训练loss离线且无critic；数据却有DeepSeek-V3 MCTS及GPT重写Thought，不能省略。数据效率对照也不是wall-clock。 |
| **DeLoop** — Tianle Chen et al., 2026；Repeated Actions as Self-Supervision for Long-Horizon Agents；[§4](https://arxiv.org/html/2610.19376#S4) | 从同一既有rollout挖循环动作作rejected、后来首次打破循环动作作chosen，二者配到循环前history，做DPO。 | pair mining无新judge/continuation；原rollout仍要收集。chosen来自更晚状态，能否搬回旧状态是弱监督前提；无恢复的永久循环无法提供正例。 |
| **K-DPO／balanced RL** — Yirong Zeng et al., 2026；The Tool-Overuse Illusion；[§4.3、§5.2](https://arxiv.org/html/2604.19749#S4.SS3) | minimal-tool与excessive-tool轨迹偏好；另一个RL变体仅对正确回答追加tool-call penalty。 | 优化TIR工具使用；K-DPO造数有1024采样预算，RL有在线工具交互。原K-DPO pair的correctness gate不充分，不能补写为等正确性比较；小模型有accuracy下降。 |
| **CoBRA** — Wenhao Zou et al., 2026；Learning Tool-Use Boundaries via Counterfactual Margins；[§3](https://arxiv.org/html/2609.00967#S3) | no-tool／forced-tool分支对比success−cost；clear margin做SFT，ambiguous样本做branch内归一化＋branch-margin RL。 | 可借工具路线边界与分支参照，原方法需要双expert及强制双分支continuation。减少部署calls不能视为训练吞吐更高。 |
| **ToolPreference／TP-LLaMA** — Sijia Chen et al., 2024；Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees；[§4.2](https://arxiv.org/html/2406.07115#S4.SS2) | 复用ToolBench DFSDT树，同prefix成功／失败sibling动作构局部DPO；去除diversity prompt。 | 已有树时挖pair便宜；树本身由ChatGPT/API搜索生成。报告减少的是DFSDT推理搜索步数，不能视为greedy调用数或训练速度。 |
| **ARPO** — Guanting Dong et al., 2025；Agentic Reinforced Policy Optimization；[§3.1–3.2、§4.6](https://arxiv.org/html/2507.19849#S3.SS1) | 既定sample budget在根轨迹与tool output后高entropy位置的partial branch间分配；共享prefix聚合advantage。 | 可借预算分配及避免重复prefix。需要在线suffix分支与工具执行；原half tool-use budget指训练交互预算，不是wall-clock减半或部署calls减半。 |
| **SMART** — Cheng Qian et al., 2025；Self-Aware Agent for Tool Overuse Mitigation；[§4](https://arxiv.org/html/2502.11435#S4) | 对组合子目标标parametric／tool-dependent，生成执行和为何调用／不调用的rationale，再SFT。 | 可借“不用工具也是正例”的监督覆盖；不是DPO。离线teacher标注、rationale和工具执行有成本，需求标签包含数据设计先验。 |

【解释】效率pattern可改变pair排序、margin、知识边界标签、循环负例、搜索树复用或探索预算。上述几类不能全部改写成单个stepwise权重。

## 10. 其他目标：探索、澄清、记忆、个性化及隐式信用

| 原方法／作者／年份 | 已核原机制【事实】 | 可迁移操作与边界【解释】 |
|---|---|---|
| **PAPRIKA** — Fahim Tajwar et al., 2025；Training a Generally Curious Agent；[§3.2–3.4](https://arxiv.org/html/2502.17543#S3.SS3) | 多种需要信息获取的文本环境中自采轨迹，以成功及较少交互轮排序；SFT与多轮DPO，只训练agent输出；按任务组learning potential分配采样。 | 可借跨任务的探索策略训练与group级课程，减少对当前任务答案的依赖。原方法仍需大量环境采样；learning potential也要统计，不是无代价识别每状态最优探索。 |
| **Information-gain clarifier** — Mengyi Deng et al., 2026；Uncertainty-Aware Clarification in LLM Agents with Information Gain；[§3.3–3.4](https://arxiv.org/html/2606.03135#S3.SS3) | 采问题、由strict user simulator回答，以clarification前后真实goal的teacher-forced log-likelihood差训练DAPO；不提问reward为0。 | 可借真实目标概率的前后差，训练“问什么／是否问”；需要训练时真实goal、额外候选问题及simulator回复。该代理不自动等于校准belief或精确Bayesian EIG；不能称无额外采样。 |
| **MCMA** — Sirui Liang et al., 2026；Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory；[§3.2–3.4](https://arxiv.org/html/2601.07470#S3.SS3) | frozen task actor＋learned memory copilot；同一轨迹生成多种记忆，按下游成功和执行长度排名，作者称DPO式训练；成功摘要和失败反思分别学。 | 可借“用下游效用给中间表示形成偏好”，将训练对象从即时actor扩展到memory。多候选记忆生成与下游执行成本高；正文Eq.7未显式写reference项，不据此背书为标准DPO推导。 |
| **iStar** — Xiaoqian Liu et al., 2025；Agentic Reinforcement Learning with Implicit Step Rewards；[§3.1](https://arxiv.org/html/2509.19199#S3.SS1) | 以已有trajectory outcome pairs训练implicit PRM，再用相对旧policy的action log-ratio生成step reward，结合episode advantage训练actor。 | 可借“trajectory preference→learned step signal”，不需额外step标签或中间状态分支，但新增PRM训练／前向。实验含WebShop、SOTOPIA及VisualSokoban，文本视角仅前两者；不是纯文本全套验证。 |
| **PUMA** — Hongru Cai et al., 2024；Large Language Models Empowered Personalized Web Agents；[§5.1–5.2](https://arxiv.org/html/2410.17236#S5.SS2) | 按用户历史检索memory，以heuristic labels SFT识别函数和生成参数，再采多种参数做DPO，匹配隐含偏好。 | 可借用户条件化的正负目标。主要是个性化Web function/parameter pipeline，不当作长程多轮信用证据；候选参数采样有成本。 |

## 11. 安全和鲁棒性分别有哪些训练操作

### 11.1 安全：意图、来源、授权、适应性攻击

| 原方法／出处 | 训练操作【事实】 | 可迁移pattern及成本边界【解释】 |
|---|---|---|
| **SecAlign**（2024），SecAlign: Defending Against Prompt Injection with Preference Optimization；[§3.2–3.3](https://arxiv.org/html/2410.05451v3#S3.SS2)；**Meta-SecAlign**（2025），Training LLMs against Prompt Injection for Robust Agents；[§3](https://arxiv.org/html/2507.02735v4#S3) | 同一attacked input配可信任务回答≻注入任务回答。SecAlign重组已有instruction/answer；Meta版本随机化注入位置，由冻结初始化模型分别回答clean/injection task造标签。 | 可借来源优先级的同输入对照；合法指令出现在不可信tool output中也不能自动执行。generic指令训练，agent为迁移测试；Meta有两次离线生成，DPO需双侧/reference评分，无环境分支。 |
| **AgentAlign**（2025），Navigating Safety Alignment in the Shift from Informative to Agentic Large Language Models；[§3.2–3.5](https://arxiv.org/html/2505.23020v1#S3.SS2) | abstract behavior chains实例化工具和参数，构造harmful/benign及敏感合法边界任务；过滤后混合执行演示与拒绝回答做SFT。 | 可借同能力链、不同意图的边界覆盖；不是给敏感工具统一负标签，也不是DPO。离线生成、judge、执行验证昂贵；恶意用户请求防御不等于间接注入防御。 |
| **Agent Safety Alignment via Reinforcement Learning**（2025）；[§3.1–3.4](https://arxiv.org/html/2507.08270v1#S3) | 显式tool_check＋yes/no确认；按拒绝、先确认、批准后执行、否认后停止给reward，联合格式信号优化；另有refusal classifier。 | 可借授权状态依赖的动作监督。需威胁标签、可信确认事件、classifier和额外交互；随机模拟确认不能推出真实权限安全。原文该部分名Multi-Modal，但实际任务是文本类别，不按标题误排为视觉。 |
| **ARLAS**（2025），Adversarial Reinforcement Learning for Large Language Model Agent Safety；[§3](https://arxiv.org/html/2510.05442v1#S3) | attacker在网页文本插入injection，agent执行；双policy GRPO，agent对手从历史attacker checkpoints采样。 | 可借历史攻击者回放，防只适应最新攻击；原方法训练attacker且逐步生成攻击，多轮rollout很重。主要验证泄露防御，不能概括所有安全行为。 |
| **RETA**（2026），Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment；[§4.2–4.3](https://arxiv.org/html/2606.15441v1#S4.SS2) | 训练多样attacker并归档策略；重写边界轨迹作安全SFT；security、utility、task-alignment rewards分别标准化后GDPO。 | 可借多目标分开归一化及安全/效用边界数据，避免全拒绝捷径。attacker、策略抽取、重写、judge及新增CoT均有成本，原部署有延迟增加。 |
| **Safety Training May Persist Through Helpfulness Optimization in LLM Agents**（2026）；[§3.1–3.2](https://arxiv.org/html/2603.02229v2#S3) | 同一轨迹分别评safety/helpfulness，按足够score gap配pair；比较S→H、H→S、混合DPO；阶段二reference取阶段一模型。 | 可借目标拆分、训练次序与reference更新的对照。需模拟交互和两套LLM评审；有限ToolEmu/LoRA结果不是不遗忘安全定理，标题当前版本是May Persist。 |

### 11.2 鲁棒：噪声、接口变化、恢复与停止

| 原方法／出处 | 训练操作【事实】 | 可迁移pattern及成本边界【解释】 |
|---|---|---|
| **NoisyAgent**（2026），Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments；[§3](https://arxiv.org/html/2605.27209v1#S3) | 在用户和工具结果注入歧义、不一致、failure/truncation/misleading；GRPO的clean/noisy组各自算advantage；按成功率gap增加噪声比例和难度。 | 可借扰动状态覆盖、分组参照和noise课程；已有rollout预算可分配两类状态，但造噪声/重试并非免费。必须保持任务可解及终局reward可靠；噪声鲁棒不证明注入/权限安全。 |
| **PAFT**（2026），Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use；[§6.1](https://arxiv.org/html/2607.01084v1#S6.SS1) | SFT增强：EFP注入异常反馈后接修复action；SBP给fatal feedback后接停止；SRP改写工具名/文档以破除符号记忆。 | 可借恢复、停止、功能语义三类局部目标。离线修复/改写生成，EFP增加长度；teacher目标需适配新接口，不能沿用失效clean action。停止行为不是安全拒绝的同义词。 |
| **ToolRL-DR**（2026），When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents；[§5.2](https://arxiv.org/html/2605.11928v2#S5.SS2) | 保持ToolRL GRPO/reward/超参不变，改为16类observation/action/metadata静态扰动数据，全替换或半混合。 | 可借只改训练分布的最小对照；原训练不含runtime transition errors。离线增广有成本，没有新增逐状态branch；测试的401/403恢复口径不能解释为授权安全。该文有训练recipe，不是benchmark-only。 |
| **RoTTuning**（2024），RoTBench: A Multi-Level Benchmark for Evaluating the Robustness of Large Language Models in Tool Learning；[§5.1](https://arxiv.org/html/2401.08326v3#S5.SS1) | GPT-4生成query/工具轨迹，改写为不同noise等级后混合LoRA SFT。 | 可借离线轨迹的接口一致变换；需一次teacher造数及增广开销。列为benchmark附带训练recipe，不把它当专门DPO方法。 |

本节第一作者/年份经原metadata核对：SecAlign与Meta-SecAlign为Sizhe Chen et al.（2024/2025），AgentAlign为Jinchuan Zhang et al.（2025），tool-check RL为Zeyang Sha et al.（2025），ARLAS为Zizhao Wang et al.（2025），RETA为Lipeng He et al.（2026），NoisyAgent为Yuxin Chen et al.（2026），PAFT为Song-Lin Lv et al.（2026），Safety Training May Persist为Benjamin Plaut et al.（2026），ToolRL-DR为Xiaolin Zhou et al.（2026），RoTTuning为Junjie Ye et al.（2024）。引用版本在表内链接；不把arXiv元数据当录用证明。

### 11.3 已核但只作邻近来源

- **SPrPO**：Pengxin Wang et al., Learning Perturbation Robust Policies for LLM Agents with Stable Optimization（2026），[§5、C.2](https://arxiv.org/html/2609.34064v1#S5)。对FFN channels加按敏感度缩放的Gaussian扰动，已有batch额外一次F/B，无新rollout；这是模型扰动鲁棒，不是工具噪声。原step时间明显增加，不能只因无新rollout就称低成本。
- **SecOPD**：Yibo Peng et al., Mitigating Adaptive Prompt Injections by On-Policy Distillation（2026），[§4](https://arxiv.org/html/2608.21500v1#S4)。attacked-input student生成，clean-input冻结同初始化模型评分，无teacher自回归或judge；训练generic instruction，AgentDojo为下游。属于本项目排除的self-distillation邻近源，不作为外部teacher Agentic OPD正式论文登记；可借上下文来源对照的操作。

## 12. 此次扩检新增的可迁移机制与覆盖边界

【解释】除了第一轮10类，还应显式考虑以下操作。每一项已有原方法出处；迁到OPD后的收益与新颖性尚未验证。

| 操作 | 具体改变什么 | 代表出处 | 对OPD迁移时必须保留的前提 |
|---|---|---|---|
| 正确性优先的字典序偏好 | 先成功，再比calls/tokens，而非统一加权和 | WebThinker | pair的成功性与质量可验证；不同状态动作不能直接配对 |
| 多维成本margin | 每步verbosity与总交互长度分开进入偏好 | DEPO | 不能把成本目标强行当teacher可靠性 |
| 结构化hard negatives | DOM邻近element、已有动作集合、依赖图错误类型 | WEPO、Magnet | 结构合法不意味着负例在语义上必错 |
| 无效循环→恢复偏好 | 从同rollout重复行为及后续突破构造局部目标 | DeLoop | 后来动作移到旧状态须仍有效；没有突破就无正例 |
| 组合动作group＋课程 | 以子任务/等长多轮片段比较，按长度和gap排序 | HPL、SDPO-social | 原标注/MC suffix成本；分段与状态一致性 |
| 安全来源对照 | trusted task响应与untrusted injection响应形成同输入pair | SecAlign/Meta-SecAlign | 安全目标与正常任务能力共同评估 |
| 授权状态条件监督 | 不确定、待确认、已授权、已否认对应不同合法动作 | tool-check RL | 确认来源可信，不能把工具自述当用户授权 |
| 分目标标准化 | 安全、效用、过程信号分开标准化再组合 | RETA | 标准化不证明无冲突，judge开销单列 |
| 环境层分组＋课程 | clean/noisy分组参照，按gap逐步增扰动 | NoisyAgent | signed RL advantage不直接乘KL；保持可解性 |
| 异常反馈后的局部修复／停止 | 学纠错action、不可恢复时终止，工具语义改写 | PAFT、RoTTuning | 目标跟随实际新接口与状态，不照抄clean target |
| 保留可行策略多样性 | 改reference约束/熵目标，支持不同正确解 | EntroPO | 更多多样性不保证更高pass¹或更低部署成本 |
| 改训练对象 | 用任务效用训练memory/clarifier/implicit PRM | MCMA、clarifier、iStar | 要计候选生成、下游执行、辅助模型成本 |
| 对手population回放 | 覆盖历史攻击和新策略，减遗忘 | ARLAS | attacker训练与环境成本高；OPD仅迁移状态分布尚待验证 |

### 12.1 发现但未完成原方法核查的候选

为保持高召回，留下窄shortlist及理由，不保存raw搜索结果。下面不作为已精读或已验证的新增mechanism证据。

| 候选／原来源 | 初筛价值与状态 |
|---|---|
| [Agent Q（2408.07199）](https://arxiv.org/abs/2408.07199) | 树搜索＋self-critique＋off-policy DPO早期代表，需补完整方法/造数 |
| [Building Math Agents with Multi-Turn Iterative Preference Learning（2409.02392）](https://arxiv.org/abs/2409.02392) | M-DPO/M-KTO，确定性transition公式已有核查，完整造数未读 |
| [DiaTool-DPO（2504.02882）](https://arxiv.org/abs/2504.02882) | 不完整query/out-of-scope dialogue states，与澄清/边界接近，待方法核查 |
| [HiTEC-KTO（2506.00042）](https://arxiv.org/abs/2506.00042) | hierarchical error checklists造工具参数负例，未确认长程多轮占比 |
| [Tool-Light（2509.23285）](https://arxiv.org/abs/2509.23285) | self-evolved preference、工具不足/过量与call后overthinking，待精读 |
| [When and What to Teach（2609.05513）](https://arxiv.org/abs/2609.05513) | teacher query gating、turn选择、trimmed DPO/SimPO；预算相关，待方法核查 |
| [Triton（2604.12666）](https://arxiv.org/abs/2604.12666) | 文本web hard negatives、SFT→ORPO→GRPO；不能将全配方效果归ORPO |
| [CausalFlow（2605.25338）](https://arxiv.org/abs/2605.25338) | repair/learning-ready pairs；未确认真的有DPO训练结果，暂为数据邻居 |
| [Optima（2410.08115）](https://arxiv.org/abs/2410.08115) | 多agent通信token/readability/quality目标；邻近任务，未方法精读 |
| [WAR（2607.17299）](https://arxiv.org/abs/2607.17299)、[ProRL Agent（2603.18815）](https://arxiv.org/abs/2603.18815) | 真训练系统吞吐线索，尚未核查完整系统方法或速度基线 |
| [StruQ（2402.06363）](https://arxiv.org/abs/2402.06363v2) | generic可信prompt/不可信data的结构化防御邻居；本轮仅metadata/摘要 |
| [AgentNoiseBench（2602.11348）](https://arxiv.org/abs/2602.11348v2) | noise评测入口；本轮未认定为训练方法 |

明确范围外/不计训练方法：SAGE-NeurIPS2025的视觉web/VLM主体（不是本wiki的SAGE-OPD）；Act Wisely和STEP的multimodal/GUI主体；INTENT为推理期planning。InjecAgent与AgentDojo作为评测环境，不单独计防御训练方法；AutoInject只训练攻击者，不能独立计为防御agent训练。匿名Reasoning SecAlign原稿版本/作者尚未核实，不作正式证据。

### 12.2 核查层级与未解决问题

- 三个独立只读检索分片分别发现17个性能/泛化、14个效率、15个安全/鲁棒候选；主线程补探索、澄清、memory、implicit credit、个性化5篇。正文§8–11收录31篇原方法/recipe核查条目，另2篇SPrPO/SecOPD只作邻近来源；它们不是33种互不重叠的算法，也不是全领域穷尽。
- 主要条目的标题、第一作者和首次年份由原arXiv abstract metadata核对；方法来源均指向原HTML章节。局部方法核查不等于整篇全文精读。候选层不与方法核查层混合。
- safety和robustness仍各有多种子目标。当前未完成：隐私/数据最小化、不可逆动作风险的训练机制、真正calibrated ask-for-help/abstention、lifelong安全保持、纯文本coding局部debugging pair、multiagent协作训练的系统覆盖。目标轴中的列举不代表这些问题已有通用解。
- 效率需分别对齐数据收集、teacher/judge生成、优化F/B、系统wall-clock、部署tokens/calls。仅有更少工具调用或更少样本，不足以断言rollout吞吐更高。
- 保持已有paper/idea实体、graph、自动index/query pack不变；本次只扩展主题报告、log、STATE。未正式入库新论文、未生成自己的idea、未跑训练或GPU实验。
- 新鲜验证：新增部分33个方法HTML来源均可打开，所引章节锚点均存在；主要条目metadata由原arXiv核对；表结构、本地入口及58个原实体/派生文件聚合hash检查通过。链接检查仅证明出处可定位，不是对方法内容的独立复核或复现。
