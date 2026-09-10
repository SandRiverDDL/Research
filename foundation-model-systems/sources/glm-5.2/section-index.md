# GLM-5.2 Section Index

```yaml
---
source_id: glm-5.2
index_status: working
source_files:
  - https://z.ai/blog/glm-5.2
  - https://huggingface.co/blog/zai-org/glm-52-blog
  - https://huggingface.co/zai-org/GLM-5.2
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: false
  tables_extracted: partial
  figures_checked: none
---
```

## 用法

这是 GLM-5.2 release bundle 的导航层，不是 summary。它没有专门 PDF 页码；后续引用使用语义 source label。需要 GLM-5 lineage 时再回读 GLM-5 TR。

## Source Files

- GLM-5.2 blog: https://z.ai/blog/glm-5.2
- HF blog mirror: https://huggingface.co/blog/zai-org/glm-52-blog
- HF model card: https://huggingface.co/zai-org/GLM-5.2
- GitHub README: https://github.com/zai-org/GLM-5
- GLM-5 TR: https://arxiv.org/abs/2602.15763

## Reading Map

| Section | Source | Why Read | Related Notes | Keywords | Status |
|---|---|---|---|---|---|
| Introduction / positioning | `blog-glm-52`, `hf-model-card` | 确定 GLM-5.2 的目标：long-horizon tasks、1M context、coding/agentic work、open weights | `README.md`, `notes/claims-and-gaps.md` | long-horizon, 1M context, open weights | read |
| Benchmark overview | `blog-glm-52`, `hf-model-card` | 判断 release claim 想证明哪些能力 | `notes/eval.md` | FrontierSWE, PostTrainBench, Terminal-Bench | read |
| Effort control | `blog-glm-52` | 理解 High/Max effort 作为 user-facing compute allocation | `notes/eval.md`, `notes/claims-and-gaps.md` | effort, token budget | read |
| Architecture for 1M context | `blog-glm-52` | 1M context 的核心结构增量 | `notes/architecture.md` | DSA, IndexShare, 128K mid-training | read |
| MTP with IndexShare/KVShare | `blog-glm-52` | speculative decoding 与 acceptance length 设计 | `notes/architecture.md` | MTP, KVShare, TV loss | read |
| Efficient serving 1M context | `blog-glm-52` | 长上下文 serving bottleneck 和 inference engine optimization | `notes/architecture.md` | KV-cache, LayerSplit, kernels, CPU scheduling | read |
| slime for Agentic RL | `blog-glm-52` | rollout/training/inference 统一 infra；parallel OPD 合并 experts | `notes/rl-training.md` | slime, OPD, rollout, expert models | read |
| RL for long-horizon tasks | `blog-glm-52` | critic-based PPO、compacted trajectories、token-level loss | `notes/rl-training.md` | PPO, critic, compaction | read |
| Anti-hack in coding agents | `blog-glm-52` | reward hacking 防护机制，训练和 eval 都相关 | `notes/rl-training.md`, `notes/eval.md` | hack detection, LLM judge, tool calls | read |
| Full benchmark table | `blog-glm-52`, `hf-model-card` | exact score lookup；主线只保留 claim-critical 数字 | `notes/eval.md` | HLE, SWE, MCP, Tool-Decathlon | partial |
| Evaluation footnotes | `blog-glm-52` | suite-specific sampling/scaffold/context/judge settings | `notes/eval.md` | temperature, judge, timeout, context | read |
| GLM-5 TR | `glm5-tr` | lineage：DSA、slime、OPD、GLM-5 training pipeline | future comparison only | GLM-5, DSA, asynchronous RL | skim |

## If You Need...

- architecture / model structure: read `notes/architecture.md`, then GLM-5.2 blog architecture section; only read GLM-5 TR if you need lineage details for DSA or base MoE.
- data pipeline / mixture: GLM-5.2 does not disclose enough; use `notes/claims-and-gaps.md` and avoid strong conclusions.
- post-training / RL: read `notes/rl-training.md`, then GLM-5.2 blog sections on slime, critic-based PPO, compaction, anti-hack.
- eval / benchmark claims: read `notes/eval.md`, then benchmark table and footnotes in GLM-5.2 blog.
- infra / efficiency: read `notes/architecture.md`; if writing infra lens, revisit 1M serving section and possibly GLM-5 TR/slime docs.
- safety: not meaningfully disclosed except anti-hacking for coding agents.
- claim audit: read `notes/claims-and-gaps.md`.

## Read Coverage

- Read into notes:
  - GLM-5.2 blog introduction, architecture, MTP, serving, slime, RL, anti-hack, benchmark table, footnotes.
  - HF model card benchmark / usage mirror.
  - GitHub README release overview and model download table.
- Skimmed only:
  - GLM-5 TR abstract/introduction/methods as lineage signal.
  - IndexShare paper only identified, not read deeply.
- Not read yet:
  - GLM-5 full TR sections on DSA, slime, OPD, pretraining pipeline.
  - IndexShare / IndexCache paper details.
  - Third-party evaluations beyond official linked benchmarks.
- Need revisit before comparison:
  - Eval footnotes for scaffold and context-length comparability.
  - GLM-5 TR if comparing GLM family with DeepSeek/MAI at architecture or RL infra level.
  - External benchmark pages if judging whether GLM-5.2’s long-horizon claims are independently credible.

## Lookup Tables / Figures

- Full Benchmark Table in GLM-5.2 blog / HF model card.
- MTP ablation: acceptance length baseline to final +20%.
- Eval footnotes: per-benchmark sampling, context length, judge/scaffold, timeout, max output tokens.
