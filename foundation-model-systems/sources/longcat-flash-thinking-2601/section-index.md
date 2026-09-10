# LongCat-Flash-Thinking-2601 Section Index

```yaml
---
source_id: longcat-flash-thinking-2601
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/longcat-flash-thinking-2601/longcat-flash-thinking-2601.pdf
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
| Abstract / intro | 1-3 | contribution and version role | `README.md` | upgraded version, DORA, Heavy Thinking | read |
| Pre-training / midtraining | 3-4 | agentic trajectory initialization | `notes/environment-scaling.md` | text-driven, environment-grounded synthesis | read |
| Environment construction | 5-8 | executable domain graphs and scaling | `notes/environment-scaling.md` | tools, database, dependency graph | read |
| DORA infra | 9-11 | asynchronous multi-turn rollout system | `notes/rl-infra-dora.md` | virtual rollout group, PD disaggregation | read |
| RL training strategy | 11-14 | curriculum, dynamic budget, GSPO | `notes/rl-infra-dora.md` | budget allocation, self-verification | partial |
| Multi-domain environment training | 14-15 | domain balance and oversampling | `notes/rl-infra-dora.md` | pass-rate, domains, convergence | read |
| Robust noisy training | 15-16 | real-world imperfections | `notes/robust-heavy-thinking.md` | instruction noise, tool noise | read |
| Heavy Thinking | 16-17 | test-time scaling | `notes/robust-heavy-thinking.md` | parallel reasoning, summary | read |
| Eval / benchmark claims | 17-19, 25-27 | claim support | `notes/claims-and-gaps.md` | BrowseComp, τ2, VitaBench | skim |
| Appendix | 20-27 | architecture/data/eval lookup | `notes/claims-and-gaps.md` | architecture, ablations | skim |

## If You Need...

- environment scaling: pages 3-8.
- DORA / rollout infra: pages 9-11.
- noisy robust training: pages 15-16.
- Heavy Thinking: pages 16-17.

## Lookup Tables / Figures

- Figure 3/4: automated environment construction and expansion.
- Figure 5/6: DORA workflow and PD disaggregation.
- Figure 10: Heavy Thinking mode.
- Table 1: noise training ablation.

