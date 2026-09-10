# Ling / Ring 2.6 Tool and Agent Training

```yaml
---
source_id: ling-ring-2.6
section_type: tool-agent-training
stage: post-training
substage: tool-agent-training
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Ring 把 coding、search、tool/workflow tasks 放进可执行 environments，而不是只学习 tool-call format。[16-18]
- Dynamic Pass Rating 根据当前 capability frontier 选题：剔除已经掌握和长期完全解不出的任务。[17]
- SWE 数据过滤 unstable tests、non-code edits、repository duplication 和不合适的 current-policy difficulty；同时限制 git history 并监控 trajectory 中的 reward hacking。[17-18]

## Why It Matters

真正的训练单元不是 prompt-response，而是 task/environment/verifier bundle。由于任务筛选依赖当前 policy，有效训练集会动态变化，应该作为 run state 被记录。

## Mechanism Sketch

1. 将 repository、search 和 tool tasks 封装成可执行 environment。
2. 用 cold-start model 估计 pass rate。
3. 保留难度适中、有效且多样的实例。
4. 使用带 bash、精确文件编辑和完成信号的 function-calling agent。
5. 执行 tests 或 environment checks 得到 terminal reward。
6. 持续监控 information leakage 与 reward hacking。[16-18]

## Details / Evidence

- 训练最大 200 turns，评测允许更长 horizon；因此 train/eval interaction budget 并不相同。[17]
- SWE tasks 只保留 pass rate 处于 0.1-0.9 的实例，是很具体的 frontier filtering 例子。[18]
- 移除 `git log --all` 降低 patch leakage；实时监控发现少量 cheating trajectory，说明 reward hacking 被当作运营指标处理。[18]

## Gaps / Open Questions

- Search 和 customer-service simulator 数据没有完整开放。
- 非 SWE tasks 的 terminal reward 和 partial-credit 设计披露不足。
- Repository cap 与 difficulty band 缺少独立消融。

## Lookup-only

- SWE retained instances、repositories、languages 与 tool names：第 17-18 页。

## Evidence Anchors

- 16-18：tool data、Dynamic Pass Rating、agent framework 与 SWE filtering。
- `[aenvironment]`：已开放 environment framework。
