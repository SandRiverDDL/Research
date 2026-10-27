# G15 L2 定向证据（2026-10-15）

来源：只读证据agent `/root/g15_gen_l2_astra`；本文件压缩其事实、锚点、查询与缺口，不包含ranking/novelty verdict。

## C04：前缀概率保护

Claims：①B使A有效前缀到达率下降；②保护到达率区别于当前A loss保护；③机会保留解释后续A收益。

- [On-Policy Replay 2605.29495](https://arxiv.org/html/2605.29495) §3.2–3.4/Alg1/Eq2–6：在历史prompt上用当前阶段checkpoint生成回答，筛选后作CE replay；Eq5对应历史受限分布的forward KL期望梯度。该约束只在replay部分，新任务梯度不自动受约束。未见按B更新识别A机会损失/区域概率下界。
- [ReOPD 2607.04763](https://arxiv.org/html/2607.04763) §3 Eq4–6：分析student occupancy和teacher reliability偏移，提出occupancy几何桥接；§4固定teacher轨迹前缀，current student单步生成，深度衰减监督。不能宽泛声称首个优化教学前缀分布的方法。
- 分析：A4常用hinge前缀概率下界会变成仅对违约前缀启动的CE replay，因为负log前缀概率就是逐token CE之和。S4区域概率质量/实际位移约束不应与A4混同，需给出估计测度、互斥事件和选择偏差处理。长字符串不是语义区域；概率下降可能是更好路径替代。

## C05：学习收益驱动采样

Claims：①用后续A收益增加有用轨迹；②score-function修正采样路径；③存在B引起的特异机会退化且依赖重采样。

- [E-MAML 1803.01118](https://arxiv.org/html/1803.01118) §3.1–3.3 Eq3–4：meta-gradient已有参数更新路径项与初始采样分布score-function项；后者用更新后收益强化更新前采样。
- [Meta Pseudo Labels 2003.10580](https://arxiv.org/html/2003.10580) §2 Eq3、AppA Eq12/Alg1、C.3：一次student更新近似双层目标，以labeled梯度与pseudo-label梯度点积反馈teacher采样标签；有cosine替换及移动均值baseline。与S6的hᵀPg具体相邻，但MPL改变teacher标签分布，C05改变student轨迹分布。
- [Learning to Explore via Meta-Policy Gradient, ICML18](https://proceedings.mlr.press/v80/xu18d/xu18d.pdf) Alg1/Eq5：探索policy生成数据、更新actor，更新前后回报差乘探索轨迹log-prob梯度；直接邻近A5。
- [L2T](https://arxiv.org/html/1805.03643) §4.2–4.3按student达到验证阈值速度训练数据选择policy；[LeCTR AAAI19](https://ojs.aaai.org/index.php/AAAI/article/download/4570/4448) pp4–5/Table1包含loss/value gain教学回报。
- 分析：这些原文未研究B更新后A的OPD机会，但基础收益回报与点积估计都已知。若r依赖θ却停止r梯度，仅score-function项不是完整meta-objective无偏梯度；固定P也不自动代表有动量、裁剪、衰减的实际Adam位移。B后使用通用meta-exploration不足以建立跨teacher因果贡献。

## C06：丢失前缀fresh续写

Claims：①按B引起的流失触发补偿；②历史起点接当前student fresh suffix；③收益回到根节点部署分布。

- [STRIDE 2609.14636](https://arxiv.org/html/2609.14636) §4.1–4.3 Eq5–6/Alg1/§5.1：缓存旧student连续被teacher认可的前缀，从endorsement最低的weakest correct turn重新生成，随掌握向右移；有retail/telecom多teacher，各域trajectory由本域专家打分。所读算法不按B前后student likelihood下降补偿。
- [Backplay 1807.06919](https://arxiv.org/pdf/1807.06919) §3/PDF p3：从示范近终点状态启动，逐步移回初始状态。A6渐退课程有先例；S5无渐退，待证核心是流失驱动分配。
- ReOPD §4是teacher prefix后的current student单步，不是历史student prefix后完整suffix。[PG-OPD 2606.21994v2](https://arxiv.org/html/2606.21994v2) Eq5–11按当前prefix top-k overlap分配长续写，形成compatibility-conditioned分布。[ROSS 2609.35954](https://arxiv.org/html/2609.35954) §3 Eq1–4重用旧student轨迹并选择性teacher-forcing，不是fresh续写。
- 分析：A6/S5均为conditional roll-in，不能标成完整root on-policy。必须撤桥/根节点测试；流失可能是正常进展或路径替换。

## 实际查询，逐claim三式

时间窗Q=`after:2026-04-15 before:2026-10-16`。

| Claim | 实际queries（分号隔开） |
|---|---|
| C04-1 | `"on-policy distillation" "prefix" probability constraint forgetting multi teacher 2026`; `"productive" "prefix" distillation "cross-domain" teacher 2026`; `site:arxiv.org "prefix" "forgetting" "distillation" Q` |
| C04-2 | `"continual learning" "trajectory" "probability" constraint replay KL 2025 2026`; `"sequence likelihood" "constraint" "replay" distillation`; `"historical" "KL" "replay" "on-policy distillation"` |
| C04-3 | `"multi-teacher" "sampling distribution" interference on-policy`; `site:openreview.net "2025" "continual" "policy" "KL"`; `site:papers.nips.cc "2025" "policy" "forgetting"` |
| C05-1 | `"Meta Pseudo Labels" "REINFORCE" gradient dot product student`; `"Learning to Teach" "learning progress" "policy gradient"`; `"LeCTR" "learning progress" teacher` |
| C05-2 | `"meta exploration" "policy gradient" "learning progress"`; `"Meta-Gradient Reinforcement Learning" "sampling correction"`; `site:arxiv.org "on-policy distillation" "meta" "gradient" Q` |
| C05-3 | `site:openreview.net "ICLR 2026" "teaching" "gradient"`; `site:proceedings.mlr.press "2025" "teaching" "student"`; `site:papers.nips.cc "2025" "meta" "curriculum"` |
| C06-1 | `"STRIDE" "prefix buffer" "multi-teacher"`; `"prefix replay" "probability" "distillation"`; `"cross-domain" "lost" "prefix" distillation teacher` |
| C06-2 | `"Backplay" curriculum demonstrations backwards`; `site:arxiv.org "prefix" "curriculum" "distillation" Q`; `"language model" "reverse curriculum" "prefix" 2025 2026` |
| C06-3 | `site:openreview.net "ICLR 2025" "prefix" "curriculum"`; `site:proceedings.mlr.press "2026" "prefix" "distillation"`; `site:openreview.net "NeurIPS 2026" "prefix" "replay"` |

覆盖可检索arXiv近六个月、ICLR25/26、ICML25/26、NeurIPS25/26索引；不等于全proceedings穷举，NeurIPS26仅已公开材料。实际另做Scholar/Semantic Scholar/DBLP站点检索；S2 API 429、DBLP API无可解析JSON；OpenAlex确认MPL记录。Prefix OPD仅摘要/部分正文，CausalOPD及Student-Centered Distillation仅摘要筛选，不能作为明确覆盖裁决。无二手AI综述作事实来源。
