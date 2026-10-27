# Kimi K2.7 Code Release Delta

```yaml
---
source_id: kimi-k2.6
section_type: stage-note
stage: release-delta
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- K2.7 Code 是 Kimi K2 当前 coding-agent release，官方明确强调 4,000+ tool calls 与 12+ hours continuous execution 的 long-horizon capability。[k27-announcement]
- 相比 K2.6，官方声称平均减少约 30% thinking-token usage，把 reasoning efficiency 作为独立优化目标。[k27-announcement]
- Release 支持 multimodal tool use，可处理 video 并通过 custom tools 做 temporal analysis 与 clip extraction。[k27-announcement]
- HighSpeed endpoint 声称保持同模型能力并提升 decode speed；它属于 serving delta，不是新 training recipe。[k27-announcement]

## Why It Matters

K2.7 Code 的 current-practice 信号是：long-horizon coding agent 不再只追求成功率，还同时优化 tool-call horizon、thinking-token cost 与 multimodal tool interface。但目前材料仍是 release/eval disclosure，不能替代 K2.5 TR。

## Mechanism Sketch

1. 在 coding-agent scaffold 中执行超长 tool-call sequence。
2. 对简单任务减少不必要 deliberation，降低 thinking-token usage。
3. 通过 tools 处理 image/video inputs。
4. 使用锁定 sampling parameters 提高 API output consistency。[k27-announcement]

## Details / Evidence

- 官方列出 Kimi Code Bench V2、Program Bench、MLS Bench Lite、Kimi Claw、MCP Atlas 与 MCP Mark Verified；这些是 release positioning，且部分 benchmark/scaffold 并未完整公开。[k27-announcement]
- Temperature、top-p、n 与 penalties 在 endpoint 中固定；这有利于产品一致性，但限制用户做 sampling-level ablation。[k27-announcement]
- Weights/code link 已给出，但公告没有描述 SFT/RL stages、reward、trajectory filtering 或 K2.5 Agent Swarm/PARL 是否延续。[k27-announcement, k27-hf]

## TR / Training Source 补查（2026-10-19）

- **核查范围**：官方 HF model card、Kimi 官方 resource 页面与 arXiv 定向检索。本轮未找到 Moonshot 发布的 K2.7 Code 专属完整 TR；这是检索结果，不是对不存在任何材料的证明。
- **官方材料边界**：model card / resource 仍主要披露能力、eval、deployment 与 native INT4，不能复原原始 code specialist / SFT / RL / consolidation recipe。[k27-hf, k27-official-resource]
- **新事实：第三方继续训练论文**：Surge AI 的 `Cross-Benchmark Transfer from RL on Agentic Coding Tasks`，arXiv:2610.00890，2026-10-01。它从已发布 K2.7 Code 开始，使用 1,700 expert-built tasks（1,000 repo + 700 terminal），用 hidden tests/verifiers 给 reward，训练 rank-32 LoRA，一轮 GSPO；属于 downstream RL，不是 Moonshot 原始发布 TR。[k27-surge-rl]
- **事实**：repo reward 为 target checks 的通过比例；任意 pass-to-pass regression 时 reward 归零。论文报告 external benchmarks 与 unseen harness transfer，但不能据此推断 K2.7 Code 原始训练流程。[k27-surge-rl]
- **证据入口**：[k27-official-resource] https://www.kimi.com/resources/kimi-k2-7-code ；[k27-surge-rl] https://arxiv.org/abs/2610.00890 。

## Surge RL 涨分的 Reviewer Audit（2026-10-19）

- **事实**：LoRA rank=32 作用于 attention 与 MLP projections；64 H200，108 rollout steps × 16 prompts × 8 rollouts，216 optimizer updates。约 1.4 万条多轮 trajectories 的规模是按配置推算，不是“只有 1,700 条 completion”。总 tokens / wall time 未在正文披露。[k27-surge-rl:§4]
- **事实**：训练 reward 为 regression-gated partial credit；hard all-or-nothing eval score 可因补齐少量遗漏显著跃升。DeepSWE 所有失败 baseline runs 的 target-test pass fraction 中位数 86%；作者逐例解释的 behavior changes 只来自 newly-solved subset，不能当作无选择偏差的因果证据。[k27-surge-rl:§7]
- **事实**：SWE-Bench Pro +4.7pp，p=0.059；DeepSWE headline +12.4pp 对 public baseline，p=0.055（对 in-house baseline +16.9pp，p=0.008）；SWE-Marathon +20pp 实为 1/20 -> 5/20，p=0.089，gain 95% CI [-3.2,42.3]pp。[k27-surge-rl:Table 4]
- **事实**：Terminal-Bench 2.1 没有 in-house base run；TB3 trained run 剔除 8 条 harness failures，按失败计仍 +9.4pp。TB3/4 是同一 family。剔除两个 public-baseline benchmarks 后 pooled p=0.02；不能只用 baseline mismatch 或 small-N 抹去全部信号。[k27-surge-rl:§5, Appendix A]
- **事实**：作者称数据早于四个 eval 发布，逐题检查无重叠，固定 final checkpoint 且不在 benchmarks 调超参；这是作者报告的控制，本轮未独立复核数据。训练是 coding、评测仍是 coding，cross-benchmark/harness 不能直接称广义跨能力 OOD。[k27-surge-rl:§3.3,§4.3,§5]
- **解释**：已有 programming knowledge 的强模型仍可能通过调整 requirement tracking / testing / termination policy，提高 all-tests-pass；LoRA 容量低并不要求 task-success delta 小。这个机制与案例相容，但未被独立消融识别。
- **假设 / 未验证**：Kimi 原始训练在这些 task distributions 已饱和、与 Surge 使用同 reward、或发布时因多目标/效率取舍压低这些 benchmarks，均没有直接证据。
- **缺口**：仅一个 training run；无 matching generic-data RL、binary-vs-partial reward、full-FT-vs-LoRA 等因果对照；未评测 coding 以外能力、全局退化或生产部署预算。统计显著不能填补这些缺口。[k27-surge-rl:§1,§5–8]

## Gaps / Open Questions

- 4,000+ tool calls 与 12+ hours 是测试能力描述，不是训练 trajectory distribution 的证据。
- Thinking-token 降低来自 length reward、distillation、routing 还是 decoding control，未公开。
- K2.7 是否保留 K2.5 的 joint text-vision RL、DEP、Agent Swarm/PARL，不能自动继承。
- HighSpeed 的精度、quantization 与 serving topology 未披露。

## Surge Training Data Availability（2026-10-19）

### 四类行为对应案例（事实，评测轨迹，不是训练题公开）

- 少漏需求：FastAPI middleware 的 get_stats/reset_stats 本应是 instance methods，base 却写为 module-level functions；RL model 满足指定接口。
- 按需求测试：base 只实现/测试匿名函数默认参数 `func(a = 1)`，漏掉 spec 要求的具名形式 `func f(a = 1)`；RL model 从具名例子开始并扩到更多变体。
- 保护已有功能：base 通过删除两个 components 实现零 layout shift，却破坏受保护的页面内容/行为；RL model 明确维护 must-change / must-preserve 两类要求。
- 自建验证依据：二维 PDE 任务 base 误设为一维并用同一假设自测；RL model 选解析二维解并反推输入来检验。另有 Verilog 用 Python emulator 对拍、Zstandard decompressor 自写 compressor 生成 round-trip inputs 的案例。[k27-surge-rl:§7.2]

### 开放状态

- **事实**：作者 blog 明确称 1,700 tasks 来自 Surge dataset catalog 的 coding collections 子集，并把获取入口指向 catalog / 联系团队；catalog 提供 Request Dataset 与商业 Trusted Program（train first, pay if it works）。这是商业获取入口，不是公开开源发布。[surge-coding-blog, surge-catalog]
- **核查结果**：截至本轮检查，论文、作者 blog、Surge HF organization 与公开 GitHub 页面未发现这 1,700 个 training tasks 的公开下载与开源 license。Surge HF 当时公开的 GDP.xlsx、DAYJOB-finance、DAYJOB-healthcare 不对应本文 coding training set。
- **证据边界**：商业 catalog 有 SWE / terminal collections，不足以保证论文 exact 1,700-task subset、hidden verifiers 或 environment snapshots 可按原版取得；具体交付内容与许可需另行确认。
- **原文入口 [surge-coding-blog]**：https://surgehq.ai/blog/hill-climbing-swe-agent-kimi-k-2-7 ，What was in the training set? / 获取段落。
- **原文入口 [surge-catalog]**：https://surgehq.ai/ots ，Coding Agents / Train first. Pay if it works。

## Lookup-only

- Headline benchmark values、速度和固定 sampling parameters：`[k27-announcement]`。

## Evidence Anchors

- `[k27-announcement]`: https://forum.moonshot.ai/t/441
- `[k27-hf]`: https://huggingface.co/moonshotai/Kimi-K2.7-Code
- `[k25-tr]`: K2.5 lineage method anchor。
