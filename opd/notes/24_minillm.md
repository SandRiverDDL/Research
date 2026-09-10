---
title: "MiniLLM: On-Policy Distillation of Large Language Models"
authors: [Yuxian Gu, et al.]
org: tsinghua
year: 2024
venue: iclr-2024
arxiv_id: 2306.08543
url: https://arxiv.org/abs/2306.08543

confidence: 2
open_source: yes
verified: s

surveys:
  song-2026: "§Intro; §2.3 f-divergence unified framework; §4.1 Fixed Divergence Objectives (Table 3 + prose)"

addresses:
  - mode-collapse-fwdkl
  - exposure-bias

decisions:
  rollout: mixed
  loss: reverse-kl
  signal: logit
  iteration: continuous
  filter: none
  extra: none
---

> **一句话**：和 GKD 同期把 OPD 带入 LLM 时代的开山参考之一。

## 核心做法

Forward-KL 迫使 student 覆盖 teacher 全部 mode，把概率分到 void region；reverse-KL 让 student mode-seeking 专注主 mode，但梯度需经 policy gradient 推导：

$$\nabla\mathcal{L}(\theta)=-\mathbb{E}_{\boldsymbol{y}\sim q_{\theta}}\left[\sum_{t=1}^{T}(R_{t}-1)\nabla\log q_{\theta}(y_{t}|\boldsymbol{y}_{<t},\boldsymbol{x})\right],\quad R_{t}=\sum_{t'=t}^{T}\log\frac{p(y_{t'}|\boldsymbol{y}_{<t'},\boldsymbol{x})}{q_{\theta}(y_{t'}|\boldsymbol{y}_{<t'},\boldsymbol{x})}$$

三个稳定 trick：single-step decomp 把 $\mathbb{E}_{y_t\sim q_\theta}[r_t]$ 直接对 vocab 求和降方差；teacher-mixed sampling $\widetilde{p}=\alpha p+(1-\alpha)q_\theta$（α=0.2）抑制 reward hacking；length normalization 防短输出偏置。

## 谱系位置

- 上游：Seq-KD (Kim & Rush 2016) — forward-KL offline；MiniLLM 针对其 void-region 问题反转 KL 方向
- 同期：GKD (Agarwal 2024) — 同样 on-policy 但 divergence-agnostic，不用 REINFORCE，更稳定
- 下游：KETCHUP (Fan 2025) 用 K-step Bellman return 解决 MiniLLM 的 REINFORCE 高方差；DistiLLM (Ko 2024) 改用 skew-KL 绕开 void-region 不稳定

## 优缺点

- ✅ [song-2026 §4.1]：sequence-level policy gradient 梯度无偏，reasoning 任务序列连贯性优于 token-level 方法
- ⚠️ [song-2026 §2.3]：commits to reverse-KL + REINFORCE，方差高，需 reward baseline + length penalty + α 调参；training compute 显著高于 GKD
- ⚠️ [song-2026 §4.1 token-vs-sequence tradeoff]：instruction-following 上不如 token-level 方法（GKD/DistiLLM），token-level teacher quality 充足时 sequence-level 优势消失

## headline number

- GPT-4 score 54.7 vs SeqKD 52.0（GPT-2 760M student，DollyEval，§Table 1）
- Rouge-L 32.5* 超越 teacher 30.4（OPT-6.7B student，S-NI，§Table 1）

<!-- pdf: §Abstract / §2.1 reverse-KL motivation / §2.2 Eq.2-5 gradient derivation / §3.2 Table 1 / §4 Related Work / §5 Conclusion -->
<!-- song-2026: §Intro / §2.3 f-divergence unified framework / §4.1 Fixed Divergence Objectives -->
