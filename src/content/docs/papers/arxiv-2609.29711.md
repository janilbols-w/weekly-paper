---
title: "Decoupling Knowledge and Privacy: Post-Task Self-Distillation Replay for LLM Continual Learning"
description: "Privacy-preserving continual learning (PPCL) must reduce the reproduction of sensitive content while retaining useful knowledge across sequential tasks."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.29711) · [PDF](https://arxiv.org/pdf/2609.29711)

## 一句话摘要

Privacy-preserving continual learning (PPCL) must reduce the reproduction of sensitive content while retaining useful knowledge across sequential tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Privacy-preserving continual learning (PPCL) must reduce the reproduction of sensitive content while retaining useful knowledge across sequential tasks. Formal privacy guarantees characterize randomized mechanisms, whereas operational output control concerns whether a trained model selectively reduces the likelihood of sensitive content in its outputs. In this work, we investigate the latter together with continual-learning utility under realistic task evolution. Retention and privacy correction operate at different granularities: task acquisition requires broad preservation of current- and old-task behavior, whereas privacy correction targets sparse annotated positions. Joint optimization leaves the current-task preservation target continually changing. We propose SPARK, a retention-correction decomposition that first freezes the learned post-task distribution and then applies selective correction around this stable reference. Self-Distillation Replay learns the current task while distilling behavior from previous tasks, and Post-Task Privacy Correction reduces annotated-PII likelihood while anchoring current- and old-task non-PII behavior to the resulting checkpoint. Extensive evaluations demonstrate that SPARK achieves effective selective PII suppression while preserving strong continual-learning utility and knowledge retention across diverse settings. Code and data will be released upon publication.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shengtao Wen, Yunying Yang, Xiang Chen, Lingbing Guo, Yu Tian, Sheng-Jun Huang
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
