---
title: "HyCoInfer: Cloud-Edge Collaborative Inference for Large Language Models on Heterogeneous GPU-FPGA Architectures"
description: "Large language model (LLM) serving relies predominantly on cloud GPUs, yet autoregressive decoding is memory-bound and often leaves their arithmetic units underutilized."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.22086) · [PDF](https://arxiv.org/pdf/2611.22086)

## 一句话摘要

Large language model (LLM) serving relies predominantly on cloud GPUs, yet autoregressive decoding is memory-bound and often leaves their arithmetic units underutilized.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving relies predominantly on cloud GPUs, yet autoregressive decoding is memory-bound and often leaves their arithmetic units underutilized. Edge FPGAs offer attractive decoding efficiency, but are ill suited to sustaining a high-concurrency serving workload alone. This paper presents HyCoInfer, a heterogeneous cloud-edge serving system that assigns prefill to cloud GPUs and distributes decoding across cloud GPUs and edge FPGAs. The design addresses three barriers to practical offloading: capacity balancing across heterogeneous accelerators, the large KV cache crossing a constrained wide-area link, and the latency added by heterogeneous execution. HyCoInfer incorporates FPGA decode capacity into GPU prefill/decode role partitioning and places requests according to queue load, prompt length, and network state. It further combines layer-wise pipelined transfer, decoder-side precomputation, and bandwidth-adaptive KV cache compression based on residual vector quantization. We implement HyCoInfer using two NVIDIA V100 GPUs and an AMD Xilinx Alveo U280 and evaluate it over 100-1000 Mbps links. At 500 Mbps, HyCoInfer delivers up to 4.11 times the request goodput of cloud-only vLLM and reduces mean end-to-end latency by up to 61.1%. Across different network conditions and workloads, the system improves overall serving capacity, with the largest gains on communication-intensive tasks, and reduces per-request energy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zewen Huang, Xiangwen Zhuge, Yingkun Hu, Zheng Yang, Qiang Ma
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
