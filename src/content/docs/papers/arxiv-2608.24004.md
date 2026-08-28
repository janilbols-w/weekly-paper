---
title: "AgentSpec: Speculative Decoding for Batch Inference of LLM Agents"
description: "Large language model (LLM)-based agent applications often incur high response time."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.24004) · [PDF](https://arxiv.org/pdf/2608.24004)

## 一句话摘要

Large language model (LLM)-based agent applications often incur high response time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM)-based agent applications often incur high response time. Speculative decoding is a promising solution to improve the inference efficiency of LLM agents without impacting generation quality. However, state-of-the-art speculative decoding algorithms exhibit substantial speed degradation under large batch sizes, limiting their effectiveness to deploy in real-world agent applications. In this work, we first present a systematic analysis of speculative decoding for LLM agents and identify two dominant factors of speedup degradation: high rejection rate of speculative tokens, and under-utilization of dynamic token budgets.B ased on these observations, we propose AgentSpec, a speculative decoding algorithm that addresses the limitations of existing methods for LLM agents. AgentSpec incorporates structure-isolated drafting that constrains speculation to semantically coherent segments of the agent workflow, reducing the drafts of irrelevant semantic paths and achieving an extremely low rejection rate. Moreover, AgentSpec adopts redundancy-aware budget allocation that exploits agent-level information to better utilize the dynamically-free token budget during the agent inference. We implement and evaluate AgentSpec on five different workloads and four different models from four different LLM families in vLLM. Our results demonstrate the superiority of AgentSpec over state-of-the-arts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xin Wang, Ziming Miao, Yi Zhu, Hui Shen, Zhongwei Wan, Fan Yang, Mi Zhang
- 发布：2026-08-25；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
