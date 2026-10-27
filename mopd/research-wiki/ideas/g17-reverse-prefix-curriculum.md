---
type: idea
node_id: idea:g17-reverse-prefix-curriculum
title: "逐步撤去 teacher 前缀，让联合能力从后向前接通"
stage: archived
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:sun2026_distill_what_you", "paper:yin2026_hopd_confidence_aware"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L2", "provisional"]
---

# 逐步撤去 teacher 前缀，让联合能力从后向前接通

**stage:** `archived`  ·  **outcome:** `pending`

L2-A1；降低本轮投入优先级；未运行pilot，provisional。

## Thesis
【候选方法；L2-A1；降低本轮投入优先级】

1. A 为每道组合题生成经过验证的中间前缀，B 续写一次，保留确有联合解的训练题。
2. 先提供完整 A 前缀，让 student 自采样后续并接受强动态多 teacher 监督；随后逐轮缩短提供的前缀，让 student 自己补齐越来越多的 A 阶段。
3. 每次缩短都依据当前交接点的联合成功率；最终必须退到零前缀，在原始问题上训练和评测。

最小形式：d_k(y|x)=δ(y≤k=z≤k^A)πθ(y>k|x,z≤k^A)；最小化 E_dk Σt>k KL(πθ,t‖q_dynamic,t)，仅当验证联合成功率≥τ时令k减小；k>0属于teacher roll-in混合分布，k=0才恢复完整student on-policy。

【待验证假设】【待验证】先让 B 所需状态稳定出现，再学习抵达它的前缀，可以跨过 A、B 必须同时成熟的学习障碍。风险是 student 依赖提供的前缀，撤去后收益消失。

【原文覆盖与候选差异】
- [TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/html/2604.24005v2)（§4.2 TCOD-B2F；Eq.5；Algorithm 2；train-test mismatch段）：已有覆盖：teacher执行成功前缀→student续写OPD→前缀逐步缩到零，已由TCOD-B2F明确实现。 剩余差异：候选用A前缀+B验证形成联合起点，并以联合成功率而非固定pacing撤除；需要证明该具体变化而非reverse OPD本身带来增益。
- [Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems](https://arxiv.org/html/2607.07674v1)（§4.2 Closed-loop adaptation / Annealing；Eq.2；§3 prefix masking）：已有覆盖：成功率反馈控制前缀长度并最终撤除，已在AdaPrefix-GRPO实现。 剩余差异：候选用动态MOPD目标及互补teacher，而非GRPO；更换目标并不自动构成足够方法增量。
- [Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning](https://arxiv.org/html/2402.05808v2)（§3.1–3.3；Eq.3）：已有覆盖：后向起点课程及起点混合的基本机制已有。 剩余差异：缺少整题可靠单teacher而由互补池提供可学前缀，是可核验但尚未成立的适用条件差异。

最小证伪：不训练的最便宜检查：64道可验证组合题，在零/半/完整A前缀上各采4次student后续，固定teachers及q_dynamic，检查正确前缀是否确实打开普通student极少到达、而B能提供有效监督的状态。约0.39M student后续tokens（每次≤512），另计A/B制备与验证。如果此条件不成立，停止本机制；条件成立也只说明值得后续与TCOD-B2F短训比较。未运行，实际GPU预算未指定、token估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分3/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。 archived仅表示本轮降低优先级，不代表被完整scoop或实验否定。

这是否只是给TCOD-B2F接上Trust式动态teacher及已有成功率调度？必须找出组合设定中可重复、无法由原版课程解释的增益。

- RISK_DIRECT_RECIPE_OVERLAP：TCOD-B2F直接覆盖主要OPD操作；剩余delta集中在联合teacher前缀和成功率课程，不能以三篇工作的组合被想象成某单篇已完整包含而ABANDON，但也不能继续宣称基础路径新颖。
- RISK_CURRICULUM_STALL：k>0的混合分布标注正确；只在后缀算loss并不直接训练被提供的A tokens。当前k达到阈值不保证更短k可学，撤除阶段可能停滞或遗忘。
- RISK_UNSPECIFIED_SURROGATE：q_dynamic未被固定，实践应与对照使用同一已有聚合；对采样state stop-gradient是常用local OPD surrogate，不能额外声称完整求导E_dθ的优化保证。
- RISK_VERIFIED_DEMO_ADVANTAGE：A前缀+B一次成功已经提供联合成功数据；所有SFT/PrefixRL/TCOD等对照应获得相同数据。自然语言中间正确性检查不能由一句“验证”免费获得。
- RISK_COST_UNDERSPECIFIED：2k×1024只描述一次遍历；多个课程阶段、成功率测量、重复prefill和失败teacher制备未包含在一个确定总数内。现成专家能否达到所需能力尚未核实。

停止条件：预检没有稀有状态与条件增益，或后续等总预算下与TCOD-B2F＋同teacher聚合无差异；这否定当前方法价值主张，不等于发现论文完整scoop。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

