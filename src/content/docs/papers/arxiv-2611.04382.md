---
title: "Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving"
description: "KV cache compression reduces the communication volume of disaggregated large language model serving, but its practical benefit depends not only on compression ratio and model quality, but also on how efficiently the compression pipeline executes."
---

**评分：54/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.04382) · [PDF](https://arxiv.org/pdf/2611.04382)

## 一句话摘要

KV cache compression reduces the communication volume of disaggregated large language model serving, but its practical benefit depends not only on compression ratio and model quality, but also on how efficiently the compression pipeline executes.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache compression reduces the communication volume of disaggregated large language model serving, but its practical benefit depends not only on compression ratio and model quality, but also on how efficiently the compression pipeline executes. This requirement becomes increasingly important as modern serving systems adopt high-bandwidth interconnects, where inefficient compression can offset a substantial portion of the saved communication time. This paper presents FastKVComp, a high-throughput KV cache compression data path built on top of KVServe. FastKVComp improves compression execution in two complementary ways. First, it fuses the distribution transformation and low-bit quantization stages into a KVaware TileLang kernel, eliminating intermediate tensor materialization and redundant memory accesses. Second, it replaces the original lossless compression backend with an open, extensible, and searchable backend based on LC, enabling high-performance compression operator pipelines. The fused kernel achieves up to 5.9x speedup, while the new lossless backend increases compression throughput from below 90 GB/s to over 500 GB/s. Across the evaluated workloads, FastKVComp reduces job completion time by up to 2.04x. End-to-end evaluation shows that these optimizations allow KV compression to retain meaningful communication benefits under modern high-bandwidth network.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Junhong Wu, Zedong Liu, Xinyang Ma, Yuhan Chen, Guangming Tan, Dingwen Tao
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
