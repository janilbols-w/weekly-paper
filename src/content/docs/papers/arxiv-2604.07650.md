---
title: "A Statistical Framework for Auditing Behavioral Dependence and Induced Bias in LLM Judges"
description: "The rapid growth of the large language model (LLM) ecosystem raises a critical question: are seemingly diverse models truly independent?"
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.07650) · [PDF](https://arxiv.org/pdf/2604.07650)

## 一句话摘要

The rapid growth of the large language model (LLM) ecosystem raises a critical question: are seemingly diverse models truly independent?

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid growth of the large language model (LLM) ecosystem raises a critical question: are seemingly diverse models truly independent? Shared pretraining data, distillation, and alignment pipelines can induce hidden behavioral dependencies, or latent entanglement, that undermine multi-model systems such as LLM-as-a-judge pipelines and ensemble verification, which implicitly assume independent signals. In practice, this manifests as correlated reasoning patterns and synchronized failures, where apparent agreement reflects shared error modes rather than independent validation. To address this, we develop a statistical framework for auditing behavioral entanglement among black-box LLMs. Our approach introduces a multi-resolution hierarchy that characterizes the joint failure manifold through two information-theoretic metrics: (i) a Difficulty-Weighted Behavioral Entanglement Index (BEI), which amplifies synchronized failures on easy tasks, and (ii) a Cumulative Information Gain (CIG) metric, which captures directional alignment in erroneous responses. Through experiments on 18 LLMs from six model families, we identify statistically significant behavioral entanglement. Such behavioral dependence is associated with judge over-endorsement bias on a disjoint MMLU-Pro evaluation set (rho = 0.508 for BEI and rho = 0.520 for CIG; p < 0.01). The association further transfers to the MATH-500 benchmark (rho = 0.441 for BEI and rho = 0.457 for CIG; p < 0.05), providing cross-benchmark evidence that the identified dependency structure generalizes beyond the data and response format used for its estimation. Finally, we demonstrate a practical use case of entanglement through de-entangled verifier ensemble reweighting, achieving 3.5 and 2.6 percentage-point gains in accuracy and precision, respectively, over majority voting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chenchen Kuai, Jiwan Jiang, Zihao Zhu, Hao Wang, Keshu Wu, Zihao Li, Yunlong Zhang, Chenxi Liu, Zhengzhong Tu, Zhiwen Fan, Yang Zhou
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
