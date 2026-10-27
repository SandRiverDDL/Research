# NeurIPS 2026 纯文本大模型后训练 Oral 与 Spotlight 论文初读

截至 2026 年 10 月 14 日的官方数据快照，本轮从 oral、spotlight 中筛出 19 篇相关论文：主会 18 篇，Evaluations and Datasets track 1 篇。重点覆盖训练目标、监督来源、优化和信用分配、模型适配，以及直接分析后训练效果的安全与审计工作。排除多模态、VLA、纯预训练、纯推理时系统及没有明确训练关联的通用 benchmark。

每篇用两句话概括主要内容与作者提出的贡献，依据原始摘要；没有将作者声称的贡献视为已独立验证的全领域首创。

## Oral

| 论文 | 研究切面 | 主要内容与贡献 |
|---|---|---|
| [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://neurips.cc/virtual/2026/poster/152494) | 可验证任务与训练数据 | 用合成统计任务和强化学习训练能可靠执行假设检验的 LLM agent，并建立 P-Bench。关键贡献是把统计推断是否有效纳入可验证训练信号，而不只检查分析代码是否运行成功。 |
| [The Attacker in the Mirror: Breaking Self-Consistency in Safety via Anchored Bipolicy Self-Play](https://neurips.cc/virtual/2026/poster/151513) | 自博弈与安全训练 | 分析同一模型同时扮演攻击者和防御者时，共享更新如何削弱对抗压力。提出冻结共同底座、分别训练两套角色 LoRA 的 Anchored Bipolicy Self-Play，以保持稳定训练和持续的攻防竞争。 |
| [Pruning and Distilling Mixture-of-Experts into Dense Language Models](https://neurips.cc/virtual/2026/poster/150472) | 结构转换与蒸馏 | 将训练好的 MoE 经专家评分、选择和分组，转换为完全稠密的 FFN，再用原 MoE 蒸馏修复能力。其贡献包括系统比较转换设计，并提出考虑专家多样性的评分方法。 |
| [Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors](https://neurips.cc/virtual/2026/poster/148241) | 训练诱发的监控规避 | 展示微调能让模型学会在指定触发语下隐藏某种内部概念，并零样本迁移到未见过的安全监控器。该结果揭示，激活监控的可靠性还需要面对模型经训练后主动规避监控的情况。 |
| [LoRAcles: Self-Supervised Weight-Space Interpretability at Scale](https://neurips.cc/virtual/2026/poster/154333) | 权重空间审计 | 训练能直接读取 LoRA 权重并用自然语言描述所学行为的语言模型。通过“文档训练出 LoRA，再让审计模型回答文档问题”的自监督流程，泛化到隐藏行为及部分语义后门检测。 |

## Spotlight

| 论文 | Track 与研究切面 | 主要内容与贡献 |
|---|---|---|
| [Theoretical Limits of Language Model Alignment](https://neurips.cc/virtual/2026/poster/153597) | Main · 对齐理论与奖励误差 | 刻画给定 KL 预算下语言模型奖励提升的理论边界，并给出利用底座样本估计可达收益的方法。进一步分析代理奖励误差导致的 reward hacking，以及奖励集成为何能缓解它。 |
| [Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use](https://neurips.cc/virtual/2026/poster/149224) | Main · 工具调用与信用分配 | CARL 在工具调用边界切分轨迹，用一个最终二元奖励为各段分配独立 advantage。通过模型自身 rollout 训练 critic，学习何时内部知识够用、何时需要工具，减少无效调用而不依赖步骤标注。 |
| [Reinforced Fast Weights via Next-Sequence Prediction](https://neurips.cc/virtual/2026/poster/154908) | Main · 训练目标与快速权重 | ReFINE 用序列级预测目标训练 fast-weight 语言模型：选择高熵位置、生成多 token rollout，再通过 GRPO 优化序列奖励。其贡献是让训练信号面向递归记忆对未来序列的效用，支持中训练、后训练及测试时训练。 |
| [Do Thinking Tokens Help with Safety?](https://neurips.cc/virtual/2026/poster/150945) | Main · 推理模型安全诊断 | 发现多个推理模型的拒答倾向在思考开始时已高度可预测，后续思考往往很少改变最终决定。结合安全干预分析，指出增加 thinking tokens 并不自动带来更好的安全审议，为训练目标设计提供反例。 |
| [ECHO: Terminal Agents Learn World Models for Free](https://neurips.cc/virtual/2026/poster/154932) | Main · 环境反馈与辅助监督 | ECHO 在 agent 的策略梯度训练之外，增加预测终端观察 token 的交叉熵损失。它复用已有 rollout 和前向计算，把 stdout、错误和文件内容转成密集监督，使失败轨迹也能提供学习信号。 |
| [Self-Distilled RLVR](https://neurips.cc/virtual/2026/poster/152431) | Main · RLVR 与自蒸馏 | RLSD 将两类信号分工：用环境验证奖励确定更新方向，用自蒸馏得到的 token 级策略差异调节更新幅度。它针对特权教师单独监督时的信息泄漏与长期不稳定问题，属于 OPD／自蒸馏路线的进一步组合。 |
| [From Next-Token to Next-Block: A Principled Adaptation Path for Diffusion LLMs](https://neurips.cc/virtual/2026/poster/152123) | Main · 已有模型的生成范式转换 | 研究如何把现成自回归 checkpoint 适配成 block-diffusion 语言模型。方法结合保持已提交上下文因果性、辅助 AR 指导及逐步增大 block 的课程，降低转换过程中的能力损失。 |
| [MUX: Continuous Reasoning via Multiplexed Tokens](https://neurips.cc/virtual/2026/poster/151022) | Main · 潜在推理与蒸馏 | MUX 将一段离散推理 token 蒸馏成按位置加权叠加的连续潜在 token，以压缩推理表示。其贡献是设计可恢复原文本的 multiplexing 目标，并分析避免潜在表示塌缩的条件。 |
| [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://neurips.cc/virtual/2026/poster/152610) | Main · 非完美验证器与策略优化 | NOPO 处理只能可靠证伪、不能可靠证真的验证器：把未被证伪的结果当作未标注样本，只压低可信失败的概率。通过样本级自衰减及组级支持权重，避免把通过不完整检查的错误捷径当成正奖励。 |
| [Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation](https://neurips.cc/virtual/2026/poster/153897) | Main · 安全保持与参数更新约束 | WSR-Tune 先构造安全条件化的权重基，把安全相关信息集中到较少方向，再冻结这些方向进行下游微调。其贡献是在重参数化空间中分离安全与任务更新，缓解适配过程对已有安全行为的覆盖。 |
| [Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples](https://neurips.cc/virtual/2026/poster/154663) | Main · 训练数据投毒与微调安全 | 主要通过预训练实验发现，植入后门所需的投毒文档数量不一定随模型和数据规模增长。论文也报告微调中的同类现象，因此可作为后训练数据安全的交叉参考，不能把全部规模结论都归为微调实验。 |
| [Breaking Information Islands in Sparse Tuning via Small-World Connectivity](https://neurips.cc/virtual/2026/poster/155451) | Main · 参数高效适配 | SWIFT 将块对角稀疏更新与固定置换结合，在不增加可训练参数的情况下建立跨特征维度连接。它从更新拓扑解释稀疏微调中的信息孤岛，并在文本推理和生成等任务中验证；本轮只取其文本模型部分。 |
| [Towards a Universal Causal Reasoner](https://neurips.cc/virtual/2026/poster/153248) | Main · 合成数据与因果推理 | UniCo 以精确因果推断生成覆盖 18 类问题的数据，转写成代码及叙事形式，并过滤依赖推理捷径的样本。用这些数据做 SFT，检验因果能力是否能迁移到分布外任务及更忠实的通用推理。 |
| [Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs](https://neurips.cc/virtual/2026/poster/139760) | Eval and Datasets · 安全评测与训练归因 | 提出 Expected Harm，将输出危害严重度与现实执行可能性结合，揭示拒答行为的风险误校准。通过分阶段 checkpoint 追踪到 SFT 数据分布及弱执行成本表征，直接连接安全评测与后训练数据设计。 |

## 从这批论文看后训练的研究切面

以下是对所选论文的综合判断，不是全社区热度排名，也不能由 oral／spotlight 数量推出未来一定爆火。

- **监督信号从哪里来**：ECHO 从环境观察取密集监督；NOPO 研究只能证伪的验证器；UniCo 以精确因果推断生成训练数据。后训练研究不只是在现成奖励上换优化器。
- **训练究竟更新什么能力或状态**：ReFINE 针对 fast-weight 记忆的序列效用；MUX 改造推理表示；MoE-to-dense 和 AR-to-block-diffusion 改造已有模型的结构及生成方式。
- **多步学习如何分配信用**：CARL 把工具使用轨迹切段，Anchored Bipolicy Self-Play 通过角色参数分离维持对抗压力，RLSD 分离更新方向和幅度的来源。
- **后训练改变了什么、会破坏什么**：LoRAcles 从权重审计习得行为，Neural Chameleons 检验监控规避，WSR-Tune 保护安全相关参数方向，Expected Harm 追溯 SFT 数据诱发的风险误校准。

若目的是寻找 OPD 之外的机制入口，优先细读 **ECHO、NOPO、ReFINE、MUX、LoRAcles**：分别对应环境监督、单边验证、记忆训练目标、潜在推理表示、权重空间审计。它们值得作为候选研究家族调查，竞争密度、已有先行工作和可复现实验尚需单独核查。Self-Distilled RLVR 则明确属于已有 OPD／自蒸馏路线。

## 邻近工作与边界

为缩小候选集，以下工作不计入上述 19 篇：

| 论文 | 保留线索的原因与边界 |
|---|---|
| [Felid: A Flexible and Efficient Design for Transformer Fine-Tuning over Encrypted Data](https://neurips.cc/virtual/2026/poster/148321) | 加密数据上的微调基础设施；摘要中的实际验证是两层 BERT，单列为基础设施邻近工作。 |
| [Training Generalizable Collaborative Agents via Strategic Risk Aversion](https://neurips.cc/virtual/2026/poster/151685) | 通用 MARL 方法包含 LLM 协作任务，但摘要不足以确认其独立的语言模型参数后训练部分。 |
| [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](https://neurips.cc/virtual/2026/poster/152173) | 学习主要落实在外部语义 guardrail memory，且实验含计算机使用环境；不计入本轮参数后训练主清单。 |
| [FeatCal: Feature Calibration for Post-Merging Models](https://neurips.cc/virtual/2026/poster/152364) | 包含 CLIP 与 FLAN-T5-base 的模型合并校准；可借鉴文本实验，但不计入本轮大语言模型核心清单。 |
| [Reasoning with Undecoded Tokens in Diffusion Language Models](https://neurips.cc/virtual/2026/poster/152594) | 训练目标及潜在 token 机制相关，但摘要未明确已有 checkpoint 后训练的独立部分。 |
| [Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test](https://neurips.cc/virtual/2026/poster/139215) | 评测 safety judge 对规则改写的稳定性，可启发奖励模型验证，但没有直接展示后训练机制。 |
| [AIs with Secret Loyalties are a Serious but Addressable Threat](https://neurips.cc/virtual/2026/poster/140059) | Position paper，提出 secret loyalties 威胁与研究议程，不是新的训练算法。 |
| [Sampling Is Not Curiosity: Why LLM Agents Should Investigate](https://neurips.cc/virtual/2026/poster/140072) | Position paper，提出需在线更新预测结构的好奇心框架，可作为探索训练的研究线索。 |
| [We Should Distinguish Unlearning From Untraining](https://neurips.cc/virtual/2026/poster/140062) | Position paper，区分删除训练样本影响与删除底层概念，属于问题定义层面的交叉参考。 |
| [RAOP: Step-Level Resource Orchestration for LLM Agents across Edge and Cloud](https://neurips.cc/virtual/2026/poster/152497) | 用 GRPO 训练资源编排策略，摘要未明确被更新的是生成语言模型；单列系统邻近工作。 |

## 数据与覆盖

- 原始名单：9,242 条展示／活动记录；其中录取论文记录按 OpenReview forum ID 去重后为 6,514 篇，覆盖 Main、Evaluations and Datasets、Position tracks。活动记录数不等于论文数。
- 主会 oral 86 篇、spotlight 209 篇；连同其他 track 的同级论文共 347 篇。分级依据官方 `decision`，不是 `eventtype`：oral 论文也可能拥有 poster 展示记录。
- 官方摘要 JSON 有 5,853 条以展示 ID 索引的摘要，不能将其条数等同于去重论文覆盖数。筛选前，347 篇中有 225 篇能匹配这份摘要文件。
- 标题初筛加边界检查共 43 篇；从官方详情页补齐 14 篇缺失摘要，额外复核 2 篇后，这 43 篇摘要全部齐全。最终纳入 19 篇、邻近工作 10 篇、排除 14 篇。
- 全部 347 篇完成标题层检查；摘要层仅核查 43 篇，标题没有显露后训练关联的工作仍可能漏检。这里只覆盖 oral／spotlight，没有扩展到普通 poster。

官方来源：[论文名单 JSON](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)、[摘要 JSON](https://neurips.cc/static/virtual/data/neurips-2026-abstracts.json)、[下载页面](https://neurips.cc/Downloads/2026)。各表中的论文链接指向原始摘要详情页。

本地数据目录：[neurips-2026-index](../literature-index/tmp/neurips-2026-index/)。`sources.json` 保存原始文件大小、来源和 SHA256；`post-training-shortlist.json` 包含所选论文摘要和中文总结；`post-training-screening.json` 保存候选集及纳入／排除理由。
