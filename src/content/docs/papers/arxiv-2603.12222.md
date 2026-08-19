---
title: "HiAP: A Multi-Granular Stochastic Auto-Pruning Framework for Vision Transformers"
description: "Vision Transformers require significant computational resources and memory bandwidth, severely limiting their deployment on resource-constraint hardware."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.12222) · [PDF](https://arxiv.org/pdf/2603.12222)

## 一句话摘要

Vision Transformers require significant computational resources and memory bandwidth, severely limiting their deployment on resource-constraint hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision Transformers require significant computational resources and memory bandwidth, severely limiting their deployment on resource-constraint hardware. Most structured pruning methods reduce theoretical cost effectively, yet they typically operate at a single structural granularity and depend on multi-stage pipelines with importance ranking, auxiliary solvers or post-hoc magnitude thresholding, followed by a separate fine-tuning phase to recover accuracy. We propose Hierarchical Auto-Pruning (HiAP), which casts ViT pruning as a single budget-aware learning problem and jointly allocates sparsity across four granularities in one end-to-end phase. HiAP introduces stochastic Gumbel-Sigmoid gates at macro level (attention heads and FFN blocks) and micro level (intra-head dimensions and FFN neurons), and trains them against the task loss together with an analytical MAC cost term. The budget coefficient steers the network to a target compute level while the gates gradually harden into a dense, smaller sub-network at convergence. It does not require importance heuristics, ranking metrics, auxiliary solvers or secondary fine-tuning. On ImageNet, HiAP compresses DeiT-Base to 7.4G MACs at 80.88% top-1 and DeiT-Small to 3.1G at 79.33%, competitive with substantially more complex pipelines at matched compute. The structurally pruned network can be accelerated natively on stock kernels, and more than 90% of the theoretical MAC reduction is realized as measured throughput on an A100.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andy Li, Aiden Durrant, Milan Markovic, Georgios Leontidis
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
