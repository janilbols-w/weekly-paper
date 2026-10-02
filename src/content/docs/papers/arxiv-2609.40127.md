---
title: "Learning Functional Subspaces for Neural Network Compression"
description: "Modern transformers pair impressive capabilities with substantial memory and compute demands."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.40127) · [PDF](https://arxiv.org/pdf/2609.40127)

## 一句话摘要

Modern transformers pair impressive capabilities with substantial memory and compute demands.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern transformers pair impressive capabilities with substantial memory and compute demands. Low-rank weight factorization reduces both while keeping the matrices dense, and thus efficient on standard hardware. Existing methods, however, choose the subspace to remove from each weight matrix with local closed-form criteria: activation energy, layer-wise reconstruction error, or a quadratic approximation of the loss. These criteria ignore how errors propagate through the network, so at high compression the errors compound with depth and performance collapses. We introduce Learnable Subspace Projections (LSP), which instead learns the subspaces to discard end-to-end. Each linear layer, or tied group of layers that read the same activations, is assigned an orthogonal projector. All projectors are optimized jointly against a global objective--the KL divergence to the dense model's output distribution or the model's original training loss--while the pretrained weights remain frozen. Projectors are initialized from a whitened SVD truncation, and ranks are allocated by the output KL each projector induces per parameter saved. After training, the projectors merge into standard low-rank factors, with each tied group sharing one factor. In attention, this also lets the model cache one narrow latent in place of full keys and values. Across LLMs (OPT-125M/1.3B, Qwen3-4B, Llama-2-7B) and ViT-B/16, LSP outperforms baselines, and its advantage widens as compression increases. At -70% compression, LSP brings Llama-2-7B to 10.9 WikiText-2 perplexity and 42.2% mean zero-shot accuracy, versus 13.3 and 36.0% for the strongest baseline. The factorized model decodes up to 1.6x faster than the dense model at small batch sizes, and aching the shared latent shrinks the combined memory of weights and KV cache by 13.5x at a 128k-token context, versus at most 6.5x for untied baseline factorizations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Massimo Bini, Anders Christensen, Stephan Alaniz, Judah Goldfeder, Ole Winther, Yann LeCun, Ravid Shwartz-Ziv, Zeynep Akata
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
