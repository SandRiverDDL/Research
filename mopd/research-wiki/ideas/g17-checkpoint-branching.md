---
type: idea
node_id: idea:g17-checkpoint-branching
title: "在一个交接点分裂稀有成功状态"
stage: archived
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:sun2026_distill_what_you", "paper:xu2026_who_teaches_which"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L2", "provisional"]
---

# 在一个交接点分裂稀有成功状态

**stage:** `archived`  ·  **outcome:** `pending`

L2-A2；降低本轮投入优先级；未运行pilot，provisional。

## Thesis
【候选方法；L2-A2；降低本轮投入优先级】

1. student 批量生成 A 阶段，在预先定义的 A→B 交接点用确定性验证器检查中间结果。
2. 把固定的后续采样预算分配给已到达有效状态的前缀，每个有效前缀最多生成4条独立student后续；不对所有位置分叉。
3. A 前缀只计一次训练权重，新增后续照常接受动态多 teacher OPD；部署仍从原题独立生成。

最小形式：L=E_z∼dπ L_prefix(z)+λE_z∼dπ(·|C(z)=1),u∼π(·|z) L_suffix(z,u)，每轮总生成token固定、每前缀副本数≤4；所有动作来自student，但后段占用分布经过条件化，不是原始无偏on-policy目标。

【待验证假设】【待验证】稀有有效前缀一旦出现，应当承担多次 B 学习机会；普通完整rollout可能把大部分后段预算消耗在无效状态。若有效前缀几乎从不出现，本法无法启动。

【原文覆盖与候选差异】
- [Branching On-Policy Distillation](https://arxiv.org/html/2610.13481v1)（§4.1–4.3；Eqs.6–11；Proposition 1；2026-10-09 v1）：已有覆盖：共享student前缀分叉、条件student后续、teacher逐token监督及prefix loss去重全部已实现。 剩余差异：候选在一个确定性验证的A→B交接点分叉；BranchOPD按entropy/disagreement选点。只有验证正确性选点在互补结构中的特殊价值尚未被该文直接回答。
- [Prefix-Guided On-Policy Distillation: Mining Golden Trajectories from Rollouts](https://arxiv.org/html/2606.21994v1)（Method: Prefix-Based Trajectory Scoring；Eqs.10–14；Algorithm 1）：已有覆盖：用短前缀质量分配固定长续写预算已存在。 剩余差异：候选从单个正确前缀生成多个后续，而PG-OPD主要继续高overlap候选；需控制正确性信息优势。
- [Know When to Stop, Where to Restart: Accelerating Multi-Turn Agentic On-Policy Distillation](https://arxiv.org/html/2609.14636v1)（§4.2；Eq.6；§5.3 multi-teacher setting）：已有覆盖：缓存高质量student前缀并重启后续OPD，且已有多teacher实验。 剩余差异：候选是单轮边界内的有限分裂与确定性检查；不是缓存后跨轮重启，也不是teacher endorsement proxy。

最小证伪：用现有student在64题各采4个prefix；只对可验证正确prefix各采4个≤512-token后续，同时给等额预算的随机/BranchOPD选点。审计单位总token中的unique有效状态、有效B监督及分支相关性，最多约0.52M后续tokens。不训练即可发现无可启动状态或无信息增量；未运行，GPU预算未指定，token未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分2/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。 archived仅表示本轮降低优先级，不代表被完整scoop或实验否定。

为什么不是BranchOPD的一个选点消融？仅把entropy选点换成已知正确边界不足以支撑独立方法论文。

- RISK_GATE_ONLY_DELTA：BranchOPD已经包含主要采样和loss操作，single boundary与最多4分支是预算选择；真正可承担贡献的是正确性选择与跨teacher监督机会的可验证关系。
- RISK_OCCUPANCY_REWEIGHTING：候选承认dπ(z|C=1)改变训练分布，这是正确的。prefix去重只消除重复计数，不会恢复原始occupancy；λ、token归一化和分支长度会改变前后段有效权重。
- RISK_LOW_EFFECTIVE_DIVERSITY：四个suffix共享同一稀有prefix，增加的是条件后续曝光而非四个独立状态；需要按unique prefix和题目聚类评估，不能把branch数当有效样本数。
- RISK_NO_START_AND_NO_REACHABILITY_GRADIENT：若正确prefix极少，本法没有可分裂对象；对suffix做local OPD不直接奖励A抵达该状态，且后段预算可能挤占A学习。
- RISK_VERIFIER_AND_COST：C(z)若依赖人工中间标签，其信息必须给各baseline。分支teacher评分会重复读取上下文；固定student输出token不等于固定训练FLOPs或teacher成本。

停止条件：正确性选点不提高有效B监督密度或unique状态覆盖，或者短训中等预算BranchOPD已经复现全部收益。不能仅因邻近工作存在就ABANDON，但当前独立方法优先级低。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

