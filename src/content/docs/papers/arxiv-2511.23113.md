---
title: "db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism"
description: "Scaling Diffusion Transformer (DiT) inference via sequence parallelism is critical for reducing latency in visual generation, but is severely hampered by workload imbalance when applied to models employing block-wise sparse attention."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.23113) · [PDF](https://arxiv.org/pdf/2511.23113)

## 一句话摘要

Scaling Diffusion Transformer (DiT) inference via sequence parallelism is critical for reducing latency in visual generation, but is severely hampered by workload imbalance when applied to models employing block-wise sparse attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling Diffusion Transformer (DiT) inference via sequence parallelism is critical for reducing latency in visual generation, but is severely hampered by workload imbalance when applied to models employing block-wise sparse attention. The imbalance stems from the inherent variation in sparsity across attention heads and the irregular distribution of dense blocks within the sparse mask, when sequence parallelism is applied along the head dimension (as in Ulysses) or the block dimension (as in Ring Attention). In this paper, we formalize a sparse imbalance ratio to quantify the imbalance, and propose db-SP, a sparsity-aware sequence parallelism technique that tackles the challenge. db-SP contains a dual-level partitioning approach that achieves near-perfect workload balance at both the head and block levels with negligible overhead. Furthermore, to handle the evolving sparsity patterns across denoising steps and layers, db-SP dynamically determines the parallel degrees for the head and block dimensions at runtime. Experimental results demonstrate that db-SP delivers an end-to-end speedup of 1.25x and an attention-specific speedup of 1.40x over state-of-the-art sequence parallel methods on average. Code is available at https://github.com/thu-nics/db-SP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Siqi Chen, Ke Hong, Tianchen Zhao, Ruiqi Xie, Zhenhua Zhu, Xudong Zhang, Yu Wang
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/thu-nics/db-SP](https://github.com/thu-nics/db-SP)
- 阅读深度：metadata
