---
title: "Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal"
description: "Providing real-time multimodal insights into images is challenging because it requires low latency, high description accuracy, and scalable solutions that are both cost-effective and efficient."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.12725) · [PDF](https://arxiv.org/pdf/2611.12725)

## 一句话摘要

Providing real-time multimodal insights into images is challenging because it requires low latency, high description accuracy, and scalable solutions that are both cost-effective and efficient.

## 为什么值得关注

待编辑增强。

## 摘要原文

Providing real-time multimodal insights into images is challenging because it requires low latency, high description accuracy, and scalable solutions that are both cost-effective and efficient. For example, given a new image of an outfit, we would like to generate insights that the image depicts "earth tones" and "linen pants" and allow users to explore similar ideas along these themes. Traditional strategies to generate such insights would typically involve building taxonomies producing a golden set labeled by humans, training models on these datasets, and deploying these models for online inference services. Such workflows are constrained by fixed taxonomy, high labeling cost, limited labeling coverage in sample space, and human errors and expertise gaps in labelers. In addition, these methods are expensive and cumbersome to iterate over time. Recent trends have started exploring generative AI models for online insights, but this method suffers from long latency and prohibitive costs to support a high volume of requests or large amounts of offline labeling needs. We present Generative Labeling On Clusters (GLOC) as a solution to provide highly scalable, cost-effective, low latency, and high accuracy online image insight services. GLOC leverages highly optimized image embeddings to form image clusters that are semantically close to each other for the purpose of the type of insights, and summarizes the insights at the cluster level, which effectively generalizes to members in the cluster. At Pinterest, GLOC powers image descriptors and pivot query suggestions for Hybrid Search, which is a multimodal search service enabling users to search with both an image and a text query. Our offline and online A/B tests demonstrate that GLOC significantly outperforms previous methods, delivering improvements in quality and efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: online inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenjie Zhang (Irene), Sainan Chen (Irene), Kshiteesh Hegde (Irene), Mengze (Irene), Li, Pouya Rezazadeh Kalehbasti, Munachim Ezema, Karina Sobhani
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
