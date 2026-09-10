# Kimi K3 Evaluation

```yaml
---
source_id: kimi-k3
section_type: stage-note
stage: eval
depth: working
confidence: medium
need_expert_review: false
---
```

## Verdict

截至 2026-07-29，**K3 是综合能力最强的 open-weight model，这个结论有独立证据；“断档第一”作为 shorthand 基本成立，但必须限定在 open-weight 综合 capability / agentic-coding positioning。** 它不是所有 benchmark 第一，也没有超越当前最强 closed frontier；在 latency、verbosity、self-hosting footprint、cyber end-to-end 与 license openness 上都不能称“断档领先”。

## Eval Design

- 官方 suite 分 Reasoning & Knowledge、Coding、Agentic、Vision 四轴，另有 internal coding/agent/conversation suites、cyber tiering、third-party results 与 cost-efficiency。[25-32]
- K3 全部 main results 用 `reasoning_effort=max`, temperature 1.0；single-step top-p 0.95，agentic top-p 1.0。[26]
- coding/agent eval 混用 Kimi Code、Claude Code、Codex；某些任务取各模型 best harness，某些按 vendor-native harness，某些用同一 harness。[26, 29-30]
- BrowseComp 使用 300K 触发 context compaction 后得 91.2；完整 1M、无 context management 为 90.4，说明 scaffold/context policy 是报告能力的一部分。[26]

## Evidence for “Open-weight #1”

### Independent composite / industry eval

- Artificial Analysis：K3 Intelligence Index 57，发布时仅落后 Claude Fable 5 与 GPT-5.6 Sol，领先 GLM-5.2 的 51；AA 将其标为 open-weights model。[31-32; aa-k3]
- Vals Index：K3 74.7，overall #2，仅落后 Fable 5 的 75.1；GLM-5.2 为 65.0。[31-32]
- Arena：WebDev #1 overall；Text Arena 约 1486，处于 top cohort 但不是第一；Agent Arena 落后 Fable/Sol/Opus。[31-32; arena-text]
- AISI/CAISI cyber：K3 在 ExploitBench 与 simulated network attack 上优于 GLM-5.2，但明显落后最强 closed cyber-capable models；这同时支持 open frontier leap 与 closed frontier gap。[31; aisi-cyber]

### Official suite

- 相对唯一列出的 open baseline GLM-5.2，K3 在公开主表的大多数 reasoning/coding/agent benchmarks 上明显领先；但只比较一个 open baseline 不能独立证明整个 open ecosystem 第一。[27]
- 相对 closed frontier，K3 在 ProgramBench、SWE-Marathon、BrowseComp、MCPMark、AutomationBench、SpreadsheetBench、部分 vision tasks 上领先；在 HLE/CritPt、DeepSWE、GDPval、OSWorld、Legal Research 与多个 vision tasks 上仍落后 Fable 5 或 GPT-5.6 Sol。[26-28]

## Where the “Gap” Is Real

- **综合 index**：AA 对 GLM-5.2 约 +6 points（57 vs 51），不是 leaderboard noise 级差异。[aa-k3]
- **agentic knowledge work**：AA-Briefcase 仅次 Fable 5，显著领先 K2.6 与 GLM-5.2；GDPval 也进入 closed frontier cohort。[31-32; aa-k3]
- **web / long-horizon coding**：WebDev Arena overall #1，SWE-Marathon/ProgramBench/Terminal-Bench 接近或进入 closed frontier。[27-28; arena-text]
- **lineage jump**：AA Kimi provider page中 K3 57，对 K2.6 44、K2.7 Code 42；这是相对上一代的显著跃迁。[aa-k3]

## Where It Is Not

- research-level reasoning：CritPt 23.4，低于 Fable/Sol/GPT-5.5；HLE 也明显落后 Fable。[26-27]
- cyber end-to-end：AISI/CAISI 报告 K3 ExploitBench 32% vs GLM-5.2 24%，但 arbitrary code execution 为 0/41，而最强 closed models 平均 20/41。[aisi-cyber]
- latency/throughput：AA model page记录约 33 tokens/s、TTFT 约 149s，且输出很 verbose；这些值会随 provider/日期变化，但足以否定“能力强所以部署体验也断档领先”。[aa-k3]
- self-hosting：约 1.56 TB published artifacts、2.8T parameters；原生 MXFP4 降低了相对成本，但绝非一般实验室或单机容易部署。[hf-model]
- openness：custom license + 未开放 data/full recipe，不是 fully open。

## Comparability Risks

- harness assignment 不统一；Kimi Code、Claude Code、Codex 自身具有不同 tools、prompts、context compaction 与 refusal/safety behavior。[26, 29-30]
- 某些 baseline 分数来自 official leaderboards，某些由 Moonshot 重跑，某些来自第三方，时间点与 hardware 不完全一致。
- SWE-Marathon 使用 final v1.1 前的 H20-calibrated branch；PostTrainBench 在 H20 而非 official H100 setting。[26]
- PerceptionBench 与大量 internal suites 未公开；只能支持 product-development signal，不能视为可复现学术证据。[28-30]
- K3 report 没给完整 variance；多个结果是单个 point estimate。
- leaderboard/Elo 和 API performance 会快速漂移；强结论应保留 `as of 2026-07-29`。

## Lookup-only

- 全量 public score table：27。
- internal capability table：29；cyber evaluation：30-31。
- independent evaluation与 cost table/plots：31-32。

## Evidence Anchors

- 25-26: suite, baselines, settings。
- 27-28: public results。
- 28-30: internal evaluation and harness assignment。
- 30-31: cyber。
- 31-32: third-party positioning and cost。
- `[aa-k3]`, `[arena-text]`, `[aisi-cyber]`: independent current checks。
