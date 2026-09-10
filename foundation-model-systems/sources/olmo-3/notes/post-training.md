# Olmo 3 Post-training

```yaml
---
source_id: olmo-3
section_type: post-training
stage: post-training
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Olmo 3 不把 post-training 看成单条 alignment pipeline，而是分成 Think、Instruct、RL-Zero 三种目标模型。[5-6]
- Think branch 用 SFT -> DPO -> RLVR 学长 reasoning trace；Instruct branch 用 SFT -> DPO -> RLVR 学短回答、function calling 和低延迟行为。[5-6]
- RL-Zero 从 base 直接做 RLVR，是研究 base data / midtraining 对 RL 可学性的实验平台。[4, 63-64]
- Dolci suite 把 post-training data 明确拆成 SFT、DPO、RL 数据，为后续做数据审计提供入口。[1, 5-6]

## Why It Matters

对你现在的后训练方向，Olmo 3 的重点是“同一个 base 按产品目标分后训练路径”。Think 和 Instruct 的分离提醒：长推理能力、低延迟交互、function calling 不是同一条 objective 可以自然兼顾的。

## Mechanism Sketch

1. Think SFT 用长 thinking traces 建基础推理格式和行为。
2. Think DPO 用 contrastive data 扩展 SFT 没达到的 frontier，并为 RL 做初始化。
3. Think RLVR 在 verifiable domains 上继续提升。
4. Instruct branch 用专门 function-calling / concise response 数据约束交互行为。
5. RL-Zero 从 base 出发，绕开 SFT/DPO，观察 RLVR 能直接学到什么。

## Details / Evidence

- TR 明确说 Think 在 SFT、DPO、RLVR 各阶段都有 gains，并强调 Dolci Think 的 contrastive data 来自 Delta Learning 思路。[5]
- Instruct 目标是避免过度 verbosity 和不必要 thinking traces，function calling 数据被纳入 SFT，DPO 加入 multi-turn preference 和 length intervention。[6]
- RL-Zero 的动机是目前很多 RLVR 研究基于不透明 base/midtrain 数据，容易产生 contamination 或 prompt-template trick 的误判。[6]

## Gaps / Open Questions

- 需要回读 pages 36-65 和 appendix A.6/A.7，抽更细的 SFT/DPO/RL 数据构成。
- OlmoRL 的具体效率优化 first pass 只记录到 4x speedup claim，还没展开机制。

## Lookup-only

- 各分支 benchmark 表和训练超参放 appendix 查询。[105-114]

## Evidence Anchors

- 5-6: post-training overview.
- 36-65: Think / Instruct / RL-Zero main sections.
- 105-114: post-training appendix.

