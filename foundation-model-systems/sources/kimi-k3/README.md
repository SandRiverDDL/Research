# Kimi K3 Source Dossier

```yaml
---
source_id: kimi-k3
source_type: model-tr
org: Moonshot AI
release_date: 2026-07-16
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: kimi-k3
role: major-release
base_source: kimi-k2.5
---
```

## 一句话

Kimi K3 是 2026-07 当前综合能力最强、并与最强 proprietary models 进入同一竞争带的 open-weight model；“断档第一”可作为 open-weight 综合能力与 agentic/coding positioning，但不应扩写成所有能力都第一、fully open，或低成本易部署。

## 为什么重要

- K3 把 open-weight pretraining scale 从 K2 的约 1T / 32.6B active 推到 2.78T / 104.2B active，同时把 native multimodality、1M context、long-horizon agentic RL 和 deployment-aware post-training 放进同一个系统。[2, 10-14]
- 它不是只有 model card：47 页 full technical report 披露 architecture、pretraining、SFT/RL/MOPD、agent environments、training/serving infra、eval 与部分 ablation，足以作为当前 Kimi lineage 的独立 major source。
- 独立评测支持“open-weight 第一”：Artificial Analysis Intelligence Index 为 57，领先 GLM-5.2 的 51；Vals Index 74.7 对 65.0；WebDev Arena 总榜第一。与此同时 K3 仍落后 Claude Fable 5 / GPT-5.6 Sol 的总体 frontier，cyber end-to-end 也明显落后最强 closed models。[31-32; aa-k3; arena-text; aisi-cyber]
- 权重已于 2026-07-27 实际发布，而非仅承诺发布；Hugging Face repository 非 gated，约 2.78T parameters、约 1.56 TB storage。[hf-model]

## 核心机制 / Takeaways

- **三轴 information-flow scaling**：sequence 用 3:1 KDA / Gated MLA hybrid，depth 用 Attention Residuals，width 用 Stable LatentMoE；三者共同服务 1M context、93-layer、896-expert sparse model。[3-9]
- **Stable LatentMoE**：16/896 routed experts + 2 shared experts；RMSNorm、SiTU-GLU 与 Quantile Balancing 分别控制 latent routed path 的 scale、activation outlier 和极端稀疏下的 load balance。[6-9]
- **native multimodal pretraining**：MoonViT-V2 从零开始与 LLM joint next-token training，不做 post-hoc alignment；官方 ablation 显示其 gradient 更稳，并匹配 SigLIP initialization 的 vision eval。[9-12]
- **post-training pipeline**：SFT cold start -> 三 domain × 三 effort 的九个 RL experts -> Multi-Teacher On-Policy Distillation；QAT 从 SFT 贯穿 RL，rollout 和 training 使用相同 MXFP4/MXFP8 scheme。[12-14]
- **agentic data/environment 是能力主轴**：multi-harness white-box RL、knowledge-graph-guided task synthesis、verifiable professional work、kernel optimization、persistent personal-assistant worlds、AET 与 web development 构成训练环境，而不是只靠静态 reasoning samples。[14-16]
- **systems 是方法的一部分**：KDA Context Parallelism、MoonEP perfect balance、partial rollouts + external KV cache、resumable microVM sandboxes、hybrid KDA/MLA prefix cache，使 3T pretraining 与 million-token RL/serving 可执行。[17-25]

## Source Bundle

- technical report: https://arxiv.org/abs/2607.24653
- official repository: https://github.com/MoonshotAI/Kimi-K3
- model card / weights: https://huggingface.co/moonshotai/Kimi-K3
- tech blog: https://www.kimi.com/blog/kimi-k3
- license: https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE
- external eval:
  - https://artificialanalysis.ai/models/kimi-k3/
  - https://arena.ai/leaderboard/text?q=kimi
  - https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities
- local pdf: `../../papers/kimi-k3/kimi-k3.pdf`
- last checked: 2026-07-29

## Lineage / Delta

- lineage: Kimi K3；architecture-level 换代，不作为 K2.6/K2.7 Code 的小 release delta。
- base source: `sources/kimi-k2.5/` 是上一份完整 Kimi TR anchor。
- newly disclosed: KDA/AttnRes/Stable LatentMoE、2.8T scale、native-from-scratch vision、1M context pretraining/RL infra、nine-expert MOPD、QAT-through-RL。
- not safe to inherit: K2.5 的具体 data mixture、Agent Swarm recipe、RL objective 细节或 benchmark setting，除非 K3 report 明确重述。

## Citation Labels

- default TR pages: `[3-9]`
- non-TR source labels:
  - `[hf-model]`: weights/model metadata。
  - `[k3-license]`: custom license。
  - `[aa-k3]`: Artificial Analysis model page / independent index。
  - `[arena-text]`: Arena leaderboard。
  - `[aisi-cyber]`: UK AISI / US CAISI cyber assessment。

## 最大证据缺口

- 没有公开 total pretraining tokens、FLOPs、训练集比例、data cutoff、完整 decontamination audit、RL prompt/environment mixture、reward implementation 或主要训练预算。
- `2.5× scaling efficiency` 是 architecture + data + recipe 的 aggregate claim，报告没有提供足够 ablation 将收益归因到 KDA、AttnRes、LatentMoE、数据或 optimizer。
- 官方主表只放一个 open-weight baseline（GLM-5.2），并混用 Kimi Code、Claude Code、Codex、不同 tool/context policies；“断档第一”需要以独立综合评测为主，不能只读 Table 2。
- 权重开放但 data、training code/config、RL environments 和 full recipe 未开放；custom license 对大规模 MaaS commercial use 和超大产品 branding 有限制，因此准确称呼是 `open-weight`，不是 `fully-open`。

## Lens Hooks

- architecture: hybrid linear/global attention + depth attention + extreme sparse LatentMoE。
- data-pipeline: native multimodal pretraining、programmatic visual data、KG-guided agent task synthesis。
- training-recipe: scaling-law retuning、progressive 1M context、QAT-through-post-training。
- rl-training: partial rollout、effort curriculum、agentic GRM、nine-expert MOPD。
- eval: model-vs-system comparability、third-party support、open-weight frontier gap。
- infra: KCP、MoonEP、resumable sandboxes、hybrid cache management。

## 阅读入口

1. `notes/claims-and-gaps.md`：先看“断档第一”与 openness 的审计结论。
2. `notes/post-training.md` 与 `notes/agentic-environments.md`：最值得迁移的训练系统。
3. `notes/architecture.md`：K3 与 K2 的 architecture-level 变化。
4. `notes/infra.md`：3T + 1M agentic workload 如何落地。
5. `notes/eval.md`：评测设置、独立验证与不可比项。
6. `section-index.md`：按页回原文。
