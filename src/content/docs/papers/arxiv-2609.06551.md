---
title: "EStream: Fast and Memory-Efficient MoE Prefill through Expert Virtualization on Mobile NPUs"
description: "Mobile vendors and application developers increasingly deploy LLMs on smartphones for diverse prefill-only services."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.06551) · [PDF](https://arxiv.org/pdf/2609.06551)

## 一句话摘要

Mobile vendors and application developers increasingly deploy LLMs on smartphones for diverse prefill-only services.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mobile vendors and application developers increasingly deploy LLMs on smartphones for diverse prefill-only services. Yet current systems rely mainly on dense models whose regular computation maps efficiently to mobile NPUs, leaving more capable MoEs underused. MoE prefill does not fit mobile NPUs: NPU graphs are fixed at compile time, yet MoE picks experts at runtime; and one request touches most experts, more than a phone can hold in memory. We present EStream, which resolves both by separating what the NPU must fix from what MoE decides at runtime. A single compiled expert graph serves every expert, with each expert's routed tokens and weight address bound at call time, so dynamic MoE execution runs entirely on the NPU without padding or CPU/GPU fallback. Expert virtualization keeps the expert pool in UFS flash storage and pages it through a fixed-size NPU-addressable arena, group by group, with loading hidden behind computation, so memory is bounded by the arena rather than by the model. It further introduces a hardware-aware configuration algorithm that automatically configures the UFS--NPU pipeline and maximizes loading--computation overlap. Across 18 comparative settings covering three 7B--16B MoEs and 256--4,096-token prompts, we evaluate EStream on a commercial Snapdragon smartphone. Compared to the fastest baseline at each setting, EStream achieves a 2.25--27.57X pure-prefill TTFT speedup and reduces peak physical memory by 1.19--12.29X. EStream further scales to MoE models with up to 46.7B parameters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Junming Zhang, Zhenzhe Zheng, Fan Wu, Xiaoyao Huang, Jie Wu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
