---
title: "Format-Aware Fusion for Fast FP4 Pretraining"
description: "Four-bit floating-point (FP4) Tensor Cores accelerate matrix multiplication, but scale computation, operand packing, layout construction, and saved backward state can erase the gain."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00053) · [PDF](https://arxiv.org/pdf/2610.00053)

## 一句话摘要

Four-bit floating-point (FP4) Tensor Cores accelerate matrix multiplication, but scale computation, operand packing, layout construction, and saved backward state can erase the gain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Four-bit floating-point (FP4) Tensor Cores accelerate matrix multiplication, but scale computation, operand packing, layout construction, and saved backward state can erase the gain. We present \emph{format-aware fusion}, which co-designs each quantization producer with its scale domain and consumer layout for native \mxfp{}, global \nvfp{}, and cooperative-thread-array-local \nvfp{}. We evaluate Llama-3-family 8B pretraining through 160 billion tokens using bfloat16 output projections and compiled cross entropy. In matched same-accelerator probes, bfloat16 and Transformer Engine \nvfp{} reach 18.8K and 27.6K tokens/s/GPU, while our fastest custom route reaches 37.9K. \mxfp{} with row-gradient stochastic rounding and fixed-sign 32-value Hadamard weight-gradient preconditioning reaches 37.2K tokens/s/GPU (86.3\% bfloat16 model FLOP utilization) and ends 2.11\% above the raw bfloat16 training-loss endpoint. A Transformer Engine recipe with four final bfloat16 blocks ends 0.87\% above bfloat16 at 27.1K tokens/s/GPU. Downstream rankings differ from training-loss rankings, showing that FP4 outcomes depend jointly on scale contract, operand, and execution path.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Robert Hu
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
