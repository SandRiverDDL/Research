# Qwen3 Section Index

```yaml
---
source_id: qwen3
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/qwen3/qwen3.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## Reading Map

| Section | Pages | Why Read | Related Notes | Keywords | Status |
|---|---:|---|---|---|---|
| Abstract / intro | 1-2 | core contribution and pipeline overview | `README.md` | thinking mode, 36T, distillation | read |
| Architecture | 3 | dense/MoE family details | `notes/architecture-pretraining.md` | QK-Norm, 128 experts | read |
| Pre-training | 3-9 | data and three-stage training | `notes/architecture-pretraining.md` | 36T, PDF extraction, synthetic math/code | partial |
| Post-training overview | 10 | four-stage pipeline | `notes/post-training.md` | cold start, RL, fusion, general RL | read |
| Long-CoT cold start / Reasoning RL | 10-11 | reasoning initialization and RL | `notes/post-training.md` | GRPO, entropy, pass@N | read |
| Thinking mode fusion | 11-12 | dual-mode template and budget | `notes/post-training.md` | /think, /no think, budget | read |
| General RL | 12 | reward system | `notes/post-training.md` | rule reward, model reward, agent ability | read |
| Strong-to-weak distillation | 12, 20-21 | small model recipe | `notes/distillation-eval.md` | off-policy, on-policy, KL | read |
| Eval | 12-23 | dual-mode eval and budget curves | `notes/distillation-eval.md` | benchmarks, budget, ablation | partial |

## If You Need...

- thinking/non-thinking mode control: pages 10-12.
- small model distillation: pages 12, 20-21.
- pretraining data: pages 2-9.
- eval setting: pages 12-23.

## Lookup Tables / Figures

- Table 1/2: dense and MoE architecture.
- Table 9: chat template for thinking/non-thinking modes.
- Figure 2: thinking budget scaling.
- Table 21/22: distillation and mode fusion ablations.

