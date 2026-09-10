# Mistral 3 Section Index

## Source Map

| Topic | Primary source | Pages / anchor | Read status | Notes |
|---|---|---:|---|---|
| family positioning / Large 3 | release blog | `[blog-mistral-3]` | read | 675B total / 41B active, Apache 2.0; no recipe |
| architecture | Ministral 3 TR | 2-3 | skimmed | dense 3B/8B/14B, frozen vision encoder, 256K context |
| Cascade Distillation | Ministral 3 TR | 3-5 | read | pruning, forward-KL logit distillation, long context |
| instruct post-training | Ministral 3 TR | 5 | read | SFT logit distillation + ODPO |
| reasoning post-training | Ministral 3 TR | 5-6 | read | CoT SFT + STEM/general GRPO + ODPO |
| eval | Ministral 3 TR | 6-8 | skimmed | internally rerun size-matched baselines |
| teacher / recipe ablations | Ministral 3 TR | 9-10 | read | teacher strength, preference-tuned teacher, long-CoT tradeoff |
| conclusion / references | Ministral 3 TR | 11-14 | lookup | no additional recipe detail |

## If You Need

- post-training pipeline: pages 5-6, then 9-10 for ablations.
- Cascade Distillation mechanics: pages 3-5.
- Mistral Large 3: use `[blog-mistral-3]`; the TR does not cover it.
- exact benchmark numbers: pages 7-8; keep lookup-only unless a comparison depends on them.
