# GLM-5 Eval

```yaml
---
source_id: glm-5
section_type: stage-note
stage: eval
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- GLM-5 eval 的主线是 agentic engineering：coding、SWE、terminal、search、long-context management 和 long-term operational benchmark，而不是只看 reasoning leaderboard。[19-23]
- Search agent eval 特别强调 judge choice 和 context management，说明 long-horizon agent 的分数高度依赖 scaffold / judge / context compression 策略。[19]
- Context management 被当成模型系统的一部分：keep-recent-k、Discard-all 和 hierarchical context management 会明显影响 BrowseComp 这类任务。[19]

## Why It Matters

GLM-5 的 eval 给了一个重要提醒：agentic model 的能力不是纯模型参数，常常是 model + tools + context policy + judge + timeout 的组合。后续比较 GLM/Kimi/MiniMax/Step/LongCat 时，要把 scaffold 和上下文策略作为一等证据。

## Mechanism Sketch

1. 对 search agent，标准化 judge prompt 和 judge model，以减少 open-source judge bias。
2. 对超长工具轨迹，用 keep-recent-k 折叠旧 observation，必要时再 discard all tool history。
3. 对 coding / SWE / terminal，强调可执行环境和 test-based reward / verification。
4. 对 long-term operation，用 Vending Bench 2 这类多步模拟任务验证持续规划能力。

## Details / Evidence

- Search eval 中，GLM-5 使用官方 OpenAI eval prompt 和 o3-mini judge，作者声称该配置与人工标注 ground truth 更一致。[19]
- keep-recent-k 只折叠最近 k 轮之前的 tool observations，而保留 trajectory skeleton；GLM-5 报告 k=5 稳定有效。[19]
- Hierarchical Context Management 把 keep-recent 与 Discard-all 结合，超过阈值后清空 tool-call history 再继续 keep-recent。[19]

## Gaps / Open Questions

- 多个 agentic benchmark 的 external tool、网络权限、timeout、sampling、judge 版本和 prompt 不一定可复现。
- 分数本身只适合作为 claim support，不应替代对 environment construction 和 context policy 的分析。

## Lookup-only

- 具体 benchmark 表格、分数和 baseline 回查 `[20-23]`。
- Search context management 的曲线和参数回查 `[19]`。

## Evidence Anchors

- 19: search judge and context management.
- 20-23: benchmark result tables and eval coverage.
