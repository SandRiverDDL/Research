# Cross-check Report 2026-06-11

> 给 cc + chy 双看的状态文件。
> 27 张 L1 卡的逐张扫描 + 漏候选搜索结果。
> 之后 new session 接手 #9 / #10 / #11 看这份。

## 谁看 / 怎么用

- **cc 看**：恢复 cross-check context，决定 #10 移哪两张、#9 哪两张是真重复、#11 补什么 paper 填覆盖 gap
- **chy 看**：审 5 张 borderline 决定保留 / 改 scope，确认 #10 移出方案
- 不进 grep / 不进对比表，是流程档不是 paper 档

## 任务背景

第一轮 autoresearch 写出 27 张 L1 卡（24 写 + 3 旧迁移）。chy 怀疑搜索质量，sonnet 用 think hard 跑 cross-check，三 phase 输出。

## Phase 1: 27 张逐张 in-scope 判定

### scope 分类

| scope | 数量 | 卡片 |
|---|---|---|
| **in** | 20 | 24_distillm / 24_gkd / 24_minillm / 25_aligndistil / 25_bopd / 25_distillm-2 / 25_taid / 26_ar-opd / 26_global-token-filter / 26_gndpo / 26_hdpo / 26_internalize / 26_multi-rollout-peer / 26_on-policy-context-distill / 26_oprd / 26_rlcsd / 26_sgsd / 26_tgpo / 26_tip / 26_vicur |
| **borderline** | 5 | 23_lion / 24_spin / 25_pangu-embedded / 26_online-experiential / 26_surgical-distill |
| **off**（建议移出）| 2 | **25_deepseek-r1** / **26_rl-policy-distill** |

### off 详情（待 #10 处理）

| 卡 | 为什么 off |
|---|---|
| `25_deepseek-r1.md` | 是 RL 训练 recipe + offline SFT 蒸馏，不是 OPD 方法 paper。综述 must-read seed 直接灌入；decisions 字段 5 个 unknown 且 framing 错误 |
| `26_rl-policy-distill.md` | 自动驾驶 nuScenes 应用论文（cs.RO domain mismatch）；TL;DR 全英文；本应被 domain filter 过滤 |

### borderline 详情（待 chy 审）

| 卡 | 边界原因 | 建议 |
|---|---|---|
| `23_lion.md` | API-only 黑盒 adversarial SFT，无 white-box student rollout | 保留（早期 distillation baseline） |
| `24_spin.md` | self-play 无外部 teacher，preference 路径，非 teacher-student OPD | 保留（覆盖 gap：preference signal 几乎空白） |
| `25_pangu-embedded.md` | 系统报告：SFT 蒸馏阶段 offline teacher 数据，RL 阶段无 KL | 保留（recipe 类） |
| `26_online-experiential.md` | 重点是在线 experiential knowledge 提炼循环，OPD 是实现手段 | 保留 |
| `26_surgical-distill.md` | minimal-edit GT teacher 构造 (y⁺,y⁻) 做 BCO，preference 非 KL | 保留（覆盖 gap：preference signal） |

### lang 检查

仅 `26_rl-policy-distill.md` 是 en-dominant（待移出）。其余 26 张全 zh-dominant，模板约束守住。

### decisions quality

**suspicious 类**（方法已写清楚但字段全 unknown）：4 张已在 06-11 workflow 修复

| 卡 | 修后 |
|---|---|
| `26_global-token-filter` | rollout=student / signal=logit / iteration=one-shot / filter=trajectory-level |
| `26_multi-rollout-peer` | loss=reverse-kl / signal=logit / iteration=one-shot |
| `26_oprd` | rollout=student / loss=mse / signal=representation / iteration=one-shot |
| `25_taid` | rollout=offline / signal=logit（修正错误填值） |
| `26_internalize` | iteration=iterative / filter=entropy-gated |

## Phase 2: 漏的候选

