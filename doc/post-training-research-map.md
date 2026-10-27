# 后训练研究分类与会议证据

更新日期：2026-10-12。

后训练可以同时按能力目标、学习机制和研究贡献分类。只按推理、agent、安全等目标整理，会把数据、奖励、蒸馏、优化和训练动力学的区别藏起来。这份地图用于建立研究广度、定位论文贡献，并识别可能形成方法族的机制变化。

这里的分类是研究组织框架，允许交叉归类；不是会议官方 taxonomy，也不改变现有项目目录或 card schema。会议实例与趋势解释单独保留，便于更新证据而不反复修改整个框架。

## 三个分类轴

| 分类轴 | 核心问题 | 例子 |
| --- | --- | --- |
| 能力与行为目标 | 希望模型会做什么、表现出什么行为？ | 数学推理、coding、工具使用、长程 agent、多模态、多语言、长上下文、安全、真实性、个性化 |
| 学习机制与研究环节 | 改变学习过程的哪一部分？ | 数据与课程、监督与反馈、优化、能力迁移、探索、持续适应、计算与系统 |
| 研究贡献类型 | 论文提供什么知识或工具？ | 新方法、机制解释、理论、benchmark、数据集、训练系统、受控实证研究 |

这三个轴不要求每篇论文只能选一个标签。例如，一篇数学推理论文可以同时研究课程与探索，贡献类型是新算法加机制分析。

## 后训练的九个研究板块

### 数据与课程

研究学什么、按什么顺序学，以及数据如何匹配当前策略。包括 SFT 冷启动数据、合成任务、成功与失败轨迹、轨迹修复、样本选择、难度控制和动态课程。判断贡献时，要区分为某个任务构建数据集与提出可迁移的数据机制。

### 监督与反馈

研究学习信号从哪里来、包含什么信息、是否可靠。包括偏好、标量奖励、过程奖励、验证器、生成式奖励模型、rubric、自然语言反馈，以及弱监督、无标准答案或无任务验证器的学习。

反馈质量与策略更新方式是两个不同问题。一个更强的 reward model 不自动意味着更好的下游策略，需要在优化压力下检验。

### 优化与信用分配

研究如何把信号变成参数更新。包括 advantage、baseline、clipping、KL、损失函数，以及 token、step、turn、trajectory 级信用分配；也包括 on-policy、off-policy、重要性采样、经验回放和分层策略优化。GRPO 最直接落在这里。

### 能力迁移与知识内化

研究如何把教师、上下文、反馈或搜索产生的能力迁移到模型参数。包括离线与在线蒸馏、自蒸馏、多教师蒸馏、上下文蒸馏，以及跨规模、架构、模态迁移。OPD 最直接落在这里，也与监督、优化、探索和系统相交。

关键问题包括 teacher–student gap、监督保真、能力保持，以及被压缩的是行为模式还是可泛化能力。

### 探索与训练动力学

研究训练为什么进步、停滞或坍塌。包括探索覆盖、entropy、多样性、pass@k、格式坍塌、梯度失衡和训练稳定性。需要区分新能力增长、已有解法概率重分配与利用评测捷径。

这一板块既产生改进方法，也产生解释其他方法有效性与边界的机制论文。

### 学习闭环与生命周期

研究何时学习、跨多少次尝试学习、系统如何参与自身更新。

- Self-play：系统参与生成任务、对手或训练交互。
- Meta-RL：通过训练获得跨尝试适应的能力；推理时适应可以发生在上下文中，不必更新参数。
- Continual post-training：任务不断到来时，更新能力并保留旧能力。
- Test-time training 或 RL：针对当前任务继续更新参数。
- RSI：递归自我改进的上层研究议程，可以采用上述机制；不能直接等同于某个固定 loss 或 recipe。

这些机制可以组合。普通自训练循环也不能仅凭名字被判定为具有持续递归能力增长。

### 计算与训练系统

训练侧研究 rollout 吞吐、异步、陈旧样本、回放、显存和参数高效更新；部署侧研究通过训练获得预算分配、思考长度、工具调用和停止决策。

当系统改变样本分布、采样策略和更新延迟时，系统与优化算法需要共同设计。纯推理加速工作属于邻近领域，只有与学习目标或更新机制相关时才纳入后训练核心。

### 对齐目标与可控适配

