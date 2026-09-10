# Qwen3 Claims and Gaps

## High-confidence Claims

- Qwen3 的主创新是 thinking/non-thinking unified model、thinking budget 和 strong-to-weak distillation。[1-2, 10-12]
- 四阶段 post-training 结构清楚，但具体 reward/verifier/infra 披露不如 LongCat 或 Step。[10-12]
- Qwen3 主线应作为 `qwen3-coder-next` 的 lineage anchor，而不是被 coder 分支替代。

## Underdisclosed / Needs Audit

- Pretraining data cleaning、dedup、synthetic data filtering。
- Reasoning RL 的 off-policy 细节、entropy control 实现、reward/verifier。
- Teacher logits distillation 的系统成本和 loss 权重。

## Comparison Risks

- Qwen3 TR 是 2025-05 主线报告；后续 Qwen3-Coder-Next / Qwen3-VL / Qwen3-Omni 需要按分支 source 处理。
- 小模型 distillation 成功不等价于 full frontier model post-training 成功。

