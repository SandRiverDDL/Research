# MAI-Thinking-1 Evaluation

```yaml
---
source_id: mai-thinking-1
section_type: eval
stage: eval
substage: none
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 核心设计是把 eval 当成 hill-climbing gate，而不是只做 leaderboard：public hard benchmarks、simple agentic loop、human preference、safety/health/tool eval 共同反馈模型迭代。[53-55, 101-106]
- Agentic coding eval 刻意使用 simple ReAct-style append loop，减少复杂 proprietary scaffold 对模型能力判断的干扰。[54, 101]
- Human side-by-side 用 expert prompts + filtered Copilot logs，强调 product-relevant behavior，但也牺牲了完全公开复现性。[55]
- MAI 报告 4-run average 和统一 sampling settings，说明它关注 sampling variance；但 closed-model comparison 仍依赖 Microsoft 自己的 eval setup。[53-54]

## Why It Matters

MAI 的 eval 部分不是最“惊艳”的方法，但能体现工业模型开发 taste：不能只看 AIME / SWE-Bench 分数，还要把 agent loop、human preference、safety gates 和 appendix methodology 放进同一个 hill-climbing loop。对 post-training 工作来说，这比单个 benchmark 排名更实用。

## Mechanism Sketch

1. 用 public hard benchmarks 报告 STEM、coding、knowledge、instruction following、long context、safety、health、tool calling 等能力。[53-54]
2. 用 simple ReAct-style agentic setup 测 SWE / Terminal-Bench，降低 scaffold confound。[54, 101]
3. 用 human side-by-side 测产品相关任务，包括 multi-turn 和 Copilot-log-derived prompts。[55]
4. 用 appendix 补充 agentic coding、safety、general capabilities、health、tool-calling eval details。[101-106]

## Details / Evidence

- Headline results 包括 SWE-Bench Pro 52.8%、AIME 2025 97.0%、AIME 2026 94.5%、LiveCodeBench v6 87.7%。[1-2]
- Benchmark evaluations 覆盖 STEM、agentic coding、knowledge、instruction following、long context、safety、health、honesty、tool calling，并对比 open- and closed-weight frontier models。[53-54]
- MAI benchmark numbers 是 4 runs 平均，统一 inference settings：temperature 1、top-p 0.97，除非另有说明。[53]
- Agentic coding evals 包括 SWE-bench Verified、SWE-Bench Pro、Terminal-Bench 2.0；设置是 simple ReAct-style append loop、256K context、SWE tasks 使用 bash/string-replace tools，Terminal-Bench 使用 bash-only。[54, 101]
- 对 Terminal-Bench 2.0，报告忽略 predefined timeouts，以避免 inference speed/infrastructure confounding。[54]
- Human side-by-side evaluation 使用 1276 个英文任务，其中 30% 是 multi-turn；任务来自 expert-authored prompts 和过滤后的 Microsoft consumer Copilot logs。[55]
- Human raters 由 Surge AI 管理，评价维度包括 instruction following、factuality、conciseness/relevance、completeness、style/tone，以及最终 7-point preference。[55]

## Gaps / Open Questions

- 哪些 benchmark prompts 从 pretraining/mid-training/RL data 中 decontaminate 了，没有完整披露。
- 结果对 4-run sampling setting 有多敏感，不清楚。
- Microsoft 自己 eval suite 里生成的 Sonnet 4.6 numbers 与 Anthropic official numbers 的可比性需要谨慎。
- 忽略 Terminal-Bench timeouts 会失去真实 agent deployment 信号，需要比较时标注。

## Lookup-only

- Headline benchmark numbers、Table 11/12 entries、appendix task details、各 benchmark exact setup。

## Evidence Anchors

- 1-2: headline benchmark claims。
- 53-54: public benchmark setup/results。
- 54: agentic coding/tool eval setup。
- 55: human side-by-side eval task/rater process。
- 101-106: appendix eval details。
