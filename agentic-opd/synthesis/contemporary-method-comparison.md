# Agentic OPD 同期方法实验对照

核查日期：2026-10-15。范围为当前 wiki 的 24 篇：19 篇方法／技术报告、EasyOPD 框架；4 篇基础背景单列范围说明。以下均为**作者报告、未复现**。原文版本固定为 wiki 已读版本；不是搜索最新全领域 leaderboard，也不核查会议录用状态。

## 阅读口径

- 每张表内部才是同一论文设置下的比较。相同模型名称／benchmark 名称不意味着跨表可直接排名；teacher 的额外训练、任务划分、prompt、最大轮数、采样与 checkpoint 选择都会改变结果。
- 「同期方法」指具名方法对照；Base、SFT、vanilla OPD、GRPO 是基础对照，技术报告中的最终模型比较另列。被排除的 OPSD／自蒸馏论文不新入库，但保留它们在正式纳入论文主表中的 baseline 分数，例如 SDAR。
- SR 为 success rate，EM 为 exact match；默认越高越好。百分点差是分数相减，不是相对提升百分比。保留不同 metric，不把 reward/score、EM、SR 合成总榜。
- 这里只摘主结果与直接方法对照；不是复制全部消融、全部 checkpoint 曲线。若省略轨迹长度／误差条会明确标明。没有记录 teacher 或重跑信息时写「未明确」，不根据惯例补齐。

## 1. ATOD：同框架比较 SOD、TCOD

【作者设置】Students 为 Qwen3-0.6B／1.7B／4B；前两者 teacher 为 **Qwen3-4B-GRPO**，4B 的 teacher 为 **Qwen3-30B-A3B-GRPO，150-step checkpoint**。各 student 训练窗口 150 steps，group size 8；评测 temperature 0.4、thinking off。ALFWorld／WebShop／Search-QA 最大交互步数分别 50／15／4。Search-QA 含 NQ、TriviaQA、PopQA、HotpotQA、2Wiki、MuSiQue、Bamboogle。主表称 validation SR，具体采样划分不能直接当作其他论文的 unseen split。

【对比方式】同一论文主表汇报，附录 C.2 明确 teacher-based baselines 使用相同 teacher checkpoint；不等于已独立核查 baseline 实现与调参充分性。TCOD 行未在主表区分 F2B/B2F，不能擅自指定变体。以下省略 Len.，保留 SR 与作者 Avg. SR。

| Student | 方法 | ALFWorld SR | Search-QA SR | WebShop SR | Avg. SR |
|---|---|---:|---:|---:|---:|
| 0.6B | Vanilla | 0.78 | 14.50 | 4.69 | 6.66 |
| 0.6B | GRPO | 30.47 | 39.36 | 29.69 | 33.17 |
| 0.6B | SDAR（自蒸馏，无外部 teacher） | 28.12 | 39.60 | 8.59 | 25.44 |
| 0.6B | OPD | 76.56 | 41.46 | 85.16 | 67.73 |
| 0.6B | SOD | 76.56 | 40.19 | 80.47 | 65.74 |
| 0.6B | TCOD | 74.22 | 42.04 | 84.38 | 66.88 |
| 0.6B | **ATOD** | **82.81** | **42.33** | **86.72** | **70.62** |
| 1.7B | Vanilla | 10.16 | 31.15 | 5.47 | 15.59 |
| 1.7B | GRPO | 31.25 | 41.99 | 47.66 | 40.30 |
| 1.7B | SDAR（自蒸馏，无外部 teacher） | 39.84 | 42.24 | 43.75 | 41.94 |
| 1.7B | OPD | 72.66 | 44.73 | 77.34 | 64.91 |
| 1.7B | SOD | 75.78 | 44.43 | 76.56 | 65.59 |
| 1.7B | TCOD | 71.88 | 45.02 | 81.25 | 66.05 |
| 1.7B | **ATOD** | **80.47** | **45.21** | **89.06** | **71.58** |
| 4B | Vanilla | 24.22 | 32.71 | 0.78 | 19.24 |
| 4B | GRPO | 76.56 | 48.19 | **82.03** | 68.93 |
| 4B | SDAR（自蒸馏，无外部 teacher） | 77.34 | 47.80 | 67.97 | 64.37 |
| 4B | OPD | 80.47 | 48.93 | 75.00 | 68.13 |
| 4B | SOD | 79.69 | 48.58 | 76.56 | 68.28 |
| 4B | TCOD | 76.56 | 48.39 | 75.78 | 66.91 |
| 4B | **ATOD** | **85.16** | **49.12** | 78.91 | **71.06** |
| — | 4B-GRPO teacher | 76.56 | 48.19 | 82.03 | 68.93 |
| — | 30B-A3B-GRPO teacher | 80.47 | 50.49 | 75.78 | 68.91 |

【解释】这套设置下 ATOD 三个规模的均值都最高；1.7B 相对 OPD／SOD／TCOD 为 +6.67／+5.99／+5.53 个百分点。但 4B-WebShop 是 GRPO 更高；两个规模的 SOD 或 TCOD 均值也会低于 vanilla OPD。不能由「新方法」推出各配置单调改进。没有主表训练 seed 误差条，因此不能仅凭小差值宣称显著。

