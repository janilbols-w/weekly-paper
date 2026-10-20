---
title: "A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill-Decode Disaggregation"
description: "The growing adoption of large language models (LLMs) has significantly increased the compute and memory demands of inference serving."
---

**评分：50/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2610.26131) · [PDF](https://arxiv.org/pdf/2610.26131)

## 一句话摘要

The growing adoption of large language models (LLMs) has significantly increased the compute and memory demands of inference serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growing adoption of large language models (LLMs) has significantly increased the compute and memory demands of inference serving. A key challenge arises from the mismatch between compute-bound prefill and memory-bound decoding: when executed together, the two phases interfere, while separating them via prefill-decode (PD) disaggregation leads to substantial resource underutilization. Specifically, prefill leaves memory bandwidth underutilized, whereas decoding underutilizes compute resources. Prior approaches, such as GPU Streaming Multiprocessor (SM) partitioning, attempt to improve utilization by spatially dividing GPU resources. However, these approaches remain fundamentally limited, as memory-bound decoding still requires a large number of SMs to saturate bandwidth, reducing the compute resources available for prefill and resulting in an inherent trade-off. To address this limitation, we propose DuoPD, a hybrid PD-disaggregation architecture that integrates lightweight Processing-Near-Memory (PNM) units into the HBM logic die. Unlike prior PIM/PNM designs that rely on costly internal bandwidth scaling and offload only partial decoding operations, DuoPD enables full decoding execution on PNM by leveraging bandwidth sharing with the GPU over a shared HBM interface. This allows compute-bound prefill and memory-bound decoding to execute concurrently with minimal interference, improving both compute and memory utilization. To realize this design, we develop a compact PNM microarchitecture, a TSV-level bandwidth sharing mechanism, and a hierarchical data mapping scheme tailored for hybrid GPU-PNM execution. Evaluations on server-scale LLMs demonstrate that DuoPD achieves up to 2.23x higher end-to-end throughput than conventional PD-disaggregation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefill-decode
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sanghyeok Han, Inseong Choi, Byungkuk Yoon, Gyeonghwan Park, Jae-Joon Kim
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
