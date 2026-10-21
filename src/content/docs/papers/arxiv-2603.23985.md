---
title: "Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score"
description: "Large language models (LLMs) have demonstrated remarkable capabilities, but their massive scale poses significant challenges for practical deployment."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.23985) · [PDF](https://arxiv.org/pdf/2603.23985)

## 一句话摘要

Large language models (LLMs) have demonstrated remarkable capabilities, but their massive scale poses significant challenges for practical deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated remarkable capabilities, but their massive scale poses significant challenges for practical deployment. Structured pruning offers a promising solution by removing entire dimensions or layers, yet existing methods face critical trade-offs: task-agnostic approaches cannot adapt to task-specific requirements, while task-aware methods require costly training to learn task adaptability. We propose DIET (Dimension-wise global pruning of LLMs via merging Task-wise importance scores), a training-free structured pruning method that combines dimension-level granularity with task-aware selection. DIET profiles activation magnitudes across tasks using only 100 samples per task, then applies majority voting to construct a single global mask. Experiments on seven zero-shot benchmarks using Gemma-2 2B and 9B models demonstrate the effectiveness of DIET. At 20% sparsity on Gemma-2 2B, DIET improves average accuracy by 2.1 percentage points over SliceGPT and by 9.2 percentage points over PuDDing. On Gemma-2 9B, DIET remains competitive with SliceGPT while consistently outperforming PuDDing at 10% and 20% sparsity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jimyung Hong, Jaehyung Kim
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
