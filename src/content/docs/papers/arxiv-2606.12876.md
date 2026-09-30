---
title: "Multi-Bitwidth Quantization for LLMs Using Additive Codebooks"
description: "As large language models (LLMs) are increasingly deployed across heterogeneous hardware with varying resource constraints, the ability to adaptively manage the performance-efficiency trade-off without retraining is critical."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.12876) · [PDF](https://arxiv.org/pdf/2606.12876)

## 一句话摘要

As large language models (LLMs) are increasingly deployed across heterogeneous hardware with varying resource constraints, the ability to adaptively manage the performance-efficiency trade-off without retraining is critical.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) are increasingly deployed across heterogeneous hardware with varying resource constraints, the ability to adaptively manage the performance-efficiency trade-off without retraining is critical. We propose Drop-by-Drop, a novel multi-bitwidth post-training quantization framework enabling inference-time precision control over LLM weights from a single quantized model. As theoretical motivation, we prove that Gaussian sources are successively refinable under a weighted mean squared error distortion motivated by LLM loss functions: successive refinement across distortion levels incurs no rate penalty relative to encoding at each level separately. Drop-by-Drop approximates this hierarchical structure in practice by incorporating Matryoshka-style supervision into additive codebook training, inducing an ordering in which codebook prefixes yield accurate partial reconstructions at each precision level. Furthermore, a block-Hadamard rotation brings the weight distribution closer to our Gaussian source assumption. The result is a single model that serves multiple bitwidths by dropping codebooks, reducing storage and quantization cost relative to the static per-bitwidth models. Across Qwen, LLaMA, Gemma, and Mistral, Drop-by-Drop achieves lower perplexity than state-of-the-art multi-bitwidth methods with competitive zero-shot accuracy, while our specialized kernels further reduce decoding latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liza Babaoglu, Shuangyi Chen, Ashish Khisti
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
