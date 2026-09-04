---
title: "HARP: Hadamard-Preconditioned Adaptive Rotation Processor for Extreme LLM Quantization"
description: "Post-training quantization (PTQ) is essential for deploying LLMs under memory and bandwidth constraints."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.29843) · [PDF](https://arxiv.org/pdf/2605.29843)

## 一句话摘要

Post-training quantization (PTQ) is essential for deploying LLMs under memory and bandwidth constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) is essential for deploying LLMs under memory and bandwidth constraints. However, extreme low-bit quantization remains highly sensitive to activation outliers and anisotropic weight curvature. Existing incoherence-based PTQ methods mitigate this issue with fixed randomized Hadamard transforms (RHTs), which improve quantization robustness but cannot adapt the rotated basis to the layer, calibration distribution, or quantizer. We introduce HARP (Hadamard-preconditioned Adaptive Rotation Processor), a learnable structured two-sided orthogonal processor that replaces fixed Hadamard mixing while preserving exact full-precision equivalence. HARP represents each rotation as a product of sparse butterfly-like block-orthogonal stages, supports non-power-of-two dimensions through Mixed-Radix schedules, and initializes to the RHT processor up to a fixed permutation. Fitted only on calibration data, HARP adapts the quantization basis to each layer and backend. Across 2--4-bit settings on Llama models from 1B to 70B, HARP consistently improves perplexity and yields its clearest zero-shot gains at 2 bits; a 2-bit Qwen3-8B experiment shows the same transfer beyond the Llama family. HARP also preserves deployment efficiency: on Llama 2 7B at 2 bits, it reaches 128 tok/s, retaining 90% of RHT throughput (142 tok/s) and running approximately $2.1\times$ faster than FP16 (61 tok/s).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Artur Zagitov, Gleb Molodtsov, Aleksandr Beznosikov
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
