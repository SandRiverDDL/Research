# MiniMax-M2 Claims / Gaps

```yaml
---
source_id: minimax-m2-series
section_type: claims
stage: source-audit
depth: working
confidence: medium
need_expert_review: false
---
```

## Strong Claims

- MiniMax-M2 Series is the right MiniMax anchor for training recipe / agentic post-training.
- MiniMax-M3/MSA is important, but currently an architecture/long-context delta rather than a full training anchor.
- The central reusable ideas are agentic data pipelines, Forge RL infra, interleaved thinking, mixed-domain RL, and self-evolution workflow.

## Weaker / Underdisclosed Claims

- Exact data composition, reward implementation, RL hyperparameters, and verifier reliability are underdisclosed.
- Self-evolution claims are promising but heavily internal; external reproducibility is limited.
- Cross-model eval should focus on scaffold and task setup before accepting rank claims.

## Comparison Hooks

- vs GLM-5: Forge vs slime; both separate agent environment/rollout from training core.
- vs Kimi K2.5: MiniMax emphasizes executable artifact pipelines and interleaved thinking; Kimi emphasizes multimodal joint training and Agent Swarm.
- vs MiMo/Nemotron: MOPD/OPD comparison needs separate source; MiniMax M2 TR does not center OPD.
- vs M3/MSA: MSA belongs in architecture/long-context lens, not post-training recipe lens.

## Evidence Anchors

- 7-16: data pipelines.
- 19-23: Forge.
- 24-30: interleaved thinking, self-evolution, eval.
- `[m3-msa:1-6]`: architecture delta.
