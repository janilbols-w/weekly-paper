---
title: "OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching"
description: "Large language model (LLM) inference serving is increasingly constrained by memory rather than compute."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.08097) · [PDF](https://arxiv.org/pdf/2608.08097)

## 一句话摘要

Large language model (LLM) inference serving is increasingly constrained by memory rather than compute.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference serving is increasingly constrained by memory rather than compute. As long-context and long-form reasoning workloads become more prevalent, the key-value (KV) cache dominates both memory footprint and memory traffic during LLM token generation, i.e., decode. In particular, HBM capacity has become a scarce and costly resource that heavily limits inference batch size and system throughput. This paper presents OasisKV, a memory-centric LLM inference system design that alleviates HBM capacity pressure by decoupling full KV-cache storage from HBM during LLM decoding. Because decode-time attention is naturally sparse, OasisKV keeps only the KV entries of the most relevant tokens in HBMs for attention computation. We observe that future important tokens can be predicted accurately in advance using lookahead tokens drafted by speculative decoding (SD). OasisKV employs an efficient attention background pipeline to identify important KV blocks. They are then prefetched from higher-capacity memory tiers (e.g., host or remote memory) and staged in HBMs before being used in the next decode step. We implement OasisKV based on vLLM. The lookahead prediction is accurate enough to keep accuracy within 0.7 points of full attention under a 2,048-token KV budget. This lets OasisKV turn sparsity into throughput gain: $1.69\times$ over dense vLLM on the reasoning workload at 0.1 points of accuracy loss, and up to $2.1\times$ on multi-GPU long-context serving. Under prefill--decode disaggregation, OasisKV reaches about $2\times$ dense throughput while admitting each request with $6.5$--$9.7\times$ less KV and holding $2.2$-$2.6$ less decode-node host memory than full KV transfer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Can Xiao, Sukmin Cho, Junbong We, Zhixiong Niu, Jianyi Cheng, Yiren Zhao, Youngjin Kwon, Yongqiang Xiong, Rui Ma, Junyi Liu
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
