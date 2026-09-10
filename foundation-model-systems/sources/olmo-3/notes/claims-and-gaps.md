# Olmo 3 Claims and Gaps

## High-confidence Claims

- Olmo 3 是 fully-open model flow source，开放范围明显高于普通 open-weight TR。[1-6]
- Base training 和 post-training 阶段划分清楚，且每个阶段都有数据/代码/模型 artifact 入口。[1-6]
- 它适合作为 open recipe / reproducibility benchmark，不适合作为 frontier industrial SOTA 的唯一代表。[3-6]

## Underdisclosed / Needs Audit

- First pass 未验证所有外部 artifact 的可下载性和 license 细节。
- Appendix 的具体 mix、decontam、post-training data 还未完整抽取。
- OlmoRL 机制需要更细读，当前只记录了定位和高层 claim。

## Comparison Risks

- 和 Kimi/GLM/DeepSeek 比分数时要标注参数规模、训练 token、开放程度和 eval setting。
- 和 MAI/Step/LongCat 比后训练时，要区分 fully-open research recipe 与 industrial frontier recipe 的目标不同。

