---
title: "CORP: Closed-Form One-shot Representation-Preserving Structured Pruning"
description: "Transformers achieve strong accuracy but incur high compute and memory cost."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.05243) · [PDF](https://arxiv.org/pdf/2602.05243)

## 一句话摘要

Transformers achieve strong accuracy but incur high compute and memory cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformers achieve strong accuracy but incur high compute and memory cost. Structured pruning reduces inference cost, but most methods rely on retraining or multi-stage optimization, which limits post-training deployment. We propose CORP, a closed-form one-shot structured pruning method that removes MLP dimensions and attention substructures using only unlabeled calibration data without gradients or fine-tuning. CORP formulates structured pruning as a representation recovery problem. It models removed components as affine functions of retained components and derives closed-form ridge regression solutions that fold compensation into model weights. This minimizes a layer-local affine/logit reconstruction objective under the calibration distribution. Experiments on ImageNet with DeiT reveal strong redundancy in both MLP and attention representations. With CORP, models retain high accuracy under aggressive sparsity. On DeiT-Huge, CORP achieves 83.24% Top-1 accuracy after pruning 50% of both MLP and attention structures.

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

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boxiang Zhang, Baijian Yang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
