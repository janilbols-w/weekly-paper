---
title: "EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models"
description: "Disaggregating the two stages, Prefill and Decode, onto separate GPU pools is now a standard optimization for (text-only) LLM serving."
---

**评分：47/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2609.31551) · [PDF](https://arxiv.org/pdf/2609.31551)

## 一句话摘要

Disaggregating the two stages, Prefill and Decode, onto separate GPU pools is now a standard optimization for (text-only) LLM serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregating the two stages, Prefill and Decode, onto separate GPU pools is now a standard optimization for (text-only) LLM serving. However, multimodal LLMs (MLLMs), which add a third phase, Encode, pose new challenges for resource allocation. Encode turns images, video, or audio into embeddings that the language model can consume, yielding a three-stage Encode-Prefill-Decode (EPD) pipeline. Existing frameworks offer only partial answers: text-only PD systems lack Encode, while EPD frameworks expose it as a separate service without regulating downstream request flow. The pipeline also carries a structural resource imbalance: every request enters through Encode before downstream work can begin, yet per-request execution leaves the encode GPU severely underutilized even at high loads, starving the downstream Prefill and Decode workers. Addressing this, we reposition Encode as the control point of the EPD pipeline, exposing three tightly coupled dimensions: when work enters downstream, where prefill executes, and how the GPU is shared. We instantiate this in EAServe across two co-designed layers. Its runtime manages load-adaptive micro-batching, rate-controlled partial offload to a co-resident prefill worker, and dynamic SM partitioning for predictable co-location. The configuration layer, Hybrid Auto Selection (HAS), navigates the joint space of GPU allocation, encode batch size, and offload ratio by pruning unbalanced allocations with per-stage capacity profiling and refining the remainder through TPE-based Bayesian optimization. Evaluated on three MLLM architectures spanning image, video, and audio, EAServe delivers up to 4.3x and 1.7x higher goodput than NVIDIA Dynamo and vLLM, respectively, under identical SLO constraints, sustains more balanced and higher GPU utilization across the EPD pipeline, and reaches near-optimal configurations faster than baseline search methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: disaggregated serving, prefill-decode
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kunxiong Zhu, Zhihao Shu, Hangyu Zheng, Minghai Qin, Miao Yin, Gagan Agrawal, Wei Niu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
