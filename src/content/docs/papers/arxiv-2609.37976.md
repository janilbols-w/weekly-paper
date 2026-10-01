---
title: "$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient"
description: "LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.37976) · [PDF](https://arxiv.org/pdf/2609.37976)

## 一句话摘要

LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singular directions, and removing the subspace component can largely improve reasoning efficiency without hurting the accuracy gained during thinking-mode post-training. Unlike existing efforts that mostly operate within the dominant subspace, we are the first to unveil the critical role of the null space and harness it for model optimization. Motivated by this finding, we propose Spectral Null-Space Swap ($S^3$), a training-free composition of paired Non-thinking and Thinking checkpoints. Our method keeps the Non-thinking model inside its own dominant subspace and takes the Thinking checkpoint outside it, improving reasoning efficiency while maintaining accuracy. We extensively evaluate $S^3$ on 2B-30B dense and mixture-of-experts (MoE) architectures spanning 28 evaluation environments across mathematical, multimodal, and audio reasoning domains. $S^3$ establishes new empirical Pareto Frontiers among training-free model composition strategies: across all settings, it reduces inference token overhead by an average of 27.4% compared to full Thinking models while simultaneously improving overall task accuracy by 1.0 percentage point (e.g., yielding +8.3% accuracy on HMMT25 alongside a 33.0% token speedup). We further use attention entropy for explanation and find that the retained component produces more concentrated attention, and we use a simplified analytical model about optimization to demonstrate why null-space can effectively reduce attention entropy, thereby improving the efficiency of reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongbo Ma, Sansheng Cao, Jiajun Fan, Bangji Yang, Ge Liu
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
