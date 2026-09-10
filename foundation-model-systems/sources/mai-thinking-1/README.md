# MAI-Thinking-1 Source Dossier

```yaml
---
source_id: mai-thinking-1
source_type: model-tr
org: Microsoft AI
release_date: 2026-06-02
priority: S
status: section-notes
openness: api-only
confidence: medium
---
```

## 一句话

MAI-Thinking-1 最值得读的不是榜单分数，而是它公开了一套 2026 reasoning model 的 hill-climbing 方法：用 scale ladder 选数据比例，用 staged mid-training / long-context extension 打底，用稳定性控制跑长 RL，用 self-distillation 重启/迁移 policy，再把多个 specialists 通过 trace-SFT + final RL 合成一个模型。

## 核心设计 / 创新点

- Data mixture optimization：不是公布一个固定配比，而是用 NLL eval、scale-ladder ablations、local/global search 和 repetition caps 来选数据比例；核心发现是小规模最优 mix 不一定迁移到目标规模。[16-20]
- Pretraining engineering：continued pretraining / mid-training 不是一个数据配比小节能覆盖；MAI 用 16K->64K->256K staged training、memorization-aware epoch caps、long-context extension、YOLO training stack 和 cluster goodput control 来支撑 base model。[21-30, 85-88, 106-109]
- Long RL stability control：MAI 把 reasoning RL 当成控制系统，显式处理 entropy、ratio spikes、language drift、length、problem difficulty 和 off-policy mismatch。[31-36]
- Self-distillation as RL engineering：self-distillation 不是普通 SFT，而是用于 collapse recovery、checkpoint migration、format conversion 和避免 policy 过窄。[34-37]
- Specialist consolidation：先训练 STEM/coding、agentic、helpfulness/safety specialists，再用 trace-SFT 聚合，最后用 lightweight RL 修 safety/style 并防 reasoning regression。[31, 49]
- Eval as climb gate：public hard benchmarks、simple agentic loop、human preference 和 safety eval 共同服务 hill-climbing decision，而不是只做 leaderboard reporting。[53-55, 101-106]

## 为什么重要

这份 TR 的价值偏 process transparency：它不提供 open weights，也没有完整公开数据和 reward，但能帮助你形成对大模型训练系统的 taste。尤其是 data mix 的 scale dependence、long RL 的稳定性控制、SFT 在 RL 中的 reset/transfer 角色，都是比具体 benchmark 数字更值得内化的内容。

## Source Bundle

- technical report: see `source-bundle.md`
- model card:
- announcement / blog: see `source-bundle.md`
- code / repo:
- weights: not open weights as of initial intake
- external eval:
- local pdf:
  - `/Users/chy/Research/foundation-model-systems/papers/mai-thinking-1/mai-thinking-1-tech-report.pdf`
- last checked: 2026-06-16

## 最大证据缺口

- “No third-party distillation / clean data” 依赖 Microsoft 内部 provenance，外部只能看 disclosure 形态，不能完全验证。[1-2, 12-13]
- Exact RL prompt distributions、reward functions、specialist data composition 和 gating criteria 没有公开。[31-49]
- Self-distillation 的 trace filtering 阈值、reward hacking filter、teacher/checkpoint selection 规则不完整。[34-37]
- Human side-by-side、safety gates 和部分 internal eval 不可完全复现。[53-55, 101-106]

## Lens Hooks

- data-mixture-search: scale ladder、local/global search、rank non-invariance、repeat caps。
- pretraining-engineering: mid-training、long-context extension、YOLO、cluster goodput。
- rl-training: GRPO-derived objective、adaptive entropy、outer ratio clip、reward decomposition、sampling/curriculum。
- sft-distillation: self-distillation as reset / checkpoint transfer / format conversion。
- consolidation: specialist trace-SFT + final RL vs DeepSeek OPD。
- eval: public hard benchmarks + simple agentic loop + human preference + safety gates。
- infra: Rocket/GB200/cluster details only if later writing infra lens。

## 阅读入口

- `section-index.md`: 回 TR 页码和 appendix。
- `notes/pretraining-data-mixture.md`: data mixture search 和 base-model data taste。
- `notes/pretraining-engineering.md`: continued pretraining、long-context extension、YOLO 和 cluster goodput。
- `notes/rl-training.md`: RL objective、sampling、reward decomposition 和 long-climb stability。
- `notes/sft-distillation.md`: self-distillation、collapse reset 和 checkpoint transfer。
- `notes/consolidation.md`: specialist teachers、SFT consolidation 和 final RL。
- `notes/eval.md`: benchmark / human eval / agentic eval 的证据强度。
- `notes/claims-and-gaps.md`: comparison 前先读。
