# 18 个模型系统的 Post-training Recipe 总结

```yaml
---
comparison_id: post-training-landscape-18-models
sources:
  - deepseek-v4
  - mai-thinking-1
  - glm-5
  - glm-5.1
  - glm-5.2
  - kimi-k2.5
  - kimi-k2.6
  - mimo-v2-flash
  - nemotron-cascade-2
  - nemotron-3
  - qwen3-coder-next
  - olmo-3
  - qwen3
  - longcat-flash-thinking-2601
  - step-3.5-flash
  - arcee-trinity-large
  - minimax-m2-series
  - mistral-3
status: reviewed
confidence: medium
---
```

## Question

在“非常经典 / 最新 SOTA / 开源程度高且有参考价值”三个标准下，18 个 model-system sources 对当前 post-training 工作分别有什么价值，哪些应进入主线，哪些只保留为 lineage / lookup reference？

## Executive Takeaway

事实：18 个 source 不是 18 个同质 recipe。真正值得作为当前 post-training 主线的，是能够解释 specialist training、RL stability、agent environment、policy consolidation、preference repair 或 fully-open reproducibility 的 sources；只有 architecture/pretraining 或 release positioning 的 source 不应因为模型名大而获得高优先级。

解释：最有迁移价值的共同结构不是某一种 PPO/GRPO 变体，而是：

```text
可控的起点 policy
-> domain / environment specialization
-> executable or rubric-grounded reward
-> long-horizon rollout stability
-> distillation / OPD consolidation
-> preference / safety repair
-> agentic + regression eval gates
```

当前主线可压缩成五个机制簇：

1. **Specialist consolidation**：DeepSeek-V4、MiMo-V2-Flash、Nemotron、GLM-5.2、MAI、Step、Qwen3-Coder-Next。
2. **Agentic environment / rollout systems**：LongCat、GLM-5/5.2、MiniMax-M2、Kimi K2.5、Nemotron、Qwen3-Coder-Next。
3. **Reasoning policy shaping**：Qwen3、MAI、Mistral 3、OLMo 3、DeepSeek-V4。
4. **Fully-open auditability**：OLMo 3 最强，Nemotron-Cascade 2 次之；多数其它模型只是 open weights 或 TR disclosure。
5. **Architecture-economics coupling**：DeepSeek-V4、GLM-5.2、MiMo、Step、Nemotron 3；价值在于让长 rollout / MOPD 可负担，而非 architecture 本身。

## Priority for Current Post-training Work

### S：主线精读与横向比较

- **DeepSeek-V4**：frontier-scale specialist OPD、reasoning modes、GRM signals、agent sandbox/rollout infra。
- **GLM-5.2**：critic-based PPO、compacted sub-traces、online anti-hacking、parallel OPD；但证据主要是 blog。
- **Kimi K2.5**：joint multimodal RL、zero-vision SFT、token-level clipping、PARL/Agent Swarm。
- **MiMo-V2-Flash**：student-on-policy multi-teacher MOPD 的具体机制与 agentic RL infra。
- **Nemotron-Cascade 2**：严格 on-policy GRPO、domain-wise Cascade RL、MOPD regression repair、较高开放度。
- **Nemotron 3**：frontier-ish open system 的 multi-environment RL、MOPD 和 rollout/quantization co-design。
- **OLMo 3**：fully-open SFT/DPO/RLVR、RL-Zero、Think/Instruct 分流，是复现与开放度标尺。
- **LongCat-Flash-Thinking-2601**：自动环境构建、DORA 异步 rollout、noise curriculum、agentic environment scaling。
- **MiniMax-M2 Series**：executable agentic data、Forge、interleaved thinking、自我迭代；作为 M3 前的 lineage recipe anchor。

### A：重要机制或经典 reference

- **MAI-Thinking-1**：data mixture search、长 RL stability control、self-distillation reset、trace-SFT consolidation。
- **GLM-5**：GLM lineage 的完整多阶段 agentic RL 与 slime infra anchor；当前实践由 5.2 增量覆盖。
- **Qwen3**：thinking/non-thinking fusion、四阶段 post-training、strong-to-weak on-policy distillation，仍是经典主线。
- **Qwen3-Coder-Next**：小 active footprint coding agent、executable environments、domain experts 与 distillation。
- **Step 3.5 Flash**：domain experts -> self-distillation -> scalable RL，MIS-PO 处理 long-horizon off-policy mismatch。
- **Mistral 3**：Ministral 3 的 `SFT/ODPO` 与 `CoT-SFT/GRPO/ODPO` 双路线、teacher-selection ablations；Large 3 本身没有 recipe。

