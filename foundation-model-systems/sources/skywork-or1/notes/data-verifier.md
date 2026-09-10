# Skywork-OR1 Data and Verifiers

```yaml
---
source_id: skywork-or1
section_type: reward-verifier
stage: post-training
substage: reward-verifier
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Data selection 使用三道明确门槛：verifiable、correct、challenging。[31-32]
- Difficulty 是 model-relative：运行 N 次 rollouts，删除 0/N 与 N/N 的 prompts，因为它们会产生 zero group advantage。[32]
- Human audit 发现，仅靠 model pass rate 会放入不完整或可猜答案的问题；因此再用两个 LLM judges 多次投票做质量过滤。[33]
- Verifier implementation 也被基准和人工检查，因为 parser bugs 与 sandbox instability 会直接改变 reward distribution。[34-35]

## Why It Matters

Verifiable RL 的干净程度受限于 parser、tests 与 task statement。False reward 足以淹没算法差异，所以 verifier audit 应先于 optimizer experiment。

## Mechanism Sketch

1. 汇总 math/code sources。
2. Deduplicate，并对近期 AIME 做 decontamination。
3. 程序化验证 gold answers/tests。
4. 用 rollouts 估计 model-relative difficulty。
5. 人工抽检问题质量。
6. 用两个 LLM judges 的重复投票过滤全量数据。
7. 在 false-positive/negative 审计后选择 math parser 与 secure code sandbox。[31-35]

## Details / Evidence

- Math data 会重新抽取答案，并删除 URL/figure-dependent questions。[31-32]
- Code tests 先在给定 solution 上执行；embedding similarity 用于删除近重复题。[32]
- Math-Verify 需要额外包装，因为直接解析 gold answer 可能改变数学表达式。[34-35]
- Code sandbox 加入 AST validation、memory limit 与稳定 multiprocessing，但仍不支持所有 multiple-valid-output task。[35]

## Gaps / Open Questions

- LLM-judge threshold 和 judge training-data overlap 可能污染 quality filtering。
- Pass-rate filtering 可能删掉需要 curriculum 或工具才能学会的高价值难题。
- Code sandbox 覆盖范围远窄于真实 software environment。

## Lookup-only

- Final dataset counts、rollout N 与 retained proportions：第 31-33 页。
- Verifier implementation：第 34-35 页。

## Evidence Anchors

- 31-33：dataset preparation 与 model-aware filtering。
- 34-35：math verifier 与 code sandbox。
- `[rl-data]`：released dataset schema。
