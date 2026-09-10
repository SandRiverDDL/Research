---
title: OPD Survey Queue (song-2026 + autoresearch leftovers)
source: 94 scored - 31 written/off-scope = 56 with arxiv_id + 10 without
status: queue
---

# OPD Survey Queue

> 第一轮 autoresearch 三源（arXiv/OpenReview/Semantic Scholar）+ song-2026 综述共 94 篇 dedup 后，
> 减去已落盘 27 张 in-scope L1 + 4 张补卡 + 2 张 off-scope = 31 张已处理，剩 **56 + 10** 待 triage。
>
> **使用方式**：cc 重跑 search 时当 negative list 防重复；逐条审 → 升 L1（写卡）/ 降 C（删）/ 留 queue。
> 所有 confidence 取自三源 raw 标签，**未读全文**。

## T3（次优先，4 篇）

| arxiv_id | year | first_author | title | source |
|---|---|---|---|---|
| 2606.05152 | 2026 | Rishabh Agrawal | Reinforcement Learning from Rich Feedback with Distributional DAgger | arxiv |
| 2605.21606 | 2026 | Xiaogeng Liu | When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning | semantic-scholar |
| 2605.28014 | 2026 | Ziqi Zhao | ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains | semantic-scholar |

## T4（低置信，53 篇 — 大多需降 C，仅供 grep title 关键词参考）

