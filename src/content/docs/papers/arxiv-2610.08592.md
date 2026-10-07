---
title: "CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution"
description: "CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.08592) · [PDF](https://arxiv.org/pdf/2610.08592)

## 一句话摘要

CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives.

## 为什么值得关注

待编辑增强。

## 摘要原文

CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives. It takes a physics-native stance: a network is a cascade of complex -- and often unitary (the DFT) -- operations acting on an amplitude vector, and classification is a Born-rule measurement $p_k = |z_k|^2 / \|z\|^2$ rather than a softmax over real logits. Every layer ships a CPU reference and a CUDA kernel checked against finite differences, and the computation graph is cloned across the batch for GPU execution. On top of the base layers we add signal-processing primitives that turn the identity conv(x,k) = IFFT(FFT(x) . FFT(k)) into a learnable complex convolutional network, together with a true-Adam optimizer and a reduced-memory inference mode. We report three studies. First, a fully complex-valued, FNet-style causal sequence model built on a new $O(N \log N)$ causal Fourier mixer -- a triangular-masked DFT evaluated by a Bluestein / chirp-z factorization: once properly tuned it matches or exceeds a parameter-matched real-valued causal FNet on character-level language modeling, reaching the real model's converged quality in under half the training steps. Second and third, bottleneck analyses on radio-modulation classification (RML2016.10a) and the Fourier phase problem of coherent-diffraction imaging, which isolate exactly where complex-valued networks still need new operators. Across all three the complex formulation provably learns the physically correct structure. Code: https://github.com/crasmarum/CNet

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cuda kernel
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Marcel Crasmaru
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/crasmarum/CNet](https://github.com/crasmarum/CNet)
- 阅读深度：metadata
