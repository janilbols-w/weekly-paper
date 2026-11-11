---
title: "Trilinear Compute-in-Memory Architecture for Energy-Efficient Transformer Acceleration"
description: "Self-attention in Transformers generates dynamic operands that force conventional Compute-in-Memory (CIM) accelerators into costly non-volatile memory (NVM) reprogramming cycles, degrading throughput and stressing device endurance."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.07628) · [PDF](https://arxiv.org/pdf/2604.07628)

## 一句话摘要

Self-attention in Transformers generates dynamic operands that force conventional Compute-in-Memory (CIM) accelerators into costly non-volatile memory (NVM) reprogramming cycles, degrading throughput and stressing device endurance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-attention in Transformers generates dynamic operands that force conventional Compute-in-Memory (CIM) accelerators into costly non-volatile memory (NVM) reprogramming cycles, degrading throughput and stressing device endurance. Existing solutions either reduce but retain NVM writes through matrix decomposition or sparsity, or move attention computation to digital CMOS at the expense of NVM density. We present TrilinearCIM, a Double-Gate FeFET (DG-FeFET)-based architecture that uses back-gate modulation to realize a three-operand multiply-accumulate primitive for in-memory attention computation without dynamic ferroelectric reprogramming. Evaluated on BERT-base (GLUE) and ViT-base (ImageNet and CIFAR), TrilinearCIM outperforms conventional CIM on seven of nine GLUE tasks while achieving up to 46.6\% energy reduction and 20.4\% latency improvement over conventional FeFET CIM at 37.3\% area overhead. To our knowledge, this is the first architecture to perform complete Transformer attention computation exclusively in NVM cores without runtime reprogramming.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Md Zesun Ahmed Mia, Jiahui Duan, Kai Ni, Abhronil Sengupta
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
