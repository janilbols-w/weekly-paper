---
title: "In-Network Market Prediction Using Machine Learning and Limit Order Books"
description: "Machine learning is significantly transforming algorithmic trading, yet the requirement for rapid execution speeds persists."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.02424) · [PDF](https://arxiv.org/pdf/2608.02424)

## 一句话摘要

Machine learning is significantly transforming algorithmic trading, yet the requirement for rapid execution speeds persists.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine learning is significantly transforming algorithmic trading, yet the requirement for rapid execution speeds persists. While both aspects aim to boost profitability, embedding advanced machine-learning techniques with reduced trading latency presents a notable challenge. Adopting in-network machine learning, which involves offloading inference to programmable network devices, offers a delicate equilibrium in this trade-off. In this paper, we present LOBIN, a solution that utilizes machine learning within the network for market prediction based on high-frequency market data feeds. LOBIN is adept at constructing limit order books and performing inference directly within programmable switches. When compared to server-based benchmarks, LOBIN not only predicts future stock price movements with higher throughput but also maintains robust machine learning performance. It achieves over a 10% reduction in latency compared to the NASDAQ order-matching server benchmark and delivers microsecond-level latency. Furthermore, the machine learning performance of LOBIN can be further enhanced through the adoption of a hybrid deployment approach that integrates both the switch and the servers. Our evaluation demonstrates that among all data feeds of evaluated stocks, the application of hybrid deployment results in approximately 45% of the traffic and 38\% of the total potential transaction value being processed within switches without server intervention, reducing latency while ensuring that the average change in error rate of predictions remains at around 3% relative to benchmarks based solely on server use.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinpeng Hong, Changgang Zheng, Joshua Lilley, Stefan Zohren, Noa Zilberman
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
