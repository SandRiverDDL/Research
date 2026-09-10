# DeepSeek-V4 Claims and Gaps

```yaml
---
source_id: deepseek-v4
section_type: claims-and-gaps
depth: working
confidence: medium
need_expert_review: false
---
```

## 问题

DeepSeek-V4 哪些 claim 值得信？哪些证据不足？哪些 missing details 会影响研究判断？

## 可信 claim

- Model scale 和 high-level architecture/training setup 比较具体：1.6T/49B V4-Pro、284B/13B V4-Flash、32T+ pretraining tokens、MoE、CSA/HCA、mHC、Muon、long-context schedule。[1, 24-26]
- Pretraining data categories 有 useful high-level disclosure：math、code、web、long documents、multilingual data，以及 mid-training 中的 agentic data。[24]
- Post-training pipeline 从 mixed RL 转向 OPD 是明确陈述。[28-34]
- Full-vocabulary OPD 需要大量工程支撑；报告给了足够 implementation detail，可以认为这是实际 system investment。[33-35]
- Eval suite 覆盖面广，并包含 hard/verifier-style tasks，不只是 preference 或 static QA。[36-38]

## 暂不信的 claim

- GRM 描述太高层，不能直接视为可复现；“actor natively functions as GRM” 需要 procedure。[29-30]
- Internal evals 和 internal framework choices 是有用信号，但 public evidence 较弱。[38-44]
- “1M context” 能力需要按 task 解释；MRCR 在 128K 后的 degradation 表明不是所有 long-context tasks 都同等解决。[40]
- Developer survey numbers 说明 product fit，但不能和 public model benchmarks 直接比较。[44]

## 关键缺失信息

- Exact pretraining data mixture proportions 和 filtering thresholds。
- Specialist model domains、expert count details、OPD teacher weighting。
- GRM training data、loss、calibration 和 failure modes。
- DSec sandbox 和 agentic evaluation tasks 的 public reproducibility。
- Long-context 和 agentic claims 的 external replication。

## 值得内化

- 最强 insight 是 system coupling：architecture 降低 long-context cost，进而支持 persistent reasoning/tool traces、million-token rollouts 和 OPD/RL 进入新 regime。
- Reasoning modes 应被看作训练出的 product modes，带有不同 length/context incentives，而不是 prompt labels。
- 用 OPD consolidating specialists 是另一种 philosophy：不是让一个 mixed RL 直接解决所有 domain。

## 随查随用

- CSA/HCA dimensions、MoE expert counts、optimizer coefficients、benchmark numbers、表格级 closed-model comparisons。
- 所有 API/comparison numbers against closed models。

## 证据锚点

- 1: abstract 和 headline claims。
- 24-26: pretraining data 和 model/training setup。
- 28-35: post-training pipeline、OPD 和 infrastructure。
- 36-44: evaluation setup 和 results。
- 44-45: limitations/future directions。
