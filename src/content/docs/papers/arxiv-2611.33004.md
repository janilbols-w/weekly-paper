---
title: "LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training"
description: "Speculative decoding accelerates large language model (LLM) generation using a lightweight draft."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.33004) · [PDF](https://arxiv.org/pdf/2611.33004)

## 一句话摘要

Speculative decoding accelerates large language model (LLM) generation using a lightweight draft.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model (LLM) generation using a lightweight draft. Existing methods evaluate complete recipes under different training configurations, leaving component effects, interactions, and composition benefits unclear. Therefore, we present LEGOSpec, a composable framework for speculative draft design and training. LEGOSpec decomposes draft models into Context, Backbone, Proposal, and Objective components that share a unified training infrastructure. Using LEGOSpec, we systematically vary components and evaluate selected combinations under matched training conditions to isolate their effects and interactions. These experiments reveal three findings: (1) Different workloads favor different backbones, depending on context length and memory budget, with within-block dependency modeling particularly important for long contexts. (2) Proposal design must balance acceptance and latency. (3) The training objective should match token distributions locally and optimize acceptance length across the block. These findings guide workload-aware configurations and DFlux, a balanced general-purpose draft combining a convolution-equipped SWA--GQA hybrid backbone, Residual Corrector, and hierarchical supervision. Across Qwen and Gemma models, DFlux improves acceptance length over the strongest baseline by up to 13.7% on regular benchmarks and 34.7% on long-context workloads. To support efficient training, LEGOSpec integrates metadata-aware scheduling and asynchronous execution, increasing training throughput by up to 79% and accelerating offline supervision preparation by up to $3.11\times$ over SpecForge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hanzhen Wang, Jiaming Xu, Guohao Dai
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
