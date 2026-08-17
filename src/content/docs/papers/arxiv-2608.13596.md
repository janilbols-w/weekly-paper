---
title: "Training-Free Knowledge Transfer Across Model Scales through Activation-Guided Pruning"
description: "Heterogeneous model fusion seeks to combine models that differ in tasks, initializations, architectures, or scales."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.13596) · [PDF](https://arxiv.org/pdf/2608.13596)

## 一句话摘要

Heterogeneous model fusion seeks to combine models that differ in tasks, initializations, architectures, or scales.

## 为什么值得关注

待编辑增强。

## 摘要原文

Heterogeneous model fusion seeks to combine models that differ in tasks, initializations, architectures, or scales. We study an underexplored cross-scale setting: improving a small recipient language model with a stronger donor despite substantial architectural mismatch. We ask whether useful capabilities can be transferred without explicit neuron-wise semantic alignment. Building on the observation that truncating a large model to a smaller architecture and injecting it with a tiny mixing weight can already improve the recipient, we propose Activation-Prune-Merge (APM), an activation-guided framework for cross-scale fusion. APM constructs task-conditioned activation maps on the donor, selects salient layers, hidden dimensions, attention heads, and MLP neurons to prune it to the recipient architecture, and injects the resulting donor slice into the original recipient using a micro interpolation coefficient. This formulation treats the donor as a source of concentrated functional components rather than requiring precise structural transplantation. Across 16 benchmarks spanning reasoning, mathematics, code generation, instruction following, and classification, APM improves the overall average accuracy from 55.5% to 60.6% over the original 3B recipient. RTE accuracy increases from 64.3% to 82.3%, QNLI from 52.3% to 65.7%, and BoolQ from 70.8% to 79.2%. Analyses of injection ratios and sequential multi-stage fusion further suggest that activation-guided extraction improves the quality of the transferable donor slice while preserving the small-ratio fusion regime. These results provide evidence that cross-scale heterogeneous fusion can succeed without explicit semantic alignment when the donor contribution is sufficiently concentrated and carefully selected.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiahe Fan, Si Chen, Yinghao Hou, Aiyuan Zhang, Hong Xie
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
