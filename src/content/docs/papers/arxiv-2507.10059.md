---
title: "GeLaCo: An Evolutionary Approach to Layer Compression"
description: "Large Language Models have achieved remarkable performance across a large number of tasks, but face critical deployment and usage barriers due to substantial computational requirements."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2507.10059) · [PDF](https://arxiv.org/pdf/2507.10059)

## 一句话摘要

Large Language Models have achieved remarkable performance across a large number of tasks, but face critical deployment and usage barriers due to substantial computational requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models have achieved remarkable performance across a large number of tasks, but face critical deployment and usage barriers due to substantial computational requirements. Model compression methods, which aim to reduce model size while preserving its capacity, are an important means to mitigate these issues. Promising approaches along these lines, such as structured pruning, typically require costly manual hyperparameter exploration or rely on local heuristics that may run the risk of ignoring better solutions. In this work we introduce GeLaCo, an evolutionary approach to LLM compression via layer collapse. Our approach supports an efficient exploration of the compression solution space via population-based search and a novel layer collapse formulation based on parametrized weight merging, with a fitness function based on similarity over residual updates and language modeling KL divergence. GeLaCo also supports both single and multi-objective evolutionary compression search, establishing the first Pareto front estimation along compression and quality axes. We evaluate GeLaCo solutions via both perplexity-based and generative evaluations over foundational and instruction-tuned models, outperforming state-of-the-art alternatives.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：David Ponce, Thierry Etchegoyhen, Javier Del Ser
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
