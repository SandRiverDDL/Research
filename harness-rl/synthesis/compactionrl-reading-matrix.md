# CompactionRL：归属、引用谱系与最近邻

核查日期：2026-10-16。范围：定向 related-work / forward-citation 核查；不是穷尽综述、查新结论或复现。

## 定位与版本

**解释 / 分类判断**：CompactionRL 属于 agentic RL，更具体是 long-horizon agentic RL 中的 learned context compaction / memory management。把任务执行和摘要生成放在同一个 policy、同一个任务结果奖励下训练，是模型学习运行机制的一种实例；不能据此把它划为与 agentic RL 并列的“harness RL”。

**原文事实**：[arXiv](https://arxiv.org/abs/2607.05378) v1 于 2026-07-06 提交，v2 于 2026-10-01 修订。当前判断以 [v2 HTML](https://arxiv.org/html/2607.05378v2) 为准；本项目早前的 §4 方法描述对应 v1，v2 方法改为 §3。

v2 §3.1：固定上下文剩余预算阈值触发摘要；摘要由同一个 trainable policy 生成，随后以摘要和最近交互重建上下文继续任务。执行和摘要共享最终任务奖励；没有单独摘要质量奖励。它学习摘要内容和任务执行，并不学习触发阈值。

v2 §3.2：critic-based PPO、token-level loss normalization、cross-segment GAE。作者明确承认跨段 GAE 是近似，而非精确重建完整轨迹的 GAE。v2 §4.3 / Table 3 新增 SUPO 对照：作者在该设置报告 CompactionRL 比 SUPO 高 4.6 / 4.9 个百分点。该结果是作者报告，未复现；不据此概括成所有任务或全部训练预算下都优于 SUPO。

**解释**：不能把它概括为首次“用 RL 学会压缩上下文”。SUPO 等更早工作已经联合训练工具使用与摘要；其具体贡献需要放在 critic、分段 loss 与跨段信用分配的组合中比较。

## 原文 related work 的领域组成

v2 §2 实际分为 Context Compaction for Long-Horizon Agents 与 Reinforcement Learning for Language Models 两个小节。下面是为阅读整理的细分，不是原文的五个独立标题。

| 领域 | 原文引用代表 | 在论文中的作用 |
|---|---|---|
| Agent 交互、记忆与反思 | ReAct、MemGPT、Reflexion、Generative Agents、MEM1 | 维持长程任务状态的基本范式 |
| 长上下文能力与评测 | Lost in the Middle、LongBench、RULER | 更长窗口不等于可靠使用全部历史 |
| Prompt / observation compression | LLMLingua、LongLLMLingua | 压缩上下文本身的背景，未必训练 agent |
| 可学习 context / memory management | SUPO、Memex(RL)、ReSum、AdaCoM、Remember When It Matters | 最直接的方法邻域；联合训练、只训练 manager、外部 summarizer 是重要区别 |
| LLM RL 与 critic / 异步优化 | PPO、RLOO、GRPO、DAPO、GSPO、VC-PPO、VAPO、SAO | 为什么使用 critic、state-dependent advantage 和单 rollout 优化 |

此外，Context-Folding 出现在 v2 §1 及参考文献中；不要把“全文引用过”与“§2 逐项讨论”混淆。

## 前序与特别近邻：reading matrix

以下“限制 / 取舍”区分原文报告与本次解释；原始摘要核查不冒充全文精读。

| Paper / source | Core idea / mechanism | 相对 CompactionRL 的关系与差别 | 限制 / 取舍、阅读边界 |
|---|---|---|---|
| [SUPO](https://arxiv.org/abs/2510.06727)，2025-10 | 周期摘要，把工具使用和 summarization 端到端纳入 RL | **最直接前序 / baseline**。CompactionRL v2 §4.3 明确对比其 GRPO 实现：rollout-level shared advantage vs learned token-level critic | 解释：共享 advantage 对段间状态差异的刻画较粗。原始摘要与 CompactionRL 对照段已核查，未重读 SUPO 全部推导 |
| [ReSum / ReSum-GRPO](https://arxiv.org/abs/2509.13313)，2025-09，最新核查 v3 | 外部摘要工具周期压缩历史，训练 agent 在摘要条件下继续搜索；通过 advantage broadcasting 覆盖分段轨迹 | **直接前序**。CompactionRL §2 区分：ReSum 不联合优化 summarizer，CompactionRL 则训练同一个 policy 的摘要 token | 解释：依赖外部摘要器质量，不能把 agent 获益直接等同于摘要策略被学习。核查原始摘要与引用上下文 |
| [Memex(RL)](https://arxiv.org/abs/2603.04257)，2026-03 | compact summaries + 稳定索引；原始经验保存在外部数据库，模型按需解引用，RL 优化读写行为 | **直接近邻**：共同解决固定窗口下的长程交互；Memex 保留可恢复的证据，CompactionRL 主要通过摘要延续 | 解释：外部存储和检索有额外接口与预算代价。核查摘要及 CompactionRL §2，未完整审阅 Memex 训练公式 |
| [Context-Folding / FoldGRPO](https://arxiv.org/abs/2510.11967)，2025-10 | 分支执行子任务，完成后 fold 成摘要；RL 与 process reward 学习分解 / 管理上下文 | **结构化上下文控制近邻**。分支 / 折叠与阈值摘要的动作结构不同 | 解释：额外的任务分解和过程奖励属于方法假设，不能和纯结果奖励无条件等同。摘要级核查 |
| [MEM1](https://arxiv.org/abs/2506.15841)，2025-06 | RL 学习每轮更新紧凑内部状态，联合记忆与推理，避免保留全部历史 | **更早的长期记忆学习前序**。偏每轮状态更新，CompactionRL 偏接近窗口上限时分段压缩 | 解释：紧凑状态同样面临信息丢失；常数状态与周期摘要的公平比较需控制任务与预算。摘要级核查 |
| [SelfCompact](https://arxiv.org/abs/2606.23525)，2026-06 | compaction tool + inference-time rubric，模型自行判断何时压缩 | **触发时机的重要对照**，早于 CompactionRL v1；无 finetuning / RL，不能当作 CompactionRL 后续 RL 方法 | 原文摘要明确无需训练；效果仍依赖模型遵循 rubric 的能力。摘要级核查 |
| [AdaCoM](https://arxiv.org/abs/2605.30785)，2026-05 | 用 RL 训练外部 context manager，task agent 保持冻结 | **训练对象不同的近邻**：优化 manager，而不是联合训练执行与摘要的同一个模型 | 原文面向冻结 / 闭源 action agents；不能直接迁移为联合训练结论。摘要及 CompactionRL §2 核查 |
| [Remember When It Matters](https://arxiv.org/abs/2607.08716)，2026-07 | 单独 memory agent 维护结构化 memory bank，选择注入 reminder 或保持沉默 | CompactionRL **v2 引用**的邻近 manager 方法；晚于其 v1，不当作 v1 的前序基础 | 核查摘要；独立模块 / 选择性提示与历史摘要替换的机制不同，未逐项复核训练细节 |

## 谁引用了它：原文确认清单

本次至少确认 **10 篇论文**的正文或 bibliography 包含 CompactionRL，不能据此声称总引用数恰好为 10。以下“后续类型”是本次解释，不是作者统一采用的分类。

| 引用论文 | 原文证据位置 | 后续类型 / 具体关系 |
|---|---|---|
| [Occamy-1.0](https://arxiv.org/html/2609.11977) | §5.2、Appendix C.2 | **明确采用其方法**：作者写明 following CompactionRL and SAO，使用 trainable compaction、segment-wise PPO 与跨段 correction；是真正的 recipe 后续使用 |
| [AutoCompact](https://arxiv.org/html/2610.02163v1) | §1、§3.1 / Table 1、§4 | **直接问题延续与实验对照**：由固定阈值走向主动学习 when / what / how to continue。Judge-corrected SFT 后用 GRPO；并非沿用 CompactionRL 的 critic / GAE 算法 |
| [CAMG-RL](https://arxiv.org/html/2609.34422v1) | §6 / Table 2、bibliography [29] | **近邻替代机制 + baseline**：把普通文件操作训练成 memory，不只把历史压成摘要；同尺寸 4B 对照中采用 CompactionRL baseline。该对比不是直接拿原论文 30B / 106B 的数字来比较 |
| [Continuous Context Management](https://arxiv.org/html/2609.35540) | §1、bibliography Li et al. 2026c | **同问题的新 formulation**：每轮更新 memory，GRPO + full-history privileged distillation。原文明确 MEM1 是其最接近的 formulation；不能说它完全由 CompactionRL 演化而来 |
| [ReFold](https://arxiv.org/html/2610.07863) | Related Work Context management、bibliography Li et al. 2026b | **训练免除的替代对照**：保留底层历史，只压缩呈现上下文，强调可逆性；引用 CompactionRL 不表示采用其 RL 算法 |
| [FC-SWE](https://arxiv.org/html/2610.07898) | related-work 中 cross-boundary advantage 讨论、bibliography Li et al. 2026b | 邻近的 long-horizon / recovery credit assignment；当前只核查摘要与引用段，不据此称为 compaction 方法后续 |
| [Rethinking Critic Learning in PPO: Understanding and Mitigating Value Flattening](https://arxiv.org/html/2609.18708) | bibliography Li et al. 2026b，引用回链 §2.1 | critic learning 背景引用；未确认继承 CompactionRL 算法 |
| [Context Language Models](https://arxiv.org/html/2609.37725) | bibliography Li et al. 2026d | context-as-file / 自主管理上下文的邻近路线；当前确认引用与摘要，未确认沿用 CompactionRL 优化公式 |
| [TrajectoryDB](https://arxiv.org/html/2609.07782) | bibliography Li et al. 2026 | 轨迹数据管理方向的引用；与直接 RL 方法 follow-up 区分 |
| [Does an Agent's History Tell You When Compaction Will Hurt?](https://arxiv.org/html/2610.08722) | bibliography [5] | TRACE paired replay 中的 compaction 伤害诊断；非训练算法延续。当前只核查摘要和引用 |

## 最值得读的后续：方法与边界

1. **Occamy-1.0**：若要看“有没有人实际 follow 它的训练 recipe”，先读 Appendix C.2。该报告还有其他训练与合并阶段，最终性能不能全归因于 CompactionRL，当前未见隔离此组件的充分因果证据。
2. **AutoCompact**：若要看“固定阈值之后还能做什么”，先读 §2–3。作者明确其研究在单 scaffold 下；RL 训练 32K、评测可到 256K。Table 1 的 CompactionRL 采用 16K 强制压缩而主动方法采用 256K，不能只看横排行数就把全部差距归给触发学习；其共享 16K 的分析提供另外一组证据。
3. **CAMG-RL**：若要看“摘要压缩之外的记忆机制”，先读 §4–6。作者报告 4B 对照平均成功率 54.4% vs CompactionRL 48.0%，是自己的四环境设置；实验只到 9B，memory 限单 episode / 单用户。
4. **CCM**：若要看“每一步都维护紧凑状态，以及 full-history teacher 提供学习信号”，先读 §2–4。收益存在任务和模型规模差异；原文报告某些大模型无训练 CCM 会损失成功率，不能只用 token 节省判断成功。

**解释 / 阅读优先级**：SUPO → CompactionRL v2 → AutoCompact → Occamy Appendix C.2 → Memex(RL) / CAMG-RL → MEM1 / CCM。此排序是回答用户问题的阅读建议，不是领域重要性或 novelty 排名。

## 检索与验证边界

- 两阶段检索：标题 / 摘要与版本发现；筛选后查原始 HTML、reference 条目和对应正文段。OpenAlex 的 13 条全文检索结果只用于发现候选，排除了目标论文自身、PREreview 与无当前一手核查的 survey 候选。
- Semantic Scholar API 本次返回 429；OpenAlex 对目标记录返回 cited_by_count=0，与逐篇原文已确认的引用不一致。因此不报告数据库“总引用数”，也不把 0 当作没有人引用。
- ACM v1 的原始 HTML 未找到 CompactionRL 名称或 2607.05378；社交媒体提及不当作论文引用。可能的其他版本变化未穷尽核查。
- 全部近邻未做统一完整精读。CompactionRL v2 已定向核查 §2–3、§4.3 / Table 3 与 Limitations；后续的核查深度分别写在上表，不冒充复现。
- 未下载 PDF、未导入 Zotero、未写正式 L1 cards、未启动训练或实验规划。原文 citation 与本地链接核查是本次验证；项目 helper 的 0-card 验证不代表内容验证。