### B：保留，但不投入主线精读

- **GLM-5.1**：只有 release delta，主要作用是版本边界。
- **Kimi K2.6**：只有产品/能力 delta；K2.5 才是 method anchor。
- **Arcee Trinity Large**：高价值 open MoE pretraining source，但与当前 post-training 工作不直接相关。

## Source Matrix

| Source | 当前角色 | Post-training 核心 | 证据 / 开放度 | 当前结论 |
|---|---|---|---|---|
| [DeepSeek-V4](../sources/deepseek-v4/README.md) | current-practice frontier anchor | specialist GRPO -> full-vocab multi-teacher OPD；GRM、reasoning modes、tool/agent infra | open weights + detailed TR；data/code 不完整 | **S**。研究 policy-level consolidation 与长轨迹系统耦合的主源 |
| [MAI-Thinking-1](../sources/mai-thinking-1/README.md) | closed industrial process anchor | long RL stability、self-distillation reset/migration、specialist trace-SFT + final RL | API-only，但 TR 对过程披露较强 | **A**。培养 RL engineering taste，不能当可复现 recipe |
| [GLM-5](../sources/glm-5/README.md) | GLM full-TR lineage anchor | SFT -> reasoning RL -> agentic RL -> general RL -> cross-stage distillation | open weights + TR | **A**。完整理解异步 agentic RL；current practice 看 5.2 |
| [GLM-5.1](../sources/glm-5.1/README.md) | release delta | coding/long-horizon/tool-use capability 增量，recipe 未披露 | blog/model-card level | **B**。仅用于版本边界，不能单独抽 method |
| [GLM-5.2](../sources/glm-5.2/README.md) | current GLM release delta | critic PPO for compacted sub-traces、anti-hacking、parallel OPD、expert merge | open weights；blog-bundle、非完整 TR | **S**。方法重要，但强结论必须标低 disclosure |
| [Kimi K2.5](../sources/kimi-k2.5/README.md) | Kimi current full-TR anchor | zero-vision SFT、joint text/vision RL、token-level ratio mask、PARL Agent Swarm | open weights + full TR | **S**。多模态 agent 与 proactive context management 主源 |
| [Kimi K2.6](../sources/kimi-k2.6/README.md) | release delta | 更强 agentic/multimodal/long-context capability，未公开新 recipe | model card / docs | **B**。跟踪 current model，不继承 K2.5 method 为新事实 |
| [MiMo-V2-Flash](../sources/mimo-v2-flash/README.md) | MOPD full-TR anchor | SFT -> specialist RL teachers -> student-on-policy MOPD；ORM + dense teacher advantage | open weights + detailed TR | **S**。当前 consolidation comparison 的核心公式源 |
| [Nemotron-Cascade 2](../sources/nemotron-cascade-2/README.md) | open post-training recipe anchor | strict on-policy GRPO、domain-wise Cascade RL、mid-pipeline MOPD、RLHF/long-context/code/SWE RL | checkpoints + SFT/RL data collection | **S**。与实际后训练工作最直接相关 |
| [Nemotron 3](../sources/nemotron-3/README.md) | open frontier system anchor | multi-environment RLVR、SWE-RL、RLHF、MOPD specialists、MTP rollout acceleration | open weights/data/recipe 较强，非 fully open | **S**。看大规模开放系统如何把 architecture、RL、deployment 联动 |
| [Qwen3-Coder-Next](../sources/qwen3-coder-next/README.md) | efficient coding-agent anchor | executable synthetic tasks、agentic midtraining、web/UX/QA/SWE experts -> distillation | open weights + TR | **A**。适合 agentic coding data/environment 与 expert packing |
| [OLMo 3](../sources/olmo-3/README.md) | fully-open reproducibility anchor | Think/Instruct 分流、SFT -> DPO -> RLVR、RL-Zero from base | weights/data/code/logs/checkpoints/eval 全链路开放 | **S**。开放度标尺，强度不是选择它的主要原因 |
| [Qwen3](../sources/qwen3/README.md) | classic mainline anchor | Long-CoT cold start -> reasoning RL -> mode fusion -> general RL；小模型 on-policy distillation | open weights + full TR | **A**。thinking/non-thinking 融合的经典 reference |
| [LongCat-Flash-Thinking-2601](../sources/longcat-flash-thinking-2601/README.md) | agentic environment scale anchor | structured agentic midtraining、DORA async RL、pass-rate allocation、instruction/tool noise curriculum | open weights + full TR | **S**。环境生成、噪声鲁棒和 rollout infra 比单一 RL loss 更重要 |
| [Step 3.5 Flash](../sources/step-3.5-flash/README.md) | efficient agent model anchor | shared SFT -> domain RL experts -> self-distillation -> scalable RL；MIS-PO binary filtering | open weights + full TR | **A**。研究 off-policy long-horizon stability 与效率 co-design |
| [Arcee Trinity Large](../sources/arcee-trinity-large/README.md) | open pretraining anchor | 没有高价值 post-training recipe；重点是 MoE/Muon/SMEBU/scaling ladder | open weights + pretraining TR | **B**。留作未来 base-model intuition，不占当前精读预算 |
| [MiniMax-M2 Series](../sources/minimax-m2-series/README.md) | agentic training lineage anchor | executable data、Agent-as-Verifier、Forge、interleaved thinking、M2->M2.7 self-evolution | open weights + detailed TR；当前模型已转 M3 | **S**。recipe 价值高，但必须标 lineage-reference |
| [Mistral 3](../sources/mistral-3/README.md) | permissive-open family + small-model recipe | Instruct: SFT distill -> ODPO；Reasoning: CoT-SFT -> STEM/general GRPO -> ODPO | Apache 2.0 weights；Ministral TR 详细，Large 3 未披露 | **A**。小模型 post-training 有价值，旗舰只作 openness reference |

