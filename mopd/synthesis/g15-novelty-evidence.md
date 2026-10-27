# G15 候选查新证据

日期：2026-10-15。范围：用户确认的 **L1 / L2 / L5**。这是针对具体候选的定向核查，没有重新进行全领域调研。论文方法是作者报告；“剩余差异”是本轮解释，方法效果均为待验证假设。最终推荐与fresh reviewer裁决见 [idea report](g15-idea-report.md)。

## 既有 MOPD 证据边界

输入来自 [G15完整分析](mopd-gap-analysis.md)、[文献综述](mopd-literature-review.md) 与下列直接论文页；本轮定点核对原文章节，未全文重读36篇。

| 既有方法 | 本轮必须尊重的覆盖/限制 |
|---|---|
| [Open](../research-wiki/papers/gao2026_openmopd_diagnosing_fixing.md) §3.2/Fig3/§4 | token份额、监督稀疏与rollout刷新已经研究；同一前缀上的token分歧少不排除参数干扰，也不证明后续采样机会受损 |
| [DN](../research-wiki/papers/li2026_beyond_teacher_assignment.md) Alg1/Tables C.10,D.3/AppE.2 | 尺度归一化直接覆盖相对支配；固定权重在部分规模已接近动态策略，不能默认复杂方法有独立价值 |
| [D³](../research-wiki/papers/sun2026_d³mopd_dynamic_domain.md) §3/AppI | KL水平/速度调度与饥饿修正已有覆盖；不能把动态分配预算当作空白 |
| [Gradients→Capabilities](../research-wiki/papers/zhu2026_from_gradients_capabilities.md) §3–5/Figs2,5 | 相同Adam状态能改变原始梯度差异；任何几何代理都须核对实际更新与行为 |
| [PMOPD](../research-wiki/papers/liu2026_pmopd_task_ordering.md) §4/Table4 | 已有任务顺序、循环及累计实际更新子空间保护 |
| [Road](../research-wiki/papers/tian2026_beyond_domainrouted_supervision.md) §3.3/Table3 | 辅助teacher在同一主域轨迹上提供监督并作部分投影；不能误作所有teacher原生分布loss保护 |
| [UP](../research-wiki/papers/zhu2026_upmopd_update_projection.md) §2.3/§3.1 | 已对实际AdamW候选位移做联合约束；其当前batch一阶保证不是长期能力保证，但这一差别本身也不是新方法 |

Open与DN在不同设置呈现不同失衡方向。现有结果没有证明在预算、固定权重、数据相关性、归一化及实际更新投影之后，必然剩下高价值瓶颈。

## 候选级近邻与可主张边界

