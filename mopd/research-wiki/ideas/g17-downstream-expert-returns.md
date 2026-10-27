---
type: idea
node_id: idea:g17-downstream-expert-returns
title: "用 B 能否接着完成，训练 student 抵达有用状态"
stage: proposed
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:yin2026_hopd_confidence_aware", "paper:sun2026_distill_what_you"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L2", "provisional"]
---

# 用 B 能否接着完成，训练 student 抵达有用状态

**stage:** `proposed`  ·  **outcome:** `pending`

L2-A4；储备；未运行pilot，provisional。

## Thesis
【候选方法；L2-A4；储备】

1. student 从原题生成 A 阶段并提交不可更改的中间结果 z。
2. 只在该交接点让 B 续写一次，以执行验证得到成功回报；任务契约禁止 B 忽略或修复已提交的 z。
3. 把该回报用于更新student的A前缀策略；student自身的完整轨迹继续做动态多teacher OPD，使B最终也进入同一个student。

最小形式：r_B(x,z)=V(x,z,u_B)，u_B∼π_B(·|x,z)；J_A=E_z∼πθ E_uB[r_B]，用(r_B−b(x))Σt∈A ∇logπθ(z_t|x,z<t)更新前缀，并保留L_dynamic_OPD。辅助回报来自πθ^Aπ_B^B的expert rollout，属于OPD+RL混合方法。

【待验证假设】【待验证】student尚不会B时，自己的终局失败会掩盖已接近成功的A状态；B的完成结果能提前训练这些状态的可达性。若A正确性标签已提供全部信号，额外B调用可能没有价值。

【原文覆盖与候选差异】
- [Learning to Generate Better Than Your LLM](https://arxiv.org/html/2306.11816v2)（§4；Algorithm 2 AggreVaTeD；Algorithm 3 D²LOLS）：已有覆盖：LLM learner roll-in、guide rollout、用guide完成回报构造advantage更新learner已由AggreVaTeD/RLGF实现。 剩余差异：候选固定在一个有不可修改契约的专长交接点，使用一次MC回报更新整个A前缀并并行MOPD，而不是一般状态采样与价值网络。
- [Policy Improvement via Imitation of Multiple Oracles](https://arxiv.org/html/2007.00795v2)（§3.2；Algorithm 1 lines 2–7；§4；Eqs.12–14）：已有覆盖：多弱oracle完成价值帮助learner改进及超越单oracle已有完整框架。 剩余差异：候选不估计所有oracle的值，也不逐状态选择，只把已知下游specialist的一次完成作为阶段级信号；需要证明这种简化在MOPD中的实际优势。
- [Active Policy Improvement from Multiple Black-box Oracles](https://arxiv.org/html/2306.10259v2)（§3.2 Eq.9；§4.1–4.2；Algorithm 1）：已有覆盖：多个black-box oracle的rollout价值、state exploration及其采样效率已有研究。 剩余差异：候选利用任务接口固定调用位置并最终把下游能力蒸馏到student；目前没有新的oracle选择算法或普遍改进保证。

最小证伪：首选一个不训练的信号检查：64题各采4个student A前缀，固定不可更改接口；每个prefix让B与student各续写2次，并记录A正确性。总≤0.524M续写tokens（其中B≤0.262M），另计前缀生成。检验B回报是否在A标签条件下仍区分可学的有用状态，是否比student回报更少全零，并审计B不能修复z。若这些都不成立，无需进入训练。未运行；实际GPU预算未指定，token未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分4/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

这是AggreVaTeD式expert-rollout reward再加普通MOPD吗？若r_B不能提供A标签之外的信息，连额外调用的必要性都不存在。

- RISK_KNOWN_GRADIENT：固定B时，(r_B−b(x))∇logπθ(z|x)是J_A的合法单样本REINFORCE估计，未重复乘proposal。该公式本身是既有expert cost-to-go思路，不是新policy-gradient结果。
- RISK_TEACHER_STUDENT_UTILITY_MISMATCH：J_A优化的是πθ^Aπ_B^B的成功，不是πθ完整成功。它可能偏好B擅长但student最终难以掌握的表示；普通OPD是否弥合此差距没有保证。
- RISK_REWARD_REDUNDANCY：若B对所有正确z几乎必成功、错误z必失败，r_B只是昂贵且有噪声的A正确性标签；若B过弱，一次rollout又可能全零。
- RISK_UNENFORCED_COMMITMENT：自然语言要求B不要修复z不够。执行接口必须实际约束后续依赖已提交z；否则B忽略z或偷偷重解会奖励错误A。
- RISK_MULTI_TEACHER_SPECIFICITY：新增辅助信号实际仅来自B，另一teacher只出现在既有OPD；必须证明互补池贡献超出单强guide或一般expert-rollout RL。
- RISK_COST_AND_UPDATE_LAG：2k次B调用≤1.024M输出tokens是单轮上界，需加输入prefill、verification、普通OPD的所有teacher/reference forwards与teacher制备。若复用旧prefix多轮更新，需明确old-policy处理，不能把当前公式自动当无偏。

停止条件：B回报在控制A正确性后无新增信息，或B通过绕过z取得成功，或B偏好的状态仅对B有效。即便信号成立，后续等预算AggreVaTeD＋MOPD或普通A奖励完全复现效果，也会使独立方法delta不成立。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

