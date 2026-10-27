# OPD 具体 Failure Modes：现象、机制与证据

更新：2026-10-06。用途：区分“多篇论文在修同一个问题”与“真正不同的瓶颈”，服务分类学习与实验诊断。

**覆盖说明**：本轮扫描现有顶层卡片标题／诊断字段，并定向复读相关卡片；不是逐篇重新精读全库，更不是 OPD 全领域系统综述。聊天中已回查的原文作为直接证据；其余明确以卡片中的 source anchors 为入口。下文不以录用、开源或作者名气替代机制验证，也不把作者的解释写成独立复现事实。

## 快速地图

| 编号 | 具体问题 | 代表论文 | 不要混淆成什么 |
|---|---|---|---|
| 1 | 极端负 log-ratio 主导更新 | TrOPD、REOPOLD、PowerOPD、TOP-D | 不是所有梯度方差的来源 |
| 2 | 单动作 Monte Carlo 梯度噪声 | vOPD、AsyncOPD | reward 方差不等于梯度方差 |
| 3 | 稀有优质替代动作几乎得不到直接强化 | AOPD、TGPO | RKL 不是只惩罚、不奖励 |
| 4 | 分布过早收缩，合理分支覆盖减少 | EOPD、REOPOLD | 熵越高不一定越好 |
| 5 | top-k 截断／归一化改变梯度或目标 | Many Faces、Revisiting OPD | 不等于 top-k baseline 有偏 |
| 6 | 长未来 return 引入耦合与高方差 | MiniLLM、Revisiting OPD | 不等于局部 token 估计噪声 |
| 7 | 低 KL 的退化一致，无纠正力 | KAT | 低 KL 不能单独判坏 |
| 8 | 高 loss／高梯度 token 功能贡献低 | Rock Tokens | 不等于高熵决策 token |
| 9 | 长后缀计算冗余／监督价值降低 | ADWIN、ESR、SFD | 冗余与错误监督不是一回事 |
| 10 | 缓存动作支持缺失与陈旧分布 | AsyncOPD、f-OPD | IS 不能恢复未缓存动作 |
| 11 | tokenizer 接口静默丢失监督 | SimCT、Revisiting OPD | 不等于教师能力弱 |
| 12 | 特权信息无法从可见输入恢复 | Many Faces | 不等于所有 OPSD 都无效 |
| 13 | OPD 与任务奖励的联合更新干扰 | Sequential、Long-Context Recipe | 不等于联合训练总是差 |
| 14 | 外推提升与结构格式崩溃错位 | Extrapolation Cliff | 只适用于相应外推设置 |

编号是本文的阅读组织，不修改项目 taxonomy。以下“可观测量”是建议的诊断指标，除非明确引用，不意味着论文已全部测过。

## 先分清目标、估计与信号

固定学生前缀 s，常见 sampled RKL 信号是 r(a,s)=log p_T(a|s)-log p_S(a|s)。在相应局部策略梯度实现中，它乘上 ∇log p_S(a|s)；这里不自动包括未来状态分布的完整梯度。

- **目标问题**：即使精确优化，目标也可能偏好不利于任务的分布，如过早失去分支覆盖。
- **估计问题**：目标可以合理，但有限采样、支持截断、错误反传或陈旧数据导致实际更新不稳定／不一致。
- **信号问题**：教师分布或可用信息本身不代表当前任务的有效纠正。

三个层面可以同时发生。高 KL、低熵、高 loss 都是观测，不能直接作为唯一根因。

## 1. 极端负 log-ratio 主导更新

**现象／作者诊断**：学生采到某 token，但 p_T 远小于 p_S，r 出现负长尾；少量位置可能占据很大更新份额，导致震荡或退化。

**方法对应**：TrOPD 用 min(p_T/p_S,1) 随机划分 token，正常区域做 sampled RKL，异常区域用教师 top-k FKL；REOPOLD 对负信号做 clipping，并组合 token 选择与阶段调度；PowerOPD 用有界幂变换；TOP-D 用混合 proximal teacher 限制负尾。

**边界**：这是相关但不相同的修法，不是四个独立新 failure modes。r 极端不保证梯度范数必然极端；还取决于 score gradient。限制幅度可能牺牲有用的大纠正。

**可观测量**：r 分位数、负尾位置占比、最大若干 token 的梯度贡献、同一配置多 seed 稳定性。

