# GLM-5.2 Evaluation

```yaml
---
source_id: glm-5.2
section_type: eval
stage: eval
substage: long-horizon-agentic
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- GLM-5.2 的 eval 主线是 long-horizon coding / agentic execution：FrontierSWE、PostTrainBench、SWE-Marathon、Terminal-Bench、MCP-Atlas、Tool-Decathlon 比传统 reasoning leaderboard 更贴近它声称的能力。[blog-glm-52]
- Release 把 1M context 和 max effort 放入 long-horizon eval setting，而不是只做默认短上下文推理；这让分数更贴近 agentic deployment，但也降低了和其他模型默认设置的可比性。[blog-glm-52]
- Anti-hack 不只用于训练，也进入 eval 设置，例如 NL2Repo 用 rule-based + LLM judgement 防止 malicious behaviors；这说明 coding eval 的方法设计已经包括 environment integrity。[blog-glm-52]
- Eval footnotes 披露了很多具体 setting：temperature/top-p、max tokens、context window、judge model、timeout、scaffold/harness、资源限制。相比只给榜单表，这对 claim audit 更有价值。[blog-glm-52]

## Why It Matters

这份 release 的 eval 值得学的是“怎么证明 long-horizon agentic model 真的能做事”。核心不是记住 GLM-5.2 在某个 benchmark 赢了谁，而是看它如何组合任务时间跨度、context budget、tool/scaffold、judge、timeout、anti-hack 和第三方 benchmark 服务。

这些 setting 也提醒你：agentic benchmark 极容易被 scaffold、timeout、token cap、internet access、judge model 和 anti-hack policy 改写结果。做 comparison 时要优先比较 eval methodology，而不是直接比较表格分数。

## Mechanism Sketch

1. 用 standard reasoning/coding/agentic benchmarks 给 broad capability map。
2. 用 long-horizon coding benchmarks 证明 1M context 和 max effort 在复杂任务上的实用价值。
3. 对不同 benchmark 单独设置 context length、max output、temperature、timeout、scaffold/harness 和 judge。
4. 在容易 reward hacking / benchmark hacking 的 coding eval 中加入 anti-hack filter / judge。
5. 把 benchmark table 当作 lookup，主线判断看 setting 是否支撑 release claim。

## Details / Evidence

- Long-horizon headline 包括 FrontierSWE、PostTrainBench、SWE-Marathon：这些 benchmark 关注小时到几十小时级工程任务、小模型后训练改进、编译器/kernel/服务构建等超长任务。[blog-glm-52]
- Standard coding benchmark 中，release 强调 Terminal-Bench 2.1 和 SWE-Bench Pro 相比 GLM-5.1 的提升；这支持“GLM-5.2 是 coding-agent 增量版本”的叙事。[blog-glm-52]
- HLE 等 reasoning tasks 使用 temperature 1.0、top-p 0.95、最大生成 163,840 tokens；HLE-with-tools 使用 300K max context 且无 context management strategy。[blog-glm-52]
- SWE-Bench Pro 用 OpenHands 和 tailored instruction prompt，400K context，temperature/top-p/max_new_tokens 单独设置。[blog-glm-52]
- DeepSWE 用 official pier evaluation framework 和 mini-swe-agent harness，isolated container，无 internet access；ProgramBench 则使用 Claude Code harness、长 timeout、400K context、internet disabled。[blog-glm-52]
- Terminal-Bench 2.1 同时给 Terminus-2 framework 和 Claude Code harness 两套结果；Claude Code setting 还通过 transparent proxy override max output token cap，并平均 5 runs。[blog-glm-52]
- MCP-Atlas 使用 500-task public subset、10-minute timeout、Gemini-3.0-Pro judge；Tool-Decathlon 使用 official evaluation service。[blog-glm-52]
- FrontierSWE、PostTrainBench、SWE-Marathon 的评测由外部/第三方组织执行，并使用 1M context、max effort、128K max output tokens。[blog-glm-52]

## Gaps / Open Questions

- Long-horizon benchmarks 的可比性高度依赖 scaffold、tool权限、timeout、context management、judge model；不同模型是否真正 same setting 需要逐个 benchmark 外部页面核查。
- 多个结果是 release-time reported scores；需要外部 leaderboard 或 benchmark owner 确认时间戳和版本。
- Max effort / 1M context 可能给 GLM-5.2 更有利的 compute budget；这不是错，但 comparison 时必须写清楚。
- Anti-hack filter 本身可能影响不同模型的行为分布；judge 误判会改变结果。
- Eval numbers 很丰富，但缺少针对 architecture/RL/anti-hack 机制的 ablation：比如没有看到“无 IndexShare / 无 anti-hack / 无 critic PPO”的最终 benchmark 对照。

## Lookup-only

- Full benchmark table: HLE、CritPt、AIME、HMMT、IMOAnswerBench、GPQA-Diamond、SWE-Bench Pro、NL2Repo、DeepSWE、ProgramBench、Terminal-Bench、FrontierSWE、PostTrainBench、SWE-Marathon、MCP-Atlas、Tool-Decathlon。[blog-glm-52]
- Headline examples: SWE-Bench Pro 62.1、Terminal-Bench 2.1 81.0/82.7、FrontierSWE 74.4、PostTrainBench 34.3、SWE-Marathon 13.0、MCP-Atlas 76.8、Tool-Decathlon 48.2。[blog-glm-52]
- Per-benchmark sampling/context/output/judge/scaffold settings in footnotes。[blog-glm-52]

## Evidence Anchors

- `[blog-glm-52]`: Benchmark overview, Full Benchmark Table, Footnote。
- `[hf-model-card]`: model card benchmark mirror。
