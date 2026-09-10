# Mistral 3 Source Dossier

```yaml
---
source_id: mistral-3
source_type: model-tr
org: Mistral AI
release_date: 2025-12-02
priority: A
status: section-notes
openness: open-weights
confidence: high
lineage: mistral-3
role: major-release
---
```

## 一句话

Mistral 3 是一个需要拆开读的 Apache-2.0 开放权重 family：675B/41B-active 的 Mistral Large 3 只有发布级披露，真正有 post-training recipe 的是 3B/8B/14B Ministral 3，其主线是 Cascade Distillation 生成 base，再分别用 `SFT -> ODPO` 和 `CoT-SFT -> GRPO -> ODPO` 生成 instruct / reasoning variants。[blog-mistral-3] [3-6]

## 为什么重要

- 对当前 post-training 工作，Ministral 3 的价值不是全球 frontier positioning，而是把小模型的 teacher selection、logit distillation、online preference optimization、reasoning RL 和 post-RL alignment 连成一条有 ablation 的公开 pipeline。[5-6, 9-10]
- 对开放模型生态，它同时发布 base / instruct / reasoning 权重并采用 Apache 2.0，便于直接比较同一 base 上的不同 post-training 路线。[blog-mistral-3]
- Mistral Large 3 的训练 recipe 未公开，因此不能把 Ministral 3 的 SFT/ODPO/GRPO 流程默认外推到旗舰模型。

## 核心机制 / Takeaways

- Cascade Distillation 用 `prune -> short-context logit distillation -> long-context distillation -> repeat`，从 Mistral Small 3.1 逐级得到 14B、8B、3B base；这更接近 compute-efficient continued pretraining，而不是 post-training。[3-4]
- Instruct 路线是 multimodal/text SFT 加 ODPO；SFT 使用强 teacher 的 logit distillation，ODPO 从 current policy 在线采样两个 response，用 pairwise reward model 的概率输出形成 soft preference loss。[5]
- Reasoning 路线从 long-context base 而非 instruct checkpoint 出发，依次做 short/long CoT SFT、STEM GRPO、rubric + LLM-judge general GRPO、最后 ODPO 修复 conversational quality。[5-6]
- 3B 模型暴露了规模相关 failure mode：vanilla SFT 会过度冗长、重复甚至无限生成；用 Magistral Small teacher 做 logit distillation后才能稳定后续 RL。[6]
- Teacher 不是越强越好：pretraining distillation 中较近的 Mistral Small 3.1 优于更强的 Medium 3；post-training 则受益于更强 teacher，而且 preference-tuned teacher 优于只做过 SFT 的 teacher。[9]
- 长 CoT 注入 instruct SFT 会提高 STEM，但也会带来 excessive reflection / backtracking；Mistral 因而保留 instruct 与 reasoning 两条分支，而不是强行融合。[9-10]

## Source Bundle

- technical report: https://arxiv.org/abs/2601.08584
- announcement / blog: https://mistral.ai/news/mistral-3/
- weights: Mistral Large 3 与 Ministral 3 3B/8B/14B 的 base/instruct/reasoning checkpoints（官方 Hugging Face 链接见发布页）
- license: Apache 2.0
- local pdf: `papers/mistral-3/ministral-3.pdf`
- last checked: 2026-07-21

## Lineage / Delta

- lineage: Mistral 3
- role: family major release
- base source: Mistral Small 3.1 for Ministral 3 Cascade Distillation
- carries over: frozen Pixtral-style vision encoder and Mistral family serving stack
- newly disclosed: Cascade Distillation、SFT logit distillation、ODPO、reasoning GRPO 和 teacher-selection ablations
- not safe to inherit: Ministral 3 recipe 不能外推为 Mistral Large 3 recipe

## Citation Labels

- default TR pages: `[3-10]`
- non-TR source labels used:
  - `[blog-mistral-3]`: family release、Large 3 positioning、weights/license/deployment

## 最大证据缺口

- Large 3 没有独立 TR，pretraining data、SFT data、preference/RL objective 和 multimodal training 均未披露。
- Ministral 3 没有公开完整训练数据、reward model、rubric generation 和 ODPO/GRPO code/config；Apache 权重不等于 fully-open recipe。
- 多数 ablation 来自内部 harness，缺少外部 reproduction 和训练成本账本。

## Lens Hooks

- architecture: 大模型 MoE 与 edge dense family 的双层产品结构
- data-pipeline: multimodal/text mixture 只给类别，不给可复现配比
- training-recipe: Cascade Distillation 与规模相关 teacher selection
- rl-training: STEM GRPO -> rubric general GRPO -> ODPO
- eval: 同一 base 的 instruct/reasoning 分支和 size scaling
- infra: FP8 SFT、NVFP4/serving support，但训练 infra 披露有限

## 阅读入口

- 先读 `notes/post-training.md`：与你当前工作的直接相关部分。
- 再读 `notes/cascade-distillation.md`：理解 base 由何而来以及 teacher selection 为什么不能简单按能力排序。
- 需要判断可信度时读 `notes/claims-and-gaps.md`。
- Mistral Large 3 只回发布页，不从 Ministral 3 TR 推断其训练细节。
