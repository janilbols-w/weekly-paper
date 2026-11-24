---
title: "Turnout: Adaptive Attention Switching for Efficient Reasoning"
description: "Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.27500) · [PDF](https://arxiv.org/pdf/2611.27500)

## 一句话摘要

Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state. This change reduces memory consumption but often hurts accuracy. In reasoning tasks, which require long generations, this effect is especially pronounced. In this work we introduce Turnout, a method that mitigates accuracy loss as a result of linearization, while maintaining its memory-reduction benefits. We apply post-hoc linearization to a pretrained full-attention model, training a linear path through distillation while leaving the original full-attention path unchanged. During response generation, the resulting hybrid model retains both paths and uses a learned policy to control when each layer switches from full to linear attention. We train the policy with reinforcement learning using a reward that balances answer correctness and memory use. Empirical evaluation of our method shows that the learned adaptive policy achieves a better accuracy-efficiency Pareto frontier on reasoning tasks compared to fixed switching and static hybrid baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anna Kuzina, Mart van Baalen, Paul N. Whatmough, Babak Ehteshami Bejnordi
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
