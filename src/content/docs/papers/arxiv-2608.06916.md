---
title: "MiCoPro: End-to-End Mixed Precision HW/SW Co-design with HW-aware Proxy Model"
description: "Quantized Neural Networks~(QNN) with low-bitwidth data have proven promising in efficient storage and computation on edge devices."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06916) · [PDF](https://arxiv.org/pdf/2608.06916)

## 一句话摘要

Quantized Neural Networks~(QNN) with low-bitwidth data have proven promising in efficient storage and computation on edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantized Neural Networks~(QNN) with low-bitwidth data have proven promising in efficient storage and computation on edge devices. To mitigate accuracy degradation while maximizing speedup, layer-wise mixed-precision quantization~(MPQ) becomes a popular solution. However, existing algorithms for exploring MPQ schemes are limited in flexibility and efficiency. Comprehending the complex impacts of different MPQ schemes on post-training quantization and quantization-aware training results is a challenge for conventional methods. Furthermore, an end-to-end framework for the optimization and deployment of MPQ models is missing in existing work. To address these challenges, we propose the MiCo framework, a holistic MPQ exploration and deployment framework for edge AI applications. The framework adopts a novel optimization algorithm to search for accuracy-optimal quantization configurations under strict latency constraints. We further extended the framework to MiCoPro, which introduces a robust Hardware-Aware Proxy (HAP) model to enhance prediction accuracy and hardware versatility. By leveraging target-specific latency modeling, MiCoPro enables rapid exploration and direct deployment from PyTorch models to bare-metal C code. We demonstrate the versatility of our framework on both the BitFusion accelerator and SIMD-extended RISC-V processors, achieving up to 40\% of latency reduction with less than 3\% of accuracy drop.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zijun Jiang, Yangdi Lyu
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
