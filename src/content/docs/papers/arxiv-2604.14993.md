---
title: "Serving Chain-structured Jobs with Large Memory Footprints with Application to Large Foundation Model Serving"
description: "As a current trend in Artificial Intelligence (AI), large foundation models are increasingly employed as the core of AI services."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2604.14993) · [PDF](https://arxiv.org/pdf/2604.14993)

## 一句话摘要

As a current trend in Artificial Intelligence (AI), large foundation models are increasingly employed as the core of AI services.

## 为什么值得关注

待编辑增强。

## 摘要原文

As a current trend in Artificial Intelligence (AI), large foundation models are increasingly employed as the core of AI services. However, even after training, serving such models at scale remains a challenging task due to their heavy resource footprints, particularly in terms of GPU memory. While recent works revealed unique characteristics of systems serving foundation models that distinguish them from traditional distributed computing systems, there is still a lack of fundamental understanding of the underlying system management problems. This work aims at addressing this gap by extracting a novel problem of "server chain composition" via block placement and cache allocation for serving chainstructured jobs with large memory footprints, which models a fundamental problem in serving large foundation models through pipeline parallelism. After showing the NP-hardness of the optimal solution, the focus is turned to developing scalable algorithms with guaranteed performance under state-of-the-art load balancing. Application of the proposed solution to a distributed large language model (LLM) serving system shows significant reduction of response times compared to state-of-the-art solutions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tingyang Sun, Ting He, I-Hong Hou
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
