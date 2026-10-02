---
title: "Self-conditioned Flow Map Language Models via Fixed-point Flows"
description: "Self-conditioning is a core technique that enhances continuous flow-based language models, where the model learns to denoise generated text by conditioning on its own denoising estimate."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.00714) · [PDF](https://arxiv.org/pdf/2607.00714)

## 一句话摘要

Self-conditioning is a core technique that enhances continuous flow-based language models, where the model learns to denoise generated text by conditioning on its own denoising estimate.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-conditioning is a core technique that enhances continuous flow-based language models, where the model learns to denoise generated text by conditioning on its own denoising estimate. While empirically successful, its performance improvements are poorly understood. Moreover, there is growing interest in the use of few-step generators based on flow maps, for which how to leverage self-conditioning is unclear. Here, we show that flow language models with self-conditioning perform a fixed-point iteration that improves generation through iterative refinement. We use this viewpoint to formulate fixed-point flows, a two-dimensional class of self-conditioned flows, where the first dimension represents the flow process and the second represents the fixed-point iteration. We show that fixed-point flows define valid flow maps, and show that they can be distilled from self-conditioned flow models by compressing both fixed-point iterations and the flow process, the former with fixed-point distillation and the latter with flow map distillation. Our resulting flow map language model, FMLM$^\star$, outperforms state-of-the-art self-conditioned models and few-step models in one- and few-step generation on OpenWebText. Code is available at https://github.com/Ugness/self-conditioned-fmlm.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jaehoon Yoo, Wonjung Kim, Floor Eijkelboom, Chanhyuk Lee, Nicholas M. Boffi, Seunghoon Hong, Jinwoo Kim
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Ugness/self-conditioned-fmlm](https://github.com/Ugness/self-conditioned-fmlm)
- 阅读深度：metadata
