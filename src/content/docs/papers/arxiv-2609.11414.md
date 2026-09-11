---
title: "SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language Model Conversations"
description: "Large language models exhibit complementary strengths, motivating routing methods that dispatch each query to the most suitable model."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.11414) · [PDF](https://arxiv.org/pdf/2609.11414)

## 一句话摘要

Large language models exhibit complementary strengths, motivating routing methods that dispatch each query to the most suitable model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models exhibit complementary strengths, motivating routing methods that dispatch each query to the most suitable model. Although existing routers are effective in single-turn settings, they do not directly transfer to multi-turn dialogue, where routing performance critically depends on how historical context is segmented, retained, and incorporated into the current prompt. This introduces two fundamental challenges: preventing information loss and information confusion during context construction, and evaluating routing quality without conflating model selection with prompt construction quality. In this paper, we propose SWRouter, a Similarity-Contractive Window Router for multi-turn large language model routing. SWRouter combines a similarity-based context segmentation mechanism for prompt construction with a dual-metric evaluation framework that decouples construction accuracy from router performance. Experiments on multi-turn dialogue benchmarks demonstrate that SWRouter consistently surpasses strong baselines, achieving a 16.26% improvement in evaluation accuracy over the best individual large language model and an additional 8.22% gain over the Conv-ID Context baseline. Our results highlight that multi-turn large language model routing requires a joint design of context construction and evaluation, rather than a direct extension of single-turn routing methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yu Wang, Yuchen Li, Rui Kong, Xinran Chen, Jiamin Chen, Hengyi Cai, Shuaiqiang Wang, Jiashu Zhao, Yulun Zhang, Zhonghao Lyu, Haoyi Xiong, Linghe Kong, Jimmy Xiangji Huang, Dawei Yin
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
