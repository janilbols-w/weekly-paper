---
title: "ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding"
description: "The key-value (KV) cache places growing demands on GPU memory capacity and bandwidth as large language models serve longer contexts and more concurrent requests."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.33719) · [PDF](https://arxiv.org/pdf/2610.33719)

## 一句话摘要

The key-value (KV) cache places growing demands on GPU memory capacity and bandwidth as large language models serve longer contexts and more concurrent requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache places growing demands on GPU memory capacity and bandwidth as large language models serve longer contexts and more concurrent requests. Its footprint limits concurrency, while repeated KV reads during attention can make decoding memory-bandwidth bound. Prior lossless KV cache compression methods reduce transfers between devices but restore the uncompressed KV cache in GPU memory before attention. They therefore leave these repeated KV reads unchanged and require additional work and memory for decompression. We present ZipFusion, which enables attention to consume the losslessly compressed KV cache directly. ZipFusion co-designs the compression format and attention kernel to reduce the bytes read from GPU memory during attention. The kernel reconstructs the original values directly in registers using simple bit operations, avoiding a separate decompression pass and easing the memory-bandwidth bound. ZipFusion also reassigns memory freed by compression across layers to store additional KV cache. Its memory manager reserves space for ongoing generation and makes the remaining capacity available to new requests. We implement ZipFusion on top of FlashInfer and integrate it with SGLang. On an NVIDIA H100, ZipFusion achieves about 1.25x speedup over FlashInfer in decode attention. With 8K context, it improves model decode throughput by up to 26.3% over uncompressed SGLang under the same GPU memory budget. At each method's largest supported batch, it also delivers up to 2.76x the throughput of the best-performing lossless KV cache compression baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuetao Chen, Peng Wang, Hong Xu
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
