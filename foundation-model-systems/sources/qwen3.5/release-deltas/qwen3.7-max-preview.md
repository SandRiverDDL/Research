# Qwen3.7 API Release Delta

```yaml
---
delta_id: qwen3.7
parent_source: qwen3.5
release_date: 2026-07
role: release-delta
confidence: low
status: intake
openness: api-only
---
```

## 定位

Qwen 官方 API platform 当前列出 Qwen3.7-Max 与 Qwen3.7-Plus；Max 为 text model，Plus 支持 text/image/video，二者均标注 1M context。[qwen-api]

这是 product/API tracking，不是 training source。当前 primary material 不足以支撑 architecture、RL recipe、所谓 all-field thinking 或 35 小时 autonomous-agent 等强结论，因此旧 stub 中这些无 anchor claim 已删除。

## 可确认 delta

- Qwen3.7 已进入官方 API flagship naming。[qwen-api]
- Max 与 Plus 的 modality 不同，不能把 Plus 的 multimodal capability 泛化给 Max。[qwen-api]
- 当前没有足够 open weights/model card/TR 证据，只能记录 product metadata。

## Source

- 官方 API platform: https://qwen.ai/apiplatform

## 不能推出的事

- 不能默认继承 Qwen3.5 architecture。
- 不能从 1M context 反推训练 context 或 long-context curriculum。
- 不能从产品 agent capability 反推 post-training environment、reward 或 scaffold。

## 升级 trigger

出现官方 model card、weights、TR 或可复现 benchmark setup 后再升级。

## Evidence Anchors

- `[qwen-api]`: 官方 flagship model listing。
