---
title: "GeoMesh: Workload-Balanced and Sign-Compressed Geo-Distributed LLM Training"
description: "Large language models are increasingly trained on GPUs distributed across multiple regions, but geo-distributed training is challenging in practice."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.18388) · [PDF](https://arxiv.org/pdf/2609.18388)

## 一句话摘要

Large language models are increasingly trained on GPUs distributed across multiple regions, but geo-distributed training is challenging in practice.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly trained on GPUs distributed across multiple regions, but geo-distributed training is challenging in practice. Real clusters often contain GPUs with different speeds and memory capacities, and they communicate over slow wide-area networks. Our analysis shows that this creates serious problems: existing synchronous methods preserve stable updates, but fast GPUs wait up to 20.9% of their runtime for slower ones, and all workers spend, on average, 65.8% of their runtime on synchronization. Recent asynchronous methods reduce waiting time but worsen the model accuracy due to stale updates. To address the problems, we present GeoMesh, a synchronous geo-distributed training framework for heterogeneous GPUs. GeoMesh balances per-worker workloads by assigning each GPU a suitable batch size and number of inner steps, so faster GPUs do more useful work instead of waiting. It also reduces communication volume by nearly 32x by exchanging compressed sign-based pseudo-gradients with lightweight magnitude and token count. Across heterogeneous GPUs and Azure-derived WAN, GeoMesh reduces time-to-target perplexity by up to 70.2% over representative baselines and lowers straggler- and WAN-induced GPU idle by up to 8.0x and 5.6x, respectively, while preserving comparable zero-shot accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Changyong Shin, Jaerim Park, Minchul Kang, Younghun Go, Zhixiong Niu, Yongqiang Xiong, Gyeongsik Yang, Chuck Yoo
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
