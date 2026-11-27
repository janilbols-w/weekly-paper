---
title: "PipeAxes: Decoupling Compute and Communication Granularities for Pipeline-Parallel LLM Serving"
description: "Pipeline parallelism can serve long-context language models on PCIe servers and across heterogeneous GPU clusters."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.34615) · [PDF](https://arxiv.org/pdf/2611.34615)

## 一句话摘要

Pipeline parallelism can serve long-context language models on PCIe servers and across heterogeneous GPU clusters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pipeline parallelism can serve long-context language models on PCIe servers and across heterogeneous GPU clusters. Existing engines split prefill into token chunks to limit decode stalls. The chunk size also sets the GPU batch width and the size of activation transfers between stages. Small chunks reload model weights more often. Large chunks can keep the GPU and the link busy long enough to delay interactive requests. PipeAxes runs wide prefill batches a few layers at a time so decodes can run between slices. A fused Triton Hadamard-INT4 codec compresses activations, which travel in independently sized row groups over parallel TCP sockets. The scheduler uses latency slack to choose batch width, slice depth, and row-group size. We evaluated PipeAxes in 97 replays covering 5,016 requests on A800, RTX 4090, and RTX 3090 GPUs. All 74 requests met their latency targets during a tenfold bandwidth swing. In a four-stage mixture-of-experts pipeline, PipeAxes served requests within their latency targets at 23.3x the rate of calibrated Revisit-PP and 4.44x the rate of Fixed-4096 with Express. In a mixed 64K-context workload, p95 time to first token for short requests fell from 129.8 s with native vLLM to 512 ms. With INT4 transport, MMLU accuracy rose by 0.06 percentage points and GSM8K accuracy fell by 0.46 percentage points relative to BF16.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiaoqiang Guo, Yifan Lin, Yang Liu, Jianan Zhang, Yingqi Peng, Jiamei Lv, Yi Gao, Wei Dong
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
