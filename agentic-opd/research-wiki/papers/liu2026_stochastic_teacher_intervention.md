---
type: paper
node_id: paper:liu2026_stochastic_teacher_intervention
title: "Stochastic Teacher Intervention for Agentic On-Policy Distillation"
authors: ["Junnan Liu", "Linhao Luo", "Zhijun Chen", "Qianren Mao", "Thuy-Trang Vu", "Gholamreza Haffari"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2610.10878"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-22T09:36:35Z
---

# Stochastic Teacher Intervention for Agentic On-Policy Distillation

## One-line thesis
【作者方法】STI-OPD 以分歧决定整轮 teacher 接管概率，用重要性加权保持固定上下文上的 reverse-KL 目标。

## Problem / Gap

【作者问题】student 的早期动作改变后续观察，使训练状态偏离 teacher 常见轨迹；固定日程或硬阈值接管又会限制探索。目标是自适应接管，并正确利用 teacher 生成 token。[§3](https://arxiv.org/html/2610.10878v1#S3)

## Method

【作者方法】每轮先生成完整 student proposal，以 sampled-token 的 k3 估计量 r−1−log r 估计 reverse-KL，按 response 长度取均值得分 s，再以 s/(1+s) 的概率让 teacher 从同一 history 重新生成整轮 response。丢弃的 proposal 不进入 history 或训练 buffer。[§3.2，Eqs.5–8](https://arxiv.org/html/2610.10878v1#S3.SS2)

保留 student token 使用 sampled reverse-KL；teacher token 乘 student／teacher 概率比。作者明确：校正仅针对固定 context 的 token 采样，不校正接管决策或接管诱导的 history 分布。[§3.3，Eqs.9–11](https://arxiv.org/html/2610.10878v1#S3.SS3)

## Key Results

【作者报告，未复现】Qwen3-1.7B student、4B teacher：ScienceWorld success 为 27.5±0.5%，FutureBridge 22.2±0.4%、普通 OPD 17.1±0.5%；ALFWorld Look 为 73.7±0.5%，FutureBridge 66.5±0.6%。不把子任务分数写作 ALFWorld 总平均。[Table 2](https://arxiv.org/html/2610.10878v1#S4.T2)

相同 teacher 接管次数预算下，ScienceWorld 为 24.2±0.4% 对 FutureBridge 18.7±0.4%。[Table 8](https://arxiv.org/html/2610.10878v1#A3.T8)

## Assumptions

【设定与阅读范围】首发 2026-10-07，读取 v1 §§3–4、主要结果表、接管预算说明和 Appendix D。Qwen3-0.6B/1.7B 为 student，4B 为主 teacher，32B 为扩展 teacher；覆盖 tool-integrated reasoning、ALFWorld、ScienceWorld。推理时仅 student，需 teacher token 概率及共同支持。[§4.1](https://arxiv.org/html/2610.10878v1#S4.SS1) 完整元数据：[arXiv](https://arxiv.org/abs/2610.10878)。

## Limitations / Failure Modes

【作者边界】采样 API teacher 不适用；整轮重新生成会为局部分歧支付整轮 teacher 成本。分歧不是任务错误或 teacher 可靠性的保证，且重要性权重不恢复原 student 的状态访问分布。[§3.3、Appendix D](https://arxiv.org/html/2610.10878v1#A4)

【成本口径】Appendix C.4 匹配的是 teacher 接管次数，不是全部 teacher forward tokens、生成 tokens 或总 GPU 时间；主文另报告 wall-clock Pareto 图。[§4.4、Appendix C.4](https://arxiv.org/html/2610.10878v1#A3.SS4)

## Reusable Ingredients

【解释】利用已生成 proposal 估计分歧、平滑随机接管、区分 token 采样校正与 history 分布改变；不能将重要性权重描述为完整轨迹去偏。[§§3.2–3.3](https://arxiv.org/html/2610.10878v1#S3.SS3)

## Open Questions

【开放问题】在相同总 teacher tokens／wall-clock 下接管收益是否稳定？低分歧但有害的 student 决策，以及高分歧但有效的替代策略，分别会如何被处理？

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

【直接相关】覆盖 [G1](../gap_map.md#g1) 的错误状态处理和 [G2](../gap_map.md#g2) 的纠错／探索分配；是随机 teacher intervention 的直接 baseline。已比较 Guided、TCOD、SAGE、FutureBridge，但本次未发现其直接比较 DASH／ATOD 的证据。[§4.1](https://arxiv.org/html/2610.10878v1#S4.SS1)

## Abstract (original)

> On-policy distillation (OPD) efficiently transfers capabilities from a stronger teacher to a student language model through dense token-level …

