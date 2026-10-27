---
title: "Accelerating SO(2)-Equivariant Materials Models through Low-Precision Emulation"
description: "Rotationally equivariant architectures improve the physical fidelity of machine-learned (ML) universal materials models based on graph neural networks (GNNs)."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.35164) · [PDF](https://arxiv.org/pdf/2610.35164)

## 一句话摘要

Rotationally equivariant architectures improve the physical fidelity of machine-learned (ML) universal materials models based on graph neural networks (GNNs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Rotationally equivariant architectures improve the physical fidelity of machine-learned (ML) universal materials models based on graph neural networks (GNNs). However, their scalability is limited by the use of non-trivial, high-precision tensor operations during both training and inference. Adopting the reduced-precision formats of matrix multiplication units (MMUs), e.g., FP8 instead of FP32, provides massive increases in throughput, up to 30x (60x) on NVIDIA Hopper (Blackwell) GPUs, but may lead to drastic loss of accuracy. Here, we introduce tailored 'emulated' low-precision operations under the integer Ozaki scheme to accelerate the 'SO(2)-equivariant' processing layers of GNNs, which dominate the runtime of (1) many state-of-the-art ML interatomic potentials (MLIPs) and (2) most universal ML Hamiltonian (MLH) models. Our framework, FlashSO(2), outperforms TF32, the most accurate native low-precision MMU format, in throughput, accuracy, and memory footprint at once. At the SO(2) layer level, it reaches 40x (7x) the throughput of MALOQ's (UMA's) reference implementation, an MLH (MLIP) model, sustaining up to 236 (232) effective Tflop/s on an NVIDIA GH200, 3.5x the FP32 peak. At the model level, FlashSO(2) helps train MALOQ 3.9x faster than its pure-FP32 version while reducing peak memory by 58% at no loss in accuracy. In molecular dynamics simulations with UMA, the speedup factor is 3.3x, and the peak memory is reduced by 51%. FlashSO(2) thus pushes the speed-accuracy Pareto frontier of equivariant materials models beyond the native low-precision formats and substantially lowers the resources required to exploit their scaling laws.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Denghui Lu, Alexander Maeder, Alexandros Nikolaos Ziogas, Mathieu Luisier, Manasa Kaniselvan
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
