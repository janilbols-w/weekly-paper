---
title: "An Approximate Queueing Model of LLM Inference Serving for SLO-Driven Autoscaling"
description: "Performance models of LLM servers support both latency evaluation and the design of controllers for autoscaling against service level objectives (SLOs) and for inference optimization."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.20957) · [PDF](https://arxiv.org/pdf/2609.20957)

## 一句话摘要

Performance models of LLM servers support both latency evaluation and the design of controllers for autoscaling against service level objectives (SLOs) and for inference optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Performance models of LLM servers support both latency evaluation and the design of controllers for autoscaling against service level objectives (SLOs) and for inference optimization. We model the multiplexed execution of prefill and decode operations with a tractable, approximate queueing model under Markovian assumptions. Three parameters characterize a model-accelerator pair, namely a baseline per-iteration overhead, a per-token compute cost, and a per-token key-value (KV) cache access cost. The model combines a mean-value analysis of per-iteration work with a state-dependent Markov chain for batch occupancy to predict mean time to first token (TTFT) and inter-token latency (ITL). We validate these predictions against measurements and show that the three parameters can be estimated from observed latencies. Over a grid of input and output lengths and arrival rates spanning light to moderate load, the relative error of the average ITL is about 5% for Llama-3.1-8B and 8% for Qwen2.5-14B running on an H100 GPU, and the corresponding TTFT errors are 14% and 16%. We then implement an autoscaling controller that uses the model to adjust inference-server replica counts as the workload changes. On an OpenShift cluster of H100 GPUs it tracks a fourfold load ramp under both latency targets, missing one in 7 of 127 control cycles, and its in-loop predictions carry median errors of at most 5% for TTFT and 9% for ITL. A decode-throughput analyzer from an existing autoscaler, which takes no latency target, misses 27 of 128 cycles under the same controller and load while provisioning 4% and 28% fewer replicas.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vishakha Ramani, Asser N. Tantawi
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
