# Step 3.5 Flash Section Index

```yaml
---
source_id: step-3.5-flash
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/step-3.5-flash/step-3.5-flash.pdf
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
| Abstract / intro | 1, 4-5 | positioning and core recipe | `README.md` | 11B active, MIS-PO, MTP | read |
| TOC | 2-3 | navigation | `section-index.md` | architecture, infra, post-training | read |
| Architecture | 5-8 | latency-first design | `notes/architecture-inference.md` | SWA/full, GQA-8, MTP, MoE | read |
| Infra / monitoring | 9-10 | training observability | `notes/claims-and-gaps.md` | metrics server, stability | skim |
| Pretraining / midtraining | 10-15 | Muon stability and data curriculum | `notes/architecture-inference.md` | loss spike, expert collapse | partial |
| Post-training overview | 15-16 | expert models and self-distillation | `notes/post-training-rl.md` | SFT, RL experts, distillation | read |
| MIS-PO | 16-17 | scalable off-policy RL | `notes/post-training-rl.md` | binary masks, trust region | read |
| Agent data / infra | 19-21 | code/search/tool agents | `notes/post-training-rl.md` | XML tool template, Kubernetes | partial |
| Eval | 21-24 | eval settings and PaCoRe | `notes/eval-release-delta.md` | PaCoRe, agent benchmarks | read |
| Appendix post-training | 35-39 | SFT/RL ablations | `notes/post-training-rl.md` | details, tool-integrated reasoning | skim |
| Eval appendix | 40-67 | benchmark protocols | `notes/eval-release-delta.md` | prompts, internal eval | skim |

## If You Need...

- architecture/inference co-design: pages 5-8 and appendix 27-30.
- MIS-PO: pages 16-17 and appendix 36-38.
- agent infrastructure: page 21.
- eval setting: pages 21-24 and appendix 40-67.

## Lookup Tables / Figures

- Figure 2: architecture.
- Table 1: SWA/full attention ablation.
- Figure 5: MIS-PO vs PPO training dynamics.
- Table 5: broad post-training eval.

