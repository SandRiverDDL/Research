# Kimi K3 Claims and Gaps

```yaml
---
source_id: kimi-k3
section_type: claims
stage: source-audit
depth: working
confidence: high
need_expert_review: false
---
```

## Bottom Line

- **事实**：K3 full weights 已公开，report、model card、inference integration 与 custom license 可访问；它是 open-weight，不是 fully open。[hf-model; k3-license]
- **判断**：截至 2026-07-29，K3 是 open-weight 综合能力第一；“断档”由多个独立综合/agentic/coding eval 支持，但应视为 current positioning，而不是永久或跨所有维度的绝对命题。[31-32; aa-k3; arena-text; aisi-cyber]
- **边界**：K3 仍总体落后 Fable 5 / GPT-5.6 Sol，且在 research reasoning、cyber end-to-end、latency、verbosity、deployability 与 openness 上存在明显短板。[26-32]

## Strongly Supported Claims

### Architecture / Scale

- 2.78T total、104.2B active、93 layers、896 routed experts、16 active/token、1M context、native vision；weights shape 与 report/model card相互一致。[10-11; hf-model]
- KDA + periodic MLA、AttnRes、Stable LatentMoE 是 K3 的实际 architecture，不是产品 scaffold claim。[3-9]
- QAT 从 SFT 贯穿 RL，released expert weights 为 MXFP4 / activations intended MXFP8；non-expert modules higher precision。[12, 14; hf-model]

### Post-training / Agent System

- SFT -> 9 RL experts -> MOPD consolidation 的 pipeline 有公式和 stage-level披露。[12-14]
- agent environments 覆盖 multi-harness、KG task synthesis、kernel optimization、persistent assistant、AET、web development，并使用 deterministic/hidden/model-based verification 的组合。[14-16]
- long-context RL infra 保留 unfinished rollout 的 model cache 与 sandbox state，AgentENV 支持 checkpoint/resume/fork/snapshot。[21-22]

## Supported but Easy to Overstate

### “2.5× scaling efficiency over K2”

- **事实**：report 给出 K2/K3 fitted scaling curves与 aggregate 2.5× compute-efficiency claim。[10-11]
- **不能推出**：KDA、AttnRes、LatentMoE、data、Muon 或 schedule 中任一 component 单独贡献 2.5×。
- **需要的证据**：matched-scale factorial ablation、fit uncertainty、held-out domain breakdown、training instability/failure runs。

### “Open frontier / 断档第一”

- **事实**：AA/ Vals / Arena / AISI 多源结果把 K3 放在 open-weight 第一，并进入 top proprietary cohort。[31-32; aa-k3; arena-text; aisi-cyber]
- **不能推出**：K3 在每个 domain 都第一，或 model-only intelligence 与 closed frontier 无差距。
- **需要的证据**：same-harness cross-open-weight suite、post-weight-release community replication、latency/cost-normalized self-host eval。

### “1M-context agent”

- **事实**：architecture、training curriculum、RL/cache/sandbox infra 都针对 1M context；BrowseComp 无 compaction 也有强结果。[12, 21-26]
- **不能推出**：任意 1M sequence 都能稳定精确 recall/reason，或 API/self-host deployment 的 1M SLO 已被公开验证。
- **需要的证据**：position-stratified recall/reasoning、multi-turn cache correctness、long-context degradation/latency curve。

## Major Disclosure Gaps

- pretraining tokens/FLOPs、data mixture、cutoff/provenance、full dedup/decontamination。
- SFT/RL dataset sizes、environment mixture、reward weights、judge identity/prompt、policy optimizer details。
- nine-expert training budget、MOPD routing/weighting、QAT quality/throughput ablation。
- safety alignment recipe、broad misuse eval、bio/chem/persuasion/autonomy risk；report 的 safety depth 主要是 cyber capability，不是完整 safety report。
- training code/config/checkpoints、data、RL environments、complete deployment stack。

## Openness Audit

- **weights**：公开、non-gated，约 1.56 TB artifacts。[hf-model]
- **code**：official repo 主要是 report/README/license；部分 supporting components（如 MoonEP、AgentENV、FLA PR）有独立开源入口，但不是完整 K3 training stack。
- **data**：未开放。
- **recipe**：stage-level disclosure，无法 end-to-end reproduce。
- **license**：允许广泛使用/修改/分发，但大 MaaS commercial use 需另签协议，超大产品有 attribution/display 条款。[k3-license]
- **结论**：`open-weights + substantial technical disclosure`；不是 `fully-open`，也不宜无限定写“开源模型”。

## Reviewer Questions

1. 如果只用同一 open harness、同一 context policy 和同一 tool budget，K3 对 GLM-5.2 / DeepSeek-V4 / Qwen current models 的 gap 还剩多少？
2. 2.5× scaling gain 中 architecture 与 data/recipe 各占多少？是否能在 <100B active regime 复现？
3. multi-harness RL 是真正 scaffold generalization，还是覆盖了 benchmark harness distribution？
4. MOPD 对九 experts 的 capability retention 相比 joint multi-domain RL、SFT merge、top-k distillation 各有多大增益？
5. native MXFP4 self-hosted weights 在不同 accelerator 上的 quality、throughput、memory 与 numerical stability 如何？
6. weights release 后，independent safety/capability eval 是否复现 API版本表现，还是存在 serving/scaffold delta？

## Evidence Anchors

- 3-12: architecture and pretraining。
- 12-16: post-training and environments。
- 17-25: infra。
- 25-32: evaluation and cost。
- `[hf-model]`, `[k3-license]`, `[aa-k3]`, `[arena-text]`, `[aisi-cyber]`。
