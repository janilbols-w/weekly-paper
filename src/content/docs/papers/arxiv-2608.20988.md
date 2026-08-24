---
title: "Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models"
description: "Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.20988) · [PDF](https://arxiv.org/pdf/2608.20988)

## 一句话摘要

Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors. We identify the softmax operator as a bottleneck for quantization stability due to its sensitivity to outliers and state-dependent Jacobian. We theoretically establish that suppressing the norm of this Jacobian helps in bounding quantization-induced performance degradation. Based on this, we propose Jacobian-Guided Noise Injection, a training strategy that injects zero-mean Gaussian noise into pre-attention logits, with variance derived directly from the Jacobian Frobenius norm. Unlike prior approaches that rely on heuristic or penalise jacobian directly, our method provides a way to identify the optimal noise variance based on the local attention sensitivity. We evaluate the method on SOTA LLM architectures, where it demonstrates improved robustness over popular PTQ methods. Empirical analysis reveals that the proposed method gives up to +37% relative gains on Top-1 accuracy on ImageNet-1K for SigLIP and improves relative perplexity by upto 40% on WikiText for language models in low bit quantisation settings, proving the efficacy of the approach.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Deepanshu Pandey, Arnav Chavan, Nahush Lele, Sankalp Dayal, Deepak Gupta
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
