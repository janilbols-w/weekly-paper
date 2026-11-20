---
title: "DynaDFlash: Dynamic Feature Projection for Block Diffusion Speculators"
description: "DFlash trains a parallel draft model on hidden features from its target model."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](http://arxiv.org/abs/2611.19085v1) · [PDF](https://arxiv.org/pdf/2611.19085v1)

## 一句话摘要

DFlash trains a parallel draft model on hidden features from its target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

DFlash trains a parallel draft model on hidden features from its target model. Inspired by the previous work of DFlare that introduced per layer combinations of target hidden states, we test whether context dependent weighting of these states helps improve acceptance length of block diffusion speculators. We trained both a DFlash baseline for the Qwen 3 of block size 16, and a dynamic model that computes gates for each layer to affect the magnitude of hidden features before projection. While mean acceptance length between the dynamic model and the DFlash baseline didn't significantly differ, we notice that the dynamic model excels for drafting in the context of math. In an evaluation of 700 prompts from the MetaMathQA and Orca-Math datasets, the mean accepted length improves by 5%. We also found this lead to a 4.1% higher throughput for a subset of the same dataset in the context of speculative decoding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Aadi Kulshrestha, Reese Chong
- 发布：2026-11-14；更新：2026-11-14
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/midas-llm-research/DynaDFlash](https://github.com/midas-llm-research/DynaDFlash)
- 阅读深度：metadata
