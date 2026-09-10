# Olmo 3 Section Index

```yaml
---
source_id: olmo-3
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/olmo-3/olmo-3.pdf
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
| Abstract / artifact list | 1 | full openness scope | `README.md`, `notes/model-flow.md` | checkpoints, data, code, logs | read |
| TOC | 2 | 118-page navigation | `section-index.md` | Base, Think, Instruct, RL-Zero | read |
| Introduction / Model Flow | 3-6 | source-level design | `notes/model-flow.md` | model flow, Dolma, Dolci | read |
| Costs / flagship results | 6-8 | cost/openness framing | `README.md` | H100, costs, results | skim |
| Base architecture / eval design | 8-13 | base model and dev eval | `notes/eval.md` | OlmoBaseEval | partial |
| Pretraining | 13-20 | Dolma 3 Mix | `notes/pretraining-data.md` | dedup, mixing, PDFs | partial |
| Midtraining | 20-30 | Dolmino and post-trainability | `notes/pretraining-data.md` | source feedback, integration tests | partial |
| Long-context extension | 30-35 | Longmino, science PDFs | `notes/pretraining-data.md` | 65K, long docs | partial |
| Think SFT / DPO / RL | 36-52 | reasoning post-training | `notes/post-training.md` | Dolci Think, Delta Learning, OlmoRL | partial |
| Instruct SFT / DPO / RL | 53-62 | concise/function-calling branch | `notes/post-training.md` | brevity, function calling | partial |
| RL-Zero | 63-65 | RL directly from base | `notes/post-training.md` | RLVR from base | read |
| Appendix training/data/eval | 84-118 | lookup and audit | `notes/claims-and-gaps.md` | decontam, hyperparams, data details | skim |

## If You Need...

- fully-open workflow argument: pages 1, 3-6.
- data recipe: pages 13-35, appendix 87-95.
- post-training recipe: pages 36-65, appendix 105-114.
- eval/decontamination: pages 10-13, 95-101, 114-118.

## Lookup Tables / Figures

- Figure 1: open model flow vs open-weight model flow.
- Figure 2: full Olmo 3 model flow.
- Appendix A.2-A.8: data/eval/hyperparameter details.

