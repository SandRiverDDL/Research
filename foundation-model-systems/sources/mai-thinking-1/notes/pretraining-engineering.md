# MAI-Thinking-1 Pretraining Engineering

```yaml
---
source_id: mai-thinking-1
section_type: pretraining-engineering
stage: pretraining
substage: mid-training-long-context-yolo
depth: working
confidence: medium
need_expert_review: true
---
```

## Core Design / Innovation

- Continued pretraining / mid-training 是 MAI 的核心工程主线，不只是 data mixture 的后续：它把 30T 16K pretraining、3.4T 64K mid-training、150B 256K extension 串成一个 staged training program。[21]
- Long-context 的关键 insight 是“先在 MFU-friendly 的较短上下文训练，再用短 extension 校准到 256K”，而不是全程用最大上下文硬训；Appendix C 显示 32K + short 256K extension 可以接近/匹配更贵的 128K long run。[86-88]
- Training stability 来自一组系统级控制：memorization-aware epoch caps、zero attention output initialization、BF16/FP8/FP32 precision partition、dropless MoE imbalance logging、deterministic kernels/checkpointing。[21-27]
- YOLO 不是普通 infra 附录，而是模型设计的一部分：MoE routing、parallelism、activation offloading、checkpointing、fault tolerance 和 architecture v2-v5 co-design 共同决定能否把 1T MoE 训练到可用 MFU/goodput。[24-30]
- Cluster 环境把 topology、hardware health、certification、scheduling 和 observability 纳入训练控制 loop；报告强调 usable training capacity / goodput，而不是只数 provisioned GPUs。[106-109]

## Why It Matters

如果目标是培养 base-model / foundation-model-system taste，pretraining 继续训练要看三件事：数据目标如何变、上下文长度如何扩、训练系统如何支撑稳定长跑。MAI 的 data-mixture note 只能回答“比例怎么选”；本 note 回答“选好之后怎么把模型继续训到 reasoning RL 可用的底座”。

这些内容对小规模复现的迁移性有限，但对理解工业界大模型训练非常重要：很多看似“模型方法”的决策，其实受 MFU、memory、routing imbalance、checkpoint recovery、cluster topology 和 eval ladder 约束。

## Mechanism Sketch

1. Base 阶段先训 30T tokens、16K context、8192 GB200 GPUs；mid-training phase 1 训 3.4T tokens、64K context、8192 GB200 GPUs；phase 2 训 150B tokens、256K context、4096 GB200 GPUs。[21]
2. Mid-training data 不改 mixture weights，只在更长 sequence length 下 repack，目的是降低 distribution shift，同时减少高质量长文档被截断。[21]
3. 对可能已经被 memorized 的 source 设置更严格 epoch caps；proxy 是两个 pretraining checkpoints 间，validation loss improvement 有多少来自 near-certain tokens。[21]
4. Long-context extension 的实际 recipe 是先 64K mid-training，再 140B tokens 256K extension；报告认为 extension 快且相对便宜，未来可扩到 1M context。[87]
5. YOLO 负责 training loop、model definition、sharding、optimizer、dataloader、checkpointing，并把 PyTorch 上层训练与 kernels、parallelism、scheduler、Ray/Kubernetes control plane 接起来。[24-28, 106-109]

## Details / Evidence

### Mid-training / Context Extension

- MAI-Base-1 三阶段训练逐步拉长 context：pretraining 16K、mid-training 1 到 64K、mid-training 2 到 256K；pretraining 和 mid-training 1 使用 EP64 + ZeRO-2，mid-training 2 使用 ZeRO-3/FSDP，并在 mid-training 阶段使用 context parallelism。[21]
- Long-context mixture 的保守做法是“不改 mixture weights，只 repack 更长 sequence”，这样保留原数据分布，同时让 instructional / academic 等长文档减少 truncation。[21]
- Appendix C 的 code NLL、retrieval NLL、generative QA 用来验证模型是否真的利用远距离上下文；没有 long-context training 的模型在超出训练长度时 NLL/QA 明显退化。[85-88]
- Progressive context scaling 的结论很关键：32K 训练 1T tokens 后加约 100B tokens 的 256K extension，在 128K context 上可以匹配 1T tokens 的 128K mid-training；短上下文质量也没有显著损失。[86-87]
- 256K code NLL 的大部分提升发生在 extension 最初 1-10% iterations；报告解释为 positional/attention calibration，而不是学到全新能力。[87-88]

### Stability / Numerics

- 训练 hyperparams 包括 AdamW、global grad norm clip 1.0、12B tokens warmup、2e-4 到 2e-5 cosine decay、layer output dropout 0.15；报告特别说较高 final-to-peak LR ratio 和 dropout 对 post-RL/eval 有帮助。[21]
- Attention 初始化用 zero attention output：因为初始 softmax 近似 uniform，会让 causal mean pooling 降低 token representation diversity，并加剧后续 MoE routing imbalance；把 output RMSNorm gains 设为 0，让模型早期像逐 token FFN，attention 再逐渐介入。[22]
- 数值精度不是简单“用 FP8”：weights/activations 默认 BF16，forward GEMM 用 FP8 E4M3，data-gradient 用 FP8 E5M2，weight-gradient compute 用 BF16 + FP32 accumulation；pre-softmax、router logits、residual stream、optimizer、DP all-reduce 等敏感路径保留 FP32。[22-23]
- Loss curve 早期有 spikes，但没有跳 batch 或手动改配置；runtime logging 认为 spikes 主要影响 coding datasets，并与 dropless routing 下 expert imbalance 相关。[23]

