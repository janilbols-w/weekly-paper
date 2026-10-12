---
title: "Proactive Agentic Orchestration"
description: "Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13485) · [PDF](https://arxiv.org/pdf/2610.13485)

## 一句话摘要

Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents. However, existing orchestration methods face two limitations: in execution, current methods fix sub-agents' goals and harnesses at creation time, limiting their adaptability to dynamic real-world environments; in optimization, sparse and delayed feedback constrains effective learning of the orchestration policy. To address these limitations, we introduce POrchestra, an on-the-fly proactive agentic orchestration framework. It allows sub-agents to proactively communicate with the orchestrator at any logical point to request harness adjustments while maintaining continuity of local execution. This mechanism not only enables sub-agents to adapt seamlessly to dynamic environments but also naturally inspires On-Policy Orchestration Distillation (OPOD) based on hindsight feedback. OPOD attributes sub-agents' proactive revision requests back to preceding orchestration decisions to derive targeted improvement signals, and leverages these signals as process supervision alongside the final reward to optimize the orchestration policy. We evaluate POrchestra on three long-horizon agent benchmarks spanning deep research, dynamic digital assistance, and software engineering. POrchestra improves task success by an average of 9.1% relative to the strongest baseline; combined with OPOD, it improves small-orchestrator success by an average of 10.0% relative to existing training baselines. POrchestra also achieves a more favorable cost-performance trade-off. Our code is publicly available at https://github.com/XueyangFeng/POrchestra.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xueyang Feng, Chaozhuo Li, Xiaohe Bo, Jiakai Tang, Chenxi Li, Qiwei Ye, Xu Chen
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/XueyangFeng/POrchestra](https://github.com/XueyangFeng/POrchestra)
- 阅读深度：metadata
