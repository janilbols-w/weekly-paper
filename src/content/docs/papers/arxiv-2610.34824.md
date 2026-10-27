---
title: "SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference"
description: "LLMs on edge devices are constrained by limited memory and bandwidth."
---

**评分：51/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.34824) · [PDF](https://arxiv.org/pdf/2610.34824)

## 一句话摘要

LLMs on edge devices are constrained by limited memory and bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLMs on edge devices are constrained by limited memory and bandwidth. Although 1.58-bit ternary weights greatly reduce model storage, long-context inference is increasingly bottlenecked by KV-cache traffic and attention. Existing accelerators also use separate datapaths for ternary linear layers and attention, incurring hardware and execution overhead. We present SPARTA, a sparse ternary LLM accelerator for efficient long-context edge inference. SPARTA integrates: (1) a phase-aware sparse dataflow exploiting heterogeneous sparsity across compute-bound prefill and memory-bound decode; (2) a unified compute fabric mapping ternary SpMM/SpMV and bit-serial attention onto shared processing elements to exploit zero-weight and zero-bit sparsity; and (3) an adaptive two-stage attention engine combining page-level Top-k selection to reduce K-cache accesses with token-level Top-p pruning to reduce V-cache traffic. SPARTA reduces KV traffic by 4.1-4.8x over full attention and 1.3-1.5x over a state-of-the-art sparse-attention scheme, with task-dependent quality loss. Compared with NVIDIA Jetson AGX Orin, SPARTA achieves 3.9x higher generation throughput and 8.3x higher end-to-end energy efficiency on average; versus AMD Ryzen 7 9700X, the gains are 5.0x and 81.7x. It also delivers 1.6-12.0x higher throughput, 2.0-4.2x higher energy efficiency, and 1.3-51.4x higher area efficiency than FIGLUT, TeLLMe, and MCBP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, edge inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yanzhen Zhou, Zhengyu Han, Qunyou Liu, Zheyu Yan, Weihong Xu, Cheng Zhuo
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
