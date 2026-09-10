# OPD 当前状态

> 只保存下次启动所需状态；任务路由见项目 `AGENTS.md`。

## 当前流程

- 目标：形成可投顶会的 OPD 工作，并从经典机制和近期录用论文中学习 idea pattern。
- 现有 71 张 L1 cards 主要由自动流程生成，只作低可信 recall，不视为已验证的领域积累或继续选择 OPD 的理由。
- 默认检索：全部 cards → 10–20 张相关 card → 3–8 篇原文。
- 新卡使用极简 YAML 和无标题正文；正文按“一句话 / Failure mode / 核心做法 / 方法增量 / 关键证据与边界”组织，只有明确因果证据时才增加“瓶颈（作者诊断）”。旧卡保持原样并由 registry 兼容。
- Synthesis 按 failure mode 分 Markdown、以决策点为表格列；新卡默认只加表格行，只有研究结论变化时才改文字判断。
- `_meta/`、旧 queue 和 generated files 是历史材料，不再维护。

```bash
cd /Users/chy/Research/opd
scripts/autoresearch.py status
scripts/autoresearch.py validate
scripts/autoresearch.py lookup <paper-id-or-url>
```

## 近期研究入口

- `synthesis/agentic-opd.md`：agentic OPD 的单页索引，按 rollout depth、prefix reliability、loss allocation、action boundary 与 termination stability 导航；TurnOPD 已精读并写入 `notes/26_turnopd.md`。
- `synthesis/arxiv-opd-120d-radar.md`：2026-03-31 至 2026-07-29 的 103 篇 LLM/agent/MLLM OPD arXiv 高召回候选；32 篇重点一句话。
- `synthesis/arxiv-opd-120d-synthesis.md`：近 120 天热点、瓶颈、idea pattern 与可信度边界；已记录 token-selection 效率口径和 privileged-information 三类混淆。
- `synthesis/opd-method-lineage-report.md`
- `synthesis/failure-modes/teacher-pattern-mismatch.md`：首份 failure-mode 综合；覆盖 pair/data/local-support/trajectory 四层 mismatch 与 20 篇核心方法。
- `synthesis/opd-method-lineage/04-idea-hooks.md`
- `synthesis/opd-method-lineage/05-evidence-and-limits.md`

## 研究约束

- 实习期间可较方便使用 8–16 卡算力。
- 当前仍在入门阶段并依赖 autoresearch，需要优先选择短反馈周期、可先做小实验否证的方向。

## 用户偏好

- 输出简短、可快速扫描。
- Card 优先优化可读性、信息密度和学习 research taste 的效率。
- 不因 schema 改动批量重写旧卡。
- 默认执行最小规则，不主动扩展系统。

## 当前选题评估：2026-09-05

- 用户要求独立重判 OPD research gap、潜在蓝海与初学者适合的方向；旧方向结论仅作参考，不作前提。
- 用户确认首篇目标为 2–3 个月完成投稿，优先反馈快、工程可控；以可持续多篇产出为取向。
- 本轮是选题分析，尚未确认具体研究方向或授权启动实验。
- 已补查 2026 年 8 月原论文，重点包括 OPSA（2608.31046）、OPD generalization（2608.16647）、TIDE（2608.09836）、CROP（2608.13387）与工具调用漂移 v5（2607.07050）。助手倾向优先验证短轨迹、可程序评测的工具决策语义保真；这是尚未实验、尚未被用户采纳的候选判断。

## 进行中：2026 三会 OPD 抽卡

- 本轮按 `doc/card-acceptance.md` 保守处理，只抽“直接 OPD”；该准入规则当前不含 ACL，因此 ACL main / Findings 未写卡。
- ICML 2026 direct OPD 已新增 5 张：FA-OPD、Decomposed OPD、Video-OPD、SDFT、HPD；EOPD、OPSD 已有旧卡，不重复写。另新增 TurnOPD 卡；全库现为 77 张，validate 为 0 errors / 0 warnings。
- 上述 5 张已按新正文结构重写：Failure mode 必写、瓶颈可选、Pattern 删除。
- GenRe² 的主贡献是 decoding-based regression RL，OPD 只是辅助 credit-assignment 组件，本轮排除。
- ICML 高相关机制：On-policy Expert Corrections、SDPO、SRPO、TMS。
- ACL main 高相关机制：BEPA、DGPO、CurioSFT、REDI；没有标题/摘要明确的标准 LLM OPD。
- ACL Findings direct OPD：Prefix OPD、COPSD、CORD、Veto；近邻包括 SmartAD、P-BRIDGE。
- 未决：OPD 高相关机制论文是否也写正式 L1 card，还是只在 synthesis 中记录；用户尚未确认。