证据：[TrOPD 原文](https://arxiv.org/abs/2606.01249)及[卡片](../../notes/26_trust-region-opd.md)；[REOPOLD](https://arxiv.org/abs/2603.11137)及[卡片](../../notes/26_reopold.md)；[PowerOPD](https://arxiv.org/abs/2606.17199)；[TOP-D 卡片](../../notes/26-top-d.md)。TrOPD 与 TOP-D 是不同论文。

## 2. 单动作 Monte Carlo 梯度噪声

**现象／作者诊断**：相同前缀下只抽一个 token，不同候选产生不同 r∇log p_S，导致更新随随机采样变化；没有极端尾也可以有高方差。

**方法对应**：vOPD 减去 action-independent baseline b(s)=E_student[r]=-KL(p_S||p_T)；AsyncOPD 用多候选动作平均降低采样噪声。

**边界／数学解释**：baseline 在相应 score-function 假设下不改变期望梯度，但不是任何 baseline 都能降低方差，也不能把负 KL 自动称为最小梯度方差 baseline。已精确求全词表动作期望时，baseline 项消失，不能再减少该位置的动作采样噪声。

**可观测量**：同一前缀重复动作采样的梯度协方差、相对均值的噪声、MC 与全词表更新对齐。仅报告 reward 标准差不足。

证据：[vOPD §2–3](https://arxiv.org/abs/2605.07865)、[卡片中的 Eq.9–13](../../notes/26-vopd.md)；[AsyncOPD §6 卡片](../../notes/26-asyncopd.md)。

## 3. 稀有优质替代动作的直接强化不足

**现象／机制解释**：学生对教师偏好的替代 token 概率极低，它就很难被采中。否定当前 token 不等于直接指定概率应转移到哪个有用候选；softmax 参数耦合仍会影响未采样动作，所以不能说它们完全没有梯度影响。

**方法对应**：AOPD 在非正优势区域加教师 top-k FKL；TGPO 在学生前缀上加入教师 top-1 CE。两者提供替代方向，粒度与软／硬监督不同。

**边界**：不是“RKL 只惩罚过度自信”。r>0 会强化已采到的教师认可动作；瓶颈是有限采样下的覆盖。教师 top-1 也不一定正确，且损失其他有效分支。

**可观测量**：教师优选集合在学生下的概率质量与采样频率、惩罚后概率流向、软目标与硬目标的受控比较。

证据：[AOPD](https://arxiv.org/abs/2605.06387)；[TGPO 全文笔记](../../notes/l2/26-tgpo-deep-dive.md)。

## 4. 分布过早收缩与合理分支丢失

**作者发现**：EOPD 报告教师高熵位置的 RKL 训练降低生成多样性并产生不稳定信号；在这些位置补充 FKL 可保持 token 熵和改善 Pass@8。REOPOLD 也针对 premature entropy collapse。

**边界**：RKL 的 mode-seeking 不意味着必然熵崩溃；教师熵、学生熵和正确分支覆盖是三个不同量。高熵可能只是无用随机性，必须同时检查有效解的多样性和准确率。

**可观测量**：分桶 token 熵、正确轨迹的独立路径数、pass@1 与 pass@k，而非只看熵曲线。

证据：[EOPD 官方论文页](https://proceedings.mlr.press/v306/jin26e.html)、[REOPOLD 卡片](../../notes/26_reopold.md)。

## 5. top-k 截断／归一化改变梯度或目标

**作者诊断**：Many Faces 指出某些 top-k RKL 实现存在偏置梯度及不稳定；Revisiting OPD 讨论 sampled token 与局部支持集。需要分清选择集合、集合内重归一化、归一化量是否反传，不能把所有 top-k 写法视为同一个算法。

**边界／数学解释**：将 loss 截断到 top-k，与仅在 top-k 上近似一个 detached baseline 不同。OPD+ 还提醒：一般 f-divergence 的学生相关 reward 不能随意全部停梯度；但标准局部 RKL 中 -∇log p_S 的期望为零，不能把其 stop-gradient 一概判错。

**可观测量**：固定前缀上的 full-vocabulary 自动微分与实际 surrogate 梯度差异、遗漏质量、不同 k 与归一化实现的结果。

证据：[Many Faces 原文](https://arxiv.org/abs/2605.11182)、[卡片](../../notes/26_many-faces-opd.md)；[OPD+ 原文](https://arxiv.org/abs/2606.01039)、[卡片](../../notes/26_opd-plus.md)。本轮没有重新复核全部实现公式。

## 6. 长未来 return 耦合：目标保真与方差的取舍

**作者诊断／已有卡片**：将后续多个 log-ratio 累加来给当前动作 credit，使估计更贴近序列目标，却增加未来随机性和长程耦合。只用当前位置信号更稳定，但一般不等于完整序列目标的梯度。

**边界**：这与第 2 项的局部动作 MC 噪声不同。return 降噪、折扣或截断可能同时改变 credit 和目标；不能只用训练稳定证明估计更正确。

**可观测量**：同一目标下的 horizon 扫描、梯度方差与偏差、跨前缀影响，而非只比较不同 loss 的最终分数。

证据入口：[MiniLLM §2 卡片](../../notes/24_minillm.md)、[Revisiting §2／Appendix D 卡片](../../notes/26_revisiting-opd.md)。本项复用已有卡片锚点，未重新精读全文。

## 7. 低 KL 的退化一致，没有纠正力

**作者发现**：KAT 观察到不可恢复前缀下，教师可能局部同意退化续写；KL 低，但监督帮助小。检测持续低 KL 后终止 rollout，改善准确率并减少生成。

**边界**：低 KL 也可能是正常已学会的位置。终止规则不是语义错误判定器，必须排除“正常一致”和“退化一致”混淆。

**可观测量**：相同低 KL 区间的成功率、重复／重置行为、教师补全的恢复概率。

证据：[KAT 原文](https://arxiv.org/abs/2606.09471)、[卡片](../../notes/26_kl-agreement-trap.md)。

## 8. 高 loss／高梯度不等于功能重要性

**作者发现／已有卡片**：Rock Tokens 持续难拟合、占用梯度，却与真正支撑推理的 Pillar Tokens 不同；功能干预检验其重要性，而非只看相关性。

**边界**：高 loss 可能来自表达习惯或真正能力差距，不能全部丢弃。结论对任务、pair 和干预方式有依赖；不能自动等同于“高熵 token 无用”。

**可观测量**：损失持续性、梯度贡献与 token 干预后的任务变化，三者分别报告。

证据：[Rock Tokens 原文](https://arxiv.org/abs/2605.09253)、[卡片 §3–4 锚点](../../notes/26_rock-tokens.md)。本轮核对摘要与已有卡片，未独立复核 knockout 实验。

## 9. 长后缀：计算冗余与监督失真要分开

**两种诊断**：ADWIN 的短前缀与完整轨迹聚合梯度方向相近，说明后续计算可能不划算；SFD／ESR 则关注后缀教师信号退化，可能直接有害。前者不必包含后者。

**方法对应**：ADWIN 用完整 probes 校验窗口；SFD 用候选 continuation 的短 lookahead 教师置信度构造额外信号；ESR 限制生成长度。

**边界**：梯度 cosine 忽略幅度，batch 平均可能掩盖少数独特方向；lookahead 置信度是 proxy，不等于最终正确率或纠错能力。FLOPs 下降不等于 wall-clock 同比例提升。

**可观测量**：前缀／后缀梯度方向和范数、功能增益、teacher 恢复能力、生成与评分的实际时间。

证据：[ADWIN 原文](https://arxiv.org/abs/2605.28396)；[SFD 原文](https://arxiv.org/abs/2605.30833)、[卡片](../../notes/26_supervision-fidelity-decay.md)；[ESR 卡片](../../notes/26_early-stopping-rollout.md)。

## 10. 陈旧缓存：动作缺失、奖励陈旧、状态漂移

**作者诊断**：AsyncOPD 中旧学生 top-k 不覆盖当前候选；有限动作缓存之外的教师分数无法靠重加权补回。当前 log-ratio 还依赖当前学生，不能一直复用旧 advantage。f-OPD 在交互任务中另区分 rollout drift 与 teacher-conditioning context 漂移。

**边界**：动作 IS 可以纠正局部采样分布，不自动恢复整条轨迹状态分布。冻结教师、同一文本前缀和评分配置下，不应凭空宣称教师分布随时间漂移。

**可观测量**：当前分布落在缓存动作外的质量、旧／新 advantage 差异、lag 与实际 policy drift、交互上下文可对齐率。

证据：[AsyncOPD §4–6](https://arxiv.org/abs/2606.24143)、[卡片](../../notes/26-asyncopd.md)；[f-OPD §3–4](https://arxiv.org/abs/2605.17862)、[卡片](../../notes/26-f-opd.md)。

## 11. tokenizer 接口的监督丢失

**作者发现**：SimCT 指出 exact shared-token matching 在 tokenizer 分歧处丢掉监督；用双方都能实现的短 multi-token continuation 单元恢复。特殊 token／模板边界也可能污染概率比较。

**边界**：监督缺失属于接口问题，不证明教师语义正确或学生容量足够；不同 tokenizer 的同名 token id 不能直接比较。

**可观测量**：有效评分覆盖、被丢位置的任务类型、短 continuation 对齐后恢复的监督与收益。

证据：[SimCT 原文](https://arxiv.org/abs/2605.07711)、[卡片](../../notes/26_simct.md)；[Revisiting 卡片](../../notes/26_revisiting-opd.md)。

## 12. 实例特权信息无法从可见输入恢复

**作者发现**：Many Faces 的设置中，PI-free 学生聚合不同 PI-conditioned teachers；实例特有的信息在测试时缺失，不能像共享规则一样稳定内化。

**解释**：若相同可见输入可以对应不同隐藏答案，学生参数无法凭空恢复该实例的隐藏信息；但可泛化的求解规律仍可能学到。

**边界**：不能据此否定所有答案条件 OPSD。要检查 PI 是否包含可迁移规则、测试任务是否同分布，以及条件教师是否真正利用 PI。VPD／Harness 改 teacher 学习或信息构造，不自动消除此限制。

**可观测量**：共享规则与实例线索的控制实验、移除／打乱 PI、无 PI 的 held-out 迁移。

证据：[Many Faces 原文](https://arxiv.org/abs/2605.11182)、[卡片](../../notes/26_many-faces-opd.md)；相关入口：[VPD](../../notes/26-vpd.md)、[Harness](../../notes/26-ophsd.md)。

## 13. 模仿教师与任务奖励的联合更新干扰

**作者结果**：Sequential 在其任务中发现先 OPD 后 RL 优于联合训练，逻辑收益更明显；Long-Context Recipe 则在其长上下文配置中支持 GRPO＋教师 KL。

**解释／边界**：教师模仿梯度与奖励梯度可能冲突，也可能互补。学生是否已有正确分支、教师质量、数据和预算都不同，不能把两篇的结果直接拼成普适结论。OPD 也没有一个普遍数学意义的“绝不能超过 teacher”的硬上限。

**可观测量**：两个梯度的 cosine、pass@1／pass@k 与正确分支覆盖、预算匹配的联合／顺序对照。

证据：[Sequential 原文](https://arxiv.org/html/2609.04108)、[Long-Context Recipe §4.3](https://arxiv.org/html/2605.12227#S4.SS3)。本项来自本轮对话原文核查，尚无独立复现或跨论文统一配置。

## 14. 外推时格式有效率出现陡降

**作者诊断／已有卡片**：Extrapolation Cliff 在近确定的结构输出设置中，外推系数越界后 parse validity 崩溃；只在成功解析样本上看质量，会遗漏主要退化来源。

**边界**：只对应 reward extrapolation 及论文的结构假设，不是普通 OPD 的普遍 failure。不能把单位置理论阈值直接外推到任意语言任务。

**可观测量**：parse／contract 有效率、有效样本内质量、端到端任务分数分别报告。

证据入口：[卡片 §4–5 锚点](../../notes/26_extrapolation-cliff.md)、[原文](https://arxiv.org/abs/2605.08737)。本轮未重新精读原文，作为待核查扩展项。

## 方法重叠与学习顺序

**综合解释**：优先读 1–6，弄清信号幅度、采样方差、动作覆盖、熵、目标偏差、未来 credit 的区别；再读 7–10，区分“信号坏”与“花费不值”；11–14 按 tokenizer、OPSD、RL 或结构输出场景选择。

| 方法 | 主要落点 | 修复形式 | 没有因此证明什么 |
|---|---|---|---|
| TrOPD | 1，兼顾 3 | token trust routing＋异常区域 FKL | 概率比不能判教师语义正确 |
| REOPOLD | 1、4 | clipping＋token 选择＋阶段调度 | 三组件不等于三个独立根因 |
| TOP-D | 1、2 相关 | proximal teacher＋优化调度 | 不是 TrOPD，也不把大 batch 直接等同样本复用 |
| PowerOPD | 1 | 有界信号变换 | 降方差不自动恢复缺失动作 |
| vOPD | 2 | action-independent baseline | reward 方差减少不保证任意梯度方差减少 |
| AOPD／TGPO | 3 | 软替代目标／硬 top-1 目标 | 教师目标不一定就是任务最优动作 |
| EOPD | 4 | 教师高熵位置补 FKL | 高熵不等于有效探索 |

## 覆盖缺口与证据纪律

- 卡片字段只用于召回，不自动作为已验证根因；旧 EOPD 标签、Revisiting 的公式方向等未经本轮公式审计，不抄进新综合作为事实。
- 原表遗漏的 TrOPD／REOPOLD 已显式映射；新增 5、6、8、11、12、14 等细分问题，不声称已穷尽。
- teacher pattern／pair 兼容性、能力前沿数据选择、视觉 grounding、Agent turn 的监督预算、参数更新几何等保留在[专题](teacher-pattern-mismatch.md)及[阅读索引](../reading/opd-method-catalog.md)，尚未在这里升级成独立可复现诊断。
- EMNLP 的 38 篇候选多数仍只有摘要证据，见[会议快照](../reading/emnlp-2026-opd-overview.md)。本表没有完成全部候选全文审计。
- 当前存在的高价值任务是比较上述诊断的因果证据；“同一指标相关＋某修法提分”不足以判定唯一根因，更不能直接宣称研究空白。
