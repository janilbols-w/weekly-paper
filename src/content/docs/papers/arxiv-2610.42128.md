---
title: "DecisionRank: On-Policy Distillation for Decision-Model Rerankers"
description: "Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.42128) · [PDF](https://arxiv.org/pdf/2610.42128)

## 一句话摘要

Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses preferences through a ranked list of document ID sequences, while the student determines the ranking using scores from the first-token position. To bridge this gap, we introduce DecisionRank, a decision model trained through item-space on-policy distillation (OPD). Item-space OPD constructs the student's rollout by sorting its document scores into a ranked sequence. A generative teacher takes the resulting ranking list as inputs and provides conditional feedback to directly supervise those scores. Combined with offline ranking supervision, DecisionRank achieves state-of-the-art performance on both general and reasoning-intensive retrieval benchmarks such as TREC DL, BEIR, and BRIGHT. Across four benchmarks, item-space OPD consistently outperforms alternative training objectives. Even at 1.7B parameters, DecisionRank surpasses its 27B generative teacher on TREC DL19--23. At 8B, it outperforms its generative listwise counterpart while running $24.5\times$ faster on TREC DL and $16.7\times$ faster on BRIGHT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanran Wu, Dian Yu, Chongyang Bai, Jieyi Zhang, Rui Liu, Tianyi Chen, Shike Mei, Hang Cui, Frank Shyu, Sandeep Pandey, Luke Simon, Chunwei Liu, Xi Liu
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