## Key Differences

### 1. Consolidation 的四种不同哲学

- **Teacher distribution matching**：DeepSeek-V4 full-vocab OPD、MiMo/Nemotron MOPD；student 在自身 trajectories 上接受 dense teacher supervision。
- **Trace packing + repair**：MAI 先用 specialist traces 做 SFT，再以 final RL 修复 safety/style/reasoning regression。
- **Expert distillation**：Qwen3-Coder-Next、Step、Qwen3 小模型把 domain/strong teacher 能力压回 unified student。
- **Sequential capability repair**：Nemotron-Cascade 2 在 domain-wise RL 中间插入 MOPD，合并 intermediate teachers 并恢复退化能力。

这四类不能都简化叫“蒸馏”。比较时应明确：trajectory 由谁生成、teacher 提供 trace 还是 logits、监督是 sparse reward 还是 dense token signal、合并发生在最终还是阶段中间。

### 2. Agentic RL 的主要瓶颈已经从 objective 转到 environment 与 systems

- GLM、LongCat、MiniMax、DeepSeek、Qwen3-Coder-Next 都把 executable environment、trajectory replay、asynchronous rollout、tool schema 或 task generation 当成核心贡献。
- 因此仅比较 PPO/GRPO 公式会遗漏真正的可扩展性差异：环境可验证性、rollout tail latency、stale-policy control、compaction、reward hacking 和 replay determinism 才是长任务能否训练的关键。

### 3. Reasoning 与 general alignment 仍存在显式冲突

- Mistral 3 用独立 Instruct/Reasoning variants，并在 GRPO 后用 ODPO 修聊天质量。
- OLMo 3 也分 Think/Instruct 产品目标。
- Qwen3 尝试 mode fusion，把两种行为装进一个模型。
- DeepSeek-V4 进一步把 reasoning effort 训练成多个运行模式。

这里没有唯一胜者。统一模型降低部署复杂度，但更容易出现 verbosity、style interference 和 budget-control 问题；分支模型更干净，但增加维护与 consolidation 成本。

### 4. “开放权重”与“开放 recipe”必须分开

