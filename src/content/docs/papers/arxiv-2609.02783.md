---
title: "EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction"
description: "Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an agentic benchmark can cost hundreds to thousands of dollars, a price paid repeatedly across iterative development cycles."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.02783) · [PDF](https://arxiv.org/pdf/2609.02783)

## 一句话摘要

Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an agentic benchmark can cost hundreds to thousands of dollars, a price paid repeatedly across iterative development cycles.

## 为什么值得关注

待编辑增强。

## 摘要原文

Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an agentic benchmark can cost hundreds to thousands of dollars, a price paid repeatedly across iterative development cycles. Prior efforts, centered on benchmark distillation, reduce the number of evaluation tasks but leave the cost of executing each retained task untouched. In this work, we introduce early outcome prediction, a complementary axis of efficiency that instead cuts cost within each task. Our key insight is that an agent's final outcome is often evident from its intermediate behavior well before execution completes. We instantiate this idea in EarlyEval, a lightweight framework that trains a pair of LightGBM success and failure classifiers over behavioral, textual, and reference-solution features, and halts an agent run the moment either classifier crosses a calibrated confidence threshold, adding negligible per-step overhead. Across three benchmarks, SWE-bench Verified, TerminalBench, and Toolathlon, EarlyEval can eliminate 13%-26% of agent steps and up to 44.1% input tokens and 29.4% output tokens at 89%-97% prediction accuracy, while perturbing per-agent resolve rates by only one to two percentage points on average.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuling Shi, Zhensu Sun, Junsen Dong, Chengcheng Wan, David Lo, Xiaodong Gu
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
