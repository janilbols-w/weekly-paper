---
title: "Attention to Mamba: A Recipe for Cross-Architecture Distillation"
description: "State Space Models (SSMs) such as Mamba have become a popular alternative to Transformer models, due to their reduced memory consumption and higher throughput at generation compared to their Attention-based counterparts."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.14191) · [PDF](https://arxiv.org/pdf/2604.14191)

## 一句话摘要

State Space Models (SSMs) such as Mamba have become a popular alternative to Transformer models, due to their reduced memory consumption and higher throughput at generation compared to their Attention-based counterparts.

## 为什么值得关注

待编辑增强。

## 摘要原文

State Space Models (SSMs) such as Mamba have become a popular alternative to Transformer models, due to their reduced memory consumption and higher throughput at generation compared to their Attention-based counterparts. On the other hand, the community has built up a considerable body of knowledge on how to train Transformers, and many pretrained Transformer models are readily available. To facilitate the adoption of SSMs while leveraging existing pretrained Transformers, we aim to identify an effective recipe to distill an Attention-based model into a Mamba-like architecture. In prior work on cross-architecture distillation, however, it has been shown that a na\"ive distillation procedure from Transformers to Mamba fails to preserve the original teacher performance, a limitation often overcome with hybrid solutions combining Attention and SSM blocks. The key argument from our work is that, by equipping Mamba with a principled initialization, we can recover an overall better recipe for cross-architectural distillation. To this end, we propose a principled two-stage approach: first, we distill knowledge from a traditional Transformer into a linearized version of Attention, using an adaptation of the kernel trick. Then, we distill the linearized version into an adapted Mamba model that does not use any Attention block. Overall, the distilled Mamba model retains most of the original Pythia-1B Transformer performance, reaching a perplexity of 14.01 close to the teacher's 13.86. This largely carries over to downstream tasks, although some gaps appear on tasks relying more on in-context recall. To show the efficacy of our recipe, we conduct thorough ablations at 1B scale with 10B tokens varying sequence mixer architecture, scaling analysis on model sizes and total distillation tokens, and a sensitivity analysis on tokens allocation between stages.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Abhinav Moudgil, Ningyuan Huang, Eeshan Gunesh Dhekane, Pau Rodr\'iguez, Luca Zappella, Federico Danieli
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