来源：[§5.1、Table 1、Appendix C.2–C.3](https://arxiv.org/html/2606.27814v6#S4.T1)。

## 2. TCOD：主要比较 vanilla OPD 与自己的两种 curriculum

【作者设置】Table 2 为 Qwen2.5-3B／7B student，teacher 是 **ALFWorld GRPO-tuned Qwen2.5-7B**；统一训练 250 steps。ALFWorld 最多 30 turns。Seen／Unseen 是 validation split；Hard 是从 training split 中筛选 teacher pass@10 失败的任务，不能当作独立 unseen benchmark。省略 Rounds。

| Student | 方法 | ALFWorld Seen SR | Unseen SR | Train-Hard SR |
|---|---|---:|---:|---:|
| — | 7B-RL teacher | 85.71 | 76.87 | 6.61 |
| 3B | Zero-shot | 7.86 | 2.24 | 0.83 |
| 3B | SFT | 32.14 | 25.37 | 4.96 |
| 3B | OPD | 65.72 | 60.45 | 10.74 |
| 3B | TCOD-B2F | 77.86 | 70.90 | 13.22 |
| 3B | TCOD-F2B | 81.43 | 79.19 | 9.92 |
| 7B | Zero-shot | 9.29 | 8.96 | 1.65 |
| 7B | SFT | 54.29 | 48.73 | 8.26 |
| 7B | OPD | 75.37 | 72.14 | 13.22 |
| 7B | TCOD-B2F | 86.43 | 77.61 | 20.66 |
| 7B | TCOD-F2B | 82.14 | 76.12 | 18.18 |

Table 3 改用 **Qwen3-30B-A3B-Instruct teacher（不是上述 task-trained teacher）**；两个 Qwen3 student。以下列默认 η=2，原表另有 η=4/6：

| Student | 方法 | WebShop SR | ALFWorld SR | ScienceWorld SR | Avg. |
|---|---|---:|---:|---:|---:|
| — | teacher | 32.84 | 39.57 | 18.42 | 30.28 |
| 1.7B | OPD | 0.14 | 0.32 | 0.05 | 0.17 |
| 1.7B | TCOD-B2F | 20.54 | 24.55 | 10.82 | 18.64 |
| 1.7B | TCOD-F2B | 21.15 | 24.12 | 10.45 | 18.57 |
| 4B | OPD | 30.12 | 36.85 | 15.95 | 27.64 |
| 4B | TCOD-B2F | 32.15 | 38.62 | 17.46 | 29.41 |
| 4B | TCOD-F2B | 31.81 | 38.95 | 17.85 | 29.54 |

【解释】本文主要证据是 curriculum 相对完整 rollout OPD 的稳定性；没有在自己的原主表中建立对 SOD、ATOD 等同期机制的排序。3B-Unseen F2B 更强，但 7B-Hard B2F 更强，3B-Hard F2B 甚至低于 OPD。不能把 F2B 与 B2F 合成一个处处最优的 TCOD。B2F 额外采集成功 teacher 轨迹，等训练步不等于等总成本。

来源：[§5.1、Tables 2–3、Appendix D](https://arxiv.org/html/2604.24005v3#S5.T2)。

## 3. Guided-OPD：AdaSwitch、TCOD-F2B

【作者设置】Qwen3-0.6B／1.7B／4B student ← Qwen3-30B-A3B frozen teacher，teacher reference 为 zero-shot，未报告追加任务训练。作者在 Trinity-RFT 重实现，250 updates、seed42；ALFWorld seen/unseen，ScienceWorld／WebShop validation，后两者 SR 要求 Score=100。固定 updates，不等总 teacher／环境成本。

下表省略 Round。**Avg Score 只平均 SW、WS 两个 Score；Avg SR 平均 ALF-IID、ALF-OOD、SW、WS 四列**，此口径由表中数字复算支持，不能当三环境同权均值。

| Student | 方法 | ALF IID/OOD SR | ScienceWorld Score/SR | WebShop Score/SR | Avg Score/SR |
|---|---|---|---|---|---|
| 0.6B | Zero-shot | 0.24 / 0.25 | 5.19 / 2.25 | 10.37 / 3.75 | 7.78 / 1.62 |
| 0.6B | OPD | 19.29 / 16.42 | 10.42 / 1.50 | 39.89 / 8.00 | 25.16 / 11.30 |
| 0.6B | AdaSwitch | 25.11 / 17.91 | 9.56 / 1.25 | 43.41 / 7.75 | 26.49 / 13.01 |
| 0.6B | TCOD-F2B | 24.29 / 14.93 | 15.71 / 3.00 | 46.37 / 8.25 | 31.04 / 12.62 |
| 0.6B | Guided-OPD | 27.14 / 19.40 | 19.63 / 3.75 | 48.44 / 9.75 | 34.04 / 15.01 |
| 1.7B | Zero-shot | 8.10 / 7.10 | 6.48 / 0.75 | 28.71 / 10.25 | 17.60 / 6.55 |
| 1.7B | OPD | 23.57 / 26.87 | 16.94 / 3.00 | 47.59 / 11.00 | 32.27 / 16.11 |
| 1.7B | AdaSwitch | 25.71 / 23.13 | 17.02 / 2.75 | 46.79 / 10.50 | 31.91 / 15.52 |
| 1.7B | TCOD-F2B | 27.86 / 24.63 | 19.08 / 3.25 | 49.47 / 14.25 | 34.28 / 17.50 |
| 1.7B | Guided-OPD | 32.86 / 29.85 | 23.24 / 5.25 | 52.63 / 11.75 | 37.94 / 19.93 |
| 4B | Zero-shot | 28.57 / 27.86 | 16.21 / 3.75 | 20.59 / 8.25 | 18.40 / 17.11 |
| 4B | OPD | 31.43 / 32.09 | 26.45 / 7.50 | 50.87 / 13.50 | 38.66 / 21.13 |
| 4B | AdaSwitch | 29.29 / 29.10 | 25.24 / 6.25 | 48.91 / 12.25 | 37.08 / 19.22 |
| 4B | TCOD-F2B | 32.86 / 31.34 | 25.86 / 9.25 | 53.13 / 19.00 | 39.50 / 23.11 |
| 4B | Guided-OPD | 37.14 / 35.08 | 29.50 / 11.50 | 55.78 / 17.75 | 42.64 / 25.37 |
| — | 30B-A3B teacher | 43.57 / 40.80 | 27.73 / 7.25 | 55.07 / 19.25 | 41.40 / 27.72 |

【解释】Guided 的汇总指标领先，但 1.7B、4B 的 WebShop 完全成功率均低于 TCOD-F2B。主表没有 seed 误差条。

来源：[§4、Table 1、配置 Table 4](https://arxiv.org/html/2606.15912v2#S4.T1)。

## 4. SAGE-OPD：TCOD-F2B、Entropy-Aware OPD，以及加 rollout 的 OPD

【作者设置】Qwen3-0.6B／1.7B student；ALFWorld、ScienceWorld 用 Qwen3-8B／32B teacher，SearchQA 用 8B，未报告追加 task-specific teacher training。作者在 verl 异步框架实现，一 epoch、batch64。SAGE 每 turn 额外一次 teacher 标签 query；ALFWorld 有 OPD(two rollouts) 额外预算对照，另两环境没有。没有多 seed 误差条。

ALFWorld 为 official seen/unseen；ScienceWorld 为30 task types×5 variations，原表 Mean Score 可负，不是普通0–100成功率。下面把两张独立主表并列，不合成平均；省略原表平均 Turns。

| Teacher→Student | 方法 | ALF seen/unseen SR | ScienceWorld SR/Mean Score |
|---|---|---|---|
| 8B→0.6B | SFT | 2.86 / 4.48 | 2.01 / -31.84 |
| 8B→0.6B | OPD | 55.00 / 56.72 | 2.01 / -12.88 |
| 8B→0.6B | OPD(two rollouts) | 56.43 / 59.70 | — |
| 8B→0.6B | Entropy-Aware | 54.26 / 54.48 | 3.36 / -11.52 |
| 8B→0.6B | TCOD-F2B | 56.43 / 61.19 | 3.03 / -2.07 |
| 8B→0.6B | SAGE | 57.86 / 61.94 | 2.01 / +3.89 |
| 8B→1.7B | SFT | 25.00 / 26.12 | 2.01 / -17.56 |
| 8B→1.7B | OPD | 60.00 / 61.94 | 4.70 / -2.78 |
| 8B→1.7B | OPD(two rollouts) | 63.00 / 64.93 | — |
| 8B→1.7B | Entropy-Aware | 63.57 / 65.67 | 3.36 / -3.13 |
| 8B→1.7B | TCOD-F2B | 64.29 / 58.21 | 4.70 / -9.68 |
| 8B→1.7B | SAGE | 64.29 / 70.15 | 6.71 / +0.24 |
| 32B→0.6B | SFT | 未列 | 2.01 / -34.59 |
| 32B→0.6B | OPD | 53.57 / 68.66 | 3.36 / -28.46 |
| 32B→0.6B | OPD(two rollouts) | 52.14 / 70.37 | — |
| 32B→0.6B | Entropy-Aware | 48.57 / 68.13 | 6.04 / -26.10 |
| 32B→0.6B | TCOD-F2B | 54.29 / 67.91 | 2.68 / -33.42 |
| 32B→0.6B | SAGE | 54.29 / 70.90 | 6.04 / -26.10 |
| 32B→1.7B | SFT | 未列 | 2.01 / -15.61 |
| 32B→1.7B | OPD | 58.57 / 74.85 | 4.03 / -29.89 |
| 32B→1.7B | OPD(two rollouts) | 62.14 / 72.39 | — |
| 32B→1.7B | Entropy-Aware | 60.00 / 79.10 | 3.36 / -14.99 |
| 32B→1.7B | TCOD-F2B | 57.14 / 73.13 | 6.04 / -14.89 |
| 32B→1.7B | SAGE | 62.82 / 73.88 | 7.38 / -16.01 |

SearchQA 用7数据集 macro EM，每 split 至多500题，Bamboogle125；以下是原 Table 3 的逐项分数：

| Student | 方法 | NQ | TriviaQA | PopQA | HotpotQA | 2Wiki | MuSiQue | Bamboogle | Avg EM |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.6B | SFT | 14.40 | 23.60 | 5.80 | 13.20 | 11.69 | 2.23 | 6.40 | 11.05 |
| 0.6B | OPD | 25.00 | 41.40 | 17.80 | 28.20 | 24.80 | 17.00 | 24.00 | 25.46 |
| 0.6B | Entropy-Aware | 25.60 | 40.00 | 18.80 | 28.80 | 25.60 | 17.40 | 24.40 | 25.80 |
| 0.6B | TCOD-F2B | 25.40 | 41.00 | 15.60 | 29.00 | 24.60 | 16.80 | 23.20 | 25.09 |
| 0.6B | SAGE | 25.20 | 41.60 | 18.40 | 29.80 | 23.20 | 15.00 | 24.00 | 25.31 |
| 1.7B | SFT | 27.40 | 39.60 | 11.60 | 21.20 | 8.80 | 12.00 | 20.00 | 20.09 |
| 1.7B | OPD | 30.60 | 47.20 | 12.40 | 33.20 | 29.60 | 24.80 | 32.80 | 30.09 |
| 1.7B | Entropy-Aware | 29.40 | 48.20 | 12.60 | 33.20 | 30.20 | 23.80 | 36.80 | 30.60 |
| 1.7B | TCOD-F2B | 31.20 | 47.60 | 12.40 | 33.80 | 28.60 | 24.00 | 36.00 | 30.51 |
| 1.7B | SAGE | 30.00 | 48.40 | 12.80 | 33.20 | 30.40 | 24.60 | 36.00 | 30.77 |

【解释】8B→1.7B 的 ALF unseen 有明显收益，但换成32B teacher，SAGE 73.88 低于 OPD 74.85、Entropy-Aware 79.10；0.6B SearchQA 也不是最优。此处不因选一个有利配置便称通用优胜。

来源：[Tables 1–3、§5.1、Appendix A](https://arxiv.org/html/2606.19659v1#S5.T1)。

## 5. TurnOPD：TCOD-F2B；同时给同时间、同步数成绩

【作者设置】ALFWorld 1.7B／4B、WebShop 1.7B student 为 Qwen3，teacher 为 **Qwen3-8B-GRPO**；Search 用 **Qwen3.5-2B←Qwen3.5-9B-GRPO**。统一 reverse-KL 实现，100 updates，并比较共享 wall-clock cutoff。Thinking 开启；invalid action 被客户端阻止、不消耗环境 step。ALF 是 valid_unseen；Search 为 PopQA/NQ/2Wiki/Hotpot 混合；WebShop accuracy 使用 dense terminal score，不等同完全成功率。

Table 2 accuracy 为 Avg@4，再平均最后4次评测；**±为 checkpoint 波动，不是独立训练 seed 方差**。

| 环境/Student | 方法 | 同时间 accuracy | 同100步 accuracy | 100步耗时(h) |
|---|---|---:|---:|---:|
| ALF/1.7B | Zero-shot / Teacher | 0.00 / 90.75 | 0.00 / 90.75 | — |
| ALF/1.7B | OPD | 73.52±1.84 | 83.00±1.69 | 4.42 |
| ALF/1.7B | TCOD-F2B | 80.06±1.43 | 80.06±1.43 | 1.87 |
| ALF/1.7B | TurnOPD | 85.60±0.95 | 86.29±0.48 | 1.93 |
| ALF/4B | Zero-shot / Teacher | 8.17 / 90.75 | 8.17 / 90.75 | — |
| ALF/4B | OPD | 90.79±0.61 | 91.81±0.83 | 2.86 |
| ALF/4B | TCOD-F2B | 86.50±1.88 | 86.50±1.88 | 1.89 |
| ALF/4B | TurnOPD | 91.73±1.41 | 92.21±0.42 | 2.16 |
| Search/2B | Zero-shot / Teacher | 36.08 / 59.00 | 36.08 / 59.00 | — |
| Search/2B | OPD | 45.77±0.48 | 47.82±0.92 | 4.45 |
| Search/2B | TCOD-F2B | 45.64±1.06 | 47.77±1.21 | 3.80 |
| Search/2B | TurnOPD | 47.24±1.03 | 47.24±1.03 | 2.94 |
| WebShop/1.7B | Zero-shot / Teacher | 25.80 / 84.46 | 25.80 / 84.46 | — |
| WebShop/1.7B | OPD | 76.98±0.79 | 81.65±1.47 | 1.57 |
| WebShop/1.7B | TCOD-F2B | 80.45±1.57 | 81.66±0.89 | 1.33 |
| WebShop/1.7B | TurnOPD | 82.80±0.75 | 82.80±0.75 | 1.24 |

【解释】最有力证据是同时间改善，而非所有任务同步数必胜：Search 同100步 OPD 47.82 高于 Turn 47.24。TCOD 在 ALF/1.7B 比 Turn 略快，但较低分。是否计入 teacher 专用 RL 训练成本，不能由 student 阶段计时表推断。

来源：[§6、Table 2、Appendix A](https://arxiv.org/html/2607.05804v2#S6.T2)。

## 6. DASH-OPD：同期对照覆盖较广，但有 baseline 改造

【作者设置】Qwen3-1.7B／4B ← frozen Qwen3-30B-A3B，未追加任务 RL。统一重跑 OPD、AdaSwitch、TCOD、Guided、Turn。**TCOD 行为 F2B/B2F 两结果平均，不是单一变体；AdaSwitch 改成逐 turn 独立触发。** WebShop100题、ALF140 IID+134 OOD、ScienceWorld1308题；分别150／250／250 updates，seed42，final checkpoint，每题单 rollout。等步数，不等总成本；没有±。下表省略原表平均 Turns。

| Student | 方法 | WebShop Score/SR | ALF IID/OOD/Overall SR | ScienceWorld Score/SR |
|---|---|---|---|---|
| 1.7B | Zero-shot | 3.33 / 2.00 | 2.86 / 0.00 / 1.46 | 10.92 / 1.76 |
| 1.7B | OPD | 32.03 / 10.00 | 23.57 / 29.10 / 26.28 | 27.23 / 7.65 |
| 1.7B | AdaSwitch | 34.43 / 12.00 | 27.14 / 26.12 / 26.64 | 35.85 / 11.01 |
| 1.7B | TCOD mean | 36.41 / 11.00 | 25.71 / 32.09 / 28.83 | 30.45 / 5.93 |
| 1.7B | Guided | 33.19 / 10.00 | 26.43 / 30.60 / 28.47 | 32.14 / 10.24 |
| 1.7B | Turn | 37.29 / 12.00 | 27.14 / 31.34 / 29.20 | 32.52 / 9.33 |
| 1.7B | DASH | 43.53 / 13.00 | 31.43 / 34.33 / 32.85 | 38.46 / 12.77 |
| 4B | Zero-shot | 22.74 / 9.00 | 31.43 / 36.57 / 33.94 | 38.39 / 16.21 |
| 4B | OPD | 35.10 / 12.00 | 34.29 / 38.81 / 36.50 | 43.71 / 16.36 |
| 4B | AdaSwitch | 34.85 / 14.00 | 35.00 / 38.06 / 36.50 | 46.19 / 20.34 |
| 4B | TCOD mean | 38.05 / 14.50 | 37.86 / 34.70 / 36.31 | 47.30 / 19.69 |
| 4B | Guided | 35.82 / 13.00 | 35.00 / 32.09 / 33.58 | 46.05 / 19.65 |
| 4B | Turn | 36.26 / 14.00 | 35.71 / 39.55 / 37.59 | 45.26 / 17.20 |
| 4B | DASH | 42.77 / 16.00 | 41.43 / 41.04 / 41.24 | 50.97 / 22.40 |
| — | Teacher | 40.67 / 17.00 | 45.00 / 36.57 / 40.88 | 51.86 / 23.01 |

【解释】本表中 DASH 的 task 性能指标均领先 student baselines；这是 DASH 重跑设置下的结论。不能拿本表 Turn=29.20 去否定原 TurnOPD 的 ALF=86.29，二者 teacher／推理模式／环境接口与汇总口径不同。

来源：[§5.1、Table 1、Appendix Table 5](https://arxiv.org/html/2607.29078v4#S5.T1)。

## 7. FutureBridge-OPD：TCOD 两变体、Guided；三 seed 与两类 teacher

【作者设置】主表 Qwen3-1.7B／4B ← frozen Qwen3-32B，未追加任务训练；补表 4B ← **GiGPO-trained Qwen3-8B**。所有 baseline 作者重跑，200 updates，三 seed mean±std。FTB 额外双分支 H=3 continuation 和环境 replay，不是等总采样预算。ALF unseen；WebShop held-out sessions4096–4195；ScienceWorld disjoint task-type split。**WebShop SR 定义 reward>0.5，不能与要求 reward=1 的完全成功 SR 混排。**

| Student | 方法 | ALF SR | WS Score | WS SR (>0.5) | SW Score | SW SR |
|---|---|---:|---:|---:|---:|---:|
| 1.7B | Zero-shot | 7.5 | 39.0 | 31.0 | 6.4 | 2.0 |
| — | Teacher32B | 50.0 | 52.8 | 51.0 | 28.8 | 12.0 |
| 1.7B | OPD | 21.5±3.0 | 32.6±2.2 | 31.7±2.9 | 22.2±1.3 | 2.0±1.5 |
| 1.7B | TCOD-F2B | 30.7±3.2 | 39.6±1.7 | 38.3±1.2 | 26.1±0.0 | 5.8±0.8 |
| 1.7B | TCOD-B2F | 35.0±3.3 | 41.8±3.7 | 40.3±3.3 | 22.3±0.4 | 6.7±0.6 |
| 1.7B | Guided | 33.1±5.4 | 44.6±11.7 | 41.7±10.6 | 23.5±2.3 | 4.7±0.6 |
| 1.7B | FTB w/o Bridge Exec | 31.4±3.2 | 58.4±3.4 | 55.3±3.7 | 18.7±3.3 | 3.7±1.2 |
| 1.7B | FTB | 40.4±3.4 | 58.1±1.5 | 57.7±1.7 | 26.4±0.4 | 6.8±0.6 |
| 4B | Zero-shot | 20.9 | 32.9 | 29.0 | 23.1 | 8.5 |
| 4B | OPD | 42.3±4.9 | 43.2±1.7 | 40.3±2.6 | 29.0±0.3 | 7.3±1.0 |
| 4B | TCOD-F2B | 47.5±4.6 | 49.7±7.9 | 46.7±6.8 | 23.9±0.4 | 11.3±2.5 |
| 4B | TCOD-B2F | 39.8±4.8 | 50.9±1.2 | 47.3±2.6 | 24.5±2.1 | 9.5±0.4 |
| 4B | Guided | 47.0±9.3 | 47.7±5.8 | 47.0±5.9 | 28.3±1.7 | 11.3±2.0 |
| 4B | FTB w/o Bridge Exec | 48.5±9.2 | 50.7±0.3 | 48.3±1.2 | 24.6±3.7 | 12.5±3.3 |
| 4B | FTB | 48.3±1.9 | 50.9±5.9 | 50.0±5.7 | 28.4±2.9 | 14.0±0.4 |

任务训练过的8B teacher→4B student：

| 方法 | ALF SR | WS Score | WS SR |
|---|---:|---:|---:|
| Teacher8B-GiGPO | 79.9 | 62.6 | 61.0 |
| OPD | 67.4±3.7 | 63.7±2.5 | 64.0±1.6 |
| TCOD-F2B | 66.5±1.3 | 63.3±2.6 | 64.7±2.1 |
| TCOD-B2F | 68.6±2.3 | 61.7±1.7 | 63.3±1.2 |
| Guided | 72.6±3.4 | 63.8±3.9 | 62.0±5.0 |
| FTB w/o Bridge Exec | 70.8±1.6 | 63.0±0.8 | 63.0±1.4 |
| FTB | 74.1±3.1 | 65.7±1.2 | 66.3±0.5 |

【解释】FTB 在多数主指标更好，但主表4B SW Score 28.4±2.9 低于 OPD 29.0±0.3；4B ALF 点估计略低自身消融。Teacher 换成任务训练8B后各方法 ALF 分数整体升高，说明只看 teacher 参数量会误导。

来源：[§4、Tables 1–2、Appendix C.1–C.4](https://arxiv.org/html/2608.01953v2#S4.T1)。

## 8. SOD：主要比较 OPD+GRPO 与自蒸馏；不是 household Agent 同期榜

【作者设置】Qwen3-0.6B／1.7B ← **GRPO-trained Qwen3-4B**。所有 RL／distillation student 从3K轨迹 SFT checkpoint 起步，30K RL prompts，最多一 epoch、每 prompt16 rollouts、最多16 tool turns；SandboxFusion code interpreter。五 independent seeds。主表指标 **average@32**，不是 pass@32；主表的「OPD」已联合 GRPO。下面仅摘均值，逐 benchmark 的原表±省略。LCB-v6为作者所称近期时间窗，具体日期cutoff未明确，不假定覆盖完整v6。

| Student | 方法 | AIME24 | AIME25 | GPQA-Diamond | LCB-v6 | Avg |
|---|---|---:|---:|---:|---:|---:|
| — | 4B-GRPO teacher | 67.60 | 60.42 | 55.19 | 63.13 | 61.59 |
| 0.6B | Vanilla | 7.71 | 12.81 | 13.24 | 14.89 | 12.16 |
| 0.6B | SFT | 5.67 | 5.42 | 15.20 | 9.61 | 8.97 |
| 0.6B | GRPO | 4.06 | 4.90 | 20.38 | 15.95 | 11.32 |
| 0.6B | OPD+GRPO | 16.82 | 22.95 | 17.76 | 22.65 | 20.04 |
| 0.6B | OPSD_gt | 12.63 | 17.04 | 17.32 | 16.73 | 15.93 |
| 0.6B | OPSD_hint | 9.77 | 14.12 | 15.98 | 12.65 | 13.13 |
| 0.6B | SOD | 20.84 | 26.13 | 22.19 | 27.72 | 24.22 |
| 1.7B | Vanilla | 9.90 | 8.96 | 26.80 | 22.73 | 17.10 |
| 1.7B | SFT | 26.77 | 22.40 | 29.85 | 24.63 | 25.91 |
| 1.7B | GRPO | 25.63 | 21.67 | 33.55 | 20.70 | 25.39 |
| 1.7B | OPD+GRPO | 43.86 | 37.04 | 31.73 | 32.45 | 36.27 |
| 1.7B | OPSD_gt | 33.85 | 24.69 | 35.02 | 22.73 | 29.07 |
| 1.7B | OPSD_hint | 34.42 | 21.43 | 33.46 | 23.12 | 28.11 |
| 1.7B | SOD | 50.83 | 41.72 | 38.72 | 40.63 | 42.98 |

Appendix C.3 的1.7B平均：pure OPD 33.79、OPD+GRPO 36.27、SOD w/o GRPO 40.78、SOD 42.98。原论文未与 TCOD／Guided／Turn 等同期 Agentic OPD 实测比较；OPSD_gt/hint 属于本项目排除分支，仅在此保留 baseline。训练总时间0.6B OPD36.4h／SOD35.1h；1.7B OPD43.9h／SOD46.1h，不能声称 SOD 总是更快。

来源：[§5.1、Table 1、Appendix B–C](https://arxiv.org/html/2605.07725v3#S5.T1)。

## 9. DGPO：Search Agent 中比较 GKD、DistiLLM、TAID 等

【作者设置】**Qwen2.5-0.5B-Instruct student ← Search-R1-PPO-3B teacher**（基于Qwen2.5-3B-Instruct，已做搜索 PPO）。Search-R1环境，Wikipedia2018+E5 top3、最多4轮；NQ+HotpotQA训练。下表为七数据集 EM，范围0–1，不是百分制。

【对比方式】作者在本配置训练各 baseline，非直接搬原论文分数；GKD／DistiLLM／TAID 为通用 KD 同期机制，并非全部专为多轮环境提出。DGPO含 cold start 和在线 teacher，未等总GPU时间；该3B teacher设置增加训练时间约9.5%。

| 方法 | NQ | TriviaQA | PopQA | HotpotQA | 2Wiki | MuSiQue | Bamboogle | Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Student | .004 | .006 | .007 | .007 | .015 | .000 | .000 | .006 |
| Teacher | .365 | .569 | .393 | .340 | .368 | .135 | .298 | .353 |
| PPO | .306 | .444 | .379 | .205 | .218 | .041 | .073 | .238 |
| SFT→PPO | .338 | .415 | .359 | .296 | .275 | .088 | .250 | .289 |
| GKD | .266 | .408 | .358 | .216 | .217 | .055 | .161 | .240 |
| SeqKD | .331 | .416 | .364 | .283 | .273 | .089 | .169 | .275 |
| KD | .331 | .431 | .373 | .286 | .284 | .091 | .290 | .298 |
| DistiLLM | .333 | .442 | .373 | .288 | .270 | .095 | .209 | .287 |
| TAID | .325 | .427 | .365 | .290 | .270 | .079 | .218 | .282 |
| DGPO | .378 | .481 | .402 | .342 | .303 | .120 | .274 | .329 |

【解释】此配置 DGPO student 均值最高但低于 teacher .353；部分任务超过 teacher 不代表整体超过。GRPO 被作者因 compact student 不稳定而排除，不是它已在同表输给 DGPO。

来源：[§§5.1–5.2、Table 2、Tables 8–10](https://arxiv.org/html/2508.20324v4#S5.T2)。

## 10. MAD-OPD：单 teacher、均权多 teacher、离线多 teacher 序列蒸馏

【作者设置】标准 Instruct checkpoints，30B版本明确为 Qwen3-30B-A3B-Instruct-2507；未报告额外任务 RL teacher。Agent training 用ToolACE约16K step-split examples，每step student生成action并由teacher debate／force-decode，不能称完整 online environment rollout。Code另用OpenThoughts3 30K训练checkpoint。统一一epoch、batch128、lr1e-5；MAD默认2 teachers×2轮debate，多teacher计算未匹配。

【对比方式】OPD用较强单teacher；MT-OPD双teacher均权无debate；MT-SeqKD strong/weak=7:3离线SFT。没有直接跑TCOD等。代表配置 **Qwen3-14B+8B→4B**：Agent accuracy%、Code pass@1（16随机seed的平均，原表Code±此处省略）。

| 方法 | BFCL-v4 | τ² | Vita | Agent Avg | LCB-v6 | MBPP+ | Code Avg | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 23.34 | 18.00 | 14.60 | 18.65 | 22.73 | 60.27 | 41.50 | 27.79 |
| MT-SeqKD | 22.51 | 26.07 | 15.85 | 21.48 | 23.18 | 58.36 | 40.77 | 29.19 |
| OPD | 24.79 | 29.17 | 15.81 | 23.26 | 25.00 | 63.82 | 44.41 | 31.72 |
| MT-OPD | 25.65 | 29.06 | 17.72 | 24.14 | 23.29 | 60.64 | 41.97 | 31.27 |
| MAD-OPD | 27.08 | 31.46 | 18.53 | 25.69 | 29.83 | 66.42 | 48.12 | 34.66 |

全部teacher/student配置的 Agent Avg：

| Teacher→Student | Base | MT-SeqKD | OPD | MT-OPD | MAD |
|---|---:|---:|---:|---:|---:|
| Qwen3 14B+8B→1.7B | 13.64 | 12.53 | 17.26 | 16.78 | 19.00 |
| Qwen3 14B+8B→4B | 18.65 | 21.48 | 23.26 | 24.14 | 25.69 |
| Qwen3 32B+30B-A3B→4B | 18.65 | 24.19 | 25.43 | 25.61 | 27.30 |
| Qwen3 32B+30B-A3B→8B | 25.39 | 28.82 | 29.62 | 30.39 | 31.57 |
| Qwen3 32B+30B-A3B→14B | 29.29 | 32.50 | 32.39 | 32.79 | 34.26 |
| Qwen3.5 27B+9B→4B | 29.25 | 22.30 | 29.07 | 28.00 | 30.79 |

【解释／限制】MAD在这些Agent均值上都领先；Agent主表无独立训练seed误差条。作者每10步保存，并按 **overall benchmark performance 选最佳checkpoint**，需与final checkpoint评估区分。Code与Agent来自不同训练checkpoint；Overall不应被读成单个checkpoint跨域能力。

来源：[§5、Table 1、Appendix B](https://arxiv.org/html/2605.01347v1)。

## 11. ReOPD：与 OPD 匹配 teacher／updates，重点是成本

【作者设置】Student Qwen3-4B-Instruct-2507，另有Qwen3-8B；均先2K tool-trajectory SFT。Teacher为4B-Instruct-2507／8B／30B-A3B-Instruct-2507，先SFT再GRPO，因此4B→4B也不是自蒸馏。Math为6.4K DAPO+Python，Search为6.5K NQ+HotpotQA、Wikipedia2018+E5 top3。OPD/ReOPD统一batch256、200 updates、lr1e-6。

【对比方式】只有Base、cold-start、SFT、vanilla OPD，无TCOD等同期Agentic OPD。Teacher-GRPO行是teacher reference，不是student GRPO。Math为六任务macro average（AIME24/25、AMC23 avg@8，其余avg@4）：

| Teacher→Student | Base | Cold-start | SFT | OPD | ReOPD | Teacher-GRPO |
|---|---:|---:|---:|---:|---:|---:|
| 4B→4B | 28.0 | 45.0 | 46.1 | 55.1 | 57.2 | 55.5 |
| 8B→4B | 28.0 | 45.0 | 45.0 | 51.0 | 53.7 | 49.9 |
| 30B-A3B→4B | 28.0 | 45.0 | — | 51.1 | 52.5 | 62.7 |
| 30B-A3B→8B | 35.3 | 46.8 | — | 56.5 | 56.8 | 62.7 |

代表4B→4B逐任务：

| 方法 | AIME24 | AIME25 | AMC23 | Minerva | Olympiad | MATH500 | Avg |
|---|---:|---:|---:|---:|---:|---:|---:|
| Base | 6.3 | 6.7 | 36.6 | 31.0 | 29.5 | 58.2 | 28.0 |
| Cold-start | 22.1 | 20.8 | 66.6 | 32.4 | 49.0 | 79.1 | 45.0 |
| SFT | 21.7 | 21.3 | 63.1 | 39.8 | 49.9 | 80.9 | 46.1 |
| OPD | 35.4 | 29.2 | 77.8 | 43.3 | 58.2 | 86.9 | 55.1 |
| ReOPD | 40.8 | 31.3 | 80.0 | 42.9 | 59.4 | 88.9 | 57.2 |

Search为avg@1、七任务 **micro average**，与上方DGPO／SAGE等macro EM不同：

| Teacher→Student | Base | Cold-start | OPD | ReOPD | Teacher-GRPO |
|---|---:|---:|---:|---:|---:|
| 4B→4B | 35.6 | 32.1 | 40.6 | 40.5 | 40.4 |
| 8B→4B | 35.6 | 32.1 | 39.1 | 39.0 | 41.0 |

| 4B→4B方法 | NQ ID | TriviaQA OOD | PopQA OOD | HotpotQA ID | 2Wiki OOD | MuSiQue OOD | Bamboogle OOD |
|---|---:|---:|---:|---:|---:|---:|---:|
| Base | 28.4 | 55.5 | 30.6 | 30.8 | 33.6 | 8.4 | 35.8 |
| Cold-start | 26.2 | 48.6 | 33.6 | 24.7 | 26.6 | 5.8 | 24.8 |
| OPD | 36.3 | 59.7 | 40.3 | 37.3 | 31.7 | 14.5 | 44.0 |
| ReOPD | 36.4 | 59.6 | 40.5 | 37.3 | 31.5 | 14.0 | 37.6 |

多teacher Table 6用两分域RL-trained 4B experts→共享4B：Math cold-start/OPD/ReOPD=47.0/55.4/55.3，Search=32.7/41.0/41.0。

【解释】Math略改善而Search均值基本持平／略降，核心优点是重用teacher轨迹后student阶段零tool calls，rollout≥4×加速；独立额外采集teacher轨迹仍>2×。这不是所有teacher训练成本都已配平。主表没有多seed方差。

来源：[§5、Tables 1–6](https://arxiv.org/html/2607.04763v3#S5)。

## 12. MemOPD：长记忆搜索，与 memory/RL 系统比较

【作者设置】Student正文为 **Qwen2.5 3B**，gpt-oss-120b生成并过滤20,036 turn examples做1epoch SFT；蒸馏teacher只明确为独立frozen 7B，准确checkpoint／追加训练未明确，不能自行指定为MEM1-7B。MEM1式HotpotQA+NQ multi-objective retrieval，Q2/Q8/Q16同时答2/8/16题；PPO/MemOPD只在Q2训练，五seeds。

【对比方式】主要对memory、搜索和RL系统，不直接对TCOD等同期OPD。Q2/Q8/Q16主表 **F1为多问题分数之和，不是0–1准确率**。PPO/MemOPD匹配初始化、data order、packed calls、action mask、eval；teacher费用不匹配。其他系统究竟逐项重跑还是引用，所读实验章节未明确。

| 方法 | Q2 summed F1 | Q8 summed F1 | Q16 summed F1 |
|---|---:|---:|---:|
| Qwen2.5-14B-Instruct | 0.904 | 1.872 | 0.704 |
| Qwen2.5-7B-Instruct | 0.365 | 1.102 | 0.214 |
| 7B+A-MEM | 0.372 | 1.431 | 0.966 |
| 7B truncate | 0.335 | 1.228 | 0.498 |
| Search-R1 | 0.533 | 0.080 | 0.011 |
| DeepResearcher | 0.646 | 0.902 | 0.106 |
| MEM1-QA 7B | 0.836 | 2.301 | 2.285 |
| Mixed-horizon SFT 3B | 0.606 | 1.146 | 1.352 |
| PPO 3B | 0.806±0.020 | 0.655±0.015 | 0.549±0.024 |
| MemOPD 3B | 0.921±0.024 | 2.510±0.019 | 2.834±0.019 |

Single-objective Wiki-RAG：

| 方法 | EM | F1 |
|---|---:|---:|
| 7B truncate | 0.296 | 0.386 |
| 7B A-MEM | 0.246 | 0.372 |
| 7B Instruct | 0.271 | 0.390 |
| 14B Instruct | 0.431 | 0.533 |
| Search-R1 | 0.452 | 0.518 |
| DeepResearcher | 0.428 | 0.512 |
| MEM1-QA SFT | 0.302 | 0.356 |
| MEM1-QA | 0.409 | 0.470 |
| PPO 3B | 0.409±0.020 | 0.486±0.021 |
| MemOPD 3B | 0.434±0.022 | 0.522±0.030 |

Fig3另给persistent-history OPD控制组：F1相对PPO+5.6%，MemOPD再+7.0%，总+13.0%；EM分别+4.4%、+10.0%、总+14.8%，均为作者相对比例。图中绝对值未可靠提取，不由表格倒算。MemOPD的long-horizon transfer明显强于本表PPO，但Wiki-RAG点估计仍低于Search-R1／14B的部分指标。

来源：[§4.1–4.5、Tables 1–2、Fig3](https://arxiv.org/html/2608.07068v1)。

## 13. Top-K Drift：接口诊断，不是同期完整 OPD 算法竞榜

【作者设置】Student Qwen/Qwen3.5-9B，两个teacher由同checkpoint分别SFT tool-call／direct-response后冻结；另有Llama-3.1-8B-Instruct分支，下表仅主Qwen配置。APIGen-MT conversation-disjoint train/val/test=3500/500/1000；decision test四balanced buckets共4000点。BFCL为本地固定harness的multi-turn dialogue execution/state exact，不是官方榜。

【对比方式】GKD接口的support/loss/decoding策略；无TCOD等完整同期方法。GKD统一319steps、top32、JSDβ0.5、student比例0.8、SFT anchor0.3，三seed；Base、Mixed SFT为单run，BFCL Hard Clip也单run。Support union额外teacher queries，step时间106.4→123.5s（约+16%），等steps不等成本。

| 方法 | APIGen Decision Acc↑ | Over-call↓ | Call Recall↑ | Respond Recall↑ |
|---|---:|---:|---:|---:|
| Base | 80.7 | 7.2 | 68.5 | 92.8 |
| Mixed SFT | 85.3 | 4.9 | 75.5 | 95.1 |
| Vanilla GKD | 88.6±0.3 | 14.2±2.1 | 91.5±1.7 | 85.8±2.1 |
| Hard Clip | 88.7±1.0 | 11.9±0.9 | 89.2±3.0 | 88.2±0.9 |
| Global Reweight | 88.6±1.3 | 9.7±0.8 | 86.9±3.3 | 90.3±0.8 |
| Soft Clamp | 88.7±0.7 | 9.0±0.2 | 86.5±1.4 | 91.0±0.2 |
| Support union | 89.8±0.8 | 7.4±0.6 | 87.0±2.0 | 92.6±0.6 |

| 方法 | BFCL Calls/turn | Loop@3 %↓ | Required call %↑ | Dialogue exact %↑ |
|---|---:|---:|---:|---:|
| Mixed SFT | 0.974 | 5.1 | 79.77 | 5.12 |
| Vanilla GKD | 1.515±0.122 | 15.1±3.0 | 92.90±0.33 | 7.04±0.31 |
| Hard Clip | 1.348 | 11.5 | 88.88 | 6.00 |
| Global Reweight | 1.297±0.088 | 10.8±1.4 | 87.78±4.62 | 5.33±0.92 |
| Soft Clamp | 1.289±0.023 | 10.3±0.4 | 88.50±2.01 | 6.17±0.38 |
| Support union | 1.118±0.057 | 8.0±0.9 | 81.22±2.38 | 4.12±0.33 |

【解释】改善over-call、decision accuracy不保证最终任务更好。Support union减少过度调用却把BFCL dialogue exact从7.04降到4.12；不能只挑诊断指标排名。另有exact restoration控制组，此处不复制完整诊断表。

来源：[§§2–5、Tables 4–5](https://arxiv.org/html/2607.07050v6)。

## 14. Planning Physics：受控100M模型实验，OPD vs GRPO

【作者设置】自定义从头训练约100M Qwen2.5-100M（Qwen2架构、vocab3000），不是现成商用Qwen checkpoint。Student受控pretraining+SFT；teacher是同架构独立领域专家，学习gold trajectories。Fantasy Alchemy／Livestock Farming／Electronic Assembly文本crafting，Short1–5、Mid6–8、Long≥9steps。附录teacher_all含train/test来源，是受控oracle研究，不能按未知测试集商业模型泛化理解。

【对比方式】vanilla OPD与GRPO、知识干预，以及顺序多teacher；MAD／CoPD／Uni-OPD仅related work，没有实测同期对照。原 Table 3代表pattern mixture **4 Opt.:4 Sub.**，每格为三domain平均：

| 方法 | Short avg@8 | Mid avg@8 | Long avg@8 | Overall avg@8 | Overall pass@8 |
|---|---:|---:|---:|---:|---:|
| Instruct | 68.12 | 9.32 | 0.94 | 26.13 | 44.03 |
| Short OPD | 81.54 | 34.71 | 11.85 | 42.70 | 47.57 |
| Short GRPO | 77.01 | 25.47 | 6.02 | 36.16 | 53.47 |
| Mid OPD | 80.86 | 33.18 | 10.08 | 41.37 | 46.74 |
| Mid GRPO | 78.44 | 31.43 | 8.93 | 39.60 | 55.28 |
| Long OPD | 80.91 | 32.71 | 10.13 | 41.25 | 46.39 |
| Long GRPO | 77.97 | 28.93 | 8.52 | 38.47 | 54.72 |

其他pattern的 Overall avg@8：

| Pattern | Instruct | Short OPD | Short GRPO | Mid OPD | Mid GRPO | Long OPD | Long GRPO |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4 Opt. | 79.29 | 77.63 | 79.38 | 77.91 | 79.00 | 78.20 | 79.20 |
| 4 Opt.:8 Sub. | 15.19 | 33.61 | 22.58 | 34.09 | 14.85 | 33.78 | 13.61 |

Table4知识gap：4Opt:4Sub下，Instruct overall avg@8/pass@8=26.13/44.03；Student+TeacherA=41.37/46.74，Student+TeacherB=31.50/36.60，两teacher自身FA accuracy均100。Tables6–7另做FA→LF→EA顺序蒸馏，非同期算法榜。

【解释】OPD在含Sub pattern的平均正确率更好，但GRPO的pass@8反而更高；metric选择改变优劣判断。作者匹配模型参数／pretraining量，不代表OPD与GRPO总teacher+rollout FLOPs对齐。附录9000steps是SFT设置，不挪作两算法共同预算。

来源：[§§5–6、Tables 3–7、Appendix](https://arxiv.org/html/2607.24720v1)。

## 15. CAST：solver teacher，对比 RL 方法

【作者设置】Qwen3-4B-Instruct-2507 student；teacher为Sokoban／Minesweeper／Rush Hour solver state cost/value，**不是LM logits teacher**。以DAPO objective结合solver turn advantage。每游戏ID和unseen各200test instances，每题4rollouts，**avg@4 success%，不是pass@4**。ID/unseen难度随棋盘／箱子／雷／车数量改变。

【对比方式】重实现GRPO／GSPO／DAPO，相同backbone/data/rollout/optimizer；GiGPO为process baseline。各游戏200／400／300updates，batch16、每prompt8rollouts。未直接与同期LM KL-OPD算法比较；solver额外成本未做同FLOPs强制匹配。

| 方法 | Sokoban ID/Unseen | Minesweeper ID/Unseen | Rush Hour ID/Unseen | Avg ID/Unseen |
|---|---|---|---|---|
| ReAct | 44.3 / 16.8 | 4.5 / 0.4 | 1.1 / 0.5 | 16.6 / 5.9 |
| GRPO | 71.3 / 30.5 | 9.7 / 0.5 | 53.8 / 26.7 | 44.9 / 19.2 |
| GSPO | 72.6 / 28.3 | 28.2 / 5.0 | 24.8 / 11.5 | 41.9 / 14.9 |
| DAPO | 71.9 / 31.3 | 29.8 / 7.3 | 32.5 / 17.4 | 44.7 / 18.7 |
| GiGPO | 70.6 / 29.6 | 13.7 / 1.4 | 51.9 / 31.3 | 45.4 / 20.8 |
| CAST | 77.0 / 34.8 | 44.7 / 11.0 | 64.7 / 39.5 | 62.1 / 28.4 |

Table2在三个source-game训练agent上取均值的zero-shot OOD：

| 方法 | ALFWorld Avg | WebShop Avg | Overall |
|---|---:|---:|---:|
| ReAct | 30.2 | 18.8 | 24.5 |
| GRPO | 27.2 | 17.5 | 22.4 |
| GSPO | 32.1 | 17.3 | 24.7 |
| DAPO | 30.4 | 16.6 | 23.5 |
| GiGPO | 30.9 | 17.9 | 24.4 |
| CAST | 37.9 | 22.7 | 30.3 |

Closed-source ReAct只作模型reference：Gemini2.5Flash平均ID/Unseen58.7/40.0、2.5Pro73.4/51.1、Sonnet4.5 50.4/31.5、Opus4.5 63.2/41.9、Sonnet4.6 75.1/57.0、Opus4.6 79.9/64.0。模型与decoding不同，不是同student算法对比。

来源：[§4、Tables 1–2、Appendix](https://arxiv.org/html/2607.25308v1)。

## 16. EasyOPD：同 backend 重跑 SOD 与普通 OPD

【作者设置】Qwen3-1.7B ← **GRPO-optimized Qwen3-4B**，共享SFT initialization、data与optimization budget，统一EasyOPD/verl多轮tool rollout。**Average@32，分数为百分数（%）**，不是pass@1。这里只取普通OPD分支，不纳入OPSD。

| 方法 | AIME24 | AIME25 | LCB-v6 | Avg |
|---|---:|---:|---:|---:|
| Base | 17.19 | 12.81 | 12.41 | 14.14 |
| GRPO | 34.06 | 26.25 | 21.93 | 27.41 |
| response-level OPD | 38.13 | 36.04 | 30.27 | 34.81 |
| SOD | 43.65 | 38.33 | 37.88 | 39.95 |

【解释】对同一实现框架中的step-wise与response-level监督有参考价值，不能直接和原SOD主表平均42.98比较：原表还含GPQA且初始化／配置不同。共享optimization budget不等于teacher总成本相同。

另Table2为跨tokenizer接口展示、非多轮性能榜：Qwen2.5-7B-Instruct→Phi-4-mini-Instruct，共享10K warm start，Math/Code Avg为Base50.2、ULD51.7、ALM52.9、DSKD52.8、SimCT53.5。Table3是OPSD，排除。

来源：[§4.1、Table 4](https://arxiv.org/html/2607.11012v1#S4.T4)。

## 17. Cross-Domain Hybrid OPD：阶段对照，不是同期方法对照

【作者设置】Hunyuan3(A21B) student；四teacher由相同A21B base分别在math/code/logic/science做GRPO，准确checkpoint名未公开。OPD用于通用response，search trajectory仍用GRPO；每prompt8rollouts、最大61440tokens。Stage I搜索RL，Stage II继续搜索RL+跨域OPD，额外训练／数据／teacher未配平。

| 内部搜索测试集，average reward | Base | Stage I | Stage II |
|---|---:|---:|---:|
| AS-MultiHopQA | .5012 | .8266 | .8386 |
| AS-LongTermQA | .5093 | .6886 | .6728 |
| AS-WideSeekQA | .4267 | .7867 | .8017 |
| AS-NewsQA | .4853 | .6250 | .6107 |
| AS-FormatQA | .1922 | .2556 | .2859 |

| 通用任务 accuracy（%） | Base | Stage I | Stage II |
|---|---:|---:|---:|
| GPQA Diamond | 73.23 | 69.95 | 76.64 |
| AIME25 | 62.00 | 59.00 | 66.33 |
| Frontier Science Olympiad | 55.00 | 52.00 | 50.00 |

【解释】部分能力恢复但非全部；没有与其他同期OPD实测，不能把stage收益当相同预算的算法优势。内部split数量所读章节未明确。

来源：[§5、Tables 2–3](https://arxiv.org/html/2608.02101v1#S5.T3)。

## 18. KAT-Coder-V2：最终模型榜，无法单独归因 OPD

【作者设置】统一student KAT-Coder-V2，由KAT-Coder-V1继续post-training；五个自训练SWE／WebCoding／Terminal／WebSearch／General experts，teacher准确checkpoint／规模未公开。联合RL+OPD，没有OPD机制单独消融。以下为不同scaffold结果；星号是引用Anthropic官方，其余在KwaiEnv重测。

| Benchmark / scaffold | KAT-Coder-V2 | Claude Opus4.6 |
|---|---:|---:|
| SWE-bench Verified / Claude Code | 79.6 | 80.8* |
| SWE-bench Verified / OpenCode | 74.8 | 75.0 |
| SWE-bench Verified / OpenClaw | 72.8 | 75.7 |
| SWE-bench Multilingual / Claude Code | 75.4 | 77.8* |
| SWE-bench Multilingual / OpenCode | 71.2 | 70.2 |
| SWE-rebench-V2 subset / Claude Code | 43.3 | 43.7 |
| SWE-rebench-V2 subset / OpenCode | 38.7 | 37.3 |

Table3 PinchBench Avg：KAT81.9、GLM5 80.3、MiniMaxM2.7 81.8、Opus4.6 82.3、GPT5.4 81.6、Gemini3.1Pro75.9；其他模型来自2026-03-25排行榜，训练／推理预算未配平。既不能把scaffold不同的分数横比，也不能把79.6归因于OPD。

来源：[§3.4、Tables 2–3](https://arxiv.org/html/2603.27703v1#S4.T2)。

## 19. KAT-Coder-V2.5：最终模型榜，没有独立 MOPD 对照

【作者设置】统一student KAT-Coder-V2.5，五teacher为SWE／general agentic reasoning／terminal／web coding／general knowledge experts；teacher准确checkpoint和student backbone规模未公开。Cold start+drift truncation等流程联合使用，未隔离收益。

| Benchmark | KAT V2.5 | GLM5.1 | GLM5.2 | KimiK2.6 | Opus4.8 |
|---|---:|---:|---:|---:|---:|
| SWE-Bench Pro | 65.2 | 58.4 | 62.1 | 58.6 | 69.2 |
| KAT Code Bench | 53.1 | 49.6 | 50.3 | 48.9 | 57.3 |
| PinchBench Avg | 94.9 | — | 87.0 | 80.7* | 93.5 |
| KAT Claw Bench | 85.5 | 84.4 | 86.8 | 85.2 | 90.7 |
| Terminal-Bench2.1 | 60.7 | 61.8 | 77.9 | 73.0 | 84.6 |
| SciCode | 50.3 | 43.8 | 50.5 | 53.5 | 53.5 |

星号80.7实际是Kimi-K2.7-Code；PinchBench来自2026-07-02 leaderboard。虽摘要强调统一Claude Code harness，不应把所有单元格笼统说成统一重跑；其余行也未像KAT-V2/Mach逐格清楚标来源。内部benchmark完整split数量本次未进一步逐节核查。不能用final模型榜推断其OPD优于ATOD／DASH。

来源：[§§5–6、Table 4](https://arxiv.org/html/2607.05471v1#S6.T4)。

## 20. Mach-Mind-4-Flash：MOPD阶段、teacher组合、部署模型三种证据

【作者设置】Student基于 **Qwen3.5-35B-A3B**，10余同规模冻结RL specialists，准确checkpoint名未公开。Production MOPD后还有HMPO，**MOPD Final不等于最终部署模型**。MOPD实验rollout_n=1、8K response cap，没有等总预算的同期OPD方法对照。

Table3阶段对照：

| Benchmark | SFT Base | Expert Teacher | MOPD Final |
|---|---:|---:|---:|
| LCB-v6 | 79.39 | 80.23 | 80.12 |
| IFEval | 92.42 | 94.64 | 94.84 |
| IFBench | 72.79 | 82.65 | 82.92 |
| LexInstructEval | 72.21 | 75.47 | 75.63 |
| SWE-bench Verified | 69.00 | 73.80 | 71.10 |
| PinchBench | 74.31 | 77.10 | 75.90 |
| ClawBench pass@3 | 80.70 | 80.30 | 83.20 |
| ClawEval | 61.82 | 67.23 | 70.35 |

Appendix C Table4固定其他组件、**单run**加入code teacher；CS／BS分别为Content-SafetyBench／Behavioral-SafetyBench：

| Teacher组合 | CS | BS | AIME25 | AIME26 | LCB6 | IFEval | IFBench | BFCL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tool-use+IF+safety | 96.94 | 76.22 | 90.62 | 91.04 | 78.63 | 92.61 | 81.62 | 76.30 |
| +code | 97.79 | 80.28 | 92.92 | 91.87 | 82.44 | 94.75 | 82.17 | 76.39 |

最终模型Table2的SWE-bench Verified：Mach70.60、GLM4.7Flash59.20*、Qwen3.5-35B-A3B69.20*、Nemotron3-120B-A12B60.50*、Qwen3.5-122B-A10B72.00*、Step3.5Flash74.40*、MiMoV2Flash80.20*、KimiK2.5 76.80*。星号均引用各官方TR；模型规模与预算不同。

【解释】阶段表证明在整合expert后部分能力提高，SWE仍低于expert teacher；teacher composition单run支持加入code expert有用，但不能给出稳健的多teacher算法排名。部署榜SWE70.60不能与MOPD Final71.10混成同一checkpoint。

来源：[§4.8–4.9、Tables 2–4](https://arxiv.org/html/2607.09375v1#S5.T3)。

## 21. 四篇基础背景为什么不进多轮分数榜

| Wiki论文 | 本次处理 | 原因 |
|---|---|---|
| GKD / On-Policy Distillation of Language Models | 不新摘单轮分数 | 是单轮OPD基础；其在Agent环境的重跑见DGPO等表，不能混用原单轮结果 |
| MiniLLM | 不新摘单轮分数 | 单轮reverse-KL蒸馏基础，不是本批多轮同期对照 |
| Speculative Knowledge Distillation | 不新摘单轮分数 | token交错采样基础，没有与本批相同环境的直接对照 |
| A Survey of On-Policy Distillation | 无方法实验排名 | survey只作导航，不能作为新算法效果证据 |

## 22. 如何从这些表判断优劣

【解释】现有证据更像几组局部比赛，而不是连通且公平的统一leaderboard：

| 原论文 | 实测的具名同期／相关KD方法（不计自己的方法、普通OPD/SFT/RL） | 可支持的判断 |
|---|---|---|
| ATOD | SOD、TCOD、SDAR（自蒸馏reference） | task-trained teacher下的OPD/RL混合与turn weighting比较 |
| Guided-OPD | AdaSwitch、TCOD-F2B | 未追加任务训练teacher下的课程／teacher执行干预比较 |
| SAGE-OPD | TCOD-F2B、Entropy-Aware OPD | 监督选择；额外query控制仅部分环境有 |
| TurnOPD | TCOD-F2B | rollout深度与同wall-time效率 |
| DASH-OPD | AdaSwitch、TCOD两变体均值、Guided、Turn | 对照覆盖较广，但baseline变体／改造必须保留 |
| FutureBridge | TCOD-F2B/B2F、Guided | 多seed、两类teacher下的bridge效用；额外continuation未等成本 |
| DGPO | GKD、SeqKD、KD、DistiLLM、TAID | compact搜索Agent对通用KD／RL机制的同设置适配 |
| MAD-OPD | MT-OPD、MT-SeqKD | 多teacher debate vs均权／序列蒸馏 |
| EasyOPD | SOD | 共享backend中response-level vsstep-wise监督 |
| TCOD、ReOPD | 没有其他具名同期Agentic OPD主表对照 | 相对vanilla OPD的curriculum／prefix成本收益 |
| SOD | OPSD_gt/hint（本项目排除分支） | TIR中的step-wise监督；不能据原表排household Agent方法 |
| MemOPD | 主要是MEM1/A-MEM/Search-R1等系统 | 记忆接口对齐与长程迁移，不是同期OPD竞榜 |
| Top-K Drift | 自身support/loss/decoding干预 | 诊断tradeoff，不是完整算法排名 |
| Planning Physics | OPD/GRPO和知识／顺序teacher干预 | 受控知识与算法差异，不是现成大模型竞榜 |
| CAST | GSPO/DAPO/GiGPO等RL | solver-based过程信号，不是LM teacher OPD竞榜 |
| Cross-Domain Hybrid OPD | 阶段比较 | 跨域能力保持，未建立同期OPD优势 |
| KAT-V2／V2.5 | 最终模型比较 | 产品能力，OPD独立贡献未知 |
| Mach-Mind-4-Flash | 阶段／teacher组合／最终模型比较 | 多expert整合事实，非同预算同期方法排名 |

【解释】如果目标是快速找有信息量的对照，优先看ATOD、DASH、FutureBridge的同篇表，再看TurnOPD的同wall-clock结果。此阅读顺序是对证据信息量的判断，**不是方法性能排名**。当前表中ATOD没有直接比DASH／FutureBridge，DASH没有直接比ATOD／SAGE／FutureBridge；不能传递推断它们之间的优劣。

【开放问题】这些局部优势在相同teacher checkpoint、environment split、horizon、metric、初始化和总teacher+环境+GPU预算下是否仍成立，原表尚不能回答。主表有分数不等于baseline调参充分性已独立审计。

核查边界：20篇指定版本原HTML的实验设置／主表／必要附录，4篇基础背景按范围说明；未复现、未审计代码、未查新，不新增idea。数值转录与链接检查只覆盖本次文档，不把这些检查扩成每篇必走流程。
