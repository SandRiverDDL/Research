# Nemotron 3 Source Dossier

```yaml
---
source_id: nemotron-3
source_type: model-tr
org: NVIDIA
release_date: 2026-06-04
priority: S
status: section-notes
openness: open-weights
confidence: medium
lineage: nemotron-3
role: major-release
base_source: nemotron-3-super
---
```

## 一句话

Nemotron 3 是 2026 年最值得关注的 open frontier system source 之一：Super 披露 120B-A12B 的 Hybrid Mamba-Attention MoE、NVFP4 pretraining、LatentMoE、MTP、agentic RL 和 quantization；Ultra 扩到 550B-A55B，并把 post-training 进一步转向 MOPD、specialized teachers、MTP rollout acceleration 和大规模 RL infrastructure。

## 为什么重要

它不是 fully open academic recipe，而是大公司级 open-weight / open-data / open-recipe 系统。对你来说，Nemotron 3 的价值在于理解 2026 open frontier 的系统形态：architecture 为吞吐服务、pretraining 用低精度/长上下文/数据 ordering 控制成本，post-training 用多环境 RL + MOPD + agentic tasks 拉能力，quantization 和 rollout infra 是模型设计的一部分。

## 核心机制 / Takeaways

- Super 的三大 architecture 贡献是 LatentMoE、MTP 和 Hybrid Mamba-Attention interleaving，目标是 accuracy per FLOP 和 accuracy per parameter，而不是只堆 active params。[Super:3-8]
- Super 披露 NVFP4 pretraining、25T token corpus、long-context extension 和 data mixture ordering，是 2026 open recipe 里少见的 pretraining-system detail。[Super:8-18]
- Super post-training 是 SFT -> multi-environment RLVR -> SWE-RL -> RLHF -> MTP healing，强调多环境 agentic RL 和异步 GRPO infrastructure。[Super:18-30]
- Ultra 沿用 Super recipe 并扩到 550B-A55B，新增/强调 MOPD、specialized teachers、MOPD warmup、reasoning efficiency/control 和 RL infrastructure scaling。[Ultra:15-33]
- Quantization 是一等公民：Super / Ultra 都给 FP8/NVFP4 方案，面向 Hopper/Blackwell 部署。[Super:33-37], [Ultra:41-47]

## Source Bundle

- technical report:
  - Ultra: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf
  - Super: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf
- model card:
  - https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16
- code / repo: https://github.com/NVIDIA-NeMo/Nemotron
- local pdf:
  - `/Users/chy/Research/foundation-model-systems/papers/nemotron-3/nemotron-3-ultra.pdf`
  - `/Users/chy/Research/foundation-model-systems/papers/nemotron-3/nemotron-3-super.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: Nemotron 3
- role: major release bundle
- base source: Super is the detailed base recipe; Ultra is larger frontier release using similar recipe with adjustments.
- delta from: Nemotron 3 Nano / Super
- carries over: Hybrid Mamba-Attention MoE, LatentMoE, MTP, RL infrastructure, quantization stack.
- newly disclosed: Ultra MOPD and scaling details; Super detailed architecture/pretraining/post-training recipe.
- not safe to inherit: exact Ultra data/hyperparameter changes unless disclosed in Ultra report.

## Citation Labels

- default source labels:
  - `[Super:18-30]`
  - `[Ultra:20-33]`

## 最大证据缺口

- “open recipes/data” 的实际可复现粒度需要进一步审计 GitHub/HF artifacts。
- Ultra 报告页数多，第一版只读了 architecture/pretraining/post-training/quantization 主线，未完整审计所有 tables/appendix。
- MOPD teacher details、RL environment implementation、asynchronous GRPO staleness controls 仍需深读。

## Lens Hooks

- architecture: Hybrid Mamba-Attention, LatentMoE, MTP。
- pretraining: NVFP4, data mixture ordering, long-context extension, stability diagnostics。
- rl-training: multi-environment RLVR, SWE-RL, RLHF, MOPD。
- infra: async GRPO, rollout acceleration, quantization, Blackwell/Hopper deployment。
- eval: open frontier positioning and agentic benchmark suite。

## 阅读入口

- `section-index.md`
- `notes/architecture-pretraining.md`
- `notes/post-training.md`
- `notes/infra-quantization.md`