### YOLO Training Stack

- YOLO 是 MAI 自研 large-scale training framework，支持 pretraining、mid-training、SFT 和 RL 的 training aspect；目标是 end-to-end control：kernels、parallelism、scheduling、checkpointing、observability 都能一起调。[24-25]
- Kernel 层包含 FP8 GEMM、MoE grouped GEMM、fused quantization，以及 Blackwell Cluster Launch Control；这些与 precision recipe 绑定。[25]
- Parallelism 组合包括 data、tensor/sequence、context、expert、pipeline；MAI-Base-1 long-context mid-training 使用 Ulysses-style context parallelism，所有 training stages 使用 tensor/sequence parallelism。[25-26]
- Expert parallelism 从 capacity-capped static shapes 走向 dropless MoE variable-size all-to-all；pretraining 把 expert parallelism 放在 NVLink domain 内，跨 rack 走 data parallelism。[26]
- Activation checkpointing/offloading 是为了让 activation memory 不阻塞 EP/NVL domain 设计；报告说所有阶段都用 transformer-layer checkpointing + fine-grained recomputation，offloading 通过 pinned host memory 异步传输。[26]
- MoE layer 同时支持 dropless 和 capacity-capped、load-balancing strategies、top-k scoring、telemetry、router replay for RL rollouts；static-memory dropless mode 用多轮 capped dispatch/compute/collect 降低 memory swings/OOM 风险。[26]

### Determinism / Fault Tolerance / Co-design

- YOLO 要求固定 hardware topology、model config、software version 下 bitwise reproducibility；checkpoint 保存 weights、optimizer、FP8 scaling history、dataloader progress 和 RNG。[27]
- Determinism 覆盖 data order、GPU reductions、stable top-k、network collectives；报告甚至为了 deterministic collectives 禁用 NVLink SHARP，承认会牺牲部分性能。[27]
- Fault tolerance 依赖 distributed checkpointing、async checkpointing、hot standbys 和 in-job restarts；DCP metadata/serialization 优化把 CPU memory overhead 和 checkpoint save time 降低 10x 以上。[27-28]
- v2-v5 的 architecture/infra co-design 显示一个规律：更复杂/更强的架构会先拉低 MFU，再靠 kernel、communication、memory optimizations 拉回来；他们声称 20+ infra/kernel optimizations 让每代大 run 都维持 20%+ MFU。[28-30]
- v5 因 35B active / 1T total 带来更大 parameter/activation memory，初始用 ZeRO-3 但 backward 变 communication-bound，最后靠 activation offloading 回到 ZeRO-2 来恢复 overlap。[30]

### Cluster / Goodput

- Appendix L 的核心设计是把 physical topology 和 hardware health 暴露成 first-class scheduling state；节点必须 healthy、topologically valid、observable、recoverable 才算 useful capacity。[106]
- GB200/GB300 以 rack-scale NVL72 作为 high-bandwidth scale-up domain，inter-rack RDMA 使用 InfiniBand；MAI 主 pretraining run 放在单个 GB200 cluster。[106]
- Certification 是 reliability boundary：single-node diagnostics、rack-level NCCL collectives、cross-rack InfiniBand validation 逐级筛掉 bad nodes / degraded links / silent corruption risk。[107]
- Control plane 由 Kubernetes、Kueue、MAI controllers、Ray 和 fleet-wide visibility 组成；pretraining 要 strict learner availability，RL 则有 learners、inference servers、rollout workers、routers 等多 actor placement/fault-tolerance 需求。[107-108]
- Observability 被接入控制 loop：XID、ECC、thermals、power、clock throttling、NVLink/IB/NVMe/PCIe/driver state 会变成 scheduling/remediation signals；目标是管理 usable training capacity 和 goodput。[108-109]

## Gaps / Open Questions

- 这部分非常工程化，但仍不足以复现：具体 kernels、scheduler policies、cluster size/failure rate、MFU breakdown、cost model 没有完全公开。
- Long-context extension 的 NLL/QA ablation 很有信息量，但它与 post-training、agentic tool use、safety 的交互披露较少；报告自己也说因此最终选择了更保守的 64K + 140B 256K extension。[87]
- Attention zero init、dropout 0.15、higher final LR 等设计都报告了有效，但公开 ablation 不足以判断哪些是 MAI 架构/scale 特有，哪些可迁移到小模型。
- YOLO/cluster 的 insight 更像工业系统 taste，不应直接变成个人小规模 recipe；比较时要区分“能内化的约束”和“只在 8K GB200 级别成立的实现”。

## Lookup-only

- Exact hyperparams、GPU counts、ZeRO stage、MFU、model version architecture table、kernel names、Kubernetes/Kueue/Ray details。
- 这些内容需要时回查；真正该记的是：continued pretraining 由 context schedule、stability controls、parallelism/memory plan 和 fault-tolerant cluster control 共同决定。

## Evidence Anchors

- 21: memorization-aware epoch capping、long-context mixture、three-phase training specs。
- 22-23: attention zero init、precision recipe、loss spikes。
- 24-30: YOLO framework、parallelism、MoE infra、determinism、fault tolerance、architecture/infra co-design。
- 85-88: long-context extension eval、progressive context scaling、final 64K + 140B 256K recipe。
- 106-109: cluster topology/health as scheduling state、certification、Kubernetes/Kueue/Ray control plane、observability/goodput loop。