cross-check 找到 4 张应该有但没写卡的关键 paper。**全部已补**。

| paper | arxiv_id | 已补 |
|---|---|---|
| OPSD (Self-Distilled Reasoner) | 2601.18734 | ✅ `26_opsd.md`（org=meta-ucla, conf=2） |
| Lightning OPD | 2604.13010 | ✅ `26_lightning-opd.md`（org=nvidia 确认，非 MIT） |
| REOPOLD（DistiLLM 作者第三代）| 2603.11137 | ✅ `26_reopold.md`（org=kaist-microsoft） |
| EOPD（Entropy-Aware OPD）| 2603.07079 | ✅ `26_eopd.md`（org=ibm） |

### 用户提到的三个目标的实际情况

| chy 怀疑 | 验证结果 |
|---|---|
| **THU OPD** | 多篇清华论文已在内（RLCSD / SGSD / FiRe-OPD / TS-OPSD），不缺 |
| **Revisiting OPD** | 未找到含 "Revisiting" + OPD 的论文。最接近 REOPOLD ("Relaxed")。**chy 待确认是否记错** |
| **NV Lightning OPD** | 找到了，作者邮箱 NVIDIA，affiliation NVIDIA（chy 原判断对，cross-check 之前误判 MIT） |

## Phase 3: 覆盖度 gap（待 #11 补）

### signal 轴

| signal | 数量 | 状态 |
|---|---|---|
| logit | 15 | 过载 |
| outcome / verifier-score | 2 | 弱 |
| **preference** | 0-1 | **gap** |
| **PRM step-level verifier** | 0 | **gap** |
| representation（OPRD 单一） | 1 | 弱 |

### rollout 轴

| rollout source | 数量 | 状态 |
|---|---|---|
| student-only | 12 | 过载 |
| mixed | 4 | OK |
| offline | 2（TAID + Lightning OPD）| 弱但已补一篇 |
| **EMA teacher / self-evolving** | 0 | **gap** |

### filter 轴

| filter | 数量 | 状态 |
|---|---|---|
| none | 7 | OK |
| verifier-pass | 2 | OK |
| trajectory-level | 1（FiRe-OPD）| 弱 |
| score-threshold（TIP 单一）| 1 | 弱 |
| entropy-gated | 1（EOPD 已补）| 弱 |
| **hardness/curriculum** | 2-4（含 borderline）| 弱 |

### iteration 轴

分布均匀（one-shot 7 / iterative 5 / continuous 5），无 gap。

## Phase 4: 待 chy 审的开放问题

1. **#9 ye-2026-policy / ye-2026-online 是否真重复**：opus cross-check 老 report 提过疑似 dedup 漏。两张卡片 arxiv_id / 标题 / 第一作者比对建议 new session 跑（low effort）
2. **#10 移出方案**：建议把 `25_deepseek-r1.md` + `26_rl-policy-distill.md` 移到 `_meta/off-scope/` 目录，保留文件不删（保 git history），加 `scope: off` tag 让 Dataview 排除
3. **borderline 5 张**：建议全保留，但 chy 自己 verify 一遍 `verified: a → s` 升级
4. **#11 search query 建议**：
   - `"preference distillation"` `"DPO distillation"` `"step-level reward distillation"`
   - `"EMA teacher distillation"` `"self-evolving teacher"`
   - `"curriculum distillation"` `"hard example mining distillation"`
5. **覆盖 gap 补完后再 cross-check 一轮**——补 paper 进来覆盖度变了，需要重看 axes 分布

## 下一 session 入口

> "继续 OPD autoresearch。读 _meta/STATE.md + _meta/SEARCH-METHOD.md + _meta/CROSS-CHECK-2026-06-11.md 恢复 context。先做 #10 scope 清理（机械），再做 #8 改 CLAUDE.md，然后 #9 dedup 验证，#7 写 survey queue。#11 / #3 单独再开一轮。"
