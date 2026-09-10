# Mistral 3 Post-training Summary

```yaml
---
source_id: mistral-3
stage: post-training
summary_role: small-model-recipe-anchor
priority_for_post_training: A
confidence: high
---
```

## Verdict

Mistral 3 必须分开判断：Mistral Large 3 只有开放权重与发布级定位，没有 post-training recipe；Ministral 3 3B/8B/14B 才有可核查流程，并明确分成 Instruct 的 `SFT -> ODPO` 与 Reasoning 的 `CoT-SFT -> GRPO -> ODPO`。[blog-mistral-3] [5-10]

## Pipeline

### Instruct Branch

```text
Cascade-distilled base
-> multimodal + text SFT with Mistral Medium 3 logit distillation
-> online response-pair sampling
-> probabilistic pairwise reward model
-> ODPO alignment
```

### Reasoning Branch

```text
long-context base
-> short + long CoT SFT
-> STEM GRPO (math / code / visual reasoning)
-> rubric + LLM-judge General GRPO
-> ODPO conversational repair
```

- Reasoning 从 base 而不是 Instruct/ODPO checkpoint 开始，说明两条路线追求不同policy geometry。[5-6]
- ODPO 在current policy上以temperature 0.7采两个responses，用PWRM概率而非hard label形成双侧preference loss；无限循环样本直接判loser，并允许tool execution。[5]

## Core Mechanisms

### SFT Logit Distillation

- Instruct SFT 使用更强 Mistral Medium 3 teacher logits；3B Reasoning 的 vanilla SFT会出现brittle、verbosity、repetition和infinite generation，因此改用Magistral Small teacher稳定后续RL。[5-6]
- Preference-tuned teacher优于只有SFT的teacher，而且收益在student后续做preference optimization后仍存在。[9]

### Two-stage GRPO

- STEM阶段用可验证math/code/vision tasks；General阶段为open-ended prompts生成atomic rubrics，由LLM judge按满足比例给reward。[6]
- 最大生成长度从32K增至80K以减少hard problems截断；这提高完成率，也增加length exploitation风险。

### Post-RL Preference Repair

- Reasoning policy在hard tasks提升后，general conversation quality下降；最终ODPO评分前剥离thinking chunks，只优化用户可见回答。[6, 10]
- 14B/8B公开alignment eval改善明显；3B公开分数不明显但内部human eval较好，显示规模相关收益不一致。[10]

## Failure Modes / Controls

- Long-CoT注入Instruct SFT会提高STEM但产生excessive reflection/backtracking，因此没有强行统一两种behavior。[9-10]
- PWRM/LLM judge可能有style bias和reward hacking；rubric生成、judge identity与calibration未公开。
- 3B对SFT和ODPO超参更敏感，不能把14B recipe原样缩放。

## Openness and Evidence

- Apache-2.0 base/instruct/reasoning权重；Ministral TR有阶段流程和ablation，但data/config/code/logs未fully open。
- Large 3不能继承Ministral recipe，只能作为permissive-open flagship reference。

## Transfer to Current Work

- 比较hard-label SFT、logit-distilled SFT与preference-tuned-teacher distillation，特别关注小模型verbosity/infinite generation。
- 在reasoning RL后加入独立conversation/preference repair，并检查是否损害STEM/code pass-rate。
- Instruct/Reasoning unified-vs-split应以quality、tokens、latency、maintenance和mode interference共同评估。

## Evidence Anchors

- [post-training.md](post-training.md): pages 5-6, 9-10 detailed mechanism。
- [cascade-distillation.md](cascade-distillation.md): base provenance and teacher choice。
- [claims-and-gaps.md](claims-and-gaps.md): Large 3 / Ministral evidence boundary。
- [../README.md](../README.md): `[blog-mistral-3]` family release evidence。
