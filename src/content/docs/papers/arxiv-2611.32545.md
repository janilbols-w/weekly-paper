---
title: "RePrism: Joint Request and Representation Scheduling for LLM Agent Serving"
description: "Agentic workflows often invoke large language models multiple times."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.32545) · [PDF](https://arxiv.org/pdf/2611.32545)

## 一句话摘要

Agentic workflows often invoke large language models multiple times.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic workflows often invoke large language models multiple times. When the dependencies are visible to the serving system, it can use them to schedule requests and cache reusable content, improving workflow execution efficiency. Prior work has largely focused on ordering requests or managing shared resources under a fixed caching scheme. A reusable prompt that specifies model behavior, however, can have multiple representations. We present RePrism, a serving system that jointly selects which ready request to serve and which eligible representation of its prompt to use. Its goal is to improve throughput and shorten session completion time (SCT). The scheduler ranks pairs of requests and representations by combining each pair's immediate value with an estimate of its future value based on the visible workflow. The resource manager allocates GPU memory to both LoRA adapters and cached key-value states. It also coordinates their admission and eviction as memory pressure changes. We compare RePrism with S-LoRA on a dynamic workload with an arrival rate of 1.8 sessions per second, and it achieves 1.37 times the request throughput and reduces P95 SCT by a factor of 4.10. Under controlled load, RePrism reduces mean time to first token by a factor of 5.26 relative to S-LoRA. On a controlled workload, RePrism's joint scoring achieves 2.7% higher request throughput and 12.3% lower mean SCT than a policy that ranks requests before selecting their representations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xijiang Shen, Aoli Zhu, Yanbo Tan, Xiyuan Hu, Huailiang Tan
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
