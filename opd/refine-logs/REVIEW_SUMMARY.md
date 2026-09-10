# Review Summary

**Problem**：用长程 agent 轨迹中首次关键工具/推理分歧的位置，替代整题 50% pass-rate 作为 OPD prompt curriculum 信号，并在 post-fork 监督失真前停止。
**Initial Approach**：越早分歧越优先；分歧后固定若干 token 截断；分歧延后时更新 prompt 概率。
**Date**：2026-08-24
**Rounds**：3 / 5
**Final Score**：8.4 / 10
**Final Verdict**：REVISE（概念上 pilot-ready；缺真实实验）

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token 或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

## Round-by-Round Resolution Log

| Round | Main Reviewer Concerns | Simplified / Modernized | Solved? | Remaining Risk |
|---|---|---|---|---|
| 1 | critical/repairable 不可辨识；earlier-first 无证据；truncation 撞 Prune-OPD | 收成因果 prompt acquisition；删独立 truncation claim；删默认 earliness | partial | branch probe 仍像 oracle，成本未冻结 |
| 2 | branch semantics、censoring noise、scalar cost 不精确 | 固定 teacher-continuation-relative branch value；two-hit confirmation；wall-clock 为唯一 scalar cost | yes | 仍需增量预测和全成本证据 |
| 3 | `D<d<Q` 状态未定义；probe baseline 可能掩盖成本 | 补全 two-hit transition；拆 sampler attribution 与 no-probe end-to-end utility | yes | 只剩 empirical pilot |

## Overall Evolution

- 原来的“raw tool disagreement 越早越好”改成“teacher alternative action 在 paired terminal continuation 中确实改变 outcome”。
- 默认 sampler 不再硬编码 earliness；它使用 confirmed first-fork movement，并把 earliness 保留为预注册 hypothesis。
- 固定 token `+L` 截断改成 action-boundary mask，而且不再作为 novelty。
- 不训练 selector/critic，不改变 OPD objective，保持一篇论文一个主贡献。
- 第三轮后 reviewer 明确认为无须继续概念扩张；停止在 8.4 是因为缺实验，不是因为还需要写更多模块。

## Final Status

- **Anchor status**：preserved；earliness 被 operationally 降为待验证假设。
- **Focus status**：tight。
- **Modernity status**：appropriately frontier-aware。
- **Strongest part**：action-local paired terminal advantage 与 repeated prompt acquisition 的 novelty boundary 已清晰。
- **Remaining weakness**：尚未证明比 ReOrder-style reliability 多解释 one-update gain，也未证明 probe 开销能在 wall-clock 上回本。

