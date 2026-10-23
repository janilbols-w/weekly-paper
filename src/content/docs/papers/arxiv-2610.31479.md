---
title: "Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon"
description: "Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.31479) · [PDF](https://arxiv.org/pdf/2610.31479)

## 一句话摘要

Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads. Which optimizations retain their benefits when moved to Apple Silicon, and what determines their applicability? We evaluate four optimization families: KV-cache pruning, speculative decoding, ported GPU kernels, and post-training quantization. Experiments span four Apple machines under a common single-request decode workload, with matched RTX 4090 comparisons where possible. KV-cache pruning can reach up to 1.75 times end-to-end throughput on Apple but can reduce throughput on desktop NVIDIA GPUs. Under the common benchmark, all evaluated speculative decoding methods reduce throughput on Apple, despite reported 2-6 times gains on server GPUs. CUDA kernel designs transfer only partially: public Metal lacks asynchronous copy, and batch-one decode makes several serving-oriented mechanisms inapplicable, although transferable components yield up to 1.20 times decode throughput. Quantization gains vary by machine. Across four families, a reported speedup is not a portable property of a technique alone but a joint function of technique, runtime, hardware contract, and workload regime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kyrylo Yemets, Andrii Yaroshevych, Victor Muryn, Ostap Khomenko, Pavlo Kryven, Maksym Kmet, Maksym Shamrai, Mariya Hirna
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
