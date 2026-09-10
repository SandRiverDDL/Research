---
title: "Online Experiential Learning for Language Models"
authors: [Tianzhu Ye, et al.]
org: microsoft-research
year: 2026
venue: arxiv
arxiv_id: 2603.16856
url: https://arxiv.org/abs/2603.16856

confidence: 2
open_source: partial
verified: a

surveys:
  song-2026: "§5.3 self-distillation table; OPCD/OEL behavioral PI"

addresses:
  - experience-internalization
  - teacher-staleness

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: iterative
  filter: none
  extra: privileged-info
---

> **一句话**：deployment experience 内化路线代表作。

## 核心做法

OEL 不直接把原始交互轨迹塞进 SFT，而是先从 deployment trajectories 抽取可迁移 experiential knowledge，再用同模型加 knowledge context 作为 teacher，通过 on-policy context distillation 固化到参数。

$$\mathcal{L}=\frac1{|y|}\sum_t D_{\mathrm{KL}}(\pi_\theta(\cdot|x,y_{<t})\|\pi_{\mathrm{teacher}}(\cdot|e,x,y_{<t}))$$

迭代循环是：部署产生轨迹 → 抽取经验 → on-policy consolidation → 更新模型 → 继续部署，推理期不需要再挂外部 memory。

## 谱系位置

- 上游：On-policy context distillation (2026) — OEL 继承 reverse-KL on student-generated prefixes
- 上游：ExPeL / Reflexion — 这些方法把经验作为外部 memory 或反思提示，OEL 改为参数内化
- 同期：OPCD (2026) — survey 将二者并列为 behavior PI / context-conditioned self-distillation
- 下游：continuous post-deployment learning — survey 把 OEL 视为把 OPCD 打开的 online loop 闭合

## 优缺点

- ✅ [作者 ack §3]：extraction 把 raw trajectory 转成 structured experiential knowledge，再 consolidation，避免直接蒸馏噪声轨迹
- ✅ [song-2026 §5.3]：OEL 将 trajectory PI 变成 continuous post-deployment distillation loop
- ⚠️ [作者 ack §4.1]：实验集中在 TextArena/FrozenLake/Sokoban 一类环境，scale 和开放式真实部署覆盖有限

## headline number

- consolidated experiential knowledge 7.8% → 21.4% vs raw trajectory on Sokoban（§4.6.1 Table 1）

<!-- pdf: §3 Online Experiential Learning / §4.6 Analysis / §5 Related Work -->
<!-- song-2026: §5.3 Self-Distillation / behavioral PI -->
