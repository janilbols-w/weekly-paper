---
title: "Reasoning Beyond Imitation: Observation Conditioned Distillation for Video LLMs"
description: "Reasoning distillation offers a promising approach to transfer temporal reasoning capabilities of powerful Video-LLMs to open-source student models."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.29728) · [PDF](https://arxiv.org/pdf/2611.29728)

## 一句话摘要

Reasoning distillation offers a promising approach to transfer temporal reasoning capabilities of powerful Video-LLMs to open-source student models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reasoning distillation offers a promising approach to transfer temporal reasoning capabilities of powerful Video-LLMs to open-source student models. However, teacher and student Video-LLMs may construct different temporal observations from the same video due to the adoption of distinct video sampling pipelines. A reasoning trajectory valid under the teacher's observations may rely on evidence inaccessible to the student and thus cannot be directly executed based on the student's observations. We formalize this as a conditional target mismatch, thereby revealing the Reasoning Acquisition-Execution Gap. To bridge this gap, we propose an acquisition-to-execution framework that first distills teacher trajectories into a student reasoning prior and then further optimizes the execution capability of this prior across multiple observations. We further introduce Execution-Aware Reference Regularization, which retains the existing prior when it is executable under current observations, while allowing a greater degree of adaptive adjustment when it is not. Experiments across multiple Video-LLM backbones and six video reasoning benchmarks show that explicitly optimizing observation-conditioned execution consistently outperforms supervised distillation and standard RL-based optimization, with gains extending to held-out out-of-domain benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junzhou Chen, Jindong Wang, Gang Zhou
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
