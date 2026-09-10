# Qwen3-Coder-Next Evaluation

```yaml
---
source_id: qwen3-coder-next
section_type: eval
stage: eval
substage: agentic-coding
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Eval 主线是 active-parameter efficiency：80B total / 3B active 是否能在 SWE-Bench、Terminal-Bench 等 agentic coding benchmarks 上接近大模型。[1-2, 11-13]
- 它不仅看 static coding tasks，还看 agent-centric benchmarks，和训练中的 executable environments 对齐。[1, 11-13]
- 具体分数不是第一价值；更重要的是它把 small active footprint coding model 放进 real developer workflow / local deployment 语境。

## Gaps / Open Questions

- Agentic eval scaffold、tool access、timeout、context 和 judge 设置需要细审。
- 和 closed frontier / Chinese open-weight models 的比较是否 same scaffold 不清楚。
- 需要结合外部 leaderboards 验证 vendor-reported claims。

## Lookup-only

- SWE-Bench / Terminal-Bench / Aider / other coding benchmark numbers in report/model card。[11-13]

## Evidence Anchors

- 1-2: headline eval positioning。
- 11-13: experiment sections。
