# 通用 Autoresearch 流程

> 从 OPD 项目 dogfood 提炼出的 workspace 级流程。当前主入口已经迁入 `research-codex-workflow` skill 的 literature pipeline；本文件保留为历史说明和项目迁移参考。具体主题可以覆盖 card schema、taxonomy 和检索策略，但不要让用户记脚本或 `_meta/` 文件名。

## 目标

把调研流程做成自然语言入口：

- `找新的论文抽卡`
- `生成/修改总结报告`
- `围绕某个 idea 做 novelty-risk 检查`

Codex 负责选择项目内脚本、读取状态、维护中间产物和验证结果；人只看核心卡、候选论文、排除/旁支、报告。

## 可通用化的 OPD 经验

- **持久记忆**：每个主题至少有 `AGENTS.md`、`doc/memory/STATE.md`、`DECISIONS.md`、`OPEN-QUESTIONS.md`。
- **人读 / 机器产物分离**：`doc/`、`notes/`、`synthesis/` 给人读；`_meta/generated/`、`_meta/briefs/`、`_meta/raw/` 自动维护。
- **L1/L2 分层**：L1 是 research index；全面精读、主观判断、实验建议、投稿判断进入 L2 note 或 synthesis。
- **Bounded inputs**：写卡前先用 paper/survey brief，不默认把完整 PDF、完整综述或整批 references 塞进上下文。
- **No original brief, no card**：queue row 不是 card；survey mention 只是 recall signal；没有 original paper PDF/HTML brief，不写正式 L1 card。
- **Survey-only 错误恢复**：正常流程不应只基于 survey mention 写 formal card；如果发现历史 survey-only note/card，必须移出正式 notes 或标成 invalid，不计入 valid L1。
- **Queue / helper / validator**：自动维护候选、已写卡、排除、validation issues，避免人工 checklist 漂移。
- **Mechanical helper**：大批量抽卡时优先使用 `status`、`lookup`、`audit`、`pack`、`validate` 这类项目本地 helper；`research-map` / `idea-context` 在用户要求 synthesis、报告、idea，或累计到阈值后再更新。
- **Research map / idea context**：给 idea 生成压缩上下文，不拼接全部 cards；它们是 synthesis substrate，不是每张卡后的必需产物。
- **Report evidence policy**：报告不是 card 拼接；强结论必须能追到 card、brief、appendix、L2 note 或原文 anchor。
- **Fast recall audit**：默认做高精度检索、known-item recovery、cross-ref grep 和 cutoff 后增量，不做大而慢的系统检索。
- **Trust-gated triage**：按 novelty risk 和可信度排序，不按顶会标签盲读。S/A 抽卡；B 入队；C 排除或旁支。
- **Subagent policy**：普通写卡不使用 subagent；只把 subagent 用于固定词表分类、字段检查、短 synthesis 独立批评。

## 不应通用化的部分

- 具体主题的 decision axes。
- 具体主题的 failure-mode taxonomy。
- 某个 survey 的 cutoff 假设。
- 某个领域的标题正则或关键词。
- OPD-specific validator 规则，例如 OPD 的 identity 禁词和六字段 vocab。

## 需要项目配置化的部分

每个新主题应定义：

- card schema：L1 必填字段和 body section。
- controlled vocab：failure modes / lifecycle roles / decision axes。
- seed sources：survey、known anchor papers、benchmark pages。
- triage policy：哪些论文必须抽卡，哪些只进 novelty-risk queue。
- triage override config：项目本地规则应放配置文件，例如 `doc/triage-rules.json`，不要硬编码进脚本。
- report templates：方法谱系、证据可信度、open questions、idea hooks。

## 成熟项目高吞吐模式

当一个主题预计当天就要抽几十到上百张卡，可以直接采用 OPD 的成熟流水线，不必走轻量启动：

1. 复制脚本结构和项目配置。
2. 替换 `doc/triage-rules.json`、card template、taxonomy、decision axes。
3. 批量生成 briefs。
4. 用项目本地 `pack --limit 3/5` 准备 bounded inputs。
5. 每批写卡后跑 `validate`，必要时再跑 `status` / `audit`。
6. 每 10-20 张卡，或准备报告/idea 时再刷新或读取 `research-map` / `idea-context`。

不要在每张卡后重建 research-map / idea-context。

## 报告优先级

报告是跨论文判断，不是逐篇摘要。默认回答：

- 当前子领域的核心矛盾。
- 方法谱系和主要分叉。
- 决策轴如何改变问题定义。
- failure mode 到方法族的映射。
- 哪些是 historical anchor、strong baseline、hygiene baseline、frontier candidate、低可信 novelty-risk。
- 关键 tension / contradiction。
- open questions / idea hooks。
- Evidence used 和 limits。

## 新主题启动最小步骤

1. 建主题目录和 `AGENTS.md`。
2. 写 `doc/memory/STATE.md`，只放下一轮启动必须读的内容。
3. 写 topic scope：哪些论文进主线，哪些只做背景。
4. 收 5-10 个 seed surveys / anchor papers。
5. 写 5-10 张 L1 cards，验证 schema 是否够用。
6. 生成第一版 synthesis / crosscut report。
7. 如果预计超过 10-15 张卡，先引入最小 validator / brief scaffold，再继续批量抽卡。
