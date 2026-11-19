---
title: "The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale"
description: "Kernelized attention methods, which aim to replace the $O(N^2)$ complexity of softmax attention with $O(N)$ alternatives, have been the focus of intense research in the last five years."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.22947) · [PDF](https://arxiv.org/pdf/2611.22947)

## 一句话摘要

Kernelized attention methods, which aim to replace the $O(N^2)$ complexity of softmax attention with $O(N)$ alternatives, have been the focus of intense research in the last five years.

## 为什么值得关注

待编辑增强。

## 摘要原文

Kernelized attention methods, which aim to replace the $O(N^2)$ complexity of softmax attention with $O(N)$ alternatives, have been the focus of intense research in the last five years. Despite growing interest, systematic evaluations and fair comparisons across approaches and scales are still missing. We analyze kernelized attention in two halves and highlight prominent limitations on each. On efficiency, FlashAttention achieves lower memory consumption and faster wall-clock time than SOTA kernelized methods during training and in vision transformers across most sequence lengths (with inference-time memory in causal language models the only clear exception), contradicting the core assumption for pure kernelized attention used as a drop-in replacement for softmax. We also discover that reported efficiency gains often fail to reproduce against modern baselines. On quality, current kernelized methods leave gaps of 2-10 points relative to softmax under a unified distillation protocol, and model scala alone does not close these gaps. We show this gap is not intrinsic to kernelization: LARA++, a principled extension of LARA that approximates softmax via importance sampling with adaptive proposal distributions, recovers up to 99% of softmax accuracy. We establish that the gap is closable; however, the computational overhead remains substantial, leaving the efficiency wall intact. Code is available at https://github.com/firatoncel/KernelRealityCheckNeurIPS2026

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：F{\i}rat \"Oncel, Cem Subakan, Mirco Ravanelli, \c{C}a\u{g}atay Y{\i}ld{\i}z
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/firatoncel/KernelRealityCheckNeurIPS2026](https://github.com/firatoncel/KernelRealityCheckNeurIPS2026)
- 阅读深度：metadata
