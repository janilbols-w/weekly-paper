---
title: "Lightweight Scheduling Policies for Continuously Batched LLM Serving Across GPU Architectures"
description: "Large language model serving is increasingly limited not only by model size and GPU speed, but also by scheduling during autoregressive decoding, where continuous batching interleaves requests at token granularity as sequences arrive and finish."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](http://arxiv.org/abs/2610.15899v1) · [PDF](https://arxiv.org/pdf/2610.15899v1)

## 一句话摘要

Large language model serving is increasingly limited not only by model size and GPU speed, but also by scheduling during autoregressive decoding, where continuous batching interleaves requests at token granularity as sequences arrive and finish.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model serving is increasingly limited not only by model size and GPU speed, but also by scheduling during autoregressive decoding, where continuous batching interleaves requests at token granularity as sequences arrive and finish. We study whether lightweight scheduling policies can improve latency-throughput tradeoffs without changing model architectures, kernels, or deploying learned schedulers. We implement a Python/PyTorch continuous-batching testbench with real Hugging Face execution and evaluate eight policies across 1,152 GPU-model-scheduler-workload runs using ShareGPT-derived traffic, six Qwen, Gemma, and Mistral models, and Modal L40S, A100, and H100 GPUs. Scheduler choice changes throughput, TTFT, completion latency, and tail behavior under fixed model, GPU, workload, batch size, and prefill budget. Aging shortest-prompt-first is the strongest practical baseline in many L40S and mixed-workload settings, while oracle remaining-length scheduling shows that job-size knowledge alone is insufficient because batching and hardware effects also shape performance. The custom dataset has been uploaded to Hugging Face.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ashman Mehra, Akshan Agarwal, Aryeh Carmi
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
