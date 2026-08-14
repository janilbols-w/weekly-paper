---
title: "Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking"
description: "Selecting a final checkpoint for multimodal large language models (MLLMs) is challenging when late-stage candidates are closely matched and downstream evaluation signals are noisy."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2605.18852) · [PDF](https://arxiv.org/pdf/2605.18852)

## 一句话摘要

Selecting a final checkpoint for multimodal large language models (MLLMs) is challenging when late-stage candidates are closely matched and downstream evaluation signals are noisy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Selecting a final checkpoint for multimodal large language models (MLLMs) is challenging when late-stage candidates are closely matched and downstream evaluation signals are noisy. Small observed differences can be comparable to variability introduced by finite evaluation samples, LLM-based judges, and ambiguous multimodal evidence, while validation loss may not identify the checkpoint preferred by downstream evaluation. We formulate late-stage checkpoint selection as a stability-aware decision problem under evaluation uncertainty and propose a progressive framework combining pointwise filtering, listwise ranking, and pairwise refinement. Repeated evaluation-set subsampling is used to characterize ranking stability, while percentile-based aggregation accounts for lower- and upper-tail behavior. Experiments show that multimodal data evaluability is critical: quality-aware curation of OCR-heavy inputs reduces ranking flip rate from 32.5\% to 11.2\% and increases inter-run agreement from 0.61 to 0.84. We further observe divergence between validation-loss progression and downstream checkpoint preference in two independent MLLM settings. An additional public Qwen2.5-VL-7B reproduction across 11 checkpoints shows tightly clustered pointwise scores and frequently tie-dominated final pairwise comparisons, while repeated evaluation most often selects an intermediate rather than the final checkpoint. These results suggest that reliable MLLM checkpoint selection should quantify and reserve evaluation uncertainty rather than force decisions from small differences in a single metric.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qinwu Xu, Zhuoheng Li, Jessie Salas
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
