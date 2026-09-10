# Kimi K3 Infrastructure

```yaml
---
source_id: kimi-k3
section_type: stage-note
stage: infra
depth: surface
confidence: medium
need_expert_review: true
---
```

## Core Design / Innovation

- K3 infra 同时服务三类不常共现的负载：hybrid recurrent/global attention、3T sparse multimodal training、1M-token persistent agentic RL。[17]
- KDA Context Parallelism 不交换随 sequence length 增长的 KV blocks，而将每段表示为 cumulative transition + locally generated state，再用 associative prefix scan 恢复各 rank incoming state。[18]
- MoonEP 用 dynamic redundant experts 保证每 EP rank 收到完全相同 token load，并由 static shapes 消除 per-layer host synchronization；这是 QB 的 routing balance 之外的 execution balance。[19-20]
- 1M RL 的关键不是单纯大 KV cache，而是 unfinished rollout 跨 iteration 保持 prefix cache、sandbox state 和 policy update；external KV pool、partial rollout、auto-throttling、resumable AgentENV 联合解决。[21-22]
- production serving 将 KDA recurrent state 与 MLA KV pages 做 unified management，并把 fine hash blocks 与 coarse physical blocks 解耦，使 1M prefix 可在细粒度边界重用。[22-24]

## Why It Matters

K3 展示了一个常被忽略的事实：long-horizon agentic RL 的有效 batch 不只是 token tensor，还包含 rollout queue、KV/cache state、tool environment、sandbox filesystem/process state。算法允许 stale trajectory 并不够，系统必须让 state resume 的成本低到训练可持续。

## Mechanism Sketch

```text
pretraining:
  KDA segment transition + local state
  -> KCP associative prefix scan
  -> PP/VP + EP + ZeRO + CP
  -> QB routing + MoonEP exact execution balance

agentic RL:
  partial rollout pauses unfinished trajectory
  -> KDA/MLA prefix written to external CPU pool on eviction
  -> AgentENV incrementally checkpoints microVM
  -> next iteration resumes model + environment state

serving:
  unified paged KDA/MLA cache
  -> sparse KDA checkpoints at fine hash boundaries
  -> cache-aware fleet affinity + per-class budget admission
```

## Details / Evidence

### KDA / Pretraining

- KCP 对每个 segment 计算 transition matrix 与 zero-init local state；一次 all-gather 后按 document order compose，communication payload 对 sequence length 保持 fixed-size。[18]
- K3 组合 PP+VP、EP、ZeRO-1 DP、Pipeline ZeRO-2、CP；activation manager 允许 recompute、quantize、local/remote offload 按 tensor composition。[18-20]
- MoonEP 为每 rank 预留最多 `E/R` redundant expert slots；online planner 近似 offline ILP reference，zero-copy permute/unpermute 直接写入 expert-grouped remote positions。[19]
- perfect rank-level balance 后仍有 intra-rank expert skew，因此 routed GEMM 再用 workload-aware scheduler。[20]

### 1M Agentic RL / Sandbox

- co-located RL 将一次 K3 1M-context experiment 控制在数百 GPUs；training state 在 rollout phase 可 offload 到 NVMe，为 CPU external KV pool 让出 DRAM。[21]
- auto-throttling 依据 active/queued requests 与 KV utilization 动态调 rollout concurrency，避免 early underfill 与 later preemption。[21]
- AgentENV 基于 Firecracker microVM，支持 incremental checkpoint/resume、pause/resume、fork、snapshot；报告最低 checkpoint/resume latency 133/49 ms，memory overcommit 最高 6.5×。[22]
- 训练/评测期间创建 51,219,741 sandboxes、1,505,678 images；这是 system-scale claim，不代表外部可复现成本。[22]

### Serving

- KDA state 与 MLA KV 使用统一 page pool；fine-grained hash block（例 512 tokens）与 coarse physical block（例 6144）解耦，只有同时存在 MLA prefix 与所有 KDA-group checkpoints 的最长 boundary 才命中。[23-24]
- speculative KDA decode 不为每个 draft position snapshot 大 state，而缓存较小 projected inputs，verification 后 on-chip replay accepted prefix。[24]
- fleet 以 session primary/secondary consistent hashing 保 cache affinity；admission control 为 short/ultra-long request classes 分配独立 budget，避免 1M burst 拖垮 TTFT。[25]

## Gaps / Open Questions

- `depth: surface`：KCP exactness、MoonEP bound 与 kernel implementation 需要 systems expert 回读公式/appendix/code。
- 缺少完整 cluster topology、GPU type/count、training duration、MFU/goodput、failure rate、energy 与 end-to-end cost。
- MoonEP repo 存在，但 K3 的 exact configuration、scheduler calibration 和 integration 未形成可复现 release。
- AgentENV 的安全隔离、snapshot consistency、P2P image distribution 与 adversarial agent threat model 需要独立 audit。
- serving cost曲线来自 production stack/API，不等同于 self-hosted 1.56 TB weights 的实际经济性。

## Evidence Anchors

- 17-18: KDA kernels and KCP。
- 18-21: PP/EP/ZeRO stack, MoonEP, memory and multimodal optimization。
- 21-22: 1M RL, external KV pool, AgentENV。
- 22-25: hybrid prefix cache, kernels, fleet scheduling。
- 44-46: QB/MoonEP derivations。
