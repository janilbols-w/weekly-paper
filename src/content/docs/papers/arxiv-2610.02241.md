---
title: "Hardware-Native Joint Sparse-Quantization for Trillion-Scale Mixture-of-Experts"
description: "Mixture-of-Experts (MoE) architectures allow frontier language models to scale to trillions of parameters, but their deployment is constrained by massive memory footprints and memory-bandwidth limitations."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.02241) · [PDF](https://arxiv.org/pdf/2610.02241)

## 一句话摘要

Mixture-of-Experts (MoE) architectures allow frontier language models to scale to trillions of parameters, but their deployment is constrained by massive memory footprints and memory-bandwidth limitations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architectures allow frontier language models to scale to trillions of parameters, but their deployment is constrained by massive memory footprints and memory-bandwidth limitations. Although modern accelerators provide Sparse Tensor Cores (SpTCs) that reduce weight storage and increase throughput through low-precision semi-structured sparsity, exploiting them for MoEs remains challenging because of substantial model-quality degradation and the lack of grouped sparse GEMM primitives. We present an end-to-end hardware-software co-design framework that compresses expert weights into hardware-native, low-precision sparse representations and accelerates their execution on SpTCs. Algorithmically, our framework relaxes discrete semi-structured support selection through continuous reparameterization, enabling differentiable joint optimization with quantized weights under a router-weighted reconstruction objective and scalable expert-parallel compression. Systemically, we develop a custom grouped sparse GEMM kernel tailored to low-precision sparse MoE inference on SpTCs. Across MoE models ranging from 30 billion to one trillion parameters, our framework improves state-of-the-art joint sparse-quantization accuracy by up to 4.35 percentage points while preserving 96.09% of the original model's performance. On NVIDIA B200 GPUs, our kernel outperforms the vendor baseline by up to $1.65\times$, increasing serving throughput by $1.18\times$ and reducing end-to-end latency by up to $4.03\times$. These results establish hardware-software co-design as a practical path toward scalable and efficient MoE deployment.

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

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kwanhee Lee, Namhoon Lee, Dan Alistarh
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
