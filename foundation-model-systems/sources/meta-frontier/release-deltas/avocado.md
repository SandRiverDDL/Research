# Avocado Release Delta (codename)

```yaml
---
delta_id: avocado
parent_source: meta-frontier
release_date: 2026-H1
role: release-delta-preview
confidence: very-low
status: stub
openness: tbd
---
```

## 定位

Avocado 是 Meta 在 2026 H1 推出的新一代 frontier 基础模型代号，被视为对 Llama 4 失误的 reset。当前公开材料以 Meta 自家 blog teaser + 第三方 leak / 报道为主，没有 model card / paper，所有 architecture / training / agent data claim 都是 rumor 级。

## 为什么记录

- Meta frontier lineage 的当前 anchor，不存目就要重抓。
- 作为 closed-weights frontier 在 disclosure 极弱时的样本：family-bundle pattern 在这种"几乎没材料"的情况下也要能跑通。
- 后续若 Avocado 正式 GA 并放出 model card / paper，可快速升级到 stage notes 或独立 dossier。

## 已知 framing 信号（极低 confidence）

- 定位为 frontier reset，与 Llama 4 切割。
- 是否 open-weights、是否 MoE、是否 native multimodal、是否 hybrid attention —— 全部待官方确认。
- agent / long-horizon / reasoning 上的具体方向 —— 没有可信公开证据。

## Source

- 待补：Meta 官方 Avocado 公告 / teaser blog URL（在 https://ai.meta.com/blog/ 下定位）。
- 第三方 leak / 报道：进 stage notes 时挑 1-2 篇相对靠谱的 cross-check（避开纯 marketing 复述）。

## 升级 trigger

满足任一即升级（按改动大小决定升到哪一级）：

1. 出官方 model card / paper / system card → 升 `status: section-notes`，写 release-delta 全文。
2. architecture-level 公开（MoE profile / attention 类型 / context 规格）→ 视改动是否和 Llama 4 拉开代差，决定是 release-delta 升级还是单独 dossier。
3. 出现可复现 benchmark / 第三方独立 eval → 至少升到 stage notes。
4. 有 frontier 级 agent / reasoning 训练 pipeline 公开（不是 blog framing）→ 进 lens / comparison 主线。

## Caveats

- **不要拿 Avocado 进 lens / comparison 的强结论**。
- "frontier reset" 是 framing 不是 fact；需要 model card / 独立 eval 才能确认 Meta 是否真的拉回 frontier 中位水平。
- leak 类材料标 `[leak]`、confidence: very-low；不在引用链上承担证据角色，只用来标记"存在性"。
