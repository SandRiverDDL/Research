# G15 L5 定向查新证据（2026-10-15）

这是证据记录，不是候选排序或质量裁决。仅查C07/C08/C09/C13。事实为原文作者方法，候选差异是待review解释；未运行实验。

## 已读的一手近邻

| 来源 | 已读锚点与覆盖 | 尚未确认覆盖的具体差异 |
|---|---|---|
| [La-MAML, NeurIPS 2020](https://arxiv.org/html/2007.13904) | §4.1 C-MAML/§4.2 La-MAML：当前任务多步inner-loop，所有已见任务outer-loss，反传学习初始化/逐参数学习率；§5比较沿途loss与终点loss | C07把B候选更新的评价放在明确A修复算子之后，按修复后的A约束选择B更新；有限步meta-optimization本身已知 |
| [Commute Your Domains, 2025](https://arxiv.org/html/2501.15556v1)；[OpenReview原文](https://openreview.net/pdf?id=h2TdQ99eR4) | §3.2 Thm3.1 Eq5–6定义梯度Lie bracket及AB/BA交换差；Cor3.2 Eq7–8预测固定域数据量下改变顺序的效果；§4双语LLM训练；§6.1不提出显式最优调度算法 | C08把交换子作为实际候选位移，加终点约束；原文主要分析/调整数据次序。显式方向是否胜过等成本AB/BA选择未证实，Adam状态不可忽略 |
| [Net2Net, ICLR 2016](https://arxiv.org/html/1511.05641) | §2.3 Net2WiderNet复制神经元、均分输出权重以保持函数，小扰动打破对称性 | C09必须学习到可重合状态并收回原宽度；函数保持的起始增宽本身不是新意 |
| [ExpandNets, NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/0e1ebad68af7f0ae4830b7ac92bc3c6f-Abstract.html)；[原文](https://arxiv.org/html/1811.10495) | §1/Fig1、附录收缩实现：线性层展开为多个连续线性层，训练后代数收缩；报告相同部署网络的收益 | C09跨非线性通道分裂后强制重合，不能沿用线性层代数折叠保证。临时增加参数而最终不增部署量已经存在 |
| [Progress & Compress, ICML 2018](https://proceedings.mlr.press/v80/schwarz18a.html)；[原文](https://arxiv.org/html/1805.06370) | §2.1冻knowledge base训练active column；§2.2用KL与online EWC压回knowledge base；固定双列，不是无限增大 | C13让临时分支承接旧A损伤、主干学B，再gate-to-zero；保护位置分工不同，但扩容后蒸馏巩固已知 |
| [FOSTER, ECCV 2022](https://arxiv.org/html/2204.04662v2) | §4.1冻结旧表示，新增模块拟合剩余误差；§4.3 expanded双分支蒸馏为单主干 | C13旧A能力缓冲与普通新任务扩容的角色不同；若普通扩容压缩等效，新增价值不成立 |

MOPD直接对照来自现有输入：PMOPD已有任务次序/循环与累计实际更新子空间；UP已保护实际AdamW位移；CaMOPD已有通用/领域交替，IM已有定时任务向量干预。见g15-generation-context.md及对应本地论文页，不能把“允许临时退步”“分阶段训练”独立当空白。

## Claims 与实际查询映射

每个候选三项claim；相近claims复用检索，不把复用写成独立搜索。检索限定arXiv、OpenReview、PMLR、NeurIPS等一手源；加入2025/2026关键词覆盖近期论文，未声称穷尽或完成Google Scholar/Semantic Scholar独立接口检索。

**C07**：①反传通过修复算子（Q1–3）；②终点约束允许中间下降（Q4–6）；③在MOPD超过普通交替修复（Q7–9）。
- Q1 `"continual learning" "repair" "bilevel" optimization`
- Q2 `"repair operator" "meta learning" continual`
- Q3 `"repair" "hypergradient" learning distillation`
- Q4 `"meta learning" "recovery" "terminal constraint" forgetting`
- Q5 `"terminal" "nonmonotonic" "multi-objective" neural optimization`
- Q6 `"nonmonotone" "Pareto" "learning" 2025 2026`
- Q7 `"multi teacher" "distillation" "lookahead" recovery 2026`
- Q8 `"on-policy distillation" "terminal" "constraint" 2026`
- Q9 `"learning without forgetting" "lookahead" 2025 2026`

**C08**：①AB/BA交换子（Q10–12）；②显式二阶方向/终点约束（Q11,13,14）；③在多teacher中超过顺序选择（Q12,14,15）。
- Q10 `"commutator" "multi-task" optimization gradient`
- Q11 `"Lie bracket" "gradient" "multi-domain" optimization`
- Q12 `"Commute Your Domains"`
- Q13 `"commutator" "optimization" "Pareto" learning`
- Q14 `"Lie bracket" "neural network" optimization 2025 2026`
- Q15 `"teacher" "distillation" "commutator"`

**C09**：①函数保持分裂（Q16–18）；②最终重合回原容量（Q17,19,20）；③路径收益超过等成本固定宽训练（Q18,20,21）。
- Q16 `"neuron splitting" merging "continual learning"`
- Q17 `"neural network" "split" "rejoin" training`
- Q18 `"Net2Net" "compression" "continual learning"`
- Q19 `"neuron splitting" "merging" optimization`
- Q20 `"capacity" "split" "merge" continual learning 2025 2026`
- Q21 `ExpandNets linear over parameterization train compact neural networks`

**C13**：①临时能力缓冲（Q22–24）；②归零回收（Q25–27）；③最终相同架构优于普通扩容蒸馏（Q23,28,29）。
- Q22 `"continual learning" "temporary" "adapter" compression 2025 2026`
- Q23 `"Progress Compress" "continual learning" Schwarz`
- Q24 `"temporary expansion" "knowledge distillation" continual`
- Q25 `"adapter" "annealing" "zero" "continual learning"`
- Q26 `"adapter" "consolidation" "on-policy distillation" 2026`
- Q27 `"grow" "shrink" "knowledge distillation" neural network`
- Q28 `"expand and compress" "LLM" 2025 2026`
- Q29 `FOSTER Feature Boosting Compression Class Incremental Learning`

代表性排除：backdoor repair不研究teacher整合；quantum Trotter commutators不提供该训练算法；neuron segmentation的split/merge是图像任务名；几何neural ODE的Lie bracket不是该多域训练结果。Firefly Neural Architecture Descent仅发现摘要/官方PDF入口，未核对方法，不作为确定覆盖证据。

## 搜索边界

以上未检出与每个完整候选同构的已发表结果，不等于不存在。C07/09/13大量基础机制已知；C08理论核心与Commute Your Domains直接相邻，必须由fresh reviewer判断完整delta。没有以搜索结果为空证明新颖性。
