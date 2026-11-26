---
title: "scOPD: Routed On-Policy Self-Distillation for LLM-Based Single-Cell Annotation"
description: "Motivation: Large language models (LLMs) have shown promise for single-cell annotation, but existing training methods mainly rely on scalar outcome rewards that provide limited supervision for intermediate biological reasoning."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.31257) · [PDF](https://arxiv.org/pdf/2611.31257)

## 一句话摘要

Motivation: Large language models (LLMs) have shown promise for single-cell annotation, but existing training methods mainly rely on scalar outcome rewards that provide limited supervision for intermediate biological reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Motivation: Large language models (LLMs) have shown promise for single-cell annotation, but existing training methods mainly rely on scalar outcome rewards that provide limited supervision for intermediate biological reasoning. Batch-level annotation is particularly challenging because it requires jointly resolving local cell identities and a global one-to-one matching constraint, such that one local error can affect the entire assignment. Moreover, a single inference pass provides insufficient evidence for locating uncertain predictions. These limitations call for fine-grained reasoning supervision during training and uncertainty-aware refinement during inference. Results: To address these challenges, we propose scOPD, an on-policy self-distillation framework for LLM-based single-cell annotation. After reasoning fine-tuning, scOPD adaptively routes qualified rollouts to reward-based optimization, while erroneous rollouts receive privileged token-level supervision from successful sibling trajectories. During inference, rollout disagreement triggers constraint-aware pairwise refinement of uncertain assignments. Across CellPuzzles and four out-of-domain disease datasets, scOPD consistently improves the performance of diverse LLM backbones, achieving average cell-level and batch-level accuracies of 81.71% and 44.49% with Qwen3-8B. Availability and Implementation: Code and data are available at https://github.com/YuZhiyin/scOPD.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhiyin Yu, Yuchen Mou, Songtao Huang, Shuaiyu Zhang, Xing Wei, Chunchun Chen, Wei Ye, Xiao Luo, Zhonghai Wu, Xiangchao Yan, Lei Bai, Shiyang Feng, Bo Zhang
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/YuZhiyin/scOPD](https://github.com/YuZhiyin/scOPD)
- 阅读深度：metadata
