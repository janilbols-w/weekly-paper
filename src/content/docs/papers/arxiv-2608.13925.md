---
title: "CForce: Boosting Parallel Decoding for dLLMs via Consistency Forcing"
description: "Diffusion large language models (dLLMs) accelerate language generation by predicting multiple masks in a single forward pass."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.13925) · [PDF](https://arxiv.org/pdf/2608.13925)

## 一句话摘要

Diffusion large language models (dLLMs) accelerate language generation by predicting multiple masks in a single forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) accelerate language generation by predicting multiple masks in a single forward pass. However, existing dLLMs can suffer from unreliable predictions in early denoising stages under aggressive parallelism strategies, leading to errors that can propagate to later stages. To tackle this issue, we present Consistency Forcing (CForce) for dLLMs, a distillation method to force the mask predictions of early stages to align with those of later stages. CForce trains the model on pre-collected self-rollout trajectories, thereby improving training-inference alignment. We introduce Confidence Adaptive KL Divergence as a distillation objective to conjoin the merits of forward and reverse KL. We further provide a theoretical analysis for the consistency objective to explain why CForce can approximately minimize the prediction error of early stages. Critically, the same formulation applies to both mask-to-token decoding and edit-capable decoding; in the edit-capable case, later token-to-token refinements provide additional supervision for earlier masked-state predictions. Experiments on non-edit and edit-capable LLaDA models show improved speed-quality trade-offs, especially under high-parallelism decoding budgets. Code is available at: https://github.com/inclusionAI/dFactory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuji Ren, Chenkai Xu, Zhuocheng Gong, Jianguo Li, Zhijie Deng
- 发布：2026-08-17；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/inclusionAI/dFactory](https://github.com/inclusionAI/dFactory)
- 阅读深度：metadata
