---
title: "Pruning Laws for Large Language Models"
description: "Scaling up model parameters and training data consistently improves the performance of large language models (LLMs), but at the cost of rapidly growing memory and compute requirements, which makes deployment on resource-limited hardware infeasible."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2504.04342) · [PDF](https://arxiv.org/pdf/2504.04342)

## 一句话摘要

Scaling up model parameters and training data consistently improves the performance of large language models (LLMs), but at the cost of rapidly growing memory and compute requirements, which makes deployment on resource-limited hardware infeasible.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling up model parameters and training data consistently improves the performance of large language models (LLMs), but at the cost of rapidly growing memory and compute requirements, which makes deployment on resource-limited hardware infeasible. Model pruning, a widely used compression technique, reduces inference costs by removing redundant parameters. However, its impact on downstream performance remains unpredictable and is typically assessed only through costly empirical sweeps. To address this gap, we introduce pruning laws, simple and interpretable scaling relations that connect a pruned LLM's post-pruning performance to its unpruned performance and pruning ratio. Across ten LLMs (1.3B-30B parameters), a 20B mixture-of-experts model, three pruning strategies (unstructured, width, and depth), and eight diverse tasks, we show that pruning laws achieve strong predictive accuracy (average extrapolation error less than 7%), reliably quantify performance degradation, and identify critical pruning thresholds beyond which recovery is infeasible. Moreover, we demonstrate that the functional form transfers across dense and mixture-of-experts architectures, pruning methods, and unseen models in zero-shot and one-shot setups, with task- and method-specific coefficients that vary in interpretable ways. These results provide both researchers and practitioners with a principled framework to select pruning strategies, estimate safe pruning ratios without exhaustive tuning, and deploy LLMs efficiently under real-world compute and latency constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ayan Sengupta, Siddhant Chaudhary, Tanmoy Chakraborty
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
