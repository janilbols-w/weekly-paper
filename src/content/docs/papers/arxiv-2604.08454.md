---
title: "Less Data Approximates More: Earning Faithful Confidence in High-Stakes Domains"
description: "Large language models are increasingly deployed in high-stakes domains, where confident yet incorrect inferences may cause severe real-world harm, bringing the long-overlooked issue of confidence faithfulness to the forefront."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.08454) · [PDF](https://arxiv.org/pdf/2604.08454)

## 一句话摘要

Large language models are increasingly deployed in high-stakes domains, where confident yet incorrect inferences may cause severe real-world harm, bringing the long-overlooked issue of confidence faithfulness to the forefront.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly deployed in high-stakes domains, where confident yet incorrect inferences may cause severe real-world harm, bringing the long-overlooked issue of confidence faithfulness to the forefront. A promising solution jointly optimizes unsupervised Reinforcement Learning from Internal Feedback (RLIF) with reasoning-trace-guided Reasoning Distillation (RD), yet it faces three persistent challenges, namely the scarcity of high-quality training corpora, factually unwarranted overconfidence, and erroneous updates amplified by indiscriminate fusion. Inspired by how human confidence accumulates from uncertainty to certainty, we propose Progressive Reasoning Gain (PRG) to measure whether reasoning steps progressively strengthen confidence in the final answer. Building on PRG, we introduce HyTuning, a hybrid post-training framework that adaptively reweights RD and RLIF, using scarce supervised reasoning traces as a stable anchor while exploiting abundant unlabeled queries for scalability. Experiments on several domain-specific and general benchmarks demonstrate that HyTuning improves accuracy while achieving confidence faithfulness under limited supervision, supporting a practical ``Less Data Approximates More'' effect. Our code will be released upon acceptance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haokai Ma, Lee Yan Zhen, Gang Yang, Yunxiang Chen, Yunshan Ma, Tat-Seng Chua, Ee-Chien Chang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
