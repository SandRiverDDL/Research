---
type: paper
node_id: paper:yuan2026_actionopd_distilling_decisions
title: "ActionOPD: Distilling Decisions, Not Tokens"
authors: ["Huining Yuan", "Xiangmin Yi", "Zelai Xu", "Zixu Wang", "Xinlei Chen", "Xiao-Ping Zhang", "Yu Wang", "Chao Yu"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2610.19820"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-22T09:36:35Z
---

# ActionOPD: Distilling Decisions, Not Tokens

## One-line thesis
【作者方法】ActionOPD 用 student 候选与黑盒 teacher 动作的语义一致性作为策略优化奖励，无需 teacher token 概率。

## Problem / Gap

【作者问题】offline imitation 有状态分布错配；token OPD 需要 teacher token 概率和兼容 tokenizer。作者将监督单位改成同状态下的语义动作，而非复现 teacher reasoning。[§§1–2](https://arxiv.org/html/2610.19820v1#S2)

## Method

【作者方法】每个状态请求 K=3 个 teacher response，再采 N=4 个 student 候选；程序检查工具名和规范化参数，冻结 LLM 判剩余语义差异。有效且首次匹配奖 1，额外匹配加频次 bonus，非法动作 −1；实用奖励已改变最初的 teacher-action likelihood 目标。[§§2.1–2.2，Eqs.2–6](https://arxiv.org/html/2610.19820v1#S2.SS2)

执行奖励最高的一个候选，保留组内全部候选做 group-relative、PPO-style 更新；同奖励组不训练但可推进环境。作者明确 argmax commit 改变状态访问分布，归一化／mask／clipping 后也不是原始梯度的无偏估计。[§2.3，Eqs.7–9](https://arxiv.org/html/2610.19820v1#S2.SS3)

## Key Results

【作者报告，未复现】Qwen3-4B/8B 配合两种外部 teacher，四个 OOD benchmark 的宏平均较 Base 提高 3.3–6.9 pp；此平均混合 BFCL accuracy、ToolSandbox similarity、AppWorld TGC 和 Tau pass¹，不是统一成功率。[Table 1、§3.1](https://arxiv.org/html/2610.19820v1#S3.T1)

Tau held-out 平均 pass¹/pass⁴：ActionOPD 40.0/14.2%，token OPD 39.6/17.5%，KD 37.5/19.2%；ActionOPD 并非每种可靠性指标都更优。pass⁴ 为四次全成功，不是 best-of-four。[Table 2](https://arxiv.org/html/2610.19820v1#S3.T2)

## Assumptions

【设定与阅读范围】首发 2026-10-14，读取 v1 §2、§3 设置／主表／消融、§5、附录 A.3/B.4。跨域实验在 6,697 个 AWM/EnvScaler 任务上训练，teacher 为 Qwen3.7-Flash／DeepSeek-V4-Flash；Tau 蒸馏比较另用 Qwen3-32B。标准分支 teacher/student 同看公开 context，不需 teacher logits；要有动作解析和可信语义 matcher。[§3.1、Appendix A.3](https://arxiv.org/html/2610.19820v1#A1.SS3) 完整元数据：[arXiv](https://arxiv.org/abs/2610.19820)。

## Limitations / Failure Modes

【作者边界】动作一致不保证正确，matcher 可误判，固定小样本在多种合理动作间可能缺乏重叠；增加 K/N 的覆盖收益和成本未在该困难情形验证。[§5](https://arxiv.org/html/2610.19820v1#S5)

【预算边界】每状态多次生成、匹配和选动作形成额外依赖。Tau 比较虽同 task starts/steps，但 KD 的成功过滤、OPD 的轨迹数量及 teacher scoring 与 ActionOPD 的 state groups 不同，未等化总 tokens、teacher queries 或 compute。[Appendix B.4](https://arxiv.org/html/2610.19820v1#A2.SS4)

## Reusable Ingredients

【解释】对 teacher 动作样本的匹配频数进行软奖励；同状态候选建立局部 baseline；将 teacher decision 与 student 自己的 token realization 分开。采样重试及 cache 会使实际样本偏离理想独立采样，应保留该实现边界。[§2、Appendix A.3](https://arxiv.org/html/2610.19820v1#A1.SS3)

## Open Questions

【开放问题】按总 teacher 调用、matcher 调用和 wall-clock 匹配后，动作语义奖励是否优于 token OPD？在多种有效路径并存时，如何避免“没采到匹配动作”产生错误负信号？

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

【直接相关】外部 black-box teacher 的 action-level OPD，直接覆盖历史 [G3](../gap_map.md#g3) 的接口前提，也与 [G2](../gap_map.md#g2) 的有效替代行为保留有关。Self-ActionOPD 是额外分支，不作为本项目外部 teacher 主证据；不因其存在排除主方法。

## Abstract (original)

> Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a …

