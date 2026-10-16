---
title: "The Fragility and Dynamics of LLM Pruning-Recovery Steps"
description: "Structural pruning followed by a recovery stage is the standard recipe for compressing large language models (LLMs), yet the two stages are typically designed and tuned in isolation."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.15574v1) · [PDF](https://arxiv.org/pdf/2610.15574v1)

## 一句话摘要

Structural pruning followed by a recovery stage is the standard recipe for compressing large language models (LLMs), yet the two stages are typically designed and tuned in isolation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structural pruning followed by a recovery stage is the standard recipe for compressing large language models (LLMs), yet the two stages are typically designed and tuned in isolation. In this work, we study how their interaction shapes the compressed model, sweeping ordering, the data that drives each stage, and the alignment of their training objectives. We find that instruction-following is the first capability to collapse under pruning, well before knowledge, reasoning, or core language modeling, and that much of the pruning in-domain loss is likely not knowledge loss but a domain-agnostic failure to respond coherently to the prompt. We find in our setting that in-domain data is the strongest pruning signal, whereas instruction-style data recovers the most. Stage order matters little, but only marginally. We further analyze how the importance ranking drifts before and after pruning. Together these results give practitioners a concrete recipe for composing pruning and recovery.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luis Frentzen Salim, Komang Rinartha, Chia-Chun Wu, Tran Van Nhiem, Lun-Wei Ku, Yung-Hui Li
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
