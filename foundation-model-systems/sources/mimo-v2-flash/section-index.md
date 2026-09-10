# MiMo-V2-Flash Section Index

```yaml
---
source_id: mimo-v2-flash
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/mimo-v2-flash/mimo-v2-flash-tech-report.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## 用法

这是 MiMo-V2-Flash TR 的导航层，不是 summary。后续写 OPD / RL / agentic eval lens 时，先读本文件判断要回哪些页。

## Source Files

- TR PDF: `/Users/chy/Research/foundation-model-systems/papers/mimo-v2-flash/mimo-v2-flash-tech-report.pdf` (31 pages)
- arXiv: https://arxiv.org/abs/2601.02780

## Reading Map

| Section | Pages | Why Read | Related Notes | Keywords | Status |
|---|---:|---|---|---|---|
| Abstract / Introduction | 1-4 | source-level claims, model positioning, MOPD headline | `README.md`, `notes/claims-and-gaps.md` | 309B/15B, MOPD, MTP | read |
| Architecture overview | 5-6 | MoE, Hybrid SWA/GA, config table | `notes/architecture.md` | SWA, GA, MoE, FP8 | read |
| Hybrid SWA ablations | 7-8 | attention sink, SWA window, long-context/reasoning effects | `notes/architecture.md` | attention sink, window 128 | read |
| MTP motivation/design | 9 | MTP as training objective + speculative decoding + RL rollout accelerator | `notes/architecture.md`, `notes/inference.md` | MTP, rollout speed | read |
| Pre-training | 9-10 | 27T schedule, code/synthetic reasoning, context extension | `notes/pretraining.md` | 32K, 256K, 27T | read |
| MOPD overview | 11-14 | three-stage post-training, multi-teacher consolidation, Table 7 | `notes/mopd.md` | MOPD, reverse KL, teachers | read |
| SFT | 14-15 | SFT data, MoE stability metric `num-zeros` | `notes/rl-training.md` | SFT, num-zeros | read |
| Domain-specialized RL | 15-17 | non-agentic and agentic RL, code/search/general agent environments | `notes/rl-training.md` | code agent, Kubernetes, tools | read |
| MOPD technical formulation | 18 | reverse-KL token advantage, importance sampling, ORM combination | `notes/mopd.md` | A_MOPD, ORM, IS | deep |
| Eval setup/results | 18-20 | benchmark scope, MOPD ablation, open/closed comparison | `notes/eval.md` | Table 9, Figure 6 | read |
| RL/inference infra | 20-21 | request prefix cache, Toolbox/Tool Manager | `notes/inference.md`, `notes/rl-training.md` | KV cache, Ray, async reward | read |
| MTP inference speed | 21-22 | entropy vs accept length, decoding speedup table | `notes/inference.md` | speculative decoding | read |
| Conclusion / limitations | 22 | limitations and future MOPD co-evolution | `notes/claims-and-gaps.md` | limitations | read |
| References / appendix material | 22-31 | citation lookup only | none | references | skim |

## If You Need...

- MOPD: read pages 11-14 and 18, then `notes/mopd.md`.
- post-training / RL: read pages 14-17, then `notes/rl-training.md`.
- architecture / model structure: read pages 5-9, then `notes/architecture.md`.
- pretraining: read pages 9-10, then `notes/pretraining.md`.
- eval methodology: read pages 18-20, then `notes/eval.md`.
- inference / rollout speed: read pages 9 and 20-22, then `notes/inference.md`.
- V2.5-Pro TR status: read `source-bundle.md`; currently no full TR found.

## Read Coverage

- Read into notes:
  - architecture: pages 5-9.
  - pretraining: pages 9-10.
  - post-training RL: pages 11-17 and 20-21.
  - MOPD: pages 11-14 and 18-19.
  - eval: pages 18-20.
  - inference: pages 9 and 20-22.
- Skimmed only:
  - references pages 22-31.
- Need revisit before comparison:
  - pages 11-14 and 18 for OPD/MOPD comparison.
  - pages 15-17 for agentic RL environment scaling.
  - pages 20-22 if comparing rollout/inference infra with GLM-5.2 slime.

## Lookup Tables / Figures

- Figure 2: architecture.
- Table 1: model configuration.
- Tables 2-4: architecture ablations.
- Table 5: base model comparison.
- Table 6: long context comparison.
- Figure 3: post-training stages.
- Table 7: MOPD before/after vs best teacher.
- Table 8: agentic RL data composition.
- Figure 4/5: RL scaling curves.
- Figure 6: ORM vs MOPD ablation.
- Table 9: final benchmark comparison.
- Figure 7 and Table 10: MTP acceptance length / speedup.
