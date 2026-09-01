---
title: "An Efficient Sparse Fine-Tuning with Low Quantization Error via Neural Network Pruning"
description: "Fine-tuning is an important step in adapting foundation models such as large language models to downstream tasks."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2502.11439) · [PDF](https://arxiv.org/pdf/2502.11439)

## 一句话摘要

Fine-tuning is an important step in adapting foundation models such as large language models to downstream tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuning is an important step in adapting foundation models such as large language models to downstream tasks. To make this step more accessible to users with limited computational budgets, it is crucial to develop fine-tuning methods that are memory and computationally efficient. Sparse Fine-tuning (SpFT) and Low-rank adaptation (LoRA) are two frameworks that have emerged for addressing this problem and have been adopted widely in practice. In this work, we develop a new SpFT framework, based on ideas from neural network pruning. At a high level, we first identify "important" neurons/nodes using feature importance metrics from network pruning (specifically, we use the structural pruning method), and then perform fine-tuning by restricting to weights involving these neurons. Experiments on common language tasks show our method improves SpFT's memory efficiency by 20-50\% while matching the accuracy of state-of-the-art methods like LoRA's variants. Code available at: https://github.com/CenjhihLi/sparsity_finetuning

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Cen-Jhih Li, Aditya Bhaskara
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CenjhihLi/sparsity_finetuning](https://github.com/CenjhihLi/sparsity_finetuning)
- 阅读深度：metadata
