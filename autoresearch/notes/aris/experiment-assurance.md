# ARIS：experiment 与 claim assurance

> 返回 [overview.md](overview.md)。核心问题不是“有没有 reviewer”，而是 raw evidence 如何一路约束最终 claim。

## Assurance chain

```text
code / configs / raw result files
  → experiment-audit
  → result-to-claim
  → manuscript numbers and wording
  → paper-claim-audit
  → citation-audit
  → submission gate
```

**事实**：技术报告把 `experiment-audit → result-to-claim → paper-claim-audit` 称为三段式 audit cascade，另以 citation lookup/audit 检查 bibliography 与上下文；报告同时明确说它是 advisory safety net，不是 formal verification。[技术报告 §3, pp. 7–9；§5.2, p. 13](../../papers/aris-2605.03042.pdf)

## 1. `experiment-audit`：先问结果文件是否可信

**事实**：executor 收集 code/config/result artifacts，交给 reviewer 检查：

- ground-truth provenance；
- score normalization；
- result files 是否真实存在；
- dead code / 未执行路径；
- claim scope 是否超出实验；
- evaluation 是 real ground truth、synthetic proxy 还是其他类型。

输出 PASS/WARN/FAIL、action items 与 claim impact。skill 在 `/research-pipeline` 中默认 advisory，并会被 `result-to-claim` 和 paper writing 读取。[experiment-audit source](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/experiment-audit/SKILL.md)

**判断**：它能抓“跑了一个自归一化 proxy 却声称真实提升”“结果路径不存在”“metric code 根本没执行”等 autoresearch 常见 integrity failures；但 reviewer 若只看摘要/挑选后的文件，仍可能漏掉 seed selection、dataset leakage 或环境污染。

## 2. `result-to-claim`：将 empirical result 限制成可说的话

**事实**：skill 先收集结果，做 deterministic evidence pre-check，再让 Codex reviewer 判断 hypothesis `yes | partial | no`、confidence 与 reasoning。若有 experiment audit，会降低/阻止不诚实 claim；随后更新 research wiki 的 experiment/idea/claim edges。新版本强调 reviewer 不可达时诚实停止，而不是 executor 自判通过。[result-to-claim source](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/result-to-claim/SKILL.md)

**重要事实**：wiki 把两个轴分开：claim `status` 是 proof axis，只能由 proof-checker 写；实验 `supports/invalidates` 是 empirical axis，以 edges 表示。实验不能把 theorem 直接改成 “verified”。[research-wiki Hook 3–4](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-wiki/SKILL.md)

**判断**：这是比普通 agent memory 更严谨的 claim ledger 语义。仍需给每个 claim 保留 raw artifact path、config hash、seed aggregation rule；否则 ledger 只记 verdict，不足以复核。

## 3. `paper-claim-audit`：零上下文核对论文数字

**事实**：executor 先收集 manuscript 与 raw results，fresh reviewer 在新 thread 中逐 claim 检查。目标包括 rounding inflation、best-seed cherry-picking、config mismatch、delta arithmetic、scope overclaim；输出 PASS/WARN/FAIL 与 machine-readable submission artifact，记录 audited input hashes 和 thread independence。[paper-claim-audit source](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/paper-claim-audit/SKILL.md)

**解释**：fresh/zero-context 的意义是 reviewer 不继承“这个方法应该成功”的生成叙事，只比较 paper claim 与 evidence。input hashes 则避免审计后再改文件却沿用旧 verdict。

## 4. `citation-audit`：存在不等于引用恰当

**事实**：skill 从 `.bib` 和 citing context 提取 pairs，借 DBLP/arXiv/CrossRef 等核验 existence/metadata，再由 fresh cross-model reviewer 判断上下文是否真的被该论文支持；可报告 REMOVE/REPLACE/soften 与 uncited entries，并产生带 input hashes 的 audit artifact。[citation-audit source](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/citation-audit/SKILL.md)

**边界**：metadata API 能确定“这篇论文存在/作者年份对”，无法确定某句 scientific entailment；后者仍是 LLM reading。paywall、版本差异、同名论文与引用上下文截断仍会误判。

## 5. Executor / reviewer 分离

**事实**：默认推荐不同 model family：executor 生成/修改，reviewer 在 fresh thread 审计；review verdict 带 trace/thread ID。ARIS 并不强制所有部署都跨 family，但 submission assurance contract 要求 reviewer independence，配置同 family 应失败或降级告警。[reviewer-routing contract](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/shared-references/reviewer-routing.md)；[技术报告 §3, pp. 7–9](../../papers/aris-2605.03042.pdf)

**判断**：cross-family 比 self-review 好的理由是降低相关错误和叙事锚定，不是 reviewer 获得了 ground truth。Claude executor + GPT reviewer 仍共享训练语料、论文写作规范与 LLM 偏好，也可能共同漏掉领域性错误。

## 6. 同源盲区仍在哪里

- **Metric contract 同源**：如果 executor/reviewer 都接受了错误 metric，后续所有 audit 只能保证数字忠实于错误目标。
- **Artifact selection 同源**：executor 决定交哪些 raw files；缺少不可篡改 run manifest 时，reviewer 看不到未提交的失败 seeds。
- **Reviewer taste reward hacking**：auto-review 的停止分数来自同一 reviewer family/contract，可能驱动 narrative optimization。
- **Code execution truth gap**：LLM 阅读代码不是 dynamic verification；环境、dependency、data split、nondeterminism 可能只在复跑中出现。
- **No independent benchmark**：目前没有外部团队系统比较 cascade 对 integrity error 的 recall/precision。

## 7. 个人采用时应增加的硬 gate

**判断**：把 ARIS 当 “it can drive, never acquit”：

1. run manifest 自动记录 git SHA、command、env lock、dataset hash、seed、stdout/stderr 与所有结果文件；
2. claim ledger 每条 claim 链到不可变 raw artifact 与 aggregation script；
3. metric/benchmark contract 在实验前由人确认，review loop 不得自行换主 metric；
4. 至少一个关键结果由独立进程/环境复跑，而非只让 reviewer 阅读；
5. LLM reviewer 只做 filter/红旗，不把分数作为主优化目标；
6. submission 前由人抽查 high-impact claims 与 citations。

这样 ARIS 才是 assurance layer；否则只是更复杂的自我评审。

