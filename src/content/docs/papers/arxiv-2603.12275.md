---
title: "GONE: Structural Knowledge Unlearning via Neighborhood-Expanded Distribution Shaping"
description: "Unlearning knowledge is a pressing and challenging task in Large Language Models (LLMs) because of their unprecedented capability to memorize and digest training data at scale, raising more significant issues regarding safety, privacy, and intellectual property."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.12275) · [PDF](https://arxiv.org/pdf/2603.12275)

## 一句话摘要

Unlearning knowledge is a pressing and challenging task in Large Language Models (LLMs) because of their unprecedented capability to memorize and digest training data at scale, raising more significant issues regarding safety, privacy, and intellectual property.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unlearning knowledge is a pressing and challenging task in Large Language Models (LLMs) because of their unprecedented capability to memorize and digest training data at scale, raising more significant issues regarding safety, privacy, and intellectual property. However, existing works, including parameter editing, fine-tuning, and distillation-based methods, are all focused on flat sentence-level data but overlook the relational, multi-hop, and reasoned knowledge in naturally structured data. In response to this gap, this paper introduces Graph Oblivion and Node Erasure (GONE), a benchmark for evaluating knowledge unlearning over structured knowledge graph (KG) facts in LLMs.This KG-based benchmark enables the disentanglement of three effects of unlearning: direct fact removal, reasoning-based leakage, and catastrophic forgetting. In addition, Neighborhood-Expanded Distribution Shaping (NEDS), a novel unlearning framework, is designed to leverage graph connectivity and identify anchor-correlated neighbors, thereby enforcing a precise semantic separation between the forgotten fact and its semantic neighborhood. Evaluations on LLaMA-3-8B and Mistral-7B across multiple knowledge editing and unlearning methods showcase NEDS's superior performance (1.000 on unlearning efficacy and 0.839 on locality) on GONE and other benchmarks. The dataset is available at https://huggingface.co/datasets/GONE-Anonymous/GONE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chahana Dahal, Ashutosh Balasubramaniam, Zuobin Xiong
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
