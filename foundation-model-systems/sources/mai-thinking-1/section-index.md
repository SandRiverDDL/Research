# MAI-Thinking-1 Section Index

```yaml
---
source_id: mai-thinking-1
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/mai-thinking-1/mai-thinking-1-tech-report.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## 用法

这是 MAI-Thinking-1 TR 的导航层，不是 summary。后续写 lens 或 comparison 时，先读本文件判断要看哪些 notes 或 PDF 页码。

## Source Files

- TR PDF: `/Users/chy/Research/foundation-model-systems/papers/mai-thinking-1/mai-thinking-1-tech-report.pdf` (109 pages)

## Reading Map

| Section | Pages | Why Read | Related Notes | Keywords | Status |
|---|---:|---|---|---|---|
| Abstract / Introduction | 1-2 | Hill-climbing framing、from-scratch/no-distillation/data/eval headline claims | `README.md`, `notes/claims-and-gaps.md` | hill-climbing, no distillation | read |
| TOC | 3-4 | 定位全篇结构 | `section-index.md` | TOC | read |
| Pre-training overview | 5 | MAI-Base-1、30T + 3.55T、GB200 cluster | `notes/pretraining-data-mixture.md`, `notes/pretraining-engineering.md` | pretraining, mid-training | read |
| Model architecture | 6-8 | MoE / attention / infra co-design；不是第一轮重点 | 未单独建 note | 35B active, 1T total, MoE | skim |
| Model ablation / eval methodology | 7-12 | Scaling ladders、NLL eval philosophy | `notes/pretraining-data-mixture.md` | ladder, NLL | partial |
| Pre-training data | 12-16 | Source families、governance、no synthetic / no open datasets | `notes/pretraining-data-mixture.md` | data governance, decontam | read |
| Data mixture selection | 16-20 | Scale-dependent data mixture、rank non-invariance、final mix | `notes/pretraining-data-mixture.md` | data mix, NLL, epochs | read |
| Training recipe / mid-training | 21-23 | Context extension / mid-training schedule；continued pretraining 工程主线 | `notes/pretraining-engineering.md` | mid-training, context, precision | read |
| YOLO / distributed training | 24-30 | Training infra、parallelism、checkpoint、determinism、architecture/infra co-design | `notes/pretraining-engineering.md` | GB200, distributed training, YOLO | read |
| RL climb overview | 30-31 | Specialist climbs + consolidation map | `notes/rl-training.md`, `notes/consolidation.md` | STEM, agentic, safety | read |
| RL recipe | 31-37 | GRPO-derived objective、adaptive entropy、outer ratio clip、reward decomposition、sampling、self-distillation | `notes/rl-training.md`, `notes/sft-distillation.md` | GRPO, entropy, length penalty | read |
| STEM climb | 37-39 | Math/science/coding climb and CoT evolution | `notes/rl-training.md` | AIME, LiveCodeBench | read |
| Agentic climb | 39-44 | SWE/tool-use training and environments | `notes/rl-training.md`, `notes/eval.md` | SWE, tool use | read |
| Helpfulness / safety climb | 44-49 | IF/safety data, reward signals, unsafe compliance vs over-refusal | `notes/rl-training.md`, `notes/claims-and-gaps.md` | IF, safety, reward | partial |
| Consolidation / RL infrastructure | 49-52 | Specialist trace distillation SFT + final RL; RL infra | `notes/consolidation.md` | consolidation, final climb | read |
| Evaluations | 53-55 | Benchmarks, human side-by-side, safety eval | `notes/eval.md` | SWE-Bench Pro, AIME, human eval | read |
| Safety red teaming | 56-58 | Safety process; not first-round focus | `notes/claims-and-gaps.md` | red team | skim |
| Cluster environment | 59-61 | Infra and deployment; Appendix L has details | `notes/pretraining-engineering.md` | GB200, goodput, sustainability | skim |
| Conclusion | 61 | Project-level framing and future directions | `notes/claims-and-gaps.md` | hill-climbing machine | read |
| Appendix B: data pipeline | 82-85 | Web/PDF/books/GitHub pipeline details | `notes/pretraining-data-mixture.md` | HTML, PDF, GitHub, dedup | read |
| Appendix C: long context | 85-88 | Context extension details; useful for pretraining engineering lens | `notes/pretraining-engineering.md` | 256K, long context | read |
| Appendix D: reasoning traces | 89-94 | CoT evolution examples | `notes/rl-training.md` | STEM CoT, agentic CoT | partial |
| Appendix E-G | 94-98 | SWE tool schema / IF taxonomy / SWE environment infra | `notes/rl-training.md`, `notes/eval.md` | tool schema, IF taxonomy | partial |
| Appendix H-K | 98-106 | STEM, agentic coding, safety, general eval details | `notes/eval.md` | eval setup | partial |
| Appendix L | 106-109 | Cluster topology、certification、scheduling、observability | `notes/pretraining-engineering.md` | cluster, observability, goodput | read |

## If You Need...

- data pipeline / mixture: read pages 12-20 and Appendix B pages 82-85, then `notes/pretraining-data-mixture.md`.
- base-model / pretraining intuition: read pages 5-23, especially 16-21, then `notes/pretraining-data-mixture.md` and `notes/pretraining-engineering.md`.
- continued pretraining / long context / training infra: read pages 21-30, Appendix C pages 85-88, Appendix L pages 106-109, then `notes/pretraining-engineering.md`.
- post-training RL recipe: read pages 31-37, then `notes/rl-training.md`.
- self-distillation: read pages 34-37, then `notes/sft-distillation.md`.
- specialist consolidation: read pages 31 and pages 49-50, then `notes/consolidation.md`.
- agentic coding training/eval: read pages 39-44 and Appendix I pages 101, then `notes/eval.md`.
- safety/helpfulness: read pages 44-49, pages 55-58, Appendix J pages 101-103.
- infra: read pages 24-30, pages 59-61, Appendix L pages 106-109, then `notes/pretraining-engineering.md`; create separate `infra.md` only if a later infra lens needs more depth.
- claim audit: read `notes/claims-and-gaps.md`, then revisit 1-2, pages 12-20, pages 31-37, pages 53-55.

## Read Coverage

- Read into notes:
  - data pipeline: 1-2, pages 5, pages 12-20, pages 82-85.
  - pretraining engineering: pages 21-30, pages 85-88, pages 106-109.
  - post-training RL: 1-2, pages 31-37, pages 39-50, pages 89-94, pages 97-101.
  - eval: 1-2, pages 53-55, pages 101-106.
  - claims/gaps: 1-2, pages 5, pages 12-20, pages 31-33, pages 49-55, pages 61.
- Skimmed only:
  - architecture 6-8.
  - cluster environment 59-61.
- Not read yet:
  - full safety red teaming details.
  - visual inspection of full long-context figures.
  - full infra implementation details beyond the report text.
- Need revisit before comparison:
  - 31-37 for RL recipe details if comparing recipe transferability.
  - 16-21 for base-model data taste and continued-pretraining handoff.
  - 21-30 and 85-88 if comparing long-context / pretraining-engineering choices.
  - 53-55 + Appendix I/K for eval comparability.
  - 49-50 for consolidation vs DeepSeek OPD.

## Lookup Tables / Figures

- Figure 1: RL climb curves (1).
- Figure 2: MAI-Base-1 architecture (5).
- Figure 5 / 6 / 7: data mixture frontier and rank non-invariance (16-19).
- Table 4: source-family knowledge cutoffs (13).
- Table 5: pretraining data composition (20).
- Figure 12: specialist climbs and consolidation (31).
- Figure 13: adaptive entropy control (32).
- Table 11 / 12: benchmark results (53-54).
- Table 13: human side-by-side task distribution (55).
