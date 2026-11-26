---
title: "REAL: Reading Out Transformer Activations for Precise Localization in Language Model Steering"
description: "Inference-time steering aims to alter an LLM's responses without changing its parameters."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2506.08359) · [PDF](https://arxiv.org/pdf/2506.08359)

## 一句话摘要

Inference-time steering aims to alter an LLM's responses without changing its parameters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference-time steering aims to alter an LLM's responses without changing its parameters. A key challenge lies in selecting internal modules that most strongly govern the target behavior; existing approaches often rely on simplistic cues or ad hoc heuristics, leading to suboptimal or unintended effects. In this work, we introduce REAL, a novel framework for identifying behavior-relevant modules (heads or layers) in Transformers. For each module, we train a vector-quantized autoencoder (VQ-AE) on its hidden activations, partitioning the latent space into behavior-relevant and behavior-irrelevant subspaces via a shared, learnable codebook. We quantify each module's behavioral relevance by evaluating how effectively the VQ-AE encodings distinguish between behavior-aligned and behavior-violating responses using a binary classification metric. This relevance score informs both module selection and steering strength. We evaluate REAL across eight LLMs from two model families (Llama and Qwen) and nine datasets spanning truthfulness enhancement, open-domain question answering under knowledge conflicts, and general alignment tasks. REAL enables more effective inference-time interventions, yielding significant improvements on these steering tasks. Notably, it achieves an average relative improvement of 20% (up to 81.5%) over the seminal ITI method on truthfulness steering. Moreover, the modules selected by our method exhibit strong zero-shot generalization in cross-domain truthfulness-steering scenarios. We provide the source code to reproduce all experimental results at https://github.com/liam0949/REAL_ICLR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Li-Ming Zhan, Bo Liu, Yujie Feng, Chengqiang Xie, Jiannong Cao, Xiao-Ming Wu
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/liam0949/REAL_ICLR](https://github.com/liam0949/REAL_ICLR)
- 阅读深度：metadata
