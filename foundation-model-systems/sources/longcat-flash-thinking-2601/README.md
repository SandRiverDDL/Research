# LongCat-Flash-Thinking-2601 Source Dossier

```yaml
---
source_id: longcat-flash-thinking-2601
source_type: model-tr
org: Meituan LongCat Team
release_date: 2026-02-01
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: longcat-flash-thinking
role: full-tr
base_source: longcat-flash-thinking
---
```

## 一句话

LongCat-Flash-Thinking-2601 是 LongCat-Flash-Thinking 的更新版完整 TR，重点不是普通 reasoning RL，而是 agentic reasoning 的环境规模化：structured agentic midtraining、10,000+ / 32,000 级环境、DORA 异步 RL、多域环境训练、噪声鲁棒训练和 Heavy Thinking。[1-4, 9-16]

## 为什么重要

它是目前项目里最适合研究 agentic RL 环境构建与 rollout infra 的 source。相比 Qwen3 的 mode fusion 或 Step 的效率型 agent model，LongCat 把“环境如何生成、验证、扩展、带噪训练、并在大规模异步系统里跑起来”写得更像系统论文。

## 核心机制 / Takeaways

- 2601 是 LongCat-Flash-Thinking 的 upgraded version；预训练大体继承 LongCat-Flash-Chat recipe，但在 midtraining 加入 agentic trajectories，为 RL exploration 做初始化。[1-3]
- 环境扩展是核心：从 domain specification 自动生成 tools、database schema、tool dependency graph，再按 verifiability-preserving 规则扩展环境。[5-6]
- DORA 被扩展到 multi-turn agentic RL：producer-consumer、virtual rollout groups、streaming async pipeline、multi-version models、PD disaggregation 和 CPU KV-cache swapping。[9-11]
- Multi-domain environment training 用 oversampling / pass-rate-based budget allocation 处理 domain imbalance，同时保持异步训练吞吐。[14]
- Robust RL 显式注入 instruction noise 和 tool noise，用 curriculum 逐步加难，目标是缩小 perfect vs imperfect environments 的性能差。[15-16]
- Heavy Thinking 通过并行 trajectory exploration + summary/refinement 做 test-time scaling。[16-17]

## Source Bundle

- technical report: https://arxiv.org/abs/2601.16725
- tech-report-pdf: https://arxiv.org/pdf/2601.16725
- repo: https://github.com/meituan-longcat/LongCat-Flash-Thinking-2601
- model: https://huggingface.co/meituan-longcat/LongCat-Flash-Thinking-2601
- model page: https://www.longcatai.org/models/flash-thinking.html
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/longcat-flash-thinking-2601/longcat-flash-thinking-2601.pdf`
- last checked: 2026-06-23

## Version Check

- latest full TR found for LongCat-Flash-Thinking line: `LongCat-Flash-Thinking-2601 Technical Report` arXiv v2 dated 2026-02-01.
- older source: `LongCat-Flash-Thinking Technical Report` arXiv 2509.18883.
- LongCat site also lists newer/lighter LongCat-Flash-Lite style releases, but this pass did not find a newer full agentic reasoning TR replacing 2601.

## Citation Labels

- default TR pages: page-only anchors.
- non-TR labels: `[repo]`, `[hf]`, `[model-page]`.

## 最大证据缺口

- 具体 environment/task generation prompts、reward/verifier、domain sampling weights 和 noise schedule 未完全公开。
- DORA 的实现是否开源、与论文描述的一致性需要 repo / system audit。

## Lens Hooks

- agentic-rl: environment scaling, multi-domain environment training, robust noisy environments.
- infra: DORA asynchronous rollout, PD disaggregation, KV-cache swapping.
- test-time-scaling: Heavy Thinking.
- consolidation: domain-specialized expert training and fusion.

## 阅读入口

- `notes/environment-scaling.md`: agentic data / environment construction。
- `notes/rl-infra-dora.md`: DORA 和多域 agentic RL。
- `notes/robust-heavy-thinking.md`: noisy environment training 和 Heavy Thinking。