研究为谁优化、按什么标准优化。安全之外，还包括个性化偏好、多元价值、多目标权衡、真实性、置信度校准、澄清和拒答。隐私、遗忘与知识编辑可作为相邻适配领域，是否纳入取决于具体训练贡献。

不能把所有用户、场景与行为目标都默认压缩成同一个标量标准。

### 测量理论与机制审计

研究训练收益是否真实、结论在哪些条件下成立。包括泛化与记忆、能力与概率重分配、reward hacking、偏好梯度效用、评测污染、对照公平性和样本复杂度。

这块横跨前八块，单列是为了保留机制、理论与评测研究的位置，避免把研究价值等同于提出新算法。

## 常见名称在地图中的位置

| 名称 | 主要位置 | 层级与边界 |
| --- | --- | --- |
| GRPO | 优化与信用分配 | 具体策略优化算法，可衍生方法族 |
| OPD | 能力迁移与知识内化 | 一类监督与训练组织方式，不是单个 loss |
| RLVR | 监督与反馈，加策略优化 | 指明奖励可验证，不唯一指定优化算法 |
| Self-play | 数据与课程，加学习闭环 | 定义训练交互的生成方式，可使用不同优化器 |
| Meta-RL | 学习闭环与生命周期 | 训练学习和适应的能力 |
| Test-time RL | 学习生命周期，加策略优化 | 在当前任务上进行 RL 更新 |
| RSI | 学习闭环的上层议程 | 自我改进目标与系统循环，不能与具体算法简单并列 |

## 本地会议证据的覆盖范围

本次分类使用本地材料，未进行新增联网检索。以下快照支持研究方向的存在，不支持全领域热度排名或未来爆发预测。

| 来源 | 覆盖 | 证据限制 |
| --- | --- | --- |
| EMNLP 2026 展示日程，2026-10-05 快照 | 5,611 个唯一条目；MAIN 2,710、FIND 2,487、IND 265、DEMO 86、TACL 50、CL 13；主要扫描 MAIN 与 FIND 的 5,197 条标题 | 无摘要；展示日程不保证等同最终录用全集；TACL 与 CL 报告不能计作 EMNLP 新录用 |
| NeurIPS 2026 OPD 专题 | 此前用户指定的 19 篇，已有会议身份匹配记录 | 按 OPD 预先选择的样本；不能估计 NeurIPS 整体后训练方向分布 |
| ICML 2026 本地 metadata 与摘要缓存 | 按题目检索、读取部分摘要作为机制解释补充 | 不是本次主要会议样本；没有逐篇全文审计或独立复现 |

EMNLP 的 keyword 初筛存在漏检和误检，且各组重叠，因此不保存为领域论文数或占比。标题级证据只能支持问题定位，不能支持具体算法机制与实验收益。

## EMNLP 2026 的代表性标题

以下均来自本地日程的 MAIN 条目。归类是阅读解释；未核对摘要的条目不据此推断方法有效性。

| 板块 | Paper ID | 标题 |
| --- | --- | --- |
| 数据与课程 | 1326-MAIN | Beyond SFT-Optimality: Cold-Start Data Selection for Reinforcement Learning via Gradient Subspace Coverage |
| 数据与课程 | 1371-MAIN | Expanding the Solvable Frontier: Policy-Adaptive Curriculum Learning for Reasoning RL |
| 监督与反馈 | 1265-MAIN | The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment |
| 监督与反馈 | 4293-MAIN | ScalePRM: Training Process Reward Models by Scaling Verification Compute Without Ground Truth |
| 优化与信用分配 | 4542-MAIN | Representation-Aware Advantage Estimation: Your Reward Model Provides More Than A Scalar Output |
| 优化与信用分配 | 3382-MAIN | Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies |
| 探索与训练动力学 | 5119-MAIN | Format Collapse in Policy Optimization for LLM Reasoning |
| 探索与训练动力学 | 5104-MAIN | Cast a Wider Net: Coordinated Pass@K Policy Optimization for Code Reasoning |
| 学习生命周期 | 736-MAIN | PrimeTTT: Priming Test-Time Training for LLMs via Meta-Learned Initialization |
| 学习生命周期 | 3483-MAIN | Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift |
| 计算与系统 | 4800-MAIN | SPIRE: Unifying Partial Rollouts, Replay, and Asynchrony in LLM Reinforcement Learning via Segment-wise Prefix Importance Sampling |
| 计算与系统 | 1096-MAIN | BORA-BUDGET: Learning When to Think Under a Token Budget |
| 对齐目标 | 4763-MAIN | Personalized Alignment of Language Models with Human Value Profiles |
| 对齐目标 | 5290-MAIN | MoPLEx: Estimating Plackett-Luce Mixture Models for Multi-Objective Alignment |
| 对齐目标 | 4241-MAIN | Ask, Condition or Abstain: Reinforcement Learning for Missing-Premise Reasoning |
| 机制审计 | 6549-MAIN | Not All Preferences Deserve Gradients: Understanding Gradient Utility in Offline Reasoning Alignment |
| 机制审计 | 5924-MAIN | Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR |

