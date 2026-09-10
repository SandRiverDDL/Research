# Nemotron-Cascade 2 Evaluation

```yaml
---
source_id: nemotron-cascade-2
section_type: eval
stage: eval
substage: reasoning-agentic-competitions
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Eval 设计围绕“高 intelligence density”：30B total / 3B active 模型在 IMO、IOI、ICPC 等强 reasoning/coding competitions 上接近 frontier open models。[1, 4-6]
- IMO 2025 结果包含 human expert review；IOI 和 ICPC 使用 official testcases / OnlineJudge，这比纯 benchmark table 更可信。[6]
- Appendix 覆盖 math、code reasoning、knowledge/STEM、instruction following、long context、agentic、multilingual 等设置；不过第一版 notes 尚未完整审计所有 setup。[2, 30-43]
- Method claim 最关键的 eval 不是 final table，而是 Cascade RL / MOPD 的 ablation 和 matched checkpoint comparison。[13-14]

## Why It Matters

Cascade 2 的 eval 应该服务两个问题：一是小 active model 能否在推理/编码赛事上达到高密度能力；二是 Cascade RL + MOPD 是否真的带来方法收益。前者是 positioning，后者更适合你学习 recipe。

## Gaps / Open Questions

- Competition eval 和 standard benchmark eval 的 sampling/scaffold/TIR 设置需要更细审计。
- 部分 baseline numbers 使用 official 或 recommended settings，跨模型完全可比性仍需谨慎。[4-6]
- Agentic benchmarks 上 Cascade 2 不一定全面领先，不能把 gold-medal reasoning 外推到所有 agentic workflows。

## Lookup-only

- Table 1/2 final scores。[4-6]
- Appendix eval setup pages。[30-43]

## Evidence Anchors

- 4-6: main result tables and competition evaluation。
- 13-14: method ablation and MOPD efficiency。
- 30-43: appendix eval setup。
