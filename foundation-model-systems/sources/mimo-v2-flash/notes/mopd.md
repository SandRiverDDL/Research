# MiMo-V2-Flash MOPD

```yaml
---
source_id: mimo-v2-flash
section_type: opd
stage: post-training
substage: multi-teacher-on-policy-distillation
depth: deep
confidence: high
need_expert_review: false
---
```

本 note 单独覆盖 MOPD，因为它是 MiMo-V2-Flash TR 的核心创新，且有足够公式/流程/ablation，后续适合和 GLM-5.2 parallel OPD、DeepSeek OPD、MAI specialist consolidation 对比。

## Core Design / Innovation

- MOPD 解决的是 multi-specialist consolidation：先训练多个 domain-specialized teachers，再让一个 student 在自己的分布上 rollout，并用 teacher logits 给 token-level dense reward。[11-14]
- 它不是普通 offline distillation：teacher 不先生成静态数据集让 student SFT，而是在 student on-policy trajectory 上按 token 给 reverse-KL 形式的 supervision。[13-14, 18]
- MOPD 把 distillation 写成 RL objective：teacher/student log-prob ratio 形成 token-level advantage，训练 loss 是 policy-gradient 风格的 `A * log pi_student`。[18]
- 训练/推理 policy 不完全同步时，用 importance sampling ratio `pi_theta / mu_theta` 过滤 discrepancy 大的 token；这比直接把 rollout 当作完美 on-policy 更工程现实。[18]
- 默认把 MOPD advantage 和 ORM / GRPO outcome advantage 相加：MOPD 提供 dense teacher guidance，ORM 提供 sequence-level outcome correctness。[18-19]

## Why It Matters

MOPD 值得内化的点是：post-training 后期的核心问题不只是“再跑一轮 RL”，而是如何把多个 specialist 的能力稳定合并到一个模型，同时避免 sequential training 的 see-saw regression。MiMo 的答案是让 student 保持自己的 on-policy distribution，用 teacher logits 做 dense credit assignment，再叠加 outcome reward。

对你的后训练工作，MOPD 是一个很好的 OPD 参考实现：它明确区分 teacher policy、student sampling policy、student training policy、token-level advantage、importance sampling filter 和 ORM advantage。这比很多 blog 只说“用 OPD 合并 experts”更有学习价值。

## Mechanism Sketch

1. SFT 得到一个通用 assistant checkpoint。
2. 用 domain-specific RL / SFT 训练多个 teachers，例如 math、coding、search agent、tool use、safety、general reasoning。
3. 给每个 prompt `x` 选择对应 domain teacher `pi_domain(x)`。
4. Student sampling policy `mu_theta` 生成自己的 response `y`，不是直接照 teacher 生成。
5. 对每个 token，计算 teacher/student log-prob ratio，作为 `A_MOPD,t`。
6. 如果 training policy `pi_theta` 和 sampling policy `mu_theta` 对 token 的概率差异过大，用 importance sampling gate 把该 token 权重设为 0。
7. 用 `w_t * A_MOPD,t * log pi_theta(y_t | x, y_<t)` 更新 student。
8. 默认再叠加 `alpha * A_ORM`，让 teacher dense signal 和 outcome/verifier reward 共同驱动训练。

## Details / Evidence

### 三阶段 post-training

- Stage 1 SFT 建基础 instruction following。[13-15]
- Stage 2 domain-specialized training：用 independent RL optimization 训练 teachers，覆盖 agentic capabilities，如 search、coding、general tool use，以及 non-agentic tasks，如 math、general reasoning、safety alignment。[13]
- Stage 3 MOPD：不做 parameter merging，也不从 experts 生成静态 offline datasets，而是把 multi-teacher knowledge integration 写成 on-policy RL process。[13]

### Token-level reverse-KL advantage

- TR 定义 target student policy `pi_theta`，student sampling policy `mu_theta`，domain teacher policy `pi_domain(x)`。[18]
- Reverse-KL gradient 可以写成 teacher/student log-prob ratio 乘以 student score function；这给出 token-level policy-gradient 形式。[18]
- MOPD surrogate loss 用平均 token loss：`- mean_t w_t * A_MOPD,t * log pi_theta(y_t | x, y_<t)`。[18]
- `A_MOPD,t = stopgrad[log pi_teacher(y_t | x,y_<t) / pi_student(y_t | x,y_<t)]`。直觉是 teacher 比 student 更认可的 token 获得正向 advantage，反之降低概率。[18]

### Training-inference importance sampling

- 因为 rollout 在 inference engine 的 `mu_theta` 上采样，而训练更新的是 `pi_theta`，MiMo 使用 training-inference importance sampling。[18]
- 如果 ratio `pi_theta / mu_theta` 不在 `[epsilon_low, epsilon_high]` 内，token 权重 `w_t` 设为 0，即丢弃 discrepancy 大的 token。[18]
- 这个设计很像 OPD/RL 工程里的 staleness control：它承认训练/采样存在异步或 engine mismatch，而不是假设完美同步。

### 和 ORM / GRPO 合并

- TR 明确说默认把 MOPD advantages 和 ORMs 计算的 advantages 合并，包括 GRPO。[18]
- 最终 advantage 是 `A_MOPD + alpha * A_ORM`。[18-19]
- Figure 6 比较了 ORM-only、MOPD without ORM、MOPD；在 AIME 2025 和 LiveCodeBench 上，MOPD 曲线优于单独 ORM 或无 ORM 版本。[19]

### Table 7 说明了它不是完美合并

- 多数 benchmark 上 MOPD 后 student 接近或超过 best teacher，例如 AIME 2025、HMMT、LiveCodeBench、Arena-Hard hard prompt、Tau2-Bench。[14]
- 但也有退化：GPQA-Diamond、Arena-Hard creative writing、SWE-Bench Verified、BrowseComp 有不同程度下降。[14]
- 这说明 MOPD 是有 tradeoff 的 consolidation，不是“所有 teacher 能力无损合并”。

## Gaps / Open Questions

- Teacher routing 没披露：如何从 prompt `x` 选择 `pi_domain(x)`，是手工 domain、classifier、mixture routing，还是多 teacher 加权？
- Teacher logits serving cost 没披露：多 teacher token-level logprob 需要很高 serving 吞吐，特别是 agentic trajectories。
- `epsilon_low / epsilon_high` 和 `alpha` 没披露，影响稳定性和 teacher/outcome reward balance。
- ORM / verifier 的具体类型、reward normalization、advantage normalization 没披露。
- 如果 teacher 对某个 domain 本身过拟合或 reward hacked，MOPD 会不会把 bad preference dense 地灌给 student？TR 没给防护。
- Table 7 有几个退化项，但没有系统解释为什么 creative writing / BrowseComp 掉分。

## Lookup-only

- Table 7 best-teacher vs after-MOPD numbers。[14]
- Figure 6 ORM / MOPD w/o ORM / MOPD curves。[19]
- Formula details: equations 5-9。[18-19]

## Evidence Anchors

- 11-14: MOPD framing, three-stage post-training, Table 7。
- 18-19: MOPD technical formulation and ORM combination。
- 19: Figure 6 ablation。
