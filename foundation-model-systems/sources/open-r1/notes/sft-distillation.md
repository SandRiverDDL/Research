# Open-R1 SFT Distillation

```yaml
---
source_id: open-r1
section_type: sft-distillation
stage: post-training
substage: sft-distillation
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Open-R1 最成熟的 milestone 是使用公开 verified-trace corpus 复现 R1-style distilled models。[repo]
- Mixture-of-Thoughts 包含约 350K 条 math、code、science verified traces，并提供配套 OpenR1-Distill-7B SFT recipe。[repo, hf-org]
- 更早的 OpenR1-Math 与 CodeForces-CoTs 把 domain trace generation、verification 和 SFT 拆成可独立替换的环节。[repo]

## Why It Matters

这是判断某个 RL 增益是否超过强 verified-trace SFT baseline 的实用入口，也使 teacher generation、data filtering 与 long-sequence cost 更透明。

## Mechanism Sketch

1. 从 DeepSeek-R1 或 distilled R1 model 采样多条 traces。
2. 验证最终 math/code outcome。
3. 构建 domain mixture，并保留 reasoning traces。
4. 使用较长 sequence length SFT 对应 Qwen base。
5. 在同一 harness 下与 DeepSeek 发布的 distill checkpoint 比较。[repo]

## Details / Evidence

- Repository 给出具体 Accelerate/DeepSpeed YAML、EOS/chat-template 处理和 32K SFT 示例。[repo]
- OpenR1-Distill-7B 在列出的若干 evaluation 上接近或超过 DeepSeek 对应 distill model，但仍受具体 harness 影响。[repo]

## Gaps / Open Questions

- Teacher generation cost 与公开 math corpora 的 contamination。
- Filtering precision、trace diversity 与 negative-example policy。
- Living repo 的当前 recipe 可能不同于早期 release，复现前必须 pin version。

## Lookup-only

- Exact config、learning rate、epochs 与 sequence length：repository SFT recipe。

## Evidence Anchors

- `[repo]`：SFT、news 与 data-generation sections。
- `[hf-org]`：datasets 与 checkpoints。