| arxiv_id | year | first_author | title | source |
|---|---|---|---|---|
| 2603.11178 | 2026 | Yuanda Xu | PACED: Distillation and On-Policy Self-Distillation at the Frontier of Student C | semantic-scholar |
| 2410.18574 | 2024 | Shivam Adarsh | SIKeD: Self-guided Iterative Knowledge Distillation for mathematical reasoning | semantic-scholar |
| 2606.11627 | 2026 | Xun Wang | When Context Returns: Toward Robust Internalization in On-Policy Distillation | arxiv |
| 2606.11173 | 2026 | Semih Kara | The Role of Feedback Alignment in Self-Distillation | arxiv |
| 2606.10334 | 2026 | Haoyu Dong | Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Vis | arxiv |
| 2606.09348 | 2026 | Yang Tian | PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment | arxiv |
| 2606.09304 | 2026 | Haoran Xu | SG-OPD: Sign-Gated On-Policy Distillation via Sign-Consistency Gating and Phased | arxiv |
| 2606.09059 | 2026 | Jianxiong Shen | Stage-1 Controls the Entropy Regime, Not the Outcome | arxiv |
| 2606.08719 | 2026 | Yishuo Cai | Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-D | arxiv |
| 2606.08432 | 2026 | Li Jiang | Trajectory-Refined Distillation | arxiv |
| 2606.07000 | 2026 | Shizhe Xiang | Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimoda | arxiv |
| 2606.06076 | 2026 | Haocheng Luo | Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self | arxiv |
| 2606.04036 | 2026 | Yifeng Liu | Self-Distilled Policy Gradient | arxiv |
| 2606.03603 | 2026 | Yucheng Zhou | World Models Meet Language Models: On the Complementarity of Concrete and Abstra | arxiv |
| 2606.03532 | 2026 | Haowei Guo | When Should the Teacher Move? Temporal Coupling and Stability in Self On-Policy  | arxiv |
| 2606.03089 | 2026 | Ming Wen | Constitutional On-Policy Safe Distillation | arxiv |
| 2606.02530 | 2026 | Hao Li | SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment | arxiv |
| 2606.01249 | 2026 | Xingrun Xing | Trust Region On-Policy Distillation | arxiv |
| 2606.00628 | 2026 | Ruiqi Zhang | Robust Reasoning via Dynamic Token Selection for Distribution-Aligned Self-Disti | arxiv |
| 2606.00564 | 2026 | Hee Suk Yoon | Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradie | arxiv |
| 2606.00305 | 2026 | Yuxuan Jiang | Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidan | arxiv |
| 2606.00172 | 2026 | Yang Li | CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping fo | arxiv |
| 2605.31159 | 2026 | Daniil Plyusov | Trust-Region Behavior Blending for On-Policy Distillation | arxiv |
| 2605.30861 | 2026 | Gaetan Narozniak | Distilling LLM Feedback for Lean Theorem Proving | arxiv |
| 2605.29089 | 2026 | Xinyu Liu | OISD: On-Policy Internal Self-Distillation of Language Models | arxiv |
| 2605.09548 | 2026 | Yihong Liu | Crosslingual On-Policy Self-Distillation for Multilingual Reasoning | arxiv |
| 2410.11325 | 2024 | Wenda Xu | Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Int | semantic-scholar |
| 2604.10688 | 2026 | Binbin Zheng | SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adapt | semantic-scholar |
| 2603.24596 | 2026 | Di Cao | X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLM | semantic-scholar |
| 2605.03677 | 2026 | Wenjin Hou | Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe | semantic-scholar |
| 2605.11182 | 2026 | Siqi Zhu | The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes | semantic-scholar |
| 2604.16830 | 2026 | Jiaxin Zhang | The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Di | semantic-scholar |
| 2604.07941 | 2026 | Shiwan Zhao | Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy L | semantic-scholar |
| 2605.13643 | 2026 | Siqi Zhu | Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Poli | semantic-scholar |
| 2605.07725 | 2026 | Qiyong Zhong | SOD: Step-wise On-Policy Distillation for Small Language Model Agents | semantic-scholar |
| 2605.22731 | 2026 | Dong Nie | Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, | semantic-scholar |
| 2605.11739 | 2026 | Yuchen Cai | Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillatio | semantic-scholar |
| 2605.15113 | 2026 | Yue Yu | Learning from Language Feedback via Variational Policy Distillation | semantic-scholar |
| 2606.09471 | 2026 | Haoran Xin | Escaping the KL Agreement Trap in On-Policy Distillation | semantic-scholar |
| 2606.09456 | 2026 | Yifan Niu | Breaking the Tokenizer Barrier: On-Policy Distillation across Model Families | semantic-scholar |
| 2606.07082 | 2026 | Zhennan Shen | On the Geometry of On-Policy Distillation | semantic-scholar |
| 2606.01476 | 2026 | Yuhang Zhou | OmniOPD: Logit-Free On-Policy Distillation via Speculative Verification | semantic-scholar |
| 2606.01039 | 2026 | Hanyang Zhao | OPD+: Rethinking the Advantage Design for On-Policy Distillation | semantic-scholar |
| 2605.31490 | 2026 | Yaocheng Zhang | Are Full Rollouts Necessary for On-Policy Distillation? | semantic-scholar |
| 2605.12483 | 2026 | Yuanda Xu | Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Prin | semantic-scholar |
| 2606.00305 | 2026 | Yuxuan Jiang | Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidan | semantic-scholar |
| 2605.07711 | 2026 | Jie Sun | SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation | semantic-scholar |
| 2605.17862 | 2026 | Xianwei Chen | f-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Cont | semantic-scholar |
| 2605.30833 | 2026 | Yanjiang Liu | Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Pol | semantic-scholar |
| 2604.04461 | 2026 | Fatemeh Khadem | DP-OPD: Differentially Private On-Policy Distillation for Language Models | semantic-scholar |
| 2606.00564 | 2026 | Hee Suk Yoon | Decomposed On-Policy Distillation for Vision-Language Reasoning: Visual Gradient | semantic-scholar |
| 2605.29343 | 2026 | Hao Lei | Draft-OPD: On-Policy Distillation for Speculative Draft Models | semantic-scholar |
| 2510.23497 | 2025 | Walid Bousselham | VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Disti | semantic-scholar |

## 缺 arxiv_id（10 篇 — 需手动补 id 才能进流水线）

| year | first_author | title | venue | source |
|---|---|---|---|---|
| 2025 | Yifan Yan | LUFFY: Learning to Reason under Off-Policy Guidance | arxiv | survey |
| 2025 | Zhenyu Xu | KDRL: Unifying Knowledge Distillation and Reinforcement Learning for Post-Traini | arxiv | survey |
| 2025 | Songhua Wu | AKL: Rethinking Kullback-Leibler Divergence in Knowledge Distillation | arxiv | survey |
| 2025 | Zaid Khan | DataEnvGym: Data Generation Agents in Teacher Environments with Student Feedback | iclr-2025 | openreview |
| 2025 | Zhaolin Gao | Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLH | iclr-2025 | openreview |
| 2025 | Maximillian Chen | Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self | iclr-2025 | openreview |
| 2024 | Yongchao Zhou | DistillSpec: Improving Speculative Decoding via Knowledge Distillation | iclr-2024 | openreview |
| 2024 | Ayan Sengupta | A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distill | iclr-2024 | openreview |
| 2024 | Akari Asai | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | iclr-2024 | openreview |
| 2024 | Sijia Chen | Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models | iclr-2024 | openreview |
