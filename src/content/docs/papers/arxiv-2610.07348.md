---
title: "Stepped MoE: Segment-Level Routing with Configurable Inference Complexity"
description: "Training large language models (LLMs) is resource-intensive, and adapting them for diverse deployment scenarios with varying computational constraints remains challenging."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.07348) · [PDF](https://arxiv.org/pdf/2610.07348)

## 一句话摘要

Training large language models (LLMs) is resource-intensive, and adapting them for diverse deployment scenarios with varying computational constraints remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large language models (LLMs) is resource-intensive, and adapting them for diverse deployment scenarios with varying computational constraints remains challenging. While elastic architectures enable flexible model deployment and sparsely activated models allow input-adaptive computation, existing approaches treat these dimensions independently. Moreover, models catered towards on-device edge inference need to conform to the memory and compute limitations of the serving devices. In this paper, we introduce a unified framework that combines elastic structures with sparsely gated architectures to create models that adapt simultaneously to both deployment constraints and task requirements. Our approach employs a model backbone that conditions on both the context and target efficiency specifications, enabling fine-grained control over the accuracy-efficiency trade-off at inference time. The model learns to activate task-relevant parameters within elastically-nested sub-networks, allowing a single model to span multiple capacity points while maintaining input-adaptive routing. Through experiments we demonstrate that we can create a model that allows the flexibility to use 1,2,3,4 billion parameters while being more accurate than their dense counter-parts (2-5\% on knowledge-intensive benchmarks) and at par with their static versions while delivering similar latency metrics as dense models. Overall, we save on device disk space by sharing the model parameters, allow flexibility of serving based on DRAM and compute available while delivering more accurate results.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Arnav Kundu, Zhaoyang Xu, Bairu Hou, Chang Gao, Reed Li, Tao Lei
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
