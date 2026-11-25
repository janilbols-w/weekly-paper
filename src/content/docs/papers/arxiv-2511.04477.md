---
title: "Practical activation sparsity for quantized LLMs on personal devices"
description: "Large language models (LLMs) increasingly run on personal devices, where generating text is slow: producing each token requires reading all of the model's weights from memory."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2511.04477) · [PDF](https://arxiv.org/pdf/2511.04477)

## 一句话摘要

Large language models (LLMs) increasingly run on personal devices, where generating text is slow: producing each token requires reading all of the model's weights from memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) increasingly run on personal devices, where generating text is slow: producing each token requires reading all of the model's weights from memory. Two techniques reduce this memory traffic. Quantization stores the weights in 4 to 8 bits. Activation sparsity treats near-zero activations as zero and skips the weights they multiply; prior work shows that it skips 40-50% of the weights of modern LLMs without retraining, at little loss in accuracy, also on quantized models. Yet the two do not combine in execution: a quantization format packs the weights that multiply many consecutive activations into one block, and a block can be skipped only if all of these activations are near zero, which rarely happens. Moreover, the near-zero activations change with every token, so balancing the GPU's load and finding them add run-time overhead. We present SpQt, which makes activation sparsity practical for quantized LLMs. SpQt (1) stores each activation's quantized weights contiguously, in a zigzag layout that keeps the quantization formats unchanged; (2) divides the nonzero activations evenly among groups of GPU threads, so the load stays balanced; and (3) finds the nonzero activations inside kernels that each decode step already runs before its matrix products, such as normalization, so that finding them adds no kernel launch. Built into llama.cpp and tested on five devices from a phone to a desktop, with Apple and NVIDIA GPUs and four quantization formats, SpQt generates tokens 1.45-2.15x faster than llama.cpp at 50% sparsity, with up to 2.6x less energy per token. With SpQt, a device can choose a sparsity level in addition to a quantization format, trading a small loss in accuracy for speed and energy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rongxiang Wang, Kangyuan Shu, Felix Xiaozhu Lin
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
