# Kimi K3 Post-training

```yaml
---
source_id: kimi-k3
section_type: stage-note
stage: post-training
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- K3 的主 pipeline 是 `SFT -> domain/effort-specialized RL -> MOPD consolidation`，不是一个 policy 在混合任务上从头联合 RL。[12-14]
- RL 将三个 broad domains（general、general agents、coding agents）与三个 effort levels（low/high/max）笛卡尔组合成九个 experts；reasoning effort 是训练变量，不只是 inference knob。[12-13]
- partial rollout 与 per-token regularization 共同处理超长 agent trajectories：前者避免 straggler 等待，后者容忍跨 iteration resume 导致的 extreme staleness。[13]
- MOPD 以 student on-policy token 为载体，用对应 domain/effort teacher 的 clipped log-ratio 作为 dense reward，整合九个 experts。[13-14]
- QAT 从 SFT 贯穿 RL，并让 rollout/training 使用一致 MXFP4/MXFP8 scheme；deployment constraint 被提前写进 capability training。[12, 14]

## Why It Matters

K3 的 post-training taste 是先让 specialists 在清晰 domain/effort budget 下 climb，再用 on-policy distillation 合并，而不是让一个 mixed-policy objective 同时承受所有冲突。对 long-horizon agent，训练算法、rollout scheduler、sandbox state 与 quantization scheme 都是同一方法边界。

## Mechanism Sketch

```text
prior Kimi specialist trajectories
-> verification + human-in-the-loop annotation
-> SFT cold start (QAT begins)
-> RL:
   general × {low, high, max}
   general-agent × {low, high, max}
   coding-agent × {low, high, max}
-> collect nine-teacher trajectories
-> MOPD unified student
-> deployment-aware draft-model fine-tuning
```

## Details / Evidence

### SFT

- SFT trajectories 由 prior Kimi domain specialists 合成，再经过 multi-stage verification 与 human annotation；使用 XTML chat template 统一 long agent data representation。[12]
- 报告没有公开 SFT 数据规模、domain weights、teacher list、human annotation rate 或 verification thresholds。

### RL / Effort Control

- partial rollout 在 `N×K` active trajectories 中达到 `λNK` complete 后开始 optimization；未完成 rollout queue 到下一 iteration 优先 resume。[13]
- effort budget 以 cold-start model 的 per-problem initial budget `b0(x)` 为基准；超过 `τ·b0(x)` 的 trajectory reward override 为 -1。general task 统计 thinking tokens，agent task 统计 reasoning + tool-call arguments 的累计 output tokens。[13]
- 先训练较大 `τ` 的 max expert，再 anneal 到 high/low；每 domain 的 `τ` 由 human-in-the-loop 调整。[13]
- 非可验证 general task 用 agentic GRM tournament binary comparison；judge 强制 read -> rubric -> score -> scorepad protocol，并对超长 verbose output 施加 budget loss。[13]

### MOPD

- 每个 sampled `(domain, effort)` 对应一个 teacher；student token 的 OPD reward 是 clipped teacher/student log-prob ratio，并作为 dense per-token reward接入同一 RL framework。[13-14]
- top-k distillation target 在该 setting 中没有显示更快 convergence 或更好 final performance，因此保留更简单的 sampled-token reward。[14]

### Deployment-aware Post-training

- routed MoE expert weights 使用 MXFP4，activations MXFP8；attention、latent projections、shared experts、routers 保持更高精度。[14]
- QAT 覆盖 SFT 与 RL，rollout/training scheme 对齐，避免 policy update 面对不同 quantization behavior。[14]
- MTP layer 被 fine-tune 成 EAGLE-3-style draft；loss 直接优化 speculative acceptance rate 的 negative log，而不是只用 KL surrogate。[14]

## Gaps / Open Questions

- RL base algorithm 关键细节仍回指 K2.5：objective、ratio clipping、per-token regularization 形式、KL、group size、reward weighting 未在 K3 report 展开。
- Figure 8 只给随 RL FLOPs 上升的方向性曲线，没有 scale、误差、compute budget 或 matched-control ablation。
- MOPD 的 teacher routing、domain/effort sampling balance、teacher checkpoint selection、student initialization、Rmax 未公开。
- QAT 的 quality loss、serving speedup、different hardware portability 与 higher-precision control 没有完整 ablation。

## Transfer Hooks

- `worth-internalizing`: effort level 作为 RL curriculum 和 teacher axis，而非纯 prompt/API setting。
- `worth-internalizing`: long-horizon partial rollout 必须与 stale-policy control、sandbox resume 和 cache retention联合评估。
- `try-at-small-scale`: 先训少量 domain specialists，再对 on-policy student token 做 clipped teacher-ratio reward。
- `try-at-small-scale`: SFT/RL rollout 与最终 quantization scheme 对齐，测 train-inference mismatch。

## Evidence Anchors

- 12: SFT, three-domain RL, nine experts。
- 13: partial rollout, staleness, effort budget, agentic GRM, MOPD start。
- 14: MOPD objective, QAT-through-RL, EAGLE-3 draft fine-tuning。
- 21-22: long-context RL and sandbox infrastructure。
