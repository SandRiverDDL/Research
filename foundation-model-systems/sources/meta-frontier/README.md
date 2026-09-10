# Meta Frontier Family

```yaml
---
source_id: meta-frontier
source_type: blog-bundle
org: Meta AI / FAIR / Meta GenAI
release_date: ongoing
priority: B
status: stub
openness: mixed
confidence: low
lineage: meta-frontier
role: family-bundle
---
```

## 一句话

Meta frontier 模型家族是当前 frontier 阵营中**信号最弱**的样本：Llama 4（2025-04 Maverick / Scout / Behemoth）发布后被广泛视为落后一档（benchmark gaming 风波、长 context claim 复现失败、Behemoth 训练推迟），随后 Meta 在 2026 H1 推出代号 **Avocado** 的新一代基础模型作为 reset。这个 family 现在主要价值是 lineage-reference + frontier 落后样本对照，不是 current-practice。

## 为什么收（即使信号弱）

- **frontier 阵营完整性**：comparison 中没有 Meta 会让 "frontier industrial system" 的样本面缺一块。
- **失败 / 落后样本的研究价值**：Llama 4 是少见的"public bench-gaming + 训练受挫"的 frontier 失败案例，对理解 eval / disclosure / training failure 的工业边界有意义。
- **Avocado 作为 reset signal**：Meta 是否能从 Llama 4 失误中恢复，是 frontier dynamics 的重要观察点；现在材料少，但要先存目以免后续重抓。

## Family Lineup

- **Llama 系列（open-weights）**：Llama 1/2/3 已是历史 baseline，不在本 family 主线。
- **Llama 4 (2025-04)** — Maverick / Scout / Behemoth；本 family 第一个 frontier 级尝试。
- **Avocado (2026 H1, codename)** — 新一代 frontier 基础模型；可能后续会改用正式 brand name（Llama 5 或其他）。
- 后续 release 视披露程度补 release-delta。

## 已知公开材料

- **Llama 4 release blog + model card**：架构（MoE 的争议设计）、long context claim、agent / tool use 段落。
- **Llama 4 后续 leak / 第三方复现**：benchmark gaming 报道、长 context 复现失败的独立 eval。
- **Avocado**：目前以 leak + Meta 自己 teaser blog 为主，没有正式 model card / paper。

## Source Bundle

见 `source-bundle.md`。

## 收录策略

- 一个 family 一个目录；release-delta 单文件。
- 优先级：
  1. `release-deltas/llama-4.md` —— frontier 落后样本，写得简洁，重点记 disclosure / 复现失败 / lineage 价值。
  2. `release-deltas/avocado.md` —— 当前主线 reset，stub 形式跟踪，等正式 release 再升级。
- **不**升级到独立 dossier，除非 Meta 后续重新出 TR 级材料且和 frontier SOTA 重新拉齐。

## Caveats

- **openness: mixed**：Llama 系开 weights，但 frontier 模型（Behemoth、Avocado）目前未见 open weights，按 closed-weights 处理。
- 不要把 Llama 4 当 current-practice 用进 lens / comparison 横向总结；要明确标 lineage-reference / behind-frontier。
- benchmark gaming 风波相关 claim 必须有第三方独立 eval anchor，不能只用 Meta 自己 blog。
- Avocado 现阶段全部 confidence: low；任何 architecture / training claim 在正式 model card 出来前都按 rumor 处理。
