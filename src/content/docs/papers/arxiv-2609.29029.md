---
title: "Exploiting answer-invariant redundancies in satellite imagery for efficient VLM inference on edge"
description: "Onboard vision-language models could enable satellites to answer queries directly, but exhaustive tiled inference over high-resolution imagery is slow and energy-intensive."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.29029) · [PDF](https://arxiv.org/pdf/2609.29029)

## 一句话摘要

Onboard vision-language models could enable satellites to answer queries directly, but exhaustive tiled inference over high-resolution imagery is slow and energy-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Onboard vision-language models could enable satellites to answer queries directly, but exhaustive tiled inference over high-resolution imagery is slow and energy-intensive. We identify answer-invariant token redundancy (AITR): image tiles and vision tokens that can be removed without changing the final answer. We present Rift, a two-stage system that performs query-conditioned tile pruning followed by elastic prefill to reduce token budget. We evaluate it on LLaVA-1.5 7B running on Jetson AGX Orin. Compared with exhaustive tiled inference, Rift reduces energy by 78% and latency by 69%, while increasing accuracy from 45% to 73%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ishani Janveja, Davis Zhang, Seoyul Oh, Deepak Vasisht
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
