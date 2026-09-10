---
title: "ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation"
authors: [Kanghui Tian, Siyuan Liu, Ziang Yan, Sheng Xia, Shuai Dong, Yi Wang]
org: shanghai-ai-lab
year: 2026
venue: arxiv
arxiv_id: 2606.05718
url: https://arxiv.org/abs/2606.05718
zotero_key:

confidence: 4
open_source: yes
verified: a

addresses:
  - privileged-context-gap
  - cross-tokenizer

decisions:
  rollout: student
  loss: forward-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: privileged-info
---

> **一句话**：可恢复视觉 privilege 的多模态 OPD 路线。

## 核心做法
Answer-based OPSD 的特权信号 R（gold answer / rationale）含 H(R|X)>0 的 student 推理时不可达分量，会诱导 shortcut imitation。改用 visual cue S，论文用 deterministic 抽象 S=f(X) 论证 H(S|X)≈0，特权信息可被 student 从 X 恢复，从而不破坏 train-test 分布。

## 谱系位置
不是引入更强 teacher 或更复杂 loss，而是换"特权类型"：visual cue 替代 answer/rationale；并新增 cue recovery module —— 在选定 transformer 层给 sink token 一组**专用** Q/K/V/O，仅在 prefill cross-attend visual tokens，不改推理接口、无 autoregressive 开销、无 cue-生成辅助 loss，cue 监督只通过 distillation 梯度隐式注入 θ_sink。

## Method
- 框架：on-policy distillation，student 自己 rollout 完整轨迹 ŷ；teacher 看到 (X, cue S) 提供监督，student 看不到 S。
- 模块：在选定层 ℓ 用 sink token h_sink^(ℓ) cross-attend V^(ℓ)=image tokens，得到 z_sink^(ℓ)，残差加回 h_sink；后续 question/answer token 通过 causal attention 读到这个内部 cue 表示 Ŝ=g(V,Q;θ_sink)。
- 目标：标准 OPD KL（PPO-style，含 importance ratio + clip），梯度对 θ_sink 形如 sg[A_n]·∇_Ŝ log p_θ(ŷ_n|X,Ŝ,ŷ_<n)·∇g —— 教师概率高于学生时把 Ŝ 推向 teacher-aligned 方向。
- 数据：Vision R1 训练集，cue text 由外部 pipeline 离线构造一次。

## 优缺点

- ✅ [作者 ack §3.1]: 将 privilege 限制为可由图像恢复的 visual cue，避免 answer/rationale privilege 的不可达 shortcut。
- ⚠️ [作者 ack §5]: cue 质量依赖外部 generator，且没有直接验证 sink token 是否重建了 cue 文本。

## headline number

- Qwen3-VL-2B/8B average +1.19/+1.24 over answer-based OPSD and +0.64/+1.08 over stronger-teacher OPD（§4 Table 1）

## Evidence
- "+1.19 / +1.24 over OPSD; +0.64 / +1.08 over OPD" — Abstract & §1，Table 1 列 "Avg(+δ)"（46.07/+1.19、59.39/+1.24、47.57/+0.64、64.96/+1.08）
- 七 benchmark = Vision R1-Test / DynaMath / MathVista / WeMath / MathVerse / MMMU-Val / Video-MME — §4 Data
- "deterministic abstraction S=f(X), H(S|X)=0" 与 "answer privilege H(R|X) can be large" — §3.1 Px2、Appendix F.1
- sink token + dedicated W_Q/W_K/W_V/W_O cross-attention，区别于复用现成 attention 的 SinkTrack — §3.2、§3.2 Px1
- PPO-style 目标 + 重要性比 + clip — Appendix F.2 Px1
- 代码：https://github.com/tiankanghui/ViCuR

<!-- pdf: §3 Method / §4 Experiments / §5 Limitations -->
