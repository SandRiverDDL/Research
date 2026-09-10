# Foundation Model Systems — Current State

> Codex hot memory。只保留 compact / 新 task 后继续工作必需的信息；稳定规则见 `AGENTS.md`，历史理由见 `DECISIONS.md`。

Last updated: 2026-07-31

## Current Goal

审计 foundation-model dossiers 中的 OPD/MOPD recipe，针对用户的 A3B MoE sampled-token OPD 训练失败问题，给出证据边界、failure diagnosis 与小规模可执行设计。

## Confirmed Task Contract

- 用户确认的第二优先级只有：Qwen3.5 → Qwen3.6 / Qwen3.7、MiniMax M3、Kimi K2.7 Code、OLMo 3.1。
- Open-R1 与 Skywork-OR1 是 assistant 从旧候选列表误扩展的额外资料，不属于上述第二优先级，也不得计入指定交付。
- Lens、comparison、跨模型 summary 只有用户明确要求时才生成；补 dossier、stage note 或 release delta 不自动授权综合产物。
- 2026-07-29 用户明确要求：进入 foundation-model-systems，为最近的 Kimi K3 建立 dossier；该 source 很重要，并重点核验其是否为“断档第一”的开源模型能力。
- 2026-07-31 用户明确要求：查基模后训练 dossiers 的 OPD 具体 recipe，判断 sampled-token OPD 是否适合 A3B MoE，并整理训练失败坑点与设计方案。
- `comparison/post-training-priority-expansion-2026-07.md` 是未经明确授权生成的额外产物，不是 authoritative deliverable；保留或删除等待用户决定。
- 无法从状态文件确认的优先级或模型清单不得推断；应回看用户原话，仍不明确时再询问。

## Completed

- Kimi K3 已建立 S-priority 独立 model-TR dossier：包含 source bundle、section index、architecture/pretraining/post-training/agentic-environments/infra/eval/claims notes 与本地 PDF。
- K3 定位结论：截至 2026-07-29 是 open-weight 综合能力第一；“断档第一”可限定用于 open-weight 综合 capability / agentic-coding positioning，但不适用于 fully-open、全部能力、latency 或部署经济性。
- K3 validator milestone：`sources=29 issues=16 warnings=0`；16 个 issue 均为已有 closed-family stubs，K3 没有新增 issue。
- 已核对 OPD/MOPD 证据：DeepSeek-V4 full-vocabulary OPD、MiMo-V2-Flash sampled-token MOPD、Nemotron-Cascade 2 的 30B-A3B sampled-token MOPD、Qwen3 student-on-policy logit distillation、Kimi K3 sampled-token MOPD。
- Qwen3.5 已升级为 section-notes；Qwen3.6 有已核验 release delta，Qwen3.7 仅保留官方 API metadata。
- MiniMax M3、Kimi K2.7 Code、OLMo 3.1 已作为现有 lineage 的 release delta 补入。
- DeepSeek-R1、Ling/Ring 2.6、Open-Reasoner-Zero 已建立 source dossier。
- Open-R1、Skywork-OR1 dossier 已生成，但按上面的 contract 只算额外资料。
- 最新 validator：`sources=28 issues=16 warnings=0`；16 个 issue 均来自已有 closed-family stubs，本轮 source 没有新增 issue。

## Next Action

1. 交付 OPD recipe / failure-mode / A3B design guidance；不自动写入 comparison artifact。
2. 若用户提供训练日志或 config，再按 failure signatures 做最小复现诊断。

## Key Paths

- `AGENTS.md`：项目 workflow 与授权边界。
- `doc/memory/DECISIONS.md`：稳定决策及理由。
- `_meta/generated/status.md`：完整 source 状态；不要复制到本文件。
- `sources/<source-id>/`：source dossier 与 evidence anchors。
- `sources/kimi-k3/`：Kimi K3 dossier；默认从 `README.md` 与 `notes/claims-and-gaps.md` 进入。

## Relevant Decisions

- `2026-07-21: Keep project memory minimal; no compact hook`
- `2026-07-21: Synthesis artifacts require explicit authorization`
