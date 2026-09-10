# GLM-5.1 Source Dossier

```yaml
---
source_id: glm-5.1
source_type: blog-bundle
org: Z.ai
release_date: 2026-05-19
priority: A
status: section-notes
openness: open-weights
confidence: medium
lineage: glm-5
role: release-delta
base_source: glm-5
---
```

## 一句话

GLM-5.1 目前更像 GLM-5 到 GLM-5.2 之间的 agentic engineering release delta：重点是 coding、long-horizon、long-context 和 tool-use 能力增强，而不是公开新的完整训练 recipe。

## 为什么重要

它适合作为 GLM-5 lineage 的中间节点：如果后续比较 GLM-5.2 的 1M context / critic-based PPO / anti-hacking，就需要知道 GLM-5.1 已经把主线从“GLM-5 TR”推进到更强 coding agent release。

## 核心设计 / Takeaways

- 官方材料将 GLM-5.1 定位为面向 agentic engineering 的下一代 flagship，强调 coding、reasoning、long-horizon task 和 tool calling。
- 由于没有找到独立完整 TR，GLM-5.1 的 pretraining、post-training、RL data、reward 和 infra 细节默认继承 GLM-5，只记录明确 release delta。
- 对项目来说，它不是新的 anchor；它是 GLM-5.2 前的版本边界，防止把 GLM-5.2 的增量误归因给 GLM-5 TR。

## Source Bundle

- release blog: https://z.ai/blog/glm-5.1
- code / repo: https://github.com/zai-org/GLM-5
- lineage TR: https://arxiv.org/abs/2602.15763
- local pdf: none for GLM-5.1
- last checked: 2026-06-23

## Lineage / Delta

- lineage: GLM-5
- role: release delta after `glm-5`, before `glm-5.2`.
- base source: `sources/glm-5/`
- next source: `sources/glm-5.2/`

## Citation Labels

- non-TR source labels:
  - `[blog-glm51]`
  - `[github-readme]`
  - `[glm5-tr]`

## 最大证据缺口

- 没有独立 TR；不能把 GLM-5.1 当作完整 recipe source。
- 具体 RL algorithm、data mixture、eval scaffold、long-horizon environment 和 distillation/OPD 细节未公开。

## Lens Hooks

- release-delta: GLM-5 -> GLM-5.1 -> GLM-5.2 lineage tracking。
- rl-training: long-horizon agentic capability claims need GLM-5 / GLM-5.2 evidence.
- eval: coding agent release rhetoric and external benchmark comparability.

## 阅读入口

- `section-index.md`: release materials 回读地图。
- `notes/release-delta.md`: 版本定位和证据边界。
- `notes/claims-and-gaps.md`: comparison 前先读。
