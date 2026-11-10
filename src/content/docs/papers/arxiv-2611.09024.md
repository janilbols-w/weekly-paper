---
title: "Knowledge Distillation from Neural Networks to Differentiable Logic Networks"
description: "Differentiable logic networks (DLNs) are interpretable, edge-friendly classifiers that learn both their logic operators and their connections through gradient descent, achieving accuracy competitive with multi-layer perceptrons at orders-of-magnitude lower inference cost."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.09024) · [PDF](https://arxiv.org/pdf/2611.09024)

## 一句话摘要

Differentiable logic networks (DLNs) are interpretable, edge-friendly classifiers that learn both their logic operators and their connections through gradient descent, achieving accuracy competitive with multi-layer perceptrons at orders-of-magnitude lower inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Differentiable logic networks (DLNs) are interpretable, edge-friendly classifiers that learn both their logic operators and their connections through gradient descent, achieving accuracy competitive with multi-layer perceptrons at orders-of-magnitude lower inference cost. Their accuracy, however, is bounded by the problems of vanishing gradients, scalability, and lack of an ecosystem, leaving a gap relative to conventional neural networks on several datasets. We introduce knowledge distillation for DLNs to narrow this gap. We distill from a trained multi-layer perceptron teacher into a DLN student, integrating the distillation objective into a two-phase training loop without altering the architecture or the inference procedure. The teacher is discarded after training. Hence, the distilled model retains the interpretability, sparsity, and inference cost of a conventionally trained DLN. We investigate this approach through four variants: a joint hyperparameter search that optimizes the distillation weight and temperature alongside the architecture, a grid search over these two hyperparameters with the architecture fixed, and two single-phase variants that employ distillation during only the neuron-function or only the connection phase. On 20 public tabular classification tasks, distillation improves balanced-class accuracy at negligible cost to gate-level operation counts and model size, though the benefit varies by dataset. Performance improvements of up to 15% are observed, in some cases surpassing the teacher itself.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hee Yun Suh, Niraj K. Jha
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
