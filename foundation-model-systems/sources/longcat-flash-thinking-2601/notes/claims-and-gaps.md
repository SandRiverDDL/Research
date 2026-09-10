# LongCat-2601 Claims and Gaps

## High-confidence Claims

- 2601 是 LongCat-Flash-Thinking 的更新版完整 TR，agentic reasoning 是核心定位。[1-3]
- Environment scaling、DORA 异步 rollout、多域环境训练和 noisy robust training 是此 source 最有价值的内容。[3-16]
- 相比普通 benchmark 分数，训练/环境/infra 设计更值得进入 lens。

## Underdisclosed / Needs Audit

- Environment generator prompts、reward/verifier、domain sampling ratios。
- GSPO/DORA 细节和开源实现状态。
- Heavy Thinking 的模型/采样/summary 配置。

## Comparison Risks

- LongCat 的 environment pipeline 很强，但开放程度不等于 Olmo 3；不要把“TR 写得细”误当成“可复现”。
- 和 Step 比较时要区分：LongCat 强在环境规模化，Step 强在低 active params 的 agent latency/cost co-design。

