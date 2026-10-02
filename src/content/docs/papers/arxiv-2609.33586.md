---
title: "Approximating Softmax in Pretrained LLMs: Model Sensitivity and Kernel Acceleration"
description: "On NVIDIA Blackwell B200, tensor-core throughput outpaces special-function exponential throughput by more than two orders of magnitude, exposing exponential evaluation in fused attention kernels."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.33586) · [PDF](https://arxiv.org/pdf/2609.33586)

## 一句话摘要

On NVIDIA Blackwell B200, tensor-core throughput outpaces special-function exponential throughput by more than two orders of magnitude, exposing exponential evaluation in fused attention kernels.

## 为什么值得关注

待编辑增强。

## 摘要原文

On NVIDIA Blackwell B200, tensor-core throughput outpaces special-function exponential throughput by more than two orders of magnitude, exposing exponential evaluation in fused attention kernels. A pretrained Transformer, however, may not need it evaluated accurately at every element. We characterize what a pretrained model does need by approximating softmax at inference in ten frozen decoder-only models (0.5B-72B). The number of positions the softmax map assigns probability to and within-row resolution can be cut substantially, yet uniform weighting of the same positions is damaging. Where a fixed resolution budget is placed matters as much as its size, with resolution near the row maximum consistently favored. Perturbations matched on scalar distortion produce model-dependent responses of opposite sign. These findings motivate Rowmax-PoT, a coarse logarithmic weight representation anchored at each row maximum, and Rowmax-H15, its hardware specialization in FlashAttention-4. On B200, the patched FP8 attention forward is 12.4% faster at causal 8K and 25.8% faster at non-causal 8K in host-side call-latency measurements; board energy per forward falls by 8.4% at causal 16K. Measured separately on the BF16 kernel path at 2K, Rowmax-H15 increases perplexity by 0.091-0.492% across five models from three families.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shangzhen Zhu, Muyan Hu, Tomasz Kozlowski
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
