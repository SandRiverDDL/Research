# G17 候选查新证据

日期：2026-10-15。用户已选择 L1/L2/L3。本文件记录候选级定向检索的原文入口与边界；不是全景调研，不宣称穷尽搜索。12项候选查新与交叉审阅已完成；下方保留检索线索与后续原文核查两个层次。所有方法创新与机制推断保持 provisional。

## 已有直接覆盖（生成输入，不是新颖性裁决）

| ID | 原文入口 | 作者机制与本轮判断边界 |
|---|---|---|
| B1 | [TrustMOPD v3 §3、App.C.4.1、App.F](https://arxiv.org/html/2609.23697v3) | 逐 student prefix 校准 teacher-reference displacement 并加权 reverse-KL；response-level ablation 已检验位置变化。MultiCap含组合训练；汇总recovery不能替代整题联合成功率。 |
| B2 | [TU-OPD v1 §3.3–3.4](https://arxiv.org/html/2607.27770v1#S3) | 蒸馏集合要求至少一teacher达到整题成功率阈值；quality weighting与winner residual已保护独有监督。该门槛只限定此方法，不能外推全部MOPD。 |
| B3 | [H-OPD v3 §3.3–3.4](https://arxiv.org/html/2607.02592v3#S3) | VL description桥接text teacher；同一student prefix逐token entropy mixture。信息传递与动态专长分配已有机制。 |
| B4 | [SMOPD v2 §3.2](https://arxiv.org/html/2608.03092v2#S3.SS2) | 同prompt reward specialists的arithmetic teacher mixture/FKL，加equal-weight GDPO；收益不可全部归因于蒸馏。 |
| B5 | [AVSD v1 §2](https://arxiv.org/html/2605.20643v1#S2) | 同backbone privileged views的geometric consensus、arithmetic residual及gate；不是独立领域experts设定。 |
| B6 | [MAD-OPD v1 §4](https://arxiv.org/html/2605.01347v1#S4) | teacher-only debate改变监督，student不见debate；按confidence聚合。协作蒸馏已有覆盖，存在K×R及context成本。 |
| B7 | [Off-vs-On Distillation v1 §3、§5、§6.3、App.G/H](https://arxiv.org/html/2609.38666v1) | 本轮原文确认：sequence-level arithmetic/geometric聚合、reverse target的continuation项、长horizon的prefix reversal已有理论；也有function-approximation扩展，不能把“仅tabular”当完整描述。尚非可规模化LLM实证recipe。 |
| B8 | [TrustMOPD官方代码](https://github.com/sunjie279/TrustMOPD-) / [数据构造方法](https://arxiv.org/html/2609.23697v3#A2.SS2) | 仓库提供训练代码与prepare_multicap.py等入口；论文提供math+IF/code+IF/math+code构造。只确认公开入口，不等于本轮下载、跑通或验证联合能力benchmark。 |

事实来源优先原文；本地完整笔记仍在 research-wiki/papers/。后续评审应沿链接核实关键相似性，不能把本文件的概括当作定理或复现实验。

## 定向检索命中的待核实近邻

下表为检索发现，除B系列已有核查外，默认仅title/abstract或检索片段核对；审阅者须打开原文的方法段后作实质裁决。这里没有预先淘汰任何候选。

| ID | 候选关联 | 原始来源 | 初筛相关点 |
|---|---|---|---|
| N1 | L1-A1 | [VG-OPD v2](https://arxiv.org/html/2609.15404v2#S3) | 已有本地全文方法笔记：criterion-gated多expert监督；需对比“局部认证”与“完整teacher可靠性”是否已有直接覆盖。 |
| N2 | L1-A1/A2/A4 | [MT-SDPO v1](https://arxiv.org/html/2609.02548v1#S4) | 答案合格teacher的critique→privileged EMA self-teacher；整题eligibility门槛和反馈验证对象需要分清。 |
| N3 | L3-A1 | [γOPD](https://arxiv.org/abs/2609.16937) | 摘要明确sequence/token temporal-credit关系、discounted future credit、multi-teacher实验；须核对候选return-to-go是否已被完整包含。 |
| N4 | L2-A1 | [R³](https://arxiv.org/abs/2402.05808) | 推理RL的reverse curriculum，逐步把开始位置从示范结尾移至开头。 |
| N5 | L2-A1/A2 | [STRIDE](https://arxiv.org/abs/2609.14636) | OPD的early stop和high-quality prefix buffer/restart；须区分一次边界分裂与已有restart采样。 |
| N6 | L2-A3 | [Hindsight Instruction Relabeling](https://arxiv.org/abs/2302.05206) / [SAC-GLAM](https://arxiv.org/abs/2410.12481) | LLM指令重标记/LLM agent hindsight已有工作；需要判断中间状态逆映射+另一专长教学的增量。 |
| N7 | L2-A4 | [MAMBA，NeurIPS 2020](https://papers.nips.cc/paper_files/paper/2020/hash/3c56fe2f24038c4d22b9eb0aca78f590-Abstract.html) | learner roll-in、expert roll-out、多oracle policy improvement。 |
| N8 | L2-A4 | [MAPS/MAPS-SE，ICML 2023](https://proceedings.mlr.press/v202/liu23av.html) | 多black-box oracle的active policy improvement与state exploration；不能把多expert cost-to-go视为未研究。 |
| N9 | L1-A4 | [Interactive KD](https://arxiv.org/abs/2109.04641) / [The Assistance Dilemma](https://arxiv.org/abs/2610.06446) | 前者有course/exam迭代student反馈；后者讨论以student真正学会而非提示仍在context中的成功奖励teacher。 |
| N10 | L1-A3/L3-A2 | [ANT，AAAI 2023](https://ojs.aaai.org/index.php/AAAI/article/view/26190) | partial label knowledge/dependencies向同一student的联合amalgamation；非LLM OPD，但直接反对“partial teacher整合本身新颖”的叙述。 |
| N11 | L1-A2 | [Neuro Symbolic Reasoning for Planning](https://arxiv.org/abs/2309.16436) / [ExVerus](https://arxiv.org/abs/2603.25810) | LLM的counterexample-guided synthesis/repair；须区分推理循环与训练单一student。 |
| N12 | L3-A2 | [RouteOPD](https://arxiv.org/abs/2609.08337) | pairwise log-odds与jointly realizable targets已有OPD方法；需比较同位置vocab pair与跨prefix、跨片段的2×2关系。 |
| N13 | L3-A3 | [Switching between Hidden Markov Models using Fixed Share](https://arxiv.org/abs/1008.4532) | HMM专家切换/过滤是强邻近；需要区分目标定义本身与新的多teacher整合结果。 |
| N14 | L2-A2 | [Cache Coherent Resampling，ICML 2026](https://proceedings.mlr.press/v306/wang26kb.html) | LLM推理的adaptive SMC/resampling；推理采样结果不能直接当训练方法已覆盖，但必须比较。 |

### 检索覆盖记录

主协作者已按每个候选的核心干预做三种具体表述查询，另对已知近邻做追踪。查询覆盖arXiv、ACL Anthology、OpenReview、NeurIPS/PMLR与AAAI入口，包含2025–2026及必要旧作。L1-A1的严格词组检索命中不足，L3-A4的“obligation”查询混入法律文献，均不能据此声称新颖；审阅阶段须改用formal verification/auxiliary state supervision等表述补查。没有扫描query_pack或重新做主题landscape。

## 方法表述的代数边界（主协作者检查，非实验）

- L3-A2 的 Δ=s11+s22−s12−s21：若分数变为 s′ij=sij+ai+bj，Δ 不变；这只说明可分离行/列偏置抵消，不保证消除所有长度、风格或可靠性偏差，更不是因果识别。
- 若 student 在所有相关完整前缀上精确匹配 teacher 的条件分布，它也会匹配对应片段概率与 Δ。因此不能声称 token 条件目标原则上无法保留跨步骤依赖；候选的可检验主张限于有限数据、有限训练和模型容量下的监督效率。
- 2×2关系由后续teacher提供，另一teacher在前段教学中的必要性必须独立建立；单teacher同样适用的loss并不自动构成多teacher整合贡献。
- 原候选的前缀来自student，但交换后的片段是teacher-forced反事实评分；不可把所有新增训练项称为纯on-policy采样。
- 补检精确“cross-ratio / conditional odds ratio / difference-in-differences + distillation”未获得足够直接命中。无命中不是新颖性证据；[RKD，CVPR 2019](https://openaccess.thecvf.com/content_CVPR_2019/html/Park_Relational_Knowledge_Distillation_CVPR_2019_paper.html)已将关系作为蒸馏对象，具体差别由候选审阅核查。

## 交叉审阅后的原文更正与收窄

以下来自承重方法段核查，不是复现实验。逐条检索表述、原文锚点及完整风险见本轮[trace目录](../.aris/traces/idea-creator/2026-10-15_run03/)。后续表格中的“剩余差异”仍为候选主张。

| 候选 | 方法段确认 | 剩余差异／不能声称的内容 |
|---|---|---|
| L1-A1 | [VG-OPD v2 §3.2–3.4](https://arxiv.org/html/2609.15404v2#S3)的许可按criterion优势，不要求整题正确；[Process-Verified RL §3–4](https://arxiv.org/html/2606.20068)已有Lean tactic验证及过程奖励 | 只能争取student当前状态上具体动作的证书与多来源动作蒸馏；局部许可和局部验证本身都不是新颖性。 |
| L1-A2 | [ExVerus §3](https://arxiv.org/html/2603.25810)已有验证反例后的推理修复；[CURE §3](https://arxiv.org/html/2506.03136)已有coder/tester协同训练 | 多critic认证否决的训练目标尚有差异；无反例不等于答案正确。 |
| L1-A3 | [ANT方法](https://ojs.aaai.org/index.php/AAAI/article/view/26190/25962)已有partial teachers及依赖传递；[Symbolic KD §2.1](https://aclanthology.org/2022.naacl-main.341.pdf)已有质量因子乘积蒸馏 | 固定答案投影评分是候选具体差异；投影相同但整体正确性不同的答案无法区分。 |
| L1-A4 | [IKD Course/Exam Eq.5–8](https://arxiv.org/html/2109.04641)已按student真实参数更新后的exam表现优化teacher；[MMKD §III Eq.6–9](https://arxiv.org/html/2306.06634)已有多teacher元聚合 | 仅剩直接优化多个生成式teacher局部消息的差异。[Assistance Dilemma §3](https://arxiv.org/html/2610.06446)冻结student参数，不是同类参数学习增益；早期检索线索不能混写。 |
| L3-A1 | [γOPD §3.1 Eq.8、§3.2 Eq.10](https://arxiv.org/html/2609.16937v1)已有return-to-go及多teacher实验；[β-OPSD §2.3–2.4](https://arxiv.org/html/2607.28582v1)也有未来log-ratio更新 | 候选未局部归一化、状态依赖的geometric factors尚有目标差异；不能把梯度载体本身称为新机制，也不足以据此宣布完整scoop。 |
| L3-A2 | [RouteOPD §3 Eq.3–12](https://arxiv.org/html/2609.08337v1)为同一状态词表pair，shared potential保证目标兼容；[RKD §3.2](https://arxiv.org/pdf/1904.05068)已有关系potential蒸馏 | 候选跨两个prefix的条件偏好变化具有明确delta，但其独立clip可能破坏重叠关系的加法恒等式；关系误差下降不等于联合成功。 |
| L3-A3 | [Fixed Share/EHMM §3](https://arxiv.org/pdf/1008.4532)已有latent transition、posterior expert mixture | 核心过滤器已知；MOPD压缩及同题组合结果未由该文包含。来源后验不是可靠性后验。 |
| L3-A4 | [Language Modeling with Latent Situations §3.1 Eq.2–3](https://aclanthology.org/2023.findings-acl.795.pdf)已有辅助state decoder、联合训练及推理时移除decoder | 活跃未履行义务与单位置监督是剩余delta；“辅助状态重建不加部署成本”已有直接覆盖。 |

【审阅者数学检查】L1-A2从π采样又按π×生存指示加权，极限目标含π²；L1-A3从π采样后按投影乘积F加权，极限含π×F。有限候选目标可定义，但不能分别冒称普通条件化与纯teacher PoE。L3-A2的clip例子：同前缀对下D12=D23=0.8c、D13=1.6c，逐项截断后D13=c≠D12+D23。这些是对候选的推导，不冒充原论文结论或已运行实验。

| L2候选 | 方法段确认 | 剩余差异／判断 |
|---|---|---|
| L2-A1 | [TCOD-B2F v2 §4.2 Eq.5、Algorithm 2](https://arxiv.org/html/2604.24005v2)已有teacher成功前缀→student后续OPD→逐步撤至零；[AdaPrefix-GRPO §4.2](https://arxiv.org/html/2607.07674v1)已有成功率反馈控制及退火 | 联合teacher构造前缀与课程仍有具体变化，但reverse OPD路径本身已有直接覆盖，降低方法优先级。 |
| L2-A2 | [BranchOPD v1 §4.1–4.3 Eq.6–11](https://arxiv.org/html/2610.13481v1)已有共享student前缀分叉、条件后续及prefix loss只计一次；[STRIDE §4.2、§5.3](https://arxiv.org/html/2609.14636v1)已有高质量prefix restart及多teacher实验 | 只剩确定性验证A→B交接点相对entropy/disagreement选点的增量；不能把branching本身称为新方法。 |
| L2-A3 | [HIR §4.2–4.3](https://proceedings.mlr.press/v202/zhang23ab/zhang23ab.pdf)已有sub-output relabeling；[CodeIt §2.2](https://arxiv.org/html/2402.04858v2)已有按错误程序的实际行为重标任务 | 精确DSL逆映射后新采B后续仍有差异；需证明改题比对同一z直接训练B有额外作用。 |
| L2-A4 | [Learning to Generate Better Than Your LLM §4、Algorithm 2](https://arxiv.org/html/2306.11816v2)已有learner roll-in、guide roll-out和完成回报训练learner；[MAMBA §3.2](https://arxiv.org/html/2007.00795v2)、[MAPS §4](https://arxiv.org/html/2306.10259v2)已有多oracle完成价值 | 单个不可修改交接点、一次完成回报并行MOPD是具体简化；必须证明B回报提供A正确性标签之外的信息。 |

### 完成状态与检索限制

三个交叉审阅分支日志分别记录40、45、51条web查询（共136条，含追踪检索，另有主协作者补检）；每候选3个承重claim，每claim至少3种表述。覆盖arXiv与顶会官方入口，但没有独立查询DBLP、Semantic Scholar等API，不宣称多数据库穷尽。部分OpenReview/CVPR入口未能直接读取，已用可用的作者arXiv原文替代；未拿到正文的来源不承担完整覆盖判断。全部来源、read_depth及访问限制在三个response.json中。

结果：L1-A1、L3-A2通过本轮早期有限查新门槛；其余10项为PROCEED WITH CAUTION。没有找到一篇完整包含某候选全部结果的特定论文，因此没有ABANDON；降低优先级只表示当前方法增量／信息价值不足。生成仅有Astra产出，评审为复用上下文的同模型交叉审阅，结论same-family provisional；未运行训练或pilot。
