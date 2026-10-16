---
title: "Joint Subspace Sparse Attention for Efficient Long-Context Decoding"
description: "Sparse attention reduces the KV-cache traffic that dominates long-context LLM decoding, but practical methods largely operate at coarse granularity."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.19026) · [PDF](https://arxiv.org/pdf/2610.19026)

## 一句话摘要

Sparse attention reduces the KV-cache traffic that dominates long-context LLM decoding, but practical methods largely operate at coarse granularity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention reduces the KV-cache traffic that dominates long-context LLM decoding, but practical methods largely operate at coarse granularity. Token-level selection offers finer control, yet presents two challenges: low-dimensional scoring may lose query--key structure needed for accurate ranking, while gathering scattered selected tokens can offset the resulting latency benefit. We introduce Joint Subspace Sparse Attention (JSSA) to address both challenges. For selection quality, JSSA learns a shared low-dimensional query--key subspace by minimizing token-score preservation error. We upper-bound the resulting non-convex objective with a tractable marginal objective that admits a closed-form spectral solution; direct refinement of the exact objective provides no measurable improvement in the tested settings. For execution efficiency, we develop a gather-free token-level indexed-attention kernel that supports distinct per-KV-head selections under the standard grouped-query attention (GQA) KV-cache layout. Across standard GQA, hybrid sliding-window/global attention, and Multi-head Latent Attention (MLA) models, JSSA consistently remains close to full-KV accuracy while avoiding the substantial generation-length inflation and architecture-dependent failures observed with competing methods. On an NVIDIA B200 GPU, JSSA achieves up to $6.43\times$ the decoding throughput of full-KV attention at 128K context. JSSA achieves reasoning accuracy comparable to model-native DSA without model training and reaches 96--99\% of its decoding throughput even at 700B scale large models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiwon Song, Yoongon Kim, Jae-Joon Kim
- 发布：2026-10-13；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
