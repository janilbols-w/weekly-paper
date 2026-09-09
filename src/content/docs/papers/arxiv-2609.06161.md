---
title: "All for 1-Bit: Towards Genuine 1-Bit Post-Training Quantization for LLMs"
description: "Large language models (LLMs) have achieved remarkable progress, yet their massive storage and memory-bandwidth demands still hinder efficient deployment."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.06161) · [PDF](https://arxiv.org/pdf/2609.06161)

## 一句话摘要

Large language models (LLMs) have achieved remarkable progress, yet their massive storage and memory-bandwidth demands still hinder efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have achieved remarkable progress, yet their massive storage and memory-bandwidth demands still hinder efficient deployment. Weight binarization is a promising solution, but existing binarization-based post-training quantization (PTQ) methods usually far exceed the nominal 1-bit storage target due to hidden overhead. To address this gap, we propose All for 1-Bit (AF1), a genuine 1-bit PTQ framework for LLMs. AF1 comprises two complementary components: (1) Null-space-Aware Binary Factorization (NABF) for improving binary reconstruction through Hessian-aware surrogate reparameterization, null-space-aware binary factorization, and scale-only global reconstruction; and (2) Hierarchical Shapley Allocation (HiSA) for assigning structural capacity using hierarchical Shapley sensitivity. Together, they preserve model accuracy under a strict 1.0-BPW budget in the PTQ setting. Experiments on LLaMA, Qwen, and Gemma families show that AF1 consistently outperforms existing binarization-based PTQ methods in perplexity and zero-shot accuracy. Compared with BF16, AF1 achieves an average 2.5 times inference speedup and over 90% memory reduction across evaluated models, providing a practical path toward deployable genuine 1-bit compression for LLMs. The code for reproducibility is available at https://github.com/Kishon-zzx/AF1.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zhixiong Zhao, Zukang Xu, Guangyu Sun, Lifeng Liu, Dawei Yang
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Kishon-zzx/AF1](https://github.com/Kishon-zzx/AF1)
- 阅读深度：metadata
