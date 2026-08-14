---
title: "vToken: Token-Level Virtualization for Reclaimable KV Caches"
description: "Large language model serving faces a critical memory bottleneck: the KV cache grows with sequence length and batch size."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.13263) · [PDF](https://arxiv.org/pdf/2608.13263)

## 一句话摘要

Large language model serving faces a critical memory bottleneck: the KV cache grows with sequence length and batch size.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model serving faces a critical memory bottleneck: the KV cache grows with sequence length and batch size. PagedAttention uses fixed-size memory blocks to reduce allocator-level fragmentation, but recent KV eviction algorithms operate at a token granularity finer than block-level management. This mismatch causes intra-block fragmentation, leaving a large fraction of allocated KV memory unreclaimable. We present vToken, a lightweight token-level virtualization layer that decouples logical token liveness from physical block placement. vToken maintains a stable logical token view through token-table indirection and realizes physical reclamation by repacking live tokens asynchronously. The design preserves PagedAttention kernels and CUDA Graph compatibility. We implement vToken in vLLM and evaluate it with H2O, Random, and Scissorhands across models. Compared with a paired Naive-Evict baseline, vToken reduces retained KV blocks per request by 27.2\%--72.3\% and improves SLA-constrained throughput by up to 1.37$\times$. Under a constrained active-KV budget, it extends the maximum feasible concurrency by up to 2$\times$, while reducing the per-policy integration footprint from 500+ lines to under 50.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanhang Gao, Xiangrui Yang, Yuanfeng Chen, Hongjia Chen, Qianru Lv, Wenfei Wu, Dongsheng Li
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
