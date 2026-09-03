---
title: "SpCCL: A Sparsity-Aware Collective Communication Library for GPU Platforms"
description: "Collective communication is essential to high performance computing and machine learning workloads, yet libraries such as NCCL do not exploit sparsity in message payloads."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.04676) · [PDF](https://arxiv.org/pdf/2607.04676)

## 一句话摘要

Collective communication is essential to high performance computing and machine learning workloads, yet libraries such as NCCL do not exploit sparsity in message payloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collective communication is essential to high performance computing and machine learning workloads, yet libraries such as NCCL do not exploit sparsity in message payloads. Sending only nonzero values can reduce network traffic, but explicitly handling sparsity introduces challenges such as compression and decompression overheads. We address these challenges with sparsity-exploiting versions of all-gather, reduce-scatter, and all-reduce collectives. Our implementations use a new bitvector-based format, Pici, designed for low space overhead and fast GPU-based compression and decompression. Further, our collective algorithms adapt to the degree of sparsity in data, modifying data representations during the course of the collective. At 99% input sparsity, our collectives achieve up to 5.25$\times$, 2.5$\times$, and 2.66$\times$ speedups over NCCL for all-gather, reduce-scatter, and all-reduce, respectively. Integrating our collectives into a representative deep learning application, we achieve a 26% end-to-end speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lannie Dalton Hough, Emir Gencer, Hoffmann Muki, Abhinav Bhatele
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
