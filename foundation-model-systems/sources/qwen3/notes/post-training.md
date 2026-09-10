# Qwen3 Post-training

```yaml
---
source_id: qwen3
section_type: post-training
stage: post-training
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Qwen3 post-training 的核心不是单纯 RL，而是把 thinking 和 non-thinking 融合进同一个模型，并让用户通过 template / budget 控制 reasoning 行为。[10-12]
- 四阶段流程：Long-CoT cold start -> Reasoning RL -> Thinking Mode Fusion -> General RL。[10-12]
- Cold start 数据强调可验证、复杂、需要深推理，并过滤掉不需要 CoT 就能答对的问题，避免模型学浅层 guessing。[10]
- Reasoning RL 使用 GRPO，并强调大 batch、多 rollout、off-policy sample efficiency、entropy 稳定控制。[10-11]
- General RL 的 reward system 覆盖 instruction following、format following、preference alignment、agent ability 和 specialized scenarios。[12]

## Why It Matters

这是“一个模型同时服务 reasoning 和普通 chat”的代表 recipe。对后训练实践，值得学的是 mode-control 数据设计和 format consistency：non-thinking 样本仍保留空 `<think></think>`，用结构一致性减少行为切换的混乱。[11]

## Mechanism Sketch

1. Long-CoT cold start 用 QwQ-32B 生成候选 reasoning traces，再过滤 incorrect、repetition、guesswork、thinking/summary inconsistency、language mixing 等问题。
2. Reasoning RL 用未进 cold-start 的 query-verifier pairs，要求 learnable、challenging、覆盖 sub-domains。
3. Thinking Mode Fusion 用 Stage 2 自身 rejection sampling 生成 thinking data，同时混入 curated non-thinking data。
4. Chat template 用 `/think` 和 `/no think` 标记模式；non-thinking assistant response 放空 thinking block。
5. General RL 用 rule reward、model reward with reference、model reward without reference 覆盖更多任务。

## Details / Evidence

- Reasoning RL 总共收集 3,995 query-verifier pairs，并报告 Qwen3-235B-A22B 在 170 RL steps 内 AIME'24 从 70.1 到 85.1。[10-11]
- Thinking budget 不是显式训练出来的：当 thinking 长度达到阈值后，手动插入 stop-thinking instruction，模型基于已有 reasoning 直接回答。[11]
- General RL 明确允许 agent rollout 完整多轮 interaction，并接收真实 environment execution feedback。[12]

## Gaps / Open Questions

- Reward/verifier 的实现细节、off-policy 训练稳定控制和 environment 构成披露有限。
- thinking budget 的停止指令是工程控制，是否会在复杂 agent 任务中引入截断偏差需要比较。

## Lookup-only

- Chat template 示例看 Table 9。[11]
- 具体 benchmark 分数放 eval note / lookup。[13-21]

## Evidence Anchors

- 10-12: post-training four-stage pipeline.
- 20-21: thinking budget, fusion, general RL ablations.

