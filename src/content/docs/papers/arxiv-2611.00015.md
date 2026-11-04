---
title: "Output-Aware Block Influence: Jacobian-Lens Weighting for Depth Pruning"
description: "Depth pruning removes entire transformer blocks and therefore depends on a reliable criterion for identifying which blocks can be removed."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.00015) · [PDF](https://arxiv.org/pdf/2611.00015)

## 一句话摘要

Depth pruning removes entire transformer blocks and therefore depends on a reliable criterion for identifying which blocks can be removed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Depth pruning removes entire transformer blocks and therefore depends on a reliable criterion for identifying which blocks can be removed. Block Influence (BI) ranks blocks by how minimally they rotate the hidden state. However, local redundancy does not necessarily imply downstream irrelevance. We address this limitation using the Jacobian Lens (J-Lens) neural artifact, a map transporting perturbations at a layer to the final residual stream. At a common sparsity level, pruning scores applying J-Lens transportation to $BI$, what we call $J-BI$, were found to improve post-pruning accuracy by up to 19 points over $BI$ while reducing damage to perplexity for Qwen3-8B, Llama-3.1-8B-IT, and Gemma-3-12B-IT. We also perform a single-block ablation study and use J-Lens probing to explain why the proposed scores improved performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kyle Lemoi, Jonathan Yong, Shubhankar Tripathy, Priestley Fernandes, Anirban Majumder, Zarreen Reza
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
