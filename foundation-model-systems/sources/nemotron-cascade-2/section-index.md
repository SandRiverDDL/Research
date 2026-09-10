# Nemotron-Cascade 2 Section Index

```yaml
---
source_id: nemotron-cascade-2
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/nemotron-cascade-2/nemotron-cascade-2.pdf
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
| Abstract / release artifacts | 1 | open model/data claim, high-level contributions | `README.md` | checkpoint, SFT/RL data | read |
| TOC | 2-3 | full structure | `section-index.md` | SFT, Cascade RL, MOPD | read |
| Main results | 4-6 | headline positioning and competition eval | `notes/eval.md` | IMO, IOI, ICPC | read |
| SFT data curation | 6-9 | SFT blend and agentic data | `notes/cascade-rl.md` | math, code, SWE, terminal | partial |
| Cascade RL framework | 10-11 | stage ordering and strict on-policy GRPO | `notes/cascade-rl.md` | GRPO, IF-RL | read |
| IF-RL / multi-domain RL | 11-12 | first RL stages and mixture rationale | `notes/cascade-rl.md` | instruction following, MCQA, tool calling | read |
| MOPD | 13-14 | dense token-level distillation and efficiency | `notes/mopd.md` | reverse KL, teacher, dense advantage | read |
| RLHF / long-context / code / SWE RL | 14-16 | later cascade stages | `notes/cascade-rl.md` | RLHF, long context, SWE | partial |
| Competition sections | 17-24 | IMO/IOI/ICPC procedures | `notes/eval.md` | TIR, human grading | skim |
| Appendix hyperparameters | 25-26 | exact training details | `notes/cascade-rl.md` | rollout size, steps | partial |
| Eval appendix | 30-43 | benchmark settings | `notes/eval.md` | setup, prompts | partial |

## If You Need...

- Cascade RL: pages 10-16 and appendix pages 25-26.
- MOPD: pages 13-14 first, then appendix hyperparameters.
- eval credibility: pages 4-6, 17-24, and appendix eval setups.
- data openness: page 1 and HF dataset pages.

## Lookup Tables / Figures

- Figure 2: Cascade RL stage order.
- Table 3: MOPD vs RLHF efficiency.
- Table 8/9: Cascade RL hyperparameters.
