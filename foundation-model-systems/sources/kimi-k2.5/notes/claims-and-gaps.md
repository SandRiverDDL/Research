# Kimi K2.5 Claims / Gaps

```yaml
---
source_id: kimi-k2.5
section_type: claims
stage: source-audit
depth: working
confidence: medium
need_expert_review: false
---
```

## Strong Claims

- Kimi K2.5 is a full TR anchor for Kimi K2.5 / K2.6 lineage reading.
- Joint text-vision pretraining/RL and Agent Swarm are the two central innovations.
- Agent Swarm is best read as parallel context management plus learned orchestration, not just a benchmark trick.

## Weaker / Underdisclosed Claims

- Zero-vision SFT is plausible and important, but may depend on strong prior multimodal pretraining.
- Agent Swarm cost, subagent policy selection, and training data are underdisclosed.
- In-house Swarm Bench should not be used as hard cross-model evidence.

## Comparison Hooks

- vs GLM-5: Kimi focuses on multimodal agent + parallel orchestration; GLM focuses on coding/search/terminal engineering and async RL infra.
- vs MiniMax-M2: Kimi trains orchestrator + frozen subagents; MiniMax emphasizes interleaved thinking and Forge for arbitrary agents.
- vs Qwen3-VL / LongCat-Omni: compare multimodal training infra, video compression, and zero-vision SFT.

## Evidence Anchors

- 2-4: joint multimodal training and zero-vision SFT.
- 4-6: Agent Swarm / PARL.
- 8-10: RL and infra.
- 13-15: Agent Swarm eval.
