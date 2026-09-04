---
title: "BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training"
description: "Long-context reasoning for large language models (LLMs) is becoming increasingly important, but training over long sequences remains challenging due to massive memory and communication requirements."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2609.03151) · [PDF](https://arxiv.org/pdf/2609.03151)

## 一句话摘要

Long-context reasoning for large language models (LLMs) is becoming increasingly important, but training over long sequences remains challenging due to massive memory and communication requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context reasoning for large language models (LLMs) is becoming increasingly important, but training over long sequences remains challenging due to massive memory and communication requirements. Sequence parallelism has emerged as an essential technique for addressing bottlenecks in long sequence LLM training. However, we observe that existing sequence parallelism methods are batch-agnostic and apply uniform sequence partitioning across all batch sizes, resulting in inefficient communication. In this paper, we introduce Batch- Aware Sequence Parallelism (BASP), a sequence parallelism approach that leverages batch structure to reduce communication overhead. BASP exploits batch structure by partitioning GPUs into disjoint sequence-parallel groups according to the micro- batch size. This design reduces the all-to-all communication group size, thereby localizing communication and improving training efficiency. Experimental results on an NVIDIA A100 cluster show that BASP improves end-to-end training time by up to 1.17 - 1.31x in Llama and Qwen models compared to standard sequence parallel baselines, while preserving identical model accuracy and memory usage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sequence parallel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Bigyan Ghimire, Jon C. Calhoun
- 发布：2026-09-02；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
