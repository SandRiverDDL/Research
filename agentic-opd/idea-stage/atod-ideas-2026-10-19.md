# ATOD 全文阅读与方法选题

> 状态修正（2026-10-19）：用户否定本报告候选的创新度，assistant撤回下文两条“主推荐”的判断。保留原分析与评审记录以便追溯，不将其作为当前推荐或已认可课题。用户以增加teacher熵说明更直接的机制切口，尚未确认该方向为新选题。

日期：2026-10-19。对象：[ATOD 2606.27814v6](https://arxiv.org/html/2606.27814v6)。已读正文§1–6、附录A–D、表1–4与图1–13，依据原HTML及内嵌图；未做代码审计或独立复现。

本轮生成16项，机械合并为15组，全部送fresh Astra审阅；保留2条方法主候选、1条先验证靶点的储备，其余12组暂不投入。全部是 **same-family provisional / outcome pending**。针对性查新截至本日，不能视为穷尽新颖性证明。没有运行GPU pilot。

**我的选择：首先验证“从回看后验学习在线信念”，同时保留“teacher辅助的任务RL控制变量”这一高风险方向。** 二者分别改变蒸馏的内容和teacher参与优化的方式。只有同预算实验证明核心机制，才有顶会方法论文的潜力。用户尚未选择方向。

## 1. 论文做了什么，证据支持到哪里

【作者方法】ATOD在student自己的轨迹上混合teacher log-ratio监督与GRPO；前者随训练减弱，后者增强。T-DUR用每轮sampled surprisal与绝对log-ratio的轨迹内min–max值构造权重：

\[
A_t=\kappa(s)w_{k(t)}[\log\pi_T(a_t|h_t)-\log\pi_S(a_t|h_t)]+\rho(s)A^{\rm GRPO},\qquad
w_k=1-(1-\tilde d_k)(1-\tilde h_k).
\]

【作者报告】1.7B主表平均成功率为71.58，对应OPD为64.91；论文还包含退火和权重组件消融。结果支持这套组合在所测设置中有效，不自动证明分歧代表教学价值或训练成本最优。[§4、Table 1、§5.2](https://arxiv.org/html/2606.27814v6#S4)

以下“欠缺”是我的分析，并非作者实验证明的失败。

| 欠缺 | 依据及推断 | 对选题的含义 |
|---|---|---|
| **没有拆开“不知道”“推错了”“teacher也错了”** | T-DUR针对token统计加权；附录B的集中界不涉及teacher建议带来的任务收益。高不确定可能来自信息尚未观察到，而非student能力不足 | 应研究监督内容与信息条件，不能只再换一种uncertainty gate |
| **分配与总强度混在一起** | 所有权重在[0,1]；轮间分配变化同时降低OPD总贡献。现有组件消融未隔离mean-weight、梯度规模与权重排列 | 先对比同均值、同梯度规模、打乱轮权重；这是方法验证，不是整篇贡献 |
| **轨迹内相对值缺乏绝对含义** | min–max依赖其他轮的极值；同一局部状态可因后面另一轮变化而得到不同权重 | 不宜把此权重解释为已校准的可学习性／teacher可靠性 |
| **深度图不是因果证据** | Fig.8的深轮统计条件于episode尚未结束；论文显示样本数随深度减少。困难任务留下、简单任务退出会改变组成 | 深轮仍不确定，不等于给深轮更多teacher监督必然更有效 |
| **长程与成本结论边界较窄** | Search-QA上限4轮；主比较按150更新步，主表未报告跨seed误差。gate需要teacher分数，不自动节省teacher forward | 应同时报告成功率、teacher计算、环境步数、总时间；不能把平均轨迹长度直接当效率 |

出处：[权重§4.3](https://arxiv.org/html/2606.27814v6#S4.SS3)、[理论附录B](https://arxiv.org/html/2606.27814v6#A2)、[消融§5](https://arxiv.org/html/2606.27814v6#S5)、[设置C.3](https://arxiv.org/html/2606.27814v6#A3.SS3)、[深度诊断C.6](https://arxiv.org/html/2606.27814v6#A3.SS6)。

【代数例子，非实验】假设三轮的d和h均为(0.1,0.2,0.3)，中间轮权重为0.75。仅将第三轮两项都改成10，中间轮权重变成约0.0201。它说明相对归一化的性质，不证明ATOD实际训练因此受损。

公平评价：作者已承认teacher质量、跨family等局限；已做固定混合与退火参数消融；也明确绝对log-ratio不是无偏KL。不能把这些写成作者完全忽略或数学错误。Figure 8的轨迹置信区间也不等于跨训练seed置信区间。

## 2. 主候选一：从回看后验学习在线信念

**实际怎么做：**

1. Student正常执行完整轨迹。对任务相关变量使用预先定义或只由当前prefix确定的schema，例如“目标物品可能在哪”“哪个必要条件已经满足”。外部teacher回看真实交互记录，批量输出各时间点变量的概率分布；未获得证据的变量仍允许不确定。
2. Student只看当时历史，预测同一组变量的分布，用forward cross-entropy拟合teacher的回看标签。既采成功也采失败，避免把标签过程变成成功条件下的选择偏差。
3. 行动策略读取student自己预测的belief，由任务reward学习取证、行动与终止。训练与部署都不把teacher回看答案放入actor输入。可使用共同的OPD热身，主阶段保留belief监督与任务RL。

核心损失只有一项新增监督：

\[
L_{\rm belief}=\mathbb E_{\tau,t}\left[-\sum_z q_T(z_t=z\mid\tau)\log b_\theta(z\mid h_t)\right],\qquad
L=L_{\rm taskRL}+\lambda L_{\rm belief}.
\]

这是对项目旧“证据ledger”候选的深入，不是全新发现。变化在于**概率信念、回看监督与部署时真实使用**，而不是添加更多结构字段。

【待验证假设】一部分长程失误来自对未知事实过早做确定判断。让student学会在信息不足时保留多个可能性、证据出现后更新，比强化某条teacher action更有利于主动取证和恢复。

例如物品在两个柜子之一，打开前历史无法区分位置；好的student应保留不确定性并选择查看。结束后teacher知道实际位置，训练应利用这一标签分布学习当前可辨识的信息，而不是把“已知正确位置时直接取物”的全知行动教给student。**不指控ATOD使用了未来信息**；这里是在设计新的teacher信号。

【理论抓手与边界】若q_T是真实、校准的smoothing posterior，训练分布一致且student输入只有h_t，则塔式法则给出

\[
\mathbb E[q_T(z_t\mid\tau)\mid h_t]=p(z_t\mid h_t).
\]

因此总体forward-CE最优解可学习filtering posterior。未来作为训练标签本身不等于泄漏；真正危险的是teacher误校准、输入含未来、事后选择变量、有限样本记忆，以及只选特定结果的轨迹。此恒等式不是新的定理，也不保证有限神经网络的校准或任务收益。若每次终局都完全揭示变量，正确one-hot hindsight标签同样可成立；不能预设soft标签必胜。

**为什么可能成篇：** 若能证明agent OPD中“教师的更强行动能力”与“部署时可获得的信息”有结构性错配，并用一种可批量生成的belief目标解决，在未见任务／信息延迟／证据冲突上保持收益，这比权重调参更有普适性。两年后模型更强也无法凭空观察尚未获得的环境信息。

**最近工作与不能主张的点：**

- [Privileged POMDP learning §§3、5](https://arxiv.org/html/2412.00985v3#S3)已研究全知teacher action蒸馏的失败与belief learning；[Meta-RL as task inference](https://arxiv.org/abs/1905.06424)已利用privileged信息学习task belief。不能主张首次用belief或事后状态监督。
- [SERL §3](https://arxiv.org/html/2605.19447v1#S3)已有hindsight teacher与action训练；[GC-OPD §3](https://arxiv.org/html/2609.37522v1#S3)已有带历史的teacher记录及student hindsight。剩余差异应是**从普通student交互日志获取软后验，学习部署时可辨识的信念，直接用于策略**。
- MemOPD解决memory重写后teacher/student真实调用上下文对齐，不能把它简化成普通摘要辅助任务。它应作为完整实现对照；另加等长摘要基线。
- [Prospective Hindsight](https://arxiv.org/abs/2610.02740)按预测与事后评估差异重加权；[Belief-Aware GSAC](https://arxiv.org/abs/2605.26155)研究不确定性驱动的蒸馏系数。二者本轮只读摘要，具体差异仍需后续method级核对。

**最便宜的验证：** 先用固定student日志与一组可独立核验隐藏事实的诊断任务，检查teacher标签与student预测在证据前后的Brier／log score、错误自信率和更新方向。再做小规模方法pilot：普通OPD／ATOD、同长度摘要、prefix-only teacher标签、hindsight标签、策略不读取belief的辅助训练。所有方法使用同样的任务信息，匹配标注与推理tokens；测未见对象与未见组合上的取证行为、成功率和环境成本。

**停止条件：** teacher后验无法校准；证据出现前student变得异常自信；效果只来自记住具体事实；摘要基线或普通状态分类即可完全复现；belief改善但决策无改善。需要跨任务可用的变量接口，若每个新域都靠大量手写schema，规模化价值显著下降。

**成本与状态：** 一次批量teacher调用可标一条轨迹，但输出量仍随turn数×变量数增长；不能把“一次调用”写成O(1)计算。部署增加短belief输出或轻量预测头，其延迟必须计入。风险中高；新颖性为暂定，有明确经典近邻；未跑pilot。

## 3. 主候选二：把teacher变成任务RL的控制变量

**实际怎么做：**

1. 各方法使用相同OPD热身，保证基础执行能力。之后student继续自主rollout，以环境回报为优化目标。
2. 用历史批次或交叉拟合，学习一个廉价c(h,a)：把teacher对当前候选token／行动的分数校准成student未来回报的预测。更新actor时冻结c；不额外采teacher环境轨迹。
3. 从采样梯度中减去这个预测，再加回其在student行动分布下的期望梯度。最初在可精确枚举的工具行动集验证，再研究token词表上的实现成本。

令s_a=∇logπ(a|h)，G为task return，b为与当前抽样行动无关的baseline：

\[
g_{\rm CV}=s_a[G-b(h)-c(h,a)]+\sum_u\pi(u|h)c(h,u)\nabla\log\pi(u|h).
\]

【数学事实】固定c、on-policy抽样及正确回报下，两项c的条件期望抵消，因此保留原task policy gradient的期望。【待验证假设】teacher概率包含普通小critic较难从少量成功轨迹学到的结构，可以降低梯度方差，从而在相同总成本下加速RL，且不持续把最优策略拉向teacher。

**为什么可能成篇：** ATOD通过降低蒸馏来放松teacher约束；这里研究teacher能否在不改变最终task目标的条件下继续有用。若成立，teacher强项被用于估计效率，student仍能学习teacher不偏好的成功策略。

**新颖性风险很高：** [Q-Prop](https://arxiv.org/abs/1611.02247)已有action-dependent control variate；[vOPD §3](https://arxiv.org/html/2605.07865#S3)已有OPD的negative-KL state baseline。不能将恒等式、减baseline或“teacher作critic”本身作为新贡献。必须证明**teacher特有的信号以足够低成本改善task-RL估计**，且比同容量普通critic强。区别于vOPD的是优化目标与action-dependent补偿，不是control variate首次出现。[RA/CoRA](https://arxiv.org/html/2610.11519v1#S2)和[JOLT](https://arxiv.org/html/2610.10447v1#S2)也需作为近期objective对照。

**最便宜的验证：** 冻结一个共同checkpoint与采样分布，在有限工具行动环境精确计算小问题的参考梯度；比较普通state baseline、同容量无teacher critic、teacher校准c的偏差与方差，且将teacher forward计入成本。再比较热身后纯RL、ATOD、普通critic方法的成功率—总成本曲线。只有真实task梯度收益，不能以teacher KL下降代替。

**必须保持的边界：**

- stop-gradient只阻止反传，不能消除同批标签过拟合带来的统计依赖；使用先前批次或交叉拟合。
- PPO clipping、GRPO标准差归一化、多轮off-policy更新、忽略词表尾部，都不能自动继承上述无偏结论。实际使用这些操作需另推导或明确仅为启发式。
- token词表可一次forward得到全部logits，但完整期望的内存／反传成本仍需测。有限action pilot通过不代表开放工具参数已解决；也不能只对top-k求和后仍称精确。
- 无偏性不保证低方差。全零reward冷启动无法凭此创造有用期望梯度，所以共同热身不能省略。

**停止条件：** 同总成本下不优于普通critic；teacher分数与student回报不相关；收益来自残留模仿项；只能在昂贵的全枚举或有偏省略下成立。风险高；最有方法／理论想象力，但不是当前已验证的新算法。

【本轮实际执行】CPU三行动精确枚举检查了抵消恒等式，误差约2.8e−17；一个人为选择的相关c降低了toy方差。这只验证实现的代数方向，不是teacher有效性证据，不作为pilot通过。记录见[algebra-sanity.json](../.aris/traces/idea-creator/2026-10-19_run01/algebra-sanity.json)。

## 4. 储备：先验证teacher会不会被student的错误推理带偏

**具体做法：** 固定真实action/observation历史，替换student自产reasoning为正确、错误和等长无关版本；比较teacher给出的action目标。若未经证实的reasoning显著改变teacher目标，再训练teacher只看任务与真实交互证据、student保留完整历史的双视图监督。

这针对ATOD没有单独检查的监督污染。它无需训练即可先检验靶点，也无需重置环境；但若只剩prompt整理，难以形成强方法贡献。必须对比[SOPD的独立step生成](https://arxiv.org/html/2608.16333v1#S4)、ActionOPD的action目标，以及随机reasoning dropout／等长摘要，排除短上下文收益。删除reasoning也可能丢失有效推导；不能预设其全是污染。

停止条件：错误reasoning对teacher决策几乎无影响；或简单dropout完全复现。暂不与两条主方法组合，避免叠模块。

## 5. 15组候选的完整去向

“暂存”表示本轮不推荐投入，不表示已被证明无效；wiki以archived/pending记录本轮淘汰，保留重审空间。

| ID | 方法 | 本轮去向与主要原因 |
|---|---|---|
| A01 | 事实视图teacher | 靶点验证储备；SOPD/GC-OPD近邻强，可能只是prompt |
| A02 | teacher计划组合探索 | 暂存；需胜过同预算普通计划多样化 |
| A03 | teacher任务RL控制变量 | 主候选2；Q-Prop/vOPD近邻，成本优势未证 |
| A04/S04 | 部分有序依赖程序 | 机械合并；暂存；options与旧时序契约候选重叠，schema成本高 |
| A05 | 回看后验→在线belief | 主候选1；privileged POMDP与旧ledger近邻，需要新机制证据 |
| A06 | 教师知识→取证需求 | 暂存；与query／evidence蒸馏差异未拉开 |
| A07 | 固定均值的随机horizon | 暂存；随机截断与重要性校正已有，方差／同步成本风险 |
| A08 | schema可证明行动类 | 暂存；ASL/ActionOPD强近邻，可能仅格式规范化 |
| S01 | 观察差分响应 | 暂存；同配对数据普通训练可能等效，延续旧候选 |
| S02 | 过期belief撤销 | 暂存；memory schema改写风险，延续旧ledger |
| S03 | 真实转移的效果等价 | 暂存；ASL已定义转移等价，剩余真实数据纠错差异待证 |
| S05 | teacher后验势函数 | 暂存；potential shaping可与critic初始化／重参数化等价 |
| S06 | 摊销teacher纠正信号 | 暂存；proxy teacher已有，尚缺抗漂移的经济性机制 |
| S07 | 可逆错误免疫 | 暂存；需超越同环境步数随机扰动与恢复课程 |
| S08 | 黑盒teacher/student密度比 | 暂存；GAD已覆盖判别器奖励核心 |

不能主张“首次效果等价蒸馏”：审阅核对的[ASL §3](https://arxiv.org/html/2506.17697v3#S3)已经用转移定义等价action集合，并用world model近似，还有结合teacher与环境奖励的训练。也不能把[ActionOPD](https://arxiv.org/html/2610.19820v1#S2)的action语义监督改名为新方法。[GAD §2](https://arxiv.org/html/2511.10643v3#S2)覆盖teacher/student判别器与在线负样本。按实际student后续收益加权已有[OG-OPD](https://arxiv.org/html/2609.35319v1#S3)；未来KL信用已有[GammaOPD](https://arxiv.org/html/2609.16937v2#S3)。这些论文是否属于本项目正式收录范围，不影响其prior-art地位。

## 6. 验证顺序与成本口径

先做冻结模型／既有日志诊断：A01的污染靶点、A05的后验校准、A03的task梯度方差。只给出现有效信号的路线安排小规模训练；这些诊断服务方法决策，不将审计本身包装成用户要的方法论文。

首轮使用同一0.6B或1.7B student与外部4B teacher；两个不同交互域，至少一个存在真实部分可观测性。确认机制后再做3个训练seed、任务OOD与更强student。保留ATOD、纯RL、相应最近方法与同信息／同容量消融。统一环境步数、teacher总tokens／FLOPs、student训练与部署tokens，报告总时间—成功率曲线。

成本先用公式预算：rollout数=更新数×prompt batch×group size，生成tokens≈rollout数×平均turn数×每turn tokens。例：25×16×8×20×120≈768万生成tokens，仅为假设规模；teacher评分、标注、反传另计。没有本机吞吐测量，不声称能在两小时完成。按工作区规则，本轮不跑训练，后续在实验代码项目或远端安排。

## 7. 可追溯记录与状态

- [全量原候选](../.aris/traces/idea-creator/2026-10-19_run01/candidate-union.json)：16项生成、15机械组，无质量预筛。
- [查新证据](../.aris/traces/idea-creator/2026-10-19_run01/literature-brief.md)：方法节阅读与仅摘要阅读分别标注。
- [Astra生成输入](../.aris/traces/idea-creator/2026-10-19_run01/001-generation.request.json)、[Sol生成输入](../.aris/traces/idea-creator/2026-10-19_run01/002-generation.request.json)、[fresh审阅输入](../.aris/traces/idea-creator/2026-10-19_run01/003-jury.request.json)、[审阅完整输出](../.aris/traces/idea-creator/2026-10-19_run01/003-jury.response.md)。

父agent保留的审阅修正：不沿用“MemOPD式普通摘要”这一简化；A05新增了Meta-RL task inference与privileged POMDP近邻，最终新颖性仍暂定；A01的PROCEED仅解释为值得做靶点验证，未升级成主方法。未把模型审阅当作独立实验证据。

本次只做全文阅读、针对性查新、方法设计、模型审阅与CPU代数核查。所有成功率提升均来自原论文作者报告；本报告推荐方法没有实测提升、没有顶会录用保证。
