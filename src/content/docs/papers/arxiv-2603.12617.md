---
title: "When Drafts Evolve: Speculative Decoding Meets Online Learning"
description: "Speculative decoding has emerged as a widely adopted paradigm for accelerating large language model inference, where a lightweight draft model rapidly generates candidate tokens that are then verified in parallel by a larger target model."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2603.12617) · [PDF](https://arxiv.org/pdf/2603.12617)

## 一句话摘要

Speculative decoding has emerged as a widely adopted paradigm for accelerating large language model inference, where a lightweight draft model rapidly generates candidate tokens that are then verified in parallel by a larger target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding has emerged as a widely adopted paradigm for accelerating large language model inference, where a lightweight draft model rapidly generates candidate tokens that are then verified in parallel by a larger target model. However, due to limited model capacity, drafts often struggle to approximate the target distribution, resulting in shorter acceptance lengths and diminished speedup. A key yet under-explored observation is that speculative decoding inherently provides verification feedback that quantifies the deviation between the draft and target models at no additional cost. This process naturally forms an iterative "draft commits-feedback provides-draft adapts" evolving loop, which precisely matches the online learning paradigm. Motivated by this connection, we propose OnlineSPEC, a unified framework that systematically leverages interactive feedback to continuously evolve draft models. Grounded in dynamic regret minimization, we establish a formal link between online learning performance and speculative system's acceleration rate, and develop novel algorithms via modern online learning techniques, including optimistic online learning that adaptively reuses historical gradients as predictive update hints, and online ensemble learning that dynamically maintains multiple draft models. Our algorithms are equipped with theoretical justifications and improved acceleration rates, achieving up to 24% speedup over seven benchmarks and five foundation models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yu-Yang Qian, Hao-Cong Wu, Yichao Fu, Hao Zhang, Peng Zhao
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
