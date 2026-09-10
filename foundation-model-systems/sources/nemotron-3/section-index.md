# Nemotron 3 Section Index

```yaml
---
source_id: nemotron-3
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/nemotron-3/nemotron-3-super.pdf
  - /Users/chy/Research/foundation-model-systems/papers/nemotron-3/nemotron-3-ultra.pdf
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
| Super architecture | Super 3-8 | LatentMoE, MTP, Hybrid Mamba-Attention | `notes/architecture-pretraining.md` | LatentMoE, MTP | read |
| Super NVFP4 / data / long context | Super 8-18 | pretraining recipe and data ordering | `notes/architecture-pretraining.md` | NVFP4, 25T, WSD | read |
| Super post-training | Super 18-30 | SFT, multi-env RL, SWE-RL, RLHF, async GRPO | `notes/post-training.md` | RLVR, SWE-RL | read |
| Super quantization | Super 33-37 | FP8/NVFP4 deployment | `notes/infra-quantization.md` | FP8, FP4 | read |
| Ultra pretraining | Ultra 3-15 | scaled Ultra recipe and stability diagnostics | `notes/architecture-pretraining.md` | 550B, stability | partial |
| Ultra post-training / MOPD | Ultra 15-33 | MOPD, teachers, warmup, rollout infra | `notes/post-training.md` | MOPD, teachers | read |
| Ultra eval | Ultra 33-40 | open frontier positioning | `notes/post-training.md` | SWE, Terminal, agentic | skim |
| Ultra quantization | Ultra 41-47 | NVFP4 operating point | `notes/infra-quantization.md` | Blackwell | read |

## If You Need...

- system recipe: start with Super 3-30, then Ultra 15-33.
- MOPD details: Ultra 20-29, then compare Cascade 2 and MiMo.
- deployment/quantization: Super 33-37 and Ultra 41-47.

## Lookup Tables / Figures

- Super Figure 12: post-training pipeline.
- Super Table 6: FP8 precision recipe.
- Ultra Table 12: quantization recipe.
