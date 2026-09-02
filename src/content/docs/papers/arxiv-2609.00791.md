---
title: "Instella-MoE Technical Report"
description: "In this work, we introduce Instella-MoE, a fully open Mixture-of-Experts (MoE) language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely from scratch on AMD Instinct MI300X and MI325X GPUs."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.00791) · [PDF](https://arxiv.org/pdf/2609.00791)

## 一句话摘要

In this work, we introduce Instella-MoE, a fully open Mixture-of-Experts (MoE) language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely from scratch on AMD Instinct MI300X and MI325X GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this work, we introduce Instella-MoE, a fully open Mixture-of-Experts (MoE) language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely from scratch on AMD Instinct MI300X and MI325X GPUs. Instella-MoE combines a sparsely activated MoE design with architectural and system-level innovations, including Gated Multi-head Latent Attention (Gated MLA) and FarSkip-Collective connectivity, enabling efficient large-scale training and inference. The model is developed through a multi-stage pipeline comprising pre-training, mid-training, long-context extension, supervised fine-tuning with feedback-driven data curation, direct preference optimization, and reinforcement learning with Multi-Teacher On-Policy Distillation. Instella-MoE achieves an average score of 76.7 across standard pre-training benchmarks, outperforming prior fully open models including OLMo-3-7B, SmolLM3-3B, and OLMoE-1B-7B, while remaining competitive with open-weight MoE and dense baselines at comparable active-parameter scales, including Moonlight-16B-A3B and Qwen3.5-4B. After post-training, our final Think checkpoint achieves an average score of 73.2 across instruction-following, reasoning, math, coding, and chat benchmarks, outperforming both fully open and open-weight models with comparable or larger active parameter counts in our evaluation. To support transparent and reproducible research, we release the complete Instella-MoE model flow, including model weights, training configurations, data mixtures, and training code. Together, these contributions establish Instella-MoE a strong, fully open foundation for efficient, high-performing MoE models and reproducible research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra, Yonatan Dukler, Gowtham Ramesh, Jialian Wu, Ximeng Sun, Wen Xie, Chaojun Hou, Vikram Appia, Zhenyu Gu, Zicheng Liu, Emad Barsoum
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
