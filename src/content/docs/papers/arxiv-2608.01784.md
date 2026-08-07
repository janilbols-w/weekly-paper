---
title: "REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models"
description: "Mixture-of-experts (MoE) models increase parameter capacity by activating only a small subset of experts for each token."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2608.01784) · [PDF](https://arxiv.org/pdf/2608.01784)

## 一句话摘要

Mixture-of-experts (MoE) models increase parameter capacity by activating only a small subset of experts for each token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-experts (MoE) models increase parameter capacity by activating only a small subset of experts for each token. This conditional-computation paradigm has enabled autoregressive language models to scale model capacity without a proportional increase in per-token computation. In diffusion language models (DLMs), however, each denoising forward jointly revisits all token positions despite their sharply different refinement demands, while the default fixed token-choice routing assigns them a uniform expert budget, creating a mismatch between expert computation and refinement demand. We argue that MoE inference in DLMs should therefore be viewed as refinement-aware compute allocation across heterogeneous token refinement states. We propose REFLEX (\textbf{RE}finement-aware \textbf{FLEX}ible expert allocation), a training-free method that keeps the default router unchanged while reorganizing expert computation around the evolving refinement process. Specifically, REFLEX introduces a coarse-to-fine hierarchy for expert-budget allocation that aligns computation with block-relative refinement roles while using the Frontier-Progress Score to resolve active-block priorities. Across multiple widely used benchmarks on two representative MoE-based DLMs, LLaDA-MoE and LLaDA2.0-mini, REFLEX reduces allocated expert computation by 15\% on average while preserving or even improving generation quality on most benchmarks relative to default routing. Compared with autoregressive-style variable-expert routing methods, REFLEX also yields a more consistent quality--computation trade-off, further supporting the importance of allocating expert computation according to the heterogeneous refinement demands exposed within each denoising forward.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing, moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiang Xia, Cheng Yan, Yiming Zhang, Jiazheng Liu, Hongyu Zhang, Wuyang Zhang
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