- **Fully-open**：OLMo 3。
- **较强开放 recipe/data**：Nemotron-Cascade 2、Nemotron 3。
- **TR 披露强但关键数据/code 关闭**：DeepSeek、GLM、Kimi、MiMo、Qwen、LongCat、Step、MiniMax、Mistral。
- **API-only process report**：MAI。
- **只有 release-level disclosure**：GLM-5.1/5.2、Kimi K2.6；其中 5.2 方法信号很强，但证据等级仍较低。

## Transferable Lessons

### For Current Post-training Work

1. 先建立 regression/eval gates，再选择 RL 或 consolidation 方法；否则阶段式训练只是在不可见地交换能力。
2. Specialist training 后必须明确 consolidation target：trace imitation、teacher logits、rewarded trajectories 或 post-RL preference repair，不能笼统说“merge experts”。
3. 长 horizon 任务应优先测 stale-policy、compaction、truncation、infinite generation、reward hacking 和 environment noise，而不是只调 PPO clip。
4. 小模型 recipe 需要单独验证 scale failure：Mistral 3B 的 vanilla SFT 崩坏、teacher choice 非单调，说明从 14B/32B 外推到更小模型不安全。
5. Agentic data 的可执行性和 replayability 应作为 data quality 的一部分；静态 trajectory correctness 不足以替代 environment-grounded evaluation。
6. Preference optimization 常常不是能力训练的替代品，而是 capability RL 后的 behavior repair stage。

### For Future Base-model Work

1. Base/midtraining 是否提前注入 code、agent trajectories、long-context dependency，决定后续 RL 的可塑性与成本。
2. Architecture 的价值要通过 rollout economics 衡量：KV cost、active parameters、MTP/speculative decoding 和 serving layout 会直接改变可承受的 RL horizon。
3. Fully-open flow 的价值在于能研究“base data -> post-training response”，而不仅是复现最终 benchmark。

## Claims I Trust

- MiMo、Nemotron-Cascade 2、Mistral 3 所描述的阶段顺序和 distillation/preference/RL mechanism，因为有明确 TR、局部公式或 ablations。
- OLMo 3 的开放度与 model-flow 可审计性，因为 artifacts 覆盖 weights/data/code/logs/checkpoints/eval。
- LongCat、GLM、MiniMax 关于 agentic training 需要专用 rollout/environment infra 的方向性结论；这与多个独立 source 的系统设计一致。
- Reasoning RL 后需要 general/preference repair 的方向性结论；在 Mistral、MAI、Qwen、Nemotron 等多条路线重复出现。

## Claims I Do Not Trust Yet

- 任何只根据官方 leaderboard 得出的“frontier/SOTA”总排序。
- GLM-5.2 parallel OPD、anti-hacking 和 critic PPO 的绝对增益，直到出现 full TR、ablation 或外部复现。
- Kimi K2.6 相对 K2.5 的 training innovation，因为目前主要是 release-level evidence。
- Mistral Large 3 的 post-training recipe；官方只披露结果定位，没有过程。
- 从 closed/internal agent eval 反推 data pipeline 或 RL mechanism 的结论。

## What To Read Next

下一轮不应继续无限加模型，而应生成三个横向 lens：

1. `MOPD / OPD consolidation`：DeepSeek-V4、MiMo-V2-Flash、Nemotron-Cascade 2、Nemotron 3、GLM-5.2。
2. `agentic environment and rollout systems`：LongCat、GLM-5、MiniMax-M2、DeepSeek-V4、Qwen3-Coder-Next。
3. `reasoning/general behavior integration`：Qwen3、Mistral 3、OLMo 3、MAI、DeepSeek-V4。

## Evidence Used

- 每一行优先使用对应 source dossier README 和其中链接的 stage notes。
- Mistral 3 新增证据来自 Ministral 3 TR pages 3-10 与 Mistral 3 official release blog。
- 本比较没有重新转写 benchmark tables；S/A/B 是对当前 post-training 工作的研究优先级，不是模型能力排名。

## Limits

- Source release dates、官方材料和“current practice”判断截至 2026-07-21。
- 多数 industrial sources 没有公开 data mixture、reward implementation、完整 configs 或 compute，因此这里只比较 disclosure-backed mechanisms。
- release delta 的信息新，但证据可能弱；full TR 信息强，但可能只是 lineage-reference。两者已分开加权。
