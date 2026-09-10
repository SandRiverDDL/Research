# GLM-5.1 Release Delta

```yaml
---
source_id: glm-5.1
section_type: stage-note
stage: release-delta
depth: light
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- GLM-5.1 的公开材料重点是 release positioning：更强 coding、long-horizon task、tool-use / agentic engineering，而不是完整训练流程。
- 它最适合作为 GLM-5 lineage 的版本边界：GLM-5 是 full TR anchor，GLM-5.2 是 1M context / long-horizon coding release delta，GLM-5.1 位于两者之间。

## Why It Matters

如果后续做 GLM family comparison，GLM-5.1 可以帮助判断哪些能力是 GLM-5 TR 已经有的，哪些可能是 5.1/5.2 release 才强调的。但它本身不提供足够细节支撑 method lens。

## Mechanism Sketch

1. 继承 GLM-5 的 architecture / post-training / slime 基础。
2. Release 叙事强调 coding-agent 和 long-horizon engineering。
3. 具体数据、RL、OPD、eval scaffold 未充分披露。

## Details / Evidence

- 官方 repo / blog 将 GLM-5.1 放在 GLM-5 family 下，和 GLM-5.2 共同服务 agentic engineering release line。[blog-glm51, github-readme]

## Gaps / Open Questions

- 没有独立 PDF TR 或完整 training recipe。
- 是否引入了新的 RL algorithm、data mixture、long-context architecture 或 OPD 流程，公开材料不足以判断。

## Lookup-only

- 具体模型下载、部署命令、benchmark entries 回查官方 blog / repo。

## Evidence Anchors

- `[blog-glm51]`: release positioning.
- `[github-readme]`: family placement and usage.