能力迁移的会议例子可复用已有 [EMNLP OPD 分类与摘要级总结](../opd/synthesis/reading/emnlp-2026-opd-overview.md)，无需在此重复整个专题。

## ICML 2026 的摘要级补充

以下是作者在摘要中的方法描述，不能直接视为普遍成立的实验结论。

- **Escaping the Verifier: Learning to Reason via Demonstrations**，本地 ID `61507`：RARO 从专家示范出发，通过 policy 与 relativistic critic 的对抗学习，研究缺少任务验证器时的推理训练。对应监督来源与学习机制。
- **Provable Sample Efficiency of Curriculum Post-Training for Transformer Reasoning**，本地 ID `62941`：在抽象推理树与特定充分条件下，分析逐渐增加推理深度或减少提示的课程策略。对应课程学习与样本复杂度理论，结论不能直接推广至任意真实 LLM 任务。
- **D-ARL: A Distribution-Matched Asynchronous Reinforcement Learning Framework for Language Reasoning**，本地 ID `60620`：围绕异步采样导致的策略分布差异，结合回放样本选择与多行为策略优化。对应训练系统与策略更新的交叉。

## 从会议快照得到的研究解释

以下是候选趋势解释；没有跨年份统一统计，不能断言增长速度或竞争程度。

1. **学习单位扩展**：从单条回答，扩展到多轮轨迹、多次尝试、连续任务及生成—反馈—更新闭环。
2. **监督信息丰富化**：过程反馈、rubric、语言反馈、奖励模型表示与可执行验证提供不同于单一分数的信息。
3. **数据优化与系统耦合**：课程依赖当前策略，采样影响梯度，异步改变样本分布。
4. **优化目标增多**：除平均准确率，还关注多样性、成本、个性化、能力保持、校准与可靠性。
5. **机制审计有独立价值**：坍塌、奖励漏洞、梯度效用与泛化边界本身可以构成研究贡献。

要判断哪个方向正在升温，需要按统一口径补摘要、按首次出现时间去重、统计独立团队与后续采用情况。单次录用名单不足以判断某个方向是蓝海。

## 用于阅读与选题

读一篇论文时，先完成一句话：

> 在某种能力或场景上，通过改变数据、监督、更新、探索或学习闭环，解决一个具体限制，并用相应证据验证。

接着区分贡献发生在哪里：成熟 recipe 的任务应用、已有机制的局部改进，还是监督来源、学习单位、更新对象或训练闭环的改变。后一类更值得检验是否能扩展为方法族，但还要验证通用性、成本与直接竞争者。

这份地图以大模型后训练为范围，不是全部 AI 研究的分类。现有主题按 [Research 根约定](../AGENTS.md) 分工：数据机制进入 agent-data，奖励与策略更新进入 agentic-rl，蒸馏进入 opd，完整模型与训练 recipe 的横向比较进入 foundation-model-systems。地图中的一个板块不自动对应一个新目录。

## 证据入口

- [EMNLP 本地快照来源与核查说明](../opd/tmp/emnlp-2026-index/README.md)
- [EMNLP 日程 CSV](../opd/tmp/emnlp-2026-index/emnlp-2026-presenter-schedule.csv)：用上表 Paper ID 精确检索。
- [NeurIPS OPD 官方匹配记录](../opd/tmp/neurips-2026-opd/official-matches.json)
- [OPD 状态与既有会议核查记录](../opd/doc/memory/STATE.md)
- [ICML metadata 缓存](../opd/tmp/icml-2026-index/icml-2026-orals-posters.json)
- [ICML 摘要缓存](../opd/tmp/icml-2026-index/icml-2026-abstracts.json)：按本地 ID 检索。

上述 tmp 缓存可能不随 Git 同步。本文保留论文标题和 ID 作为恢复锚点；缓存缺失时，不应把未重新核实的摘要判断升级为全文结论。
