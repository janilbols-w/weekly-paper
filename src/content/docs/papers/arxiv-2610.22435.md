---
title: "TRACE: Transformer Residual Activation Codebook Encoding for Communication-efficient Distributed Edge Inference"
description: "Distributed Transformer inference across co-located edge devices is fundamentally communication-bound, as exchanging activations between sequence-parallel partitions dominates inference latency under commodity edge bandwidths."
---

**评分：47/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.22435) · [PDF](https://arxiv.org/pdf/2610.22435)

## 一句话摘要

Distributed Transformer inference across co-located edge devices is fundamentally communication-bound, as exchanging activations between sequence-parallel partitions dominates inference latency under commodity edge bandwidths.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed Transformer inference across co-located edge devices is fundamentally communication-bound, as exchanging activations between sequence-parallel partitions dominates inference latency under commodity edge bandwidths. Existing compression schemes reduce this cost but retain a structural bottleneck: the received data must still undergo key/value projection before attention can proceed, serializing computation behind communication. This paper presents Transformer Residual Activation Codebook Encoding (Trace), a framework that addresses these limitations. Trace places a Vector Quantizer (VQ) at the post-attention residual of every Transformer layer and precomputes codebook-indexed key/value representations. During inference, exchanged activations are encoded into compact codebook indices, allowing receivers to directly recover keys and values through table lookup instead of executing the downstream computations required to derive them. By eliminating the received data downstream computation, Trace enables communication--computation overlap and reduces a key latency bottleneck in distributed Transformer inference. A hierarchical clustering further structures the learned codebook into a multi-resolution hierarchy, enabling runtime adaptation of the communication bitrate without retraining. The framework supports two operating variants: one prioritizing accuracy and the other balancing accuracy and efficiency through buffer-compatible quantization. Experiments on ViT-Base (ImageNet-1K and CIFAR-100) and ViViT-B (UCF-101) show that Trace achieves up to 1.89% higher accuracy and up to 1.27x end-to-end inference speedup compared with the state-of-the-art VQ-based distributed inference framework. Compared with uncompressed sequence-parallel inference, Trace reduces communication overhead by up to 22,624x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Muhammad Azlan Qazi, Alexandros Iosifidis, Qi Zhang
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
