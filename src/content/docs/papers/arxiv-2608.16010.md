---
title: "Breaking the Compression Barrier: Cross-Architecture Compression Boundary Learning via Reverse Regrowth"
description: "Model compression is critical for deploying networks on resource-constrained edge devices."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.16010) · [PDF](https://arxiv.org/pdf/2608.16010)

## 一句话摘要

Model compression is critical for deploying networks on resource-constrained edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model compression is critical for deploying networks on resource-constrained edge devices. While pruning-based methods can significantly reduce model size, they often suffer from abrupt performance collapse beyond a sparsity thresh-old, making it difficult to identify the feasible compression limit of the model. To address this challenge, we propose a boundary-Learning reverse regrowth framework, BRIDGE, that reformulates compression as a constructive boundary-search problem. Unlike forward pruning, our method first drives the model to an extremely sparse state to expose the collapse region, and then selectively regenerates the critical structure to restore performance. The proposed framework employs a hierarchical regeneration strategy, including coarse-grained layer selection and fine-grained regeneration parameter selection, to accurately identify which parameters require recovery. Experiments show that our method can recover models from the brink of collapse on both CNNs and Transformer architectures, demonstrating its architecture in-dependence. BRIDGE achieves a performance improvement of up to 1.49% in unstructured pruning and up to 4.77% in structured pruning. These results demonstrate that reverse regeneration can effectively extend the compression limit while maintaining stable performance. The source code is available at https://github.com/EnumaCaliber/BRIDGE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhaocen Liu, Satvik Praveen, Yi Sheng
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EnumaCaliber/BRIDGE](https://github.com/EnumaCaliber/BRIDGE)
- 阅读深度：metadata
