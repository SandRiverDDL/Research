# Arcee Trinity Large Section Index

```yaml
---
source_id: arcee-trinity-large
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/arcee-trinity-large/arcee-trinity-large.pdf
coverage:
  toc_index: false
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## Reading Map

| Section | Pages | Why Read | Related Notes | Keywords | Status |
|---|---:|---|---|---|---|
| Abstract / intro | 1-2 | positioning and scale | `README.md` | 400B, 13B active, Muon | read |
| Tokenizer | 2-4 | numeric/multilingual tokenization | `notes/architecture-stability.md` | digit chunking, 200k BPE | skim |
| Attention / QK-Norm | 5-6 | stability and long context | `notes/architecture-stability.md` | local/global, gated attention | read |
| MoE / SMEBU | 6-8 | expert routing stability | `notes/architecture-stability.md` | sigmoid routing, SMEBU | read |
| Pretraining data | 9-11 | 17T data and synthetic mix | `notes/pretraining-data.md` | DatologyAI, phases, synthetic | read |
| Training / Muon | 11-14 | optimizer and stability | `notes/pretraining-data.md` | zero spikes, batch, Muon | partial |
| Eval / Preview | 14-15 | model states and results | `notes/claims-and-gaps.md` | Base, Preview | skim |
| Appendix | 23-29 | contributors and extra details | `notes/claims-and-gaps.md` | tables, hyperparams | skim |

## If You Need...

- SMEBU: page 7.
- Muon/QK-Norm stability: page 5 and training section pages 11-14.
- data composition: pages 9-11.
- post-training: this TR has little detail; check later Trinity-Large-Thinking sources separately.

## Lookup Tables / Figures

- Figure 1: training loss graph.
- Figure 2: architecture.
- SMEBU equations: pages 7-8.

