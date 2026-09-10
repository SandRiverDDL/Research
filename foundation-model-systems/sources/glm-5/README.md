# GLM-5 Source Dossier

```yaml
---
source_id: glm-5
source_type: model-tr
org: Z.ai
release_date: 2026-02-19
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: glm-5
role: full-tr
base_source: glm-4.7
---
```

## 一句话

GLM-5 是 GLM-5 lineage 的完整 TR anchor：它把 744B/40B MoE、DSA 长上下文降本、28.5T pretraining、slime 异步 RL、agentic coding/search 环境和 OPD-like cross-stage distillation 连成一条“面向 agentic engineering 的模型系统”主线。[1-4, 12-18]

## 为什么重要

对后训练岗位，GLM-5 最值得学的是长轨迹 agentic RL 的系统化处理：异步 rollout、TITO、防 off-policy、可执行 SWE/terminal/search 环境、DP-aware routing 和 slime rollout infra。对未来基模方向，它展示了 architecture、data、infra、post-training 之间如何协同，而不是把 RL 当作单独算法模块。

## 核心设计 / Takeaways

- Architecture 侧从 GLM-4.5 的 355B/32B active 扩到 744B/40B active，同时用 DSA/MLA/MTP 抵消长上下文推理成本。[4-6]
- Pretraining 不是只加 token：27T/28.5T corpus、code/math/science/web 质量筛选、long-document chunk aggregation、repo-level code、issue/PR 数据和 4K->200K midtraining curriculum 是一组服务 agentic task 的数据工程。[8-9]
- Post-training 流程是 SFT -> Reasoning RL -> Agentic RL -> General RL -> On-Policy Cross-Stage Distillation；核心是多阶段能力不互相遗忘，而不是单一 RL 算法。[10-14]
- Agentic RL 的关键不只是 reward，而是 fully asynchronous + decoupled training/inference/rollout：长轨迹 rollout 会让同步 RL GPU 空转，GLM-5 用 Multi-Task Rollout Orchestrator 和 slime 把任务服务化。[12-17]
- 训练稳定性靠多层工程约束：DSA deterministic top-k、freeze indexer、TITO、direct double-sided IS、丢弃 stale/noisy samples、DP-aware routing。[12, 16-17]
- Eval 明显围绕 agentic engineering 展开：SWE、terminal、search、Vending Bench、context management，而不是只展示数学/知识分数。[19-23]

## Source Bundle

- technical report: https://arxiv.org/abs/2602.15763
- tech-report-pdf: https://arxiv.org/pdf/2602.15763
- release blog: https://z.ai/blog/glm-5
- code / repo: https://github.com/zai-org/GLM-5
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/glm-5/glm-5.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: GLM-5
- role: full TR anchor for GLM-5 / GLM-5.1 / GLM-5.2 lineage.
- downstream deltas:
  - `glm-5.1`: release delta for longer-horizon agentic engineering.
  - `glm-5.2`: release delta for 1M context and stronger long-horizon coding.

## Citation Labels

- default TR pages: page-only anchors like `[12-17]`
- non-TR labels:
  - `[blog-glm5]`
  - `[github-readme]`

## 最大证据缺口

- Agentic RL data、reward details、task mixture、OPD / cross-stage distillation proportions没有完全公开。
- slime 作为 infra 披露较多，但和训练 loss / policy lag / optimizer reset 的 ablation 仍不完整。
- DSA 的 deployment value 明确，但 sparse attention 和 indexer 在 RL 中的稳定边界需要和 DeepSeek/MiniMax/Kimi 的 sparse/long-context方案横向比较。

## Lens Hooks

- architecture: DSA、MLA、MTP、MuON Split、744B/40B MoE。
- pretraining-data: 28.5T corpus、repo-level code、long-context midtraining。
- rl-training: asynchronous agentic RL、TITO、direct double-sided IS、stale sample filtering。
- infra: slime、rollout serving、PD disaggregation、DP-aware routing。
- eval: long-horizon SWE/search/terminal context management。

## 阅读入口

- `section-index.md`: 40 页 TR 的回读地图。
- `notes/architecture-pretraining.md`: MoE/DSA/MTP 和 pretraining/midtraining 数据。
- `notes/agentic-rl.md`: slime、异步 RL、TITO、off-policy 稳定控制和环境构建。
- `notes/eval.md`: agentic engineering eval 和 context management。
- `notes/claims-and-gaps.md`: comparison 前的证据边界。
