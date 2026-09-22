---
title: "Garbage Attention in Large Language Models: BOS Sink Heads and Sink-aware Pruning"
description: "Large Language Models (LLMs) are known to contain significant redundancy, yet a systematic explanation for why certain components, particularly in higher layers, are more redundant has remained elusive."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.06787) · [PDF](https://arxiv.org/pdf/2601.06787)

## 一句话摘要

Large Language Models (LLMs) are known to contain significant redundancy, yet a systematic explanation for why certain components, particularly in higher layers, are more redundant has remained elusive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are known to contain significant redundancy, yet a systematic explanation for why certain components, particularly in higher layers, are more redundant has remained elusive. In this work, we identify the BOS sink phenomenon as a key mechanism driving this layer-wise sensitivity. We show that attention heads with high BOS sink scores are strongly associated with functional redundancy: such heads, especially in deeper layers, contribute little to predictive performance and effectively serve as dumping grounds for superfluous attention weights. Leveraging this insight, we introduce a simple pruning strategy that removes high-BOS sink heads. Experiments on Gemma-3, Llama-3.1, and Qwen3 demonstrate that this approach identifies redundant transformer components more reliably than weight- and activation-based criteria in terms of downstream task retention, remaining close to dense baselines at low-to-moderate pruning ratios. We further find that high-scoring sink heads sustain their focus on BOS as context length grows. Overall, our results suggest that structural properties of attention offer a more direct basis for model compression than magnitude-based methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaewon Sok, Jewon Yeom, Seonghyeon Park, Jeongjae Park, Taesup Kim
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
