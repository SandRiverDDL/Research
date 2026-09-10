# Schema v2 设计判断 — Handoff for Max Think

> compact 后给 max think 的单文件输入。读完这一份就够，不需要其他 context。
> **任务**：判断下面提出的 schema v2 设计是否合理；逐条回答末尾 4 个问题。

## 一句话背景

OPD 文献调研，已写 31 张 L1 卡（每张 30-50 行 markdown）。最近发现腾讯 song-2026 综述（arxiv 2604.00626）reference 132 篇 arxiv id，覆盖远超我们手写卡片，且作者已经把每篇方法的"核心创新点"在综述正文里精确定位了。

**核心矛盾**：
- 老 schema 卡片每张 25-30k token 写出来，内容大部分是把综述已经讲过的东西用中文重写一遍
- 综述本身是英文 + LaTeX-渲染 markdown，"晦涩难懂"，chy 想要中文 + 可 grep 的形式
- 但又不想浪费 token 重抄综述

## 提议的新方向

**只写综述给不了的东西，其他全部 pointer 化**。

卡片的核心价值是：(a) decisions dict 能 grep；(b) survey_ref 一秒跳回综述对应 section；(c) 中文一句话定位。**不**是重新讲方法原理（综述已经做了）。

## 老 schema（v1，现行）

```yaml
---
title / authors / org / year / venue / arxiv_id
confidence / open_source / verified
decisions: {rollout/loss/signal/iteration/filter/extra}
---

> **TL;DR**: [中文 1-2 句]

## Core Idea
[中文 3-5 句解释方法]

## What's Actually New
[vs 前作的 1-3 段对比]

## Method
[公式 + 实验 setup + 一段中文]

## Verdict
- 升 L2？yes/no
- 理由：...

## Evidence
- "数字 X" 来自 §Y
- ...
```

行数：30-50 行 / 卡。token：25-30k / 卡（含读 PDF）。

## 新 schema（v2，待评估）

```yaml
---
# frontmatter 不变（org/year/decisions/...），新增一行：
survey_ref: "§3.2 / Table 2 row 'GKD'"   # ← 在 song-2026 综述里的位置
---

> **一句话**：[综述对该方法的定位，中文，≤30 字]

## 核心创新
[**唯一**真正新的那个东西，1-3 句中文。综述哪个 section 把它单独拎出来讲，就抄那个点。]

## 核心机制
[公式或伪代码 + 一句中文解释。综述给的公式直接搬，不重写。]

## 在 OPD 谱系里的位置
- 上游：[综述里说它继承 / 改进了哪篇]
- 下游：[哪些后续方法在它基础上做（如有）]
- 替代品：[同 niche 的竞争方法]

## 数字（可选，仅当综述报了关键对比）
- [一两个 headline number，标 §页码]
```

行数：10-15 行 / 卡。token：~1k / 卡（不读 PDF，只 grep 综述对应 section）。

## 重写流程

对每张卡：
1. **grep 综述**：用 paper title / first_author 在 `~/.arxiv-mcp-storage/2604.00626.md` 里找，抓周围 ±500 字
2. **定位 section**：综述把它放在哪节（§3.x divergence / §4.x signal / §5.x stability）
3. **抽核心创新**：综述讨论该方法时单独给的那一两句"区别于前作的点"，翻译成中文
4. **抽核心机制**：综述里的公式 / 伪代码块直接搬
5. **填谱系位置**：综述里 "X is a variant of Y" / "X improves over Z" → 直接抄

整个过程**纯文本搬运 + 翻译**，不需要重新 reasoning 论文方法。

## Pilot 对照：GKD（24_gkd.md）

### 综述里出现 GKD 的三处片段（实际 grep 结果）

**§Introduction（char ~8442）**：
> GKD (Agarwal et al., 2024), alongside the concurrent MiniLLM (Gu et al., 2024), brought on-policy distillation into the LLM era in mid-2023, and in less than two years the literature has expanded to over one hundred papers spanning divergence design, reward-guided optimization, self-play, multi-teacher debate, agentic trajectory distillation, and cross-modal transfer.

**§Taxonomy of relaxations（char ~22228）**：
> Seq-KD (Kim and Rush, 2016) relaxes assumption (2) by operating at the sequence level but retains the static data assumption. **GKD (Agarwal et al., 2024) relaxes assumption (4) by training on student-generated sequences.** DSKD (Zhang et al., 2025b) relaxes assumption (1) through dual-space alignment. G-OPD (Yang et al., 2026d) relaxes assumptions (2)–(4) simultaneously...

**§3.x Mixture parameterization（char ~31166）**：
> **GKD (Agarwal et al., 2024) defines π_mix = λ·p_θ + (1−λ)·p_data** as an explicit interpolation, and is agnostic to D_f, empirically testing Forward KL, Reverse KL, and JSD. Setting λ → 1 makes GKD pure on-policy.

### 老卡（v1）— `notes/24_gkd.md` 现状

