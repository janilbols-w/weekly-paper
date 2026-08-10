---
title: "Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM"
description: "Heterogeneous architectures that combine neural processing unit (NPU) and processing-in-memory (PIM) are increasingly adopted to accelerate LLM inference."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.06989) · [PDF](https://arxiv.org/pdf/2608.06989)

## 一句话摘要

Heterogeneous architectures that combine neural processing unit (NPU) and processing-in-memory (PIM) are increasingly adopted to accelerate LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Heterogeneous architectures that combine neural processing unit (NPU) and processing-in-memory (PIM) are increasingly adopted to accelerate LLM inference. Prior work focuses on building a unified memory that allows NPUs and PIM to share data without duplication. However, these designs implicitly assume that each tensor is bound to a fixed execution device, and therefore rely on static, device-biased data mappings. We observe that this assumption does not hold in modern LLM workloads. Due to phase changes (e.g., prefill vs. decode) and dynamic behaviors such as MoE routing, the optimal execution device for the same tensor can change at runtime. Under such dynamic execution, device-biased mappings become mismatched to access patterns, leading to substantial bandwidth underutilization and performance loss. This paper presents PFM (PIM-as-Flexible-Memory), a dual-view memory system that decouples physical data layout from accessor-visible logical views. PFM stores data in a jointly optimized physical layout and exposes different logical interpretations to NPUs and PIM, enabling efficient access across devices without data duplication or relayout. We further design accessor-aware address translation and runtime scheduling mechanisms to support dynamic execution when LLM workloads fluctuate and the optimal execution device dynamically changes. Our evaluation across LLMs shows that PFM improves end-to-end throughput by up to 2.32$\times$, demonstrating its effectiveness and broad applicability as a unified memory management solution for NPU-PIM systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management, unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shixin Zhao, Lian Liu, Tianhua Han, Mengdi Wang, Yinhe Han, Ying Wang
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
