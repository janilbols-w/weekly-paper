---
title: "Characterizing High Bandwidth Flash for LLM Serving"
description: "Large language model (LLM) serving requires substantial memory to store model weights and KV caches."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.39131) · [PDF](https://arxiv.org/pdf/2609.39131)

## 一句话摘要

Large language model (LLM) serving requires substantial memory to store model weights and KV caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving requires substantial memory to store model weights and KV caches. As models grow larger and contexts become longer, memory capacity and bandwidth increasingly become bottlenecks for serving performance. Agentic workloads compound this pressure through repeated interactions over growing contexts, making it increasingly important to retain KV state for reuse. High-bandwidth flash (HBF) offers a way to expand accelerator memory capacity for large language model (LLM) serving, but its access costs and limited write endurance complicate its use. We evaluate HBF for high-throughput agentic serving across system design and scheduling choices to understand when additional capacity improves serving performance and energy efficiency. We introduce an HBM-HBF-host hierarchical storage system and buffered cache-aware scheduling, and use trace-driven simulations to analyze their effects on performance, energy consumption, and HBF write lifetime. Across the evaluated workloads, the fastest HBF-augmented systems reduce completion time by 36.1-87.0% relative to HBM-only systems. Modeled energy savings reach 55.8%, although HBF increases energy consumption on some light workloads. Buffered cache-aware scheduling extends estimated HBF write lifetime from 4.77 to 14.82 years in the evaluated configuration. These results demonstrate the importance of coordinating data placement and scheduling to improve serving efficiency while sustaining a practical HBF write lifetime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zack Yu, Chloe Wong, Coleman Hooper, Minjae Lee, Wonjun Kang, Youngjin Cho, Michael W. Mahoney, Yakun Sophia Shao, Kurt Keutzer, Amir Gholami
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
