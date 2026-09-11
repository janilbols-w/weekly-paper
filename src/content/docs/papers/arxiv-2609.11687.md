---
title: "Structured Transforms for Low-Overhead Quantization of Language Models"
description: "We revisit Kashin-decomposition-based weight quantization for large language models and propose an improved algorithm with stronger convergence properties and structured, efficient orthogonal transforms."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.11687) · [PDF](https://arxiv.org/pdf/2609.11687)

## 一句话摘要

We revisit Kashin-decomposition-based weight quantization for large language models and propose an improved algorithm with stronger convergence properties and structured, efficient orthogonal transforms.

## 为什么值得关注

待编辑增强。

## 摘要原文

We revisit Kashin-decomposition-based weight quantization for large language models and propose an improved algorithm with stronger convergence properties and structured, efficient orthogonal transforms. The method retains the core factorization of each weight into two components -- one with bounded infinity norm and the other with bounded infinity norm after an orthogonal transformation -- but replaces the dense random orthogonal matrix with a sign-randomized Discrete Cosine Transform (DCT), reducing the per-iteration cost from $\mathcal{O}(N^2)$ to $\mathcal{O}(N \log N)$. The proposed greedy algorithm with alternating updates guarantees the four-peak distribution required for stable 2-bit clustering of each factor and admits closed-form initialization of cluster centers, removing the multi-restart k-means bottleneck of prior work. Composed with OPTQ-style sequential error compensation and QuIP-style incoherence preprocessing, the resulting JAX pipeline is competitive with OPTQ, QuIP, QuIP-RG and a fine-tuning- and vector-quantization-free variant of QuIP# at 4-bit per channel on OPT, Llama-2 and Pythia, with favorable wall-clock scaling. The bounded-$\ell_\infty$ factorization is also notably robust: on stress configurations where QuIP variants diverge to four-digit perplexity (Pythia-6.9B) or abort with NaNs in LDL back-substitution (Mistral-7B), Kashin-DCT remains numerically stable and stays close to FP16 baseline. At inference time, each weight decomposes into two 2-bit factor codes per channel that are structurally suited to native-2-bit hardware.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Daria Cherniuk, Alexander Rudikov, Boris Kashin, Ivan Oseledets
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
