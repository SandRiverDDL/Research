# Step 3.5 Flash Claims and Gaps

## High-confidence Claims

- Step 3.5 Flash 是当前 StepFun 最完整公开训练 TR；Step 3.7 是更新模型但主要是 model card/blog disclosure。
- 核心技术主线是 low-active-parameter agent model：hybrid attention + MTP + self-distillation + MIS-PO。
- MIS-PO 是值得进 RL lens 的独立机制。

## Underdisclosed / Needs Audit

- MIS-PO thresholds、reward/verifier、rollout freshness、advantage estimator。
- Expert models 的构建细节和 distillation mixture。
- Step 3.7 的训练 recipe。

## Comparison Risks

- Step 的 headline benchmark 包含复现和非官方 baseline，eval comparison 要优先看 setting。
- Step 和 LongCat 都讲 agentic RL，但 Step 更偏 latency/cost + off-policy stability，LongCat 更偏 environment scaling + async infra。

