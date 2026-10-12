---
title: "How Much Computation Does Every Forecast Need? Structured Block Skipping in Two Time-Series Foundation Models"
description: "Time-series foundation models use the same network depth for every input, although forecasting windows differ in structure and difficulty."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13208) · [PDF](https://arxiv.org/pdf/2610.13208)

## 一句话摘要

Time-series foundation models use the same network depth for every input, although forecasting windows differ in structure and difficulty.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time-series foundation models use the same network depth for every input, although forecasting windows differ in structure and difficulty. We test whether whole Transformer blocks can be removed at inference time in two pretrained models: Chronos-Bolt and TimesFM 2.5. Our bypasses avoid the original block computation and preserve the dense model exactly when all blocks are enabled. Masks are selected only on calibration windows and evaluated on 1,088 held-out windows from ETTh1, Traffic, Weather, and Exchange. At moderate sparsity, Chronos-Bolt with 7/11 candidate blocks and TimesFM with 16/20 blocks show little change in mean relative forecasting quality across datasets while reducing median A100 batch-1 latency by 11.2% and 13.4%. More aggressive TimesFM skipping accelerates inference further but substantially harms Traffic and Weather. Across both models, different equal-budget masks win on different windows, and a retrospective oracle significantly improves over the best static mask on every dataset. However, dataset-specific masks transfer inconsistently, and Chronos representations do not support reliable unseen-domain routing. These results establish cross-architecture structured redundancy and input-dependent opportunity, but not a deployable dynamic inference method.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Max Bourgeat
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
