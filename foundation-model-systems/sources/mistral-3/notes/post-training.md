# Mistral 3 Post-training

```yaml
---
source_id: mistral-3
section_type: post-training
stage: post-training
substage: sft-preference-rl
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 同一 base 被明确分成两条路线：Instruct 用 `SFT -> ODPO`，Reasoning 用 `CoT-SFT -> GRPO -> ODPO`；Mistral 没有把所有模型强行做成 unified thinking/non-thinking policy。[5-6]
- Instruct SFT 本身包含来自 Mistral Medium 3 的 logit distillation，而不只是 hard-label response imitation。[5]
- ODPO 在 current policy 上在线采两个 responses，以 pairwise reward model 排序，并用偏好概率而非 hard winner/loser 调整 DPO loss。[5]
- Reasoning RL 先做可验证的 STEM/visual tasks，再做 rubric + LLM judge 的 general RL，最后用 ODPO 修复 reasoning model 的聊天与指令质量。[6]

## Why It Matters

- 这是一个清楚展示“capability RL 后仍需要 preference repair”的小模型 recipe；它适合和 Qwen3 的 mode fusion、OLMo 3 的 Think/Instruct 分流、Nemotron Cascade 的阶段式 RL 对比。
- 3B 的失败说明 post-training recipe 不具 scale invariance：同样的 vanilla SFT 在小模型上会产生 verbosity、repetition 和 infinite generation，必须先用 teacher logits 稳定 policy。[6]
- Instruct 中增加 long CoT 虽提升 STEM，却损害自然聊天风格，说明 reasoning data mixture 不能只看 task accuracy。[9-10]

## Mechanism Sketch

### Instruct

1. 以 high-quality multimodal + text instruction data 做 SFT。
2. 冻结 vision encoder、训练 adapter，并用 Mistral Medium 3 logits 蒸馏。
3. ODPO 在线采样 response pairs，PWRM 输出 win probabilities。
4. 用概率加权的双侧 DPO loss、reward temperature calibration 和 beta rescaling 做 alignment；无限循环样本强制判 loser，并允许 rollout 执行 tools。[5]

### Reasoning

1. 从 long-context base 开始，不继承 instruct/ODPO checkpoint。
2. 对 short + long CoT 做 SFT，过滤格式错误、重复和异常 language switching。
3. STEM GRPO：math/code/visual reasoning，过滤 invalid、过易和过难题。
4. General GRPO：为 open-ended prompts 生成 atomic rubrics，让 LLM judge 按满足比例给 reward。
5. Post-RL ODPO：评分前去除 thinking chunks，只优化用户可见回答的 preference quality。[5-6]

## Details / Evidence

- Reasoning GRPO 的最大生成长度从 32K 增加到 80K，以减少 hard problems 的截断。[6]
- ODPO 对 14B/8B 的公开 alignment benchmark 改善明显；3B 的公开分数改善不明显，但内部 human eval 更好，因此仍选 ODPO checkpoint 发布。[10]
- Preference-tuned teacher 做 SFT distillation 优于只有 SFT 的 teacher，而且收益在 student 自己做 preference optimization 后仍保留。[9]

## Gaps / Open Questions

- SFT/CoT 数据来源、比例、teacher version 和过滤阈值未公开。
- PWRM data、calibration、ODPO beta-rescaling 细节及实现没有代码锚点。
- General RL 的 rubric generator 和 judge identity 未公开，存在 evaluator bias / reward gaming 风险。
- 没有把 `SFT -> GRPO -> ODPO` 与 joint/mixed objective 做充分对照。

## Lookup-only

- ODPO pair sampling temperature: 0.7。
- GRPO max generation length: 80K。
- reasoning trace domains: math、code、general dialogue、IF、multilingual、tool use、visual reasoning。

## Evidence Anchors

- 5: Instruct SFT/ODPO、Reasoning SFT 起点与数据。
- 6: 3B SFT failure、STEM/general GRPO、post-RL ODPO。
- 9-10: teacher、long-CoT 和 ODPO ablations。
