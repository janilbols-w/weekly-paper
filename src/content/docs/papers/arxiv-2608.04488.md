---
title: "Energy- and Memory-Efficient PEFT Methods for Personalized On-Device SLMs on Consumer GPUs"
description: "Despite rapid advances in large language models (LLMs), deploying and personalizing them on resource-constrained devices remains impractical due to high VRAM, time, and energy costs."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2608.04488v1) · [PDF](https://arxiv.org/pdf/2608.04488v1)

## 一句话摘要

Despite rapid advances in large language models (LLMs), deploying and personalizing them on resource-constrained devices remains impractical due to high VRAM, time, and energy costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite rapid advances in large language models (LLMs), deploying and personalizing them on resource-constrained devices remains impractical due to high VRAM, time, and energy costs. Parameter-Efficient Fine-Tuning (PEFT) of Small Language Models (SLMs) offers a promising alternative, yet few studies compare PEFT methods across architectures using both general and personalization benchmarks while accounting for energy consumption. We compare five fine-tuning approaches (Full Fine-Tuning, LoRA, LoRA+, QLoRA, and BitFit) on four SLMs from two families (Transformer-based: TinyLlama-1.1B, Qwen3-1.7B; SSM-based: Mamba-1.4B, Mamba-2-1.3B) across three GLUE tasks (SST-2, QNLI, STS-B) and three LaMP personalization tasks (LaMP-1, LaMP-2, LaMP-3). Each configuration is evaluated with the energy-focused NetScore-E and the memory-focused NetScore-M, the two variants that reflect the constraints binding on-device deployment. Methods are selected with a strict energy-first rule (highest NetScore-E, ties broken by NetScore#). LoRA+ achieves the highest NetScore-E in 19 of 24 configurations and the highest NetScore-M in 13 of 24, and is the selected method in 18 of 24. QLoRA, available only for the Transformer models, cuts peak finetuning VRAM by up to 3.9x relative to LoRA and therefore takes the best NetScore-M in 5 of the 12 Transformer configurations, although its de-quantization overhead leaves it selected in only one of them once energy decides. BitFit and full fine-tuning are almost never competitive on either variant, and TinyLlama-1.1B leads the energy-focused NetScore-E on five of the six benchmarks and the memory-focused NetScore-M on four. These results show that compact SLMs paired with PEFT provide a practical, energy-aware path to personalized on-device deployment, with the optimal method set by the dominant constraint: LoRA+ for energy and QLoRA for memory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kuanysh Akhmetzhanov, Jurn-Gyu Park
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
