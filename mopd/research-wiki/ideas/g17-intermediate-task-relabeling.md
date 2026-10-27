---
type: idea
node_id: idea:g17-intermediate-task-relabeling
title: "把错误中间结果改配为正确的新题，提前训练 B"
stage: proposed
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:yin2026_hopd_confidence_aware", "paper:lu2026_beyond_best_teacher"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L2", "provisional"]
---

# 把错误中间结果改配为正确的新题，提前训练 B

**stage:** `proposed`  ·  **outcome:** `pending`

L2-A3；储备；未运行pilot，provisional。

## Thesis
【候选方法；L2-A3；储备】

1. 选用能精确反向生成题目的任务族，例如把自然语言解析成DSL，再执行DSL。student 对原题生成中间程序 z。
2. 若 z 语法有效但不符合原题，用确定性渲染器生成新题 x′，使 z 对 x′ 恰好正确；不修改 z。
3. 以 x′、z 为上下文，让 student 自采样后续并接受 B 及动态多 teacher 监督；原题仍继续普通OPD，最终只评测原始分布的完整生成。

最小形式：构造R使g(R(z))=z；z∼πθ(·|x)，u∼πθ(·|R(z),z)，仅对u加入L_OPD(R(z),z,u)。z并非从πθ(·|R(z))采样，故这是显式relabelled off-policy前缀加on-policy后续。

【待验证假设】【待验证】部分失败A输出已经包含可供B学习的有效状态；通过改变题目一致性而非等待A完全正确，可以减少B监督饥饿。主要风险是逆向渲染分布过窄，收益不能回到原题。

【原文覆盖与候选差异】
- [The Wisdom of Hindsight Makes Language Models Better Instruction Followers](https://proceedings.mlr.press/v202/zhang23ab/zhang23ab.pdf)（ICML 2023 PDF pp.4–5；§4.2–4.3；Algorithm 1；Sub-output Relabeling）：已有覆盖：失败输出重标指令、中间sub-output重标及后缀监督均已存在。 剩余差异：候选要求确定性DSL逆映射，并在重标记后新采B后续，而不是对旧输出做监督。
- [CodeIt: Self-Improving Language Models with Prioritized Hindsight Replay](https://arxiv.org/html/2402.04858v2)（§2.2 Sampling and hindsight relabeling / Learning；Eq.1）：已有覆盖：以错误程序的真实行为构造有效新任务，再学习这些程序已实现。 剩余差异：候选把程序当中间状态而非最终预测目标，后接另一个teacher擅长的续写任务。
- [Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations](https://arxiv.org/html/2607.04235v1)（§3.2–3.4；Goal identification；Action relevance labeling）：已有覆盖：利用轨迹中非原目标的中间成功、重标目标并持续训练已有。 剩余差异：候选不依赖LLM猜目标，也不复用旧后续，而是精确构题后新采student续写；这些具体差异尚未被已核论文完整包含。

最小证伪：最便宜先做64个真实失败z的依赖审计：检验R与g的精确往返，并在相同z上比较B的目标分布/完成结果是否因提供R(z)而获得原题所需的新信息；与只给z的B子任务输入逐一配对，最多128个≤512-token续写约0.066M tokens。若B目标完全由z决定，则重标记特有机制没有成立，仍可把数据复用视为一般B训练。未运行；实际GPU预算未指定，估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分5/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

既然只训练B且z已足以执行，为什么要改题？相对“同一批z直接训练B”的因果增量是什么？

- RISK_RELABEL_REDUNDANCY：在典型DSL→执行任务中，若z已是B的充分输入，则正确后续仅取决于z。此时R(z)没有新增下游信息，候选可能退化为直接B子任务训练；这是当前设定的关键内部反例。
- RISK_INVERSE_SCOPE：g(R(z))=z只有在明确的形式语法/语义映射内才可保证；自然问题中别名、隐藏约束及歧义使等式不成立。不能把强LLM重写器当确定性inverse。
- RISK_DISTRIBUTION_SHIFT：原z来自π(z|x)，不是π(z|R(z))；候选已正确标注显式off-policy前缀。这里有意改变任务分布，无需假装importance correction能自动变回原题目标。
- RISK_NO_A_UPDATE：只对u计算额外loss，不直接训练student从新题生成z。B曝光增加不保证A→B联合可达性提高，且student易学到渲染模板shortcut。
- RISK_SYNTHETIC_COVERAGE：需对原题、R(z)题和随机合成题的难度/操作关系配平；错z可能集中于简单或无效程序。teacher额外生成为零仍不等于没有prefill、B评分和数据验证成本。

停止条件：在所选任务族中，R(z)相对同z的B子任务监督没有信息或迁移增量；或inverse需泄露最终答案/调用完整solver。若后续原题收益被普通合成数据完全解释，当前方法主张也失败。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

