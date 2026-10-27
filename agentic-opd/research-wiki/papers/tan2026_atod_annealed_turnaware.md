---
type: paper
node_id: paper:tan2026_atod_annealed_turnaware
title: "ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks"
authors: ["Qitai Tan", "Zefang Zong", "Mo Li", "Yipeng Shi", "Yang Li", "Peng Chen"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.27814"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks

## One-line thesis
【作者方法】ATOD 逐步降低 OPD、提高 GRPO 系数；T-DUR 结合 disagreement 与 student uncertainty，保留高分歧或高不确定 turn，衰减两者均低的 turn。

## Problem / Gap
【作者问题】多轮agent需要同时利用teacher的密集监督与环境奖励；固定OPD/RL混合未必适合整个训练过程，错误前缀也可能使teacher/student分歧不再反映纠错需要。[§1、§4](https://arxiv.org/html/2606.27814v6#S4)

## Method
【作者方法】student自采样完整轨迹，token advantage为退火后的teacher log-ratio与GRPO之和。T-DUR对每轮平均绝对log-ratio与sampled surprisal分别做轨迹内min–max，组合为`w=1−(1−d_norm)(1−h_norm)`；权重在[0,1]。训练前80步，OPD系数1→0.1，RL系数1→2；总训练150步。[Eq.8–15](https://arxiv.org/html/2606.27814v6#S4.SS1)、[C.3](https://arxiv.org/html/2606.27814v6#A3.SS3)

## Key Results
【作者报告，未复现】Table 1：1.7B student平均SR为71.58，OPD为64.91。不是每个单项均优于纯RL，也不能由平均轨迹长度推导统一的成本优势。Table 2及Fig.6包含组件与退火参数消融。[Table 1](https://arxiv.org/html/2606.27814v6#S4.T1)、[§5](https://arxiv.org/html/2606.27814v6#S5)、[C.4](https://arxiv.org/html/2606.27814v6#A3.SS4)

## Assumptions
【阅读层级，2026-10-19】已读v6正文§1–6、附录A–D、表1–4和图1–13，使用原HTML与内嵌SVG图，无PDF下载。未做代码审计或独立复现。实验使用Qwen3同家族teacher/student及可验证任务奖励；不代表跨family设置已验证。

## Limitations / Failure Modes
【作者承认】teacher质量、跨family与更广模态仍有限制。[附录A](https://arxiv.org/html/2606.27814v6#A1)

【本次解释】(1)权重改变轮间分配也改变总体OPD强度，缺均值／梯度规模匹配和权重打乱对照；(2)轨迹内min–max并非绝对teacher可靠性；(3)深轮统计条件于尚未结束的episode，存在任务组成变化；(4)主表缺跨训练seed误差，按更新步数比较不等于同总计算预算；(5)teacher logits先计算，降权不直接省teacher调用。上述是证据缺口，不是已证明的失败。[§4.3](https://arxiv.org/html/2606.27814v6#S4.SS3)、[C.3–C.6](https://arxiv.org/html/2606.27814v6#A3.SS3)

【避免误读】附录B证明proxy集中性质，并未证明任务价值；作者已明确绝对log-ratio不是无偏KL，不能将此指控为数学错误。T-DUR保留高分歧或高不确定turn，不应概括为高分歧降权。[附录B](https://arxiv.org/html/2606.27814v6#A2)

## Reusable Ingredients
【解释】OPD到reward学习的平滑过渡；turn级统计与同家族多规模设置。Student uncertainty只是可学习性候选proxy，二者不能等同。

【公开权重，2026-10-19核查】作者将三个环境各自GRPO训练的Qwen3-4B与Qwen3-30B-A3B共6个teacher发布在[TanQT24/ATOD_ckpt](https://huggingface.co/TanQT24/ATOD_ckpt)。0.6B/1.7B student使用4B teacher，4B student使用30B-A3B teacher。HF API核对仓库公开、未gated，6个目录均有safetensors/config/tokenizer；单个4B权重约8.82GB，30B-A3B约61.07GB（磁盘文件大小，非推理显存）。各子目录的`actor_hf/`可按模型卡加载，需匹配对应环境prompt/action格式。本次只核权重清单，未下载或运行模型。

## Open Questions
【开放问题】teacher监督究竟应传授行动、可辨识信念还是有助于估计任务梯度的信息？同预算下，T-DUR收益来自内容分配还是减弱teacher约束？对应[本次全文驱动选题](../../idea-stage/atod-ideas-2026-10-19.md)，全部未做pilot。

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
关联G2（纠错与自主探索）；本次2条主候选为[回看后验→在线belief](../ideas/bayes-consistent-hindsight-belief-distillation.md)、[teacher任务RL控制变量](../ideas/teacher-action-control-variate.md)，另有[事实视图靶点验证](../ideas/evidence-separated-decision-target.md)。推荐为assistant判断，用户尚未选定方向。全部15组去向、prior art和完整审阅输入见[报告](../../idea-stage/atod-ideas-2026-10-19.md)。

## Relevance to This Project
【本轮定位】方法／报告。对应 [G2](../gap_map.md#g2)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §4.2–4.3、§5.1、Table 1](https://arxiv.org/html/2606.27814v6)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2606.27814)。

> Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense …
