# Kimi K2.7 Code Release Delta

```yaml
---
source_id: kimi-k2.6
section_type: stage-note
stage: release-delta
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- K2.7 Code 是 Kimi K2 当前 coding-agent release，官方明确强调 4,000+ tool calls 与 12+ hours continuous execution 的 long-horizon capability。[k27-announcement]
- 相比 K2.6，官方声称平均减少约 30% thinking-token usage，把 reasoning efficiency 作为独立优化目标。[k27-announcement]
- Release 支持 multimodal tool use，可处理 video 并通过 custom tools 做 temporal analysis 与 clip extraction。[k27-announcement]
- HighSpeed endpoint 声称保持同模型能力并提升 decode speed；它属于 serving delta，不是新 training recipe。[k27-announcement]

## Why It Matters

K2.7 Code 的 current-practice 信号是：long-horizon coding agent 不再只追求成功率，还同时优化 tool-call horizon、thinking-token cost 与 multimodal tool interface。但目前材料仍是 release/eval disclosure，不能替代 K2.5 TR。

## Mechanism Sketch

1. 在 coding-agent scaffold 中执行超长 tool-call sequence。
2. 对简单任务减少不必要 deliberation，降低 thinking-token usage。
3. 通过 tools 处理 image/video inputs。
4. 使用锁定 sampling parameters 提高 API output consistency。[k27-announcement]

## Details / Evidence

- 官方列出 Kimi Code Bench V2、Program Bench、MLS Bench Lite、Kimi Claw、MCP Atlas 与 MCP Mark Verified；这些是 release positioning，且部分 benchmark/scaffold 并未完整公开。[k27-announcement]
- Temperature、top-p、n 与 penalties 在 endpoint 中固定；这有利于产品一致性，但限制用户做 sampling-level ablation。[k27-announcement]
- Weights/code link 已给出，但公告没有描述 SFT/RL stages、reward、trajectory filtering 或 K2.5 Agent Swarm/PARL 是否延续。[k27-announcement, k27-hf]

## Gaps / Open Questions

- 4,000+ tool calls 与 12+ hours 是测试能力描述，不是训练 trajectory distribution 的证据。
- Thinking-token 降低来自 length reward、distillation、routing 还是 decoding control，未公开。
- K2.7 是否保留 K2.5 的 joint text-vision RL、DEP、Agent Swarm/PARL，不能自动继承。
- HighSpeed 的精度、quantization 与 serving topology 未披露。

## Lookup-only

- Headline benchmark values、速度和固定 sampling parameters：`[k27-announcement]`。

## Evidence Anchors

- `[k27-announcement]`: https://forum.moonshot.ai/t/441
- `[k27-hf]`: https://huggingface.co/moonshotai/Kimi-K2.7-Code
- `[k25-tr]`: K2.5 lineage method anchor。
