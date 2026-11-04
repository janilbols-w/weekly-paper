---
title: "HERALD: High-Throughput Block Diffusion LLM Inference via CPU-GPU Cooperative KV Cache Retrieval"
description: "Block diffusion LLMs (block dLLMs) improve decode throughput by generating tokens in parallel, and are emerging as a next-generation alternative to autoregressive LLMs."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.21633) · [PDF](https://arxiv.org/pdf/2606.21633)

## 一句话摘要

Block diffusion LLMs (block dLLMs) improve decode throughput by generating tokens in parallel, and are emerging as a next-generation alternative to autoregressive LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block diffusion LLMs (block dLLMs) improve decode throughput by generating tokens in parallel, and are emerging as a next-generation alternative to autoregressive LLMs. At long contexts, however, the KV cache remains a major throughput bottleneck in both memory bandwidth and capacity. For autoregressive LLMs, dynamic sparse attention is often combined with KV offloading to alleviate both bottlenecks, keeping the full KV cache in CPU DRAM and fetching only a critical subset to the GPU. However, KV subset selection and retrieval over bandwidth-limited PCIe incur substantial offloading overheads that often stall the GPU. We present HERALD, the first dynamic sparse attention method for block dLLMs that supports KV offloading. HERALD exploits a property of block dLLMs: a critical KV subset selected once per block is reused across all of its denoising steps, so the next block's selection can be hidden behind the current block's denoising. HERALD realizes this with a two-stage selection algorithm co-designed with its execution system. While the GPU denoises the current block, the CPU speculatively searches the full KV cache for the next block with a single query merged from the current block's B queries, cutting the selection compute by Bx; the GPU then refines the candidates into the final top-K subset with the next block's real queries. At K=1024, HERALD achieves near-lossless accuracy relative to Dense on LongBench and reasoning tasks across four block dLLMs, and improves decode throughput by up to 3.70x over Dense GPU-only inference, 2.59x over MAGE, a state-of-the-art block-dLLM sparse attention method, and 8.38x over MAGE-Offload, its direct KV-offloading extension.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Omin Kwon, Doyeon Kim, Jongseok Park, Seung Yul Lee, Ion Stoica, Jae W. Lee
- 发布：2026-08-04；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
