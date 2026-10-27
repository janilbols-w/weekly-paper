---
title: "OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching"
description: "Large language model (LLM) inference serving is increasingly constrained by memory rather than compute."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.08097) · [PDF](https://arxiv.org/pdf/2608.08097)

## 一句话摘要

Large language model (LLM) inference serving is increasingly constrained by memory rather than compute.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference serving is increasingly constrained by memory rather than compute. As long-context and long-form reasoning workloads become more prevalent, the key-value (KV) cache dominates both memory footprint and memory traffic at the token generation (i.e., decode) stage. HBM capacity has therefore become a critical bottleneck, constraining inference batch size and throughput. This paper introduces OasisKV, a memory-centric LLM inference system that alleviates HBM limitations by offloading the KV-cache to alternative memory tiers. Exploiting the sparsity of decode-time attention and leveraging speculative decoding to predict important tokens, OasisKV selectively prefetches and stages only the most relevant KV entries in HBM for efficient LLM inference computation. To support growing LLM context and the larger batches enabled by sparse HBM residency, OasisKV employs tiered KV management across decode, prefill, and remote-memory nodes, relaxing decode-host memory capacity limits under disaggregated serving. An asynchronous prefetch pipeline hides off-GPU transfer latency while bounding per-step traffic to fit the available bandwidth. We implement OasisKV on vLLM. With only 2,048 KV tokens resident in HBM, OasisKV maintains average accuracy within a negligible 0.61 points of full attention on LongBench v2 for long-context understanding and across AIME24-25 and GPQA-Diamond for long-form reasoning. This sparsity translates into a 1.86x throughput gain over vLLM on AIME24. Synthetic long-context workloads further show up to 2.2x higher throughput in multi-GPU serving. Under prefill-decode disaggregation, OasisKV achieves 2.29x vLLM's throughput while supporting 2.42x as many concurrent requests under the same host-memory budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Can Xiao, Sukmin Cho, Junbong We, Zhixiong Niu, Jianyi Cheng, Yiren Zhao, Youngjin Kwon, Yongqiang Xiong, Rui Ma, Junyi Liu
- 发布：2026-08-08；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