```markdown
> **TL;DR**: 让 student 自己采样序列、teacher 在这些 on-policy rollout 上给 token-level 概率作为标签，可在 forward-KL / reverse-KL / JSD(β) 之间任选 divergence；相对 supervised KD 在 XSum / WMT / GSM8K 上把 student 提升 2.1× / 1.7× / 1.9×。

## Core Idea
把 auto-regressive KD 框成 interactive-expert imitation learning：用 student 自己 rollout 解决 train-inference distribution mismatch（exposure bias），teacher 只提供 token-level logits 作 expert label。GKD 把 student data fraction λ ∈ [0,1] 与 divergence 𝒟（forward-KL / reverse-KL / JSD(β)）解耦成两个独立超参，不 backprop 通过采样过程，所以比 MiniLLM 的 policy gradient 稳定。

## What's Actually New
vs. MiniLLM (Gu et al. 2023, 同期)：MiniLLM 用 reverse-KL + policy gradient 还要一堆 stabilizing tricks...vs. ImitKD (Lin 2020)：ImitKD 只到 λ=0.5 mix、固定 forward-KL...

## Method
GKD 损失：L = (1−λ)·E[𝒟(p_T‖p_S)] + λ·E_{y~p_S}[𝒟(p_T‖p_S)]，每 step 以概率 λ 用 student rollout 否则用 ground-truth。Algorithm 1 是 mixture sampling。Sweep：λ∈{0,0.5,1}、𝒟∈{forward-KL, reverse-KL, JSD(0.1/0.5/0.9)}。Models：T5-small/base/large/XL...Tasks：XSum (ROUGE-2)、WMT en-de (BLEU)、GSM8K... 还做了 GKD + REINFORCE 的 RLAIF 实验。

## Verdict / Evidence ...
```

总计 49 行。

### 新卡（v2）— 草稿

```markdown
---
title: "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes"
authors: [Rishabh Agarwal, ...]
org: gdm
year: 2024
venue: iclr-2024
arxiv_id: 2306.13649
confidence: 1
open_source: unknown
verified: a
survey_ref: "§Intro / §Taxonomy assumption-4 / §Mixture-param"

decisions:
  rollout: student
  loss: forward-kl     # divergence-agnostic; default 用 forward-KL
  signal: logit
  iteration: continuous
  filter: none
  extra: none
---

> **一句话**：和 MiniLLM 同期把 OPD 带入 LLM 时代，用 mixture coefficient λ 把"on-policy 程度"和"divergence 选择"解耦。

## 核心创新
解除经典 KD 的 4 个隐含假设里的第 (4) 条 "off-policy training data"——student 自己 rollout、teacher 在 student 序列上提供标签。divergence 与 mixture rate 完全正交，可任选 forward-KL / reverse-KL / JSD。

## 核心机制
$$\pi_\text{mix} = \lambda \cdot p_\theta + (1-\lambda) \cdot p_\text{data}, \quad \mathcal{L} = \mathbb{E}_{y \sim \pi_\text{mix}}[\mathcal{D}_f(p_T \| p_S)]$$

λ→1 = 纯 on-policy；λ=0 退回 SeqKD。不 backprop through sampling，所以比 MiniLLM 的 policy gradient 稳定。

## 在 OPD 谱系里的位置
- 上游：Seq-KD (Kim & Rush 2016) — 只放松 sequence-level，不放松 data 来源
- 同期：MiniLLM (Gu 2024) — 同样 on-policy 但 reverse-KL + policy gradient
- 下游：DistiLLM (Ko 2024) / TAID (Miranda 2025) / G-OPD (Yang 2026) 等几乎所有 OPD 方法都以 GKD 为 baseline
```

总计 ~25 行（其中 frontmatter 占 17 行）。body 实际 8 行。

## 4 个判断题

请逐条回答：

### Q1：v2 schema 是否真的包含了"研究员后续会用到的所有信息"？
对比 v1 → v2，砍掉的部分（What's Actually New 详细对比 / Method 实验 setup / Verdict / Evidence trace）是否会让卡片**作为查询入口**失去价值？还是说这些细节本来就该 fall back 到综述 + 原 paper？

### Q2：survey_ref 字段的格式
当前提议是 `§3.2 / Table 2 row 'GKD'` 这种自由文本。是否应该改成结构化（比如 `survey_sections: [intro, §3.2, table-2]`）方便后续 grep？还是综述 section 引用本质就是自由文本，不必结构化？

### Q3：核心创新 vs 核心机制 是否会重复
v2 里这两节都很短，但概念上"创新点"和"机制公式"有耦合。GKD 例子里"创新=放松 data 来源到 student rollout，机制= π_mix 公式"，分两节 vs 合一节哪种更可读？

### Q4：v1 老卡如何处理
31 张老卡是删掉重写、还是改名 `*-v1.md` 留作 git history、还是直接 in-place edit？31 张里有些（cross-check 补的 4 张 + autoresearch 写的 ~10 张比较新的）信息密度本来就比综述还高（因为综述截稿前它们还没出来），是否需要保持 v1 格式不动，仅对"综述已详述"那 ~13 张做 v2 重写？

## 决定后的下一步

如果 v2 设计 ok：
1. 确认 v1 → v2 的处理策略（Q4 的答案）
2. 起一个 workflow，对需要重写的卡片 fan-out 跑（每张并发 1k token，~80 张总共 80k token 一轮搞完）
3. 跑完 chy 抽样审 5 张，没问题就 merge

## 其他可能被问到的 context（备查，不必读）

- 卡片目录：`~/Research/opd/notes/`
- 综述本体：`~/.arxiv-mcp-storage/2604.00626.md`（382k chars，含 reference）
- 老 schema 出处：`~/.claude-internal/skills/paper-summary/templates/L1-base.md`
- 老 schema 当时设计逻辑：`~/Research/opd/_meta/STATE.md` § "用户偏好（chy 在本次 session 拍板）"
- 综述 reference 里 132 个 arxiv id，与我们已写 31 张交集仅 13 张，差集 119 张（其中大部分是 backbone / borderline，不是都要写卡）
