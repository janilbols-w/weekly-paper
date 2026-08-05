---
title: "Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents"
description: "The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.01285) · [PDF](https://arxiv.org/pdf/2608.01285)

## 一句话摘要

The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions.

## 为什么值得关注

待编辑增强。

## 摘要原文

The continued development of LLMs toward persistent and adaptive intelligence increasingly requires long-term memory mechanisms that preserve and reuse information across interactions. Existing memory systems either compress and structure histories for efficient access or perform deep research over broader trajectories. The former lowers online cost but may omit temporal, causal, or cross-step dependencies, while the latter improves evidence coverage at substantial latency and inference cost. This raises a key question: can a memory system achieve strong answer quality while maintaining low online latency? We introduce Router-Mem, an evidence-conditioned progressive execution framework for long-horizon agent memory. Router-Mem first applies a shared low-cost retrieval prefix to obtain evidence. A lightweight sufficiency router then predicts whether the context supports early termination, which enable a single-token decision at inference time. It is trained with evidence-level supervision and rationale-conditioned representation distillation. When evidence is insufficient, Router-Mem reuses retrieval hits to expand memory blocks and perform deeper analysis and aggregation. Experiments on AMA-Bench and BEAM show that Router-Mem achieves 55.17\% and 38.77\% score while reducing average inference time by 27.3\% and 25.5\% compared with full memory execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yidan Lin, Kaixiang Wang, Jiong Lou, Jie Li
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
