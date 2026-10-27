我建议优先保留 **ASTRA-05：回看后验→在线信念学习**，以及高风险的 **ASTRA-03：teacher 辅助的纯任务 RL 控制变量**。前者改变传授的知识，后者改变 teacher 参与学习的方式；两者都无需逐状态重置或分叉。当前只是 **same-family provisional** 判断，不是录用保证。

下表覆盖全部15组。**PROCEED** 表示具体差异通过本轮早期查新；**CAUTION** 均注明差异薄弱在哪里。没有足够证据判整项 ABANDON；这也不意味着15项都值得投入。

| 候选 | 最近工作与可核验差异 | 最强反对意见、规模风险与最便宜否证 | 判定 |
|---|---|---|---|
| A01 事实视图 teacher | SOPD、GC-OPD；teacher 删除未经验证的 reasoning，保留实际交互证据，生成决策目标 | 可能只是换 prompt，或收益来自 step-wise generation。固定 action/observation，置换错误 reasoning；若目标几乎不变，靶点不存在。每轮一次短 teacher 生成，可批量化 | **PROCEED** |
| A02 计划组合探索 | TCOD、层次 options；将 teacher 的多策略组合分布传给自主执行的 student | 计划多样性可能只是语言多样性，仍属数据增广。固定 teacher tokens 与 rollout 数，对比普通多样化计划；有效成功策略覆盖不增即止 | **CAUTION** |
| A03 控制变量 | Q-Prop、vOPD；teacher 仅降低**任务回报梯度**方差，而非继续改变优化目标 | 控制变量恒等式已知；仅把 critic 特征换成 teacher 概率不足。全词表求和可能吃掉收益；先比较同成本梯度方差与普通 critic | **CAUTION，推荐** |
| A04/S04 依赖程序 | options、ArCHer、GC-OPD；蒸馏可重组的前置关系和终止条件 | 核心收益可能由人工契约检测提供。程序数随领域增长；对比等长线性计划，在未见组合上无收益即否证 | **CAUTION** |
| A05 回看信念后验 | MemOPD、SERL、privileged POMDP learning；将 hindsight 变成信念分布监督，而非全知 action | teacher 后验未必校准，变量选择可能偷带未来信息。每轨迹一次标注；先测证据出现前后的校准与更新 | **PROCEED，首选** |
| A06 知识→取证需求 | Search-R1、GC-OPD；蒸馏缺失证据的识别与获取，而非知识答案 | 尚未与普通 query distillation 拉开方法差异；工具成本可能成为收益来源。固定检索次数，用新事实替换旧知识后检验 | **CAUTION** |
| A07 随机 horizon | randomized truncation、TurnOPD；固定平均预算下校正深层信号的存活概率 | 随机截断估计已有基础，真正差异须落在可用的低方差估计；长尾拖慢同步。与同 horizon 覆盖、无校正对照比较 | **CAUTION** |
| A08 可证明行动类 | ASL、ActionOPD；以 schema 能证明的等价关系聚合概率 | 目前可能只剩格式规范化。开放 action 集求和昂贵；若 canonicalization 即复现收益，则不足成篇 | **CAUTION** |
| S01 观察差分 | ActionOPD、反事实增广；监督跨观察的策略响应关系 | 差分 loss 是否超越同一批成对数据尚不清楚；自然配对稀疏。与相同样本普通 OPD 对比即可快速否证 | **CAUTION** |
| S02 信念撤销 | MemOPD、GC-OPD；显式学习撤销失效判断的操作 | 目前可能是 memory 摘要换 schema。失败轨迹标注易有选择偏差；对比等长摘要与解释，不能只比无 memory | **CAUTION** |
| S03 效果等价 | **ASL** 已有转移等价集；剩余差异是用真实交互学习并拆分错误类 | 相同观察不保证相同长期效果；自然数据缺反事实支持。先测隐藏后果不同的行动是否被错误合并，再谈收益 | **CAUTION** |
| S05 后验势函数 | potential shaping、value distillation；新增的是 teacher 证据后验这个价值来源 | shaping 与对应 critic 可代数等价；不能把重新参数化称新信用分配。与 teacher 初始化 critic 比较，成本约每轨迹两次评分 | **CAUTION** |
| S06 纠正信号摊销 | proxy teacher、active distillation；预测真实外部 teacher 的纠正量并在线刷新 | 当前主体仍是蒸馏 teacher scorer，需新结果证明漂移下的经济性。固定总算力，对比随机查询与简单缓存 | **CAUTION** |
| S07 可逆错误免疫 | TCOD、DASH、recovery curriculum；teacher 主动挑选教学偏离 | 可能只是训练扰动增广；恢复额外步数不可忽略。等步数随机扰动若等效，teacher 选择机制即失败 | **CAUTION** |
| S08 黑盒密度比 | **GAD**、GAIL；剩余差异是动态 agent 状态上的低查询条件估计 | 核心“teacher/student 判别器→策略奖励”已有。判别器可能学风格；与同预算 GAD、ActionOPD、action SFT 比较 | **CAUTION** |

