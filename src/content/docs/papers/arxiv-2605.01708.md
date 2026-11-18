---
title: "SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving"
description: "Contemporary systems serving large language models (LLMs) have adopted prefill-decode disaggregation to load-balance between the compute-bound prefill phase and the memory-bound decode phase."
---

**评分：52/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2605.01708) · [PDF](https://arxiv.org/pdf/2605.01708)

## 一句话摘要

Contemporary systems serving large language models (LLMs) have adopted prefill-decode disaggregation to load-balance between the compute-bound prefill phase and the memory-bound decode phase.

## 为什么值得关注

待编辑增强。

## 摘要原文

Contemporary systems serving large language models (LLMs) have adopted prefill-decode disaggregation to load-balance between the compute-bound prefill phase and the memory-bound decode phase. Under this design, prefill workers generate a KV cache that must be transferred to decode workers before generation can begin. With these workers residing on different physical systems, this transfer becomes a significant bottleneck to serving LLMs at scale, especially for long-input and agentic workloads. Existing lossless codecs are unsuitable here as they primarily target offline weight compression, run on CPUs, or use variable-length coding whose compression cannot keep up with KV production during prefill. We introduce SplitZip, a GPU-friendly lossless compressor for KV cache transfer that preserves KV tensors bitwise and integrates into existing serving frameworks without modifying model execution. SplitZip exploits redundancy in floating-point exponents of KV activations, encoding frequent exponent values with fixed-length codes and routing rare exponents through a sparse escape stream of (position, value). A calibrated top-16 exponent codebook eliminates online histogramming, while the regular dense path and sparse escape correction make both encoding and decoding efficient on GPUs. On real BF16 activation tensors, SplitZip achieves $613.3$ GB/s compression throughput and $2181.8$ GB/s decompression throughput, outperforming prior lossless compressors on the critical codec path. End-to-end transfer experiments show up to $1.32\times$ speedup for BF16 KV cache transfer, $1.30\times$ speedup for TTFT, and $1.23\times$ increase in Request Throughput. The same approach extends to FP8 KV caches, providing up to $1.14\times$ compression over native E5M2. Code is available at https://github.com/Intelligent-Microsystems-Lab/SplitZip

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yipin Guo, Siddharth Joshi
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Intelligent-Microsystems-Lab/SplitZip](https://github.com/Intelligent-Microsystems-Lab/SplitZip)
- 阅读深度：metadata
