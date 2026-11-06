---
title: "CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation"
description: "Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.06501) · [PDF](https://arxiv.org/pdf/2611.06501)

## 一句话摘要

Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency. While Large Language Models (LLMs) excel in offline translation, current LLM-based SimulST systems predominantly rely on prefix-incremental generation. This paradigm suffers from redundant Key-Value cache recomputation and necessitates external Voice Activity Detection to process unbounded streams. To overcome these bottlenecks, we propose an end-to-end interleaved read-write framework built upon an omni-modal LLM. By interleaving speech chunks and text tokens, our architecture achieves full KV cache reuse, natively supporting segmentation-free, infinite-length inference. Furthermore, to learn optimal streaming policies without rigid offline alignments, we introduce a novel Actor-Critic self-enhancement pipeline. An RNN-T Actor dynamically samples read-write trajectories, while an LLM-based Critic evaluates these paths via intrinsic semantic and latency rewards, distilling the optimal policy back to the Actor. Extensive experiments on sentence-level (FLEURS, CoVoST2) and document-level (MuST-C, ACL 60/60) benchmarks demonstrate that our model establishes new state-of-the-art quality-latency Pareto frontiers, substantially outperforming existing cascaded and static-alignment baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chenyang Le, Pei Zhang, Yuxiang Chen, Bing Han, Derek F. Wong, Baosong Yang, Yanmin Qian
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
