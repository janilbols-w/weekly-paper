---
title: "Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory"
description: "Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.07169) · [PDF](https://arxiv.org/pdf/2608.07169)

## 一句话摘要

Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Taeil Kim, Kangsan Kim, Sung Ju Hwang
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
