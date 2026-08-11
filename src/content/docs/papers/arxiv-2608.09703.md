---
title: "Matryoshka Language Model Suites"
description: "Training a language model suite classically requires training each model separately and serving them independently."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.09703) · [PDF](https://arxiv.org/pdf/2608.09703)

## 一句话摘要

Training a language model suite classically requires training each model separately and serving them independently.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training a language model suite classically requires training each model separately and serving them independently. We improve both training and inference efficiency by stacking sub-models of increasing size into a single nested architecture trained end-to-end. This Matryoshka training framework reduces the total parameter count of the suite, enables low-cost distillation from the largest to all smaller sub-models at every training step, and is well-suited for speculative decoding as the draft model is contained within the verifier. We validate our approach by training a Matryoshka suite comprising 500M, 1.5B, and 3B sub-models. Our suite is on par with independently trained baselines on benchmark performance and validation and out-of-domain perplexities, while using 36% less training compute and improving the throughput of speculative decoding by 14-26%. We also ablate key architectural choices, offering guidance for building strong Matryoshka LM suites.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nathan Godey, Yoav Artzi
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
