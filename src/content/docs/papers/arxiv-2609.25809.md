---
title: "You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs"
description: "Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.25809) · [PDF](https://arxiv.org/pdf/2609.25809)

## 一句话摘要

Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coarser architectures and likelihood-scored multiple-choice benchmarks, leaving three central questions open in the fine-grained regime: how redundant per-token expert selection is, how effectively existing pruning methods exploit that redundancy, and what governs a model's sensitivity to pruning. We fill this gap with a systematic empirical study of twelve fine-grained MoE checkpoints spanning nine architecture families, with a core suite of eleven benchmarks covering knowledge QA, mathematics, code generation, and general reasoning. We find that expert selection is far more redundant than the field's operating points assume: uniformly retaining about two thirds of the selected experts preserves 98.8% of unpruned performance on average, requiring only a one-integer change and delivering 1.2-1.7x measured speedup across two serving backends. This simple baseline leaves little room for dynamic allocation at conservative budgets: even the best published rules differ from it by under 1% at matched expert budgets. Their value emerges under aggressive pruning, where the best rules recover up to 3.0% over uniform truncation, with gains concentrated in the generative tasks that suffer the sharpest degradation. Sensitivity to aggressive pruning also depends on the model: larger and thinking models are more resilient, whereas multimodal models are more vulnerable. Together, these findings reveal how much expert computation fine-grained MoEs can dispense with, and establish when dynamic allocation earns its complexity, informing both practical deployment and future pruning methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuanteng Chen, Qiwei Lai, Chen Tianqi, Peisong Wang, Yuantian Shao, Nanxin Zeng, Zhilei Liu, Chuangyi Li, Jing Liu, Jian Cheng
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
