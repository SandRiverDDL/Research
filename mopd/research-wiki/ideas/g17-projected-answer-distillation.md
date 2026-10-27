---
type: idea
node_id: idea:g17-projected-answer-distillation
title: "投影答案蒸馏：让每位 teacher 只监督自己能解的部分"
stage: proposed
outcome: pending
added: 2026-10-15T13:48:25Z
based_on: ["paper:wang2026_smopd_multireward_reinforcement", "paper:nguyen2026_avsd_adaptiveview_selfdistillation"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L1", "provisional"]
---

# 投影答案蒸馏：让每位 teacher 只监督自己能解的部分

**stage:** `proposed`  ·  **outcome:** `pending`

L1-A3；储备；未运行pilot，provisional。

## Thesis
【候选方法；L1-A3；储备】

1. 限定有确定性输出投影的任务，例如同一结构化答案同时包含符号关系和单位或类型。投影器只解析共享实体与字段，不求解题目。
2. 每位 specialist 只学习并评分自己负责的投影答案；完整题仍可能超出任一teacher的稳定能力。
3. student 自采样4个完整答案；对每个答案提取所有投影，以各teacher对投影的概率乘积构成联合候选目标，再蒸馏回原student。
4. 部署student直接生成完整答案；不调用投影teachers。最终正确性验证只用于评测和公平RL对照。

最小形式：给定固定解析投影φ_i及student候选y_m，q_m∝exp(Σ_i λ_i log p_i(φ_i(y_m)|x))；固定投影长度口径后，最小化−Σ_m stopgrad(q_m)logπθ(y_m|x)。λ_i在独立局部校准集上固定，不依赖整题赢家。

【待验证假设】【待验证】teacher在可解投影上的概率比其完整答案概率更有信息；多个投影共同约束同一组实体时，可从student候选中识别联合有效解。主要风险是各投影分别合理却联合矛盾。

【原文覆盖与候选差异】
- [Knowledge Amalgamation for Multi-Label Classification via Label Dependency Transfer](https://ojs.aaai.org/index.php/AAAI/article/view/26190/25962)（pp.9982–9984 Problem Formulation；Proposed Method: ANT；Prediction Integrator Eq.4 onward）：已有覆盖：ANT 已从掌握不同标签子集的teachers向覆盖全部标签的student迁移局部知识及共享依赖；部分teacher整合本身不新。 剩余差异：候选针对生成式完整答案的固定投影，用各自可解的分布评分student自采样答案，不采用ANT的teacher间条件修订与标签整合器。
- [Symbolic Knowledge Distillation: from General Language Models to Commonsense Models](https://aclanthology.org/2022.naacl-main.341.pdf)（§2.1 Eq.1–3；§4 Critic Model；§5）：已有覆盖：用product-of-experts式质量因子构造目标并训练student已有方法。 剩余差异：候选的因子来自不同部分答案分布，且采样者为student；尚需证明投影信息而非一般reward weighting产生增量。

最小证伪：未运行。只对32道已有完整答案及全局验证器的题做projection碰撞和排序审计：为每题取现成student候选，检查同一组φ_i是否包含正确/错误完整答案，并比较联合分数相对单投影和完整答案聚合的真实正确性排序。所有正确答案仅用于审计。实际GPU预算未指定，token估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分5/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

目前更像partial-label amalgamation加通用product评分及reward-weighted self-training。需要实证证明投影对象本身解决了完整答案监督的具体失败，而不是把任务拆成若干独立字段后再拼接。

- R3-IMPLICIT-PROPOSAL：设 F(y)=∏_i p_i(φ_i(y)|x)^λ_i。对 y_m~π_old 后按 F(y_m) 加权，经验目标在大样本下趋于 Q(y)∝π_old(y)F(y)，而非 Q(y)∝F(y)。前者可解释为KL约束的指数倾斜更新，有限四候选目标也可定义；问题是当前claimed_delta尚未区分这个已知优化含义与纯teacher联合分布。
- R3-PROJECTION-IDENTIFIABILITY：若不同完整答案有相同全部投影，却只有一个合法，则所有teacher因子完全相同，方法没有信息区分它们。共享实体不自动排除这种纤维内歧义；例如字段分别正确但关系、程序行为或证明连贯性错误。
- R3-PRIOR-DOUBLE-COUNTING：各p_i(φ_i(y)|x)都是条件分布，直接乘积可能重复计算共享实体/先验，不能自动视为一致联合分布。固定λ校准尺度不等价于证明概率兼容；candidate-set score可以使用，但语义需保持为评分而非正确posterior。
- R3-CANDIDATE-SUPPORT：四个完整student候选中如果没有联合有效解，目标只能相对偏好现有候选；投影teacher本身不生成缺失的完整解。可以跨轮渐进改进，但原方法没有对此提供保证，不能把局部可解直接等同监督充分。
- R3-NO-HIDDEN-SOLVER：φ_i必须只是解析，不得通过求解题目、修正实体或判断正确答案提供免费额外知识。不同长度/表述的projection logprob、重复字段与语义等价变体都可能改变乘积。

停止条件：若高频存在全部投影相同而全局正确性相反的候选，或联合投影分数不能改善真实正确性排序，则该任务上的监督充分性被推翻；若必须引入完整求解器消歧才能生效，已超出原候选。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

