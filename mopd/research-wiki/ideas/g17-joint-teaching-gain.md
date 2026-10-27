---
type: idea
node_id: idea:g17-joint-teaching-gain
title: "直接训练 teacher 的联合教学收益"
stage: archived
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:he2026_learn_from_whoever", "paper:wang2026_madopd_breaking_ceiling"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L1", "provisional"]
---

# 直接训练 teacher 的联合教学收益

**stage:** `archived`  ·  **outcome:** `pending`

L1-A4；原高风险储备，2026-10-17已撤回；未运行pilot，provisional。

【2026-10-17判断修订】创新性与训练吞吐／框架侵入性的理由不足，撤回推荐并归档；不是文献完整覆盖或实验否定，outcome保持pending。当前判断见[报告顶部修订](../../synthesis/g17-idea-report.md)。

## Thesis
【候选方法；L1-A4；原高风险储备，2026-10-17已撤回】

1. 从两个已有专长teacher出发；在同一student前缀，各输出≤128-token局部提示，不要求提供完整答案。
2. 冻结的当前student副本读取两份提示，在原student前缀上给出下一token目标；实际student不看提示，只学习该条件目标。
3. 抽取少量批次做一次临时student更新，再测未见组合题上的成功率变化；把这个真实教学增益作为两位teacher提示策略的共同奖励，更新teacher LoRA。
4. 交替优化提示策略与常规OPD；最终冻结teachers完成蒸馏，部署只保留无提示student。

最小形式：q=p_stopgrad(θ)(·|s,h₁,h₂)，θ′=θ−α∇θ KL(q||πθ)；teacher消息策略通过REINFORCE最大化R=Acc_V(θ′)−Acc_V(θ)，V与产生提示的训练题分离。

【待验证假设】【待验证】最会独立解题的teacher不一定最会提供联合可学信号；直接奖励共同教学增益，可使各teacher输出互补且能被student吸收的局部知识。必要知识来自初始专长训练，验证信号是实际student答案的任务检查结果，不是假设的局部oracle。

【原文覆盖与候选差异】
- [Learning to Teach with Student Feedback](https://arxiv.org/html/2109.04641)（Method / Course Step Eq.2–5；Exam Step Eq.6–8；Eq.11）：已有覆盖：IKD 的course/exam双层优化已用student真实一步更新后的独立数据表现优化teacher，这是候选中心目标的直接先例。 剩余差异：候选优化两个LLM的离散局部消息策略，用联合验证回报和REINFORCE，而非单teacher连续soft-target的meta-gradient。
- [Adaptive Multi-Teacher Knowledge Distillation with Meta-Learning](https://arxiv.org/html/2306.06634)（§III-A；§III-B Eq.6–9；§III-C）：已有覆盖：MMKD 已按更新后student表现优化多teacher监督的联合组织。 剩余差异：候选更新teacher消息生成策略本身；MMKD更新聚合权重网络。这是具体差异，但尚未证明该差异解决互补性问题。
- [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs](https://arxiv.org/html/2609.02548v1)（§4.3 Eq.4–5；§4.4 Eq.6–7）：已有覆盖：多teacher反馈→privileged self-teacher→无提示student的内循环已经存在。 剩余差异：候选允许不完整teacher并外层学习其消息，而MT-SDPO的teacher固定且先经整题资格验证。

最小证伪：未运行。仅检查元奖励是否可辨认：冻结同一student起点，在8个训练小批次各比较4组已有teacher提示的一步临时更新，用独立32题进行配对前后评估，并重复相同提示估计随机噪声。若提示间教学增益差小于重复噪声，当前meta奖励不足以支持优化。实际GPU预算未指定，token估算未测速，不承诺所需GPU小时。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分4.5/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

中心双层教学目标已由IKD建立，多teacher的student感知元优化又有MMKD；privileged反馈蒸馏已由MT-SDPO覆盖。剩余组合是否提供独立方法贡献，不能靠昂贵的LLM化实现回答。

- R4-KNOWN-META-TEACHING-CORE：不能把以student真实学习增益训练teacher写成首次贡献，IKD已直接包含该双层目标；与MMKD的多teacher元优化相比，新意主要落在局部生成消息及其互补性。
- R4-SPARSE-META-REWARD：一个临时更新对16个验证题各采一次的accuracy差可能低于噪声。独立Bernoulli前后估计在最坏方差下标准误约0.177，且一次样本差以1/16为粒度。teacher提示策略将获得高方差、稀疏共同奖励；不能把这些调用估算当作足够统计功效。
- R4-COMPLEMENTARITY-NOT-IDENTIFIED：两位teacher同收一个总奖励不保证互补，一位可能承担全部有用信息，另一位搭便车；也可能等价于一个teacher生成双倍长度消息。去掉任意teacher后掉分还须排除总token/信息量减少。
- R4-LOCAL-HINT-BOUNDARY：128-token上限不保证消息仅有局部知识，短消息也可泄露完整答案。需如实审计消息的信息来源，不能把conditioned student副本称为天然不具完整求解能力；其获得两个消息后可能就是联合solver，这不违规但须计入方法定义和成本。
- R4-OBJECTIVE-CADENCE：q在单个s上的next-token形式清楚，sampling prefix来自无提示student也清楚；但每条轨迹只提示一次还是所有位置重新提示未完全定义，必须在实施前固定，不能按一次消息预算却按全轨迹逐位置提示效果叙述。
- R4-META-OVERFITTING-COST：验证集必须与teacher生成消息的题及最终测试隔离。持续依据相同验证集更新teacher会适应元训练集，不能把其收益当未见泛化。teacher制备、临时student更新、前后验证、消息生成和副本评分需全部计费，原token估算未测速。

停止条件：如果真实post-update无提示增益不可区分于采样噪声，或固定单teacher同token提示已达到相同增益，原方法的核心可学互补性前提失败。未找到完整包含双生成teacher消息元训练的单篇论文，因此不ABANDON；当前优先级受成本和已有核心机制限制。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

