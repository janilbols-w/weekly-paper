---
title: "Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"
description: "Large Language Models (LLMs) now exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), with impressive performance across math and coding benchmarks."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.25098) · [PDF](https://arxiv.org/pdf/2604.25098)

## 一句话摘要

Large Language Models (LLMs) now exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), with impressive performance across math and coding benchmarks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) now exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), with impressive performance across math and coding benchmarks. In parallel, research in model compression has developed pruning methods that seek to remove redundant/detrimental parameters without sacrificing task performance. The intersection of these two research advancements lays the foundation for our work. Specific to reasoning LLMs, prior work has shown that structured pruning (methods which remove entire set of layer blocks), significantly degrades TTS reasoning performance. However, in this work, we revisit this assumption and investigate whether unstructured pruning (methods that carefully remove only certain redundant/detrimental weights) exhibits similar limitations. Surprisingly, our extensive experiments across four reasoning benchmarks on two reasoning LLMs: s1.1-7B and Qwen3-8B, consistently show that unstructured pruning augments TTS performance compared to structured pruning, and at times can even outperform the unpruned full-weight LLMs. Furthermore, we also empirically study the impact of different layer-wise sparsity allocation strategies, which are an important parametric choice for instantiating these unstructured methods. These findings challenge the conventional notion that pruning always reduces TTS performance and in fact, suggest that carefully undertaken pruning can retain TTS effectiveness.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
