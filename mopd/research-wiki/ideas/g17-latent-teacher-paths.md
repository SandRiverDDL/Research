---
type: idea
node_id: idea:g17-latent-teacher-paths
title: "潜在监督路径蒸馏"
stage: proposed
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:sun2026_distill_what_you", "paper:yin2026_hopd_confidence_aware"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L3", "provisional"]
---

# 潜在监督路径蒸馏

**stage:** `proposed`  ·  **outcome:** `pending`

L3-A3；储备；未运行pilot，provisional。

## Thesis
【候选方法；L3-A3；储备】

1. 把监督来源设为整条轨迹上的隐变量路径 z₁:T，使用小型 Markov 转移矩阵描述持续使用与跨专家接续；所有 experts 仍读取完整 student 历史。
2. 每收到一个 student token，依据其在各 expert 下的似然更新路径后验，再计算下一位置的 teacher mixture。
3. 把该精确可计算的条件目标蒸馏进一个 student；部署时移除路径变量。转移矩阵在小型校准集上固定，并与相同切换次数的普通平滑路由对照。

最小形式：r₁=ν；Q_t(a|h_t)=Σ_k r_tk q_k(a|h_t)。观测 y_t 后，r̄_tk=r_tk q_k(y_t|h_t)/Q_t(y_t|h_t)，r_{t+1,j}=Σ_k r̄_tk A_kj。L=E_{y~πθ}Σ_t KL(Q_t||πθ(·|h_t))，监督 detached。该 Q 是对完整 Markov teacher 路径求和所得的合法自回归策略；不是把 teacher 当作无记忆模型。

【待验证假设】【待验证】某些互补结构需要保留监督来源的跨步骤关联，单点 reliability 权重可能在有限样本下破坏这种关联；完整路径后验可作为较便宜的归纳偏置。来源一致性并不保证任务正确性。

【原文覆盖与候选差异】
- [Switching between Hidden Markov Models using Fixed Share](https://arxiv.org/pdf/1008.4532)（§3 Expert Hidden Markov Models, pp.4–5；Figure 3；Example 3.2 Bayesian mixture；§1.1 tracking the best expert）：已有覆盖：EHMM的latent transition、posterior mixture及下一步预测直接包含该过滤器结构；这一数学机制本身已知。 剩余差异：已核查论文不含把该完整teacher压缩到LLM student的MOPD训练及联合能力结果。应用增量尚未被一篇论文完整包含，故不能仅因HMM已知而ABANDON。
- [Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation (γOPD)](https://arxiv.org/html/2609.16937v1)（§3.1 Proposition 3.2, Eq.8；§3.2 Eq.9–10, γ=1 endpoint；§4.1–4.2, Table 2；Appendix D Algorithm）：已有覆盖：已有MOPD设置下的时间信用方法，说明超越token-local训练不是空白。 剩余差异：γOPD干预梯度时间范围；本候选干预监督生成模型的latent来源关联，二者不同。

最小证伪：只做可枚举的双expert两阶段问题：固定局部准确率与状态覆盖，直接计算Q的联合成功，对比独立mixture和同切换率平滑；再改变文风相似性但保持能力不变。Q本身无优势即可在任何LLM训练前证伪。未运行；实际GPU预算未指定，tokens估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分4/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

这是标准EHMM/Fixed Share预测器接现成KD；来源一致性与任务依赖没有必然联系。必须先证明Q自身优于同切换率平滑，才能谈student优化贡献。

- 【数学核查】ν、A为概率分布/转移矩阵，各q_k为合法条件分布且Q_t(y_t)>0时，给定递推正确；full-history experts不违反EHMM定义，无需假设teacher自身无记忆。
- 在student轨迹上做detached forward-KL是student-state加权的局部蒸馏，不等于sequence KL(Q‖π)；候选未声称后者，但报告不可混写。
- 【命名风险：把生成来源当可靠性】后验解释的是哪个teacher更可能生成student已经写出的token；它不是哪个teacher更适合未来，也可能奖励复现student的错误、文风和通用高频token。
- 固定齐次A只提供通用持续/切换先验，未显式知道任务中的承诺或A→B边界。若联合解需要在低B-likelihood前缀后立即交给B，过滤器可能恰好延迟这种转换。
- A的校准目标、额外标签和hyperparameter选择预算未定义；若靠联合答案选A，需与平滑路由共享信息。完整mixture需要一致支持集，top-k截断及underflow会改变实际Q。

停止条件：若Q在控制切换率后不能改善正确联合解概率，或只改变文风就翻转优势，则来源路径不是候选所需的依赖信号；无需把它升级成更复杂router来维持候选。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

