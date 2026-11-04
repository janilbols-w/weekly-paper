---
title: "Inference First, Training Underneath: Layer-Granular LoRA Co-Serving with LayerLoom"
description: "Serving and fine-tuning a large language model on the same GPUs can turn the idle capacity between inference bursts into training progress, and low-rank adaptation (LoRA) makes this co-location cheap because both workloads read a single frozen copy of the base weights."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2611.00652) · [PDF](https://arxiv.org/pdf/2611.00652)

## 一句话摘要

Serving and fine-tuning a large language model on the same GPUs can turn the idle capacity between inference bursts into training progress, and low-rank adaptation (LoRA) makes this co-location cheap because both workloads read a single frozen copy of the base weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving and fine-tuning a large language model on the same GPUs can turn the idle capacity between inference bursts into training progress, and low-rank adaptation (LoRA) makes this co-location cheap because both workloads read a single frozen copy of the base weights. The difficulty lies in the fine-tuning backward pass, which has no counterpart in inference. Current co-serving systems schedule backward work per serving iteration: each iteration carries a fixed backward budget, and requests that arrive in the meantime wait for it to finish, so fine-tuning dictates inference latency whenever load spikes. We observe that the backward pass of a LoRA microbatch decomposes into per-layer tasks over the same weights that the inference forward pass visits, which allows backward work to be scheduled at layer rather than iteration granularity. Building on this observation, LayerLoom attaches same-layer backward tasks to the inference forward pass and, at each layer, runs only as many of them as the latency slack of in-flight requests permits. To keep a ready task at every layer, LayerLoom maintains a wavefront of fine-tuning microbatches staggered across layers, and it bounds the wavefront's activation memory by offloading microbatch state to host memory and prefetching it ahead of the layer where the scheduler plans to use it. A fused kernel serves the paired forward and backward GEMMs from a single read of each base weight. Because all backward work of an iteration finishes within its forward pass, new requests join the next iteration as in continuous batching. On an RTX 4090 GPU running Llama-3.1-8B under a bursty production trace, LayerLoom raises joint SLO attainment by 13.5-21.8 points over prior works with fine-tuning throughput that is comparable or up to 12% higher, and it reaches the same training losses.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: continuous batching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zongpu Zhang, Yishu Yin, Xuehai Qian
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
