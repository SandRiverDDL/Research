# DeepSeek-V4 Section Index

```yaml
---
source_id: deepseek-v4
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/deepseek-v4/deepseek-v4-tech-report.pdf
  - /Users/chy/Research/foundation-model-systems/papers/deepseek-v4/deepseek-v4-model-card.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## 用法

这是 DeepSeek-V4 TR 的导航层，不是 summary。后续写 lens 或 comparison 时，先读本文件判断要看哪些 notes 或 PDF 页码。

## Source Files

- TR PDF: `/Users/chy/Research/foundation-model-systems/papers/deepseek-v4/deepseek-v4-tech-report.pdf` (58 pages)
- model card: `/Users/chy/Research/foundation-model-systems/papers/deepseek-v4/deepseek-v4-model-card.pdf` (8 pages)

## Reading Map

| Section | Pages | Why Read | Related Notes | Keywords | Status |
|---|---:|---|---|---|---|
| Abstract / headline claims | 1 | 模型规模、1M context、efficiency 和 headline benchmark claims | `README.md`, `notes/claims-and-gaps.md` | 1.6T, 49B active, 1M context | read |
| Introduction | 4-5 | Long-context / test-time scaling motivation | `notes/architecture.md` | test-time scaling, long-horizon | read |
| Architecture overview | 6-8 | V3 inheritance, mHC, MoE changes | `notes/architecture.md` | DeepSeekMoE, mHC, MTP | read |
| CSA / HCA | 9-13 | Long-context efficiency 的核心机制 | `notes/architecture.md` | CSA, HCA, KV compression | read |
| Muon optimizer | 14 | Optimizer 变化和 training stability 线索 | `notes/architecture.md` | Muon, AdamW | read |
| General infrastructure | 14-23 | Expert parallelism、kernel、training/inference framework | 未单独建 note | EP, TileLang, KV cache | skim |
| Pre-training data | 24 | Data categories 和 corpus high-level disclosure | `notes/claims-and-gaps.md` | 32T, code, math, long docs | read |
| Model / training setup | 24-26 | 参数、schedule、context extension、sparse attention warmup | `notes/architecture.md` | 4K->1M, MoE, dense warmup | read |
| Training instability | 26 | MoE spike mitigation | `notes/architecture.md` | Anticipatory Routing, SwiGLU clamping | read |
| Base eval | 27-28 | Base model capability comparison | `notes/eval.md` | V3.2, V4-Flash, V4-Pro | read |
| Post-training pipeline | 28-33 | Specialist training、reasoning modes、GRM、OPD | `notes/consolidation.md`, `notes/reward-verifier.md` | GRPO, GRM, OPD, Think Max | read |
| Post-training infrastructure | 33-36 | Full-vocab OPD、FP4 QAT、WAL、sandbox | `notes/consolidation.md`, `notes/tool-agent-training.md` | full-vocab OPD, DSec | read |
| Standard benchmark eval | 36-40 | Public benchmark setup and results | `notes/eval.md` | SWE, Terminal-Bench, MRCR | read |
| Real-world tasks | 40-44 | Writing/search/code-agent internal eval | `notes/eval.md`, `notes/claims-and-gaps.md` | R&D coding, developer survey | read |
| Conclusion / limitations | 44-45 | Future direction and gaps | `notes/claims-and-gaps.md` | sparsity, multimodal, data curation | partial |
| References / eval details | 45-58 | Lookup for exact benchmark setup and citations | `notes/eval.md` | appendix, benchmark details | partial |
| Model card | model card 2-8 | Distribution/license/use/model-data facts | `source-bundle.md` | license, use, model data | skim |

## If You Need...

- architecture / long-context efficiency: read pages 6-14, then `notes/architecture.md`.
- pretraining data / model setup: read pages 24-26, then `notes/architecture.md` + `notes/claims-and-gaps.md`.
- post-training OPD: read pages 28-35, then `notes/consolidation.md`.
- GRM / reward signals: read pages 29-30, then `notes/reward-verifier.md`.
- agentic sandbox / rollout infra: read pages 30-36, then `notes/tool-agent-training.md`; consider creating `notes/infra.md` if comparison needs infra detail.
- eval / benchmark claims: read pages 36-44, then `notes/eval.md`.
- claim audit: read `notes/claims-and-gaps.md`, then revisit pages 1, pages 24-35, pages 36-44.
- exact table numbers: read TR Table 1 (28), Table 6 (38), Table 8 (44); do not rely on memory.

## Read Coverage

- Read into notes:
  - architecture: 1, pages 4, pages 6-14, pages 24-26.
  - post-training: 28-36.
  - eval: 27-28, pages 36-44.
  - claims/gaps: 1, pages 24-35, pages 36-45.
- Skimmed only:
  - general infra 14-23.
  - model card 2-8.
- Not read yet:
  - full references.
  - full evaluation details appendix.
- Need revisit before comparison:
  - 33-35 for full-vocab OPD engineering if comparing recipe feasibility.
  - 36-44 for benchmark comparability and internal eval limitations.
  - 14-23 if writing infra/efficiency lens.

## Lookup Tables / Figures

- Figure 1: headline benchmark + FLOPs/KV cache efficiency (1).
- Figure 2: overall architecture (6).
- Figure 3 / 4: CSA / HCA architecture (9, pages 11).
- Table 1: base-model comparison (28).
- Table 2 / 3: reasoning modes and Think Max instruction (29).
- Table 6: post-trained benchmark comparison (38).
- Figure 8 / 9 / 10: formal reasoning and long-context / reasoning effort (40+).
- Table 8: internal R&D coding benchmark (44).
