# Qwen3-Coder-Next Section Index

```yaml
---
source_id: qwen3-coder-next
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/qwen3-coder-next/qwen3-coder-next.pdf
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
| Intro | 1-2 | positioning and model goal | `README.md` | 80B-A3B, coding agent | read |
| Scaling up Agentic Training | 2-3 | task synthesis and infra | `notes/agentic-training.md` | executable environments | read |
| Mid-training data | 3-6 | natural/synthetic/multi-turn/FIM data | `notes/agentic-training.md` | agentic mid-training | read |
| Post-training | 6-11 | SFT, experts, distillation | `notes/expert-distillation.md` | WebDev, UX, QA, SWE | read |
| Experiments | 11-13 | agentic/coding/general eval | `notes/eval.md` | SWE, Terminal | read |
| Infra notes | 13+ | Slurm/Ray bottlenecks | `notes/agentic-training.md` | Slurm, Ray | partial |

## If You Need...

- agentic coding recipe: pages 2-6.
- expert distillation: pages 6-11.
- eval: pages 11-13 and model card/blog.

## Lookup Tables / Figures

- Figure 1: active parameter efficiency benchmark comparison.
- Post-training expert figures/pages 6-11.
