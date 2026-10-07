---
title: "Component and Dimension Sparsity in Transformer Refusal Mechanisms"
description: "Activation steering manipulates large language model behavior by intervening on internal activations, but the mechanistic basis of these interventions remains poorly understood."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.06903) · [PDF](https://arxiv.org/pdf/2610.06903)

## 一句话摘要

Activation steering manipulates large language model behavior by intervening on internal activations, but the mechanistic basis of these interventions remains poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Activation steering manipulates large language model behavior by intervening on internal activations, but the mechanistic basis of these interventions remains poorly understood. We decompose refusal steering into component-level interventions across four open-weight models, identifying the sparse subsets of attention and MLP components whose steering suffices to reproduce the full behavioral effect. We find that refusal directions concentrate in sparse component mechanisms comprising 28--48\% of upstream components, retaining 88--101\% of steering effectiveness. Within these mechanisms, effective steering further concentrates in approximately 50\% of residual stream dimensions, retaining 85--98\% of the component-mechanism baseline, consistent with a privileged basis structure. Sparsity thus operates at two levels: which components are steered, and which dimensions within those components carry the signal. Together these findings show that refusal is not diffusely encoded across a transformer but assembled by a structured, identifiable mechanism, providing a foundation for mechanistic understanding of how refusal behaviors are represented and steered. To facilitate reproducibility, we release all code and raw experimental results in https://github.com/wang-research-lab/Refusal_Mechanisms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Vincent Siu, Glenn Grant-Richards, Vlad Pavlovich, Yizhou Sun, Dawn Song, Chenguang Wang
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/wang-research-lab/Refusal_Mechanisms](https://github.com/wang-research-lab/Refusal_Mechanisms)
- 阅读深度：metadata
