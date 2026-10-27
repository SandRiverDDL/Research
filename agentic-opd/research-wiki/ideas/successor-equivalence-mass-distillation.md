---
type: idea
node_id: idea:successor-equivalence-mass-distillation
title: "把 teacher 的下一步效应蒸馏成等价行动集合"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:agarwal2023_onpolicy_distillation_language", "paper:gu2023_minillm_onpolicy_distillation", "paper:wang2026_cast_game_solvers", "paper:chen2026_look_ahead_before"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "shortlist-rank-1"]
---

# 把 teacher 的下一步效应蒸馏成等价行动集合

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A1；生成模型 `gpt-6-astra`；首轮推荐第1项。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 实际访问的 h，teacher 生成少量工具行动，student 再生成若干候选；在环境副本执行这些行动。
2. 按可核验的任务可见效应分组，例如返回证据、文件变化和资源消耗；teacher 行动的经验频率定义效应分布 qT(z|h)。
3. 训练 student 给达到同一目标效应的行动集合分配概率质量，随后继续自主 rollout。

更新规则：L = −Σz qT(z|h) log Σ[a∈Az] πθ(a|h)。a 是包含结束符的完整工具调用；未枚举行动的概率归入 other。Az 可以同时包含 teacher 与 student 提出的行动。

待验证假设：多轮工具任务允许不同语法、路径或操作顺序产生相同有效状态；按效应聚合监督能保留 student 的可行策略，减少逐 token 模仿带来的无益替换。

查新结论（早期文献核查，不是效果验证）：P。[semantic STOP](https://arxiv.org/abs/2609.20511)已有等价动作概率求和；新增的是**在student状态执行候选、据环境效应建立等价类**。不能claim求和原理首创。

最小验证：先做可重置文件操作与结构化检索两个环境；比较 OLIVE 式 CE、相同候选逐条 CE、集合概率质量目标；匹配 teacher tokens、候选数和环境调用，测成功率、等价行动覆盖和总成本。

同数据、同总成本的关键对照：完全相同候选与执行结果，比较逐行动CE与集合质量目标；计入所有分叉。

## Key risks
效应签名可能把影响后续任务的不同状态误合并；严格签名又可能几乎没有可合并样本。

评审补充：即时效应相同不保证未来等价；少量teacher样本估计类分布很噪。

证伪条件：在存在大量可验证等价行动的设置中，集合目标仍不优于相同数据的逐条 CE；或者收益只来自额外环境调用。

资源条件：Black-box 独立 teacher 文本输出；student 完整行动 logprob；环境 snapshot/branch；可审计效应签名。隐藏状态可用于验证，但不能输入部署 student。

估算：条件估算：小模型 pilot 约 1–2 人周；每状态 2 个 teacher 加 4 个 student 候选，需要最多 6 次单步分叉。训练与评测 GPU 成本取决于未确认的硬件。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[agarwal2023_onpolicy_distillation_language](../papers/agarwal2023_onpolicy_distillation_language.md)；[gu2023_minillm_onpolicy_distillation](../papers/gu2023_minillm_onpolicy_distillation.md)；[wang2026_cast_game_solvers](../papers/wang2026_cast_game_solvers.md)；[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