这里有两个应明确加入最终报告的直接先例。**ASL** §3.2 已定义 \(S(a)=T(s,a)\) 及其等价行动集合，§3.3 用 world model 预测状态变化；它还包含外部 teacher reference action 与环境奖励结合的 RL，以及文本输入实验，因此不能因“GUI”标签忽略。S03 的真实转移校验仍有差异，但“首次蒸馏效果等价类”已不能主张。[ASL 原文](https://arxiv.org/html/2506.17697v3#S3)

**GAD** §2 已在同 prompt 下训练 teacher/student 判别器，在线刷新 student 负样本，并把判别器分数作为 GRPO 奖励。S08 不能仅靠“条件密度比”重新命名获得方法贡献。[GAD 原文](https://arxiv.org/html/2511.10643v3#S2)

**首选 A05：用未来监督学习现在应有的不确定性。** 最小机制应只有：外部 teacher 为固定的任务相关变量标注轨迹后验；student 只看当前历史预测其分布；策略读取自己的信念并由任务奖励学习行动。不要再叠加图、分叉和 verifier。

它有一个成立但容易被误说的统计依据：若 teacher 给出的是真实 smoothing posterior，则
\[
\mathbb E[p(z_t\mid\tau)\mid h_t]=p(z_t\mid h_t).
\]
因此用 forward cross-entropy 学习完整轨迹标签，人口风险的最优预测仍是当前历史下的 posterior。**训练标签看未来本身不等于泄漏**；真正的问题是 teacher 不校准、student 输入含未来、变量 schema 由未来决定，或只标失败轨迹而改变条件分布。Privileged POMDP 文献已经说明“全知 teacher action 直接蒸馏”并非一般可靠，因此不能把 belief learning 本身称首次提出。[相关原文 §§3–5](https://arxiv.org/html/2412.00985#S3)

必要对照是 MemOPD 式摘要、当前 prefix teacher 标签、确定性 hindsight 标签，以及使用相同标签但策略不读取 belief 的辅助训练。**杀死条件**：收益只存在于见过的任务事实；证据前异常自信；或普通等长摘要完全复现收益。两年后它仍可能重要：更强 teacher 不能替部署 student 观察尚未获取的环境信息，但能提供更准确的后验监督。

**第二选 A03：让 teacher 帮助估计任务梯度，不替任务规定答案。** 先共同 OPD 热身，随后令 \(c(h,a)\) 为冻结、独立拟合的 teacher 辅助回报预测器，使用
\[
g=\nabla\log\pi(a\mid h)[G-b(h)-c(h,a)]
+\sum_u\pi(u\mid h)c(h,u)\nabla\log\pi(u\mid h).
\]
两项中的 \(c\) 在条件期望下抵消。条件包括 on-policy 采样、正确回报估计、校准器与本条样本独立或交叉拟合，以及期望项精确或无偏估计。**stop-gradient 不会自动修复同批过拟合；PPO clipping、GRPO 标准差归一化和遗漏词表尾部也不会自动保留该无偏结论。**

vOPD 降低的是 OPD 梯度方差，使用 action-independent negative-KL baseline；它没有包含这里的纯 task-RL 目标。但 Q-Prop 已有 action-dependent control variate，故新贡献必须是 teacher 提供了普通 critic 难以低成本获得的结构，而非这条恒等式。[vOPD §3](https://arxiv.org/html/2605.07865#S3)、[Q-Prop](https://research.google/pubs/q-prop-sample-efficient-policy-gradient-with-an-off-policy-critic/)

先在有限工具行动集做精确求和，对照普通 critic、无 teacher 的同容量校准器、ATOD、热身后纯 RL。**杀死条件**：同总成本下方差不降；收益来自残留 imitation 项；或只在全词表高成本版本成立。全零 reward 冷启动不能靠无偏性创造有用的期望梯度。更强 teacher 可能提高相关性，但这一耐久价值仍是待验证假设。

另两处数学边界不能略过：S05 若采用
\(r'=r+\gamma\Phi(h')-\Phi(h)\)、终点势为零，并令 \(V'=V-\Phi\)，则 TD residual 逐项相同；其贡献只能来自更好的价值先验或优化实现，不能宣称产生了新的任务信用。[经典等价结果](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/potential_based_shaping_equals_initialization.pdf) S03 的效果等价则至少要保留奖励和相关后继分布；仅凭相同下一条文字观察无法识别它，未访问行动的等价性也无法从自然数据凭空证明。

我认为 ATOD 最有价值的三个不足是：

1. **监督内容没有被修复。** 作者在附录A已承认 teacher 可靠性；我进一步推断，错误 reasoning、未知信息和真实错误被混进同一种 token gap，提高权重可能放大错误目标。这支持 A05，也让 A01 值得先做便宜验证。
2. **“分配更好”与“监督更弱”没有分离。** \(w\in[0,1]\) 同时改变轮间分配和总体 OPD 强度；表2缺 mean-weight、梯度规模匹配与打乱轮权重对照。附录B的集中界不证明任务价值；作者已明确绝对 log-ratio 不是无偏 KL，不能将其当数学错误。
3. **长程与规模化结论证据有限。** 深轮诊断条件于仍未结束的 episode，存在组成变化；Search-QA 上限4轮，主比较按150更新步而非总计算量，主表未报告跨 seed 不确定性。这些是本次推断的证据缺口，不是作者已承认的全部局限。[ATOD §§4–5、附录A–C](https://arxiv.org/html/2606.27814v6)

本次未改文件、未跑实验；推荐应先通过上述低成本否证，再进入方法项目。
