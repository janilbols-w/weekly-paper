---
title: "ABLE: Representing and Mapping LLMs via Attribution-Based Large-model Embedding"
description: "The explosive growth of large language models (LLMs) has created a heterogeneous and poorly documented ecosystem, making systematic model comparison increasingly important for provenance auditing, security analysis, and model selection."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2606.07524) · [PDF](https://arxiv.org/pdf/2606.07524)

## 一句话摘要

The explosive growth of large language models (LLMs) has created a heterogeneous and poorly documented ecosystem, making systematic model comparison increasingly important for provenance auditing, security analysis, and model selection.

## 为什么值得关注

待编辑增强。

## 摘要原文

The explosive growth of large language models (LLMs) has created a heterogeneous and poorly documented ecosystem, making systematic model comparison increasingly important for provenance auditing, security analysis, and model selection. Existing representation methods struggle to address this setting efficiently. Approaches analyzing internal parameters are powerful when architectures are compatible, but face scalability barriers under structural heterogeneity, while methods relying on external outputs may conflate models with similar behaviors and are difficult to align in richer output spaces across different tokenizers. To bridge this gap, we propose ABLE (Attribution-Based Large-model Embedding), a framework that leverages the interpretability space to construct model representations. By aggregating gradient-based feature attributions via a tokenizer-agnostic word-level alignment, ABLE captures model-specific input-sensitivity patterns rather than only surface-level outputs. Beyond empirical utility, we provide a stability analysis showing that, under standard regularity assumptions for differentiable Transformer-style models, ABLE induces a Lipschitz-continuous parameter-to-embedding map with finite-sample convergence guarantees. Extensive experiments on 239 open-source LLMs demonstrate that our training-free approach achieves competitive or superior performance in relation prediction, model routing, and benchmark score prediction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zirui Wang, Yusen Hou, Shaofeng Liang, Bowen Tian, Yanlin Zhang, Wenshuo Chen, Yutao Yue
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
