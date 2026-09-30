---
title: "SparSP: Exploiting Communication Sparsity for Sequence-Parallel Video DiTs"
description: "Diffusion Transformers have become the dominant architecture for video generation."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32197) · [PDF](https://arxiv.org/pdf/2609.32197)

## 一句话摘要

Diffusion Transformers have become the dominant architecture for video generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Transformers have become the dominant architecture for video generation. Their substantial computational cost motivates scaling inference across multi-GPU servers, yet efficient scaling remains challenging on commodity GPUs connected via PCIe, whose bandwidth is limited. Although sparse attention substantially reduces computation, its implications for communication remain underexplored. This paper argues that attention sparsity should be treated as a communication primitive. We present SparSP, an efficient sparse sequence parallel communication system that co-designs token distribution, communication routing, and asynchronous execution for sparse video diffusion models. First, Dependency-Aware Placement distributes sequence blocks according to diffusion models' sparse attention patterns. Second, Demand-Directed KV Routing transfers KV blocks directly to requesting GPUs without intermediate relays. Third, a Decoupled Transfer Runtime separates communication from GPU computation to reduce resource contention and maximize effective bandwidth. Our evaluation shows that SparSP improves attention performance by 1.38- 1.5$\times$, achieves an average 1.17$\times$ (up to 1.69$\times$) end-to-end speedup across three representative servers and three video diffusion models, and reduces communication volume by 12.54-23.05%. Moreover, we achieve an average 1.53-1.76$\times$ bandwidth improvement over NCCL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Desen Sun, Xinrui Zhong, Yuke Wang, Sihang Liu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
