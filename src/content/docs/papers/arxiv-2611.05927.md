---
title: "Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models"
description: "Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B)."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.05927) · [PDF](https://arxiv.org/pdf/2611.05927)

## 一句话摘要

Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B).

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B). Expert pruning has emerged as an effective compression strategy, but existing methods aggregate importance uniformly across tokens, ignoring that the same expert may serve different roles for vision versus language processing. To address this, we propose MAEP (Modality-Aware Expert Pruning), a training-free framework that decomposes expert importance by modality in a single forward pass. MAEP introduces (1) Delta-H Output ($\Delta H$), a redistribution-aware metric measuring the MoE output change when an expert is removed, and (2) low-attention vision tokens as a vision-side pruning signal that is dataset-stable: its expert-importance ranking remains stable across different datasets. Text-side importance serves as a preservation signal while vision-side importance serves as a pruning signal, and experts are ranked globally across layers. Experiments on three MoE-based MLLMs across multimodal and text benchmarks show that MAEP outperforms modality-agnostic baselines on the majority of multimodal benchmarks while remaining competitive on text-only tasks, reducing the BF16 expert weight footprint by about 27 GB (about 47% of total memory) so that the full weight footprint of an approximately 58 GB model fits within a single 40 GB GPU. Code is available at https://github.com/nota-github/MAEP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Donggeun Kim
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/nota-github/MAEP](https://github.com/nota-github/MAEP)
- 阅读深度：metadata
