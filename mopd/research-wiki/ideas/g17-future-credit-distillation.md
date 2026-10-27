---
type: idea
node_id: idea:g17-future-credit-distillation
title: "后缀分歧回传蒸馏"
stage: archived
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:di2026_understanding_off_onpolicy", "paper:sun2026_distill_what_you"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L3", "provisional"]
---

# 后缀分歧回传蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

L3-A1；降低本轮投入优先级；未运行pilot，provisional。

## Thesis
【候选方法；L3-A1；降低本轮投入优先级】

1. Student 按常规自采样；所有 experts 对同一轨迹评分，保留可信权重及未归一化的 geometric teacher factors。
2. 把实际采到的后续 teacher log-score 与 student entropy 合成 return-to-go，使后续专长难以接续的代价影响较早决定。
3. 用同题多条完整轨迹的独立基线降低方差；不为每个状态生成额外 continuation，也不增加部署组件。

最小形式：固定本轮可信权重 w_k(h)，f(h,a)=exp(Σ_k w_k(h)log q_k(a|h))，Q_seq(y|x)∝∏_t f(h_t,y_t)。最小化 KL(P_θ||Q_seq)。对 y~π_old，R_t=Σ_{u≥t}[log f(h_u,y_u)−logπ_old(y_u|h_u)]；一次 on-policy 更新最大化 Σ_t stopgrad(R_t−b_t)logπ_θ(y_t|h_t)。b_t 不依赖当前动作；多次复用须处理 importance correction。全部未来分数来自实际轨迹，不假设 oracle continuation。

【待验证假设】【待验证】有限容量和有限更新预算下，只优化当前位置的条件分布，可能没有把后续跨专家不相容充分归因到上游选择；完整轨迹梯度能改善联合成功。不是断言 token 策略不能表达依赖。

【原文覆盖与候选差异】
- [Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation (γOPD)](https://arxiv.org/html/2609.16937v1)（§3.1 Proposition 3.2, Eq.8；§3.2 Eq.9–10, γ=1 endpoint；§4.1–4.2, Table 2；Appendix D Algorithm）：已有覆盖：Eq.8和Eq.10的γ=1端点已给出相同形式的return-to-go梯度；已有多teacher math/code实验及无逐状态分叉的实现。 剩余差异：候选使用状态依赖权重和未局部归一化的多teacher factors，不能直接当作该文归一化teacher实例；同题联合依赖收益也未由其跨域均分证明。
- [Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives](https://arxiv.org/html/2609.38666v1)（§5 Eq.5.1–5.2；Remark 5.2；§6.3 Long Horizons）：已有覆盖：sequence geometric目标及continuation correction已有明确理论。 剩余差异：候选权重随prefix变化，并提出用MC PG训练；这些选择能否带来可规模化的新增结果尚无证据。
- [β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation](https://arxiv.org/html/2607.28582v1)（§2.3 Eq.12–15；§2.4 Eq.16–19；局部归一化近似说明）：已有覆盖：实际轨迹未来log-ratio求和、stop-gradient及token log-prob更新已作为实用recipe出现。 剩余差异：其采用局部归一化reference/privileged-teacher混合，不是本候选的全局factor目标。

最小证伪：不训练LLM：在可枚举二阶段、full-history双expert系统中，固定teacher知识、覆盖和student容量，精确计算候选Q、局部目标与γOPD目标的联合成功偏好及单步梯度；专门比较保留/除去log Z项。只要目标层面无新可用偏好，就无须上GPU。当前未运行；实际GPU预算未指定，原tokens估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分3/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。 archived仅表示本轮降低优先级，不代表被完整scoop或实验否定。

核心更新已经是γOPD/β-OPSD公开的return-to-go；当前剩余的是动态factor目标的具体实例，尚未给出它为何优于普通同目标sequence PG的独立机制。不能用已知梯度换一个多teacher名字。

- 【数学核查】固定本轮目标、完整支持集且有限EOS horizon时，给定return-to-go在θ=θ_old处是该sequence KL的无偏梯度方向；未知全局normalizer对θ为常数，不需估计。多轮旧轨迹更新则不再自动无偏。
- 【命名风险：目标归一化】令q_dyn=f/Z(h)，候选log f=log q_dyn+log Z(h)。它相对归一化teacher的sequence PG多出未来log Z(h)项；不能在实现中把f重新softmax后仍声称优化原目标，也不能把此差别抹掉后直接宣布γOPD已完整包含。
- 【命名风险：一致但错误】Z(h)的奖励可能偏好teacher一致的容易/错误路径；较强sequence credit不会自动纠正teacher pool缺知识。须先验证候选Q对正确联合解确有偏好。
- 同题baseline必须来自其他独立rollout或只依赖当前history；把当前轨迹放进均值会改变估计。原提案4 rollouts相对1 rollout的总采样四倍必须配平。
- 近one-hot权重使Z接近1，真正剩余增量可能消失；top-k或sampled-token近似与全分布目标差异应明确。

停止条件：若未归一化项没有改善正确联合解的目标排序，且候选梯度与普通同目标sequence PG逐项相同，则放弃其独立新方法定位，保留为基线；不将此写成已完成实验。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

