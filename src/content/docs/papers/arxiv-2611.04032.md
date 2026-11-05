---
title: "ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration"
description: "Serving an LLM efficiently depends on the engine, how the model is split across GPUs, precision, scheduler settings, speculative decoding, KV-cache management, and prefill-decode disaggregation."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.04032) · [PDF](https://arxiv.org/pdf/2611.04032)

## 一句话摘要

Serving an LLM efficiently depends on the engine, how the model is split across GPUs, precision, scheduler settings, speculative decoding, KV-cache management, and prefill-decode disaggregation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving an LLM efficiently depends on the engine, how the model is split across GPUs, precision, scheduler settings, speculative decoding, KV-cache management, and prefill-decode disaggregation. The best configuration depends on the model, hardware, workload, and objective. Operators usually find it by trial and error. Exhaustively measuring the candidates in our study would take about 25,000 GPU-hours. ROCm InferaSim predicts serving performance from a few short measurements. Choices such as batch size, prompt length, and GPU count change the amount of work per GPU without changing the kernels. ROCm InferaSim benchmarks each distinct set of kernels once, on at most one node. We call this measurement an anchor. Analytical laws carry that anchor to other deployments that run the same kernels. For multi-node deployments, ROCm InferaSim reduces the configuration to a single-node equivalent, measures it, and scales the result analytically. A simulator replays multi-turn traffic, and a tuning agent searches configurations using the predictions. On AMD Instinct MI355X GPUs with vLLM, SGLang, and ATOM, 11 anchors took 9.1 GPU-hours, against 204 GPU-hours to measure the 226 fixed-length configurations they cover. On 172 configurations, time per output token has 8.1% median error. On a multi-turn coding workload, throughput is within 8%. For 159 disaggregated deployments, none used as an anchor, throughput is within 5.5%. A five-candidate short list contains a deployment within 12% of the best feasible pairing of model and latency target.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anshu Raina, Yao Fu, Zhang Jiejing, Peyman Razaghi, Shiksha Patel, Ravi Gupta, Deval Shah, Adeem Jassani, Subhajit Dutta Chowdhury, Lorri Rao, Kailash Gogineni, Zhenyu Gu, Onil Gunawardana, Emad Barsoum
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
