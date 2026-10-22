---
title: "HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference"
description: "Large language model (LLM) inference exhibits distinct computational characteristics across its two phases: prefill is compute-intensive, whereas decode is more memory-bound."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.29873) · [PDF](https://arxiv.org/pdf/2610.29873)

## 一句话摘要

Large language model (LLM) inference exhibits distinct computational characteristics across its two phases: prefill is compute-intensive, whereas decode is more memory-bound.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference exhibits distinct computational characteristics across its two phases: prefill is compute-intensive, whereas decode is more memory-bound. As a result, AI accelerators achieve varying levels of efficiency across the two phases. GPUs are well suited to prefill, but are often underutilized during decode. By contrast, NPUs can utilize their compute resources more effectively during decode. Motivated by this observation, we explore a heterogeneous architecture that integrates GPUs and NPUs, mapping prefill to GPUs and decode to NPUs to achieve high performance and efficiency. However, realizing such heterogeneous integration is challenging because LLM phase disaggregation requires KV cache transfer from prefill to decode (that is, from GPUs to NPUs), which is complicated by differences in inter-device communication mechanisms and KV cache tensor layouts. To address this, we propose HAWK, a transfer mechanism that enables rapid KV cache transfer across heterogeneous devices. HAWK establishes a remote direct memory access (RDMA) path for direct cross-device transfers while handling inter-device tensor layout discrepancies as part of the transfer process. In particular, HAWK allocates tensor-layout-aware RDMA buffers on the NPU side to match the target tensor layout. Leveraging these buffers, HAWK orchestrates data transfer from a conventional contiguous GPU RDMA buffer to the corresponding NPU buffers, allowing transferred tensors to be consumed directly without additional data rearrangement while maintaining transfer efficiency. We implement and evaluate HAWK on a system built with commercially available GPUs and NPUs, demonstrating performance within 7.88% of a GPU-only system under the same SLO constraints while achieving up to 1.26$\times$ higher power efficiency and 1.72$\times$ higher cost efficiency.

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

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junhyeok Park, Jungeun Yoon, Kyungmin Kim, Hunsoon Lee, Shinyoung Ahn, Kangho Kim
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
