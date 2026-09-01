---
title: "Bergson: An Open Source Library for Data Attribution"
description: "Data attribution is a promising field in interpretability that aims to explain model behavior through the influence of its training data, with applications including debugging undesirable model behavior and training dataset curation."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2606.11660) · [PDF](https://arxiv.org/pdf/2606.11660)

## 一句话摘要

Data attribution is a promising field in interpretability that aims to explain model behavior through the influence of its training data, with applications including debugging undesirable model behavior and training dataset curation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Data attribution is a promising field in interpretability that aims to explain model behavior through the influence of its training data, with applications including debugging undesirable model behavior and training dataset curation. However, significant engineering effort is required to perform it at scale, and many cutting edge techniques lack open-source tooling and support. Bergson is an open source library that aims to enable faster progress in the field by providing a host of techniques that scale to very large language models and pre-training datasets. The library natively supports on-disk gradient stores and multi-node distributed training, and provides quality of life tools for researchers. Finally, we introduce the first open-source implementations of three leading data attribution methods: MAGIC, SOURCE, and TrackStar. The library is available at https://github.com/EleutherAI/bergson .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Lucia Quirke, Louis Jaburi, David Johnston, William Z. Li, Gon\c{c}alo Paulo, Guillaume Martres, Girish Gupta, Stella Biderman, Nora Belrose
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EleutherAI/bergson](https://github.com/EleutherAI/bergson)
- 阅读深度：metadata
