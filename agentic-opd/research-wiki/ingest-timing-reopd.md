# ReOPD 单篇入库计时

日期：2026-10-14；北京时间 21:18:42–21:23:22。
论文：[Multi-Turn On-Policy Distillation with Prefix Replay](papers/liao2026_multiturn_onpolicy_distillation.md)，arXiv 2607.04763v3。

## 实测耗时

| 阶段 | 耗时 |
|---|---:|
| 准备与选文 | 40.1 秒 |
| 获取原文与元数据（并行） | 3.3 秒 |
| 阅读原文、核对 PDF | 62.4 秒 |
| 整理正文、入库与更新索引 | 93.0 秒 |
| 验证、状态更新与计时记录 | 80.8 秒 |
| **合计** | **279.6 秒** |

计时方式：各阶段边界保存系统 UTC 时间与 monotonic clock；耗时取 monotonic 差值。阶段时间包括模型阅读 / 整理、工具调用、输出与等待，不能当成纯网络或脚本执行时间。计时从首个工具中的记录点开始，到验证及状态更新完成；不含首条说明和最终聊天回复的生成。

并行网络请求各自耗时：PDF 2.900 秒；HTML 1.936 秒；arXiv metadata 1.470 秒，不能相加当作获取阶段总时长。

## 本次验证

临时 Python 检查通过：12 节 schema、9 个 TODO 补全、protected 字段未变、相对链接有效、10 个原论文 HTML anchors 存在、graph / index / query pack 包含新 paper。重复调用 canonical ingest_paper 后正文 SHA-256 不变，strict scan clean。没有运行旧 card validator。

ARIS helper 执行实际入库、关系写入、索引 / query pack / log 更新；方法、数字与成本边界由原论文阅读核对。未进行独立 reviewer 复核、代码审计或实验复现。本记录不是常驻 wiki validator。

阅读范围：原论文 §§3-6，PDF pp. 12、14、15、16、19 目视核对。关键边界：零 tool calls 指 student 蒸馏阶段；需要 teacher 轨迹池和 teacher 分布查询。

原始计时：[JSON](../_meta/timing/second-paper-ingest.json)。先前 TCOD 已使 ARIS 安装 / wiki 初始化完成，本次没有这部分成本。

当前环境无 say 语音命令，未能语音通知。
