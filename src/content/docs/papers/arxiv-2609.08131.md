---
title: "Jacap: Robust KV Cache Eviction via Jacobian-Based Nonlinear Information Capacity Preservation"
description: "Key-value (KV) cache eviction is essential for scaling long-context inference in Large Language Models."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.08131) · [PDF](https://arxiv.org/pdf/2609.08131)

## 一句话摘要

Key-value (KV) cache eviction is essential for scaling long-context inference in Large Language Models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Key-value (KV) cache eviction is essential for scaling long-context inference in Large Language Models. However, existing policies predominantly rely on empirical heuristics, lacking a rigorous characterization of token utility under the inherently nonlinear softmax attention mechanism. In this work, we rethink KV cache eviction through the lens of local information geometry, modeling the attention process as a nonlinear Gaussian communication channel. By performing a first-order Taylor expansion of the attention mapping, we derive the Jacobian Information Capacity, a novel objective that explicitly captures query relevance, softmax sensitivity, and structural diversity. Guided by this theory, we introduce Jacap, a capacity-aware eviction method that utilizes softmax-aware importance weighting and statistical leverage scores for subset selection. Extensive experiments across diverse architectures and benchmarks demonstrate that \textsc{Jacap} delivers superior performance in most scenarios, particularly in high-compression regimes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaming Yang, Chenwei Tang, Liangli Zhen, Chenyang Zhang, Jiancheng Lv
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
