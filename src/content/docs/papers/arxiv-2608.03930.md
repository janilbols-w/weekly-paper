---
title: "Logic Before Language: Pre-pretraining on Formal Derivations Fosters Skill Acquisition and Compressibility"
description: "Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03930) · [PDF](https://arxiv.org/pdf/2608.03930)

## 一句话摘要

Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pre-pretraining language models (LMs) on symbolic data can accelerate and improve natural language acquisition. However, existing pre-pretraining tasks, such as Dyck and procedural algorithms, rely on narrow primitives that fail to capture the expressive capacity of natural language. Moreover, prior studies remain restricted to relatively small token budgets, offering limited insight into skill emergence and representational dynamics. To address these limitations, we propose logic pre-pretraining (Logic-PPT) as a principled initialization strategy, leveraging formal derivations to impart richer structural and linguistic biases. Formal derivations require abstract mechanisms that are central to natural language, simultaneously binding variables, connecting quantifiers and relational dependencies, and composing predicate-argument structures over long contexts. Scaling our evaluation to a 100B-token regime, logic pre-pretraining substantially accelerates skill acquisition in LMs, achieving 80\% accuracy on linguistic tasks with 36B fewer tokens than standard initialization, and outperforming alternative pre-pretraining baselines. Mechanistically, formal derivations induce persistent structural reorganization, distinctively characterized by a lower-rank, spectrally concentrated representation space. Crucially, we show that this internal geometry enables improved model compressibility via pruning, matching the dense baseline performance even at $\approx$33\% sparsity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jo-Ku Cheng, Nikolaos Aletras, Marco Valentino
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
