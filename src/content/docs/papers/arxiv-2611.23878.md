---
title: "HETEROVLM: Edge Multi-Request Vision-Language Model Serving on a Heterogeneous Versal SoC with AI Engines and Programmable Logic"
description: "Edge devices in vehicles and robots serve concurrent requests with different deadlines to a vision-language model (VLM), each mixing a compute-bound encoder and prefill with a memory-bound decode."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.23878) · [PDF](https://arxiv.org/pdf/2611.23878)

## 一句话摘要

Edge devices in vehicles and robots serve concurrent requests with different deadlines to a vision-language model (VLM), each mixing a compute-bound encoder and prefill with a memory-bound decode.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge devices in vehicles and robots serve concurrent requests with different deadlines to a vision-language model (VLM), each mixing a compute-bound encoder and prefill with a memory-bound decode. GPU serving targets datacenter throughput with per-iteration host scheduling: an urgent request waits for the running iteration, and small-batch decode costs much energy per token. Prior accelerators on Versal AI Engine (AIE) SoCs map one model onto a fixed AIE dataflow graph for one input stream, without decode or request scheduling. HETEROVLM keeps the AIE graph static and makes it schedulable. The AIE array runs the encoder, prefill and attention, and the programmable logic (PL) holds GEMV engines for small decode steps and a scheduler that orders short work units by class and deadline. Concurrent requests share one decode step that reads the weights once. An urgent request preempts at a work-unit boundary, and the paused request resumes from its results in DDR. On an AMD Versal VC1902, text and camera questions get their first tokens in 140 and 303 ms. HETEROVLM decodes a single request 1.3x and 4.0x faster than NVIDIA Tesla T4 and Jetson Orin Nano GPUs, with 61% and 73% of their energy per token, and uses 51% of the energy per token of an NVIDIA GeForce RTX 3090 Ti. The same bitstream serves multiple VLMs by loading their own instruction programs and weights. A demo is available at https://anonymous.4open.science/r/demo heterovlm-EFM2/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhiheng Chen, Yu-An Chou, Yifan Zhang, Ye Qiao, Saptarshi Mitra, Sitao Huang
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
