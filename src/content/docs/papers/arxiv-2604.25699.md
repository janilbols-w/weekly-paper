---
title: "NVLLM: A 3D NAND-Centric Architecture Enabling Edge on-Device LLM Inference"
description: "The rapid growth of LLMs demands high-throughput, memory-capacity-intensive inference on resource-constrained edge devices, where single-batch decoding remains fundamentally memory-bound."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2604.25699) · [PDF](https://arxiv.org/pdf/2604.25699)

## 一句话摘要

The rapid growth of LLMs demands high-throughput, memory-capacity-intensive inference on resource-constrained edge devices, where single-batch decoding remains fundamentally memory-bound.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid growth of LLMs demands high-throughput, memory-capacity-intensive inference on resource-constrained edge devices, where single-batch decoding remains fundamentally memory-bound. Existing out-of-core GPU-based and SSD-like accelerators are limited by DRAM-bound weight movement and inefficient storage access granularity. We present NVLLM, a 3D NAND-centric inference architecture that offloads feed-forward network (FFN) computation into the Flash while executing attention on lightweight CMOS logic with external DRAM. Through wafer-to-wafer stacking, NVLLM tightly integrates multi-plane 3D NAND with compute pipelines, error correction code (ECC) units, and buffers, enabling page-level FFN weight access without DRAM traversal. All GEMM/GEMV operations are decomposed into dot-product primitives executed by out-of-order PE lanes, operating directly on raw NAND reads with integrated ECC. Attention weights remain in DRAM, and a KV-cache-aware scheduler sustains throughput as the context length grows. Evaluated on OPT and LLaMA models with up to 30B parameters, NVLLM achieves a 16.7$\times$--37.9$\times$ speedup over A800-based out-of-core inference and up to 4.7$\times$ speedup over SSD-like designs, with only 2.7\% CMOS area overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingbo Hao, Changwei Yan, Haoyu Cui, Zhihao Yan, Yizhi Ding, Zhangrui Qian, Weiwei Shan
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