| 候选 | 已核对的一手近邻与锚点 | 剩余可检验差异；不能主张什么 |
|---|---|---|
| C01 函数保持再参数化 | [COST NeurIPS25](https://papers.nips.cc/paper_files/paper/2025/file/fa30825df7ceaba452d5533538ea29c2-Paper-Conference.pdf) §4.1/4.3；[Parameter Symmetries](https://arxiv.org/html/2504.15399v1) §4.2 Alg2 | 对称变换后lookahead元优化已有；剩余是A/B最弱域有限步收益、等范数与精确状态变换下的跨teacher效应 |
| C02 互惠元蒸馏 | [MER](https://arxiv.org/html/1810.11910) §3/Alg1；[La-MAML](https://arxiv.org/html/2007.13904) §4；[Efficient MER](https://arxiv.org/html/2508.01908) §3.2 | 互惠未来学习已有；若投影消掉起点loss梯度，元增益梯度就是负的投影终点loss梯度，不能靠“收益”命名制造区别 |
| C03 学习方向输运 | [ONG](https://arxiv.org/html/2508.17169v3) §4/Alg1/§6；[OGD](https://proceedings.mlr.press/v108/farajtabar20a.html)；[OPGD ICLR26](https://proceedings.iclr.cc/paper_files/paper/2026/file/1f8638a87bddd34e090698f0bfaa9c02-Paper-Conference.pdf) §4/Alg1 p8 | 上述为保护输出、历史方向投影或当前模型重算方向；未见保存成功功能变化J_old v、求J_new u匹配，再促进未来B学习的完整实现。ONG把transport列为未来工作，不能当已完成 |
| C04 教学前缀概率保护 | [On-Policy Replay](https://arxiv.org/html/2605.29495) §3.2–3.4/Eq5；[ReOPD](https://arxiv.org/html/2607.04763) §3–4 | A4逐前缀hinge可化为违约触发式CE replay；S4有效区域概率质量约束是另一变体，估计测度未定义充分。剩余是B诱发A机会流失的因果链及针对性保护 |
| C05 采样分布梯度 | [E-MAML](https://arxiv.org/html/1803.01118) §3.1/Eq3–4；[MPL](https://arxiv.org/html/2003.10580) AppA/Eq12；[Meta-Policy Gradient](https://proceedings.mlr.press/v80/xu18d/xu18d.pdf) Alg1/Eq5 | 后续收益作score-function回报、梯度点积反馈均已有。剩余是冻结teachers、改变student采样以修复B对A的作用；只用score项且stop-gradient回报不等于完整meta-gradient |
| C06 流失前缀fresh续写 | [STRIDE](https://arxiv.org/html/2609.14636) §4/Eq6/Alg1/§5.1；[Backplay](https://arxiv.org/pdf/1807.06919) §3 p3；ReOPD §4 | STRIDE已在多teacher中做缓存student前缀和fresh续写；Backplay已有向根节点渐退。剩余是按B前后流失量分配补偿，且撤桥后root能力保留 |
| C07 修复后终点保护 | La-MAML §4；UP §2.3；PMOPD §4 | 可微有限步优化已知；具体delta是B方向通过A修复映射的导数选择，约束完整组合更新的终点。必须胜过同成本普通B→A修复与终点筛选 |
| C08 更新交换子转向 | [Commute Your Domains](https://arxiv.org/html/2501.15556v1) §3.2 Thm3.1/Cor3.2、§6.1 | AB/BA差、梯度Lie bracket及顺序收益理论已有；原文未给显式最优调度算法。候选执行该方向，而非只预测顺序效果，需胜过直接AB/BA选择 |
| C09 分裂与重合 | [Net2Net](https://arxiv.org/html/1511.05641) §2.3；[ExpandNets](https://arxiv.org/html/1811.10495) Fig1/附录收缩实现 | 函数保持增宽、训练增参部署收回已知；候选非线性通道强制重合无代数收缩保证，需证明最终原宽度收益 |
| C10 共享塑性度量 | [GAP](https://arxiv.org/html/2304.01552) §III-A/Eq7–9/Alg1；La-MAML §4 | 元学preconditioner已有；剩余为B-only与A→B配对目标带来的跨teacher增益，不能只展示一般加速 |
| C11 目标相关学习核 | [C-CHAIN](https://arxiv.org/html/2506.00592v1) §4；[PLATE](https://arxiv.org/html/2602.03846v1) §4.1；[Dynamical Isometry](https://arxiv.org/html/2606.09762v1) §4；[Learning Dynamics of CL](https://arxiv.org/html/2609.33620v1) §5/Eq7 | CHAIN保输出、PLATE固定塑性子空间，均不是在线残差核谱保持；但目标方向传输退化已有直接证据。需证明核保护对应真实B收益，不阻断A学习 |
| C12 监督目标编译 | [MetaDistil ACL22](https://aclanthology.org/2022.acl-long.485.pdf) §3.2/Eq2–3/Alg1 | 按student反馈调整teacher监督已有；剩余为A监督怎样改变后续B学习，须排除仅把quiz域换B、牺牲A或放大B起点误差 |
| C13 临时能力缓冲 | [Progress & Compress](https://proceedings.mlr.press/v80/schwarz18a.html) §2；[FOSTER](https://arxiv.org/html/2204.04662v2) §4.1/4.3 | 扩容/蒸馏压回已有；候选让旧A损伤暂存分支、主干学B。必须归零回收且胜过同参数同成本普通expand/compress |

补充覆盖：C05还对照[L2T](https://arxiv.org/html/1805.03643) §4.2–4.3和[LeCTR](https://ojs.aaai.org/index.php/AAAI/article/download/4570/4448) Table1的学习进展教学回报；C06还核对[PG-OPD](https://arxiv.org/html/2606.21994v2) Eq5–11与[ROSS](https://arxiv.org/html/2609.35954) §3，前者为compatibility-conditioned续写分配，后者重用历史轨迹，不可互相当作同一种fresh-suffix方法。

## 检索覆盖与缺口

- 每候选提取三项核心claim；每claim至少三种实际查询表达，允许相邻claims复用查询。完整映射分别见 [L1记录](../.aris/traces/idea-creator/2026-10-15_run02/g15-l1-evidence.md)、[L2记录](../.aris/traces/idea-creator/2026-10-15_run02/g15-l2-evidence.md)、[L5记录](../.aris/traces/idea-creator/2026-10-15_run02/g15-l5-evidence.md)。
- 主要检索arXiv、OpenReview、PMLR、NeurIPS及必要ACL/CVF一手来源；定向覆盖近六个月（2026-04-15至2026-10-15）和2025/26会议可公开搜索索引。不是全部proceedings或所有论文的穷举；NeurIPS26仅公开可检索材料。
- Scholar/Semantic Scholar/DBLP站点搜索已尝试，S2 API限流、DBLP API无可解析返回；OpenAlex只用于确认MPL条目。未用二手AI综述判定机制覆盖。
- OPGD原文访问缺口已由ICLR官方PDF补上，见[补核记录](../.aris/traces/idea-creator/2026-10-15_run02/008-g15-fresh-novelty-review.supplement.md)。function-space transport邻域仍非穷尽；MetaDistiller、Firefly等仅发现/摘要，不作为完整覆盖裁决。原文只核对所列章节，版本一致性未验证处不默认补齐。
- 没有找到完整覆盖某候选的论文，不等于证明全新。所有结论均为选题早期门槛；fresh审阅属于same-family provisional，不是实验或外部同行确认。
