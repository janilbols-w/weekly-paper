---
title: "IndexerStage: Staging Indexer-K across Memory Tiers for Sparse-Attention LLM Serving"
description: "Long-context sparse-attention serving can remain limited by graphics processing unit (GPU) memory after attention data is offloaded."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.28625) · [PDF](https://arxiv.org/pdf/2611.28625)

## 一句话摘要

Long-context sparse-attention serving can remain limited by graphics processing unit (GPU) memory after attention data is offloaded.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context sparse-attention serving can remain limited by graphics processing unit (GPU) memory after attention data is offloaded. DeepSeek Sparse Attention retains Indexer-K state to select the tokens that attention will read. Its indexer scans this growing state in full at every layer and decode step. A full scan requires the current layer's state, however, not simultaneous residency of every layer. We present IndexerStage, a serving runtime that externalizes Indexer-K state while preserving native GPU score, top-k, and attention kernels. It stages completed pages through shared execution buffers and preserves new entries locally. Joint memory-and-transfer admission checks storage and each layer's transfer demand before accepting a growing batch. The backing tier gathers pages; the model-serving GPU controls transfer timing and byte budgets. We implement IndexerStage in SGLang on 16 model-serving and 16 backing H800 GPUs. Across 16K--64K inputs, local streaming storage occupies 0.65--0.70 GiB per model-serving GPU. Relative to host-memory-backed HiSparse, batch size increases by 12.28--23.08% and decode throughput in tokens per second (TPS) reaches 1.08--1.14x. At 64K with the latent-KV backing path fixed, the larger batch achieves 1.10x decode TPS; enabling streaming at batch size 24 adds 2.42% to time per output token. Mixed-length dynamic serving increases mean generating batch size by 12.07% and delivers 1.31x decode TPS.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, serving runtime
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xin Zhang, Weifeng Zhang, Xianyan Xie, Huijun Shen, Xijin Yin, Zhen He, Yinben Xia, Xiang Li, ZeKun He, Yachen Wang, Xianneng Zou, Guo Chen
- 发布：2026-11-21；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
