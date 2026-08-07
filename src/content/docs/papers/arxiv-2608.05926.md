---
title: "BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks"
description: "Edge inference is a promising paradigm to provide large language model (LLM) inference services in next-generation mobile networks."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.05926) · [PDF](https://arxiv.org/pdf/2608.05926)

## 一句话摘要

Edge inference is a promising paradigm to provide large language model (LLM) inference services in next-generation mobile networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge inference is a promising paradigm to provide large language model (LLM) inference services in next-generation mobile networks. LLM inference mainly relies on two approaches: Autoregressive decoding (AD) generates output tokens sequentially, resulting in long latency; Speculative decoding (SD) accelerates inference by using a small language model (SLM) to generate multiple draft tokens for LLM verification, but incurs extra memory costs. Due to this latency-memory tradeoff, neither approach alone can efficiently serve users with heterogeneous demands under limited edge computing resources. To address this challenge, we propose a hybrid autoregressive-speculative inference (BALANCE) framework for edge LLM inference. In BALANCE, an edge server hosts both an SLM and an LLM, assigns each user to AD or SD, and performs the two modes simultaneously. To maximize the number of served users, we formulate a task throughput maximization problem to jointly determine user scheduling and computing resource allocation between AD and SD under user latency requirements and server memory constraints. Since the problem is NP-hard, we develop a polynomial-time algorithm that transforms the original problem into two sub-problems and obtains a sub-optimal solution with a constant approximation guarantee. Experiments demonstrate that BALANCE consistently outperforms conventional AD and SD and significantly improves task throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guanqiao Qu, Shuo Chen, Qian Chen, Kin K. Leung, Xianhao Chen
- 发布：2026-08-06；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
