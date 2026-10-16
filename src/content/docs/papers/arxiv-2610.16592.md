---
title: "Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcement Learning"
description: "Agentic reinforcement learning (RL) is commonly used to enhance the capabilities of large language models (LLMs) in solving complex multi-turn tasks."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](http://arxiv.org/abs/2610.16592v1) · [PDF](https://arxiv.org/pdf/2610.16592v1)

## 一句话摘要

Agentic reinforcement learning (RL) is commonly used to enhance the capabilities of large language models (LLMs) in solving complex multi-turn tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic reinforcement learning (RL) is commonly used to enhance the capabilities of large language models (LLMs) in solving complex multi-turn tasks. During rollout, agentic RL exhibits a workload pattern distinct from that of traditional RL: multi-turn interactions repeatedly introduce prefill requests, causing prefill and decode workloads to coexist throughout rollout. This workload makes prefill-decode (PD) disaggregation, a design widely used for online LLM serving, promising for speeding up agentic RL rollout. This paper shows that PD disaggregation can improve rollout efficiency by (a) mitigating interference among data-parallel attention modules, (b) enabling stage-specific parallelism, and (c) reducing end-to-end trajectory completion time. However, a fixed prefill-decode allocation may fail to sustain these benefits as workload composition varies across tasks and over time. We therefore present Prorsa, an agentic RL framework for prediction-guided prefill-decode resource allocation. Prorsa observes the lifecycle of every trajectory to forecast short-horizon prefill and decode demand. These forecasts then guide worker allocation decisions and trigger role switching of rollout engines, aligning prefill and decode capacity with anticipated workload demand. Across synchronous and asynchronous agentic RL settings, Prorsa achieves end-to-end rollout speedups of 1.11x-4.05x over prefill-decode colocation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefill-decode
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Chiheng Lou, Xiangwei Deng, Bangjun Xiao, Xiaodong Ji, Yikai Zhao, Xin Jin, Hailin Zhang
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
