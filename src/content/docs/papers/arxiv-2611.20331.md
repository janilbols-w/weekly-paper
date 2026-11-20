---
title: "LENS: Replacing LayerNorm and Softmax in Transformers with Learnable Normalization States"
description: "LayerNorm and attention Softmax are critical operations in Transformers."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.20331) · [PDF](https://arxiv.org/pdf/2611.20331)

## 一句话摘要

LayerNorm and attention Softmax are critical operations in Transformers.

## 为什么值得关注

待编辑增强。

## 摘要原文

LayerNorm and attention Softmax are critical operations in Transformers. However, they cannot be efficiently mapped to General Matrix Multiplication (GEMM) computations on hardware. Therefore, modern hardware accelerator designs, such as NPUs on ASIC/FPGA, consume a large amount of hardware resources or chip area to implement their specific arithmetic units. Building on previous work about LayerNorm, Softmax, and their alternatives, we introduce Learnable Normalization States (LENS), a framework that reformulates LayerNorm as tiny MLPs by abstracting a common structure from related methods and extends this method to Softmax, which moves more of the computation in Transformers to GEMM as a hardware-friendly architecture. We evaluate LENS on image classification with Vision Transformers (ViT) and autoregressive language modeling with Pythia models, including generalization tests on WikiText and LAMBADA. Across these tasks, LENS matches or exceeds baseline performance in several vision settings and retains most of the baseline performance in the remaining vision and language experiments. These findings may suggest that hand-designed normalization and attention functions are not the only choice as alternatives to LayerNorm and Softmax. LENS also provides a basis for exploring Transformer architectures for resource-limited accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuhao Liu, Salim Ullah, Akash Kumar
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/liuyh-Horizon/LENS](https://github.com/liuyh-Horizon/LENS)
- 阅读深度：metadata
